# Open items

What is not done, in one place. Each entry is a sentence or two and a pointer
to the section of `HISTORY.md` that has the background; the background is not
repeated here. When an item is finished, its write-up goes into `HISTORY.md`
as part of that session's section and the line here is **deleted**, not struck
through — a struck line is how the previous state file grew to 1,800 lines.

Current state is `STATE.md`; the rules and the shape of the system are
`ARCHITECTURE.md`.

## Cheap, and worth doing next

- **Read twenty random titles per topic.** The topic facet is keyword rules,
  and the numbers (`sync_catalog.py` prints the distribution) say how many
  talks each rule catches, not whether it caught the right ones. Nobody has
  yet sat down with `query.py --topic <name> -n 20` for each of the fifteen
  and marked what is mis-shelved; that reading is what tunes a phrase list.
  The likeliest offenders are the broad ones — *Enterprise adoption &
  strategy*, *Science, healthcare & applied ML*. *The topic facet — built*.

- **26 Supadata transcripts carry double-escaped HTML entities** — `&amp;#39;`
  where the caption has an apostrophe. A search hole (the stemmer sees `amp`
  and `39`) and a display one in the markdown. Fix is local and costs no
  credit: `html.unescape` over `segments[].text` in `fetch_transcripts.save()`,
  and one pass over the 26 files on disk, then `sync_catalog.py` and
  `build_index.py`. Found 2026-09-02 — *The bug list, worked* → *Still open,
  deliberately*.
- **`_misses.json` records the exception class, not the reason.** `reason` is
  `"LookupError"` on every entry; the fact is in `detail`. Either rename the
  fields or make the post-run check assert on `detail`. *Closing the 422* →
  *`_misses.json` records the exception class, not the reason*.
- **`--probe` reports a verdict, not a cause.** A TLS-inspecting proxy
  (Zscaler) answering a JSON API with an HTML interstitial at HTTP 200 was
  reported as `BLOCKED — spent`, and cost an hour. The HTML-at-200 case now
  says so once; the probe still cannot tell a proxy interception from a
  YouTube block. *Closing the 422* → *The run was blocked by a proxy*.

- **The semantic layer is talk-level plus chunk anchors; the browser has none.**
  `query.py` fuses model2vec vectors when `tools/install_semantic.sh` has run;
  `index.html` cannot, since a query must be embedded client-side (the 30 MB
  model, or a hosted call). Chunk-level *ranking* (not only anchoring) and a
  cross-encoder rerank are the two obvious next steps if recall on paraphrased
  questions is still short. *Search enrichment*.
- **`--lang` needs a `language` column** in `talks.db`: a `DB_SCHEMA_VERSION`
  bump (which also invalidates `data/embeddings/`) for one filter whose main
  use is excluding the twelve `hi` mis-detections the badge already flags.
  *Search enrichment*.
- **Did-you-mean for query typos**: an `fts5vocab` table and `difflib` over
  its stems (31,810 load in 50 ms, a match ~30 ms). Schema bump; today
  relaxation drops the absent word and says so. *Search enrichment*.
- **A fuzzy `--speaker`**: a trigram FTS5 table over title + speakers, the
  query's trigrams OR-ed and ranked by bm25 (0.14 s to build, 1–2 ms a query).
  Schema bump; `check_speaker()`'s difflib suggestion is the substitute.
  *Search enrichment*.
- **`--related <id>`**: the talk's top tf-idf stems as one OR query through
  `rank()`, df from `fts5vocab`. Schema bump; the mechanism is 10 ms, choosing
  the terms is the work. *Search enrichment*.
- **`--near N` for bare queries**: `together_q` as `NEAR(...)`. No bump, but
  it changes ranking, so the `ranking` suite decides. *Search enrichment*.
- **`--year 2024-2025` as a range** is not in argparse; `--min-year`/`--max-year`
  or a repeated `--year` cover it and the skill cites those. An hour in the
  parser. *Search enrichment*.
