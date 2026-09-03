# Search — the browser and the index files that feed it

## What

`index.html` is the public face of the corpus: one self-contained static page
(63 KB, vanilla JS, no build step, no dependencies) served from GitHub Pages at
<https://ppruchnerovic.github.io/ai-talks-universe/>. There is no backend, so
the search index is *files* that `tools/build_index.py` emits into `data/`
and the page fetches lazily. This spec covers:

| Piece | Role |
|---|---|
| `index.html` | loads the catalogue, parses the query, ranks on two layers (metadata + transcript), filters/facets, shows transcript "moments", keeps the whole view in the URL hash, exports, keyboard and a11y |
| `tools/build_index.py` | one offline pass over `data/talks.json` + `data/transcripts/` that emits **both** index halves: `data/talks.db` (SQLite/FTS5, for the CLI) and the browser files `data/search-meta.json` + `data/tindex/` |
| `tools/assemble_site.sh` | copies exactly what the page fetches into an output dir; what `pages.yml` publishes |
| `tools/uitest/` | Playwright + Chromium suites that drive the page against a local static server (or `KB_URL=` a deployed copy) |

Responsibilities that live elsewhere: what a talk record *is* and how
`talks.json` is derived (`data-model.md`, `catalog-sync.md`); transcript
fetching and file format (`transcripts.md`); `query.py`, `excerpt.py` and the
SQLite schema in depth (`search-cli.md`); the optional embedding layer
(`semantic.md`) — **the browser has no semantic layer** and never will without
client-side embedding; the GitHub workflows (`publishing.md`).

The one architectural contract: **two rankers, one corpus, and they agree by
construction.** Both tokenise on Porter stems (`atu.stem()` in Python, a
line-for-line twin inside `index.html`, `tools/test_stem.py` diffing them over
the corpus vocabulary), both weight speakers at 4× a description word, both
expand the same synonym table (`atu.SYNONYMS`, shipped to the browser in the
manifest), both relax an unmatched query in the same order, both treat a
~24-word passage as the unit two terms must share to count as "said together",
and neither scores the conference type. `suite-ranking` asserts the agreement.

