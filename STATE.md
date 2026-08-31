# Build state and handoff notes

Working notes for whoever — or whichever session — picks this up next. The
user-facing documentation is `README.md`; this file records what is done, what
is running, what is left, and the decisions that should not be relitigated.

Built by porting the WeAreDevelopers talk knowledge base at
`../presentations/kb/` (see its `README.md` and `STATE.md`) onto a different and
harder data source. The search machinery — SQLite FTS5 + a sharded browser
index, passage-level co-occurrence ranking, the transcript fetcher's three
routes and quota handling — is that design, carried over deliberately. What is
new here is the catalogue layer, because there is no agenda API.

## Where things stand

| Piece | State |
|---|---|
| Registry (`conferences.json`) | Done. 46 conferences, 67 sources, mirrored from `ai-conferences.md`; `check_registry.py` passes. |
| Enumeration (`sync_catalog.py`) | Done. 14,797 videos cached in `data/catalog/`, 6,979 surviving talks. |
| Enrichment (`enrich.py`) | Done for the 2026 scope. **9,598 videos via the Data API**, in one run. See *What the collection runs actually got*. |
| Per-talk markdown | Done. 6,979 files, regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. |
| CLI (`query.py`) | Done, and its ranking was rebalanced — see *Design decisions*. |
| Browser UI (`index.html`) | Done. Conference / category / year facets, passage-level ranking. |
| Browser UI tests (`tools/uitest/`) | **156 checks over 9 suites, 5 failing, none skipped.** The failures are fixtures the bigger corpus outgrew, not the UI — see *Next steps*. |
| Fetcher tests (`tools/test_fetch_transcripts.py`) | Done. 64 offline checks over the pool, the routes, the year selection and the supadata error classes. |
| Claude Code skill | Done — `ai-conference-talks`, in `.claude/skills/`. |
| Transcripts | **182 of 6,979**, from 184 files in `data/transcripts/`; 4 videos are recorded as having no captions. Exact timings throughout: ai-engineer 93, ai-devcon-tessl 66, ai-dev-deeplearning 12, code-with-claude 10, langchain-interrupt 1. Still the long pole, but no longer IP-bound — see *The quota*. |
| Workflows | Written, never run: `pages.yml` (mirror to gh-pages) and `kb-refresh.yml` (weekly re-enumerate). |
| Published site | **Not set up yet.** Nothing has been committed or pushed. |

## What the collection runs actually got

A chained run of the whole pipeline finished on 2026-08-31 from a residential
connection:

| Stage | Result |
|---|---|
| `fetch_transcripts.py --priority 1 --source exact --retry-after 15 --max-rounds 3` | **52 transcripts**, then blocked. Two further rounds 15 minutes apart got nothing — the allowance had not refilled. 0 misses. |
| `enrich.py` (yt-dlp route, no API key) | **369 of 5,816**, then refused. |
| `sync_catalog.py` + `build_index.py` | Clean. |
| `fetch_transcripts.py --source supadata --min-year 2026 --priority 1 --limit 95` | **95 fetched, 0 missed**, every one exact. 96 of the 100 free credits, including the `--probe`. |

Then a `YOUTUBE_API_KEY` turned up, and
`enrich.py --all --min-year 2026 --include-unknown-year` did in one run what the
yt-dlp crawl could not: **9,598 videos enriched**, 7 unavailable, 4,823 skipped
because they were already dated before 2026. That is roughly 200 quota units of
the 10,000 a day, and none of it touched the IP allowance the captions need. The
corpus grew with it, because `scope: "ai"` conferences match on description:
5,816 talks became 6,979.

The unknown-year problem is closed: **3,082 talks without a year became 2**,
which is what `--include-unknown-year` was added for. Everything downstream that
was guessing — year facets, `--min-year` selection, the "is this stale" call on a
talk — now has a date to read. Collection stays scoped to 2026, and that scope
went from 770 talks to **2,159**: most of the dates that arrived were recent, so
the selection filter now selects rather than mostly excluding the unknown.

Then the Supadata free tier was tried against the hardest part of the backlog —
long 2026 practitioner talks, most of them over 20 minutes and so through
Supadata's job-polling path — and returned **95 of 95**. Nothing was charged for
a video with no captions (0%, against the ~4.4% the free routes miss), so a
credit budget needs no headroom: credits ≈ talks, one per talk at any length
under `mode=native`. That settled it and **Supadata Pro is now bought** — $17 a
month, 3,000 credits. Supadata is the primary route for this corpus from here;
the free per-IP routes are the fallback.

