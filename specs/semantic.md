# The optional semantic layer

## What

An opt-in, embedding-based recall layer for `tools/query.py`. FTS5 in
`talks.db` (see `search-cli.md`) answers every query on the standard library;
what it cannot do is find a talk that *means* the question without *saying*
it ("keeping agents from going off the rails" shares no stem with
"guardrails"). This layer adds that and only that.

Three rules, enforced by the code, not by convention:

| Rule | Meaning | Where enforced |
|---|---|---|
| Opt-in | Vectors are built by `tools/install_semantic.sh` and by nothing else — never by `atu.db_stale()`, `build_index.py`, CI or a first query. A clone that has not run the script behaves exactly as before. | `build_embeddings.py` is the only writer of `data/embeddings/`; no workflow in `.github/` mentions it |
| Silent fallback | `available()` is False when vectors are missing, stale, half-written, or the libraries/model are absent. `query.py` then searches FTS5 alone and says nothing unless `--explain`. | `semantic.why_unavailable()`, `query.semantic_layer()` |
| Union, not rerank | Lexical and vector rankings are merged by reciprocal rank fusion so each side can add talks the other missed. Nothing is reordered on the lexical side alone; the failure being fixed is recall. | `semantic.fuse_rrf()`, `query.fuse_semantic()` |

What it is:

- Model: `minishlab/potion-base-8M` — model2vec *static* embeddings, 256-d,
  ~30 MB safetensors. A text's vector is a weighted mean of its token vectors,
  so it loads in ~0.1 s and embeds the corpus in seconds; quality is
  "moderate" (knows "guardrails" is near "safety", not that "off the rails" is
  an idiom). Needs numpy + tokenizers; no torch, no onnx, nothing compiled.
- Two levels: **talk vectors** (one per `talks.json` entry, always built) and
  optional **chunk vectors** (one per ~70 s transcript window, `--chunks`).
  Talk vectors drive ranking; chunk vectors are used only to *anchor*
  `--excerpt` on a vector-only hit (chunk-level ranking is a TODO, not built).
- Fused only for **bare queries** in `query.py`. Explicit FTS5 syntax
  (`title:`, `NEAR`, `OR`, quotes) and listings are run as typed, never fused.
- Not in the browser (`index.html`) — a query would need client-side
  embedding. Not required by the skill; the skill documents its caveats. See
  `search-browser.md`, `skill.md`.

Everything it creates is gitignored and derived (like `talks.db`):
`tools/.venv-semantic/` (venv + HF model cache) and `data/embeddings/`.
`rm -rf tools/.venv-semantic data/embeddings` removes all of it and nothing
in the repo notices.

State of this checkout (2026-09-03): **not installed** —
`python3 tools/semantic.py --status` reports `available: False (no embeddings
yet; run tools/install_semantic.sh)`. `test_semantic.py` passes on the
standard library and skips its end-to-end block.

## Where

| Path | Contents |
|---|---|
| `tools/semantic.py` | The layer's API and CLI. Two halves: stdlib-only (staleness, `.npy` header reader, pool mapping, RRF) that runs on every query, and the numpy half that runs in whichever interpreter has the libraries. |
| `tools/build_embeddings.py` | The only writer of `data/embeddings/`. Runs inside the venv. Talk text composition, chunk windows, batching, atomic writes, stamp. |
| `tools/install_semantic.sh` | The one install/rebuild entry point: venv, pip (wheels only), build, then a system-python `--status` smoke test. |
| `tools/requirements-semantic.txt` | Fully pinned wheel set: `model2vec==0.9.0`, `numpy==2.5.2`, `tokenizers==0.23.1`, `safetensors==0.8.0`, `huggingface_hub==1.29.0` + transitive deps. No torch/onnx. |
| `tools/test_semantic.py` | 67 checks on the stdlib half with paths redirected to a temp dir; end-to-end block only when a layer is installed. |
| `tools/query.py:756-880` | The consumer: `semantic_layer()`, `semantic_text()`, `fuse_semantic()`, `semantic_anchors()`. `--semantic/--no-semantic` at `:1502`, wiring at `:1555-1585`, anchors at `:1607`. |
| `tools/excerpt.py` | `--at SECONDS` (`:194`) — the companion a vector-only hit needs; `excerpt_talk(..., anchors=)` is what `query.py --excerpt` feeds. |
| `tools/uitest/suite-ranking.js:58` | Runs `query.py --no-semantic` so browser-vs-CLI agreement is lexical vs lexical. |
| `.gitignore` | `tools/.venv-semantic/`, `data/embeddings/`. |
| `.claude/skills/ai-conference-talks/SKILL.md:276-292` | "The optional semantic layer" — the caveats a model needs. |
| Docs | `ARCHITECTURE.md:541-560` (flowchart, stamp), `README.md:395-427`, `HISTORY.md:1613-1650` (measurements), `TODO.md:39-44` (next steps), `STATE.md:35`. |

