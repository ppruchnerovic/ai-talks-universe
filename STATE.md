# State and handoff

Where the corpus and the tools stand today, and how to run the next collection
without repeating a mistake this repo has already made. This is the file to
read first in a new session; it is meant to stay short.

| File | What it holds |
|---|---|
| `README.md` | the user-facing documentation: what the corpus is, how to search it, how to rebuild it |
| **`STATE.md`** (this file) | the state table, the handoff recipe, the quota, and the numbers to refresh after a run |
| `ARCHITECTURE.md` | the diagrams — pipeline, data flow, the fetcher's routes and failure classes, both rankers, CI — and the design decisions not to relitigate |
| `TODO.md` | everything open, one list |
| `HISTORY.md` | the dated write-ups of every session's work, verbatim; where the numbers and decisions here get their provenance |

Built by porting the WeAreDevelopers talk knowledge base at
`../presentations/kb/` (see its `README.md` and `STATE.md`) onto a different and
harder data source. The search machinery — SQLite FTS5 + a sharded browser
index, passage-level co-occurrence ranking, the transcript fetcher's routes and
quota handling — is that design, carried over deliberately. What is new here is
the catalogue layer, because there is no agenda API.

## Where things stand

| Piece | State |
|---|---|
| Registry (`conferences.json`) | Done. **53 conferences, 84 sources** — 83 YouTube listings and one `"type": "videos"` seed — mirrored from `ai-conferences.md`; `check_registry.py` passes. Seven conferences added 2026-09-01, see *The seven conferences added on 2026-09-01* in `HISTORY.md`. |
| Enumeration (`sync_catalog.py`) | Done. **17,677 videos** cached in `data/catalog/`, **8,826 surviving talks** — 9,325 before the 2023 year floor, see *The pre-2023 cut* in `HISTORY.md` — plus **222 InfoQ-only presentations**, **9,048 in the corpus**. 8,468 of them enumerated from YouTube, 358 seeded — see *The WeAreDevelopers import* in `HISTORY.md`. |
| Speakers | **4,982 of 9,048 (55%)** since 2026-09-02, up from 3,447 (38%): the bold-Unicode `Speakers:` heading Microsoft's channels use, the `A & B, Company` and `by A and B` title shapes. See *Review of 2026-09-02* in `HISTORY.md`, section D, and `test_speakers.py`. |
| Enrichment (`enrich.py`) | Done for the 2026 scope. **9,598 videos via the Data API**, in one run. See *What the collection runs actually got* in `HISTORY.md`. |
| Per-talk markdown | Done. 9,048 files, regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. Since 2026-09-02 the passages overlap at a half-passage stride and `talks.db` carries `PRAGMA user_version` (`atu.DB_SCHEMA_VERSION`, now 6 — the topic column and `talk_topics` join table came in on 2026-09-02) — 379 MiB, 48 s to build, and `atu.connect()` rebuilds it by itself when it is stale. The browser index is **keyed on Porter stems** (`atu.stem()`, memoised; the same function in JavaScript inside `index.html`, `test_stem.py` diffs them over the corpus vocabulary) and carries the **whole description's postings** per stem (`d`) plus the metadata document frequency (`m`): 46 MB in 712 shards, 52,327 stems, 35,352 of them in descriptions; `search-meta.json` 5.6 MiB, 94% of its trigger, now display-only. Byte-identical run to run. See *Review of 2026-09-02* in `HISTORY.md`, sections C and E. |
| Topics | Done, 2026-09-02. **7,162 of 9,048 talks carry at least one of fifteen per-talk topics**, 1,886 none (613 of those have no description). Keyword rules in `atu.TOPICS` over title, tags and description, never the transcript; channel boilerplate stripped per conference first. `--topic` in the CLI, a Topic select and chips in the browser. See *The topic facet — built* in `HISTORY.md` and *What a talk is about* in `ARCHITECTURE.md`; the open item is a human read of twenty titles per topic (`TODO.md`). |
| CLI (`query.py`) | Done, and its ranking was rebalanced — see *Design decisions* in `ARCHITECTURE.md`. `--brief` and `--ids` were added for the skill — see *Making the skill affordable* in `HISTORY.md`. Rewritten 2026-09-02 around a gate on content words with progressive relaxation, plus `--transcript`, `--min-year`, repeatable `--conference`/`--category`/`--year` and a `~` on estimated timestamps — see *Review of 2026-09-02* in `HISTORY.md`, section C. Later the same day: relaxation drops a word **no talk says** before the commonest one (a typo used to take the real word with it), and `--stats` prints the corpus's counts from the index so the skill quotes nothing from memory. |
| Excerpting (`excerpt.py`) | Done, 2026-09-01. Windowed passages instead of whole transcripts; **100% of the passages `query.py` ranks survive, on 17% of the words**. See *Making the skill affordable* in `HISTORY.md`. |
| Browser UI (`index.html`) | Done. Conference / category / year facets, passage-level ranking. Since 2026-09-02: queries and index share one Porter stemmer, descriptions are searched whole through the shards rather than on their first 300 characters, a query no talk fully matches relaxes one word at a time and says so in the status line, highlighting is token-exact on stems, and an interpolated moment is shown as `~12:34`. See *Review of 2026-09-02* in `HISTORY.md`, section E. |
| Browser UI tests (`tools/uitest/`) | **193 checks over 9 suites, 0 failing, none skipped** (2026-09-02, after the topic facet: the topic select, membership filtering, stacking, chips, the hash round-trip). Before that, 183. New since the 172: stems, relaxation, the description tail beyond the clip, the `~` mark, and the `load` suite's title-link check now accepts an InfoQ page when newest-first puts one on top — it had been asserting YouTube since before InfoQ existed. Ranking agreement margins 9, 10, 8, 8, 9, 8, 10, 9 of 10 against a threshold of 4 (were 10, 9, 6, 6, 10, 6, 10, 9). |
| Excerpt tests (`tools/test_excerpt.py`) | Done. **14 offline checks** over window selection and merging — no corpus, no network, 0.1s. |
| Other offline tests | `test_query.py` (34, the parser, id resolution and `--topic` resolution), `test_topics.py` (the topic rules, one check per phrase pattern, and the boilerplate filter), `test_infoq.py` (the fold-in), `test_speakers.py` (19, every speaker shape and the false positives), `test_stem.py` (both stemmers over all 103,551 corpus tokens; skips its node half if node is missing). All green. |
| Fetcher tests (`tools/test_fetch_transcripts.py`) | Done. **128 offline checks** over the pool, the routes, the year selection, the four failure classes, the off-IP lease rule and the caption-language selection. |
| Claude Code skill | Done — `ai-conference-talks`, in `.claude/skills/`. Rewritten 2026-09-01 around a retrieval ladder that costs ~17k tokens a question instead of ~150k — see *Making the skill affordable* in `HISTORY.md`. Revised 2026-09-02 (section F): no hard-coded counts (`query.py --stats` instead), search the topic's words not the question, `url` rather than a YouTube template, `~` timestamps cited as approximate, `year` is the edition's, `-n` is a budget. |
| Transcripts | **3,174 of 9,048** over 35 conferences — 2,946 with exact timings (four of them held back from the index as ASR failures) and 228 estimated, from infoq.com. Before InfoQ: 2,946 of 8,822, all exact. ai-engineer 540, wearedevelopers 433, pydata 205, microsoft-build 187, berkeley-agentic-ai-summit 159, kubecon 151, ndc 149, ai-devcon-tessl 132, qcon-infoq 106, ai-council 94, mcp-dev-summit 84, devoxx 79. **The 2026 scope is complete**: of its 2,942 talks, 2,914 have a transcript and 28 have no captions, so nothing is pending. `I1GvlW1H4WI` entered the scope when the year-from-title fallback was fixed and was fetched for one credit — see *The pre-2023 cut* in `HISTORY.md`. The 422-talk backlog the seven new conferences created was fetched the same day — see *Closing the 422* in `HISTORY.md`. Twelve are `hi` and cannot be improved — see *Bug 7 cannot be fixed by refetching* in `HISTORY.md`. What is left is pre-2026 and deliberately unfetched — see *Collection is scoped to 2026* in `ARCHITECTURE.md`. |
| Imports (`import_kb.py`) | Done for WeAreDevelopers World Congress 2026: 358 talks and their transcripts, from `../presentations/kb`. Offline and rerunnable. |
| Workflows | Both run. `pages.yml` was rewritten on 2026-09-02: it now runs `tools/assemble_site.sh` and pushes only what the browser fetches to `gh-pages` as one orphan commit — 249 MB instead of the whole 411 MB repo. **Verified live 2026-09-02**: the merge of `infoq-presentations` was its first deploy — the assemble step reported 250 MB (transcripts 199 MB, tindex 46 MB, search-meta.json 5.7 MB), `gh-pages` is one orphan commit, and the `load` and `moments` suites pass 34 of 34 against the published site. `kb-refresh.yml` pushes a review branch instead of committing to `main`, after the run that did — see *The CI refresh regression* in `HISTORY.md`. |
| Published site | **Live** at <https://ppruchnerovic.github.io/ai-talks-universe/>, served from `gh-pages` — since 2026-09-02 the assembled 250 MB site rather than a mirror of the repository. |

