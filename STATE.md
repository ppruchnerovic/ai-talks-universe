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
| Registry (`conferences.json`) | Done. **53 conferences, 84 sources** — 83 YouTube listings and one `"type": "videos"` seed — mirrored from `ai-conferences.md`; `check_registry.py` passes. Seven conferences added 2026-09-01, see *The seven conferences added on 2026-09-01*. |
| Enumeration (`sync_catalog.py`) | Done. **17,677 videos** cached in `data/catalog/`, **8,826 surviving talks** — 9,325 before the 2023 year floor, see *The pre-2023 cut* — plus **222 InfoQ-only presentations**, **9,048 in the corpus**. 8,468 of them enumerated from YouTube, 358 seeded — see *The WeAreDevelopers import*. |
| Speakers | **4,982 of 9,048 (55%)** since 2026-09-02, up from 3,447 (38%): the bold-Unicode `Speakers:` heading Microsoft's channels use, the `A & B, Company` and `by A and B` title shapes. See *Review of 2026-09-02*, section D, and `test_speakers.py`. |
| Enrichment (`enrich.py`) | Done for the 2026 scope. **9,598 videos via the Data API**, in one run. See *What the collection runs actually got*. |
| Per-talk markdown | Done. 9,048 files, regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. Since 2026-09-02 the passages overlap at a half-passage stride and `talks.db` carries `PRAGMA user_version` (`atu.DB_SCHEMA_VERSION`, now 5) — 379 MiB, 48 s to build, and `atu.connect()` rebuilds it by itself when it is stale. The browser index is **keyed on Porter stems** (`atu.stem()`, memoised; the same function in JavaScript inside `index.html`, `test_stem.py` diffs them over the corpus vocabulary) and carries the **whole description's postings** per stem (`d`) plus the metadata document frequency (`m`): 46 MB in 712 shards, 52,327 stems, 35,352 of them in descriptions; `search-meta.json` 5.6 MiB, 94% of its trigger, now display-only. Byte-identical run to run. See *Review of 2026-09-02*, sections C and E. |
| CLI (`query.py`) | Done, and its ranking was rebalanced — see *Design decisions*. `--brief` and `--ids` were added for the skill — see *Making the skill affordable*. Rewritten 2026-09-02 around a gate on content words with progressive relaxation, plus `--transcript`, `--min-year`, repeatable `--conference`/`--category`/`--year` and a `~` on estimated timestamps — see *Review of 2026-09-02*, section C. Later the same day: relaxation drops a word **no talk says** before the commonest one (a typo used to take the real word with it), and `--stats` prints the corpus's counts from the index so the skill quotes nothing from memory. |
| Excerpting (`excerpt.py`) | Done, 2026-09-01. Windowed passages instead of whole transcripts; **100% of the passages `query.py` ranks survive, on 17% of the words**. See *Making the skill affordable*. |
| Browser UI (`index.html`) | Done. Conference / category / year facets, passage-level ranking. Since 2026-09-02: queries and index share one Porter stemmer, descriptions are searched whole through the shards rather than on their first 300 characters, a query no talk fully matches relaxes one word at a time and says so in the status line, highlighting is token-exact on stems, and an interpolated moment is shown as `~12:34`. See *Review of 2026-09-02*, section E. |
| Browser UI tests (`tools/uitest/`) | **183 checks over 9 suites, 0 failing, none skipped** (2026-09-02). New since the 172: stems, relaxation, the description tail beyond the clip, the `~` mark, and the `load` suite's title-link check now accepts an InfoQ page when newest-first puts one on top — it had been asserting YouTube since before InfoQ existed. Ranking agreement margins 9, 10, 8, 8, 9, 8, 10, 9 of 10 against a threshold of 4 (were 10, 9, 6, 6, 10, 6, 10, 9). |
| Excerpt tests (`tools/test_excerpt.py`) | Done. **14 offline checks** over window selection and merging — no corpus, no network, 0.1s. |
| Other offline tests | `test_query.py` (23, the parser and id resolution), `test_infoq.py` (the fold-in), `test_speakers.py` (19, every speaker shape and the false positives), `test_stem.py` (both stemmers over all 103,551 corpus tokens; skips its node half if node is missing). All green. |
| Fetcher tests (`tools/test_fetch_transcripts.py`) | Done. **128 offline checks** over the pool, the routes, the year selection, the four failure classes, the off-IP lease rule and the caption-language selection. |
| Claude Code skill | Done — `ai-conference-talks`, in `.claude/skills/`. Rewritten 2026-09-01 around a retrieval ladder that costs ~17k tokens a question instead of ~150k — see *Making the skill affordable*. Revised 2026-09-02 (section F): no hard-coded counts (`query.py --stats` instead), search the topic's words not the question, `url` rather than a YouTube template, `~` timestamps cited as approximate, `year` is the edition's, `-n` is a budget. |
| Transcripts | **3,174 of 9,048** over 35 conferences — 2,946 with exact timings (four of them held back from the index as ASR failures) and 228 estimated, from infoq.com. Before InfoQ: 2,946 of 8,822, all exact. ai-engineer 540, wearedevelopers 433, pydata 205, microsoft-build 187, berkeley-agentic-ai-summit 159, kubecon 151, ndc 149, ai-devcon-tessl 132, qcon-infoq 106, ai-council 94, mcp-dev-summit 84, devoxx 79. **The 2026 scope is complete**: of its 2,942 talks, 2,914 have a transcript and 28 have no captions, so nothing is pending. `I1GvlW1H4WI` entered the scope when the year-from-title fallback was fixed and was fetched for one credit — see *The pre-2023 cut*. The 422-talk backlog the seven new conferences created was fetched the same day — see *Closing the 422*. Twelve are `hi` and cannot be improved — see *Bug 7 cannot be fixed by refetching*. What is left is pre-2026 and deliberately unfetched — see *Collection is scoped to 2026*. |
| Imports (`import_kb.py`) | Done for WeAreDevelopers World Congress 2026: 358 talks and their transcripts, from `../presentations/kb`. Offline and rerunnable. |
| Workflows | Both run. `pages.yml` was rewritten on 2026-09-02: it now runs `tools/assemble_site.sh` and pushes only what the browser fetches to `gh-pages` as one orphan commit — 249 MB instead of the whole 411 MB repo. **Not yet verified live**: the rewrite is on the `infoq-presentations` branch and has not been through a push to `main`; watch the first deploy's `du` lines and load the site afterwards. `kb-refresh.yml` pushes a review branch instead of committing to `main`, after the run that did — see *The CI refresh regression*. |
| Published site | **Live** at <https://ppruchnerovic.github.io/ai-talks-universe/>, served from `gh-pages`. Until the new `pages.yml` has run once it is still the old whole-repo mirror. |

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
2,525. It happened again on 2026-09-01 — see *The bug list, worked*.

Coverage as it stands, after the 2026 extraction, the priority-1 run, the CI
merge, the 2026-09-01 bug pass and the seven conferences added the same day:
the 2023 floor applied: 6,868 descriptions, **8,822 of 8,822 with a year**,
3,219 with a speaker, 4,512 with YouTube tags, **2,946 transcript files on disk of which 2,942 are indexed**
— four are held back by the words-per-minute floor, see *The wpm floor and the
doc_len it did not fix* (12 of the files are `hi`, which no route can improve —
see *Bug 7 cannot be fixed by refetching*). **548,120 passages**;
`data/talks.db` 184.4 MiB, `search-meta.json` **5.43 MiB (5,695,808 bytes), 91%
of the 6 MiB trigger, after `META_DESC_CHARS` was halved 600 -> 300 and the year
floor took 503 talks' descriptions out of it** — it
carries descriptions, not transcripts, so 420 new transcripts did not move it;
`data/tindex/` **38.5 MiB** over **674 shards** carrying 43,303 terms — split
two characters deep instead of one, so the largest shard is 1.7 MB rather than
the ~4 MB a one-character split gave. Of the 2,942 talks in the 2026 scope,
**2,914 have a transcript file, 2,910 of them indexed, 28 have no captions, and
none is pending** — the wpm floor is an index-time judgement and `select()`
reads the disk, so a held-back talk is never re-selected for a fetch.

**The year gap is closed outright.** The "2 without a year" this file quoted for
weeks were two of the seven hollow records, and they are gone: every one of the
8,822 talks now has a year — including the 1,977 that arrived on 2026-09-01,
which were enriched before the sync that kept them.

## The 402 that was recorded as "no captions"

Found by testing on 2026-08-31, before it had a chance to fire. STATE.md
already claimed the property it violated: *"your account is out of credits"
retires the route for the run and leaves the talk retryable*. It did not.

`_supadata_get` raised `LookupError("supadata: out of credits")` on a 402. Both
runners ask `is_block(e)` before recording a miss, a `LookupError` is not a
block, so the talk went into `_misses.json` with `reason: "LookupError"` — the
file that means *this video has no captions*, which `select()` then skips on
every later run unless someone passes `--retry-misses`. An empty balance was
being written down as a permanent fact about a video.

It is not one talk. `_supadata_off` closes the route only for talks not yet
dispatched, so every request already in flight when the balance hits zero gets
its own 402 and its own poisoned entry — up to `--workers` of them, which is 32
at the setting the handoff recommends. Credits ≈ talks and about 2,370 of the
month's 3,000 are spent, so the next full run is the one that would have hit
it.

The fix is a third exception class rather than reusing `BlockedError`, and the
difference matters under `--source exact`: a block benches the leased identity
and retries the talk on another IP, which is exactly wrong for an account
refusal — no other IP has a fuller balance, and the identity that was benched
had done nothing wrong. So `AccountError` is neither a block nor a miss:
`about_the_video()` is what the runners now ask, `attempt()` still benches only
on `is_block()`, and a round with nothing left to fetch with ends on
`ACCOUNT_ADVICE` ("top up, or run the free routes") rather than on the IP-block
advice, which would have sent the reader to switch networks over a billing
problem.