- **`uitest`'s assembled-site helper waits a fixed 10 s** for its throwaway
  server while copying 199 MB of transcripts to /tmp; under load the
  navigation suite sees `ERR_CONNECTION_REFUSED` and passes on re-run. Poll
  the port instead. *Search enrichment*.

## Curation calls — a decision, not a fix

- **`owasp-global-appsec`: 28 enumerated, 2 kept.** The 26 dropped are the
  AppSec programme — threat modelling, PKI, security champions. Same argument
  that gave the WeAreDevelopers seed `"scope": "all"`: is a security
  conference's non-AI half worth having? Nobody has decided.
- **Candidate conferences, unverified:** NDSS, IEEE S&P, MLSys, CVPR post
  full sessions to YouTube and would extend the corpus towards academic
  work. VivaTech and GitNation were checked and rejected. *The seven
  conferences added on 2026-09-01*.

## Known and accepted — flagged so nobody pays for them by accident

- **Three transcripts are English with badly degraded ASR** (`hbShI0crCOg`,
  `6NC9laD5OHY`, `RS4DmYTvHIo`, labelled `de`): coherent for a minute, then
  fragments. The wpm floor deliberately does not reach them — a threshold that
  would sweep up two real Japanese workshops and an 8.8-hour livestream.
  Needs a different signal (fragment ratio, mean cue length) or a three-id
  deny-list. *The wpm floor, and the doc_len it did not fix*.
- **Route 2 (`yt-dlp`) passes `--sub-langs` limited to `LANGUAGES`**, so a
  video whose only track is off-list writes no caption file and becomes a
  permanent miss on the free route. The fix is fetching every language on
  every video, which is bandwidth on all of them. Bites only on our-IP runs.
- **`count` drifts by one in three catalogs** (`ai-devcon-tessl`,
  `ai-engineer`, `qcon-infoq`): three videos were copied in by hand in
  `ec68e00a` without bumping it. Only `--refresh` rewrites those files, so
  the next weekly run clears it.
- **The `refresh_report.py` gate is advisory.** A reviewer can merge a
  regressed branch, and a local `--refresh` from a throttled connection still
  writes hollow records into `data/catalog/`; the check is on the derived
  corpus, not on the cache. *The CI refresh regression*.
- **The `ranking` browser suite measures corpus size as much as ranking
  quality.** It asserts 4 of the CLI's top 10 land in the web's top 40; three
  queries have started and stopped failing on their own as the corpus grew,
  and the rankings were good on both sides every time. Green today (margins
  8–10 of 10), and still the one open test-quality item — what it measures
  needs rethinking, not its threshold. *Design decisions* → *The two rankers
  are compared at the web's top 40*.
- **The pre-2026 descriptions are not backfilled.** 4,823 videos were skipped
  by the year filter; one `enrich.py --all` without `--min-year` and about a
  hundred quota units. Nothing depends on it — 2026 is a selection policy,
  not a coverage target — and 503 of those videos are now below the corpus
  floor anyway.

## Not built, by choice

- **No cross-conference deduplication of the same talk.** A speaker who gives
  one talk at three conferences appears three times. Arguably correct (three
  recordings, three audiences); a "same talk elsewhere" link would be useful.
  Video ids are already deduplicated globally, so this is only about
  re-recorded talks.
- **No per-source health report.** `sync_catalog.py` prints drops per
  conference, but nothing tracks a source that has quietly gone stale for
  months. The `stale: true` flag in `data/catalog/<conf>.json` is the hook.
- **`enrich.py` has no pacing story for a whole-corpus yt-dlp refetch.** Fine
  incrementally; a full re-fetch of every description via yt-dlp is an hour
  and should only ever be done with a Data API key, where it is 4% of a day.
- **Publishing lighter transcripts.** When transcripts alone approach the
  Pages ceiling, strip `duration` and the second decimal of `start` at
  publish time — ~30% of the bytes, without touching `data/transcripts/` on
  `main`. A `build_index.py --site` step later, not now. *Review of
  2026-09-02* → *B. The published site is the whole repository*.
