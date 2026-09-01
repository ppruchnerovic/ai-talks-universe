# AI talks universe

A searchable knowledge base of recorded talks from the world's AI conferences —
titles, descriptions, speakers, conference and year, recording links and, where
they have been fetched, full timestamped transcripts.

**8,822 talks from 53 conferences.** The curated list of which conferences and
why is [`ai-conferences.md`](ai-conferences.md); its machine-readable mirror,
which the pipeline actually reads, is [`conferences.json`](conferences.json).

Browse it at <https://ppruchnerovic.github.io/ai-talks-universe/> — no install,
works on a phone, and the URL carries the search so you can send someone a link
straight to a query.

## Where the data comes from

There is no agenda API here. Fifty-three conferences publish their programmes in
the only machine-readable place they have in common: YouTube. So the corpus is
built in two stages that cost very different things.

| Stage | Cost | What it gives |
|---|---|---|
| **Enumerate** (`sync_catalog.py --refresh`) | cheap, one page request per 100 videos | video id, title, duration, channel |
| **Enrich** (`enrich.py`) | 1 API unit per 50 videos, or ~1.4s per video without a key | description, publish date, YouTube tags |
| **Transcribe** (`fetch_transcripts.py`) | one Supadata credit per talk, or metered per IP on the free routes | every word spoken, with timings |
| **Import** (`import_kb.py`) | free, offline | a conference YouTube will not list, from an agenda that already knows it |

Each stage caches to disk and is resumable, and the corpus is re-derived from
those caches offline. That separation is the point: enumeration can be redone
weekly for nothing, while transcripts accumulate over months.

Enumeration has one blind spot, and it is not a small one: a recording that is
**unlisted** is on YouTube but on no channel page and no playlist, so no amount
of paging finds it. The WeAreDevelopers World Congress publishes 358 talks that
way — enumeration of its channel found exactly one of them. What knows those
video ids is the congress's own agenda, so for such a conference the registry
carries a source of `"type": "videos"` that reads a file in `data/seeds/`
instead of a URL. `import_kb.py` writes one from a corpus built against an
agenda API, together with the transcripts that corpus already had, and
everything downstream then treats those talks like any other.

### What survives into the corpus

A conference registered with `"scope": "all"` contributes everything it
publishes. One registered `"scope": "ai"` — NDC, GOTO, KubeCon, re:Invent,
Black Hat and the other general conferences with AI tracks — contributes only
the sessions whose title, description or tags match the AI vocabulary in
`tools/atu.py`. A single source can override its conference: the
WeAreDevelopers World Congress seed carries `"scope": "all"`, because a
curated agenda is a programme rather than a channel's uploads, and its
security, testing and platform sessions are worth having whether or not they
say "AI". Without that, an *AI* talks corpus would be four fifths
Kubernetes networking and iOS layout. Each conference also carries a minimum
duration, which drops the stings, trailers and sponsor spots channels mix in.

There is a year floor as well, registry-wide: **the corpus starts at 2023**.
Before that this is a different subject — the modern-LLM vocabulary appears in
3-9% of the 2015-22 talks against 30% of 2023's, and nothing older than 2023 was
ever worth a transcript credit, so none has one. What that leaves out is applied
ML and data engineering: AMLD 2022, Data Council before it renamed itself, MLOps
World 2021, Web Summit pitch heats. **CAMLIS, DEF CON AI Village and BSides Las
Vegas override it** with `"min_year": null` and keep their whole back catalogue,
because adversarial ML was the same subject before the vocabulary changed and 36
of DEF CON AI Village's 37 talks are 2019-21. A talk whose year is not yet known
passes the floor — enrichment is what resolves a year — and enumeration caches
every year regardless, so the floor is a re-derivation away from being moved:
`sync_catalog.py --no-min-year` rebuilds with the whole catalogue.

Of 17,677 videos enumerated, 8,822 survive. `sync_catalog.py` prints exactly
what each conference dropped and why, the year floor included.

## Layout

