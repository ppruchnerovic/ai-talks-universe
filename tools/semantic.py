#!/usr/bin/env python3
"""The optional semantic layer: static embeddings over the talks, for query.py.

Nothing in the repository requires this. FTS5 in talks.db answers every query
on the standard library; what it cannot do is find a talk that means the
question without saying it — "keeping agents from going off the rails" shares
no stem with "guardrails" or "reliability". This module adds that, and only
that, on three rules:

  1. Opt-in. The vectors are built by tools/install_semantic.sh and by nothing
     else — never by atu.db_stale()'s auto-rebuild, never on first query.
  2. Silent fallback. available() is False when the vectors are missing, were
     built from an older talks.json, or the libraries are not installed; the
     caller then searches FTS5 alone and can print why_unavailable() on stderr.
  3. Union, not rerank. fuse_rrf() merges the lexical and the semantic ranking
     by reciprocal rank so each side can contribute talks the other missed; the
     failure mode being fixed is recall, and a reranker cannot add a talk.

The model is minishlab/potion-base-8M: model2vec static embeddings, 256
dimensions, ~30 MB of safetensors, needing numpy + tokenizers and no torch.
A text's vector is a weighted mean of its tokens' vectors, which is why it
loads in 0.1 s and embeds the whole corpus in seconds, and also why it is
"moderate" rather than "high" on the quality ladder: it knows that
"guardrails" and "safety" live near each other, not that "off the rails" is
an idiom.

The interpreter problem
-----------------------
query.py runs on the system python3, which has no numpy. The libraries live
in tools/.venv-semantic (created by install_semantic.sh). Every function here
that needs them goes through _call(): if numpy and model2vec import in the
current interpreter the work runs in-process; otherwise the same work is run
as a subprocess of the venv's python — `semantic.py --serve` reads one JSON
request on stdin and prints one JSON reply — and the parent, which needs
nothing but json, returns the parsed reply. One code path (_do) serves both,
so the subprocess cannot drift from the in-process answer. The subprocess
costs about 0.6 s wall (measured: median 0.60 s over five talk queries, 0.70 s
for chunks), 0.5 s of it the model load; the dot product over 9k talk
vectors is under a millisecond and over 177k chunk rows about 0.1 s.

Files (data/embeddings/, gitignored — derived like talks.db)
------------------------------------------------------------
  talks.f16.npy          (N, 256) float16, each row L2-normalised, row i is
                         talks.json[i] — the same order build_index.py numbers
                         talks, so talk n == row n - 1 for a fresh build.
  talks.ids.json         {"ids": [...N video ids...], "stamp": {...}, "chunks": M|null}
                         Readable with the standard library, which is what
                         lets the staleness check run without numpy.
  chunks.f16.npy         (M, 256) float16, one row per transcript window,
                         only after install_semantic.sh --chunks.
  chunks.spans.f32.npy   (M, 3) float32: [talk row, start s, end s] per window.

Staleness
---------
The stamp records what talks.json the vectors came from (its generated_at and
byte size — sync_catalog.py advances generated_at only when the corpus
changes), how many transcripts existed, atu.DB_SCHEMA_VERSION, the model name
and LAYER_VERSION. Any mismatch makes available() False with a reason, so a
stale layer steps aside instead of returning row numbers that no longer mean
the same talks. It is never rebuilt automatically.
"""

from __future__ import annotations

import functools
import glob
import json
import os
import pathlib
import re
import subprocess
import sys

import atu

MODEL_NAME = "minishlab/potion-base-8M"

# Bumped when the text a talk is embedded from, or the chunk windows, change
# shape in build_embeddings.py — an older file would still load and would
# still be wrong, exactly the failure atu.DB_SCHEMA_VERSION exists for.
LAYER_VERSION = 1

VENV = atu.ROOT / "tools" / ".venv-semantic"
VENV_PYTHON = VENV / "bin" / "python"

# Hugging Face's cache, kept inside the venv directory rather than in
# ~/.cache/huggingface: everything install_semantic.sh creates then lives in
# one gitignored place and `rm -rf tools/.venv-semantic` removes all of it.
# HF_HOME is set from here, unconditionally, before model2vec is imported, so
# an interpreter that already has the libraries uses the same cache and a
# user's own HF_HOME cannot point the query path at a cache with no model in
# it.
MODEL_CACHE = VENV / "hf-cache"

EMBEDDINGS = atu.DATA / "embeddings"
TALK_VECTORS = EMBEDDINGS / "talks.f16.npy"
TALK_IDS = EMBEDDINGS / "talks.ids.json"
CHUNK_VECTORS = EMBEDDINGS / "chunks.f16.npy"
CHUNK_SPANS = EMBEDDINGS / "chunks.spans.f32.npy"

