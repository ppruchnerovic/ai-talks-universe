# Data model: the registry and the corpus

## What

This domain is the *shape* of the knowledge base: which conferences are read,
what one talk record is, and the four files that carry the same corpus for
different readers. It owns:

- **The registry** — `conferences.json` (what the tools read) and its human
  twin `ai-conferences.md` (why each source is there). Always edited together;
  `tools/check_registry.py` fails when they drift.
- **The talk record** — the 25 keys every entry in `data/talks.json` carries,
  where each comes from, and the derive-time rules that decide what survives
  (year floor, AI filter, duration), who spoke (`speakers`) and what it is
  about (`topics`, `category`).
- **The four representations** — `talks/<conf>/<id>-<slug>.md`,
  `data/talks.json`, `data/talks.csv`, `data/talks.db` — which is derived from
  which, and which tool writes each.
- **`tools/atu.py`** — the shared module every tool imports: path constants,
  registry/catalog/transcript loaders, id and URL helpers, the AI-relevance
  regex, the topic rules, the year resolver, the stemmer.

It does **not** own: enumerating YouTube or merging caches
(`catalog-sync.md`), fetching transcripts (`transcripts.md`), the SQLite/FTS
schema and the browser index (`search-cli.md`, `search-browser.md`,
`semantic.md`), or publishing (`publishing.md`). Caches under `data/` are
described here only as far as the derivation needs them.

One sentence of the architecture that everything below depends on: **the
corpus is re-derived offline from committed caches.** `python3 sync_catalog.py`
(no `--refresh`) touches no network and produces byte-identical output, so
every rule in this spec is reversible without a fetch.

## Where

### The registry

| File | What it is |
|---|---|
| `/home/peter/git/ai-talks-universe/conferences.json` | The registry. Top level: `version`, `note`, `min_year` (2023, the corpus floor), `fields` (prose docs for the non-obvious keys), `conferences[]` (53 entries). |
| `/home/peter/git/ai-talks-universe/ai-conferences.md` | Human curation. One `### <Conference>` block per conference under `## <section>` headings; each block lists Site, YouTube channel/playlists, availability and the reasoning. Sections `## Academic research…` and `## Checked but weak sources…` are ignored by the checker. |
| `/home/peter/git/ai-talks-universe/tools/check_registry.py` | Compares the two. `markdown_blocks()` (line 33) maps each `###` heading to the YouTube URLs under it; `key()` (line 51) reduces a URL to `list:<id>` or `chan:@handle` so tracking params and `/videos` suffixes do not matter. Flags a documented block whose URLs the registry reads *none* of, and a registered YouTube source no block mentions. `videos` and `infoq` sources are skipped (no YouTube URL to match). Exit 1 on drift. Runs in CI (`.github/workflows/kb-refresh.yml:68`). |

A conference entry (the key is **`sources`**, not "listings"):

| Key | Required | Meaning |
|---|---|---|
| `slug` | yes | Registry id, unique (`atu.load_registry` exits on a duplicate). Becomes `talks[].conference`, the `talks/<slug>/` directory and `data/catalog/<slug>.json`. |
| `name` | yes | Display name -> `conference_name`. |
| `category` | yes | One of five venue labels: `Practitioner AI conferences`, `General software conferences`, `Security conferences`, `Vendor events`, `Business & industry events`. The browser calls this "Conference type"; the field, CSV column and `--category` flag keep the name `category`. |
| `site`, `availability`, `blurb` | yes | `site` -> `conference_site`; `availability` is `free`/`partial`/`gated` -> copied to the record. |
| `scope` | yes | `all` keeps every session; `ai` keeps only what `atu.looks_ai()` matches on title + description + tags. 25 `all`, 28 `ai`. |
| `priority` | yes | 1 = transcribe first. Copied to the record; read by `enrich.py` and `fetch_transcripts.py` for ordering. |
| `min_duration` | yes | Seconds. A video with a shorter *or unknown* duration is dropped. |
| `min_year` | no | Per-conference override of the top-level floor. **`null` means no floor** (camlis, defcon-ai-village, bsides-lv keep their back catalogue). Presence of the key is what counts, not its value. |
| `match` | no | Regex (case-insensitive) that title+description must match. Used by 5 conferences whose channel carries more than the conference (`ai-dev-deeplearning: "AI Dev"`, `ray-summit`, `dotai`, `fully-connected-wandb`, `usenix-security`). |
| `exclude` | no | Regex against the title. Supported by `keep_video()`; **no entry currently uses it**. |
| `sources[]` | yes | The listings, below. |