The corpus grew with it: **69,665 passages, up from 41,233**. `data/talks.db` is
45.5 MB, `search-meta.json` 5.4 MB, `data/tindex/` 4.2 MB over 27 shards
carrying 13,841 terms from 184 transcripts.

Coverage as it stands: 5,138 descriptions, 6,977 of 6,979 with a year, 2,591
with a speaker, 3,185 with YouTube tags, 182 with a transcript. Of the 2,159
talks in the 2026 scope, **151 have a transcript and 2,004 are pending** — 616
priority 1, 849 priority 2, 539 priority 3.

**This IP is still flagged for captions.** `fetch_transcripts.py --probe` will
tell you when it has recovered; it takes hours, and switching networks buys a
fresh window immediately. Metadata no longer competes for it — the Data API is a
separate allowance, which is the whole reason to prefer it.

That now costs a run its cheap half rather than the run itself: with Pro
credits, the per-IP allowance gates nothing, it only decides how much of a batch
comes back free. The one metadata gap left is the 4,823 videos the year filter
skipped, and those cost quota units rather than a sitting.

## Next steps, in order

1. **Commit and push.** Nothing is committed yet. Then enable GitHub Pages on
   the `gh-pages` branch; `pages.yml` mirrors `main` into it on every push.
2. **Fix the five UI checks the corpus outgrew.** None of them is a UI
   regression — rebuilding the index at the old 1,200-character clip fails the
   same five. `moments` picks a title word from a transcribed talk and expects
   that talk in its own result set; the word it picked is "agent", which
   thousands of talks now answer, so the card is nowhere near the first page —
   the fixture needs a word that is still distinctive at 6,979 talks. `controls`
   needs one description short enough not to overflow the clamp to prove its
   negative case, and the Data API's descriptions are uniformly long. `ranking`
   asserts 4 of the CLI's top 10 land in the web's top 40 and now gets 0 for
   "kubernetes" and "multi agent" and 1 for "inference": at this size there are
   far more than 40 good title matches, so two correct rankings can disagree
   completely. Both were re-read by hand and both are still good, which is the
   argument for changing what the check measures rather than the ranking.
3. **Re-run the UI tests** after any collection run: `cd tools/uitest && node run.js`.
   They degrade to `SKIP` rather than failing when a fixture has not been
   collected yet, so a green run on a thin corpus is weaker evidence than a
   green run on a full one — read the skip count, not just the failures.
4. **Run the 2026 extraction.** 2,004 talks in the 2026 scope still have no
   transcript (616 of them priority 1). Supadata Pro is bought, so this is no
   longer a grind against an allowance — 3,000 credits a month covers the whole
   backlog with about a thousand to spare, and the measured rate is one credit
   per talk. It is deliberately left for its own session; see *Handoff*.
5. Re-check the conferences that came back thin: `owasp-global-appsec` (2
   talks), `tedai-vienna` (6), `apple-wwdc` (7), `meta-connect` (9). Some are
   genuinely small playlists; some may need a better source or a looser filter.
   `fully-connected-wandb` came back at 49 and is off this list.
6. Backfill the pre-2026 descriptions if anything ever wants them: the year
   filter skipped 4,823 videos, which is one `enrich.py --all` without
   `--min-year` and about a hundred quota units. Nothing depends on it — the
   2026 scope is a selection policy, not a coverage target.

## Handoff — running the 2026 extraction

Everything below is set up; the run itself is the only thing left.

```bash
cd tools
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --priority 1   # the 616 practitioner talks first
.venv/bin/python sync_catalog.py && .venv/bin/python build_index.py
```

- **Prefer `--source exact` once `--probe` says the IP has recovered.** It runs
  the free routes first and only falls through to Supadata, so credits are spent
  on what the IP quota could not cover rather than on everything.
- **Deps live in a venv at `tools/.venv`**, not in the system interpreter, so
  use `tools/.venv/bin/python`. `.gitignore` already covers `tools/.venv/`.
- **`SUPADATA_API_KEY` and `YOUTUBE_API_KEY` are exported in `~/.bash_profile`,
  which a non-login shell does not read.** A tool-driven or CI shell sees
  neither and the run silently degrades to the free routes. Source it
  explicitly. This cost real debugging time.