INSTALL_HINT = "run tools/install_semantic.sh"

# Reciprocal rank fusion's smoothing constant. 60 is the value from the
# original paper (Cormack, Clarke, Buettcher 2009) and the one every search
# engine ships; it makes rank 1 worth 1/61 and rank 10 worth 1/70, so a talk
# on both lists at middling ranks beats a talk that leads one list and is
# absent from the other. That is the behaviour wanted here: a talk FTS5 ranks
# 3rd and the vectors rank 8th is a safer answer than one only the vectors
# like.
RRF_K = 60


# --- what is on disk ---------------------------------------------------------

def corpus_stamp() -> dict:
    """What the vectors must have been built from, cheap enough for every query.

    talks.json is 20 MB, so it is not parsed: generated_at sits in its first
    line and is read with a regex over the first 4 KB, and the byte size
    backs it up. The transcript count is one listdir. atu.DB_SCHEMA_VERSION is
    included because a bump usually means the passage shape moved, and the
    chunk windows are aligned to it.
    """
    generated_at = None
    size = 0
    if atu.TALKS_JSON.exists():
        size = atu.TALKS_JSON.stat().st_size
        with atu.TALKS_JSON.open("rb") as f:
            m = re.search(rb'"generated_at":\s*"([^"]*)"', f.read(4096))
        generated_at = m.group(1).decode() if m else None
    n_tr = len(list(atu.TRANSCRIPTS.glob("*.json"))) if atu.TRANSCRIPTS.exists() else 0
    return {
        "model": MODEL_NAME,
        "layer_version": LAYER_VERSION,
        "db_schema_version": atu.DB_SCHEMA_VERSION,
        "talks_json_generated_at": generated_at,
        "talks_json_bytes": size,
        "transcripts": n_tr,
    }


def stale_reason(built: dict | None, current: dict) -> str | None:
    """Why a stamp read from talks.ids.json no longer describes the corpus.

    A pure comparison, so the test file can exercise every branch without a
    corpus. Each reason ends in the one thing to do about it.
    """
    if not built:
        return f"no embeddings yet; {INSTALL_HINT}"
    if built.get("model") != current["model"]:
        return (f"embeddings were built with {built.get('model')!r}, tools expect "
                f"{current['model']!r}; {INSTALL_HINT} --force")
    if built.get("layer_version") != current["layer_version"]:
        return (f"embeddings are layer v{built.get('layer_version')}, tools expect "
                f"v{current['layer_version']}; {INSTALL_HINT} --force")
    if built.get("db_schema_version") != current["db_schema_version"]:
        return (f"embeddings predate index schema v{current['db_schema_version']}; "
                f"{INSTALL_HINT} --force")
    if (built.get("talks_json_generated_at") != current["talks_json_generated_at"]
            or built.get("talks_json_bytes") != current["talks_json_bytes"]):
        return f"embeddings are older than talks.json; {INSTALL_HINT}"
    if built.get("transcripts") != current["transcripts"]:
        return (f"embeddings were built over {built.get('transcripts')} transcripts, "
                f"there are now {current['transcripts']}; {INSTALL_HINT}")
    return None


def npy_shape(path: pathlib.Path) -> tuple[int, ...] | None:
    """The shape in a .npy header, read with the standard library.

    The format is a magic string, a version, a little-endian header length
    and an ASCII dict literal — so the row count can be checked against
    talks.ids.json by an interpreter that has no numpy, and a build that died
    between writing the vectors and the ids is caught rather than indexed.
    """
    try:
        with path.open("rb") as f:
            magic = f.read(6)
            if magic != b"\x93NUMPY":
                return None
            major = f.read(1)[0]
            f.read(1)
            hlen = int.from_bytes(f.read(2 if major == 1 else 4), "little")
            header = f.read(hlen).decode("latin1")
    except OSError:
        return None
    m = re.search(r"'shape':\s*\(([^)]*)\)", header)
    if not m:
        return None
    parts = [p.strip() for p in m.group(1).split(",") if p.strip()]
    return tuple(int(p) for p in parts)


