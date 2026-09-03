"""Build the semantic layer's vectors — the only writer of data/embeddings/.

Runs inside the venv, which is the one interpreter here with numpy and
model2vec; install_semantic.sh is the normal caller and the command is

    tools/.venv-semantic/bin/python tools/build_embeddings.py [--chunks] [--if-stale]

Nothing in the repository runs this on its own: not build_index.py, not
atu.db_stale(), not a query. That is rule 1 of tools/semantic.py, and the
stamp written here is what lets rule 2 (silent fallback when stale) work.

What a talk is embedded from (semantic.LAYER_VERSION 1)
------------------------------------------------------
One text per talk, these lines joined by newlines, empty ones dropped:

    title
    speakers, comma separated
    conference name · edition (when it differs) · category
    tags, comma separated
    description, whole
    the first OPENING_WORDS words of the transcript, when there is one

The model is a static embedder — a text's vector is the mean of its tokens'
vectors — so composition is a question of *mass*, not of position: every
word pulls the vector equally, and a long transcript slice would drown the
title under a thousand "so", "um" and "next slide". The opening is the slice
worth having: README's excerpt section says why (the thesis is nearly always
there), and OPENING_WORDS is about a minute of speech, comparable to the
description's median 150 words rather than dominating them. Talks without a
transcript embed their metadata alone, which is the same thing minus the
opening — 65% of the corpus — so a query that lands on a transcript's
vocabulary does not push transcript-less talks out on principle.

Chunks (--chunks)
-----------------
A window is WINDOW_WORDS consecutive transcript words starting every
WINDOW_STRIDE words, the words timed as build_index.timed_words() times them.
Both are multiples of build_index.PASSAGE_STRIDE, so every window begins on
a boundary of the passage grid talks.db is searched on, and a window's start
handed to `excerpt.py --at` opens the same speech the FTS5 layer would have
quoted. 192 words is ~70 s at the corpus's 2.7 words/s — long enough that a
mean of its tokens says what the minute is about, short enough that a query
about one point in a talk still lands on it. A 50% stride means a point that
straddles one window's edge sits in the middle of the next; search_chunks'
per_talk cap keeps those twins from filling a result list. Transcripts
build_index.held_back() rejects (a 30-second caption stub on an hour-long
talk) are skipped here for the same reason they are skipped there.

Determinism
-----------
The output is a function of talks.json, the transcripts and the model: no
timestamps, no random state, batching that does not touch the arithmetic.
Rebuilding from the same inputs gives byte-identical files, which is the
repository's rule for every derived artefact and what makes `--if-stale`
safe to run on every install. The stamp is taken before the corpus is read
and checked again after; a corpus that changed under the build is an error,
not a stamp that lies.

Files are written vectors first and talks.ids.json last, each through a
temporary name and os.replace, so semantic.why_unavailable() sees either the
previous complete layer or the new one — never a manifest for vectors that
do not exist yet.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import atu  # noqa: E402
import build_index  # noqa: E402
import semantic  # noqa: E402

# How much of a transcript joins the talk-level text. See the module docstring.
OPENING_WORDS = 250

# Chunk geometry, in words, both multiples of build_index.PASSAGE_STRIDE.
WINDOW_WORDS = 16 * build_index.PASSAGE_STRIDE    # 192
WINDOW_STRIDE = 8 * build_index.PASSAGE_STRIDE    # 96

# Texts per model.encode() call. Purely a memory bound — the vector of a text
# does not depend on what else is in its batch.
BATCH = 4096

# What a local model folder must hold for StaticModel.from_pretrained(); the
# rest of the Hub repo (an onnx export as large as the model itself, a README)
# is never read, so fetch_model() does not fetch it.
MODEL_FILES = ("config.json", "model.safetensors", "tokenizer.json")


# --- the model --------------------------------------------------------------------

def fetch_model() -> tuple[pathlib.Path, int]:
    """The model's snapshot directory, downloading the files it needs if absent.

    Downloads land in semantic.MODEL_CACHE in huggingface_hub's own layout, so
    semantic.model_snapshot() finds them from any interpreter afterwards.
    Returns the directory and how many bytes were fetched (0 when cached).
    """
    os.environ["HF_HOME"] = str(semantic.MODEL_CACHE)
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    local = semantic.model_snapshot()
    if local and all((local / f).exists() for f in MODEL_FILES):
        return local, 0
    import huggingface_hub

    fetched = 0
    for name in MODEL_FILES:
        try:
            path = pathlib.Path(huggingface_hub.hf_hub_download(semantic.MODEL_NAME, name))
        except Exception as e:  # noqa: BLE001 — whatever the Hub client raises
            raise SystemExit(
                f"could not download {name} of {semantic.MODEL_NAME} from the Hugging Face "
                f"Hub into {semantic.MODEL_CACHE}: {type(e).__name__}: {e}\n"
                "The model is fetched once (~30 MB) and needs the network for that; "
                "nothing else in the install does. If curl reaches huggingface.co but this "
                "does not, a proxy's CA is in the system store and not in certifi's: "
                "export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt") from None
        fetched += path.stat().st_size
    local = semantic.model_snapshot()
    if not local:
        raise SystemExit(f"downloaded {semantic.MODEL_NAME} but no snapshot appeared under "
                         f"{semantic.MODEL_CACHE}")
    return local, fetched


# --- texts ------------------------------------------------------------------------

def talk_text(t: dict, segs: list[dict] | None) -> str:
    """The one text a talk is embedded from; the docstring documents the shape."""
    venue = [t.get("conference_name") or t.get("conference") or ""]
    if t.get("edition") and t["edition"] != venue[0]:
        venue.append(t["edition"])
    if t.get("category"):
        venue.append(t["category"])
    lines = [
        t.get("title") or "",
        ", ".join(t.get("speakers") or []),
        " · ".join(v for v in venue if v),
        ", ".join(t.get("tags") or []),
        t.get("description") or "",
    ]
    if segs:
        words = []
        for s in segs:
            words.extend(s["text"].split())
            if len(words) >= OPENING_WORDS:
                break
        lines.append(" ".join(words[:OPENING_WORDS]))
    return "\n".join(" ".join(l.split()) for l in lines if l and l.strip())


def chunk_windows(segs: list[dict]) -> list[tuple[float, float, str]]:
    """(start s, end s, text) for every window of a transcript; see the docstring.

    The tail rule is to_passages()'s: a window starts at every stride while
    at least a stride of words remains, so the last one may be short but
    never shorter than WINDOW_STRIDE — unless the whole transcript is.
    """
    words = build_index.timed_words(segs)
    if not words:
        return []
    last = segs[-1]
    end_of_talk = float(last["start"]) + float(last.get("duration") or 0)
    out = []
    pos = 0
    while pos < len(words) and (pos == 0 or len(words) - pos >= WINDOW_STRIDE):
        chunk = words[pos:pos + WINDOW_WORDS]
        nxt = pos + WINDOW_WORDS
        end = words[nxt][0] if nxt < len(words) else end_of_talk
        out.append((float(chunk[0][0]), max(float(end), float(chunk[0][0])),
                    " ".join(w for _, w in chunk)))
        pos += WINDOW_STRIDE
    return out


def transcript_segments(t: dict) -> list[dict] | None:
    """The talk's transcript segments, or None when absent or held back."""
    tr = atu.load_transcript(t["id"])
    if not tr:
        return None
    if build_index.held_back(tr.get("word_count", 0), t.get("duration_min")):
        return None
    return tr.get("segments") or None


