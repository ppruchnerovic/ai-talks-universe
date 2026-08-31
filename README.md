# AI talks universe

A searchable knowledge base of recorded talks from the world's AI conferences —
titles, descriptions, speakers, conference and year, recording links and, where
they have been fetched, full timestamped transcripts.

**6,979 talks from 46 conferences.** The curated list of which conferences and
why is [`ai-conferences.md`](ai-conferences.md); its machine-readable mirror,
which the pipeline actually reads, is [`conferences.json`](conferences.json).

Browse it at <https://ppruchnerovic.github.io/ai-talks-universe/> — no install,
works on a phone, and the URL carries the search so you can send someone a link
straight to a query.

## Where the data comes from

There is no agenda API here. Forty-six conferences publish their programmes in
the only machine-readable place they have in common: YouTube. So the corpus is
built in two stages that cost very different things.

| Stage | Cost | What it gives |
|---|---|---|
| **Enumerate** (`sync_catalog.py --refresh`) | cheap, one page request per 100 videos | video id, title, duration, channel |
| **Enrich** (`enrich.py`) | 1 API unit per 50 videos, or ~1.4s per video without a key | description, publish date, YouTube tags |
| **Transcribe** (`fetch_transcripts.py`) | one Supadata credit per talk, or metered per IP on the free routes | every word spoken, with timings |

Each stage caches to disk and is resumable, and the corpus is re-derived from
those caches offline. That separation is the point: enumeration can be redone
weekly for nothing, while transcripts accumulate over months.

### What survives into the corpus

A conference registered with `"scope": "all"` contributes everything it
publishes. One registered `"scope": "ai"` — NDC, GOTO, KubeCon, re:Invent,
Black Hat and the other general conferences with AI tracks — contributes only
the sessions whose title, description or tags match the AI vocabulary in
`tools/atu.py`. Without that, an *AI* talks corpus would be four fifths
Kubernetes networking and iOS layout. Each conference also carries a minimum
duration, which drops the stings, trailers and sponsor spots channels mix in.

Of 14,797 videos enumerated, 6,979 survive. `sync_catalog.py` prints exactly
what each conference dropped and why.

## Layout

```
├── index.html                     zero-install search UI (GitHub Pages)
├── conferences.json               the registry — what to read, and how to filter it
├── ai-conferences.md              the human curation behind that registry
├── data/
│   ├── talks.json                 canonical corpus — the source of truth
│   ├── talks.csv                  same thing for spreadsheets
│   ├── catalog/<conf>.json        raw enumeration + collected details, per conference
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
    ├── build_index.py             everything -> talks.db + browser index
    ├── query.py                   ranked search from the terminal
    ├── check_registry.py          conferences.json vs ai-conferences.md
    ├── test_fetch_transcripts.py  offline checks for the quota bookkeeping
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
the timestamp, so results deep-link into the video. FTS5 syntax works:
`"exact phrase"`, `OR`, `NOT`, `prefix*`.

### With Claude Code

The `ai-conference-talks` skill (`.claude/skills/`, at the root of this repo,
so any Claude Code session started here loads it) drives `query.py` and then
reads the matching talk files — which is what you want for questions like
*"what do people at different conferences say about agent reliability"*:
retrieval finds the talks, the model compares the positions.

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
conferences changed.

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
corpus costs about 140 units and `--all` over the full 14,797-video catalogue
about 296 — 3% of a day's allowance, which is why a re-enrichment is never the
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
API run closed it to 2, and it stays true for whatever a fresh enumeration adds.

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
`--min-year 2026` keeps only those years — 2,159 of the 6,979 talks are 2026 —
and a talk whose year is not known yet is left out unless
`--include-unknown-year` says otherwise. Nothing is removed from the corpus by
this: it is a selection filter, and `query.py --year` still reads every year.

`--source exact` refuses to fall back to estimates; `--retry-after` parks the
run when YouTube blocks the IP and resumes where it stopped. A block is **not**
recorded as a miss, so a plain rerun picks those talks straight back up;
`data/transcripts/_misses.json` means "this video has no captions", and
`--retry-misses` forces another attempt.

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
| `SUPADATA_API_KEY` | yes | one credit a talk at any length, and 95 of 95 on a measured batch — so as many as you buy |
| `kome.ai` (the default fallback) | **no** — estimated | unmetered, but deep links land near a quote, not on it |

What does *not* help, and was measured rather than assumed: slowing the run
down. `--min-delay`/`--max-delay` and the exponential backoff on retry are
there to be a good citizen, not to raise the ceiling — the allowance is per IP,
not per request rate.

Re-running will not *upgrade* an estimated transcript to an exact one — it skips
talks it already has. To redo one, delete its file first. Afterwards rerun
`sync_catalog.py` (to inline transcripts into the markdown) and
`build_index.py`, and commit.

The `Refresh the catalogue` workflow keeps the metadata current automatically;
it deliberately does not attempt transcripts, because YouTube blocks GitHub's IP
ranges outright. `--source supadata` is the one route that would work from CI,
since it never touches the runner's IP — it is not wired into the workflow
because that would spend credits on a schedule.

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

### The browser UI

`index.html` is one self-contained file with no build step, which makes it easy
to change and easy to break quietly — a search that silently stops matching
looks exactly like a search with no results.

```bash
cd tools/uitest
npm install            # playwright + chromium, ignored by git
node run.js            # 156 checks, about three minutes
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