### `tools/semantic.py` — key symbols

| Symbol | Purpose |
|---|---|
| `MODEL_NAME`, `LAYER_VERSION = 1` | Model id; bump `LAYER_VERSION` when `talk_text()` or chunk geometry changes shape (old files would still load and be wrong). |
| `VENV`, `VENV_PYTHON`, `MODEL_CACHE` | `tools/.venv-semantic`, its python, and `tools/.venv-semantic/hf-cache` (HF_HOME is forced there before model2vec imports, so a user's own HF cache is never consulted). |
| `EMBEDDINGS`, `TALK_VECTORS`, `TALK_IDS`, `CHUNK_VECTORS`, `CHUNK_SPANS` | `data/embeddings/{talks.f16.npy, talks.ids.json, chunks.f16.npy, chunks.spans.f32.npy}`. |
| `RRF_K = 60` | RRF smoothing constant (Cormack et al. 2009). |
| `corpus_stamp()` | What vectors must have been built from: model, layer_version, `atu.DB_SCHEMA_VERSION`, `talks.json` `generated_at` (regex over first 4 KB, not a parse) + byte size, transcript file count. Cheap enough for every query. |
| `stale_reason(built, current)` | Pure comparison → reason string ending in what to do (`--force` for model/layer/schema mismatches, plain rerun for corpus drift), or None. |
| `npy_shape(path)` | Reads a `.npy` header with the stdlib so row counts can be checked without numpy. |
| `why_unavailable()` / `available()` | The gate: stamp current, vectors present, rows == ids, an interpreter (in-process or venv), model snapshot downloaded. |
| `has_chunks()` | Chunk vectors exist, row count matches manifest `chunks`, spans file present. |
| `pool_to_rows(pool, ids)` | Maps `query.py`'s pool (talks.db `n` 1-based ints, video ids, or a mix) to vector rows; unknowns ignored, never raised. |
| `embed(texts)` | L2-normalised float32 vectors; shared by build and query so both embed identically. Needs numpy. |
| `_do(op, req)` / `_call(op, req)` | One implementation; `_call` runs it in-process if numpy+model2vec import, else as `VENV_PYTHON semantic.py --serve` (JSON on stdin/stdout, 120 s timeout, cwd = repo root). |
| `search_talks(query, k=50, pool=None)` | → `[(video_id, cosine)]`, pool applied *before* top-k. Raises if not `available()`. |
| `search_chunks(query, k=50, pool=None, per_talk=1)` | → `[(video_id, start_s, end_s, cosine)]`; `per_talk` caps windows per talk (overlapping windows produce twins). Empty when no chunks. |
| `fuse_rrf(lexical, semantic, k=60, w_lexical=1, w_semantic=1)` | Union by RRF: each id scores `w/(k+rank)` per list it is on; ties by lexical then semantic position; duplicates within a list count once. Only positions are compared — bm25 and cosine are never mixed. |
| `embed_query(text)` | The query vector as a plain list. |

### On-disk format (`data/embeddings/`)

| File | Shape / content |
|---|---|
| `talks.f16.npy` | `(N, 256)` float16, rows L2-normalised, row i == `talks.json[i]` == talks.db `n = i+1` (same order `build_index.py` numbers talks). 4.4 MiB for 9,048 talks. |
| `talks.ids.json` | `{"ids": [video ids], "stamp": corpus_stamp(), "chunks": M or null}`. Written **last**; stdlib-readable. |
| `chunks.f16.npy` | `(M, 256)` float16, one row per transcript window; only with `--chunks`. 86 MiB for 176,573 windows. |
| `chunks.spans.f32.npy` | `(M, 3)` float32: `[talk row, start s, end s]`. |

### `tools/build_embeddings.py` — key symbols

| Symbol | Purpose |
|---|---|
| `OPENING_WORDS = 250` | Transcript words appended to the talk text (0/250/600 were tried; 250 measured best). |
| `WINDOW_WORDS = 192`, `WINDOW_STRIDE = 96` | 16× and 8× `build_index.PASSAGE_STRIDE` (12), so every window starts on `talks.db`'s passage grid and a start handed to `excerpt.py --at` opens the same speech FTS5 would quote. ~70 s per window at 2.7 words/s. |
| `BATCH = 4096` | Texts per `encode()`; memory bound only — batching never changes a vector. |
| `fetch_model()` | Downloads only `config.json`, `model.safetensors`, `tokenizer.json` into `MODEL_CACHE` (HF layout); returns bytes fetched (0 when cached). |
| `talk_text(t, segs)` | title / speakers / `conference · edition · category` / tags / whole description / first 250 transcript words, newline-joined, empties dropped. Talks without a transcript (≈65%) embed metadata alone. |
| `chunk_windows(segs)` | Windows over `build_index.timed_words()`; last window may be short but ≥ `WINDOW_STRIDE`. Transcripts `build_index.held_back()` rejects are skipped. |
| `save_npy` / `save_json` | Temp name + `os.replace`; vectors first, manifest last, so a reader sees the old complete layer or the new one. |
| `up_to_date(want_chunks)` | The `--if-stale` check (via `why_unavailable()` + `has_chunks()`). |
| `build(want_chunks)` | Stamp taken before reading the corpus and re-checked after; a corpus that changed under the build is an error. Without `--chunks`, stale chunk files are deleted. |

### `tools/query.py` integration

- `semantic_layer(want, explain)` `:770` — `--no-semantic` → None; unset →
  layer if available, else None (reason on stderr only under `--explain`);
  `--semantic` → `SystemExit` with the reason if unavailable.
- `semantic_text(raw)` `:791` — embeds the question *as asked* minus `-word`
  exclusions; stopwords are kept (they carry meaning to an embedding).
- `fuse_semantic(con, sem, res, text, k)` `:800` — `k = max(3 × limit, 50)`
  (`SEMANTIC_WIDTH`, `SEMANTIC_MIN_K` `:766-767`). Fuses the lexical **head**
  (top k) with `search_talks(text, k, pool=res.allowed − res.banned)`, so
  `--conference`, `--year`, `-word` etc. bind both sides. Scores are fused
  scores scaled so best = 1.0; lexical hits beyond k trail below, in their own
  order. Each hit gets `via` ∈ `lexical | semantic | both` and `cosine` when
  the vectors saw it. A `via: "semantic"` hit has no bm25, no moments, no
  snippet; rendered "(semantic match: none of the query's words, near it in
  meaning)" `:1276`.
