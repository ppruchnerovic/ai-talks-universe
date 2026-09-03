#!/usr/bin/env python3
"""The semantic layer's standard-library half — what query.py runs before numpy.

tools/semantic.py has two halves. One needs numpy and model2vec and runs in
the venv; the other — the staleness stamp, the .npy header reader, the pool
translation, reciprocal rank fusion — runs on the system python3 on every
query, and is what decides whether the layer is used at all. A bug there is
worse than a bug in the vectors: it either uses a stale layer as if it were
current, or throws the layer away when it is fine. This checks that half
against synthetic inputs, with the module's file paths pointed at a temporary
directory so no build is needed and none is touched.

The one end-to-end check at the end runs only when a layer is installed, and
runs through the subprocess path — still no numpy here.

    cd tools && python3 test_semantic.py            # < 1 s; system python3, no numpy
"""

import json
import pathlib
import struct
import sys
import tempfile
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import semantic  # noqa: E402

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


# --- stale_reason: every branch, one thing to do about each --------------------

CUR = {"model": "m", "layer_version": 1, "db_schema_version": 5,
       "talks_json_generated_at": "2026-01-01T00:00:00+00:00", "talks_json_bytes": 10,
       "transcripts": 3}

check("no stamp at all is 'no embeddings yet'",
      "no embeddings yet" in (semantic.stale_reason(None, CUR) or ""))
check("an empty stamp is 'no embeddings yet'",
      "no embeddings yet" in (semantic.stale_reason({}, CUR) or ""))
check("an identical stamp is current", semantic.stale_reason(dict(CUR), CUR) is None)
check("a stamp missing a key is stale", semantic.stale_reason({"model": "m"}, CUR) is not None)

EXPECT = [("model", "built with", True), ("layer_version", "layer v", True),
          ("db_schema_version", "predate index schema", True),
          ("talks_json_generated_at", "older than talks.json", False),
          ("talks_json_bytes", "older than talks.json", False),
          ("transcripts", "transcripts", False)]
for key, phrase, wants_force in EXPECT:
    built = dict(CUR)
    built[key] = "other" if isinstance(CUR[key], str) else CUR[key] + 1
    why = semantic.stale_reason(built, CUR) or ""
    check(f"{key} mismatch is reported with the install hint",
          phrase in why and semantic.INSTALL_HINT in why, why)
    check(f"{key} mismatch {'asks for' if wants_force else 'does not ask for'} --force",
          ("--force" in why) == wants_force, why)

live = semantic.corpus_stamp()
check("corpus_stamp() carries every key stale_reason() compares", set(CUR) <= set(live), sorted(live))
check("corpus_stamp() names the model and layer the tools expect",
      live["model"] == semantic.MODEL_NAME and live["layer_version"] == semantic.LAYER_VERSION)

# --- fuse_rrf: union, ranks not scores, deterministic ---------------------------

K = semantic.RRF_K
out = semantic.fuse_rrf(["x", "y", "z"], ["y", "q", "x"])
got = dict(out)
check("fusion is a union", set(got) == {"x", "y", "z", "q"}, out)
check("each id scores 1/(k+rank) on every list it is on",
      abs(got["x"] - (1 / (K + 1) + 1 / (K + 3))) < 1e-12 and abs(got["q"] - 1 / (K + 2)) < 1e-12)
check("output is best first", all(a[1] >= b[1] for a, b in zip(out, out[1:])), out)

lex = ["L", "B"]
sem = ["s1", "s2", "s3", "s4", "B"]
out = semantic.fuse_rrf(lex, sem)
check("lexical 2nd + semantic 5th beats lexical 1st alone (the docstring's 1/62 + 1/65 > 1/61)",
      out[0][0] == "B" and out[1][0] == "L", out)

out = semantic.fuse_rrf(["a", "b"], ["b", "a"])
check("an exact tie is broken by lexical position", [v for v, _ in out] == ["a", "b"], out)
out = semantic.fuse_rrf(["a"], ["b"])
check("a tie between a lexical-only and a semantic-only id goes to the lexical one",
      [v for v, _ in out] == ["a", "b"], out)
out = semantic.fuse_rrf([], ["p", "q"])
check("a semantic-only ranking comes back in its own order", [v for v, _ in out] == ["p", "q"], out)
check("two empty rankings fuse to nothing", semantic.fuse_rrf([], []) == [])

out = semantic.fuse_rrf(["a", "a", "b"], [])
got = dict(out)
check("a duplicate within one list counts once, at its first position",
      len(out) == 2 and abs(got["a"] - 1 / (K + 1)) < 1e-12, out)

