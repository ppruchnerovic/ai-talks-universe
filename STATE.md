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
| Registry (`conferences.json`) | Done. 46 conferences, 68 sources — 67 YouTube listings and one `"type": "videos"` seed — mirrored from `ai-conferences.md`; `check_registry.py` passes. |
| Enumeration (`sync_catalog.py`) | Done. 15,157 videos cached in `data/catalog/`, 7,351 surviving talks. 14,800 of them enumerated from YouTube, 357 seeded — see *The WeAreDevelopers import*. |
| Enrichment (`enrich.py`) | Done for the 2026 scope. **9,598 videos via the Data API**, in one run. See *What the collection runs actually got*. |
| Per-talk markdown | Done. 7,351 files, regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. |
| CLI (`query.py`) | Done, and its ranking was rebalanced — see *Design decisions*. |
| Browser UI (`index.html`) | Done. Conference / category / year facets, passage-level ranking. |
| Browser UI tests (`tools/uitest/`) | **170 checks over 9 suites, 1 failing, none skipped** (re-run after the 2026 extraction). `ranking`'s "inference" failure fixed itself as the transcript corpus grew, which is the instability the check has always had; the one left is a `controls` fixture — see *Next steps*. |
| Fetcher tests (`tools/test_fetch_transcripts.py`) | Done. **71 offline checks** over the pool, the routes, the year selection, the supadata error classes and the off-IP lease rule. |
| Claude Code skill | Done — `ai-conference-talks`, in `.claude/skills/`. |
| Transcripts | **2,525 of 7,351**, all exact timings, over 30 conferences. ai-engineer 540, wearedevelopers 433, pydata 205, microsoft-build 187, kubecon 151, ndc 149, ai-devcon-tessl 132, qcon-infoq 106, devoxx 79, owasp-genai 73. **The whole 2026 scope is done**: of 2,520 talks, 2,493 have a transcript, 27 have no captions to fetch, 0 pending. What is left is pre-2026 and deliberately unfetched — see *Collection is scoped to 2026*. |
| Imports (`import_kb.py`) | Done for WeAreDevelopers World Congress 2026: 358 talks and their transcripts, from `../presentations/kb`. Offline and rerunnable. |
| Workflows | Both run. `pages.yml` mirrors `main` into `gh-pages` on push, verified live. `kb-refresh.yml` now **opens a pull request** instead of committing to `main`, after the run that did — see *The CI refresh regression*. |
| Published site | **Live** at <https://ppruchnerovic.github.io/ai-talks-universe/>, served from `gh-pages`, which `pages.yml` mirrors from `main` on every push. |

## What the collection runs actually got

A chained run of the whole pipeline finished on 2026-08-31 from a residential
connection:

| Stage | Result |
|---|---|
| `fetch_transcripts.py --priority 1 --source exact --retry-after 15 --max-rounds 3` | **52 transcripts**, then blocked. Two further rounds 15 minutes apart got nothing — the allowance had not refilled. 0 misses. |
| `enrich.py` (yt-dlp route, no API key) | **369 of 5,816**, then refused. |
| `sync_catalog.py` + `build_index.py` | Clean. |
| `fetch_transcripts.py --source supadata --min-year 2026 --priority 1 --limit 95` | **95 fetched, 0 missed**, every one exact. 96 of the 100 free credits, including the `--probe`. |
| `fetch_transcripts.py --source supadata --min-year 2026 --priority 1` (Pro) | **614 fetched, 1 missed** of 615 selected, every one exact. No block, no credit error. This cleared the 2026 priority-1 backlog. |
| `fetch_transcripts.py --source supadata --min-year 2026 --priority 3 --workers 32` | **1,227 fetched, 22 missed** in under six minutes. Cleared the whole 2026 scope — see *The 2026 extraction*. |

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

The corpus grew with it: **69,665 passages, up from 41,233**. At that point
`data/talks.db` was 45.5 MB, `search-meta.json` 5.4 MB and `data/tindex/` 4.2 MB
over 27 shards carrying 13,841 terms from 184 transcripts.

## The 2026 extraction, and the run that was 80× too slow

The remaining 1,391 talks were fetched on 2026-08-31 in **under six minutes**.
The first attempt at the same work was quoting **7.7 hours**, and the gap was
entirely on this side of the wire — same key, same network, same API.

It started as `--source exact --min-year 2026 --priority 3`, which managed 3
talks a minute. Three things were serialising it, and only the first is
obvious:

- **The egress lease pinned every worker to one identity.** `attempt()` leases
  an `Egress` per talk, which is exactly right when an IP allowance is the
  scarce thing — two workers down one IP spend it twice as fast for no extra
  throughput. But Supadata egresses from *their* IPs, so with the pool at its
  usual single direct entry the lease made `--workers` a lie: 2 workers, one
  request in flight. The 614-talk priority-1 run above was serial for the same
  reason and nobody noticed, because it still beat the free routes.
- **`--min-delay`/`--max-delay` paced every talk 3-7 seconds** against an
  allowance the Supadata route does not draw on.
- **`--source exact` paid for two refusals per talk** — a blocked
  `youtube-transcript-api` call and a yt-dlp subprocess — before falling
  through. The `strikes >= 3` shortcut that would have stopped re-trying a
  dead route applies only to `--source auto`, not to `exact`.

So `uses_our_ip(source)` now decides all three: a supadata/kome-only run leases
no identity and skips the pacing. `spent()` had to learn it too, or an idle
pool would read as "still has options" and the round would never end.

**Making 429 non-fatal was the prerequisite, not a nicety.** It used to retire
the Supadata route for the whole run, alongside 401 and 402 — reasonable when
one request is in flight, useless the moment there are 32, since a rate limit
is the one account-level refusal that waiting *does* fix. It now backs off and
retries, and a 429 that outlasts the backoff raises `BlockedError`. That second
half fixes a real hazard rather than a slow one: the old path raised
`LookupError`, so the talk in flight was written to `_misses.json` — the file
that means *this video has no captions*. A rate limit was being recorded as a
permanent fact about a video.

Measured, at 12 workers and then 32, with no 429 at either:

| Configuration | Rate |
|---|---|
| `--source exact`, default pacing (as shipped) | ~3 / min |
| `--source supadata --workers 12` | ~30 / min |
| `--source supadata --workers 32` | **~250 / min** |

1,227 fetched, 22 missed, no block and no credit error. The ceiling was never
found — 32 is where looking stopped, not where it broke. Seven checks were
added to `test_fetch_transcripts.py` for the lease rule and both 429 paths;
that suite is 71 now and needs no network.

Every one of the 27 misses is a fact about the video, checked rather than
assumed: 13 have no captions, 10 return `403 "This video requires channel
membership to access"`, 4 are the older yt-dlp no-subtitles entries. One was
verified against the API by hand to be sure the concurrency was not
manufacturing them.

A thing to know about this directory: **48 YouTube ids begin with an
underscore**, and `_misses.json` lives beside the transcripts. Any code that
separates them by filename prefix silently drops 48 talks. Nothing in `tools/`
does — they all address transcripts by exact video id — but an ad-hoc counting
script written during this run did, and reported 2,477 where the corpus had
2,525.

Coverage as it stands, after the 2026 extraction, the priority-1 run and the
CI merge:
5,557 descriptions, 7,349 of 7,351 with a year, 2,947 with a speaker, 3,587
with YouTube tags, **2,525 with a transcript**. **491,282 passages**, up from
197,099; `data/talks.db` 161.6 MB, `search-meta.json` 5.8 MB (unmoved — it
carries descriptions, not transcripts, and the 6 MB trigger still stands),
`data/tindex/` **34.2 MB** over 27 shards carrying 40,927 terms. Of the 2,520
talks in the 2026 scope, **2,493 have a transcript, 27 have no captions, and
none are pending**.

## The WeAreDevelopers import

The corpus this repo was ported from — `../presentations/kb` — holds the 358
recorded talks of WeAreDevelopers World Congress 2026, each with an exact-timing
transcript, harvested from the congress agenda API. None of it was here. The
check that settled why: of those 358 video ids, **1** appears anywhere in the
14,797 videos enumeration had found, and that one turned up because it was also
posted normally.

The recordings are on `@_wearedevs`, but not on its `/videos` tab. Unlisted
videos are reachable by link and by nothing else, so this was never a paging cap
(`first: 700`) or the AI filter — no depth of enumeration would have found them.
What knew the ids was the agenda, and the agenda had already been harvested.

So `import_kb.py` reads that corpus and writes two things, with no network at
all: `data/seeds/wearedevelopers-wwc26.json`, and one transcript per talk
re-keyed from the kb's own talk id to the YouTube video id. The registry gains a
source of `"type": "videos"` pointing at the seed, and `sync_catalog.py` folds
seeds in on **every** run rather than only under `--refresh`, because reading a
seed is reading a file in the repo.