# --- the build ------------------------------------------------------------------------

def embed_batches(texts: list[str]):
    """semantic.embed() over BATCH-sized slices, as one float16 matrix."""
    import numpy as np

    parts = [semantic.embed(texts[i:i + BATCH]).astype(np.float16)
             for i in range(0, len(texts), BATCH)]
    if not parts:
        return np.zeros((0, semantic._model().dim), dtype=np.float16)
    return np.concatenate(parts)


def save_npy(path: pathlib.Path, arr) -> int:
    """np.save through a temporary name; returns the size in bytes."""
    import numpy as np

    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("wb") as f:
        np.save(f, arr)
    os.replace(tmp, path)
    return path.stat().st_size


def save_json(path: pathlib.Path, obj) -> int:
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        f.write("\n")
    os.replace(tmp, path)
    return path.stat().st_size


def up_to_date(want_chunks: bool) -> str | None:
    """Why nothing needs building, or None when something does."""
    why = semantic.why_unavailable()
    if why:
        return None
    if want_chunks and not semantic.has_chunks():
        return None
    m = semantic._manifest()
    return (f"embeddings are current: {len(m['ids']):,} talks"
            + (f", {m['chunks']:,} chunks" if m.get("chunks") else "")
            + f" from talks.json {m['stamp'].get('talks_json_generated_at')}")