A source entry:

| Key | Meaning |
|---|---|
| `type` | `channel` (25), `playlist` (58), `videos` (1: a seed file), `infoq` (1: infoq.com pages). |
| `url` | Identity of the source. `merge_source()` deletes a cached video only when the source with the same `url` no longer lists it. For a seed it is the agenda URL, for documentation only. |
| `label` | Becomes the talk's `edition` (and the catalog record's `label`). |
| `year` | Set when a playlist is one edition; overrides every other year signal (`atu.year_of` reads it first). |
| `first` | Channel only: page at most N entries deep. Channels list newest first, so it is a recency cap. |
| `seed` | `videos` only: filename under `data/seeds/`. |
| `scope`, `min_duration`, `match`, `exclude`, `min_year` | Per-source overrides of the conference rule. This is how the WeAreDevelopers seed carries `"scope": "all", "min_duration": 0` while the same conference's channel stays `ai`-filtered, and how the three `lf-ai-dev` playlists are `all` inside an `ai` conference. |

### The talk record

`data/talks.json` is `{generated_at, source, ai_filter, min_year, conferences[{slug,name,category}], count, talks[]}`. `atu.load_talks()` returns just `talks`. Every record has all 25 keys (built at `tools/sync_catalog.py:827-858`, `build_talks()`):

| Key | Type | Source |
|---|---|---|
| `id`, `video_id` | str | Identical. An 11-char YouTube id, or `iq-<slug>` for a presentation that exists only on infoq.com (`atu.INFOQ_ID_PREFIX`). |
| `slug` | str | `atu.slugify(title)`: NFKD -> ASCII -> `[a-z0-9-]`, cut at 60 chars on a hyphen, `"untitled"` if empty. |
| `title` | str | Catalog title, whitespace-folded at enumeration. |
| `description` | str | `clean_description()` of the catalog/seed/InfoQ description: link-only lines, hashtag walls and "Subscribe/Follow us…" lines removed. `""` when none. |
| `speakers` | list[str] | See *Who gave the talk*. `[]` when none identified. |
| `conference`, `conference_name`, `category`, `conference_site`, `availability`, `priority` | | Copied from the registry conference. |
| `edition` | str/null | The source `label` (playlist name, seed label, InfoQ edition name). |
| `year` | int/null | `atu.year_of(catalog record)`: explicit `year` (source or seed) > year in `published_at` > first non-span year in `label` > in `title` > `null`. Not the upload year when an edition says otherwise. |
| `channel` | str/null | Uploader channel; `"InfoQ"` for InfoQ records. |
| `duration_min`, `duration_s` | int/null | `duration_s` from the listing; `duration_min = round(duration_s/60)`. |
| `published_at` | str/null | ISO timestamp. Upload time from enrichment; for a seed, when the session was given; for InfoQ, the page's date. |
| `tags` | list[str] | `clean_tags()` (whitespace folded, empties dropped). InfoQ-only records have `[]`. |
| `topics` | list[str] | 0..n of the fifteen `atu.TOPIC_NAMES`, sorted. See *What a talk is about*. |
| `youtube_url` | str/null | `https://www.youtube.com/watch?v=<id>` only if `atu.is_youtube_id(id)`; **null for `iq-` records**. |
| `url` | str/null | Canonical link: `youtube_url`, else `page_url`, else null (`atu.watch_url`). |
| `page_url` | str/null | InfoQ presentation page when there is one. |
| `source_url` | str | The registry source `url` that listed the video. |
| `has_details` | bool | `details_at` is stamped on the catalog record (enriched, seeded or InfoQ-fetched). |

