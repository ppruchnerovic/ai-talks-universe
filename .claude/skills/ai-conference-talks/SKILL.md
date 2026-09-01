---
name: ai-conference-talks
description: |
  Answer questions from the AI conference talk knowledge base — thousands of
  recorded talks from the world's AI conferences (AI Engineer, LangChain
  Interrupt, Code with Claude, OpenAI DevDay, NeurIPS-adjacent practitioner
  events, KubeCon AI tracks, Microsoft Build, AWS re:Invent, CAMLIS, DEF CON AI
  Village and more) with titles, YouTube descriptions, speakers, conference and
  year, recording links and — where fetched — full timestamped transcripts. Use
  this whenever the user asks what was said at an AI conference, who talked
  about a topic, what different speakers or vendors think about something,
  which talks to watch on a subject, how a topic was covered across
  conferences or across years, or asks to compare or synthesize positions
  across presenters. Also use it to pull a specific talk's recording link,
  description or conference. Do NOT use it for talks outside this corpus.
---

# AI conference talk knowledge base

The corpus lives in this repo; every path below is relative to the repo root.
If you are working from a different checkout, clone
`https://github.com/ppruchnerovic/ai-talks-universe` and run the commands there.

```
data/talks.json                    canonical records, one per talk
data/transcripts/<video_id>.json   timestamped transcript segments, when fetched
data/talks.db                      SQLite FTS5 index — the thing you actually query
talks/<conference>/<video_id>-<slug>.md   one readable file per talk
tools/query.py                     ranked search over both layers
```

## Know what the corpus is before you trust it

Two properties change how you should answer, and both are visible in the data:

* **Transcript coverage is partial and grows slowly.** YouTube meters caption
  downloads per IP, so only a fraction of the corpus has a transcript. A talk
  without one is a *title and a description* — enough to recommend it, not
  enough to state what the speaker argued. `has_transcript` says which is which,
  and `query.py` marks transcript-bearing hits with `· transcript`.
* **Descriptions are YouTube descriptions**, not conference abstracts. They are
  written by the channel, often promotional, and sometimes empty.

## How to answer

**Always retrieve before answering. Never answer from memory** — you do not
know what was said at these events, and inventing a speaker's position is the
one failure mode that makes this KB worthless.

### 1. Retrieve

```bash
cd tools
python3 query.py "context engineering" -n 12 --json
python3 query.py --list-conferences        # valid slugs; --list-categories too
```

`--json` gives you, per hit: title, speakers, conference, edition, year,
duration, `youtube_url`, `snippet` (from whichever layer matched) with
`snippet_from` and `matched` naming that layer, the legacy
`description_snippet`, and `moments` — timestamped
transcript hits with the exact seconds.

Useful flags: `--conference langchain-interrupt`, `--category "AI security"`,
`--year 2026`, `-n 25`, `--no-moments`. FTS5 syntax works: `"exact phrase"`,
`OR`, `NOT`, `prefix*`.

For a broad question, **run several queries with different vocabulary** rather
than one. People say the same thing many ways — for agent reliability try
`evals`, `guardrails`, `observability agents`, `failure modes`, `human in the
loop`, `agent testing`. Union the results.

To compare conferences or years, run the same query with different
`--conference` / `--year` values rather than eyeballing one ranked list.

### 2. Read the strong hits

`query.py` ranks and snippets; it does not give you the argument. For the talks
that matter, read the full record:

```bash
cat talks/ai-engineer/*-context-engineering-*.md
```

When a talk has a transcript, the markdown contains it, chunked into ~45s
paragraphs each carrying a deep link into the video. That is where a speaker's
actual position lives.

### 3. Synthesize

For "what do people think about X" questions, structure the answer around
**positions, not talks**:

- Group speakers who broadly agree; name the axis they disagree on.
- Attribute every claim to a named speaker and the conference they said it at.
  Speaker names are extracted from titles and descriptions and are sometimes
  missing — say "a speaker at <conference>" rather than guessing a name.
- Quote only from transcripts, never from descriptions (a YouTube description
  is a promise written by a marketing team, not a statement).
- Link each point to the recording, deep-linked when you have a timestamp:
  `https://www.youtube.com/watch?v=<video_id>&t=<seconds>s`.
- Say plainly when the corpus is thin: if only two talks touch the topic, or if
  none of the matching talks has a transcript, that is part of the answer.

### Fetching what is missing

If the question turns on a talk whose transcript has not been fetched, you can
get it — but it is metered, so ask before spending it:

```bash
cd tools
python3 fetch_transcripts.py --probe                 # is this network usable?
python3 fetch_transcripts.py -c ai-engineer --limit 10 --source exact
python3 sync_catalog.py && python3 build_index.py    # fold it in
```