@functools.lru_cache(maxsize=1)
def _manifest() -> dict | None:
    """talks.ids.json parsed once per process, or None when absent/unreadable."""
    try:
        with TALK_IDS.open(encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _libs_here() -> bool:
    try:
        import numpy  # noqa: F401
        import model2vec  # noqa: F401
    except ImportError:
        return False
    return True


def _venv_ready() -> bool:
    """The venv exists and has model2vec in it — a glob, not a subprocess."""
    return VENV_PYTHON.exists() and bool(glob.glob(str(VENV / "lib" / "python3*" /
                                                       "site-packages" / "model2vec")))


def why_unavailable() -> str | None:
    """One line for stderr when the layer cannot be used, or None when it can."""
    manifest = _manifest()
    why = stale_reason(manifest.get("stamp") if manifest else None, corpus_stamp())
    if why:
        return why
    shape = npy_shape(TALK_VECTORS)
    if shape is None:
        return f"{TALK_VECTORS.name} is missing; {INSTALL_HINT}"
    if shape[0] != len(manifest["ids"]):
        return (f"{TALK_VECTORS.name} has {shape[0]} rows for {len(manifest['ids'])} ids "
                f"— a build died half-way; {INSTALL_HINT} --force")
    if not (_libs_here() or _venv_ready()):
        return f"numpy/model2vec are not installed; {INSTALL_HINT}"
    if model_snapshot() is None:
        return f"{MODEL_NAME} is not downloaded; {INSTALL_HINT}"
    return None


def available() -> bool:
    """Vectors present, built from the current corpus, and a way to run them."""
    return why_unavailable() is None


def has_chunks() -> bool:
    """Whether passage-level vectors exist for the current corpus."""
    if not available():
        return False
    m = _manifest()
    if not m.get("chunks"):
        return False
    shape = npy_shape(CHUNK_VECTORS)
    return bool(shape) and shape[0] == m["chunks"] and CHUNK_SPANS.exists()


# --- pools ----------------------------------------------------------------------

def pool_to_rows(pool, ids: list[str]) -> list[int] | None:
    """The row numbers a caller's pool selects, or None for "everything".

    query.py keys its pool by talks.db's dense `n`, which build_index.py
    assigns from the position in talks.json — the same order the vectors are
    written in, so n is row n - 1. A video id is accepted too, and the two may
    be mixed. Anything unknown is ignored rather than raised: a pool from an
    index built a minute later than the vectors would otherwise be an error
    on the query path, when the staleness stamp is what should say so.
    """
    if pool is None:
        return None
    index_of = None
    rows = set()
    for key in pool:
        if isinstance(key, bool):
            continue
        if isinstance(key, int):
            if 1 <= key <= len(ids):
                rows.add(key - 1)
        elif isinstance(key, str):
            if index_of is None:
                index_of = {vid: i for i, vid in enumerate(ids)}
            i = index_of.get(key)
            if i is not None:
                rows.add(i)
    return sorted(rows)


# --- the work: runs in whichever interpreter has numpy ----------------------------

_MODEL = None


def _model():
    """The loaded StaticModel, once per process.

    Loaded from the snapshot directory in MODEL_CACHE when it is there, which
    is an offline, 0.1 s operation; otherwise from the Hub by name, which
    downloads into MODEL_CACHE on the first call.
    """
    global _MODEL
    if _MODEL is None:
        os.environ["HF_HOME"] = str(MODEL_CACHE)
        os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        from model2vec import StaticModel

        local = model_snapshot()
        _MODEL = StaticModel.from_pretrained(str(local) if local else MODEL_NAME)
    return _MODEL


def model_snapshot() -> pathlib.Path | None:
    """The downloaded model's directory inside MODEL_CACHE, if any."""
    repo = "models--" + MODEL_NAME.replace("/", "--")
    hits = sorted(glob.glob(str(MODEL_CACHE / "hub" / repo / "snapshots" / "*" / "model.safetensors")))
    return pathlib.Path(hits[-1]).parent if hits else None


def embed(texts: list[str]):
    """L2-normalised float32 vectors, one row per text. Needs numpy + model2vec.

    Shared by build_embeddings.py and the query path, so a query is embedded
    exactly as the corpus was. An empty text embeds to the zero vector, which
    scores 0 against everything rather than dividing by zero.
    """
    import numpy as np

    texts = [t if isinstance(t, str) else "" for t in texts]
    if not texts:
        return np.zeros((0, _model().dim), dtype=np.float32)
    v = _model().encode(texts, show_progress_bar=False, use_multiprocessing=False,
                        max_length=None).astype(np.float32)
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    return v / np.where(norms == 0, 1.0, norms)


@functools.lru_cache(maxsize=1)
def _talk_matrix():
    import numpy as np

    return np.load(TALK_VECTORS).astype(np.float32)


@functools.lru_cache(maxsize=1)
def _chunk_arrays():
    import numpy as np

    return np.load(CHUNK_VECTORS, mmap_mode="r"), np.load(CHUNK_SPANS)


def _top(scores, k: int):
    """Indices of the k largest scores, highest first, ties by lower index."""
    import numpy as np

    k = max(0, min(k, scores.shape[0]))
    if k == 0:
        return np.zeros(0, dtype=np.int64)
    # argpartition first: the sort is over k rows rather than all of them.
    part = np.argpartition(-scores, k - 1)[:k]
    order = np.lexsort((part, -scores[part]))
    return part[order]


def _do(op: str, req: dict) -> list:
    """The one implementation behind every public search function."""
    import numpy as np

    ids = _manifest()["ids"]
    if op == "embed":
        return embed([req["query"]])[0].tolist()
    q = embed([req["query"]])[0]
    rows = req.get("rows")
    k = int(req.get("k", 50))

    if op == "talks":
        V = _talk_matrix()
        if rows is not None:
            rows = np.asarray(rows, dtype=np.int64)
            if rows.size == 0:
                return []
            scores = V[rows] @ q
            best = _top(scores, k)
            return [[ids[int(rows[i])], float(scores[i])] for i in best]
        scores = V @ q
        return [[ids[int(i)], float(scores[i])] for i in _top(scores, k)]

    if op == "chunks":
        C, spans = _chunk_arrays()
        talk_of = spans[:, 0].astype(np.int64)
        if rows is not None:
            keep = np.flatnonzero(np.isin(talk_of, np.asarray(rows, dtype=np.int64)))
            if keep.size == 0:
                return []
        else:
            keep = None
        M = np.asarray(C if keep is None else C[keep], dtype=np.float32)
        scores = M @ q
        per_talk = int(req.get("per_talk") or 0)
        want = k if not per_talk else min(scores.shape[0], k * max(per_talk, 4) + 64)
        out, seen = [], {}
        # Overlapping windows mean a talk's best moment usually has a twin one
        # stride away; per_talk caps how many of them one talk may occupy.
        while len(out) < k:
            best = _top(scores, want)
            for i in best:
                j = int(i) if keep is None else int(keep[i])
                t = int(talk_of[j])
                if per_talk and seen.get(t, 0) >= per_talk:
                    continue
                seen[t] = seen.get(t, 0) + 1
                out.append([ids[t], float(spans[j, 1]), float(spans[j, 2]), float(scores[i])])
                if len(out) >= k:
                    break
            if want >= scores.shape[0]:
                break
            want = min(scores.shape[0], want * 4)
        return out

    raise ValueError(f"unknown op {op!r}")


def _call(op: str, req: dict) -> list:
    """Run _do here if the libraries import, else in the venv's interpreter."""
    if _libs_here():
        return _do(op, req)
    if not _venv_ready():
        raise RuntimeError(f"numpy/model2vec are not installed; {INSTALL_HINT}")
    proc = subprocess.run(
        [str(VENV_PYTHON), str(pathlib.Path(__file__).resolve()), "--serve"],
        input=json.dumps({"op": op, **req}), capture_output=True, text=True,
        timeout=120, cwd=str(atu.ROOT),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"semantic layer failed: {proc.stderr.strip()[-500:]}")
    return json.loads(proc.stdout)


# --- the API query.py imports -------------------------------------------------------

def embed_query(text: str) -> list[float]:
    """The query's vector as a plain list — the only shape both interpreters share."""
    return _call("embed", {"query": text})


def search_talks(query: str, k: int = 50, pool=None) -> list[tuple[str, float]]:
    """The k talks whose talk-level vector is nearest the query: (video_id, cosine).

    `pool` restricts the candidates — talks.db `n` integers, video ids, or a
    mix, as pool_to_rows() explains — and is applied *before* the top-k, so
    the caller always gets k answers from inside its filters when k exist.
    Requires available(); check it first, this raises when it is not.
    """
    if not available():
        raise RuntimeError(why_unavailable())
    rows = pool_to_rows(pool, _manifest()["ids"])
    return [(vid, score) for vid, score in _call("talks", {"query": query, "k": k, "rows": rows})]


def search_chunks(query: str, k: int = 50, pool=None, per_talk: int = 1
                  ) -> list[tuple[str, float, float, float]]:
    """The k transcript windows nearest the query: (video_id, start, end, cosine).

    start and end are seconds into the video, on the same passage grid
    talks.db uses (see build_embeddings.chunk_windows), so a hit can be handed
    to `excerpt.py --at START`. `per_talk` caps how many windows one talk may
    take, 1 by default — the overlapping windows would otherwise fill the
    list with one talk's neighbouring moments. Empty when there are no chunk
    vectors; has_chunks() says so beforehand.
    """
    if not has_chunks():
        return []
    rows = pool_to_rows(pool, _manifest()["ids"])
    hits = _call("chunks", {"query": query, "k": k, "rows": rows, "per_talk": per_talk})
    return [(vid, start, end, score) for vid, start, end, score in hits]


def fuse_rrf(lexical, semantic, k: int = RRF_K, w_lexical: float = 1.0,
             w_semantic: float = 1.0) -> list[tuple[str, float]]:
    """Union of two rankings by reciprocal rank fusion, best first.

    Each id scores w / (k + rank) on every list it appears on, ranks from 1,
    and the scores add. A talk present on both lists beats one leading only
    one of them (with k = 60: 1/62 + 1/65 > 1/61), which is the point — the
    two rankers agree on it — while a talk only the vectors found still
    enters below them rather than being dropped, which is the recall the
    layer exists for. Cosines and bm25 values are never compared with each
    other: only positions are, so neither side needs normalising.

    Ties are broken by lexical position, then semantic position, so the
    output is deterministic. Duplicates within one list count once, at their
    first position. The lists may hold any hashable ids; they are returned as
    given.
    """
    scores: dict = {}
    first: dict = {}
    for weight, ranked in ((w_lexical, lexical), (w_semantic, semantic)):
        seen = set()
        for rank, vid in enumerate(ranked, 1):
            if vid in seen:
                continue
            seen.add(vid)
            scores[vid] = scores.get(vid, 0.0) + weight / (k + rank)
            first.setdefault(vid, [None, None])
    for rank, vid in enumerate(lexical, 1):
        if first[vid][0] is None:
            first[vid][0] = rank
    for rank, vid in enumerate(semantic, 1):
        if first[vid][1] is None:
            first[vid][1] = rank
    inf = float("inf")
    order = sorted(scores, key=lambda v: (-scores[v], first[v][0] or inf, first[v][1] or inf))
    return [(vid, scores[vid]) for vid in order]


# --- command line -------------------------------------------------------------------
#
#   python3 semantic.py --status                  what is on disk and why it is (un)usable
#   python3 semantic.py "agents going off the rails"          top talks, through _call()
#   python3 semantic.py --chunks "…" -n 10        top transcript windows
#   python3 semantic.py --embed-query "…"         the vector as JSON
#   … --serve                                     the subprocess protocol (stdin JSON)

def _status() -> int:
    m = _manifest()
    print(f"vectors:   {TALK_VECTORS}  shape={npy_shape(TALK_VECTORS)}")
    print(f"chunks:    {CHUNK_VECTORS}  shape={npy_shape(CHUNK_VECTORS)}  usable={has_chunks()}")
    print(f"stamp:     {json.dumps(m.get('stamp') if m else None)}")
    print(f"corpus:    {json.dumps(corpus_stamp())}")
    print(f"libraries: in-process={_libs_here()}  venv={_venv_ready()}  model={model_snapshot()}")
    why = why_unavailable()
    print(f"available: {why is None}" + (f"  ({why})" if why else ""))
    return 0


def main(argv: list[str]) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="semantic.py", description="poke the semantic layer")
    ap.add_argument("query", nargs="?")
    ap.add_argument("-n", "--limit", type=int, default=10)
    ap.add_argument("--chunks", action="store_true", help="search transcript windows")
    ap.add_argument("--embed-query", metavar="TEXT", help="print TEXT's vector as JSON")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--serve", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if args.serve:
        req = json.load(sys.stdin)
        json.dump(_do(req.pop("op"), req), sys.stdout)
        return 0
    if args.status:
        return _status()
    if args.embed_query is not None:
        json.dump(embed_query(args.embed_query), sys.stdout)
        print()
        return 0
    if not args.query:
        ap.error("a query, --status or --embed-query is required")
    why = why_unavailable()
    if why:
        print(f"semantic layer unavailable: {why}", file=sys.stderr)
        return 2
    if args.chunks:
        hits = search_chunks(args.query, args.limit)
    else:
        hits = search_talks(args.query, args.limit)
    if args.json:
        json.dump(hits, sys.stdout)
        print()
        return 0
    titles = {}
    if not args.json:
        try:
            titles = {t["id"]: t["title"] for t in atu.load_talks()}
        except SystemExit:
            pass
    for h in hits:
        if args.chunks:
            vid, start, end, score = h
            print(f"{score:.3f}  {vid}  {start:7.1f}-{end:<7.1f}  {titles.get(vid, '')}")
        else:
            vid, score = h
            print(f"{score:.3f}  {vid}  {titles.get(vid, '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