- **`sync_catalog.py` then `build_index.py` afterwards**, in that order:
  the first inlines the new transcripts into the markdown, the second rebuilds
  `talks.db` and the browser index. Neither touches the network.
- **No need to ration inside the month.** 3,000 credits against 2,004 pending
  talks at one credit each leaves ~1,000 spare.

## The quota — read this before a transcript run

Carried over from the WeAreDevelopers corpus, where it cost a day to establish,
and confirmed again here (blocked at 52 on a residential connection, 37 the
next day).

| Egress | Fetched before the block |
|---|---|
| Corporate NAT (Zscaler) | 235, then 52 in a later sitting |
| Residential ISP | 25, and 52 then 37 here |
| Mobile carrier | 22 |

**yt-dlp metadata extraction draws on the same allowance.** This was suspected
and is now measured: with captions already exhausted at 52, `enrich.py`'s
yt-dlp route managed 369 videos before being refused outright. So the two stages
compete, and a metadata crawl costs you a transcript sitting. Do not run them
together, and prefer the Data API for metadata — a different service with its
own published quota, which does not touch this at all.

Slowing down does not help. What is metered is an allowance per egress IP that
refills over hours, and both free exact routes draw on the same one — yt-dlp is
a fallback for a *refusal*, not for an exhausted quota. Corporate NAT addresses
front many users and carry a larger allowance. Recovery is slow and uneven.

So the only two levers are more IPs, or a route that does not use ours, and
`fetch_transcripts.py` now implements both. `--proxy` / `--proxy-file` builds a
pool in which each proxy is an `Egress` with its own strikes, fetch count and
bench deadline; a block benches that one identity for `--proxy-cooldown`
minutes and the round carries on down the rest, so N usable residential IPs is
worth about N sittings. `SUPADATA_API_KEY` adds a fourth route with *exact*
timings fetched from their IPs, which the quota therefore does not touch — the
first route here that is both exact and unmetered, and the only one that would
work from CI.

**Supadata is the lever that was taken, and it is live.** `SUPADATA_API_KEY`
(Pro, 3,000 credits a month) and `YOUTUBE_API_KEY` are both exported in
`~/.bash_profile`; no proxy pool was bought. The trial settled the question with
numbers: 95 of 95, no misses, 0% charged for a captionless video against ~4.4%
on the free routes, so credits ≈ talks and a budget needs no headroom. Against
that, the free routes yield ~35 a sitting from this IP and the two of them draw
the *same* per-IP allowance, so they do not compose — clearing 2,000 talks that
way is two months of once-daily runs for about three hours of actual fetching.
What is being bought is the calendar, not the throughput.

Three properties in there are load-bearing and are covered by the offline
checks written alongside them (fake egresses and a faked HTTP layer, so they
need no network):

- **A block is retried on another identity, not deferred to the next round.**
  Otherwise every identity, as it hit its limit, would cost a talk it never
  actually refused. The retry budget is one attempt per identity plus one for
  the off-IP routes, capped at 8.
- **A block never becomes an estimate.** Under `--source exact`, a spent pool
  falls through to Supadata and then stops; it does not quietly return kome's
  interpolated timings. An unfetched talk is recoverable, a mislabelled
  transcript is not.
- **Supadata's 206 is a miss, its 402/429 is not.** "No captions for this
  video" is a fact about the video and gets written to `_misses.json`; "your
  account is out of credits" retires the route for the run and leaves the talk
  retryable. Account-level limits are also why 429 there is *not* treated as an
  IP block: benching an identity would not help.

Hence `--retry-after MINUTES`, which parks the run and resumes; each round
re-derives its work from disk, so a blocked round costs only time. A block is
**not** written to `_misses.json` — that file means "this video has no
captions". Keeping the two apart is what lets a plain rerun collect everything a
block skipped.

Do not reach for the YouTube Data API for captions: `captions.download` requires
OAuth *and* permission to edit the video, so third-party talks return 403.
(The Data API *is* the right tool for descriptions — that is `enrich.py`.)

## Design decisions worth not relitigating

- **Two files describe the conferences, on purpose.** `ai-conferences.md` is the
  human curation — why a source is worth having, what is gated, what was
  rejected and why. `conferences.json` is what the tools read.
  `check_registry.py` compares them per conference block, not per URL, because a
  block usually lists both a channel and the playlists on it and the registry
  deliberately takes only one of the two.

