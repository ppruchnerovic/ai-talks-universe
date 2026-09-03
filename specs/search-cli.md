# Searching from the terminal — `query.py`, `excerpt.py`, `talks.db`

## What

Two scripts in `tools/`, one SQLite file in `data/`, all standard library plus
the SQLite that ships with Python 3.12 (FTS5 with `porter unicode61`).

| Piece | Does | Does not |
|---|---|---|
| `tools/query.py` | Ranks talks for a query over two FTS5 layers — talk metadata (`talks_fts`) and timestamped transcript passages (`segments_fts`) — with filters, facets, sorts and four output shapes. Optionally fuses in the vector layer. | Build the index; build vectors; render anything in a browser. |
| `tools/excerpt.py` | Prints the parts of one or more talks that answer a query, under a word/time budget, instead of the whole 8–9K-token transcript. Three cheaper views: `--quotes`, `--outline`, `--at`. | Rank talks (it imports `query` for parsing and shares its bm25). |
| `data/talks.db` | Derived, gitignored, ~400 MB. Built by `build_index.build_sqlite()` (see `search-browser.md`), auto-rebuilt by `atu.connect()` when stale. | Ship anywhere. `n` (dense rowid) never leaves the file. |

Consumers: a human at a terminal, the `ai-conference-talks` skill (`skill.md`,
which parses `--json`/`--brief`/`--ids` and pipes into `excerpt.py`), and the
browser's ranking-agreement Playwright suite (`search-browser.md`), which
parses `query.py --json` as a bare list. The browser ranker in `index.html`
and this CLI must agree by construction: same stemmer (`atu.stem()` and its JS
twin, `test_stem.py`), same field weights, same "said together" bonus
constants, same `atu.SYNONYMS` groups.

Related specs: `data-model.md` (talk record fields), `transcripts.md` (where
segments come from), `search-browser.md` (`build_index.py`, `tindex/`,
`search-meta.json`), `semantic.md` (`semantic.py`, `data/embeddings/`),
`skill.md`.

## Where

### `data/talks.db` — the schema (`tools/build_index.py:43-88`, `SCHEMA`)

| Table | Kind | Columns / notes |
|---|---|---|
| `talks` | table | `n` PK (position in `talks.json`), `id` (video id or `iq-…`), `title`, `description`, `speakers` (comma-joined), `conference`, `conference_name`, `category`, `edition`, `year`, `channel`, `tags` (comma-joined), `duration_min`, `published_at`, `url`, `youtube_url`, `page_url`, `availability`, `priority`, `has_transcript`, `transcript_words`, `timing` (`exact`/`estimated`/NULL), `topics` (JSON list) |
| `talk_topics` | table | `(talk_n, topic)` one row per pair; what `--topic` and `--list-topics` read. Topics are in neither FTS table. |
| `talks_fts` | FTS5, content-carrying | `title, description, tags, speakers, conference_name`; rowid = `talks.n`; `tokenize='porter unicode61'` |
| `segments` | table | `rowid, talk_n, start` (seconds), `pos` (word offset), `bridge` (1 for the half-stride overlapping tiling), `text` (24 words) |
| `segments_fts` | FTS5, external content on `segments` | `text` only; `tokenize='porter unicode61'` |

- Passages: `PASSAGE_WORDS = 24`, `PASSAGE_STRIDE = 12` (`build_index.py:105-106`). Every passage has a twin overlapping it; readers wanting the transcript back whole take `bridge = 0`.
- `PRAGMA user_version` = `atu.DB_SCHEMA_VERSION` (`tools/atu.py:816`, currently **6**), stamped last in `build_sqlite()` so a half-built file reads as v0.
- `atu.db_stale()` (`atu.py:819`) → rebuild reasons: file missing, `user_version` mismatch, `talks.json` or `data/transcripts/` mtime newer than the db. `atu.connect()` (`atu.py:849`) rebuilds via `build_index.main(["--quiet"])` (~30 s, says so on stderr) and opens read-only. Both CLIs use it.

