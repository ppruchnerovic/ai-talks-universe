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
tools/query.py                     ranked search — which talks answer this
tools/excerpt.py                   the passages of a talk that answer it
```

## Know what the corpus is before you trust it

Two properties change how you should answer, and both are visible in the data:

* **Transcript coverage is partial** — 2,942 of the 8,822 talks. A talk without
  one is a *title and a description*: enough to recommend it, not enough to
  state what the speaker argued. `has_transcript` says which is which, and
  `query.py` marks transcript-bearing hits with `· transcript`.
* **Descriptions are YouTube descriptions**, not conference abstracts. They are
  written by the channel, often promotional, and sometimes empty.

## How to answer

**Always retrieve before answering. Never answer from memory** — you do not
know what was said at these events, and inventing a speaker's position is the
one failure mode that makes this KB worthless.

Retrieval is three widening steps, and most questions are answered by the first
two. **Never `cat` a talk markdown file to find out what a speaker said.**
Those files inline the whole transcript — 8,500 tokens on average, 26,000 for a
long workshop — and reading a handful of them is what turns a one-sentence
question into a six-figure token bill. `excerpt.py` gives you the parts of the
same transcript that bear on the question, with the same deep links, for a
tenth of that.

### 1. Find the talks — one search, not five

```bash
cd tools
python3 query.py "context engineering" -n 15 --brief
python3 query.py --list-conferences        # valid slugs; --list-categories too
```

`--brief` prints one block per hit — title, speakers, conference, year,
duration, whether it has a transcript, which layer matched, the description
snippet, the URL. That is what you need in order to *choose*, at about a fifth
of the bytes of `--json`. Reach for `--json --brief` when you are going to
compute something from the results, and for full `--json` — tags, channel,
publication date, four transcript moments per hit — only when the question is
about those fields.

People say the same thing many ways, so cover the vocabulary **inside one
query** rather than by running five:

```bash
python3 query.py 'evals OR guardrails OR "human in the loop" OR "failure modes"' -n 20 --brief
```

FTS5 ranks the union, so a talk that hits several of those terms rises to the
top by itself — and you pay for one result set instead of five overlapping
ones. Run a second, narrower query only when the first comes back thin, or
misses a vocabulary you can see is missing.

Useful flags: `--conference langchain-interrupt`, `--category "AI security"`,
`--year 2026`, `-n 25`, `--ids`. To compare conferences or years, re-run with
different `--conference` / `--year` rather than eyeballing one ranked list.

### 2. Read what those talks actually say

`query.py` ranks and snippets; it does not give you the argument. `excerpt.py`
does, for as many talks at once as you like:

```bash
python3 excerpt.py O72p-rBb2bA 5ID22ACI7IM -q "eval driven development"
python3 query.py "agent memory" -n 6 --ids | xargs python3 excerpt.py -q "agent memory"
```

It prints each talk's metadata, its description, its **opening** — where a
speaker states what they are about to argue — and a window of continuous
speech around each passage that matched, deep-linked to the second. It closes
with how much of the transcript you have seen, so a thin excerpt is visible as
one.

Give `-q` the same topic you searched for; the passages are ranked by the same
bm25 that ranked the talk. Then:

* `-n 3` when you are triaging many talks; `-n 10 --window 90` when one talk is
  the answer and you need the argument in full.
* `--full` for the whole transcript. Justified when the user asks about one
  named talk end to end; never as the default, and never for several talks at
  once.
* `--json` when you need the passages as data.

Reading the markdown file directly is for when you want the record itself — its
frontmatter, its tags — not for finding a quote.

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

### What a question should cost

A one-sentence question is one search and a handful of excerpts — on the order
of 15k tokens, not 150k. Past that you are almost certainly reading transcript
you did not need. Widen deliberately instead: another `-q` against the talks
you already have is cheaper, and likelier to be relevant, than another talk
read end to end.

### Fetching what is missing

If the question turns on a talk whose transcript has not been fetched, you can
get it — but it is metered, so ask before spending it:

```bash
cd tools
python3 fetch_transcripts.py --probe                 # is this network usable?
python3 fetch_transcripts.py -c ai-engineer --limit 10 --source exact
python3 sync_catalog.py && python3 build_index.py    # fold it in
```