- `semantic_anchors(sem, text, hits, per_talk)` `:860` — for vector-only hits
  under `--excerpt`, `search_chunks(pool=those talks)` gives start seconds
  that `excerpt.excerpt_talk(anchors=)` centres on instead of the opening.
  Empty without chunk vectors.
- Stderr note when on: `semantic layer on: N talks found by meaning alone,
  ranked by fused rank` (stdout under `--excerpt`).

### Commands

```bash
tools/install_semantic.sh              # venv + wheels + model + talk vectors (~10 s build after install)
tools/install_semantic.sh --chunks     # + transcript windows (~85–90 s more); kept on later runs without the flag
tools/install_semantic.sh --force      # rebuild even when the stamp is current
python3 tools/semantic.py --status     # what is on disk, the stamp vs the corpus, and why (un)usable
python3 tools/semantic.py "agents going off the rails" -n 5 [--json]   # talk-level, layer alone
python3 tools/semantic.py --chunks "eval harness" -n 10                # window-level
python3 tools/semantic.py --embed-query "text"                         # vector as JSON
tools/.venv-semantic/bin/python tools/build_embeddings.py [--chunks] [--if-stale]   # what the script calls
cd tools && python3 test_semantic.py   # < 1 s, system python, no numpy
python3 tools/query.py "..." --semantic | --no-semantic | --explain
```