```
├── index.html                     zero-install search UI (GitHub Pages)
├── conferences.json               the registry — what to read, and how to filter it
├── ai-conferences.md              the human curation behind that registry
├── data/
│   ├── talks.json                 canonical corpus — the source of truth
│   ├── talks.csv                  same thing for spreadsheets
│   ├── catalog/<conf>.json        raw enumeration + collected details, per conference
│   ├── seeds/<name>.json          talks enumeration cannot see, listed outright
│   ├── transcripts/<video_id>.json  exact caption timings, one file per talk
│   ├── talks.db                   SQLite + FTS5, used by query.py (gitignored)
│   ├── search-meta.json           compact metadata the browser loads up front
│   └── tindex/                    transcript inverted index, sharded, lazy-loaded
├── talks/<conf>/<video_id>-<slug>.md   one readable file per talk
└── tools/
    ├── atu.py                     shared helpers, and the AI-relevance test
    ├── sync_catalog.py            registry -> talks.json + csv + markdown
    ├── enrich.py                  descriptions, dates and tags
    ├── fetch_transcripts.py       YouTube captions -> transcripts/   (run locally)
    ├── import_kb.py               another corpus -> seeds/ + transcripts/ (offline)
    ├── build_index.py             everything -> talks.db + browser index
    ├── query.py                   ranked search from the terminal
    ├── excerpt.py                 the passages of a talk that answer a question
    ├── check_registry.py          conferences.json vs ai-conferences.md
    ├── refresh_report.py          field coverage before vs after a refresh
    ├── test_fetch_transcripts.py  offline checks for the quota bookkeeping
    ├── test_excerpt.py            offline checks for the excerpt budget
    └── uitest/                    browser tests for index.html
```

### Why four representations

They serve different readers and cost almost nothing to keep in sync, since all
of them are generated from the same run.

| Artifact | For | Why not the others |
|---|---|---|
| `data/talks.json` / `.csv` | scripts, spreadsheets, any future tool | exact, complete, no parsing of prose |
| `talks/**.md` | humans, `grep`, Claude Code | git-diffable per talk; an agent can read one file and have the whole talk |
| `data/talks.db` | ranked CLI search | generated; delete it any time and rebuild |
| `search-meta.json` + `tindex/` | the browser | must exist as files, since GitHub Pages has no backend |

## Searching

### In a browser

<https://ppruchnerovic.github.io/ai-talks-universe/> — type a topic, filter by
conference, category or year, sort by relevance / newest / title, and click
**Find this in the talk** to jump to the exact seconds where a phrase is
spoken. That link only appears for talks that have a transcript, and only once
you have searched for something, since what it finds are the moments matching
your query.

Multi-word searches rank talks that say the words *together*, in one passage,
above talks that merely say each of them somewhere.

### From the terminal

```bash
cd tools
python3 query.py "context engineering"
python3 query.py "prompt injection" --category "AI security" -n 20
python3 query.py "agents in production" --conference langchain-interrupt
python3 query.py "evals" --year 2026 --json          # for scripts and agents
```

Both the descriptions and the transcripts are searched. Transcript hits carry
the timestamp, so results deep-link into the video, and each result says which
layer matched. FTS5 syntax works: `"exact phrase"`, `OR`, `NOT`, `prefix*`, and
is always taken literally. A bare multi-word query is ANDed first and relaxed to
an OR of its terms only if that matches nothing, so a natural-language question
still returns ranked results — it says on stderr when it relaxes.

`--conference` and `--category` are case- and separator-insensitive and suggest
near misses; `--list-conferences` and `--list-categories` print the valid
values. `--brief` drops the fields and the extra transcript moments that help
you *read* a result but not *choose* one, which is about a fifth of the bytes;
`--ids` prints nothing but the video ids, to pipe into the next command.

### Reading a talk without reading all of it

A talk's markdown file inlines its whole transcript: 33 KB on average, 420 KB
for the longest workshop. That is the right thing for a human who has decided
to read one talk, and the wrong thing for anything — an agent, a script, you —
that wants what a speaker said about *one topic* across a dozen of them.

```bash
cd tools
python3 excerpt.py O72p-rBb2bA -q "eval driven development"
python3 query.py "agent memory" -n 6 --ids | xargs python3 excerpt.py -q "agent memory"
python3 excerpt.py O72p-rBb2bA --full          # the whole transcript after all
```

`excerpt.py` prints the talk's metadata, its description, its opening — where
the thesis nearly always is — and a window of continuous speech around each
passage that matched, merged where those windows overlap and deep-linked to
the second. What it leaves out it says: every excerpt ends with how much of the
transcript you have seen.

`-n` is a budget rather than a count — n windows' worth of speech, which the
merge may hand back as fewer and wider passages — because counting passages
bounds nothing. On a talk that says the query word every other minute, six
windows that each grow to meet their neighbours are the transcript again.
Measured over eight topics and 45 talks: **100% of the passages `query.py`
ranked survive into the excerpt, on 17% of the words.**

### With Claude Code