Two sibling paths had the same defect and were fixed with it, because the
question is never "is this a 402" but "does this failure say anything about the
video":

- **A run of 5xx, a dropped connection or a timeout.** `_supadata_get` ended
  `raise last`, handing the runners a bare `HTTPError` or `URLError` after four
  attempts. Neither is a block nor an account refusal, so a supadata outage
  would have cost one talk per request, permanently.
- **A job that never finishes.** The 15-minute polling deadline raised
  `LookupError`. The credit is already spent and the captions may well exist;
  writing the talk off as having none loses both.

Both now raise `TransientError`, which benches nothing — what failed was the
far end, not one of our identities — and ends no round: the route may work on
the very next talk, so the run carries on and the talk waits for a rerun. A job
that comes back *failed* is still a `LookupError`, because that one is a verdict
on the video.

Nothing needs repairing in the corpus: all 27 entries in `_misses.json` are
genuine — 13 no captions, 10 members-only 403s, 4 yt-dlp no-subtitles — and
none carries a credit, rate-limit or network detail. Twenty-one checks cover
the three paths, including two full `run_parallel` rounds — one whose fake
account runs dry mid-flight, which must stop with an empty miss file, and one
where two talks fail transiently, which must *not* stop and must still leave
the miss file empty.

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

## The bug list, worked — 2026-09-01

All fourteen bugs from the 2026-08-31 pass are fixed, in five parallel streams
partitioned by file so nothing collided. What follows is the outcome, and in
five places **the audit that found the bug had it wrong** — those corrections
matter more than the fixes, because they were being quoted as fact.

### Where the original list was wrong

- **The hollow records were seven, not three.** `has_details` is not a catalog
  field at all — it is derived in `build_talks()` from `details_at`, which is
  what had to be inspected. Only three reach `talks.json`; the other four sit in
  `scope: "ai"` conferences and are dropped by the AI filter, having no title or
  description to match on. All seven are dead videos (one deleted, six private),
  checked with one GET each against a control.
- **Clearing `details_at` would have been the wrong repair.** `enrich.py`
  stamps it on videos the Data API does not return, precisely so private ones
  are not retried forever. Clearing it buys a re-stamp and wasted quota every
  run. The seven were removed instead.
- **The "six transcripts under 20 words a minute" conflated two things.** Two
  are complete, coherent Japanese transcripts of Japanese-language workshops;
  the low rate is an artifact of whitespace word-counting on Japanese. They were
  kept. Only four files were junk. Measured properly, the wpm tail is smooth
  down to ~90 (demos, Q&A, slow speakers) and then breaks hard.
- **Sorting the non-monotonic transcripts would have corrupted one of them.**
  In `daMEEWVlgY8` the file order is the coherent sentence and it is one cue's
  *start* that is wrong — a zero-length cue hitting `fetch_supadata`'s 0.5s
  floor. Sorting would have emitted "...corporations and / completely
  autonomous. / government with almost no human intervention,". `bJKdXhnw7NU` is
  the interleaved-track case: 15 spliced cues of duration exactly 1.0
  duplicating their neighbours' words in a different caption style. In both, the
  segment holding the bad start *is* the damaged one, so the repair was to pull
  that start back, not to reorder. Reading order preserved; only `start` values
  changed.
- **The `pick_and_fetch` language claim was false.** `Transcript.translate()`
  constructs a new object with the target `language_code`, so it already
  returned `"en"`. But there was a worse bug in the same three lines that the
  audit missed: `t.translate("en")` raises `TranslationLanguageNotAvailable`
  when no English translation exists, which is neither a block, an account
  refusal nor a transient — so `about_the_video()` waved it straight into
  `_misses.json` as "this video has no captions", for a video that demonstrably
  has them.

### The root cause behind bug 7, and why it gated the fix

`fetch_supadata()` sent only `url` and `mode=native`, no `lang`, so Supadata
chose the track. That is how ten English talks acquired Devanagari transcripts —
complete-looking, normal word rate, indexed as the talk, containing none of its
searchable English. Delete-and-refetch was therefore unreliable, which is why
only the four *empty* ones were deleted and six complete-but-wrong-script files
were deliberately left in place until the fetcher was fixed.

`lang` alone is not sufficient, and the documented semantics are the reason: the
API *substitutes* rather than failing — "if the video does not have a transcript
in the preferred language, the endpoint will return a transcript in the first
available language and a list of other available languages". So the fetcher asks
`lang=en`, checks the answer, and re-requests once against `availableLangs` only
when the first answer is off-list and the video offers something on-list. No
second credit on the happy path.

**A foreign-only track is saved, honestly labelled — not missed, not retried.**
`_misses.json` would be a lie and would lose the talk permanently. A retryable
non-verdict is worse: it re-selects the talk and burns a credit every run, and
next month the track is still Hindi — it never converges, at unbounded cost.
`LANGUAGES` is a preference order for choosing among the tracks a video offers,
not a statement about what the corpus may hold; it already carries twelve
languages deliberately.

### The four fixes that make bugs self-healing rather than hand-repaired

The data was fixed *and* the code that produced it, so a re-enumeration cannot
reintroduce any of it:

- `clean_tags()` in `sync_catalog.build_talks()` and the same fold in
  `enrich.apply_details()` — titles were already whitespace-folded and
  descriptions already sanitised, which is exactly why no title was corrupted
  and three tags were. It folds rather than splits on purpose: splitting would
  *invent* tags out of a source's formatting accident.
- `keep_video()` now rejects an empty title and treats a null duration as
  failing `min_duration`. Both independently catch all three hollow records that
  reached the corpus and fire on nothing else; the private videos are still
  listed in their playlists, so a refresh *will* re-offer them.

### Bug 7 cannot be fixed by refetching, and the remedy this file recommended was wrong

This was settled on 2026-09-01 by running it. The ten `hi` talks were deleted
and refetched with `--source exact`, both free routes working. **All ten came
back `hi` again**, and the four near-empty ones came back byte-for-byte as bad —
153, 159, 167 and 185 words, at 2.5 to 3.7 words a minute over 41- to
73-minute talks. It reproduces exactly; it was never a fetch accident.

The reason is upstream of every route this repo has:

```
youtube_transcript_api.list('1tcir8BPP3M')  ->  hi (generated), not translatable
supadata mode=native lang=en                ->  lang: hi, availableLangs: ['hi']
```