- **The AI filter is a property of the conference, not of the corpus.** A
  dedicated AI conference contributes everything (`scope: "all"`); a general one
  contributes only what matches `atu.AI_RE` (`scope: "ai"`). The regex allows a
  trailing hyphen but not a leading one, so "AI-native" and "ML-powered" match
  while "chai-latte" and "html-first" do not. That asymmetry is load-bearing;
  the first version rejected "The AI-native SDLC".

- **Enumeration is flat, and details are a separate stage.** A flat listing is
  one request per 100 videos; a full extraction is ~1.4s *each* and draws on the
  same IP reputation the transcript fetch needs. Fusing them would make a weekly
  refresh a multi-hour crawl.

- **A source that returns nothing keeps its cached videos.** `yt-dlp` exits 0
  with no entries when it is throttled — a successful-looking run that would
  otherwise delete a conference. There is a second backstop:
  `sync_catalog.py` refuses to write a corpus more than 10% smaller than the
  last one without `--allow-shrink`.

- **Talks are keyed by YouTube video id, but the indexes use a dense integer.**
  Repeating an 11-character id in every posting would roughly treble the browser
  index, and FTS5 needs an integer rowid anyway. `build_index.py` assigns `n`
  from the position in `talks.json` (which `sync_catalog.py` sorts
  deterministically). `n` never leaves the index it was built for; everything
  that outlives a build — transcripts, markdown — is keyed by video id, and both
  index halves are always rebuilt together. `index.html` reads `data-n` for
  ranking and `t.v` for the transcript URL.

- **Speaker extraction is two-pass, and the second pass is what makes the first
  safe.** No per-title rule can tell "Lian Li" from "Rare Disease Applications"
  — both are capitalised words in a delimiter-separated title. What tells them
  apart is the rest of the conference: a *name* appearing in more than a tenth
  of its talks is the host or the brand, and a *word* appearing across more than
  6% of a conference's candidate names is a topic label, because real names do
  not share vocabulary. Both filters are applied per conference. Coverage was
  32% from titles alone and 37% once the descriptions arrived, since many
  channels write "Speaker: …" in the description.

- **Collection is scoped to 2026; the corpus is not.** `enrich.py` and
  `fetch_transcripts.py` both take `--year` / `--min-year` /
  `--include-unknown-year`, and the standing intent is `--min-year 2026`: an
  allowance that refills over hours should not be spent on talks that have gone
  stale. It filters *selection only* — `sync_catalog.py` still derives every
  year into `talks.json` and `query.py --year` still reads them, because
  enumeration costs nothing. On enrichment, add `--include-unknown-year`:
  enrichment is what resolves a year, so without it the talks that have none can
  never become known 2026 talks. There were 3,082 of them; the run that carried
  the flag left 2. `year_of()` moved to `atu.py` when the
  second and third tool needed it.

- **Enrichment takes conferences whole, in priority order.** Every run is a
  partial run, so what a blocked run leaves behind is a design choice. Taking a
  slice of each conference would leave forty conferences 6% enriched and none of
  them answerable; taking them whole means "what was said at AI Engineer" works
  completely while the rest wait. The first run predated this and spent all 369
  of its budget on `ai-engineer` purely because that was registry order —
  `enrich.py` now sorts by `priority` first.

- **`query.py` normalises each layer before blending them, and this was a
  correctness fix, not a tuning preference.** `bm25()` is only comparable within
  one table. A passage is a ~25-word document, so almost any match in one scores
  near the maximum — a raw passage score (~8) lands on top of the best possible
  title score (~9) and then accumulates over four moments. Blended raw, *every*
  query returned the same handful of long workshops, the talks that happen to
  have been transcribed, however well another talk's title answered it: the CLI
  top hit for "kubernetes" was a workshop that mentions it in passing. The
  WeAreDevelopers corpus hid this because all 358 talks had transcripts. Now
  each layer is normalised to [0,1] across the result set and blended
  `1.0 × meta + 0.7 × transcript`, so a talk's own metadata leads and what was
  said on stage is strong corroborating evidence rather than an override.
  Transcript-only hits still surface — `query.py postgres` still finds the talk
  that only says it out loud, at rank 4.