**Built** (from the 2026-09-02 search enrichment, verified against the code;
line numbers below are the current file's): `title:`/`speaker:`/`conf:`/
`year:`/`transcript:` syntax, `-word`, quoted phrase as a gate, "said
together" badge, `OR` groups then synonyms, explicit `prefix*`, speaker
typeahead, duration sorts and length bucket, facet counts, "Spoken only",
"also matches in the full description", export/copy-link/`j`/`k`/newest-first
memory, the transcript-language badge. **Not built, by choice** — the open
items live in `TODO.md`: related talks, typo tolerance, autocomplete,
`_vocab.json`, per-talk pages (`#talk=`), inline snippets on every card.

## Where

### `index.html` — a map by line

| Lines | Section | What is there |
|---|---|---|
| 9–172 | CSS | `[hidden] { display:none !important }` at `:26` — the reset that keeps script-hidden controls hidden (do not remove; `suite-controls` guards it). `.card.cur` `:105` is the `j`/`k` mark |
| 175–221 | header | `#q` `:182`; hint text with the syntax examples `:187`; the filter row: `#f-conf` `:193`, `#f-cat` (conference type) `:194`, `#f-topic` `:195`, `#f-year` `:196`, `#f-len` `:197`, `#f-sort` `:204` (`rel/new/title/short/long`), `#f-spk` + `<datalist id="spk-list">` `:211`, toggles `#f-tr` `:214` and `#f-spoken` `:216` (both start `hidden`, `boot()` decides), `#clear` `:218` |
| 223–234 | main | `#status` (`role=status aria-live=polite`), `#tools` export bar (`#x-md #x-csv #x-link`), `#results`, `#more` |
| 245–277 | state | `PAGE=20`; **legend of `search-meta.json` keys `:250–263`**; `TALKS BY_N MANIFEST STOP DF` `:265`; `SHARDS` `:266` (shard key → shard); `TRANSCRIPTS` `:267` (video id → parsed transcript); `SYN` `:270` (stem → synonym alternatives); `prefGet/prefSet` `:276` — `localStorage['atu.sort']`, only ever `'new'` |
| 285–384 | Porter stemmer | between the literal markers `// --- porter stemmer ---` / `// --- end porter stemmer ---`; `test_stem.py:77` regex-lifts exactly this block and runs it under node. `stem()` `:328` |
| 389–410 | tokeniser | `TOKEN_RE` `:389`, `surface()` `:390` (lowercase, stopwords from the manifest, compound parts *and* whole), `tokenize()` `:406` (stemmed, drops stems < 2 chars) |
| 416–488 | `boot()` | fetches `data/search-meta.json` and `data/tindex/_manifest.json` in parallel (manifest failure → `null`, metadata-only mode); resolves `k` indices to topic names `:429`; builds per-talk `_hay`, `_f` field token sets (`title tags speakers conference`, plus `abstract` only when there is no manifest) `:434–446`, `_tok`; `DF` `:455`; subtitle + hides `#f-tr` when every talk has a transcript and `#f-spoken` when none does `:464–468`; `SYN` from `MANIFEST.synonyms` `:475`; then `fillFilters()`, `readHash()`, `run()` |
| 490–509 | `fillFilters()` | options built from the data: conferences by name, types, topics (union of per-talk lists), years newest-first, speaker datalist. Each option keeps `dataset.name` so facet counts can rewrite labels |
| 517–531 | shards | `shardChar`/`shardKeyOf` `:517` — two chars, `[a-z]` kept, digits → `0`, else `_`; **must equal `build_index.shard_key()`**. `loadShards(terms)` `:521` fetches only unlisted-yet shards the manifest names; a failed shard becomes `{}` |
| 534–584 | metadata scoring | `W = {title 9, tags 5, speakers 4, conference 3, abstract 2}` `:534`; `entryOf/dfOf/idf/talksWith` `:538–543` (a shard's `m` replaces the local DF when present); `fieldHit()` `:548` — exact 1.0, prefix 0.55 only for stems ≥ 4 chars or starred; `scoreMeta()` `:559` — per-term field hits × idf, description hits from the shard's `d` postings, phrase bonus 14×max idf; `META_FIELDS` `:584` |
| 589–633 | transcript scoring | `decodePositions()` `:589` (base-36 delta string → passage index set); `scoreTranscripts()` `:597` — BM25 `k1=1.4 b=0.72` with the manifest's `doc_len`/`avg_doc_len`; exact stem, else/also the 12 most-posted stems it prefixes at 0.45 decay |
| 640–671 | passage bonus | `PASSAGE_W=1.6 NEAR_W=0.5`, saturates at `log(4)`; `cooccur()` `:647`, `passageFactor()` `:663` — only ever promotes, mirrors `query.py`'s `W_SEG` |
| 680–720 | `gather(q)` | the gate and the merge: excluded stems drop talks (shard `d`+`p` postings and `_tok`); every group must be said by some alternative, phrase gate (metadata substring, or all its stems in one passage) `:708`; total = `meta + transcript × 2.2 × passageFactor` `:714`; returns `{t, score, fromTranscript, together, deep}` |
| 725–802 | `parseQuery(raw)` | `FIELDS` `:725`, `ITEM_RE` `:732` (minus, `field:`, quoted or bare — the colon is read here, never by the tokeniser); `year:`/`conf:` become `set`; `OR` joins into the previous group; `*` suffix marks prefix; de-dup of repeated words; synonym expansion into `g.alts` with `g.also` for the status line |
| 808–824 | `applyQuerySet()` | `year:`/`conf:` drive the selects (`conf:` by slug, name, or substring) and un-drive them when deleted unless the user changed the select since |
| 829–869 | `search(raw)` | parse → apply set → `spoken` flag → `loadShards` → listing mode when only exclusions/filters → `gather` → **relaxation** `:852`: drop a group no talk says at all, else the widest-reaching group, one at a time, recorded in `dropped`; sort by score; `hl` = typed stems only |
| 880–899 | `highlight()` | token walk with `TOKEN_RE_I`; lights whole tokens whose surface, stem, or ≥4-char stem prefix matches — never substrings |
| 901–962 | `card()` | link is `t.l` (InfoQ page) else YouTube watch URL `:909`; badges `:911–930`: conference (filter button), edition, year, minutes, `transcript` (only when coverage is partial), `transcript language: xx`, `said together`, `also matches in the full description` (`deepMatch()` `:958`), topic chips (`.b.topic`, set the topic filter), tag chips (`.b.tag`, run a search, first 6); clamped description + unfold button; "Find this in the talk" only when `t.w` and a query |
| 966–971 | `markOverflow()` | shows the unfold button only where the 4-line clamp hides text; re-run on resize `:1213` |
| 976–1014 | filters & facets | `LEN` buckets `:976`; `filterFn(skip)` `:983` — conf/type/topic/year/len/speaker-substring/transcript-only as one predicate with one dimension skippable; `facetCounts()` `:1000` counts each option under *every other* filter and rewrites **labels only** (values are what the hash and tests read) |
| 1016–1068 | `render()` | unranked when nothing searched; relevance falls back to newest with a note; sorts; status line with the transcript-only count, relax note, synonym note; pagination via `shown` |
| 1071–1103 | export | Markdown / CSV of `viewHits`, copy-link via clipboard |
| 1108–1115 | `moveCur()` | `j`/`k` over on-screen cards only |
| 1118–1177 | `showMoments()` | fetches `data/transcripts/<v>.json` once per page, token-scores each segment with `fieldHit`, picks ≤ 6 passages ≥ 60 s apart, links `watch?v=&t=<s>s` (or a plain span for InfoQ), stamps `~m:ss` when `t.x` |
| 1181–1209 | wiring | `run()` with a request sequence guard; 140 ms debounce on `#q` and `#f-spk`; selects `change` → `run()`; sort change persists `'new'`; Reset clears everything incl. the preference |
| 1215–1260 | click delegation on `#results` | conference badge → `#f-conf`; topic chip → `#f-topic`; tag chip → query; unfold; "Find this in the talk" open/close toggle |
| 1264–1274 | keyboard | `/` focuses search; `j`/`k`/`Enter` only when not typing; modifiers ignored |
| 1276–1306 | URL state | `writeHash()` uses `history.replaceState` (never `pushState`); params `q conf cat topic year len spk tr spoken sort`; `readHash()` validates `len` and `sort` against whitelists, applies the remembered sort only when the hash says nothing |

Ranking in the browser vs. the CLI (`search-cli.md` has the SQLite side): the
browser scores whole-transcript BM25 from postings and adds a passage
co-occurrence bonus from encoded positions; `query.py` scores individual
passages in `segments_fts`. Field weights differ, so the two disagree on
*order* by design and agree on *membership* — hence `suite-ranking` compares
the CLI's top 10 against the web's top 40.

### The index files (`data/`)

**`search-meta.json`** — `{"topics": [name…], "talks": [record…]}`, compact,
loaded whole before anything can be typed (5.8 MiB, 9,048 records at the time
of writing; 6 MiB trigger, see How). Record keys, from `build_index.py:430–465`:

| key | holds | notes |
|---|---|---|
| `i` | dense index `n` | 1-based position in `talks.json`; the id every posting and `data-n` uses; never leaves the build |
| `v` | video id (or `iq-…`) | transcript file name and YouTube URL |
| `t` `d` | title, description **clip** | `d` is clipped to `META_DESC_CHARS` (300) — display only; the full description is searched via shards |
| `s` `a` | speakers, tags | lists |
| `c` `cs` `g` `e` `y` | conference name, slug, **conference type** (registry `category`), edition, year | `g` is a filter, never scored |
| `m` `p` `u` | duration min, published_at, conference site | |
| `w` | transcript word count | `0` = no transcript *as content*; gates the badge, the toggle and the moments link |
| `k` | topic indices into `topics` | omitted when none (7,162 of 9,048 have it) |
| `l` | talk's own page URL | only when there is no YouTube URL (InfoQ, 222) |
| `x` | `1` | timings interpolated (`timing == "estimated"`, 228) → `~m:ss` |
| `lg` | language code | only when not `en` (27; the `hi` ones are mis-detected English) |

**`tindex/_manifest.json`** (`build_index.py:513–521`): `shards` (sorted list
of keys that exist — 711), `n_docs`, `avg_doc_len`, `doc_len` (`{n: len}`),
`stopwords` (`atu.STOPWORDS`, 182 — the browser tokenises with these),
`synonyms` (`atu.SYNONYMS`, 16 groups), `stemmed: true`.

**`tindex/<xx>.json`** — one object per two-character shard key, `{stem: entry}`:

| key | holds | used for |
|---|---|---|
| `f` | idf over transcripts | transcript BM25 |
| `p` | `[[n, tf, "b36.delta.positions"], …]` sorted by tf desc | transcript BM25; passage co-occurrence; "Find this in the talk" gating |
| `d` | `[[n, tf], …]` over the **whole** description | metadata layer beyond the clip; `-word` exclusion |
| `m` | talks whose metadata (description included) says the stem | metadata-layer idf (replaces the browser's local `DF`) |

A stem posted once in one transcript and in no description is dropped
(`build_index.py:494`). Positions index the primary passage tiling only.

**`talks.db`** — gitignored, derived; schema at `build_index.py:43–89`
(`talks`, `talk_topics`, `talks_fts`, `segments` with `bridge`, `segments_fts`,
`PRAGMA user_version = atu.DB_SCHEMA_VERSION`). Depth in `search-cli.md`.

### `tools/build_index.py` (604 lines)

| Symbol | Line | Purpose |
|---|---|---|
| module docstring | 1–20 | the three outputs and the two invocations |
| `SCHEMA` | 43 | SQLite DDL, dropped and recreated every run |
| `PASSAGE_WORDS=24`, `PASSAGE_STRIDE=12` | 105 | passage size; the bridge tiling is SQLite-only |
| `MIN_WPM=10`, `MIN_RATED_MINUTES=5` | 121 | ASR-failure floor: below it a transcript is indexed as *no content* (`w=0`) but the file stays |
| `TOKEN_SHARE_FLOOR`, `TOKENS_PER_WORD` | 139 | BM25 length for scripts the tokeniser cannot read |
| `META_DESC_CHARS=300` | 148 | the display clip; halve it when the file crosses the trigger |
| `META_SIZE_TRIGGER_BYTES` | 164 | 6 MiB, binary; `meta_size_report()` `:176` prints where the file stands every run |
| `timed_words`, `to_passages` | 189, 208 | word-level timings interpolated inside a caption line; overlapping passages `{start,pos,bridge,text}` |
| `HELD_BACK`, `held_back`, `transcript_text` | 236, 239, 255 | which transcripts were withheld and why (printed by `main`) |
| `build_sqlite(talks)` | 283 | `talks.db`; stamps `user_version` last |
| `shard_char`, `shard_key` | 329, 345 | **must equal `shardKeyOf()` in `index.html:517`** |
| `b36`, `encode_positions` | 361, 371 | passage positions as base-36 gaps |
| `meta_stems(t)` | 385 | the fields the browser scores (title, tags, speakers, conference+edition, description — *not* category); feeds `m` |
| `build_browser_index(talks, desc_chars)` | 401 | `search-meta.json` + shards + manifest; terms written **sorted** so output is byte-identical |
| `parse_args` | 526 | `-o/--out DIR` (write outputs elsewhere, read inputs from `data/`), `-q/--quiet`, `--desc-chars N` |
| `main(argv)` | 564 | `argv` defaults to `[]`, not `sys.argv` — `query.py` imports and calls it |

### `tools/assemble_site.sh` (37 lines)

`tools/assemble_site.sh OUT_DIR` — `rm -rf OUT_DIR`, then copies `index.html`,
`.nojekyll`, `ai-conferences.md` (footer link), `data/search-meta.json`,
`data/tindex/`, `data/transcripts/` minus `_misses.json`; prints `du -sh` as
the size report. `pages.yml` runs it with `_site` on every push to `main` and
publishes that tree as an orphan `gh-pages` commit (`publishing.md`).
`suite-navigation` runs the same script and serves the result, so a path the
page fetches that the script forgets fails a test.

### `tools/uitest/` — Playwright harness

`package.json`: dependency `playwright ^1.56`, `postinstall` runs
`playwright install chromium`, `npm test` = `node run.js`. Needs node (v24 in
use) and `python3` (for `http.server`). `node_modules/` is gitignored.

| File | What it does |
|---|---|
| `run.js` | discovers `suite-*.js`, serves the **repo root** on a free port with `python3 -m http.server` (or uses `KB_URL`), runs each suite in its own process, parses the `##RESULT pass fail skip` line, prints a tally, exits non-zero on any failure. `node run.js search filters` runs only those |
| `lib.js` | exports `BASE chromium check skip newPage boot search statusText cardCount titles cardNs resultCount meta suite`. `newPage` records console errors, page errors and failed requests; `boot(page, hash)` waits for `#sub` to stop saying "Loading"; `search(page, q)` fills `#q` and waits past the 140 ms debounce and shard fetch; `suite(name, body)` owns the browser and prints the tally. `BASE` defaults to `http://localhost:8765/` when a suite is run by hand |

| Suite | Exists to catch |
|---|---|
| `suite-load.js` | subtitle counts vs. the data; selects built from the data (conference, type, topic union, years newest-first, the five sorts); facet counts on labels; `#f-tr` hidden exactly when coverage is total; one card end-to-end (link, `noopener`, badge slug, topic chips); no moments link before a query |
| `suite-search.js` | AND semantics, order-independence, de-dup; tokens not substrings (`rag` never lit inside `program`); prefix and stem behaviour; relaxation and its status note; phrase as gate; each field incl. a description word beyond the clip; transcript-only hits counted; compounds/punctuation; `title:` `speaker:` `year:` `conf:` `transcript:`; `-word`; `OR`, synonyms (only the typed word lit), `prefix*`; empty/stopword/whitespace/bare-quote queries; typing vs. pasting race |
| `suite-controls.js` | `#more` and `.abs-more` really hidden (the `[hidden]` reset); pagination 20/40/60 and reset on new query; unfold only where the clamp hides text; tag chips search and scroll to top; `/`, `j`/`k`, `Enter`; export bar shows/hides, Markdown download |
| `suite-filters.js` | each filter returns exactly its talks; conference + year stack; topic membership (a two-topic talk under both), topic chip sets the filter; filters narrow a search; all five sorts and the "newest first — search to rank" note; length bucket, speaker box and typeahead; facet counts change labels not values; Spoken only; Reset; conference badge as filter; every param round-trips through the hash, unknown values fall back safely |
| `suite-moments.js` | picks a query from a transcribed talk's title; ≤ 6 passages, `m:ss` ascending, ≥ 60 s apart, deep links at the second, `~` for interpolated timings; open/collapse/re-open; transcript fetched once, by video id; "never spoken" message; 404 degrades to a message. Skips entirely with no transcripts |
| `suite-resilience.js` | one shard 404 → metadata-only with a strictly smaller count (and proves the fault matched a real request); no `tindex/` at all; catalogue 500 says so; HTML/script/regex injection via the query; 400-char, non-Latin, punctuation-only, eight-term queries; a record with only title + id renders; 390 px phone: no horizontal overflow, filter row wraps, unfold re-measured |
| `suite-a11y.js` | rewrites the catalogue in flight to force partial transcript coverage, then checks the `transcript` badge and `#f-tr` toggle/URL/Reset; landmarks, one `h1`, `lang`, real buttons, accessible names on every control, `role=status` announcement, Tab order (speaker box after the selects), focus ring; WCAG AA contrast of composited chip colours |
| `suite-ranking.js` | for eight queries, `python3 query.py Q -n 10 --json --no-semantic` top 10 must overlap the web's top 40 by ≥ 4 (skipped when `data/talks.db` is absent); unambiguous topics rank on-topic first; same query twice → same order |
| `suite-navigation.js` | cold boot < 8 s; no shard fetched up front; a query fetches only its shards; warm query < 2.5 s; hash replaced in place (Back leaves the page); a pasted URL reproduces the view; footer links; then **assembles the site** and re-checks load, search, a transcript fetch, every relative link, no failed requests |

Related: `tools/test_stem.py` (Python vs. JS stemmer over the corpus; needs
node, ~10 s) is the guard for any edit inside the stemmer markers.

## How

```bash
cd tools && python3 build_index.py            # both halves, ~50 s; prints held-back transcripts and the size report
python3 build_index.py -o /tmp/idx            # rebuild elsewhere to diff against the committed one
python3 test_stem.py                          # after touching the stemmer in either language
cd uitest && npm install && node run.js       # all suites, ~4 min; node run.js search filters for a subset
KB_URL=https://ppruchnerovic.github.io/ai-talks-universe/ node run.js navigation   # against production
python3 -m http.server 8765 -d <repo root>    # to poke at the page by hand (a suite run directly expects this port)
tools/assemble_site.sh _site                  # what pages.yml publishes; _site/ is gitignored
```

Invariants and the mistakes a model makes here:

- **Always rebuild both halves together, and commit `search-meta.json` +
  `tindex/` but never `talks.db`.** `n` is the position in `talks.json`; a
  browser index from one build and a database from another disagree silently.
  Output is byte-identical run to run (terms sorted, `generated_at` untouched),
  so a diff after a rebuild shows only real corpus changes — a noisy diff means
  something upstream changed, not the build.
- **`shard_key()` ≡ `shardKeyOf()`, and the stemmers must agree word for
  word.** A mismatch is not an error: the browser asks for a shard the manifest
  does not list and transcript search quietly degrades to metadata hits. Edit
  the stemmer only between its markers, in both files, then run `test_stem.py`.
- **Tokens, never substrings.** `highlight()`, `showMoments()` and every
  scorer go through `tokenize()`/`fieldHit()`; the trap word is `rag` (inside
  `program`, `storage`, `fragment`). Do not "simplify" any of them to
  `includes()` or a bare RegExp.
- **Conference type (`g`, `#f-cat`) and topics (`k`) are filters, never scored
  fields**, in the browser and in `meta_stems()` alike — scoring a venue label
  made "security" match every talk at ten security conferences. `META_FIELDS`
  at `index.html:584` names only the fields `_f` can carry; do not add
  `category` to it.
- **Adding a per-talk key to `search-meta.json`** costs every visitor bytes
  before they type. Keep it tiny (indices, not names — that is why `k` is
  integers), omit it when empty, and watch the size report: over 6 MiB the
  documented remedy is halving `META_DESC_CHARS`, though after two halvings
  the next crossing should move descriptions out of the up-front payload.
- **A new filter or control touches six places:** the markup, `fillFilters()`,
  `filterFn()` and `facetCounts()`, `writeHash()`/`readHash()` (whitelist the
  values), `#clear`, and `suite-filters` round-trip checks. Facet counts
  rewrite option *labels* only; tests and the hash read *values*.
- **`replaceState`, never `pushState`.** `suite-navigation` asserts Back leaves
  the page rather than stepping through keystrokes.
- **Hide with the `hidden` property and keep the `[hidden]` CSS reset.** An
  author `display:` rule on `#more`, `.abs-more`, `#f-tr` or `#f-spoken`
  outranks the UA `[hidden]` rule; that shipped once as "Show more (-16 left)".
- **`w` gates everything transcript-related.** Held-back ASR failures get
  `w=0` and no text in either index; the file stays on disk so the fetcher does
  not re-buy it. Never expose a transcript badge, toggle or moments link from
  any field other than `w`.
- **In the suites, skip rather than fail when a fixture does not exist yet**
  (`L.skip`), but never let a check pass over an empty sample — several checks
  first assert the sample is non-empty for exactly that reason. Anything that
  asserts a cold transcript fetch needs its own page (`TRANSCRIPTS` is
  per-page). Fill `detail` in `L.check` with what was actually seen.
- **`suite-ranking`'s CLI half** needs `data/talks.db` built and runs
  `--no-semantic` so lexical is compared with lexical. If it goes red after a
  corpus change, read ARCHITECTURE.md:883 first — the top-40 window is a
  known-fragile check, not proof the browser broke.
- **Facts the prose has drifted from before, so check the code, not a doc:**
  the page has five sorts (`SORTS = rel/new/title/short/long`), not three;
  `highlight()` is a token walk over `TOKEN_RE_I` comparing each token to the
  query's words, stems and long-stem prefixes — nothing from the query is ever
  compiled into a RegExp (same whole-token guarantee as the old `\b` version);
  the uitest check count is whatever `run.js` tallies and is recorded in
  `STATE.md`, nowhere else.