There is **no transcript field in `talks.json`**. Transcript existence is
`data/transcripts/<id>.json` existing (`atu.transcript_path`). The markdown
front matter's `transcript: true|false` is computed at render time from that.

Record order is deterministic (`sync_catalog.py:865-867`): registry order,
then year descending, then title lowercased, then id. `build_index.py` assigns
its dense integer `n` from this position, so the order is load-bearing.

Duplicates: the same video id in two conferences' catalogues is kept by the
**first conference in registry order** and counted as `duplicate` in the
other's drop report.

### The four representations

| File | Written by | Derived from | Committed |
|---|---|---|---|
| `data/talks.json` | `sync_catalog.py` | `data/catalog/*.json` + `data/seeds/*.json` + `data/infoq/*.json` + the registry | yes — the source of truth |
| `data/talks.csv` | `sync_catalog.py`, same run | `talks.json` records via `csv_row()` (`sync_catalog.py:984`): 14 columns (`CSV_FIELDS`, line 980); `speakers` joined with `", "`, `topics` with `"; "` | yes |
| `talks/<conf>/<id>-<slug>.md` | `sync_catalog.py`, same run; the whole `talks/` tree is deleted and rewritten | one record + `data/transcripts/<id>.json` inlined as ~45 s paragraphs with `&t=` deep links (`transcript_block()`, line 911) | yes |
| `data/talks.db` | `build_index.py`; rebuilt automatically by `atu.connect()` when `atu.db_stale()` says so | `talks.json` + `transcripts/` | **no** (gitignored; schema pinned by `atu.DB_SCHEMA_VERSION = 6`) |

Why four (README "Why four representations"): JSON/CSV are exact and complete
for scripts; the markdown is git-diffable per talk and lets an agent read one
file for the whole talk; the DB is a throwaway index for ranked CLI search.
The browser's `search-meta.json` + `tindex/` are a fifth, derived from
`talks.json` + transcripts by `build_index.py` — see `search-browser.md`.

Markdown layout (`MD_TEMPLATE`, `sync_catalog.py:872`): YAML front matter
(`id`, `title`, `slug`, `conference`, `conference_name`, `category`,
`edition`, `year`, `speakers`, `channel`, `duration_min`, `published_at`,
`video_id`, `url`, `youtube_url`, `tags`, `topics`, `transcript`), then
`# title`, a bold speaker line ("Speaker not identified" when empty), a
backticked meta line, `#tags`, the watch/site links, `## Description`, and
`## Transcript` with a `*N words · source: X (lang, exact|estimated timings)*`
header when a transcript file exists. `generated_at` in `talks.json` is kept
from the previous file when nothing else changed (`generated_at()`, line
1014), so a no-op rebuild is byte-identical.

### The caches the derivation reads

| Path | Shape | Who writes | Role in derivation |
|---|---|---|---|
| `data/catalog/<slug>.json` | `{slug, name, enumerated_at, sources[{url,label,year,count,stale?}], count, videos{<id>: {video_id, title, duration_s, channel, label, year, source_url, description?, published_at?, tags?, details_at?, page_url?, infoq_at?…}}}` | `sync_catalog.py --refresh` (listing), `enrich.py` (details), `infoq.py` (onto matched records), `sync_seeds()`/`sync_infoq()` (folded in every run) | The only input `build_talks()` reads per conference. |
| `data/seeds/<name>.json` | `{conference, channel, label, year, source, generated_at, count, videos[{video_id, title, duration_s, description, speakers, tags, published_at, session_page}]}` | `import_kb.py` | `enumerate_seed()` (line 127) turns each into a catalog record; `SEED_FIELDS` (line 124) win over enrichment because `details_at` is stamped. Only one today: `wearedevelopers-wwc26.json`, 358 talks. |
| `data/infoq/<edition>.json` | `{edition, name, year, fetched_at, count, talks{<slug>: {slug, page_url, title, description, speakers, has_transcript, matched_youtube?, …}}}` | `infoq.py` | `enumerate_infoq()` (line 179) emits `iq-` records for talks with no `matched_youtube`; `claim_for_infoq()` (line 219) folds an `iq-` record onto a YouTube record whose title now matches, moving its transcript. |
| `data/transcripts/<id>.json` | `{video_id, title, conference, language, auto_generated, source, timing: exact|estimated, word_count, segments[{start, duration, text}]}` (compact JSON) | `fetch_transcripts.py`, `infoq.py`, `import_kb.py` | Inlined into the markdown; indexed by `build_index.py`. `_misses.json` sits beside them — never count transcripts by filename prefix. |