The `ai-conference-talks` skill (`.claude/skills/`, at the root of this repo,
so any Claude Code session started here loads it) drives `query.py --brief` and
then `excerpt.py` — which is what you want for questions like *"what do people
at different conferences say about agent reliability"*: retrieval finds the
talks, the excerpts carry what was said, and the model compares the positions.

The two-step matters more here than anywhere else, because a model pays for
every byte it reads. Answering one question by searching and then reading the
matching talk files whole costs on the order of 60,000 tokens and rises with
every talk added to the comparison; the same question through `--brief` and
`excerpt.py` costs about 17,000 and holds every passage the search ranked. The
skill says so in as many words, and says what a question should cost, because
"read the talks" is the instruction a model will otherwise follow literally.

## Rebuilding

```bash
cd tools
python3 sync_catalog.py --refresh    # re-enumerate every source (~10 min)
python3 enrich.py                    # descriptions and dates
python3 fetch_transcripts.py         # ON YOUR OWN MACHINE — see below
python3 sync_catalog.py              # fold the new material in (offline)
python3 build_index.py               # rebuild both search indexes
```

`sync_catalog.py` without `--refresh` and `build_index.py` are idempotent —
rerunning gives byte-identical output, so a git diff shows exactly what the
conferences changed. That holds literally, including `talks.json`'s
`generated_at`, which advances only when the corpus actually changes rather than
on every run. `build_index.py --help` lists its flags without rebuilding.

A transcript is indexed as content only if it says something. A file below ten
words a minute, over a talk of five minutes or more, is an ASR failure rather
than a transcript — four here are YouTube mis-reading English audio as Hindi and
then giving up, at 2.5 to 3.7 words a minute against a corpus median of 164 —
and those are left out of both indexes, out of the transcript counts and out of
the "Find this in the talk" link. The file itself is kept, since deleting it
would only make the fetcher re-select the talk and buy the same bytes again, and
the run prints every id it held back with the rate that did it. Separately, a
transcript in a script the tokeniser cannot read is measured by its word count
rather than by its token count, so that the handful of Latin brand names inside
a Devanagari or Japanese transcript do not rank as though they were the whole
talk.

### Fetching what has no transcript yet

Nothing is pending. The seven conferences added on 2026-09-01 brought in 422
talks without transcripts, and all 422 were fetched the same day — 420 returned
captions, 2 had none; the one talk the year-fallback fix later moved into 2026
was fetched the same way, for one credit. When a refresh brings new talks in,
this is the run, and it takes about five minutes:

```bash
cd tools
source ~/.bash_profile               # SUPADATA_API_KEY + YOUTUBE_API_KEY live here;
                                     # a non-login shell does not read that file
.venv/bin/python fetch_transcripts.py --probe          # 1 credit; says which route to name
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --workers 32 \
  && .venv/bin/python sync_catalog.py \
  && .venv/bin/python build_index.py
```

Chain the three, rather than running the fetch alone: a transcript that is not
folded in and indexed is invisible to the browser, the CLI and the markdown, so
it is a credit spent for nothing. The selection re-derives itself from disk on
every run — it takes what has no transcript — so an interrupted run is resumed
by repeating the same command, and there is no list to keep.

Then confirm the fetch classified its failures correctly and the UI still
passes, which is what `STATE.md` walks through, and commit `data/`, `talks/` and
the counts in this file.

### Adding a conference

Add it to `conferences.json` and to `ai-conferences.md`, then:

```bash
cd tools
python3 check_registry.py                      # they must agree
python3 sync_catalog.py --refresh -c <slug>
python3 build_index.py
```

Prefer per-edition playlists to a whole channel for vendors who publish far
more than their conference, and a channel for a dedicated conference channel.
`"first": N` caps how deep a channel listing is paged; channels list newest
first, so it is a recency cap.

If the recordings are unlisted, no source URL will reach them. Register a seed
instead — `{"type": "videos", "seed": "<file>.json", "url": ..., "label": ...,
"year": ...}` — and put the ids in `data/seeds/<file>.json`. Reading a seed is
reading a file, so `sync_catalog.py` folds it in on every run, `--refresh` or
not, and a seed's own abstracts, speakers and tags win over what enrichment
would collect: they come from the programme, not from a channel description.
`import_kb.py` writes the seed for a conference whose agenda was already
harvested elsewhere. A source may also carry its own `scope`, `min_duration`,
`match` or `exclude`, overriding the conference's — which is how one
conference contributes its whole congress programme through a seed while its
channel listing still contributes only the AI talks.