What it added: **7,336 talks, up from 6,979** — the whole congress, all 358,
each with abstract, stated speakers, agenda tags and an exact transcript, which
no other conference here can say. Passages went to **172,376**, and at that
point `data/talks.db` was 74.5 MB, `search-meta.json` 5.7 MB and
`data/tindex/` 11.8 MB over 27 shards.

The first pass let the conference's own filters run over the seed and took 242
of the 358 — 110 dropped as not-AI, 6 as too short. That was reverted on the
call that the dropped ones are worth having: they are the congress's security,
testing, reliability and platform sessions, which is exactly the material an AI
engineer needs and which happens not to say "AI" in the abstract. The six short
ones are real lightning talks, 2 to 5 minutes, not stings.

Five decisions inside it, none of them free:

- **The seed overrides the conference's filters, rather than the conference
  changing scope.** Flipping `wearedevelopers` to `"scope": "all"` would also
  have admitted ~450 unrelated uploads from its channel listing, which spans
  2018 to 2026 and is not a programme. So `keep_video` now resolves `scope`,
  `min_duration`, `match` and `exclude` from the source first and the
  conference second, and only the seed carries the override.
- **`published_at` is when the talk was *given*.** The agenda knows the session
  start; it does not know when the video was uploaded. Everywhere else in the
  corpus that field is a YouTube upload time, so this is the one place the two
  are not the same thing.
- **The seed's fields beat enrichment.** Its records are stamped `details_at`,
  so `enrich.py` skips them and the programme committee's abstract is not later
  overwritten with the channel boilerplate YouTube carries under these talks.
  `--refetch` still forces it.
- **Duration is the last caption cue, not the slot.** The agenda's
  `duration_min` is the scheduled slot, rounded to 15 minutes and including
  changeover. It survives the seed's `min_duration: 0`, since a duration is
  read on every card and deep-linked against, not only filtered on.

**This IP is still flagged for captions.** `fetch_transcripts.py --probe` will
tell you when it has recovered; it takes hours, and switching networks buys a
fresh window immediately. Metadata no longer competes for it — the Data API is a
separate allowance, which is the whole reason to prefer it.

That now costs a run its cheap half rather than the run itself: with Pro
credits, the per-IP allowance gates nothing, it only decides how much of a batch
comes back free. The one metadata gap left is the 4,823 videos the year filter
skipped, and those cost quota units rather than a sitting.

## The CI refresh regression — fix before the next weekly run

`kb-refresh.yml` ran on its schedule and committed `e0cdc09`, "Refresh the AI
talk catalogue", straight onto `main`. It has to be reverted, and the reason is
worth knowing before the workflow fires again.

The workflow re-enumerates every source with `sync_catalog.py --refresh` from a
GitHub runner. YouTube throttles those ranges — which is why the workflow
deliberately does not attempt transcripts — but enumeration is not exempt, it
just fails *quietly and partially*. What came back had titles and durations and
no uploader, so the refresh wrote **`channel: null` over ~4,540 talks**: 5,241
of its 6,980 records carry a null channel, against 649 of 7,351 here.

**The existing backstops did not catch it.** A source that returns nothing keeps
its cached videos, and `sync_catalog.py` refuses to write a corpus more than 10%
smaller without `--allow-shrink`. Both guard the *count*. This run returned a
plausible number of videos with a field hollowed out, so nothing tripped. A
field-level guard — refuse to write if a populated field goes null on more than
some fraction of a conference — is what would have.

The merge (`aaca745`) therefore takes this tree wholesale with `-s ours` rather
than reconciling field by field. The one thing the CI run genuinely had was
three videos newly posted since the last enumeration:

| Video | Conference |
|---|---|
| `D7_ipDqhtwk` How We Build Effective Agents: Barry Zhang, Anthropic | ai-engineer |
| `Lm-1O2gIVwg` Scott Jenson on Evolving Desktop OS, Local-First, & Agentic UX | qcon-infoq |
| `F2Ay09T4EHQ` GitHub, Snyk, Docker & Anthropic on Securing AI Agents | ai-devcon-tessl |

Those were copied into `data/catalog/` by hand and re-enriched from the Data
API, so they arrive with the channel and date the CI records lacked. Enriching
those three conferences with `--all` also detailed 17 other pending videos, and
because `qcon-infoq` is `scope: "ai"` and matches on description, the corpus
went 7,336 → **7,351** rather than 7,339.

Note the catalogues sat at exactly 900 / 500 / 300 videos before the insert:
those are the `first: N` paging caps, so a channel that keeps publishing pushes
its oldest enumerated video out of the window rather than growing the file.