out = semantic.fuse_rrf(["a"], ["b"], w_semantic=3.0)
check("w_semantic scales the semantic side", out[0][0] == "b" and abs(out[0][1] - 3 / (K + 1)) < 1e-12, out)
out = semantic.fuse_rrf(["a"], ["b"], w_lexical=2.0)
check("w_lexical scales the lexical side", out[0][0] == "a" and abs(out[0][1] - 2 / (K + 1)) < 1e-12, out)
out = semantic.fuse_rrf(["a"], [], k=0)
check("k is the smoothing constant: k=0 makes rank 1 worth 1.0", out == [("a", 1.0)], out)
out = semantic.fuse_rrf([1, 2], [2])
check("ids are any hashable, returned as given", [v for v, _ in out] == [2, 1], out)
out = semantic.fuse_rrf(("a", "b"), iter(["b"]))
check("rankings may be tuples or iterators", [v for v, _ in out] == ["b", "a"] or [v for v, _ in out] == ["a", "b"], out)

# --- pool_to_rows: talks.db n (1-based) or video ids, mixed, unknowns dropped -----

IDS = ["v1", "v2", "v3", "v4"]
check("no pool means everything", semantic.pool_to_rows(None, IDS) is None)
check("an empty pool selects nothing", semantic.pool_to_rows([], IDS) == [])
check("n is 1-based: n == row + 1", semantic.pool_to_rows([1, 3], IDS) == [0, 2])
check("out-of-range n is ignored, not raised", semantic.pool_to_rows([0, 5, 99, -1], IDS) == [])
check("video ids map through the manifest order", semantic.pool_to_rows(["v2", "v4", "nope"], IDS) == [1, 3])
check("n and ids mix, deduplicated and sorted", semantic.pool_to_rows([3, "v1", "v3", 1], IDS) == [0, 2])
check("booleans are not row numbers", semantic.pool_to_rows([True, False], IDS) == [])
check("any iterable of keys works", semantic.pool_to_rows({2: "x", 1: "y"}.keys(), IDS) == [0, 1])
check("a set works", semantic.pool_to_rows({"v3"}, IDS) == [2])


# --- npy_shape: the header reader that lets the staleness check skip numpy --------

def fake_npy(path: pathlib.Path, shape: tuple, version: int = 1, descr: str = "<f2") -> None:
    """A .npy file with a real header and no data — enough for npy_shape()."""
    header = f"{{'descr': '{descr}', 'fortran_order': False, 'shape': {shape!r}, }}"
    if len(shape) == 1:
        header = header.replace(f"{shape!r}", f"({shape[0]},)")
    preamble = 6 + 2 + (2 if version == 1 else 4)
    pad = 64 - (preamble + len(header) + 1) % 64
    header = header + " " * pad + "\n"
    with path.open("wb") as f:
        f.write(b"\x93NUMPY" + bytes([version, 0]))
        f.write(struct.pack("<H" if version == 1 else "<I", len(header)))
        f.write(header.encode("latin1"))


with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d)
    fake_npy(d / "a.npy", (12, 256))
    check("npy_shape reads a version 1 header", semantic.npy_shape(d / "a.npy") == (12, 256))
    fake_npy(d / "b.npy", (5,))
    check("npy_shape reads a 1-d shape", semantic.npy_shape(d / "b.npy") == (5,))
    fake_npy(d / "c.npy", (178000, 256), version=2)
    check("npy_shape reads a version 2 header (4-byte length)", semantic.npy_shape(d / "c.npy") == (178000, 256))
    (d / "junk.npy").write_bytes(b"not a numpy file at all")
    check("npy_shape is None for a non-npy file", semantic.npy_shape(d / "junk.npy") is None)
    check("npy_shape is None for a missing file", semantic.npy_shape(d / "absent.npy") is None)


# --- why_unavailable / available / has_chunks against a directory we control ----

def point_at(d: pathlib.Path) -> None:
    semantic.EMBEDDINGS = d
    semantic.TALK_VECTORS = d / "talks.f16.npy"
    semantic.TALK_IDS = d / "talks.ids.json"
    semantic.CHUNK_VECTORS = d / "chunks.f16.npy"
    semantic.CHUNK_SPANS = d / "chunks.spans.f32.npy"
    semantic._manifest.cache_clear()


def manifest(d: pathlib.Path, ids, stamp, chunks=None) -> None:
    (d / "talks.ids.json").write_text(json.dumps({"ids": ids, "stamp": stamp, "chunks": chunks}))
    semantic._manifest.cache_clear()