### Descriptions, dates and tags

`enrich.py` prefers the YouTube Data API and falls back to yt-dlp:

```bash
export YOUTUBE_API_KEY=...            # free; console.cloud.google.com
cd tools && python3 enrich.py --all
```

The key is free and there is no paid tier — 10,000 quota units a day per
project, resetting at midnight Pacific, with no billing account and no card. At
<https://console.cloud.google.com>: create a project, enable **YouTube Data API
v3** under *APIs & Services → Library*, then *Credentials → Create credentials →
API key*. Restrict it to that one API afterwards, since an unrestricted key that
leaks works against every API the project has enabled; leave the *application*
restriction unset, because this runs from a script rather than a browser. If the
export lives in `~/.bash_profile` it will not reach a non-login shell — put it
in `~/.bashrc`, or source it explicitly.

`videos.list` bills one unit per call and takes 50 video ids at a time, so the
corpus costs about 190 units and `--all` over the full 17,677-video catalogue
about 354 — 4% of a day's allowance, which is why a re-enrichment is never the
thing to ration. Without a key it is a full yt-dlp extraction per video —
roughly an hour for the corpus at two workers, and it draws on the same IP
reputation the transcript fetch depends on, so do not run it alongside a
transcript run.

The key does nothing for transcripts. `captions.download` requires OAuth *and*
edit permission on the video, so third-party talks return 403 however the
request is authenticated, and the per-IP caption throttle is a different
mechanism from Data API quota. Metadata is the one thing this buys.

`--all` matters for the conferences registered `"scope": "ai"`: their relevance
filter reads the description, so a talk whose *title* never says "AI" is
dropped before it is ever enriched. Enrich `--all` first, then re-sync.

`--year` / `--min-year` / `--include-unknown-year` select here exactly as they
do for transcripts, with one twist: enrichment is what *resolves* a year, so a
year-scoped run wants the third flag or it can only ever re-select talks whose
year is already known. That mattered when 3,082 talks had no year; the Data
API run closed it to 2, and removing the three hollow records closed it to 0. It
stays true for whatever a fresh enumeration adds.

```bash
cd tools && python3 enrich.py --min-year 2026 --include-unknown-year
```

### Transcripts, and YouTube's quota

`fetch_transcripts.py` tries four routes, cheapest first:

| Route | Timing | Works from | Cost |
|---|---|---|---|
| `youtube-transcript-api` | **exact** — deep links land on the second | only un-flagged IPs, in practice a home connection | free |
| `yt-dlp` | **exact** — a different Innertube client, so it sometimes gets through when the first is refused | same | free |
| `supadata.ai` | **exact** | anywhere — it egresses from their IPs, so the quota below does not apply | one credit per talk, any length |
| `kome.ai` | **estimated** — interpolated from word position | anywhere, including CI and cloud containers | free |

```bash
pip install -r tools/requirements.txt
cd tools
python3 fetch_transcripts.py --probe                     # is this network usable?
python3 fetch_transcripts.py --priority 1 --source exact --retry-after 20
```

**Expect to be rate limited.** YouTube meters the caption endpoint per egress IP
with an allowance that refills over hours, and both free exact routes draw on
the same one. In practice a consumer connection yields ~20-25 talks before it
closes; slowing down does not raise that number, which is why the two things
that *do* raise it each get a section below. On this corpus the free routes are
now the fallback rather than the plan — see *Beating the per-IP quota*.

This corpus is far larger than any single sitting can transcribe, so the
registry carries a `priority` per conference and the fetcher selects on it —
`--priority 1` is the practitioner conferences whose content is the reason this
exists. Within a priority it takes the longest talks first.

It selects on year too, because on AI topics a 2023 talk is rarely worth a unit
of an allowance that refills over hours. `--year 2026` (repeatable) or
`--min-year 2026` keeps only those years — 2,942 of the 8,822 talks are 2026,
of which 2,914 have a transcript and 28 have no captions, so none is waiting on
a fetch — and a talk whose year is not known yet is left out unless
`--include-unknown-year` says otherwise. This is a selection filter and removes
nothing: `query.py --year` reads every year the corpus has. What the corpus
*has* is a separate decision, made once in the registry — see the year floor
above.

`--source exact` refuses to fall back to estimates; `--retry-after` parks the
run when YouTube blocks the IP and resumes where it stopped. A block is **not**
recorded as a miss, so a plain rerun picks those talks straight back up;
`data/transcripts/_misses.json` means "this video has no captions", and
`--retry-misses` forces another attempt. Nor is an account refusal — a Supadata
key with no credits left stops the round and leaves every talk it had in flight
retryable, since running out of money says nothing about a video.