**These videos expose exactly one caption track, auto-generated, and YouTube's
ASR mis-detected English audio as Hindi.** There is no English track to fetch,
so no route can produce one and `--source supadata` is not a second opinion —
it reads the same tracks. The six substantial files are complete Devanagari
*transliterations* of English speech ("थैंक यू फॉर कमिंग" = "thank you for
coming"); the four short ones are the same ASR failing outright.

The language fix did exactly what it should: it asked for `en`, got `hi`,
checked `availableLangs`, found nothing on-list, and kept the track honestly
labelled instead of writing a false `_misses.json` entry. **That is the fix
working, not failing** — before it, this run would have been ten permanent
misses on ten videos that demonstrably have captions.

So the ten stay, and the earlier instruction to "delete the file and refetch" is
struck: it costs a round trip and returns the same bytes. The only route to
English here is Supadata `mode=generate`, which transcribes audio at two credits
a *minute* rather than one a talk — about 66 credits for these ten, against a
standing decision to use `mode=native` only. That is a policy change, not a bug
fix, and it is the one thing that would actually work.

One of the two things this left to decide is now done — the four near-empty
files are no longer indexed, see the next section, and the claim there that a
wpm floor would also catch the three degraded `de` ones was wrong. The other
stands: **nothing distinguishes a foreign transcript in the UI.** The eight
substantial `hi` files still count toward the transcript total and none can
answer an English query.

### The wpm floor, and the doc_len it did not fix

Built 2026-09-01, from the previous session's handoff. The floor is in
`build_index.py`: `MIN_WPM = 10`, applied only when the duration is known and at
least `MIN_RATED_MINUTES = 5`. It catches exactly four files — `m0Le7rXlsNs`,
`nKZVd8r89nI`, `NdGBsn8tRzs`, `1tcir8BPP3M`, at 2.5 to 3.7 wpm — and the next
slowest real transcript is 19.9, so the threshold is a gap rather than a tuning
parameter: anything from 5 to 19 does the same work. Median is 164.5, p1 98.4.
The files stay on disk; `select()` reads the disk, so nothing is re-fetched.

Two things about the handoff's plan were wrong, and the second is the larger
finding.

**Returning empty text is not enough.** The plan was that `has_transcript`
becomes 0 at `build_index.py`'s `1 if text else 0` and the talk drops out of
everything. It does not: the browser gates the transcript badge, the
has-transcript filter and "Find this in the talk" on `w` — `index.html:270`,
`455`, `480`, `505` — and `w` is `search-meta.json`'s copy of `word_count`,
which is `transcript_text()`'s **third** return value, not its first. Dropping
only the text would have left a live word count with no text behind it: the
deep link into 150 words of fragments intact, and `transcript_words` in SQLite
disagreeing with `has_transcript` on the same row. All three values are zeroed
together, and the docstring says why so it is not "simplified" back.

**"Nearly harmless — they match no English query" was false, and the real defect
is bigger than the floor.** `atu.TOKEN_RE` is `[a-z0-9]…`, so it skips
Devanagari and keeps the Latin islands. `NdGBsn8tRzs` tokenised to 15 tokens,
three of them `facebook`, three `whatsapp`, one `instagram`. BM25's length
normalisation then read a 15-token document in which "facebook" was
overwhelmingly frequent. Measured in the live UI with Playwright before the fix:
**5th of 95 for "facebook", 6th of 82 for "whatsapp", 7th of 62 for
"instagram"**. `query.py` was never affected — FTS5's `unicode61` indexes the
Devanagari, so its segment lengths are honest. This was browser-only.

A wpm floor cannot fix that, because the worst case is not slow.
`HotbjSIgLOM` is 6,084 Devanagari words over 39 minutes — **156 wpm**, nowhere
near any floor — tokenising to 20 tokens, 8 of them `netflix`. It ranked **1st
of 4 for "jio"** and 18th of 97 for "netflix". Fifteen transcripts have
`len(tokens) < 25% of word_count`: `hi`x12, `ja`x2, `ar`x1. The floor reached
four of them.

So `index_length()` sets the BM25 document length: `len(toks)` normally, and
`round(0.42 × word_count)` when the tokeniser can see less than a quarter of the
transcript. 0.42 is the corpus median of tokens per word; across the 2,930
transcripts the tokeniser can read that ratio runs 0.33 to 0.91. **BM25 uses
only `dl/avg`**, which is why this is safe: nothing changes for a readable
transcript, `avg_doc_len` moves 2205.74 -> 2215.57 (0.4%), and the unreadable
ones are demoted rather than removed — a talk that really does say "netflix"
eight times should still be findable, just not above the talks about Netflix.

Measured after, in the same live UI: the fragment file is absent from all three
queries, `HotbjSIgLOM` goes 1st -> 3rd for "jio" and 18th -> 19th for "netflix".
172 UI checks pass with none skipped, including `ranking`, which checks
agreement with `query.py`; the 128 fetcher checks pass; and `build_index.py`
into `--out` is still byte-identical to `data/`, so the idempotency claim in
README holds.

Two things not to redo. The floor deliberately does **not** reach the three
degraded `de` transcripts (`hbShI0crCOg`, `6NC9laD5OHY`, `RS4DmYTvHIo`) — they
sit at 51.9, 64.5 and 66.4 wpm, and a threshold above 66 would sweep up the two
Japanese workshops at 19.9 (complete transcripts; whitespace word-counting on
Japanese is the artifact) and `GiqyYQdYoIY` at 52.3, the 8.8-hour Code with
Claude Tokyo livestream with 27,550 real English words. Three false positives
out of ten drops, two of them the exact mistake the original audit made. Those
need a different signal — fragment ratio, mean cue length, dictionary hit rate —
or a hand-maintained deny-list of three ids. And `sync_catalog.py` still writes
`transcript: true` and inlines the block for all 2,946, because it keys on file
existence: the markdown is the evidence trail, and the four held-back files are
still what YouTube returned. That divergence is deliberate; `build_index.py`
prints the four ids and their rates on every run so it is never silent.

### Still open, deliberately

- **37 transcripts are not labelled English** — `hi`x12 (the unfixable ones
  above; the 2026-09-01 fetch added two more, `HotbjSIgLOM` and `LthkAkIQhgc`,
  both ai-council, both English audio transliterated into Devanagari), 10
  literal `"none"` (English text Supadata could not name, which will
  refetch cheaply and label properly), `de`x3, `es`x2, `ja`x2, `lt`x2, `no`x2,
  and one each of `vi`, `ar`, `sv`, `nl`. Most are genuinely those languages and
  belong in the corpus; the `no` ones are probably real Norwegian, NDC Oslo. The
  `"none"` ten are the only cheap win in the list.
- **Three transcripts are English with badly degraded ASR** (`hbShI0crCOg`,
  `6NC9laD5OHY`, `RS4DmYTvHIo`, labelled `de` in the WeAreDevelopers import) —
  coherent for a minute, then collapsing into fragments. Real but half-missing.
- **Route 2 (`yt-dlp`) passes `--sub-langs` limited to `LANGUAGES`**, so a video
  with only an off-list track writes no caption file and becomes a permanent
  miss — the same invariant violation as bug 7, on the free route. The only fix
  is fetching every language on every video, which costs bandwidth on all 7,348.
  Flagged rather than silently paid for. It bites only on our-IP runs.
- **`count` drifts by one in three catalogs** (`ai-devcon-tessl` 300/301,
  `ai-engineer` 900/901, `qcon-infoq` 500/501). Not a code bug: both writers set
  `count = len(videos)` correctly. It traces to `ec68e00a`, where three videos
  were copied in by hand without bumping `count`. Only `--refresh` rewrites a
  non-seeded catalog, so a plain rebuild will not clear it.

### What the pass confirmed clean, so nobody re-derives it

The shard-key invariant holds over all 40,927 terms against the real
`shardKeyOf()` (0 disagreements, 670 manifest shards = 670 on disk); the browser
index, every markdown file and every CSV cell reproduce byte-for-byte from
`talks.json` plus the transcripts; all artifacts agree on the talk count with no
duplicates or orphans; the 48 underscore-leading ids survive every layer; the
dense `n` is `talks.json` position everywhere; every seeded WeAreDevelopers talk
kept its agenda abstract, speakers and tags; and 180 of 180 sampled transcript
timestamps land on a real caption cue. `sync_catalog.py` and `build_index.py`
make no network call, checked under an audit hook that raises on
`socket.connect` — as were all the offline suites run in this pass.

**The 48-underscore trap bit again during this pass**, exactly as this file
warns: a prefix-filtered count reported 2,473 transcripts where the corpus has
2,521. The warning works; the trap is just very easy to fall into.

**Documentation correction, re-verified against the rebuilt corpus:** this file
said `query.py postgres` finds the transcript-only talk at rank 4. It is rank 14
(*Microsoft Build 2026 Day 1 Opening Keynote*). The substance holds — metadata
leads, transcript-only hits still surface — but the rank drifted with the corpus.


## The seven conferences added on 2026-09-01

The registry was audited against what the world actually publishes, and seven
conferences were missing rather than rejected. They are now registered, and the
corpus went **7,348 -> 9,325 talks** (17,677 videos enumerated, up from 15,150):

| Conference | Kept | Scope | Priority | Why it was a hole |
|---|---:|---|---|---|
| `mcp-dev-summit` | 136 | all | 1 | MCP's own conference (LF Agentic AI Foundation). Nothing else here covers the protocol as a subject rather than a feature |
| `berkeley-agentic-ai-summit` | 227 | all | 2 | Where agent research meets production practice; Dawn Song's centre |
| `ai-council` | 479 | ai | 2 | Data Council, renamed for 2026; ten years of AI-and-data-stack talks |
| `lf-ai-dev` | 328 | ai + per-source `all` | 2 | Open-source GenAI/ML infra: AI_dev standalone through 2025, folded into Open Source Summit from 2026 |
| `microsoft-ignite` | 761 | ai | 3 | Build was registered and Ignite was not, which is the one asymmetry a reader would notice. 502 sessions in the 2025 playlist alone |
| `sequoia-ai-ascent` | 29 | all | 2 | Karpathy, Hassabis, Brockman, Jim Fan — talks this corpus was being asked about and did not have |
| `yc-ai-startup-school` | 17 | all | 2 | Same argument, single track, full talks rather than clips |

Four decisions inside that, none of them mechanical:

- **Playlists, not channels, wherever the channel is a firehose.** The MCP
  channel also carries "The Context" livestreams and shorts; `@events_msft`
  carries every Microsoft event including Build, so registering it would file
  Build sessions under Ignite; Sequoia's and YC's channels are mostly clips and
  portfolio material. Only `ai-council` gets a channel source, with `first: 500`.
- **`lf-ai-dev` is one conference carrying two scopes**, using the same
  source-level override the WeAreDevelopers seed established: the AI_dev
  playlists are `"scope": "all"` because the whole event is AI, while the Open
  Source Summit playlists keep the conference's `"scope": "ai"` and contribute
  only their AI sessions. The event genuinely merged in 2026; splitting it into
  two registry entries would have implied a split that did not happen.
- **Berkeley publishes the same summit twice** — 160 individual talks and 175
  whole-day stage streams. Registering both would have doubled the edition and
  put four-hour "talks" in the corpus, so only the per-talk playlist is read.
  The 2025 edition has no per-talk playlist, which is why its 69 records are
  stage sessions and its durations look wrong beside everything else.
- **`ai-council` is `scope: "ai"` even though the conference renamed itself
  after AI.** Its back catalogue is Data Council: Kafka, Airflow, warehouses.
  The filter keeps 479 of 767 and drops exactly that.

Enrichment ran first, deliberately: `enrich.py --all --include-unknown-year` on
the seven cost about 50 quota units for 2,502 videos, and because three of them
are `scope: "ai"` and match on description, the sync that followed kept 9,325
rather than 8,763. Every one of the new talks has a year, so the 2026 selection
filter sees them properly.

**`search-meta.json` crossed its 6 MiB trigger** at 7.76 MiB and the documented
remedy was applied — `META_DESC_CHARS` 600 -> 300, back to 5.79 MiB. That file
is what every visitor downloads before typing anything.

**What this left: 422 talks in the 2026 scope with no transcript**, where
there were none pending before. That backlog was closed the same day — see
*Closing the 422*.

Checked in the same audit and deliberately **not** registered: VivaTech (keynote
clips and press coverage, no full-session playlist) and GitNation / JSNation /
React Summit (recordings live on gitnation.com, not YouTube) — both fail the
same test as the entries in *Checked but weak sources* in `ai-conferences.md`.
Worth a later look, unverified: NDSS, IEEE S&P, MLSys and CVPR, which do post
full sessions to YouTube and would extend the corpus towards academic work.

## Closing the 422 — 2026-09-01

The backlog the seven new conferences created is gone. The fetch selected
exactly **422**, the count this file predicted, which is the check that it was
selecting what was meant; **420 came back, 2 were genuine misses**. Transcripts
went **2,525 -> 2,945** and passages **491,282 -> 547,954**. `search-meta.json`
did not move, as predicted — it carries descriptions, not transcripts.

Verified before committing, both checks this file asks for:

- **All 29 entries in `_misses.json` are facts about the video** — "no
  subtitles for the requested languages", "no timed transcript for this video",
  a members-only 403, and one age-restricted 403. No network verdict among
  them.
- **172 UI checks, 0 failing, 0 skipped** — the strongest that evidence gets
  here, since a skip means a fixture the corpus does not have yet.

### The run was blocked by a proxy, and the fetcher blamed the wrong thing

`--probe` opened with **0 usable routes**: supadata failed
`JSONDecodeError after 4 attempts`, and the free routes reported `BLOCKED —
spent`. Both were one cause, and neither message named it.

The cause was **Zscaler**, the TLS-inspecting proxy on this egress. Given a
Chrome `User-Agent` on an API call it reads the request as web browsing and
answers with an HTML *Browser Isolation* interstitial — **at HTTP 200**, so it
arrives as unparseable JSON, four retries deep, and retires the route for the
whole run. Isolated to that one variable while the proxy was still up: the same
`curl` request with the browser UA returns the interstitial, with curl's own UA
returns the transcript.

Two changes in `fetch_transcripts.py`:

- **`UA` is an honest client identifier now, not a browser string.** Both its
  call sites are third-party JSON APIs — supadata and kome — and neither is
  YouTube, so the browser string bought nothing there while costing the entire
  route on this network. The YouTube routes are untouched:
  `youtube-transcript-api` and `yt-dlp` bring their own.
- **HTML at HTTP 200 from a JSON API now says so, once.** It was retrying an
  interstitial four times and reporting a parse error.

**The free routes were never spent either.** With Zscaler stopped, the probe
that had said `BLOCKED — spent` returned 15,871 words with exact timings, on
the same video, the same machine, twenty minutes later. So the fetcher reports
a proxy interception as an exhausted IP allowance. The direction is the safe
one — `BLOCKED` is retryable and nothing reached `_misses.json` — but it sends
you to spend credits on a route that was working, and it is why the Zscaler row
in *The quota* should not be trusted. A probe that reported the *reason*, not
just the verdict, would have saved this session an hour.

### `_misses.json` records the exception class, not the reason

`reason` holds `"LookupError"` for all 29 entries. The check this file
recommended printed the set of `reason` values, so it printed
`29 ['LookupError']` — which cannot distinguish "no captions" from a
misclassified network verdict, the exact thing it exists to catch. The fact is
in **`detail`**, and the snippet in *Next steps* item 4 now reads that instead.
Worth renaming the fields, or having the checker assert on `detail`.

## The pre-2023 cut — 2026-09-01

The corpus now starts at 2023. `conferences.json` carries a registry-wide
`"min_year": 2023`, `sync_catalog.keep_video()` enforces it, and the corpus went
**9,325 -> 8,822 talks**.

What decided the line, measured rather than assumed: the modern-LLM vocabulary
(llm/gpt/rag/agent/prompt/inference in title or description) appears in **3% of
2015-20, 9% of 2021, 4% of 2022 — and 30% of 2023, 53% of 2025, 63% of 2026**.
2022 -> 2023 is where this corpus changes subject. Nothing older than 2023 has a
transcript, and none was ever going to get one under *Collection is scoped to
2026*.

The 503 that went, by conference: `amld` 130, `ai-council` 122,
`mlops-world-tmls` 85, `wearedevelopers` 82, `web-summit` 53, `dotai` 19, `goto`
9, `ray-summit` 3 — AMLD 2022, Data Council before it renamed itself after AI,
MLOps World 2021, Web Summit pitch heats, "Building ASP.NET apps on Google
Cloud".

**Three conferences override the floor with `"min_year": null`** and keep their
whole back catalogue: `camlis` (59 pre-2023), `defcon-ai-village` (36) and
`bsides-lv` (14). Two reasons, and the first is the one that generalises:
adversarial ML, model evasion, data poisoning and deepfakes are the same subject
they were before the vocabulary changed, where applied ML in 2021 is not. The
second is arithmetic — 36 of DEF CON AI Village's 37 talks are 2019-21, so a
flat floor would have left a registered conference with one talk.

Four things worth not re-deriving:

- **The floor is checked last in `keep_video()`, after the AI filter**, so the
  `pre-2023` count in the drop report is what the floor actually cost — the
  talks that would otherwise have been kept. Checked first it reads **1,618**,
  because it swallows every old video the AI filter was going to reject anyway.
  Same corpus either way; only the report differs, and the report is the thing
  a reader uses to decide whether the floor is right.
- **An unknown year passes the floor**, which is the opposite of the
  `min_duration` rule directly above it and deliberate. Enrichment is what
  *resolves* a year, so dropping the undated would hide every talk a fresh
  enumeration found until the next enrich run — and hide it from
  `refresh_report.py`, which is what reads the difference. The floor is a claim
  about talks proven old. There are 0 undated talks today; there were 3,082
  once, and a `--refresh` makes more.
- **It bought no transcript bytes, and that was known in advance.** Not one of
  the 503 had a transcript, so `data/tindex/` is unchanged at 38.4 MiB and the
  passage count is unchanged at 547,925. What moved is the up-front download:
  `search-meta.json` **5.79 -> 5.43 MiB, 96% -> 91% of the 6 MiB trigger**, and
  `talks.db` 186.7 -> 184.3 MiB. If the trigger is crossed a third time, this
  is not the lever — 2025 and 2026 are 74% of that file.
- **It is reversible without a fetch.** `data/catalog/` still caches all 17,677
  videos; the floor is applied at derive time. `sync_catalog.py --no-min-year`
  rebuilds the 9,325-talk corpus, and moving the line is an offline re-run.

**`refresh_report.py` calls this a regression, once.** Against the pre-cut commit
it reads -503 on `year`, -469 on `channel`, -445 on `description` and so on, all
past the 2% tolerance, and says *do not merge as-is*. That is the gate working
rather than failing: it compares field coverage against the committed corpus and
cannot tell a deliberate policy cut from a throttled run — which is the whole
reason it exists, after one scheduled run wrote `channel: null` over ~4,540
talks. Once the cut is committed the comparison is like for like and the next
weekly PR is green. Do not widen `--tolerance` to make this one quiet.

### The year fallback was wrong, and the cut would have deleted a 2026 talk

`atu.year_of()` falls back to the first `20[12]\d` in the title, and the
corpus's only 2015 record was *"Production ML across 2015-2035: A Journey to the
Past and the Future [PyCon DE & PyData 2026]"* — a 2026 talk filed under 2015 by
its own subject matter. A cut on `year < 2023` would have deleted it silently.

`atu.year_span_re`/`year_in_text()` now skip a year that *opens* a span, and
only that one: the closing year is still a year the text states, so "GOTO
2024-2025" resolves to 2025 rather than to nothing. Measured against the whole
corpus before changing anything — only **four** records have more than one
distinct year in their title, and in three of them (all `owasp-genai` meeting
recordings, "Meeting October 23 2024 Finalizing The 2025 Top 10") the *first*
match is the right one. A "prefer the last year" rule would have fixed one
record and broken three. All 14 pre-2018 records got their year this way; every
record from 2018 on that has a `published_at` agrees with its title year, 0
disagreements.

That fix is why the cut dropped 503 rather than the 504 predicted, and why the
2026 scope grew by one to 2,942. That one talk was then fetched: the run
reported **1 selected**, which is the check that the selection was what this file
predicted, and came back exact at 5,495 words for one credit. Passages
547,925 -> 548,120, `_misses.json` unchanged at 29.

## Making the skill affordable — 2026-09-01

One sentence to the `ai-conference-talks` skill cost about **150,000 tokens**.
Measured rather than guessed, the money was all in one instruction. The skill
said *"for the talks that matter, read the full record: `cat
talks/ai-engineer/*-context-engineering-*.md`"*, and a model follows that
literally. Those files inline the whole transcript: of the 2,942 that have one,
the mean file is **33 KB — about 8,500 tokens — and the longest is 420 KB**.
Eight of them is 58,000 tokens before the model has thought about anything, and
the skill also said to *"run several queries with different vocabulary … union
the results"*, at ~6,000 tokens of `--json` each.

Three changes, in descending order of what they were worth.

**`excerpt.py` — read the passages, not the talk.** It takes video ids and a
`-q`, and prints the metadata, the description, the **opening** — where a
speaker states what they are about to argue, which is what makes a passage
lifted from minute 34 attributable — and a window of continuous speech either
side of each passage that matched, merged where those overlap, deep-linked to
the second. It closes with `934 of 3,219 words (29%)`, so a thin excerpt is
visible as one rather than being mistaken for the talk. Passage ranking is the
same `bm25(segments_fts)` that ranked the talk in `query.py`, restricted to the
one talk, so what you read is what put the talk in the results.

Measured over eight topics and 45 talks: **138 of 138 search-ranked moments
land inside the excerpt, on 17.0% of the words** (48,069 of 283,190). The
whole-file recipe and the excerpt recipe were run against the same eight ids
for the same question: **58k tokens against 17k, a 70% cut, with nothing the
search had ranked left behind.**

**`query.py --brief`.** The skill's step 1 is *choosing* talks, and the fields
that help you read a result are not the fields that help you choose one. So
`--brief` drops the channel, the tags, the publication timestamp, the edition
and the second snippet of the same description, and drops four transcript
moments per hit to two. In text mode a 12-hit result set goes from **15 KB to
5 KB**; in `--json` from 25 KB to 10 KB. Default `--json` is byte-identical to
before, which is what `suite-ranking.js` compares against.

**`query.py --ids`,** so reading the hits is a pipe rather than eight ids
retyped: `query.py "…" --ids | xargs python3 excerpt.py -q "…"`.

And one instruction change with no code behind it: cover the vocabulary
**inside one query** — `'evals OR guardrails OR "human in the loop"'` — rather
than by running five and unioning them by hand. FTS5 already ranks the union,
and a talk hitting several of the terms rises by itself; five overlapping
result sets are paid for five times.

### Two bugs found while building it

* **The budget, which is why `-n` is not a count.** The first version merged
  every window around every hit. On a talk that says the query word every other
  minute, six windows each grow to meet their neighbours and the merge returns
  one span covering the talk — the excerpt *was* the transcript, 8,500 tokens
  where 1,500 was asked for, and nothing in the output said so. `-n` is now a
  budget of *n* windows' worth of speech, spent best-ranked hit first, and
  `test_excerpt.py` holds that shape: a hit every 30 seconds through a
  40-minute talk must not come back as more than the budget.

* **Video ids beginning with a hyphen.** `-stDHMwbBRw` is a talk here, and
  argparse reads it as an unknown option and refuses the run — which is exactly
  what `query.py --ids | xargs excerpt.py` produces as soon as one of the hits
  starts with a hyphen. Ids are now lifted out of `argv` before argparse sees
  it, matched on the real shape of a YouTube id.

There is also a correctness fix that the token work only exposed: the excerpt
query needs the same **relaxation** `query.py` does. A segment is ~25 words, so
the strict `"eval" AND "driven" AND "development"` that ranks *talks* correctly
matches no single segment, and the first version fell through its "no hits"
branch to printing the whole transcript. It now retries the OR, and a query
that genuinely matches nothing in a talk returns the opening and says so — the
one thing it must never do is silently cost a full read.

## Review of 2026-09-02 — fixes and improvements to make

A read of the whole solution after the InfoQ fetch landed: the search stack
(`query.py`, `excerpt.py`, `build_index.py`, `atu.py`, `index.html`), the
skill, the pipeline scripts and the workflows. Every item below was verified
against the corpus or by reading the line it names, not inferred; the ones
marked *measured* were run. The offline tests pass, the `ranking` and `search`
browser suites pass 48 of 48, and CLI latency is not a problem — 0.03-0.2 s for
a normal query, 0.6 s for a stopword, 30 s for a full index build. What is
wrong is smaller and sharper than that: three things break the documented
workflow today, the published site is on a growth curve towards the Pages
ceiling, and the ranking has a handful of holes that a natural-language
question falls straight through.

Work them in the order given. The first block is bugs; the second is the site;
the third and fourth are accuracy; the last is the skill, which should be
edited only after the tools it describes have changed.

### Status — 2026-09-02, after the second session

**Every block of this review is done.** The first session left six commits on
`infoq-presentations`, `d8c2c138` through `d830dc0a`, one per block A–C; the
second added D, E, and F with the docs pass. Every offline test passes and the
full browser suite passes 183 of 183 with nothing skipped. Nothing is merged to
`main` and nothing has been pushed — that is *Next steps* 8.

| Block | State |
|---|---|
| **A.1–A.3** | **Done.** `atu.connect()` + `DB_SCHEMA_VERSION`; `quote_term()` in `query.py`; `ids_in_filename()` in `excerpt.py`. |
| **A.4** InfoQ | **Done.** `data/infoq/` turned out to be tracked already (15 files), so that half was moot; the rest — `INFOQ_CLAIMED` carried through `merge_source`, the stale guard, `claim_for_infoq()` two-way dedupe with transcript re-keying, per-edition catalog writes, the `iq-` guards in `fetch_transcripts.select()` and `enrich.select()`, the markdown wording — is in, tested in `test_infoq.py`. **Not done from A.4:** the README sentence about the CSV `youtube_url` → `url` rename (part of the docs pass below). |
| **A.5–A.6** fetcher | **Done.** `RateLimited(TransientError)` with `Retry-After`; `YTDLP_NETWORK_RE`; kome transient after retries; `egress_blocked` riding along so a verdict after a block still benches; `--probe` gets the real misses; `enrich.BLOCK_MARKERS` anchored; `--out` mkdirs; `--limit`+`--retry-after` prints a note; README worker default. One existing test changed meaning: a persistent supadata 429 is now asserted *not* to be a block. |
| **B** site | **Done** in the tree, **not yet run in CI** — see the Workflows row above. `tools/assemble_site.sh` is shared by `pages.yml` and the new checks at the end of `suite-navigation.js`. `_site/` is gitignored. |
| **C.1–C.6** ranking | **Done.** Details in the `d830dc0a` commit message. Measured: the eight ranking queries keep 6–10 of their previous top 10; browser agreement margins 10, 9, 6, 6, 10, 6, 10, 9 of 10 (threshold 4) — "fine tuning" and "retrieval augmented generation" each fell from 8 to 6, still comfortably green, both re-read by hand and good on both sides. `PASSAGE_WORDS` is 24 (was 25) so the stride divides evenly; `tindex/` and `search-meta.json` were regenerated and committed (`x: 1` on the 44 estimated-timing talks, which `index.html` does not read yet). |
| **D** speakers | **Done.** NFKC before the heading regex, the bullet and bare lines under it, `&`/`and`/`+` splits with the every-part rule, the `by Name` tail, `[TAG]` stripping, role words in `NOT_A_NAME`. 1,557 talks gained a speaker; missing fell 5,601 → 4,066. The one real name lost is Charles Humble, named on 19 GOTO talks and therefore over the 10% host ceiling. `test_speakers.py`. |
| **E** browser | **Done.** Porter stemming on both sides (`atu.stem()`, the JS twin, `test_stem.py`); description postings and the metadata df in the shards, so the 300-character clip is display only; relaxation with a status-line note, typo first then commonest — the same fix went into `query.py`, whose relaxation used to drop the real word and keep the typo; token-exact highlighting on stems; `~` on estimated moments. The single-use term cut stays for transcript-only terms; a term in even one description is kept. |
| **F** skill | **Done.** `query.py --stats` exists (`--json` too) and the skill sends the model there instead of quoting a count; the rest of the list in section F is in the text. |
| Docs pass | **Done.** README header, *Who gave the talk*, the CSV column, *From the terminal*, the browser paragraph, *What gets published*, the stemmer paragraph under *Rebuilding*, the new tests in *Layout* and *Testing*, the 2026 counts; this file's tables. |

What the second session learned, for whoever touches these next:

* **Verify with**: `cd tools && python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py && python3 test_speakers.py && python3 test_stem.py && python3 test_fetch_transcripts.py`, then `cd uitest && node run.js` (all nine suites, about four minutes). The first `query.py` call rebuilds `talks.db` (48 s) if `data/transcripts/` or `talks.json` is newer than the DB on disk — `atu.db_stale()` working, not a fault.
* **The speaker rules are exact on their line arithmetic.** `DESC_SPEAKER_RE` must use `[ \t]*` after the colon, not `\s*` — `\s*` eats the newline and hands "* Joshua Corbett" to the name test, which rejects the bullet — and the line after the heading is counted from `m.end()`, not `m.start()`, because the pattern's leading `^\s*` matches the blank lines above the heading. Both mistakes were made and each looked like "the heading is never found".
* **`build_index.py` must iterate the shard terms sorted.** A set's order differs run to run, and the build's byte-identity — which the README promises and the review verified — quietly went with it until two consecutive builds were diffed.
* **The stemmer is memoised** (`functools.lru_cache`): un-memoised it took the build from 48 s to 1 m 54 s on ~30 million transcript tokens.
* **Relaxation order matters in both rankers**: "drop the commonest word" on `kubernetes zzzz` dropped *kubernetes*, since the typo is present in zero talks and so is never the commonest. A word present nowhere goes first.

### A. Bugs that break the documented workflow

1. **A stale `talks.db` crashes every query.** `query.py` selects `url` and
   `youtube_url`, which the DB on disk did not have — every search died with
   `no such column: url`. `query.py:477` and `excerpt.py` rebuild only when the
   file is *missing*, never when the schema or `talks.json` is newer, and the
   README's "delete it any time" is the only remedy. Since the skill's first
   step is `query.py`, a stale index is either a crash or, worse, an index that
   quietly lacks the last refresh's talks. Fix: `build_sqlite` sets
   `PRAGMA user_version = <SCHEMA_VERSION>`; `connect()` in both tools rebuilds
   when the version differs *or* `TALKS_JSON` is newer than `TALKS_DB`, and
   says so on stderr. Put `connect()` in `atu.py` so the two tools cannot
   drift. (The DB was rebuilt by hand during the review; it is gitignored.)

2. **The OR query the skill recommends fails on hyphenated terms.**
   *Measured:* `gpt-4 OR claude` → `no such column: 4`; `fine-tuning OR rag` →
   `no such column: tuning`; `c++ OR rust` → `syntax error near "+"`; any comma
   in an explicit query is a syntax error. `explicit_query` (`query.py:122`)
   joins bare terms unquoted, and an FTS5 bareword is `[A-Za-z0-9_]` and
   non-ASCII only. Fix: in `explicit_query`, wrap every term that is not
   already quoted and not a pure bareword in `"…"`, preserving a trailing `*`
   (`gpt-4*` → `"gpt-4"*`), and drop bare commas. Add these four strings to a
   `test_query.py` — there is none, and `parse_query`/`explicit_query` are pure
   functions that deserve one.

3. **`excerpt.py` cannot open a markdown path for most ids.** `find_talk`
   (`excerpt.py:110`) takes the text before the *first* hyphen of the file
   name, so `talks/ai-engineer/O72p-rBb2bA-evals-….md` resolves to `O72p` and
   reports "not in the corpus" — *measured*. Every id containing a hyphen
   (about one in six), every id starting with one, and every `iq-` id fails,
   which is precisely the input the skill's "reading the markdown file directly
   is for the record" sentence produces. Fix: take the first 11 characters when
   `atu.is_youtube_id()` accepts them; otherwise try each hyphen-delimited
   prefix of the name against `talks.id`, longest first.

4. **The InfoQ fold-in is fragile in the working tree.** Three separate
   things, all found by the pipeline review:
   - `data/infoq/` is **untracked**, and `sync_infoq` deletes every `iq-`
     record when the cache directory is empty — which is what
     `kb-refresh.yml`'s checkout would see. 222 talks would vanish under the
     10% shrink guard, unflagged. Commit the directory, and make `sync_infoq`
     keep the cached videos and set `stale: true` when the cache is missing,
     the way an empty listing already does.
   - `sync_catalog.py --refresh` strips what `infoq.py` wrote onto a matched
     YouTube record: `speakers`, `year`, `label`, `page_url`, `infoq_url`,
     `infoq_at` are not in the `carried` list at `sync_catalog.py:251`, and
     the cache's `matched_youtube: true` means it is never re-applied. Latent
     today, fails on the first weekly refresh. Add them to `carried`.
   - `atu.is_youtube_id()` accepts an `iq-` id of exactly 11 characters
     (`iq-ai-infra`), which would give it a `youtube.com/watch?v=iq-…` link.
     Exclude the `iq-` prefix. `fetch_transcripts.select()` and `enrich.py`
     have no guard either and would send such an id to Supadata or the Data
     API; add `if not atu.is_youtube_id(t["id"]): continue` to both.
   - Smaller: `infoq.py` writes the catalog only at the end of `main`, so a
     Ctrl-C between editions leaves a transcript on disk that the catalog never
     learns about; write after each edition. Dedupe is one-directional — an
     `iq-` talk that later appears on the channel becomes a permanent
     duplicate; drop an `iq-` record whose `title_key` matches a YouTube record
     in `build_talks`. `excerpt.py:226` labels an InfoQ abstract "YouTube's,
     not an abstract", and the markdown says "No description published on
     YouTube" for `iq-` records. The CSV column `youtube_url` → `url` rename is
     unmentioned in the README.

5. **Transient failures become permanent misses in the fetcher.** A yt-dlp
   `TimeoutExpired`, a DNS failure, a dead proxy or a kome 5xx is mapped to
   `LookupError` (`fetch_transcripts.py:538-548`, `:321-324`), which
   `about_the_video()` does not exempt, so it is written to `_misses.json` and
   `select()` skips the talk forever. A proxy that dies mid-run records every
   talk it touched as "no captions". This is the failure class *The 402 that
   was recorded as "no captions"* was about, still open on two routes. Fix:
   raise `TransientError` for the subprocess timeout and for network-shaped
   yt-dlp stderr, and after kome's retry loop. Three related ones:
   - `--probe` reports a healthy IP as failed once the next unfetched talk is
     a known no-captions video (`main:972` passes `{}` for misses to
     `select`). With the 2026 scope complete, `--probe --min-year 2026` now
     always probes a captionless video. Pass `load_misses()`.
   - A Supadata "no captions" verdict is overridden by an earlier IP block
     (`fetch_one:714`, `raise blocked or last`), so the talk is re-selected and
     re-charged every round. Prefer a non-IP route's `LookupError`.
   - A Supadata 429 raises `BlockedError` and benches the *local* IP for 45
     minutes, and 429s are never printed — the README's "raise `--workers`
     until 429s appear in the log" cannot happen. Give it its own
     `RateLimited(TransientError)`, log it, honour `Retry-After`.
   - `enrich.py:114` matches the substring `blocked`, which yt-dlp also prints
     for one geo-restricted video, and aborts the whole run. Anchor on "Sign in
     to confirm" / "HTTP Error 429".

6. **Small.** `build_index.py --out DIR` fails unless DIR exists
   (`redirect_outputs` should `mkdir -p`). `--limit` silently disables
   `--retry-after`. README says workers default to one per identity; the code
   says `max(2, …)`.

### B. The published site is the whole repository

`pages.yml` force-pushes `main` to `gh-pages`, so the site is every byte of the
repo: **411 MB today, 41% of GitHub Pages' 1 GB ceiling**, and 169 MB of it is
never fetched by the browser — `talks/` markdown (114 MB), `data/catalog/`
(25 MB), `talks.json` (19 MB), `talks.csv` (11 MB).

The growth curve is the reason to act now rather than later. A transcript is
~62 KB and covers 3,170 of 9,048 talks; at full coverage that is ~560 MB of
transcripts plus a proportionally larger `tindex/`, about **850 MB** — too
close to the wall to leave to the next refresh. The fix is to publish only what
`index.html` fetches, which is exactly four things: `data/search-meta.json`,
`data/tindex/`, `data/transcripts/<id>.json`, and itself. That drops the site
to ~240 MB immediately, and keeps the markdown and the catalogs on `main`
where they are the readable, diffable artifact.

Replace the single `git push` step with an assembled tree, pushed as one orphan
commit so `gh-pages` carries no history of its own:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Assemble the site — only what the browser fetches
        run: |
          set -euo pipefail
          rm -rf _site && mkdir -p _site/data
          cp index.html .nojekyll _site/
          cp data/search-meta.json _site/data/
          cp -r data/tindex _site/data/tindex
          cp -r data/transcripts _site/data/transcripts
          rm -f _site/data/transcripts/_misses.json    # bookkeeping, not content
          du -sh _site _site/data/*
      - name: Publish as a single orphan commit
        run: |
          set -euo pipefail
          cd _site
          git init -q -b gh-pages
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -q -m "Publish ${GITHUB_SHA::8}"
          git push --force "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Three things to check when it goes in. `index.html` must still fetch nothing
outside those paths — grep it for `fetch(` and `href="data/`; today it does not.
The `navigation` UI suite serves the repo root and would not notice a path the
site lacks, so add one check that runs against an assembled `_site/` rather
than the checkout. And the `du` line is the size report: read it on every
deploy, since the `search-meta.json` trigger in `build_index.py` watches the
up-front payload, not the site.

When transcripts alone approach the ceiling, the next lever is the transcript
files themselves rather than the site layout: `duration` is unused by the
browser and `start` carries two decimals it never displays, and stripping both
at publish time is ~30% of the bytes without touching `data/transcripts/` on
`main`. That is a `build_index.py --site` step later, not now.

### C. Ranking — where a natural-language question falls through

The rankers are sound on keyword queries; the browser suite says so, and so
does reading the results. The holes are all at the edges of what a query is.

1. **Stopwords are ANDed into the strict query** (`query.py:158`).
   *Measured:* "how do you evaluate agents in production" is `"how" AND "do"
   AND "you" AND "evaluate" AND "agents" AND "in" AND "production"`. The
   transcript layer contributes nothing — seven words never share a 25-word
   passage — and the four top hits were metadata-only talks whose descriptions
   contain "how", "do", "you" and "in", with those words highlighted. The same
   query as "evaluate agents production" returned four transcript-bearing
   talks that were plainly better. Fix: build `strict` from the content words,
   falling back to all words only when every word was a stopword. The
   `relaxed` form already does this; the strict one should too.

2. **Relaxation is a cliff.** AND-everything jumps to OR-anything only at zero
   rows, so a question with one wrong word either returns a few accidental
   matches and never relaxes, or drops to OR and lets a common word win:
   "what do people say about agent reliability" relaxed to
   `people OR say OR agent OR reliability` and ranked *Your People Are The
   Future Of Your Brand* first — *measured*. Two changes, both cheap:
   - Relax **progressively**: drop the term with the highest document
     frequency and retry, until one term is left, before going to OR. The
     `fts5vocab` shadow table (`CREATE VIRTUAL TABLE v USING
     fts5vocab(talks_fts, 'row')`) gives the frequency in one query per term.
   - Add a query-time stopword list — `people say said talk talks think
     discuss mention cover speaker conference` and the question words — that
     applies only to queries, so the index and the browser are unchanged.

3. **The segment layer should always score the OR form with a co-occurrence
   bonus**, which is what `index.html`'s `passageFactor` already does and
   `query.py` does not. Under the strict form, a two-word query gets moments
   only from passages that say both words; under the relaxed form it gets
   moments from either and cannot tell. Score segments on the OR form, then
   multiply a talk's `seg` by `1 + PASSAGE_W · min(1, log1p(together)/log 4)`
   where `together` counts passages matching every content term — the same
   constants as the browser, so the two rankers agree by construction rather
   than by the `ranking` suite's 4-of-10 threshold.

4. **Passages do not overlap** (`build_index.py:161`, `PASSAGE_WORDS = 25`).
   A phrase or a term pair that straddles a boundary matches neither passage,
   so `"spec driven development"` and "said together" ranking silently miss a
   share of hits that depends on where the cut fell. Emit passages at a
   half-passage stride: roughly double the `segments` table (548k → ~1.1M rows,
   185 → ~350 MiB for `talks.db`), unchanged `tindex/` if positions keep
   counting the un-overlapped index. Measure before and after with the eight
   `ranking` queries.

5. **Estimated timings are not surfaced.** 44 InfoQ transcripts carry
   `"timing": "estimated"`, and only the markdown says so; `query.py` and
   `excerpt.py` print those stamps exactly like exact ones, so an answer will
   cite "at 12:34" for a position interpolated from word count. Add a `timing`
   column to `talks`, prefix estimated stamps with `~` in both renderers, and
   put the field in `--json`.

6. **Missing filters.** There is no `--transcript` filter, which the skill's
   "quote only from transcripts" needs — the browser has one. `--conference`
   and `--year` take one value; make them repeatable, and add `--min-year` as
   the fetcher already has it.

### D. Speakers — the field with a 4× weight is 63% empty

*Measured:* 5,603 of 8,822 talks (pre-InfoQ count) had no speaker, and
`speakers` is weighted 4.0 in `talks_fts` and 4 in the browser, so a query
that names a person misses most of what that person said. Two fixes recover
about a quarter of the gap from data already on disk:

| Cause | Talks recoverable | Fix |
|---|---|---|
| Descriptions carry a **`𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:`** heading in Unicode mathematical-bold letters, followed by a `* Name` bullet list — Microsoft Ignite 732, Build 172, AI Council 68, MLOps World 49 | **1,057** | `unicodedata.normalize("NFKC", desc)` before `DESC_SPEAKER_RE` (`sync_catalog.py:345`), and read the bullet lines that follow the heading, not only the same line |
| Titles of the form `Topic — A & B, Company` or `A and B` — AI Engineer, GOTO, AI Council | **~440** | In `speakers_from_title` (`:377`), split a segment on `&`, `and`, `+` and accept the segment only if **every** part passes `name_like`; a comma still cuts to the part before it. Splitting without the every-part rule produced "Web Scraping" and "Hours of Speech" as speakers — measured, and why the rule is there |

Conferences at 99% missing — Ignite, Build, re:Invent, Devoxx, QCon's YouTube
side — are the first row plus the `by Name` pattern Devoxx uses in titles.
After the change, re-run `sync_catalog.py` (offline) and check the
`speakers` diff by conference before committing; a false positive puts a
brand into the heaviest-weighted field of every one of its talks.

### E. The browser diverges from the CLI

- **No stemming.** `talks.db` tokenises with `porter unicode61`; the browser
  index uses `atu.tokenize` as-is. "evaluate" does not find "evaluation" in
  the browser, "agents" does not find "agent" unless the prefix rule fires,
  and the prefix rule (`index.html:360`) fires only when the exact key is
  absent and then takes an arbitrary first twelve keys of the shard. Build
  `tindex/` from stemmed terms — a Porter implementation is ~120 lines in
  either language, and there are audited ports of the same algorithm — and
  stem the query in JS. The `ranking` suite is the regression test.
- **Descriptions are searched on their first 300 characters only**
  (`META_DESC_CHARS`, `build_index.py:122`), because the whole text ships in
  `search-meta.json` and that file is at 91% of its 6 MiB trigger. Move the
  description *terms* into the sharded index — same postings format, a
  `metadata` flag on the posting — and keep only the display clip in
  `search-meta.json`. That widens recall and shrinks the up-front payload at
  once, and removes the trigger's reason to exist.
- **No relaxation at all** (`index.html:420`): every term must appear
  somewhere. A one-word typo is "Nothing matched". Drop the highest-DF term
  and retry, as in C.2, and say so in the status line.
- **The single-use term cut** (`build_index.py:378`) drops any term said once
  in one talk. That is the size trade-off working as designed, but it makes a
  name spoken once unfindable; if E.2 shrinks the payload, revisit.

### F. The skill, after the tools have changed

Edit `.claude/skills/ai-conference-talks/SKILL.md` last, once A.2, C.5 and C.6
exist, so it describes tools that do what it says.

- **Hard-coded counts go stale on every fetch** (`SKILL.md:37` says 2,942 of
  8,822; it is 3,170 of 9,048 now). Add `query.py --stats` — talks,
  transcripts, conferences, years, per-conference transcript coverage — and
  tell the skill to run it instead of quoting numbers.
- **Search with content terms, not the question.** Until C.1 and C.2 land,
  "what do people say about X" is a worse query than "X"; say so, with the
  example above. Even after, name the rule.
- **Hyphenated terms must be quoted inside OR queries** until A.2 lands:
  `"fine-tuning" OR rag`.
- **The deep-link template is YouTube-only** (`SKILL.md:131`). Use the `url`
  field from `--json`; InfoQ pages take no `&t=`; and once C.5 exists, cite a
  `~` timestamp as approximate, never to the second.
- **Say what `year` means**: the edition year, not the publish date — InfoQ
  drips recordings for a year, and the browser's "newest" sort is by
  `published_at`.
- **Prefer quotable talks explicitly**: `matched` and `has_transcript` in
  `--brief` are how; `--transcript` (C.6) is the filter.
- **`-n` on `excerpt.py` is a budget of speech, not a count**, and a
  multi-word `-q` falls back to OR inside a talk, so passages rank by the
  rarest term — say both, so the model does not read `-n 3` as "three
  quotes".
- The fetch section is right on flags; add that `--limit` disables
  `--retry-after`, and that the probe's false negative (A.5) exists until
  fixed.

### What the review confirmed clean, so nobody re-derives it

`check_registry.py` passes; `test_excerpt.py`, `test_fetch_transcripts.py`,
`test_infoq.py` pass; the `ranking` and `search` browser suites pass 48/48
against the rebuilt DB. `sync_catalog.py` without `--refresh` was proven
byte-idempotent on a copy, `generated_at` included, and the CSV round-trips
with multi-line descriptions. The committed `search-meta.json` and every
`tindex/` shard are byte-identical to a fresh build of the committed
`talks.json`. `import_kb.py`, `refresh_report.py`, `segment_plain_text` and
`year_in_text` had nothing to report. Every flag the README and the skill
name exists.

## Next steps, in order

1. ~~**Enable GitHub Pages** on the `gh-pages` branch.~~ **Done** — the site
   serves at <https://ppruchnerovic.github.io/ai-talks-universe/>, `gh-pages`
   matches `main` commit for commit, and a browser run against production loads
   the catalogue in 777 ms, searches, and deep-links into transcripts from the
   lazily-fetched shards.
2. ~~**Work the bug list.**~~ **Done** — all fourteen fixed on 2026-09-01, see
   *The bug list, worked*. What is left from it is deliberate, not forgotten:
   the ten `hi` transcripts that no route can improve, the `yt-dlp --sub-langs`
   hole, and the `count` drift that needs a `--refresh`.
   `ranking`, by contrast, is green, and that is worth reading as evidence
   rather than as a fix: it asserts 4 of the CLI's top 10 land in the web's
   top 40, and
   **"inference"** was failing at 1 of 10 until the 2026 extraction, after which
   it passes untouched. `moments` and `multi agent` did the same thing earlier.
   Three queries have now started and stopped failing on their own, which says
   the check measures corpus size as much as ranking quality — the rankings were
   re-read by hand each time and were good on both sides of every flip. Changing
   what it measures is still the right fix; a green run today is not it — this
   remains the one open test-quality item. The 2026-08-31 margins, for whoever changes it: 10, 10, 10, 8, 8, 8, 6 and 10 of
   the CLI's top 10 inside the web's top 40, against a threshold of 4. Only
   "agent evaluation" at 6 is anywhere near it, and "inference" now sits at 8.
3. **Re-run the UI tests** after any collection run: `cd tools/uitest && node run.js`.
   They degrade to `SKIP` rather than failing when a fixture has not been
   collected yet, so a green run on a thin corpus is weaker evidence than a
   green run on a full one — read the skip count, not just the failures. The
   last full run (2026-09-02, 183 checks) skipped **nothing**, which is the
   strongest that evidence has been: every conditional fixture now exists in
   the corpus.
4. ~~**Fetch the 422 pending 2026 talks, then rebuild and commit.**~~ **Done**
   on 2026-09-01 — 420 fetched, 2 genuine misses, indexed and verified; see
   *Closing the 422* for what it cost and what it taught. The one talk that
   later entered the scope — `I1GvlW1H4WI`, from the year-fallback fix in *The
   pre-2023 cut* — was fetched the same way for one credit. The recipe below
   stands for the next time a refresh brings talks in:

   ```bash
   cd ~/git/ai-talks-universe/tools
   source ~/.bash_profile                    # SUPADATA_API_KEY + YOUTUBE_API_KEY; not optional

   .venv/bin/python fetch_transcripts.py --probe                 # 1 credit, tells you which route
   .venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --workers 32 \
     && .venv/bin/python sync_catalog.py \
     && .venv/bin/python build_index.py     # chain them: an unindexed transcript is a credit wasted
   ```

   Then check, before committing — each of these is a bug this repo has actually
   had:

   ```bash
   python3 - <<'EOF'                        # every miss must be about the video:
   import json                              # no captions, or a members-only 403.
   d = json.load(open('../data/transcripts/_misses.json'))
   for v in d.values(): print(v.get('detail'))   # NOT 'reason' — see below
   EOF

   cd uitest && node run.js && cd ..        # 183 checks; read the skip count too
   ```

   The fetch should report **422 selected** — `berkeley-agentic-ai-summit` 159,
   `ai-council` 94, `mcp-dev-summit` 85, `lf-ai-dev` 70, `sequoia-ai-ascent` 14
   (`microsoft-ignite` and `yc-ai-startup-school` have no 2026 talks, so a
   `--min-year 2026` run takes nothing from them). A different number means the
   selection is not what this file describes — check before spending credits.

   `build_index.py` prints where `search-meta.json` stands against its 6 MiB
   trigger; transcripts do not go into that file, so this run should not move
   it. Then commit `data/`, `talks/` and the refreshed numbers in `README.md`
   and this file — see *Numbers to refresh when the corpus changes*.

   Two things not to redo while in there: the ten `hi` talks were refetched on
   2026-09-01 and came back `hi` again, so do not delete and refetch them a
   third time (*Bug 7 cannot be fixed by refetching*), and spending the credit
   remainder on pre-2026 talks is a change of policy rather than a backlog
   (*Collection is scoped to 2026*).
5. Re-check the conferences that came back thin — done for three of the four,
   and only one is a real question. `apple-wwdc` (115 enumerated → 7),
   `meta-connect` (41 → 9) and `tedai-vienna` (11 → 6, the drops being "Opening
   Gala", "Highlights" and "TED Talks Day") are the filter working: WWDC is
   SwiftUI and visionOS, Connect is VR, and the TEDAI playlist really is that
   small. **`owasp-global-appsec` is the open one**: 28 enumerated, 2 kept, and
   the 26 dropped are the AppSec programme — threat modelling, unicode
   normalisation, PKI, security champions. That is the same argument that gave
   the WeAreDevelopers seed `"scope": "all"`, so it is a curation call rather
   than a bug: is a security conference's non-AI half worth having in an AI
   talks corpus? `fully-connected-wandb` came back at 49 and is off this list.
6. Backfill the pre-2026 descriptions if anything ever wants them: the year
   filter skipped 4,823 videos, which is one `enrich.py --all` without
   `--min-year` and about a hundred quota units. Nothing depends on it — the
   2026 scope is a selection policy, not a coverage target. It is a smaller job
   than it was: 503 of those videos are now below the corpus floor and no longer
   in `talks.json` at all, though enrichment still reads them from
   `data/catalog/`, which is what would let the floor move back down.
7. ~~**Work the 2026-09-02 review**, in its own order.~~ **Done** — A–F and
   the docs pass, nine commits on `infoq-presentations`, every test green; see
   *Status* under *Review of 2026-09-02*.
8. **Merge `infoq-presentations` to `main` and watch the first `pages.yml`
   run**: it is the rewritten workflow's first deploy. Read the `du` lines in
   the *Assemble the site* step (expect ~249 MB), then load the site and use
   "Find this in the talk" once.

## Handoff — running a transcript extraction

**Nothing is pending.** The 422 talks the seven new conferences brought in were
fetched on 2026-09-01 (*Closing the 422*), and the one the year-fallback fix
later moved into the scope went the same way (*The pre-2023 cut*). The
commands are in *Next steps* item 4 and are the same shape as any future
selection:

```bash
cd ~/git/ai-talks-universe/tools
source ~/.bash_profile                     # see below — this is not optional
.venv/bin/python fetch_transcripts.py --probe
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --workers 32 \
  && .venv/bin/python sync_catalog.py \
  && .venv/bin/python build_index.py
```

`--min-year 2026` re-derives its work from disk every time, so it selects
exactly what has no transcript yet — there is no list to keep and a rerun after
an interruption is safe. The ten `hi` talks were refetched on 2026-09-01 and
came back `hi` again; do not delete and refetch them a third time, and see *Bug
7 cannot be fixed by refetching* before deciding they look like a backlog. As of
that date the probe reports **both free exact routes usable** — the residential
IP has recovered — so `--source exact` is worth a look first if you would rather
spend a sitting than credits; it yields ~25 talks before the IP closes, against
~250 a minute on Supadata.

After any run, **check the languages of what arrived**, since `--source exact`
is the free-route path and route 2's `--sub-langs` hole is still open:

```bash
python3 - <<'EOF'
import json, glob, os
for f in glob.glob('data/transcripts/*.json'):
    if f.endswith('_misses.json'): continue
    L = (json.load(open(f)).get('language') or '')
    if not L.lower().startswith('en'): print(os.path.basename(f)[:-5], L)
EOF
```

A line here is not automatically a problem — the corpus holds Japanese, Spanish
and German talks that really are in those languages. What it catches is the
other kind: an English talk whose only caption track is somebody else's ASR.

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
- **~2,370 of the month's 3,000 credits are spent**, after the 422-talk run.
  Credits ≈ talks, so a run needs no headroom beyond its own selection count.

## The quota — read this before a transcript run

Carried over from the WeAreDevelopers corpus, where it cost a day to establish,
and confirmed again here (blocked at 52 on a residential connection, 37 the
next day).

| Egress | Fetched before the block |
|---|---|
| Corporate NAT (Zscaler) | 235, then 52 in a later sitting |
| Residential ISP | 25, and 52 then 37 here |
| Mobile carrier | 22 |

**Read the Zscaler row with suspicion.** On 2026-09-01 a probe down that egress
reported `BLOCKED — spent`, and it was not the allowance: with Zscaler stopped,
the same probe on the same video minutes later returned 15,871 words. The
fetcher cannot tell a proxy interception from a YouTube block, so an unknown
share of what that row records may be the proxy rather than the quota — see
*Closing the 422*.

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
  IP block: benching an identity would not help. This property was documented
  before it was true — see *The 402 that was recorded as "no captions"*.

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

- **The transcript index is sharded two characters deep, and `shard_key()` in
  `build_index.py` must agree exactly with `shardKeyOf()` in `index.html`.**
  There is no shard-*count* knob: the key is the term's prefix, so the depth is
  the count. One character meant every term starting with "s" shared a 4.0 MB
  file that was downloaded whole to answer one query; two gives 674 shards, a
  1.7 MB worst case and a 1.2 KB median, for the same 38.4 MB total — this buys
  query cost, not repo size. The constraint that sets the depth is that terms
  sharing a prefix must share a shard, because the browser resolves "agent" ->
  "agentic" by scanning the keys of the one shard it fetched. Two is the
  deepest split that keeps that for free, since both tokenizers drop terms
  shorter than two characters and the shortest possible query term is
  therefore exactly a whole key. Going deeper needs the browser to fetch every
  shard matching a short prefix, which is a real change rather than a constant.
  A disagreement between the two functions is **silent**: the browser asks for
  a shard the manifest does not list, gets nothing, and transcript search
  quietly degrades to metadata-only hits.

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
  run, and now raise `AccountError` for the same reason 429 raises
  `BlockedError` — see below.

- **Four kinds of failure, and only one of them is a fact about the video.**
  `_misses.json` is permanent, so what may be written there is the whole
  question. A `LookupError` is a verdict on the talk (no captions, 206, 404, a
  job that came back failed); `BlockedError` is a verdict on our IP, which
  benches that identity and retries the talk elsewhere; `AccountError` is a
  verdict on our account, which benches nothing — no other IP has a fuller
  balance — retires the route and ends the round; `TransientError` is no
  verdict at all, so it benches nothing and ends nothing, and the talk simply
  waits for a rerun. `about_the_video()` is the one predicate the two runners
  ask before writing a miss, which is what makes a new failure class retryable
  by default instead of silently permanent — the previous arrangement asked
  `is_block()`, so everything that was not an IP block was cached forever.

- **Collection is scoped to 2026, the corpus to 2023, and enumeration to
  nothing.** Three lines for three costs, and collapsing them is the mistake.
  `enrich.py` and `fetch_transcripts.py` both take `--year` / `--min-year` /
  `--include-unknown-year`, and the standing intent is `--min-year 2026`: an
  allowance that refills over hours should not be spent on talks that have gone
  stale. That one filters *selection only*. The corpus line is the registry's
  `"min_year": 2023`, applied once at derive time and overridable per conference
  — see *The pre-2023 cut*; `query.py --year` still reads every year the corpus
  has. Enumeration has no line at all: `data/catalog/` caches all 17,677 videos
  whatever the other two say, because listing is free and it is what makes both
  of them reversible without a fetch. On enrichment, add `--include-unknown-year`:
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
  that only says it out loud, at rank 14 (it was rank 4 when this was written;
  the rank drifted with the corpus, the property did not).

- **A bare query is ANDed, then relaxed; explicit FTS5 syntax never is.** ANDing
  every token is right for a keyword query and returns nothing at all for a
  natural-language question, which is how an agent actually asks. So a bare
  multi-word query falls back to an OR of its content words *only when the AND
  matches nothing*, and says so on stderr — ranking still puts the talks matching
  every term, together, on top. Anything the user typed as FTS5 (`"phrase"`,
  `OR`, `NOT`, `prefix*`) is passed through verbatim and never relaxed, because
  guessing at explicit syntax is how a search silently stops meaning what it says.

- **Query terms are de-duplicated and capped, and this was a complexity fix.**
  A pasted blob scaled super-linearly — `agent` x400 took 169 seconds. Bare
  queries de-duplicate case-insensitively and cap at 32 terms with a warning;
  explicit syntax is de-duplicated only in a flat chain joined by a single
  idempotent operator, never across parentheses, `NEAR`, `NOT` or mixed
  operators. Same query now runs in 0.19s, and the worst case anywhere is 1.5s.

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
  6,979 talks with 5,138 — past the line that was set as the trigger, so
  the clip halved and it came back to 5.4 MiB. Seven new conferences then took
  it to **7.76 MiB (8,135,293 bytes), 129% of the trigger**, and the documented
  remedy was applied again: `META_DESC_CHARS` 600 -> 300, back to **5.79 MiB
  (6,068,517 bytes)**, 96% at 9,325 talks with 7,313 descriptions. That is the
  second halving, so a third crossing is better met by moving descriptions out
  of the up-front download than by clipping them to 150 characters.
  **The trigger's unit is binary and now says so in code**:
  `META_SIZE_TRIGGER_BYTES = 6 * 1024 * 1024` = 6,291,456 bytes. This mattered —
  the file is *under* 6 MiB but *over* 6 MB decimal, so the ambiguity alone
  decided whether the clip needed halving. **`atu.human_size()` was fixed to
  match on 2026-09-01**: it always divided by 1024 while labelling "MB", so
  every size this repo ever printed looked decimal and was not. It now says
  `MiB`, and `atu.decimal_size()` exists for comparing against a vendor figure.
  The divisor did not change, so no recorded number moved — only the labels, and
  historical "MB" figures in this file are all MiB. `build_index.py` reports
  where the file stands after each run.
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

`query.py --stats` prints the talk, transcript, conference and year counts
from the index, per year and per conference — start there. `README.md` states
9,048 talks / 3,174 transcripts / 53 conferences / 17,677 enumerated, and how
many of them are 2026 and how many of those are transcribed; this file states
transcript, description, year, tag and speaker coverage, the per-conference
transcript split, the 2026 pending backlog, the passage count, the credits
spent this month, and the sizes of `talks.db`, `search-meta.json` and
`tindex/`. `sync_catalog.py` prints the coverage at the
end of a run and `build_index.py` prints the passage count, the sizes and where
`search-meta.json` stands against its 6 MiB trigger.

Count transcripts by **exact video id**, never by filename prefix: 48 ids begin
with an underscore and `_misses.json` lives beside them, so a prefix filter
under-reports by 48. This has now caught two separate sessions.

## Not done

- **Retrieval is a ladder, and the skill states what a question should cost.**
  `query.py --brief` chooses talks, `excerpt.py` reads the passages, the
  markdown file is for the record rather than for a quote. This is written down
  as a budget — "one search and a handful of excerpts, on the order of 15k
  tokens, not 150k" — because a model given "read the matching talks" reads
  them whole, and there is no signal in a 33 KB file that says it was 8,500
  tokens to learn one paragraph. The cost of a wrong instruction here is not a
  wrong answer; it is a right answer at ten times the price, which nothing in
  the output makes visible.

- **No semantic/vector search.** BM25 plus an agent reading the ranked passages
  has covered the query patterns so far. If "find talks that mean X without saying
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