**Fixed: the workflow now proposes rather than writes.** It commits to
`automation/kb-refresh` and opens one long-lived pull request against `main`,
rewritten each week rather than a new PR every Monday. It no longer pushes to
`gh-pages` either — that was the other half of the damage, since the degraded
corpus went live before the commit was noticed. Publishing is now a consequence
of merging: `pages.yml` fires on a push to `main`.

`refresh_report.py` is the thing that makes that gate useful. A 4,600-file diff
of generated JSON cannot be reviewed by reading it, so the report diffs field
coverage against the committed corpus and puts the table in the PR body. Past
the tolerance the PR opens as a **draft**, titled so it is visible in the list
without opening it. Run against the offending commit it says what a reviewer
would have needed to see:

| Field | Before | After | Δ |
|---|---:|---:|---:|
| `channel` | 6,702 | 1,739 | **-4,963** |

The tolerance is 2% of the corpus per field, non-zero because re-enumeration
legitimately drops the occasional video whose uploader deleted it, and that
takes its fields with it. Exit codes are 0 clean, 1 no baseline, 2 regressed.

What is *not* done: the guard is advisory. A reviewer can still merge a draft PR
after un-drafting it, and `sync_catalog.py` itself will still write hollow
records to `data/catalog/` on a local `--refresh` from a throttled connection —
the check is on the derived corpus, not on the cache it comes from.

## Next steps, in order

1. **Enable GitHub Pages** on the `gh-pages` branch. `main` is pushed and
   `pages.yml` mirrors it into `gh-pages` on every push, but Pages itself has
   never been switched on, so the published URL in `README.md` does not serve
   anything yet.
2. **Fix the one UI check the corpus outgrew.** `controls` needs one
   description short enough not to overflow the clamp to prove its negative
   case, and now finds **0 of 180** untruncated: the Data API's descriptions are
   uniformly long. It is not a UI regression — rebuilding the index at the old
   1,200-character clip fails it too, and it drifts with the corpus rather than
   with the code.
   `ranking` is now green, and that is worth reading as evidence rather than as
   a fix: it asserts 4 of the CLI's top 10 land in the web's top 40, and
   **"inference"** was failing at 1 of 10 until the 2026 extraction, after which
   it passes untouched. `moments` and `multi agent` did the same thing earlier.
   Three queries have now started and stopped failing on their own, which says
   the check measures corpus size as much as ranking quality — the rankings were
   re-read by hand each time and were good on both sides of every flip. Changing
   what it measures is still the right fix; a green run today is not it.
3. **Re-run the UI tests** after any collection run: `cd tools/uitest && node run.js`.
   They degrade to `SKIP` rather than failing when a fixture has not been
   collected yet, so a green run on a thin corpus is weaker evidence than a
   green run on a full one — read the skip count, not just the failures.
4. ~~**Finish the 2026 extraction.**~~ **Done** — 1,227 fetched in under six
   minutes, 0 pending. About 1,950 of the month's 3,000 credits are now spent.
   The next decision here is whether to spend the remainder on pre-2026 talks,
   which is a change of policy rather than a backlog: see *Collection is scoped
   to 2026* before doing it.
5. Re-check the conferences that came back thin: `owasp-global-appsec` (2
   talks), `tedai-vienna` (6), `apple-wwdc` (7), `meta-connect` (9). Some are
   genuinely small playlists; some may need a better source or a looser filter.
   `fully-connected-wandb` came back at 49 and is off this list.
6. Backfill the pre-2026 descriptions if anything ever wants them: the year
   filter skipped 4,823 videos, which is one `enrich.py --all` without
   `--min-year` and about a hundred quota units. Nothing depends on it — the
   2026 scope is a selection policy, not a coverage target.

## Handoff — running a transcript extraction

The 2026 scope is fetched. This is the shape of the next one, whatever selects
it:

```bash
cd tools
source ~/.bash_profile                     # see below — this is not optional
.venv/bin/python fetch_transcripts.py --probe
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --workers 32
.venv/bin/python sync_catalog.py && .venv/bin/python build_index.py
```

- **Name `--source supadata` and raise `--workers` whenever `--probe` says the
  IP is spent.** That is the difference between ~3 talks a minute and ~250 —
  see *The 2026 extraction*. `--source exact` is right only when the free
  routes might actually work, because it pays two refusals a talk when they do
  not, and it holds the egress lease while doing so.
- **`--probe` first, every time.** It costs one credit and decides which of the
  two flags above you want.