- **The two rankers are compared at the web's top 40, not its top 10.** They
  disagree about ordering by design: `talks.db` tokenises with Porter stemming,
  the browser matches token prefixes, and their field weights differ. On a
  corpus this size "kubernetes" has dozens of near-identical title matches, so
  which ten come first is a coin toss between two good answers. Measured over
  the suite's eight queries, the CLI's top 10 lands in the web's top 10 between
  0 and 9 times, and in its top 40 between 4 and 10 times. The check asserts 4
  at 40. Both rankings were inspected by hand at the time and both are good.
  That range no longer holds: at 6,979 talks it is 0 to 10 and three of the
  eight queries fail, because a common term now has hundreds of good title
  matches and 40 is too narrow a window to catch any of them. The rankings are
  still both good — what needs rethinking is the check.

- **`data/talks.db` is gitignored.** It is derived, rebuilds in seconds, and
  would otherwise push megabytes of churning binary into every commit.
  `search-meta.json` and `tindex/` *are* committed — GitHub Pages can only serve
  files that exist in the repo.

- **Descriptions are clipped to 600 characters in `search-meta.json`**
  (`build_index.py: META_DESC_CHARS`) and only there. The full text stays in
  `talks.json`, the markdown and `talks.db`. Every visitor downloads that file
  before typing anything, and YouTube descriptions run long and repetitive — the
  same channel boilerplate under 400 talks. `sync_catalog.clean_description`
  already strips link-only lines, hashtag walls and "Subscribe" lines, which
  would otherwise be indexed as if the speaker had said them.
  The extrapolation held: at 5,816 talks the file was 1.6 MB with no
  descriptions and 2.0 MB with 369 of them, and enrichment took it to 7.3 MB at
  6,979 talks with 5,138 — past the 6 MB line that was set as the trigger, so
  the clip halved and it came back to 5.4 MB. Description coverage is still only
  74%, so this will need looking at again; the 6 MB trigger stands.
  GitHub Pages gzips; the local test server does not, which is why
  `suite-navigation` allows 8 seconds for a cold load.

- **Hiding a control needs more than `hidden`.** `index.html` hides `#more`,
  `.abs-more` and `#f-tr` by setting the `hidden` property, but any author rule
  that sets `display` on one of them outranks the UA stylesheet's `[hidden]` —
  so the element stays on screen while the script believes it is gone. This
  shipped in the corpus this was ported from: a four-hit search offered "Show
  more (-16 left)". A `[hidden] { display: none !important; }` reset covers all
  three and `suite-controls` guards it. Do not remove the reset.

- **Ranking matches tokens, never substrings.** Two bugs were found by testing
  in the original and must not be reintroduced: without IDF weighting a generic
  term outranks a rare one, and with raw substring matching "rust" matches every
  talk containing "t*rust*". Here the trap word is **"rag"**, which sits inside
  "program", "storage" and "fragment" — `suite-search` asserts it is never
  highlighted inside them. `showMoments()` and `highlight()` are the two places
  that historically slipped back to substrings; both go through `tokenize()` and
  `\b`-anchored matching.

## Numbers to refresh when the corpus changes

`README.md` states 6,979 talks / 46 conferences / 14,797 enumerated, and how
many of them are 2026; this file states transcript, description, year, tag and
speaker coverage, the per-conference transcript split, the 2026 pending backlog
and its priority breakdown, the passage count, and the sizes of `talks.db`,
`search-meta.json` and `tindex/`. `sync_catalog.py` prints the coverage at the
end of a run and `build_index.py` prints the passage count and the sizes.

## Not done

- **No semantic/vector search.** BM25 plus an agent reading the top hits has
  covered the query patterns so far. If "find talks that mean X without saying
  X" becomes a real need, embeddings over the transcript passages are the next
  step — the chunking in `segments` is already the right granularity.
- **No cross-conference deduplication of the same talk.** A speaker who gives
  the same talk at three conferences appears three times. That is arguably
  correct (three recordings, three audiences), but a "same talk elsewhere" link
  would be useful. Video ids are already deduplicated globally, so this is only
  about *re-recorded* talks.
- **No per-source health report.** `sync_catalog.py` prints drops per
  conference, but nothing tracks a source that has quietly gone stale for
  months. The `stale: true` flag written into `data/catalog/<conf>.json` is the
  hook for it.
- **`enrich.py` has no `--refetch` pacing story for the whole corpus.** It is
  fine incrementally; a full re-fetch of 6,979 descriptions via yt-dlp is an
  hour and should really only be done with an API key.