## Verifying a change

```bash
cd tools
python3 check_registry.py
python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py \
  && python3 test_speakers.py && python3 test_topics.py && python3 test_stem.py \
  && python3 test_fetch_transcripts.py
cd uitest && node run.js                 # nine suites, 193 checks, about four minutes
KB_URL=https://ppruchnerovic.github.io/ai-talks-universe/ node run.js load moments   # against production
```

The first `query.py` call after a corpus change rebuilds `talks.db` (48 s)
because `atu.db_stale()` sees `talks.json` or `data/transcripts/` newer than
the database — that is the mechanism working, not a fault. Read the browser
suite's **skip count** as well as its failures: a check whose fixture the
corpus does not have yet skips rather than fails, so a green run on a thin
corpus is weaker evidence than one on a full one. The last full run skipped
nothing.

Things a session has actually got wrong, kept here because each looked like
something else at the time:

* **Verify with**: `cd tools && python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py && python3 test_speakers.py && python3 test_topics.py && python3 test_stem.py && python3 test_fetch_transcripts.py`, then `cd uitest && node run.js` (all nine suites, about four minutes). The first `query.py` call rebuilds `talks.db` (48 s) if `data/transcripts/` or `talks.json` is newer than the DB on disk — `atu.db_stale()` working, not a fault.
* **The speaker rules are exact on their line arithmetic.** `DESC_SPEAKER_RE` must use `[ \t]*` after the colon, not `\s*` — `\s*` eats the newline and hands "* Joshua Corbett" to the name test, which rejects the bullet — and the line after the heading is counted from `m.end()`, not `m.start()`, because the pattern's leading `^\s*` matches the blank lines above the heading. Both mistakes were made and each looked like "the heading is never found".
* **`build_index.py` must iterate the shard terms sorted.** A set's order differs run to run, and the build's byte-identity — which the README promises and the review verified — quietly went with it until two consecutive builds were diffed.
* **The stemmer is memoised** (`functools.lru_cache`): un-memoised it took the build from 48 s to 1 m 54 s on ~30 million transcript tokens.
* **Relaxation order matters in both rankers**: "drop the commonest word" on `kubernetes zzzz` dropped *kubernetes*, since the typo is present in zero talks and so is never the commonest. A word present nowhere goes first.