- **Deps live in a venv at `tools/.venv`**, not in the system interpreter, so
  use `tools/.venv/bin/python`. `.gitignore` already covers `tools/.venv/`.
- **`SUPADATA_API_KEY` and `YOUTUBE_API_KEY` are exported in `~/.bash_profile`,
  which a non-login shell does not read.** A tool-driven or CI shell sees
  neither and the run silently degrades to the free routes. Source it
  explicitly. This cost real debugging time.
- **`sync_catalog.py` then `build_index.py` afterwards**, in that order:
  the first inlines the new transcripts into the markdown, the second rebuilds
  `talks.db` and the browser index. Neither touches the network.
- **Do not skip the rebuild.** The priority-1 run finished 39 minutes after the
  last `build_index.py`, so 276 fetched transcripts sat on disk invisible to the
  browser, the CLI and the markdown until the pair was re-run. A transcript that
  is not indexed is a credit spent for nothing. At 250 a minute this is worse,
  not better: chain the two commands onto the fetch so the window cannot open.
- **Check `_misses.json` after a big run**, and read the details rather than
  the count. Every entry should be a fact about the video — no captions, or a
  403 for a members-only recording. Anything that looks like a network verdict
  is a bug in the classification, and it is permanent: `--retry-misses` is the
  only way back.
- **~1,950 of the month's 3,000 credits are spent.** Credits ≈ talks, so a run
  needs no headroom beyond its own selection count.

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

- **The AI filter is a property of the source, then of the conference — never
  of the corpus.** A dedicated AI conference contributes everything
  (`scope: "all"`); a general one contributes only what matches `atu.AI_RE`
  (`scope: "ai"`); and a single source may override its conference, which is
  how the WeAreDevelopers World Congress seed contributes all 358 sessions
  while the same conference's channel listing still contributes only its AI
  talks. The distinction that matters is not the topic but the provenance: a
  curated agenda is a programme, a channel listing is uploads. The regex allows a
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

- **A seed is a source, not a hand-edit of the catalogue.** Videos could have
  been written straight into `data/catalog/<conf>.json`, and would even have
  survived a refresh, since deletion is per source URL. They would not have
  survived a reader: nothing in the registry would say where 358 videos came
  from, and a fresh clone could not re-derive them. `"type": "videos"` puts the
  provenance where every other source's provenance is, and costs one merge path
  that both kinds of source share.

- **Stated speakers bypass the two-pass name filter.** The filter exists because
  a title is all most of this corpus has, and it works by assuming a name seen
  across a tenth of a conference is a brand. An agenda that names its speakers
  outright breaks that assumption in the right direction — a real speaker with
  many sessions is prolific, not a brand — so seeded names skip both passes.
  Speaker coverage went from 2,591 to 2,947 on 357 talks, because every one of
  them has a name the heuristics would mostly have missed.

- **The egress lease is about spending an IP's allowance, not about being
  polite.** So a route that egresses from somebody else's IP takes no lease and
  no pacing delay (`uses_our_ip()`), and a route that uses ours still takes
  exactly one at a time. The temptation on reading `Pool` is to conclude that
  serialising is the safe default and leave it alone; it is not safe, it is 80×
  slower, and the guarantee it exists to provide does not apply to Supadata at
  all. The three checks that pin this down — nothing leased, workers actually
  overlapping, and `spent()` ending the round on an idle pool — are in
  `test_fetch_transcripts.py` and need no network.

- **A 429 is not the same kind of refusal as a 402.** Both are account-level,
  which is why they were handled together, and that was wrong once more than
  one request was in flight: waiting fixes a rate limit and does not fix an
  empty balance. 429 backs off and retries, then raises `BlockedError` — never
  `LookupError`, because that path writes `_misses.json` and a miss means *this
  video has no captions* forever. 401 and 402 still retire the route for the
  run.

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
  the clip halved and it came back to 5.4 MB. It is **5.8 MB** now at 7,351
  talks with 5,557 descriptions, so it is creeping back towards the line.
  Description coverage is still only 75%, so this will need looking at again;
  the 6 MB trigger stands.
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

`README.md` states 7,351 talks / 46 conferences / 15,157 enumerated, and how
many of them are 2026 and how many of those are transcribed; this file states
transcript, description, year, tag and speaker coverage, the per-conference
transcript split, the 2026 pending backlog, the passage count, the credits
spent this month, and the sizes of `talks.db`, `search-meta.json` and
`tindex/`. `sync_catalog.py` prints the coverage at the
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
