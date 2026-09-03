# Catalog sync: enumerating, enriching, deriving

## What

This domain turns the registry (`conferences.json`) into the corpus
(`data/talks.json`, `data/talks.csv`, `talks/**.md`). It owns four tools and
three cache directories:

| Stage | Tool | Network | Writes |
|---|---|---|---|
| Enumerate | `sync_catalog.py --refresh` | yt-dlp flat listing, one page per 100 videos, no caption endpoint | `data/catalog/<conf>.json` |
| Enrich | `enrich.py` | YouTube Data API v3 (or yt-dlp per video) | descriptions, dates, tags into the same catalog files |
| InfoQ | `infoq.py` | infoq.com HTML at 3 s/page | `data/infoq/<edition>.json`, `data/transcripts/iq-*.json`, and onto matched records in `data/catalog/qcon-infoq.json` |
| Import | `import_kb.py` | none | `data/seeds/<name>.json`, `data/transcripts/<vid>.json` |
| Derive | `sync_catalog.py` (no flags) | none | `data/talks.json`, `data/talks.csv`, `talks/<conf>/<id>-<slug>.md` |

Responsibilities:

- Every video a source ever listed is cached in `data/catalog/`; the corpus is
  a *filtered, derived* view of those caches plus seeds and the InfoQ cache.
- Derive is offline and idempotent: with unchanged caches, a run rewrites
  `talks.json`, `talks.csv` and `talks/` byte-identically (including
  `generated_at`, which only advances when the body changes). A git diff after
  `--refresh` therefore shows exactly what the conferences changed.
- Speakers (title/description heuristics), topics (`atu.topics_of`), the
  AI-relevance filter (`atu.looks_ai`) and the year floor are all applied at
  derive time, so any of them can be changed and re-run without a fetch.

Not responsible for: transcript fetching (see `transcripts.md`), index
building (`build_index.py`, see `search-cli.md` / `search-browser.md`), the
registry schema and talk-record semantics (see `data-model.md`), CI workflows
(see `publishing.md`).

Numbers in the code's docstrings lag: `sync_catalog.py:4` says "46
conferences"; the registry today has 53 conferences and 85 sources (83
YouTube listings, one `videos` seed, one `infoq` source).

## Where

### `tools/sync_catalog.py` (1138 lines)

| Symbol | Line | Purpose |
|---|---|---|
| `enumerate_source(src)` | 69 | `yt-dlp --flat-playlist --dump-json` on one URL; `src.first` becomes `--playlist-end`. Keeps only 11-char ids, drops nested playlist entries. Returns records with `video_id,title,duration_s,channel,label,year,source_url`. Empty result on timeout (600 s) or throttle. |
| `enumerate_seed(src, conf)` | 127 | Reads `data/seeds/<src.seed>`; copies `SEED_FIELDS` (`description,speakers,tags,published_at,session_page`) and stamps `details_at` = seed `generated_at` so enrich.py skips these. |
| `enumerate_infoq(src)` | 179 | Reads every `data/infoq/*.json`; emits only talks with `matched_youtube: false` (the `iq-` ids), `channel: "InfoQ"`, `details_at` from the cache. Copies `INFOQ_FIELDS` (`description,speakers,published_at,page_url,video_url`). |
| `claim_for_infoq(videos, found)` | 219 | An `iq-` talk whose title now matches a YouTube record in the catalog is folded onto it (metadata via `infoq.enrich_existing`, transcript copied and re-keyed) and not emitted. Idempotent. |
| `merge_source(videos, src, found)` | 301 | Deletes videos this `source_url` no longer lists; carries `description,published_at,tags,details_at` from the previous record when the listing lacks them; if `infoq_at` is set, carries all of `INFOQ_CLAIMED` (line 175) over the listing's values. |
| `sync_seeds(reg)` / `sync_infoq(reg)` | 330 / 262 | Fold `videos` / `infoq` sources into their catalogs on every run. Write only if the catalog changed. A missing/empty InfoQ cache keeps the previous iq- records and marks the source `stale: true`. |
| `refresh_conference(conf, pace)` | 358 | `--refresh` per conference: enumerate each non-offline source, merge, write catalog with `enumerated_at`. A source returning nothing keeps its cached videos and is marked `stale`. |
| `speakers_from_title` / `speakers_from_description` / `name_like` | 488 / 511 / 443 | The speaker heuristics; `blocked_words(conf)` (554) blocks the conference's own name words. Tested by `tools/test_speakers.py`. |
| `clean_description` / `clean_tags` | 572 / 601 | Strip link-only lines, hashtag walls, "Subscribe…" lines; fold whitespace inside tags (self-healing on every derive). |
| `keep_video(v, conf, ai_filter, src, floor)` | 626 | The filter: untitled → `min_duration` (unknown duration fails) → `match`/`exclude` regex → `scope == "ai"` AI test → year floor (unknown year passes). Source rules override conference rules; `min_year: null` means no floor. Returns `(keep, reason)`. |
| `boilerplate` / `without_lines` | 714 / 734 | Per-conference: description lines repeated verbatim on >10% of talks and tags on >30% are removed before topic scoring (needs ≥10 talks). |
| `build_talks(reg, only, ai_filter, floor)` | 740 | Per conference: filter, dedupe across conferences (first in registry order wins), two-pass speaker filter (a name on >10% of talks or sharing a word with >6% of names is dropped; stated speakers bypass), topics, and the talk record (827–858). Records governed by the `infoq` source's rules when `infoq_at` is set (765). |
| `render_md` / `MD_TEMPLATE` / `transcript_block` | 944 / 872 / 911 | One markdown file per talk; transcript inlined as ~45 s paragraphs, deep-linked with `&t=` only when `youtube_url` exists. |
| `CSV_FIELDS` / `csv_row` | 980 | The CSV columns (`url`, not `youtube_url`). |
| `check_not_shrinking` | 991 | Refuses to write if the new count is <90% of the committed `talks.json` count unless `--allow-shrink`. |
| `generated_at(body)` | 1014 | Keeps the previous stamp when the serialized body is unchanged. |
| `main` | 1046 | Flags below. `--refresh -c` limits enumeration; derive is *always* over every conference (1081). |