### `tools/query.py` (1675 lines) — function map

Constants worth knowing (lines 70–144): `W_META=1.0`, `W_SEG=0.7`; `MOMENTS=4` passages kept per talk, `MOMENT_CANDIDATES=12`; `PASSAGE_W=1.6`, `SATURATE=log 4` (must equal `index.html`'s `passageFactor`); `QUERY_STOPWORDS` (question furniture: "people say talk…", on top of `atu.STOPWORDS`); `MAX_TERMS=32`; `FTS_COLUMNS`/`LAYERS`; `SORT_SCORE_FLOOR=0.3`, `SORT_WIDTH=5`, `SORT_MIN_WIDTH=100`; exit codes 141/130 for SIGPIPE/SIGINT.

**The query language** (lines 154–431)

| Symbol | Line | Purpose |
|---|---|---|
| `COLUMNS` | 161 | Column-filter names and aliases: `title`, `description`/`desc`, `tags`/`tag`, `speakers`/`speaker`, `conference`/`conf`/`conference_name`, and the CLI-only `transcript` (passage layer). No `year:`/`topic:` prefixes — those are `--flags`. |
| `EXPLICIT_RE` | 168 | Decides explicit vs bare: any `"`, `*`, `OR/NOT/AND/NEAR`, or a known column prefix glued to a term (`title:x`; `agents: what` stays bare). |
| `SCAN_RE`, `quote_term()` | 175, 265 | Tokenise explicit syntax; quote barewords FTS5 would misread (`gpt-4`→`"gpt-4"`, `c++`, `don't`), keep `prefix*` outside the quotes, pass column prefixes through unquoted. |
| `explicit_items()`, `explicit_query()` | 289, 318 | Items + the operator if a flat chain; dedupe and cap only flat AND/OR chains. Stray commas dropped unless `NEAR` present. |
| `split_layers()` | 339 | Per-layer expressions for column filters: `transcript:` items go to `segments_fts` (prefix stripped), other prefixes to `talks_fts`; in a flat AND chain every item is a gate. Parenthesised/NEAR/NOT expressions cannot mix `transcript:` with other filters → `SystemExit`. |
| `synonyms()` | 387 | A bare word whose *stem* belongs to an `atu.SYNONYMS` group (`atu.py:67`) becomes the OR of the group — one gate term. |
| `parse_query()` → `Parsed` | 405, 195 | Explicit → run as typed, never expanded or relaxed. Bare → `-word` exclusions lifted out, stopwords dropped (kept if *all* are stopwords), deduped, capped, synonym groups, `strict` = AND of groups. Empty words → a listing (`strict == ""`). `Parsed.relaxed` = OR of everything (used by `excerpt.py` inside one talk). |

**Filters and the search** (lines 434–763)

| Symbol | Line | Purpose |
|---|---|---|
| `build_filters()` → `Filters` | 443 | One WHERE fragment on `talks t`: `conference`/`category`/`year` IN-lists, `min/max_year`, `min/max_duration`, `since`/`before` (ISO text compare on `published_at`, fallback to `year` when NULL), `speaker` (LIKE substring, escaped), `topic` (membership in `talk_topics`, OR-ed), `transcript`, `exact_timing`. |
| `talks_matching()`, `talks_saying()` | 498, 515 | Set of talk `n` matching an FTS5 expression on one/either layer — the gate. |
| `Result` | 527 | `hits` (whole pool, best first — the cut happens later), `dropped`, `meta_q`, `seg_q`, `allowed`, `banned`. |
| `search()` | 563 | The gate + relaxation loop: intersect per-term `talks_saying` sets (∩ filters, − exclusions); while empty and >1 term, drop a term *no* talk says first, else the commonest; then `rank()` on the OR of the kept groups with `together_q` = their AND. Explicit queries: gate on `Parsed.gate` if any, otherwise rank directly. |
| `kept_query()` | 624 | The bare query as actually searched (dropped groups removed) — what `--excerpt` passes down. |
| `rank()` | 639 | Metadata: `bm25(talks_fts, 8.0, 2.0, 4.0, 4.0, 1.5)` (title, description, tags, speakers, conference). Transcript: best `MOMENTS` non-overlapping passages per talk via `ROW_NUMBER()`, summed with `1/sqrt(k)` diminishing returns, × `(1 + 1.6·min(1, log1p(together)/log 4))`. Each layer normalised to [0,1] over the pool, then `score = 1.0·meta + 0.7·seg`. |
| `collapse_dupes()` | 730 | One hit per folded title; the rest of the ids go in `also`. |

**Semantic fusion** (lines 766–876; the layer itself is `semantic.md`): `semantic_layer()` (use when vectors current, `--semantic` insists, `--no-semantic` refuses), `semantic_text()` (the raw question minus `-word`s — stopwords are meaning to an embedding), `fuse_semantic()` (RRF as a *union* over the top `max(3·n, 50)` lexical hits and the same-k vector hits from the same pool; lexical tail appended below; `via` = `lexical`/`semantic`/`both`), `semantic_anchors()` (chunk timestamps for vector-only hits so `--excerpt` has somewhere to look). Bare queries only.

**Choosing what to show** (lines 879–1040): `SORTS`, `SORT_KEYS`, `above_floor()` (candidates ≥ 0.3 × best score, within the top `max(5·n, 100)`), `arrange()` (relevance = as ranked; other sorts, `--random`, `--per-conference/--per-year K` all draw from above the floor), `add_columns()` (`TALK_COLUMNS` at 943), `add_snippets()` (959: `highlight()` for short columns, `snippet()` for description/passages; `matched` = which layers hit, in index order so title beats description; a vector-only hit is labelled `semantic`), `count_facets()` (1022; `FACETS` = conference, year, category, has_transcript — **not** topic).

**Filter values, stats** (lines 1041–1195): `norm()`, `facet()` (also handles `topic` via the join table), `resolve()` (1073: case/separator-insensitive; one word of a label suffices when unambiguous, the label it *heads* wins; otherwise fails with did-you-mean from `difflib`), `check_speaker()` (1124: fails a `--speaker` matching nobody with the nearest whole names), `stats()`/`print_stats()` (1148: counts from the index, `--stats --json` for data).

**Output** (lines 1197–1397)

| Symbol | Line | Purpose |
|---|---|---|
| `want_color()`, `set_color()` | 1200 | Colour only on a TTY, off under `NO_COLOR`, `--color/--no-color` override. |
| `fmt_ts()` | 1214 | `m:ss`, prefixed `~` when `timing == "estimated"`. |
| `render()` | 1235 | Text: numbered hits, speakers, conference · edition · year · duration · transcript · `match: …`, `(also: …)`, topics, `--explain` score line, snippet, up to 4 moments with `&t=Ns` deep links (only for YouTube urls). |
| `render_facets()` | 1288 | `N matching talks` + top-12 counts per facet. |
| `BRIEF`, `BRIEF_MOMENTS=2`, `EXPLAIN`, `HIT_FIELDS` | 1303–1318 | `--brief` preset; the per-layer fields popped unless `--explain`; the valid `--fields` names. |
| `shape()`, `emit_json()` | 1333, 1356 | JSON: bare array of hits; `speakers`/`tags` as lists; match markers `[[…]]`; moments `[{start, text}]`. Only `--facets` wraps in `{"total", "facets", "notes", "hits"}`. `--brief` is single-line JSON. |
| `emit_md()` | 1386 | Markdown table; default columns `MD_FIELDS` (1374), `--fields` overrides. |

**CLI** (lines 1399–1675): `main()` at 1424 defines every flag (see the table
below), `parse_known_args` so a `-word` exclusion survives argparse
(`EXCLUSION_ARG_RE` 1421). `excerpt_query()` (1639) chooses what `--excerpt`
searches inside each talk. `run()` (1657) maps SIGPIPE/SIGINT to exit codes.

Flags, grouped: query filters `--conference`, `--category` (conference type),
`--topic`, `--year` (all repeatable, resolved), `--min-year`, `--max-year`,
`--since`, `--before`, `--speaker`, `--min-duration`, `--max-duration`,
`--transcript`, `--exact-timing`; ordering `-n/--limit`, `--sort`, `--random`
`--seed`, `--per-conference K`, `--per-year K`; corpus views `--facets`,
`--list-conferences`, `--list-categories`, `--list-topics`, `--stats`; output
`--json`, `--md`, `--brief`, `--fields`, `--ids`, `--no-moments`, `--explain`,
`--color/--no-color`; reading `--excerpt`, `--passages N`; vectors
`--semantic/--no-semantic`.

### `tools/excerpt.py` (914 lines) — function map

Constants (lines 59–121): `ID_RE` (an id starting with `-`), `TAKES_VALUE`, `WINDOW=40` s either side of a hit, `OPENING=60` s always included with a query, `PASSAGES=6`, `OVERSAMPLE=4`, `MAX_QUOTE_WORDS=60`, `OUTLINE_BUCKET=120` s, `OUTLINE_TERMS=5`, `OUTLINE_STOPWORDS`.

| Function | Line | Purpose |
|---|---|---|
| `split_ids()` | 123 | Lift hyphen-leading video ids out of argv before argparse sees them. |
| `COLS`, `ids_in_filename()`, `find_talk()` | 145–187 | Accept a video id, YouTube URL, or `talks/<conf>/<id>-<slug>.md` path; a YouTube id is the first 11 chars, an InfoQ id is tried longest-prefix-first. |
| `parse_at()` | 193 | `--at` as `600`, `10:00`, `1:02:03`, comma lists. |
| `spans_for()`, `covered()`, `merge()` | 223–258 | **The budget**: best hit first, ±`window` each, stop once the merged union reaches `limit × 2 × window` seconds. Overlapping/touching windows become one passage. |
| `tiles_in()`, `trim_to_words()` | 261, 276 | Primary tiles per span; `--words` trims end tiles farthest from any anchor, never the middle. |
| `hits_for()` | 311 | bm25 over this talk's passages on `parsed.strict`, falling back to `parsed.relaxed` (OR) and reporting that it did — a 25-word passage rarely holds all of a question's words. |
| `query_stems()` | 351 | Stems (incl. synonym members) a passage matched on, for finding the sentence. |
| `primary_tiles()`, `tile_at()` | 371, 382 | `bridge = 0` tiles in order; the tile under a second. |
| `passages()` | 400 | The main view: anchors (`--at`, semantic) spent first, then ranked hits; nothing matching → the opening only, with a note (never the whole transcript). |
| `sentences()`, `timed_words()`, `quote_for()`, `quotes()` | 475–589 | `--quotes`: the first sentence overlapping the hit that holds a query stem, its time interpolated within the tile; falls back to the tile when speech has no punctuation. Count offered as "more" is of distinct sentences. |
| `outline()`, `bucketize()` | 592, 610 | `--outline`: per-bucket top tf-idf stems (idf across this talk's buckets) and a hit-density count (`#` column, the reliable one). |
| `header()`, `stamp()`, `print_notes()`, `render*()` | 651–755 | Markdown-ish text. Notes go to **stdout**. Header says whether the description is InfoQ's abstract or YouTube's blurb; `&t=` links only for YouTube. Ends with `x of y words (z%)`. |
| `excerpt_talk()` | 758 | Entry point for a caller with a talk in hand (`query.py --excerpt`): mode `passages`/`quotes`/`outline`, returns data. |
| `as_json()`, `main()` | 797, 818 | `--json` is a list, one object per talk: metadata + `mode`, `notes`, and `passages`/`quotes`/`outline`, `excerpt_words`. `--total-words` is shared across transcript-bearing talks in argv order. |

Flags: `ID…`, `-q/--query`, `-n/--passages` (budget: windows, or quotes under
`--quotes`), `--window`, `--opening` (0 for none), `--at` (repeatable),
`--words`, `--total-words`, `--quotes`, `--outline`, `--full` (mutually
exclusive views), `--json`. Exit 1 only if every id was missing.

### Tests (all plain scripts; `check()` prints `ok`/`FAIL`, exit non-zero on failure)

| File | Runs in | Exists to catch |
|---|---|---|
| `tools/test_query.py` | 0.1 s; pure functions + a throwaway in-memory db (line 186 on) | Explicit terms FTS5 misreads (`gpt-4 OR claude`, `c++`), structure preserved, bare-query stopword/ dedupe rules, column filters reaching FTS5 as filters and split per layer, `-word` exclusion, synonym expansion, `ids_in_filename()` on hyphenated ids, `--topic` join, `resolve()` on case/separators/one-word labels and ambiguity. |
| `tools/test_excerpt.py` | 0.1 s, pure functions | The excerpt that is the whole transcript: `merge`, `spans_for` budget, what `--window`/`-n` buy, `trim_to_words`, sentence splitting for `--quotes`, `query_stems`, `bucketize`, `parse_at`, hyphen-leading ids. |
| `tools/test_stem.py` | ~6–10 s; reads the corpus, runs node if present | `atu.stem()` and the JS stemmer lifted out of `index.html` disagreeing on any corpus token (a silent miss on one side); Porter paper examples first. |
| `tools/test_speakers.py` | 0.1 s | `sync_catalog.speakers_from_title/description()` false positives — a brand or job title in the 4×-weighted field (`catalog-sync.md`). |
| `tools/test_topics.py` | 0.1 s | `atu.topics_of()` firing on the wrong title; the rule boundaries; every pattern matching its own canonical phrase; boilerplate filter (`data-model.md`). |

### Decision docs

- `TODO.md` — the search enrichment items that are still open.
- `HISTORY.md:1511` "Search enrichment — 2026-09-02" — the write-up of what landed.
- `ARCHITECTURE.md:363-416` (CLI), `:466-540` (index files), `:560-585` (excerpt); `README.md:319-455`, `:807-862`.

## How

### Commands

```bash
cd tools                       # scripts import atu/query by bare name; subagents reset cwd
python3 query.py "agent memory" -n 6 --excerpt
python3 query.py "mcp" --json --brief          # bare array; notes on stderr
python3 query.py "…" --ids | xargs python3 excerpt.py -q "…"
python3 excerpt.py O72p-rBb2bA -q evals --quotes
python3 test_query.py && python3 test_excerpt.py && python3 test_stem.py   # no pytest; run each file
```

First run after a `sync_catalog.py`/transcript fetch rebuilds `talks.db`
(~30 s, message on stderr). Force it with `rm data/talks.db`.

### Invariants a model gets wrong

- **Any change to what `build_sqlite()` writes** — a column, a table, passage shape, `MIN_WPM`, topic rows — bumps `atu.DB_SCHEMA_VERSION`. Without it every existing checkout queries a mismatched file. Bumped three times so far (`d8c2c13`, `d830dc0`, `0a57a43`). `semantic.py` also compares this version, so a bump invalidates embeddings (`semantic.md`).
- **Two rankers agree by construction.** Changing `W_META/W_SEG`, `PASSAGE_W`, `SATURATE`, the bm25 column weights, `atu.STOPWORDS`, `atu.SYNONYMS`, `atu.stem()` or relaxation order in `query.py` needs the same change in `index.html` (`search-browser.md`) and a run of the Playwright ranking suite. `QUERY_STOPWORDS` is CLI-only by design.
- **`--json` is a bare array** and stays one; the skill and the browser suite parse it. Advisory text goes to stderr (`warn()`), with two deliberate exceptions: the `--facets` envelope repeats the notes, and `--excerpt` in text mode prints notes to stdout because the reader is a model that never sees stderr. `excerpt.py` prints *everything* to stdout and has no colour — keep it that way.
- **Explicit FTS5 syntax is sacred**: run as typed on both layers, never relaxed, never synonym-expanded, never sent to the vector layer. Only bare queries get the gate/relax/synonym/semantic treatment. The test for "explicit" is `EXPLICIT_RE`; a colon only counts with a known column name glued to a term.
- **`-n` means different things**: result limit in `query.py`, a *budget of windows* in `excerpt.py` (`--passages` under `--excerpt`). It is a budget, not a count, so merged passages come back fewer and wider; do not "fix" that into a count.
- `--sort`, `--random`, `--per-*` never see the whole match set — only hits above `SORT_SCORE_FLOOR` (0.3 × best) inside the top `max(5·n, 100)`. A listing (no query) has `score = None` and is exempt.
- `--facets` counts conference/year/category/has_transcript over the whole pool, not topics; `--list-topics` counts talks per topic from `talk_topics` (sums to more than the corpus).
- `rank()` takes both pools whole and normalises across the pool; adding a `LIMIT` to `meta_sql`/`seg_sql` silently breaks the [0,1] scaling that the blend depends on.
- A transcript below `MIN_WPM` is indexed as no transcript (`has_transcript = 0`, zero words) though its file stays on disk; `--stats` counts as the db does.
- Video ids can start with `-`; `excerpt.py` lifts them before argparse. When adding an option that takes a value, add it to `TAKES_VALUE` or its value may be read as an id.
- `--speaker` is a substring LIKE on the comma-joined column (ASCII case-folding only); `speakers:"name"` is an FTS5 phrase on the stemmed column. They are not equivalent.

### The 2026-09-02 search enrichment — what is built, what is still open

Three defects found in that review are fixed. Column filters were mangled in
the CLI: `EXPLICIT_RE` now recognises prefixes, `quote_term()` passes them
through, `split_layers()` strips all but `transcript:` on the passage layer,
covered by `test_query.py` "column filters reach FTS5 as filters". `year:2025`
in the browser belongs to `search-browser.md`. Unconditional ANSI is fixed by
`want_color()`.

Verified against the code:

| Area | Item | Status in code |
|---|---|---|
| CLI, no schema change | column filters, TTY colour + `NO_COLOR`, `--speaker`, `--sort`, `--min/max-duration`, `--max-year`, `--since/--before`, `--exact-timing`, `--explain`, `--fields`, `--md`, `--random --seed`, filter-only listings, `-word`, `--facets`, `--per-conference/--per-year` | **All built.** |
| CLI, query-time | synonym groups | **Built** as query-time `atu.SYNONYMS`, shared with the browser via `tindex/_manifest.json`; no schema bump was needed. |
| CLI, schema change | `language` column / `--lang`, `fts5vocab` did-you-mean for query typos, trigram fuzzy `--speaker`, `--like/--related`, `--near N` | **Not built**; the open items are in `TODO.md`. Each needs a `DB_SCHEMA_VERSION` bump (except `--near`, which changes ranking). `check_speaker()`'s difflib did-you-mean is the partial substitute for fuzzy speakers; query-word typos are handled by relaxation (an absent word is dropped first), not corrected. |
| Skill | `--excerpt`, `--quotes`, `--outline`, `--words/--total-words`, `--at`, duplicate collapse | **Built.** Dupes are folded at query time in `collapse_dupes()` (`also` field), not marked at build time. |
| Semantic | the optional vector layer | **Built** as model2vec talk-level vectors with optional chunk anchors, opt-in via `tools/install_semantic.sh`, RRF union — `semantic.md`. |

Where a doc and the code disagree, the code wins. What remains open lives in
`TODO.md`, not here.