Depth on these lives in `catalog-sync.md` and `transcripts.md`.

### Deriving the corpus: what survives

`keep_video()` (`tools/sync_catalog.py:626`), once per catalog video, with a
source's overrides applied via `rule(key) = src.get(key, conf.get(key))`. In
order, and the reason string is what the run's drop report prints:

1. `untitled` — no title (a hollow record from a private/deleted video).
2. `short` / `no-duration` — `duration_s` below `min_duration`, or missing. Unknown duration **fails**. `min_duration: 0` switches the check off.
3. `match` — title+description does not match the `match` regex.
4. `exclude` — title matches the `exclude` regex.
5. `not-ai` — conference/source `scope == "ai"` and `atu.looks_ai(title, description, tags)` is false. Skipped entirely with `--no-ai-filter`.
6. `pre-<floor>` — `atu.year_of(v)` is known and below the floor. Unknown year **passes**. Floor resolution: source `min_year` if the key is present, else conference `min_year` if present, else registry `min_year`; `--no-min-year` sets it to None. Checked last so the report shows what the floor alone cost.

A record with `infoq_at` is governed by the conference's `infoq` source's
rules regardless of which source first listed it (`build_talks()`, line 765).

`atu.AI_RE` (`tools/atu.py:403`) is the AI vocabulary: word-boundary matching,
a trailing hyphen allowed ("AI-native" matches) but no leading one
("chai-latte" does not). `AI_TERMS` (line 384) is the list.