REAL = {k: getattr(semantic, k) for k in ("EMBEDDINGS", "TALK_VECTORS", "TALK_IDS",
                                          "CHUNK_VECTORS", "CHUNK_SPANS")}
try:
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        point_at(d)
        why = semantic.why_unavailable() or ""
        check("an empty embeddings directory is unavailable with a reason",
              "no embeddings yet" in why and semantic.INSTALL_HINT in why, why)
        check("available() agrees", semantic.available() is False)
        check("has_chunks() is False when unavailable", semantic.has_chunks() is False)

        (d / "talks.ids.json").write_text("{not json")
        semantic._manifest.cache_clear()
        check("an unreadable manifest is 'no embeddings yet', not a crash",
              "no embeddings yet" in (semantic.why_unavailable() or ""))

        stale = dict(live)
        stale["talks_json_bytes"] = live["talks_json_bytes"] + 1
        manifest(d, ["a", "b", "c"], stale)
        fake_npy(d / "talks.f16.npy", (3, 256))
        check("a stamp from an older talks.json steps aside",
              "older than talks.json" in (semantic.why_unavailable() or ""))

        manifest(d, ["a", "b", "c"], live)
        (d / "talks.f16.npy").unlink()
        check("a current manifest with no vectors reports the missing file",
              "talks.f16.npy is missing" in (semantic.why_unavailable() or ""))

        fake_npy(d / "talks.f16.npy", (2, 256))
        why = semantic.why_unavailable() or ""
        check("a row count that disagrees with the ids is a half-finished build",
              "2 rows for 3 ids" in why and "--force" in why, why)

        fake_npy(d / "talks.f16.npy", (3, 256))
        why = semantic.why_unavailable()
        libs = ((semantic._libs_here() or semantic._venv_ready())
                and semantic.model_snapshot() is not None)
        check("consistent files are available exactly when an interpreter and the model are there",
              (why is None) == libs, why)
        check("has_chunks() is False when the manifest says none",
              semantic.has_chunks() is False)

        manifest(d, ["a", "b", "c"], live, chunks=7)
        check("has_chunks() needs the chunk files, not just the count",
              semantic.has_chunks() is False)
        fake_npy(d / "chunks.f16.npy", (7, 256))
        check("has_chunks() needs the spans file too", semantic.has_chunks() is False)
        fake_npy(d / "chunks.spans.f32.npy", (7, 3), descr="<f4")
        check("has_chunks() is True with count, vectors and spans agreeing (when available)",
              semantic.has_chunks() is libs)
        fake_npy(d / "chunks.f16.npy", (6, 256))
        check("has_chunks() is False when the chunk row count disagrees",
              semantic.has_chunks() is False)
finally:
    for k, v in REAL.items():
        setattr(semantic, k, v)
    semantic._manifest.cache_clear()

check("the real paths are restored", semantic.TALK_IDS == REAL["TALK_IDS"])


# --- end to end through the subprocess, only when a layer is installed ---------

why = semantic.why_unavailable()
if why:
    print(f"SKIP the end-to-end half: {why}")
else:
    t0 = time.time()
    hits = semantic.search_talks("keeping agents from going off the rails", k=5)
    dt = time.time() - t0
    check("search_talks returns k (video_id, cosine) pairs", len(hits) == 5 and
          all(isinstance(v, str) and isinstance(s, float) for v, s in hits), hits)
    check("search_talks is best first", all(a[1] >= b[1] for a, b in zip(hits, hits[1:])))
    check(f"one query round-trips in under 3 s (took {dt:.2f} s)", dt < 3)
    ids = semantic._manifest()["ids"]
    sub = semantic.search_talks("agents", k=3, pool=[ids[0], 2, ids[5]])
    check("a pool restricts the candidates", {v for v, _ in sub} <= {ids[0], ids[1], ids[5]}, sub)
    vec = semantic.embed_query("hello")
    check("embed_query returns a unit-length list of floats",
          isinstance(vec, list) and abs(sum(x * x for x in vec) - 1) < 1e-3, len(vec))
    if semantic.has_chunks():
        ch = semantic.search_chunks("what an eval harness should measure", k=4)
        check("search_chunks returns (video_id, start, end, cosine) with start <= end",
              len(ch) == 4 and all(s <= e for _, s, e, _ in ch), ch)
        check("search_chunks caps one window per talk by default", len({v for v, *_ in ch}) == 4, ch)
    else:
        print("SKIP chunks: not built (install_semantic.sh --chunks)")

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: " + "; ".join(FAILS))
    sys.exit(1)
print("all checks passed")