Measured (HISTORY.md, 2026-09-02): cold install 196 s (pip 118 MiB in 12 s,
model 29.5 MiB, talks ~10 s, chunks ~85 s); 1–2 s when current;
byte-identical on `--force`. Query: `available()` ~12 ms; subprocess
round-trip ~600 ms (≈0.5 s is model load); in-process 18 ms warm. Fused
`query.py` call ~1.2 s vs 0.55 s lexical. Disk: venv ~133 MB + model 30 MB +
vectors 4.4 MiB (+ 88 MiB with chunks). CPU only; no GPU path exists or is
needed.

## How

- **Never wire the build into anything automatic.** Not `db_stale()`, not
  `build_index.py`, not `kb-refresh.yml`, not a first-query "let me build
  that for you". After `sync_catalog.py` the layer goes stale by design and
  steps aside until someone reruns `install_semantic.sh`.
- **Row order is the contract.** Vector row i == `talks.json[i]` == talks.db
  `n = i+1`. Anything that reorders `talks.json` or changes `build_index.py`'s
  numbering silently breaks `pool_to_rows()`; the stamp (generated_at + size)
  is what catches it. Do not add a code path that reads vectors without going
  through `available()`.
- **Bump `LAYER_VERSION`** whenever `talk_text()`, `OPENING_WORDS`,
  `WINDOW_WORDS`/`WINDOW_STRIDE` or the model changes. Bump
  `atu.DB_SCHEMA_VERSION` only for `talks.db` changes — the layer already
  reacts to that one.
- **Keep the stdlib half stdlib.** Everything on the query path before
  `_call()` (`corpus_stamp`, `npy_shape`, `why_unavailable`, `pool_to_rows`,
  `fuse_rrf`) must import on the system python3, which has no numpy
  (verified: Python 3.12.3, no third-party packages on the system interpreter).
  Import numpy/model2vec only inside functions.
- **One implementation, two interpreters.** New vector ops go in `_do()` and
  are reached via `_call()`; the `--serve` protocol is JSON-only, so return
  plain lists/floats, never arrays.
- **Fuse the lexical head, not the whole list** (`max(3n, 50)`): fusing
  everything let deep lexical hits the vectors liked outrank exact-title
  hits (1 of 10 vs 5 of 10 in lexical top-40 for "agent evaluation").
- **A vector-only hit contains none of the query's words.** Do not feed it to
  `excerpt.py -q <the query>` — it falls into the "showing the opening" path.
  Use `query.py --excerpt` (anchors automatically, needs `--chunks`) or
  `excerpt.py --at m:ss` / a `-q` in the talk's own vocabulary.
- **Ranking-agreement tests are lexical vs lexical.** `suite-ranking.js`
  passes `--no-semantic`; keep it that way unless the browser gains its own
  layer. Anyone with the layer installed who runs `query.py` by hand gets
  fused results — remember that when comparing numbers to docs.
- **Determinism.** Rebuilds from the same inputs are byte-identical; no
  timestamps in the files (the stamp copies `talks.json`'s `generated_at`,
  it does not mint one). Keep it so: `--if-stale` relies on it.
- **Pinned wheels only.** `install_semantic.sh` passes
  `--only-binary=:all:`; adding a dependency means adding its exact pin and
  its transitive pins to `requirements-semantic.txt`. Behind a TLS-rewriting
  proxy the model fetch can fail where pip succeeds (certifi vs system CA);
  the script exports `SSL_CERT_FILE` to the system bundle when unset.
- **Where docs and code disagree, the code wins:**
  - `README.md:418-421` says a missing layer "says why on stderr". Code:
    silent unless `--explain` (`query.py:786-788`); only `--semantic` errors.
    SKILL.md and ARCHITECTURE.md state it correctly.
  - `TODO.md:39` lists chunk-level *ranking* and a cross-encoder rerank as
    possible next steps — neither exists; chunks anchor excerpts only.
