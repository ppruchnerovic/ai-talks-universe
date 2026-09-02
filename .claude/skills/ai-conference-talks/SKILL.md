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
data/talks.db                      SQLite FTS5 index — built on first use, rebuilt when stale
talks/<conference>/<video_id>-<slug>.md   one readable file per talk
tools/query.py                     ranked search — which talks answer this
tools/excerpt.py                   the passages of a talk that answer it
```

## Know what the corpus is before you trust it

Do not quote coverage numbers from memory — they change with every fetch.
Ask the index, which takes a second:

```bash
cd tools
python3 query.py --stats             # talks, transcripts, conferences, per year, per conference, per topic
```

Four properties change how you should answer, and all are visible in the data:

* **Transcript coverage is partial and uneven.** `--stats` shows it per year
  and per conference; as a rule the recent years are near-complete and the
  older ones are bare. A talk without a transcript is a *title and a
  description*: enough to recommend it, not enough to state what the speaker
  argued. `has_transcript` says which is which, `query.py` marks
  transcript-bearing hits with `· transcript`, and `--transcript` filters to
  them — use it whenever the question needs a quote.
* **Descriptions are mostly YouTube descriptions**, written by the channel,
  often promotional, sometimes empty. The exceptions are the InfoQ talks and
  the seeded WeAreDevelopers programme, whose descriptions are real abstracts.
* **`year` is the edition's year, not the upload date.** InfoQ posts a
  conference's recordings for a year afterwards; a talk filed under 2025 was
  given in 2025 however late it appeared. The browser's "newest" sort is by
  publication date, which is a different thing.
* **Not every talk is a YouTube video.** Each record has a `url` — the
  canonical link — and a `youtube_url` that is `null` for the talks that exist
  only as InfoQ pages (their ids start with `iq-`). Link to `url`.

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
python3 query.py --list-conferences        # valid slugs; --list-categories and --list-topics too
```

**Search for the topic's words, not for the question.** A bare query is
reduced to its content words — "what do people say about agent reliability"
is searched as `agent reliability` — but the reduction is a safety net, not a
strategy: `evals for agents in production` is a better query than the sentence
it came from, and you choose the vocabulary. Every word has to appear
somewhere in a talk, metadata or transcript, for it to rank; when no talk has
all of them, the search drops a word no talk says (a typo) first, then the
commonest, one at a time, and **says so on stderr** — read that line, because
it tells you what the results are actually about.

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
python3 query.py 'evals OR guardrails OR "human in the loop" OR fine-tuning' -n 20 --brief
```

FTS5 ranks the union, so a talk that hits several of those terms rises to the
top by itself — and you pay for one result set instead of five overlapping
ones. Hyphenated and punctuated terms (`fine-tuning`, `gpt-4`, `c++`) are
safe inside an OR chain. Run a second, narrower query only when the first
comes back thin, or misses a vocabulary you can see is missing.

Useful flags: `--conference langchain-interrupt` (repeatable), `--category
security` (the conference type: five kinds of venue, `--list-categories`),
`--topic evals` (repeatable; `--list-topics` prints the fifteen), `--year
2026` (repeatable), `--min-year 2025`, `--transcript`, `-n 25`, `--ids`. To
compare conferences or years, re-run with different `--conference` /
`--year` rather than eyeballing one ranked list.

`--category` is where a talk was given — *Practitioner AI conferences*,
*General software conferences*, *Security conferences*, *Vendor events*,
*Business & industry events* — and `--topic` is what it is about. They
cross: `--category security --topic agents` is what security-conference
speakers say about agents; `--category vendor --topic security` is what
vendor keynotes say about security. Only 577 of the 1,314 security-topic
talks are from security conferences, so neither flag substitutes for the
other.

`--topic` is a per-talk facet — fifteen subjects such as *Agents &
orchestration*, *Evals, observability & reliability*, *RAG, retrieval &
knowledge*, *Security, safety & red teaming* — derived by keyword rules from
each talk's title, tags and description, never from its transcript. A talk
may carry several, and about a fifth carry none (keynotes, panels, talks
with no description), so it narrows a search rather than replacing one:
`query.py "memory" --topic agents` is memory as an agent concern, `--topic
rag` memory as retrieval. One word of a topic's name resolves when it is
unambiguous (`evals`, `rag`, `security`); `--brief` prints each hit's topics,
which is a cheap way to see what a result set is actually about.

### 2. Read what those talks actually say

`query.py` ranks and snippets; it does not give you the argument. `excerpt.py`
does, for as many talks at once as you like:

```bash
python3 excerpt.py O72p-rBb2bA 5ID22ACI7IM -q "eval driven development"
python3 query.py "agent memory" -n 6 --transcript --ids | xargs python3 excerpt.py -q "agent memory"
```

It prints each talk's metadata, its description, its **opening** — where a
speaker states what they are about to argue — and a window of continuous
speech around each passage that matched, deep-linked to the second. It closes
with how much of the transcript you have seen, so a thin excerpt is visible as
one.

Give `-q` the same topic you searched for. Inside one talk a multi-word `-q`
falls back to the OR of its words when no 25-word passage holds all of them,
and the passages then rank by the rarest word — so if the excerpts are about
the wrong word, narrow `-q` rather than widen `-n`. Then:

* **`-n` is a budget of speech, not a count of quotes.** `-n 3` buys three
  windows' worth of transcript, which the merge may hand back as one wide
  passage or three narrow ones. Use `-n 3` when triaging many talks; `-n 10
  --window 90` when one talk is the answer and you need the argument in full.
* `--full` for the whole transcript. Justified when the user asks about one
  named talk end to end; never as the default, and never for several talks at
  once.
* `--json` when you need the passages as data.

Reading the markdown file directly is for when you want the record itself — its
frontmatter, its tags — not for finding a quote. `excerpt.py` accepts the
markdown path as well as the id.

### 3. Synthesize

For "what do people think about X" questions, structure the answer around
**positions, not talks**:

- Group speakers who broadly agree; name the axis they disagree on.
- Attribute every claim to a named speaker and the conference they said it at.
  Speaker names are extracted from titles and descriptions and are missing on
  about two fifths of the talks — say "a speaker at <conference>" rather than
  guessing a name.
- Quote only from transcripts, never from descriptions (a YouTube description
  is a promise written by a marketing team, not a statement).
- Link each point to the recording, using the talk's `url`. For a YouTube
  talk, deep-link with `&t=<seconds>s`; an InfoQ page takes no timestamp
  parameter, so give the time in words. A timestamp printed as `~12:34` is
  **interpolated from word position**, not measured — cite it as approximate
  ("around 12 minutes in"), never to the second.
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

`--limit` runs one round and returns, so it disables `--retry-after`; the
fetcher says so when both are given. An `iq-` talk is never fetched — its
transcript came with its page.