### Beating the per-IP quota

Since what is metered is an allowance per egress IP, there are exactly two ways
to get more than one sitting's worth, and they compose.

**Fetch from more IPs.** Each proxy is a separate identity with its own
allowance. A block benches that one identity for `--proxy-cooldown` minutes and
the run carries straight on down the others, so a pool of *N* usable IPs is
worth roughly *N* sittings in one go. A talk that was in flight when its
identity got benched is retried on another rather than left for the next round.

```bash
cd tools
cat ~/proxies.txt                  # one per line; host:port:user:pass as vendors export it
python3 fetch_transcripts.py --probe --proxy-file ~/proxies.txt   # which of them work
python3 fetch_transcripts.py --proxy-file ~/proxies.txt --priority 1 --source exact
```

`--probe` reports one line per identity, so a dead or unauthenticated proxy is
visible before it costs a round. Credentials are redacted from every line the
script prints. Workers default to one per identity (max 8), and an identity is
only ever used by one worker at a time — two parallel requests down the same IP
spend that IP's allowance twice as fast for no extra throughput. Residential
IPs work; datacenter ranges are blocked hardest, so a cheap datacenter pool
mostly buys benched identities.

**Or fetch from someone else's IP.** `supadata.ai` returns real caption
timings, from their infrastructure, so the quota never enters into it. This is
the primary route for this corpus:

```bash
export SUPADATA_API_KEY=...        # supadata.ai
cd tools
python3 fetch_transcripts.py --source supadata --priority 1   # ignores the IP quota entirely
python3 fetch_transcripts.py --priority 1 --source exact      # free routes first, then this
```

With a key, `--source exact` uses the free routes until an IP is blocked and
then keeps going on Supadata, so a run only spends credits on what the IP
quota could not cover. `mode=native` is used deliberately: it asks only for
captions YouTube already has, at one credit a talk, rather than paying two
credits a minute to transcribe audio. Talks over 20 minutes come back as a job
the fetcher polls — which here is most of them, since it takes the longest
talks first.

**Once `--probe` says the IP is spent, ask for `--source supadata` by name.**
`--source exact` will still get there, but it pays a refused
`youtube-transcript-api` call and a yt-dlp subprocess on every talk before it
does, and it holds the egress lease while it happens. Naming the route skips
both, and because that route egresses from somebody else's IPs there is no
allowance to ration and nothing to lease — so `--workers` becomes real
parallelism rather than a queue behind a single identity:

```bash
python3 fetch_transcripts.py --source supadata --min-year 2026 --workers 32
```

Measured on this corpus, same key, same network: **3 talks a minute at
`--source exact` with the default pacing, against ~250 a minute at
`--source supadata --workers 32`** — 1,249 talks in under six minutes rather
than the better part of a day. Nothing about the far end changed; what changed
is that 32 requests are in flight instead of one. There is no published rate
limit, so a 429 is backed off and retried rather than being fatal, and the run
finds the ceiling by itself: raise `--workers` until 429s start appearing in
the log. At 32 there were none.

Measured on the free trial: **95 talks requested, 95 returned**, all with exact
timings, no misses, and most of them long enough to go through the polling
path — 96 of the 100 free credits for 95 transcripts. Nothing was charged for a
video that turned out to have no captions, against a ~4.4% miss rate on the free
routes, so a credit budget needs no headroom: credits ≈ talks. The paid tier is
$17 a month for 3,000 credits, which is why buying the backlog outright beats
grinding it — 2,000 talks at ~35 a sitting is two months of once-daily runs for
about three hours of actual fetching, and the cost is calendar waiting on an
allowance that refills over hours, not work.

| Lever | Exact timings | Yield |
|---|---|---|
| one home connection | yes | ~20-25 a sitting, then hours |
| `--proxy-file` with N residential IPs | yes | ~N × 25 a sitting |
| `SUPADATA_API_KEY` | yes | one credit a talk at any length, and 95 of 95 on a measured batch — so as many as you buy, at ~250 a minute with `--workers 32` |
| `kome.ai` (the default fallback) | **no** — estimated | unmetered, but deep links land near a quote, not on it |

What does *not* help, and was measured rather than assumed: slowing the run
down. `--min-delay`/`--max-delay` and the exponential backoff on retry are
there to be a good citizen, not to raise the ceiling — the allowance is per IP,
not per request rate.