CLI: `--refresh`, `-c/--conference SLUG` (repeatable), `--no-ai-filter`,
`--no-min-year`, `--allow-shrink`, `--pace SECONDS` (max jitter between source
enumerations, default 1.5).

Output paths: `atu.TALKS_JSON`, `atu.TALKS_CSV`, `atu.TALKS_MD` (the `talks/`
tree is `rmtree`'d and rebuilt each run, line 1108).

### `tools/enrich.py` (320 lines)

| Symbol | Line | Purpose |
|---|---|---|
| `fetch_api(ids, key)` | 74 | `videos.list?part=snippet,contentDetails`, 50 ids per call, 1 quota unit. Returns `description,published_at,tags,duration_s,channel`. Exits on 403 (quota/restricted key). |
| `fetch_ytdlp(vid)` | 125 | Fallback: full `yt-dlp -J` per video (~1.4 s). Raises `BlockedError` on `BLOCK_MARKERS` (line 122: "Sign in to confirm", 429). |
| `select(reg, args)` | 143 | Which videos need details: the current corpus (`talks.json`) by default, or every cached video with `--all`; skips records with `details_at` unless `--refetch`; whole conferences in priority order; year filter via `atu.year_wanted`. |
| `apply_details(cat, vid, det)` | 196 | Writes `description` (CR/CRLF normalised), `published_at`, `tags` (whitespace-folded), `duration_s`, `channel`, `details_at` onto the catalog record. |
| `main` | 226 | Per conference: API route in batches of 50, or `enrich_ytdlp` (283, threaded, paced, stops the run on the first block). Catalog written after each conference. Videos the API does not return (private/deleted/blocked) get `details_at` + empty description so they are not retried. |

CLI: `-c SLUG`, `--all`, `--priority N`, `--limit N`, `--refetch`, `--year YYYY`
/ `--min-year YYYY` (exclusive), `--include-unknown-year`, `--workers` (yt-dlp
only, default 2), `--min-delay`/`--max-delay`, `--api-key` (default
`$YOUTUBE_API_KEY`).

Cost: key is free, 10,000 units/day. Corpus ≈ 190 units, `--all` over the
whole catalog ≈ 354. The key does nothing for transcripts.

### `tools/infoq.py` (544 lines)

| Symbol | Line | Purpose |
|---|---|---|
| `CONF = "qcon-infoq"`, `PACE = 3.0`, `CACHE = data/infoq` | 68–80 | Hard-wired: this route feeds one registry entry; robots.txt asks for `Crawl-delay: 3`. |
| `editions()` | 150 | Parses the edition filter tags off `/presentations/`; an edition slug must end in `-20YY` (that year is every talk's year). InfoQ exposes only recent editions. |
| `enumerate_edition(slug, pace)` | 169 | Pages `/<edition>/presentations/<offset>/` 12 at a time until a page adds nothing; `has_transcript` from `data-transcript`. |
| `parse_talk(page, rec)` | 260 | Title (`og:title`), speakers (ld+json `author`), description = `og:description` + bio, `duration_s` (ISO 8601), `published_at` (`datePublished`), `video_url`, `transcript_lines`. |
| `parse_transcript(page)` | 234 | `div#presentationNotes`, nested-div aware (`div_inner`, 111); keeps h2/h3 headings, drops InfoQ furniture (`FURNITURE_RE`), splits paragraphs into sentences (`SENTENCE_RE`). |
| `title_key` / `match_existing` / `catalog_index` | 297 / 318 / 331 | Match onto YouTube records by full-length slug; exact match wins; prefix match only if the shared part is ≥ `MIN_PREFIX` (30) chars and exactly one candidate. iq- records are never match targets. |
| `save_transcript(vid, talk)` | 353 | `atu.segment_plain_text` interpolates starts across `duration_s`; writes `source: "infoq"`, `timing: "estimated"`, `auto_generated: false`. |
| `enrich_existing(rec, talk, edition, stamp)` | 384 | What a match writes onto the YouTube record: `description, speakers, label, year, page_url, infoq_url, published_at, duration_s, details_at, infoq_at`. |
| `run_edition(...)` | 419 | Per edition: enumerate, skip cached talks (re-fetch only if flagged `has_transcript` and the transcript file is missing), fetch, match, write transcript, update cache. Catalog written after every edition. |

CLI: `--year YYYY` (repeatable; edition year, not publish date), `--edition SLUG`,
`--list`, `--limit N` (per edition), `--refetch`, `--dry-run`, `--pace`.

Tests: `tools/test_infoq.py` — `cd tools && python3 test_infoq.py`, ~48 offline
checks: the matcher (ambiguity → no match, short prefix → no match, exact beats
prefix), page parsing on an inline fixture (nested div, furniture, headings,
sentence split), segment interpolation, id/url helpers, edition parsing, and
the sync_catalog fold-in (`merge_source` keeps `INFOQ_CLAIMED`, missing cache
keeps iq- records, `claim_for_infoq` is idempotent).

### `tools/import_kb.py` (212 lines)

Offline import of a conference whose recordings are unlisted on YouTube, from
a corpus built against the conference's agenda API (default
`../presentations/kb`, the WeAreDevelopers World Congress 2026).

| Symbol | Line | Purpose |
|---|---|---|
| `read_kb(kb)` | 50 | Reads `<kb>/data/talks.json` and locates `<kb>/data/transcripts/`. |
| `duration_s(talk, tr)` | 60 | End of the last caption cue, falling back to the scheduled slot. |
| `seed_record(talk, tr)` | 88 | One seed video: `video_id,title,duration_s,description,speakers,tags` (track + tags), `published_at` (= `starts_at`, when the talk was given), `session_page`. |
| `convert_transcript(...)` | 104 | Re-keys a kb transcript to the YouTube id, adds `imported_from`. Never overwrites an existing transcript file. |
| `main` | 120 | `--kb PATH`, `--conference SLUG`, `--name` (seed file), `--label`, `--year`, `--channel` (default: most common channel in the catalog), `--origin`, `--dry-run`. |

### Cache formats

**`data/catalog/<conf>.json`** (written by `refresh_conference`, `sync_seeds`,
`sync_infoq`, `enrich.py`, `infoq.py`):

```
{ slug, name, enumerated_at, count,
  sources: [ {url, label, year, count, type?, stale?} ],
  videos: { "<video_id>": record } }        # sorted by id
```

A video record (all keys seen in the caches today):

| Field | From | Notes |
|---|---|---|
| `video_id`, `title`, `duration_s`, `channel`, `label`, `year`, `source_url` | enumeration | `label`/`year` are the source's; `year` null for a channel listing |
| `description`, `published_at`, `tags`, `details_at` | enrich.py | `details_at` set means "do not enrich again"; enrich.py stamps unavailable videos too |
| `speakers`, `session_page` | seed | seed fields win over enrichment |
| `speakers`, `page_url`, `infoq_url`, `video_url`, `infoq_at` | infoq.py | `infoq_at` marks a YouTube record InfoQ claimed; `merge_source` then preserves `INFOQ_CLAIMED` across a `--refresh` |

`year_of(v)` (`atu.py:709`) resolves the year as: `year` → year in
`published_at` → year in `label` → year in `title`.

**`data/seeds/<name>.json`** (written by `import_kb.py`, read by
`enumerate_seed`):

```
{ conference, channel, label, year, source, generated_at, count,
  videos: [ {video_id, title, duration_s, description, speakers, tags,
             published_at, session_page} ] }
```

The registry source that reads it: `{"type": "videos", "seed":
"<name>.json", "url": ..., "label": ..., "year": ..., "scope": "all",
"min_duration": 0}` — the `url` is only an identifier for `source_url`.

**`data/infoq/<edition>.json`** (written by `run_edition`, read by
`enumerate_infoq`):

```
{ edition, name, year, fetched_at, count,
  talks: { "<infoq-slug>": {slug, page_url, has_transcript, title, description,
            speakers, duration_s, published_at, video_url,
            id,                # YouTube id if matched, else "iq-<slug>"
            matched_youtube, edition, edition_name, year,
            transcript_words, fetched_at} } }
```

Only `matched_youtube: false` talks reach the corpus from this file; matched
ones already live on their YouTube record in `data/catalog/qcon-infoq.json`.

Transcript file format (shared with `transcripts.md`): `{video_id, title,
conference, language, auto_generated, source, timing, word_count, segments:
[{start, duration, text}]}`; InfoQ writes `source: "infoq"`, `timing:
"estimated"`.

### Related

- `tools/atu.py`: `load_registry`, `load_catalog`/`catalog_path`, `write_json`
  (indent 2, or compact for transcripts), `year_of`, `add_year_args`/`year_wanted`,
  `looks_ai`, `topics_of`, `segment_plain_text`, `is_youtube_id`, `INFOQ_ID_PREFIX`.
- `tools/check_registry.py`: `conferences.json` must agree with `ai-conferences.md`.
- `tools/refresh_report.py`: field-level diff of a rebuilt corpus vs the
  committed one; used by `kb-refresh.yml` (which runs `sync_catalog.py --refresh`,
  `enrich.py --limit 4000`, `sync_catalog.py` — see `publishing.md`).

## How

Standard rebuild (from `tools/`):

```bash
python3 sync_catalog.py --refresh        # ~10 min, network
python3 enrich.py                        # needs YOUTUBE_API_KEY, else slow yt-dlp
python3 sync_catalog.py                  # offline derive
python3 build_index.py
```

Adding a conference (registry schema in `data-model.md`):

1. Edit `conferences.json` and `ai-conferences.md` together; `python3 check_registry.py`.
   Prefer per-edition playlists (with `year`) over a whole channel for vendors;
   use `first: N` as a recency cap on channels.
2. `python3 sync_catalog.py --refresh -c <slug>` — enumerates and derives.
3. If the conference is `scope: "ai"`: `python3 enrich.py --all -c <slug>
   --include-unknown-year`, then `python3 sync_catalog.py` again. The AI
   filter reads descriptions, so titles that never say "AI" are dropped
   until this runs. STATE.md lists enrich *before* the first `--refresh`;
   that cannot work for a new slug (enrich.py reads the catalog, which does
   not exist yet) — enumerate first, as here.
4. `python3 build_index.py`; transcripts per `transcripts.md`.
5. Unlisted recordings: write a seed (`import_kb.py` or by hand in the seed
   format above) and register a `type: "videos"` source; it is folded in on
   every run without `--refresh`.

Invariants and caveats:

- `sync_catalog.py` without `--refresh` must leave a clean tree clean. If a
  no-op run dirties `talks.json` or `talks/`, something upstream is
  non-deterministic (dict order, wall clock, an un-normalised field) — fix
  that, do not commit the churn.
- `-c` scopes enumeration only. Derive always runs over every conference, and
  the shrink guard compares against the committed `talks.json`; a partial
  catalog checkout will trip it. `--allow-shrink` is for a real drop only.
- Never hand-edit `data/catalog/` for metadata fixes: `enrich.py --refetch`
  or the next `--refresh` merge will overwrite it. Fix the derive step
  (`clean_*`, speaker rules, `keep_video`) instead; those are re-applied on
  every run.
- `details_at` is the "already enriched" flag for every route (Data API,
  seed, InfoQ). Clearing it is how to force a re-enrich of one record;
  `--refetch` does it for a selection.
- InfoQ-claimed records (`infoq_at`) are governed by the `infoq` source's
  rules (`scope: "all"`) at derive time, and their InfoQ fields survive a
  channel `--refresh`. Do not "simplify" `merge_source` by dropping
  `INFOQ_CLAIMED`; `test_infoq.py` covers this.
- `infoq.py` de-duplicates against the catalog as of the run; a talk that
  reaches the YouTube channel later is folded by `claim_for_infoq` on the
  next sync. Do not lower `--pace` below 3.
- Do not run yt-dlp-route `enrich.py` alongside a transcript fetch: it spends
  the same per-IP reputation. With `YOUTUBE_API_KEY` set there is no such
  conflict.
- Year-scoped enrich runs need `--include-unknown-year`, otherwise they can
  only re-select talks whose year is already known.
- `talks/` is deleted and rewritten every derive; anything placed there by
  hand is lost.