Two guards after the filter, both in `sync_catalog.py`: a source that returns
nothing keeps its cached videos (marked `stale` in the catalog's `sources`),
and `check_not_shrinking()` (line 991) refuses to write a corpus more than 10%
smaller than the previous `talks.json` without `--allow-shrink`.

### Who gave the talk

`build_talks()` (`sync_catalog.py:788-822`), per conference:

1. If the catalog record already has `speakers` (a seed or InfoQ stated them), they are used verbatim and **skip both filters below**.
2. Else `speakers_from_description()` (line 511): NFKC-normalise, find a `Speaker(s):` / `Presenter(s):` / `Presented by` / `By:` heading (`DESC_SPEAKER_RE`, line 428); names on that line split on `,`/`&`/`and`, or on the bulleted/bare lines under it until the first non-name.
3. Else `speakers_from_title()` (line 488): strip a leading `[TAG]`; try `… by A and B` at the end (`BY_NAME_RE`); else split on `—`/`–`/`|`/`•`/`·`/` - ` and test each segment.
4. `name_like()` (line 443) accepts a segment only if: after cutting at the first `,` or `(`, it is 3-42 chars, no digits, 2-4 words, every word capitalised (`[A-ZÀ-Þ][a-zà-ÿ'’-]*.?`, particles like "van"/"de" allowed after the first), no word in `NOT_A_NAME` (roles, brands, topic words; line 402) or in `blocked_words(conf)` (every word of the conference name, slug and source labels; line 554). `names_in()` accepts `A & B` only if **every** part is a name.
5. Second pass, per conference over the guessed names: a name on more than `max(4, 10% of candidates)` talks is the host/brand; a word on more than `max(5, 6% of all candidate names)` is a topic word, and every name containing it is dropped.

### What a talk is about

- `category` is inherited from the conference; it is a venue, never a subject, and enters no ranker.
- `topics` = `atu.topics_of(title, tags', description')` (`tools/atu.py:662`), where `tags'` and `description'` have the conference's boilerplate removed first — by the caller, `sync_catalog.py`; `atu` has no notion of boilerplate and takes no ignore list. Scoring (`topic_scores`, line 648): any phrase of a topic in the title = 2; each *distinct* phrase of that topic in tags+description = 1; assigned at score >= 2 (`TITLE_HIT`, `TOPIC_THRESHOLD`, lines 606-607). Transcripts are never read.
- The phrase lists are `atu.TOPICS` (line 436): fifteen `(name, [regex phrases])`, compiled with the same boundaries as `AI_RE` (`_phrase_re`, line 618). Deliberate boundaries: bare "enterprise" never fires *Enterprise adoption*; a bare tool name ("Copilot", "Cursor") never fires *AI in the SDLC*; "prompt" excludes "prompt injection".
- Boilerplate (`sync_catalog.py:708-737`): for a conference with >= `BOILERPLATE_MIN_TALKS` (10) candidates, a description line (>= `BOILERPLATE_MIN_CHARS`, 40) repeated verbatim under more than `BOILERPLATE_LINE_SHARE` (10%) of its talks, or a tag on more than `BOILERPLATE_TAG_SHARE` (30%) of them, is stripped before scoring (`boilerplate()`, `without_lines()`; call site at line 818-826). Titles are never stripped. All four thresholds live in `sync_catalog.py`; nothing in `atu.py` knows about them.

### `tools/atu.py` — what is exported

| Symbol | Line | Purpose |
|---|---|---|
| `ROOT, DATA, TALKS_MD, CATALOG, TRANSCRIPTS, TINDEX, REGISTRY, TALKS_JSON, TALKS_CSV, SEARCH_META, TALKS_DB` | 16-27 | Absolute paths resolved from the file location; tools run from anywhere. |
| `WATCH` | 29 | `https://www.youtube.com/watch?v={vid}`. |
| `load_registry()` | 32 | Parse `conferences.json`; exit on missing file or duplicate slug. |
| `load_talks()` | 735 | `talks.json["talks"]`; exits if the file is missing. |
| `catalog_path(slug)`, `load_catalog(slug)` | 742, 746 | Catalog file; missing -> `{"slug", "videos": {}}`. |
| `transcript_path(vid)`, `load_transcript(vid)` | 754, 758 | Transcript file; missing -> None. |
| `write_json(path, obj, compact=False)` | 766 | Pretty (indent 2, trailing newline) or compact; creates parents. |
| `slugify(text, max_len=60)` | 87 | Filename slug. |
| `video_id(url)`, `VIDEO_ID_RE` | 96-103 | Extract an 11-char id from a YouTube URL. |
| `is_youtube_id(vid)`, `YOUTUBE_ID_RE`, `INFOQ_ID_PREFIX` | 110-123 | An `iq-` id is never a YouTube id even when it is 11 chars. |
| `watch_url(vid, page_url=None)` | 126 | Canonical link, or None. |
| `looks_ai(*texts)`, `AI_RE`, `AI_TERMS` | 384-407 | The AI filter. |
| `TOPICS`, `TOPIC_NAMES`, `TITLE_HIT`, `TOPIC_THRESHOLD`, `topic_scores()`, `topics_of()` | 436-665 | The topic facet. `topic_scores(title, tags, description)` / `topics_of(...)` take exactly three arguments; the caller strips boilerplate before calling. |
| `year_of(record)`, `year_in_text()`, `YEAR_RE`, `YEAR_SPAN_RE` | 672-704 | Year resolution; a year opening a span ("2015-2035") is skipped. |
| `add_year_args(ap)`, `year_wanted(year, args)` | 707-732 | `--year/--min-year/--include-unknown-year`, shared by `enrich.py` and `fetch_transcripts.py`. |
| `segment_plain_text(lines, total_seconds)` | 138 | Untimed prose -> estimated-timing segments (kome, InfoQ). |
| `STOPWORDS`, `tokenize()`, `TOKEN_RE` | 45, 185 | Tokeniser shared by the indexers. |
| `stem()`, `stems()` | 290, 361 | Porter stemmer (memoised); must agree with the JS copy in `index.html`. |
| `SYNONYMS` | 67 | Query-time synonym groups for both rankers. |
| `DB_SCHEMA_VERSION`, `db_stale()`, `connect()` | 800-849 | Staleness and auto-rebuild of `talks.db` (see `search-cli.md`). |
| `human_size()`, `decimal_size()` | 776, 852 | Binary (MiB) vs decimal labels; do not change the divisor. |

### Tests for this domain

| File | Runs | Checks |
|---|---|---|
| `tools/test_speakers.py` | `cd tools && python3 test_speakers.py`, 0.1 s | Every title/description speaker shape the corpus has; a brand, role or joined non-name is rejected. |
| `tools/test_topics.py` | `cd tools && python3 test_topics.py`, 0.1 s, no corpus | Each topic fires on a title naming it and not on one that does not; the rule boundaries; the scoring arithmetic; every phrase regex compiles and matches its own canonical phrase; the boilerplate stripping. |
| `tools/test_stem.py` | `cd tools && python3 test_stem.py`, ~6-10 s, reads the corpus, needs `node` | `atu.stem()` agrees with the JavaScript stemmer on every corpus token. Relevant here only because `stems()` is what the browser index is keyed on. |
| `tools/check_registry.py` | instant | Registry vs markdown. |

All are plain scripts with a `check(name, cond)` helper: exit 1 on any FAIL.

## How

Adding or changing a conference:

```bash
# edit conferences.json AND ai-conferences.md together
cd tools
python3 check_registry.py                                     # must exit 0
python3 enrich.py --all -c <slug> --include-unknown-year      # scope "ai" only: the filter reads descriptions
python3 sync_catalog.py --refresh -c <slug>                   # enumerate one, derive all
python3 build_index.py
```

Rebuilding the corpus after a rule change (no network): `cd tools && python3 sync_catalog.py && python3 build_index.py`.

Rules a model gets wrong:

- **Never hand-edit `talks.json`, `talks.csv` or anything under `talks/`.** They are overwritten whole by the next `sync_catalog.py` run (the `talks/` tree is `rmtree`d). Change the registry, a seed, or a rule in `sync_catalog.py`/`atu.py`, then re-derive. The same goes for `data/catalog/`: an edit there survives a refresh only until `enrich.py` or a re-enumeration touches the record.
- **Both registry files, every time.** Adding a source to `conferences.json` without a `###` block in `ai-conferences.md` (or vice versa) fails `check_registry.py`, which runs in CI. The block must contain the same channel handle or playlist id; prose alone is not enough for YouTube sources.
- **`min_year: null` is a value, not an absence.** To keep a conference's back catalogue, write the key with `null`; omitting it inherits the 2023 floor.
- **Do not build a youtube.com link from `id` without `atu.is_youtube_id()`.** `iq-` ids can be exactly 11 URL-safe characters. Use `url`/`youtube_url` from the record, or `atu.watch_url()`.
- **Transcript presence is a file, not a field.** Check `atu.transcript_path(id).exists()` (or the markdown's `transcript:` line, which is derived from it). Count transcripts by exact id: `_misses.json` and 48 ids beginning with `_` break any prefix filter.
- **A derive-time rule is only measurable on the drop report.** `sync_catalog.py` prints per-conference drop reasons and the topic distribution on every run; after changing `AI_TERMS`, `TOPICS`, `NOT_A_NAME` or a threshold, read that output for a conference that suddenly moved, and run `test_topics.py` / `test_speakers.py`. The sanity threshold is the 10% shrink guard; anything smaller passes silently.
- **`speakers` and `topics` come from the record's stated data first.** A seed's or InfoQ's `speakers` list bypasses the name filter entirely, so a bad name in a seed goes straight into a field weighted 4x in both rankers. Fix it in the seed, not with a filter.
- **`year` is the edition's year, not the upload year.** A playlist `year` in the registry beats `published_at`; adding a per-edition playlist is the way to correct a mis-dated batch, not editing records.
- **Preserve the record order and the byte-identity.** Anything that makes `sync_catalog.py` output differ between two no-op runs (a wall clock, a set iterated unsorted) is a bug: it dirties a 15 MB tracked file and defeats `git diff` as the change log.