Supadata picks a caption track itself unless asked, and asking is not enough on
its own: given `lang=en` it falls back to whatever the video has rather than
failing, so the fetcher checks the answer and re-requests against the video's
own `availableLangs`. A talk that really has no English track is saved under the
language it is in, never written to `_misses.json` — that file means *no
captions*, and a Hindi track is captions.

Twelve talks here are like that, and no route can mend them: their single
auto-generated track is YouTube's ASR mis-reading English audio as Hindi, so
`availableLangs` is `['hi']` and there is nothing else to ask for. Deleting and
refetching returns the same bytes.

Re-running will not *upgrade* an estimated transcript to an exact one — it skips
talks it already has. To redo one, delete its file first. Afterwards rerun
`sync_catalog.py` (to inline transcripts into the markdown) and
`build_index.py`, and commit.

The `Refresh the catalogue` workflow re-enumerates weekly and **opens a pull
request** rather than committing to `main`. It deliberately does not attempt
transcripts, because YouTube blocks GitHub's IP ranges outright. `--source
supadata` is the one route that would work from CI, since it never touches the
runner's IP — it is not wired into the workflow because that would spend
credits on a schedule.

The review gate exists because enumeration from a runner degrades rather than
fails: a throttled listing returns titles and durations with no uploader, and
one scheduled run wrote `channel: null` over ~4,540 talks before anyone saw it.
The counting backstops — keep the cache when a source returns empty, refuse a
corpus 10% smaller — both passed it, because the record count was fine and the
records were hollow. So `refresh_report.py` diffs *field coverage* against the
committed corpus and puts the table in the PR body:

```bash
cd tools
python3 refresh_report.py                 # markdown; exit 2 if a field regressed
python3 refresh_report.py --tolerance 0.05
```

A field may lose up to 2% of the corpus before that counts as a regression,
which leaves room for the occasional video its uploader deleted. Past that the
PR opens as a draft, titled so the failure is visible in the list.

## Testing

### The fetcher's bookkeeping

```bash
cd tools && python3 test_fetch_transcripts.py     # ~1s, no network
```

Fake egress allowances and a faked HTTP layer, because what is worth testing in
`fetch_transcripts.py` is not the requests but the accounting around them:
every error in it is quiet and expensive. A block recorded as a miss loses a
talk permanently; an estimate returned under `--source exact` mislabels one; a
talk dropped because its proxy was benched costs a fetch nobody notices.

### The excerpt budget

```bash
cd tools && python3 test_excerpt.py               # ~0.1s, no network, no database
```

Same reason: the failure it prevents is silent and expensive. A query whose
terms are spread through a long talk once chained every window into one span
and returned the whole transcript under the name of an excerpt — 8,500 tokens
where 1,500 was asked for, with nothing in the output saying so. Window
selection and merging are pure functions of the hit times, so they are tested
without a corpus.

### The browser UI

`index.html` is one self-contained file with no build step, which makes it easy
to change and easy to break quietly — a search that silently stops matching
looks exactly like a search with no results.

```bash
cd tools/uitest
npm install            # playwright + chromium, ignored by git
node run.js            # 172 checks, about three minutes
node run.js search filters      # just those suites
```

`run.js` serves the repo on a free port, runs each suite in its own process,
and exits non-zero if anything failed. Every check prints what it actually saw.

| Suite | Covers |
|---|---|
| `load` | catalogue loads, filters built from the data, one card end to end |
| `search` | every field, phrases, prefixes, the transcript layer, tokenising |
| `controls` | pagination, description unfold, tag chips, `/` shortcut |
| `filters` | conference / category / year, the three sorts, Reset, the shareable hash |
| `moments` | "Find this in the talk" — ranking, deep links, caching |
| `resilience` | missing data at each layer, hostile queries, a 390px phone |
| `a11y` | accessible names, keyboard reach, announcements, contrast |
| `ranking` | agreement with `query.py`, plus properties that hold regardless |
| `navigation` | load cost, lazy shards, history, links out |

Three things worth knowing when adding a check:

* **Coverage grows in layers.** Descriptions arrive with `enrich.py`,
  transcripts a sitting at a time. A check whose fixture does not exist yet
  calls `L.skip(...)` rather than failing — but it must not pass silently, or
  the suite quietly stops testing anything.
* **The transcript cache is per page.** Anything asserting a cold fetch has to
  open its own page.
* **`ranking` skips its CLI half** when `data/talks.db` is missing, rather than
  making `query.py` build it mid-test.