def build(want_chunks: bool) -> int:
    t0 = time.time()
    stamp = semantic.corpus_stamp()
    snapshot, fetched = fetch_model()
    t_fetch = time.time() - t0
    semantic._model()
    t_model = time.time() - t0 - t_fetch
    print(f"model    {semantic.MODEL_NAME}  snapshot {snapshot.name[:12]}  "
          + (f"downloaded {fetched / 2**20:.1f} MiB in {t_fetch:.1f} s, " if fetched else "cached, ")
          + f"loaded in {t_model:.2f} s")

    talks = atu.load_talks()
    ids = [t["id"] for t in talks]
    if len(set(ids)) != len(ids):
        raise SystemExit("talks.json has duplicate ids; the vectors would not map to talks")

    # Talk level. Transcripts are read once and kept only for talks that have
    # one; at 3k transcripts that is the corpus text in memory, ~100 MB.
    t1 = time.time()
    texts, segs_of = [], {}
    for i, t in enumerate(talks):
        segs = transcript_segments(t)
        if segs:
            segs_of[i] = segs
        texts.append(talk_text(t, segs))
    V = embed_batches(texts)
    del texts
    size_v = save_npy(semantic.TALK_VECTORS, V)
    print(f"talks    {len(ids):,} vectors ({len(segs_of):,} with a transcript opening)  "
          f"{time.time() - t1:.1f} s  {semantic.TALK_VECTORS.name} {size_v / 2**20:.1f} MiB")

    # Chunk level.
    n_chunks = None
    if want_chunks:
        import numpy as np

        t2 = time.time()
        spans, buf, parts = [], [], []
        for row in sorted(segs_of):
            for start, end, text in chunk_windows(segs_of[row]):
                spans.append((row, start, end))
                buf.append(text)
                if len(buf) >= BATCH:
                    parts.append(embed_batches(buf))
                    buf = []
        if buf:
            parts.append(embed_batches(buf))
        C = (np.concatenate(parts) if parts
             else np.zeros((0, semantic._model().dim), dtype=np.float16))
        S = np.asarray(spans, dtype=np.float32).reshape(-1, 3)
        size_c = save_npy(semantic.CHUNK_VECTORS, C)
        size_s = save_npy(semantic.CHUNK_SPANS, S)
        n_chunks = int(C.shape[0])
        print(f"chunks   {n_chunks:,} windows of {WINDOW_WORDS} words, stride {WINDOW_STRIDE}, "
              f"over {len(segs_of):,} transcripts  {time.time() - t2:.1f} s  "
              f"{semantic.CHUNK_VECTORS.name} {size_c / 2**20:.1f} MiB + "
              f"{semantic.CHUNK_SPANS.name} {size_s / 2**20:.1f} MiB")
    else:
        for p in (semantic.CHUNK_VECTORS, semantic.CHUNK_SPANS):
            if p.exists():
                p.unlink()
                print(f"chunks   removed stale {p.name} (built without --chunks)")

    if semantic.corpus_stamp() != stamp:
        raise SystemExit("talks.json or the transcripts changed during the build; "
                         "run it again")
    save_json(semantic.TALK_IDS, {"ids": ids, "stamp": stamp, "chunks": n_chunks})
    print(f"stamp    {json.dumps(stamp, sort_keys=True)}")
    print(f"done     {time.time() - t0:.1f} s total  →  {semantic.EMBEDDINGS}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="build data/embeddings/ for tools/semantic.py")
    ap.add_argument("--chunks", action="store_true",
                    help="also embed transcript windows (chunks.f16.npy, chunks.spans.f32.npy)")
    ap.add_argument("--if-stale", action="store_true",
                    help="do nothing when the layer already matches the corpus")
    args = ap.parse_args(argv)
    if not semantic._libs_here():
        raise SystemExit("numpy and model2vec are needed here; run this with "
                         f"{semantic.VENV_PYTHON} (or {semantic.INSTALL_HINT})")
    if args.if_stale:
        # The model first: a missing model is a reason for why_unavailable(),
        # and without it current vectors would look stale and be rebuilt —
        # or, worse, pass --status and pull the whole Hub repo on the first
        # query. Fetching (or confirming) it is a glob when it is there.
        snapshot, fetched = fetch_model()
        if fetched:
            print(f"model    {semantic.MODEL_NAME}  downloaded {fetched / 2**20:.1f} MiB")
        ok = up_to_date(args.chunks)
        if ok:
            print(ok + f"; model cached ({snapshot.name[:12]})")
            return 0
    return build(args.chunks)


if __name__ == "__main__":
    sys.exit(main())