* **Count transcripts by exact video id, never by filename prefix.** 48 ids
  begin with an underscore and `_misses.json` lives beside them, so a prefix
  filter under-reports by 48. This has caught two separate sessions.
* **`_misses.json`'s `reason` is the exception class, not the reason.** It is
  `"LookupError"` on every entry; the fact is in `detail`. The check in the
  handoff below reads `detail`.
* **`SUPADATA_API_KEY` and `YOUTUBE_API_KEY` live in `~/.bash_profile`**,
  which a non-login shell does not read. A tool-driven shell sees neither and
  the run silently degrades to the free routes. `source` it explicitly.

## Handoff — running a transcript extraction

**Nothing is pending.** The 422 talks the seven new conferences brought in were
fetched on 2026-09-01 (*Closing the 422* in `HISTORY.md`), and the one the year-fallback fix
later moved into the scope went the same way (*The pre-2023 cut* in `HISTORY.md`). The
commands below are the same shape as any future selection:

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
  see *The 2026 extraction* in `HISTORY.md`. `--source exact` is right only when the free
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

After the fetch and the rebuild, before committing — each of these is a bug
this repo has actually had:

```bash
python3 - <<'PY'                         # every miss must be about the video:
import json                              # no captions, or a members-only 403.
d = json.load(open('../data/transcripts/_misses.json'))
for v in d.values(): print(v.get('detail'))   # NOT 'reason' — see above
PY

cd uitest && node run.js && cd ..        # 193 checks; read the skip count too
```

`build_index.py` prints where `search-meta.json` stands against its 6 MiB
trigger; transcripts do not go into that file, so a transcript run should not
move it. Then commit `data/`, `talks/` and the refreshed numbers in `README.md`
and this file — see *Numbers to refresh when the corpus changes*.

Two things not to redo while in there: the twelve `hi` talks were refetched on
2026-09-01 and came back `hi` again, so do not delete and refetch them a third
time (*Bug 7 cannot be fixed by refetching* in `HISTORY.md`), and spending the
credit remainder on pre-2026 talks is a change of policy rather than a backlog
(*Collection is scoped to 2026* in `ARCHITECTURE.md`).

### Adding a conference

```bash
cd tools
# edit conferences.json and ai-conferences.md together
python3 check_registry.py
python3 enrich.py --all -c <slug> --include-unknown-year   # first, for scope "ai": the filter reads descriptions
python3 sync_catalog.py --refresh -c <slug>
python3 build_index.py
python3 fetch_transcripts.py --probe && python3 fetch_transcripts.py --source supadata -c <slug> --min-year 2026 --workers 32 \
  && python3 sync_catalog.py && python3 build_index.py
```

The fetch reports how many it **selected** before spending anything. If that
number is not the count of new 2026 talks without transcripts, the selection is
not what you think it is — stop and look before it costs credits. Prefer
per-edition playlists to a whole channel for vendors who publish far more than
their conference; if the recordings are unlisted, register a seed. Both are in
the README under *Adding a conference*, and the reasoning behind the last seven
additions is *The seven conferences added on 2026-09-01* in `HISTORY.md`.

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
*Closing the 422* in `HISTORY.md`.

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
  before it was true — see *The 402 that was recorded as "no captions"* in `HISTORY.md`.

Hence `--retry-after MINUTES`, which parks the run and resumes; each round
re-derives its work from disk, so a blocked round costs only time. A block is
**not** written to `_misses.json` — that file means "this video has no
captions". Keeping the two apart is what lets a plain rerun collect everything a
block skipped.

Do not reach for the YouTube Data API for captions: `captions.download` requires
OAuth *and* permission to edit the video, so third-party talks return 403.
(The Data API *is* the right tool for descriptions — that is `enrich.py`.)

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
