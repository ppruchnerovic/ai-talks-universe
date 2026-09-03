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
| Registry (`conferences.json`) | Done. **53 conferences, 85 sources** — 83 YouTube listings, one `"type": "videos"` seed and one `"type": "infoq"` source — mirrored from `ai-conferences.md`, whose 54 blocks cover them (*QCon AI* and *InfoQ Dev Summit / QCon* both feed `qcon-infoq`); `check_registry.py` passes, and its "83 sources" counts the YouTube listings only. Seven conferences added 2026-09-01, see *The seven conferences added on 2026-09-01* in `HISTORY.md`. |
| Enumeration (`sync_catalog.py`) | Done. **17,677 videos** cached in `data/catalog/`, **8,826 surviving talks** — 9,325 before the 2023 year floor, see *The pre-2023 cut* in `HISTORY.md` — plus **222 InfoQ-only presentations**, **9,048 in the corpus**. 8,468 of them enumerated from YouTube, 358 seeded — see *The WeAreDevelopers import* in `HISTORY.md`. |
| Speakers | **4,982 of 9,048 (55%)** since 2026-09-02, up from 3,447 (38%): the bold-Unicode `Speakers:` heading Microsoft's channels use, the `A & B, Company` and `by A and B` title shapes. See *Review of 2026-09-02* in `HISTORY.md`, section D, and `test_speakers.py`. |
| Enrichment (`enrich.py`) | Done for the 2026 scope. **9,598 videos via the Data API**, in one run. See *What the collection runs actually got* in `HISTORY.md`. |
| Per-talk markdown | Done. 9,048 files, regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. Since 2026-09-02 the passages overlap at a half-passage stride and `talks.db` carries `PRAGMA user_version` (`atu.DB_SCHEMA_VERSION`, now 6) — 379 MiB, 48 s to build, and `atu.connect()` rebuilds it by itself when it is stale. The browser index is **keyed on Porter stems** (`atu.stem()`, memoised; the same function in JavaScript inside `index.html`, `test_stem.py` diffs them over the corpus vocabulary) and carries the **whole description's postings** per stem (`d`) plus the metadata document frequency (`m`): 44 MB in 711 shards, 52,327 stems, 35,352 of them in descriptions; `search-meta.json` 5.6 MiB, 94% of its trigger, now display-only. `tindex/_manifest.json` carries the **synonym groups** (`atu.SYNONYMS`) both rankers expand, and a record has `lg` when its transcript is not English. Byte-identical run to run. See *Review of 2026-09-02* and *Search enrichment* in `HISTORY.md`. |
| Topics | Done, 2026-09-02. **7,162 of 9,048 talks carry at least one of fifteen per-talk topics**, 1,886 none (613 of those have no description). Keyword rules in `atu.TOPICS` over title, tags and description, never the transcript; channel boilerplate stripped per conference first. `--topic` in the CLI, a Topic select and chips in the browser. See *The topic facet — built* in `HISTORY.md` and *What a talk is about* in `ARCHITECTURE.md`; the open item is a human read of twenty titles per topic (`TODO.md`). |
| CLI (`query.py`) | Done, and its ranking was rebalanced — see *Design decisions* in `ARCHITECTURE.md`. Rewritten 2026-09-02 around a gate on content words with progressive relaxation (*Review of 2026-09-02*, section C). Enriched the same day — see *Search enrichment* in `HISTORY.md`: column filters fixed (`title:` `speakers:` `{title tags}:` `transcript:`), colour only on a TTY, `--speaker`, `--sort`, duration and date filters, `--max-year`, `--exact-timing`, `--explain`, `--fields`, `--md`, `--random`, `-word`, `--facets`, `--per-conference`/`--per-year`, synonym groups, duplicate collapse `(also: …)`, `--excerpt`, and `--semantic`/`--no-semantic` (auto: on when the optional layer is installed, silent otherwise). `--topic`/`--list-topics` and the category-as-conference-type rename came in from *The topic facet* and *Category becomes conference type*, same day. |
| Excerpting (`excerpt.py`) | Done, 2026-09-01. Windowed passages instead of whole transcripts; **100% of the passages `query.py` ranks survive, on 17% of the words**. Since 2026-09-02: `--quotes` (~30 tokens a quote), `--outline` (~17 a two-minute bucket), `--at SECONDS`, `--words`/`--total-words`, `--full`, `--json`; notes in the output, not stderr. Costs measured in *Search enrichment* in `HISTORY.md`. |
| Semantic layer (`semantic.py`, optional) | Built 2026-09-02, **not committed** — `data/embeddings/` is derived and gitignored like `talks.db`, and installed only by `tools/install_semantic.sh [--chunks]` (196 s cold, 133 MB venv + 30 MB model, no torch). model2vec `potion-base-8M` over every talk and 176,573 transcript windows; `query.py` fuses it by union + reciprocal rank when present and is unchanged when absent. Talk-level only; the browser has no semantic layer. See *Search enrichment* in `HISTORY.md`. |
| Browser UI (`index.html`) | Done. Conference / conference type / topic / year facets with counts, speaker filter, length bucket, passage-level ranking. Since 2026-09-02: queries and index share one Porter stemmer, descriptions are searched whole through the shards, relaxation says which word it dropped, highlighting is token-exact on stems, `~12:34` for interpolated moments (*Review of 2026-09-02*, section E); then field syntax `title:` `speaker:` `conf:` `year:` `transcript:`, `-word`, phrase gate, OR and synonym groups, `prefix*`, duration sorts, "spoken only", the said-together / full-description / transcript-language badges, Markdown/CSV export, copy link, `j`/`k` (*Search enrichment*). 61 KB, no build step. |
| Browser UI tests (`tools/uitest/`) | **229 checks over 9 suites, 0 failing, none skipped** (2026-09-02, confirmed 2026-09-03; were 183, then 192 with the topic facet). The 37 from *Search enrichment* cover the field syntax, exclusions, synonyms, the speaker box (filter, typeahead, hash, `aria-label`, Tab order), duration sorts, facet labels, spoken-only, export and `j`/`k`. `suite-ranking` runs `query.py --no-semantic` so it compares lexical to lexical; margins 9, 10, 9, 8, 7, 8, 10, 9 of 10 against a threshold of 4. |
| Excerpt tests (`tools/test_excerpt.py`) | Done. **57 offline checks** over window selection and merging, the sentence splitter behind `--quotes`, the outline buckets, `--at` parsing — no corpus, no network, 0.1s. |
| Other offline tests | `test_query.py` (75: the parser, column filters, exclusions, synonyms, id resolution, `--topic`/`--category` resolution, the fusion helpers), `test_topics.py` (509, the topic rules, one check per boundary), `test_semantic.py` (60 without the layer, on the standard library: staleness, reciprocal-rank fusion, the pool mapping; its end-to-end block skips when the layer is absent), `test_infoq.py` (48, the fold-in), `test_speakers.py` (18, every speaker shape and the false positives), `test_stem.py` (5: both stemmers over all 104,061 corpus tokens; skips its node half if node is missing). All green. |
| Fetcher tests (`tools/test_fetch_transcripts.py`) | Done. **154 offline checks** over the pool, the routes, the year selection, the four failure classes, the off-IP lease rule and the caption-language selection. |
| Claude Code skill | Done — `ai-conference-talks`, in `.claude/skills/`. Rewritten 2026-09-01 around a retrieval ladder that costs ~17k tokens a question instead of ~150k — see *Making the skill affordable* in `HISTORY.md`. Revised 2026-09-02 (section F): no hard-coded counts, search the topic's words not the question, `~` timestamps cited as approximate, `-n` is a budget. Revised again for *Search enrichment*: `--facets` before choosing a slice, `--per-conference` instead of a five-call loop, `--excerpt`, the `--quotes`/`--outline` costs, synonyms-not-inflections in OR chains, `python3 tools/query.py` from the repo root, the semantic layer's caveats. |
| Transcripts | **3,174 of 9,048** over 35 conferences — 2,946 with exact timings (four of them held back from the index as ASR failures) and 228 estimated, from infoq.com. Before InfoQ: 2,946 of 8,822, all exact. ai-engineer 540, wearedevelopers 433, pydata 205, microsoft-build 187, berkeley-agentic-ai-summit 159, kubecon 151, ndc 149, ai-devcon-tessl 132, qcon-infoq 106, ai-council 94, mcp-dev-summit 84, devoxx 79. **The 2026 scope is complete**: of its 2,942 talks, 2,914 have a transcript and 28 have no captions, so nothing is pending. `I1GvlW1H4WI` entered the scope when the year-from-title fallback was fixed and was fetched for one credit — see *The pre-2023 cut* in `HISTORY.md`. The 422-talk backlog the seven new conferences created was fetched the same day — see *Closing the 422* in `HISTORY.md`. Twelve are `hi` and cannot be improved — see *Bug 7 cannot be fixed by refetching* in `HISTORY.md`. What is left is pre-2026 and deliberately unfetched — see *Collection is scoped to 2026* in `ARCHITECTURE.md`. |
| Imports (`import_kb.py`) | Done for WeAreDevelopers World Congress 2026: 358 talks and their transcripts, from `../presentations/kb`. Offline and rerunnable. |
| Workflows | Both run. `pages.yml` was rewritten on 2026-09-02: it now runs `tools/assemble_site.sh` and pushes only what the browser fetches to `gh-pages` as one orphan commit — 249 MB instead of the whole 411 MB repo. **Verified live 2026-09-02**: the merge of `infoq-presentations` was its first deploy — the assemble step reported 250 MB (transcripts 199 MB, tindex 46 MB, search-meta.json 5.7 MB), `gh-pages` is one orphan commit, and the `load` and `moments` suites pass 34 of 34 against the published site. `kb-refresh.yml` pushes a review branch instead of committing to `main`, after the run that did — see *The CI refresh regression* in `HISTORY.md`. |
| Published site | **Live** at <https://ppruchnerovic.github.io/ai-talks-universe/>, served from `gh-pages` — since 2026-09-02 the assembled 250 MB site rather than a mirror of the repository. |

## Verifying a change

```bash
cd tools
python3 check_registry.py
python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py \
  && python3 test_speakers.py && python3 test_topics.py && python3 test_semantic.py \
  && python3 test_stem.py && python3 test_fetch_transcripts.py
cd uitest && node run.js                 # nine suites, 229 checks, about four minutes
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

* **Verify with**: `cd tools && python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py && python3 test_speakers.py && python3 test_topics.py && python3 test_semantic.py && python3 test_stem.py && python3 test_fetch_transcripts.py`, then `cd uitest && node run.js` (all nine suites, about four minutes). The first `query.py` call rebuilds `talks.db` (48 s) if `data/transcripts/` or `talks.json` is newer than the DB on disk — `atu.db_stale()` working, not a fault.
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

cd uitest && node run.js && cd ..        # 229 checks; read the skip count too
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
python3 sync_catalog.py --refresh -c <slug>                # enumerate first: enrich.py reads the catalog this writes
python3 enrich.py --all -c <slug> --include-unknown-year   # for scope "ai": the filter reads descriptions, so titles that never say "AI" are dropped until this runs
python3 sync_catalog.py                                    # derive again, now with the descriptions
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
