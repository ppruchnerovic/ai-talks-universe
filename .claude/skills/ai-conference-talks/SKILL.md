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

The corpus lives in this repo; every path below is relative to the repo root,
and every command is written to be run **from the repo root** as
`python3 tools/query.py …` — a subagent's working directory is reset between
calls, so `cd tools` does not survive to the next command. If you are working
from a different checkout, clone
`https://github.com/ppruchnerovic/ai-talks-universe` and run the commands there.

```
data/talks.json                    canonical records, one per talk
data/transcripts/<video_id>.json   timestamped transcript segments, when fetched
data/talks.db                      SQLite FTS5 index — built on first use, rebuilt when stale
talks/<conference>/<video_id>-<slug>.md   one readable file per talk
tools/query.py                     ranked search — which talks answer this
tools/excerpt.py                   the passages of a talk that answer it
tools/install_semantic.sh          optional: a semantic layer query.py uses when present
```

Both tools print plain text when their output is piped — no ANSI colour
reaches you — so what you read is what the bytes cost.

## Know what the corpus is before you trust it

Do not quote coverage numbers from memory — they change with every fetch.
Ask the index, which takes a second:

```bash
python3 tools/query.py --stats            # talks, transcripts, conferences, per year and per conference
python3 tools/query.py "agent reliability" --facets   # the same counts, for this query's matches
```

Four properties change how you should answer, and all are visible in the data:

* **Transcript coverage is partial and very uneven.** `--stats` shows it per
  year and per conference; as a rule the transcripts are almost all on the
  most recent year's talks (99% of 2026, a few percent of 2025, none earlier)
  and some conferences (Ignite, re:Invent) have none at all. So a ranked list
  for any topic is dominated by 2026 and by the conferences with transcripts,
  **because that is where the quotable text is, not because that is where the
  topic was discussed**. Run `--facets` before choosing a slice, so you know
  what a `--year` or `--conference` filter will actually leave you. A talk
  without a transcript is a *title and a description*: enough to recommend it,
  not enough to state what the speaker argued. `has_transcript` says which is
  which, `query.py` marks transcript-bearing hits with `· transcript`, and
  `--transcript` filters to them — use it whenever the question needs a quote.
* **Descriptions are mostly YouTube descriptions**, written by the channel,
  often promotional, sometimes empty. The exceptions are the InfoQ talks and
  the seeded WeAreDevelopers programme, whose descriptions are real abstracts.
* **`year` is the edition's year, not the upload date.** InfoQ posts a
  conference's recordings for a year afterwards; a talk filed under 2025 was
  given in 2025 however late it appeared. `--since`/`--before` go by the
  publication date, which is a different thing (and falls back to the year
  for the fifth of the talks that have no date).
* **Not every talk is a YouTube video.** Each record has a `url` — the
  canonical link — and a `youtube_url` that is `null` for the talks that exist
  only as InfoQ pages (their ids start with `iq-`). Link to `url`.

A few transcripts are not English, and a dozen labelled Hindi are English
audio the ASR mis-read; they count in the totals and cannot answer an English
query. Nothing filters on it; if a talk that should match does not, that may
be why.

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
python3 tools/query.py "context engineering" -n 15 --brief
python3 tools/query.py --list-conferences        # valid slugs; --list-categories too
```

**`-n` here is the number of results.** In `excerpt.py` the same letter is a
budget of passages per talk — do not carry `-n 15` from this step into the
next one.

**Search for the topic's words, not for the question.** A bare query is
reduced to its content words — "what do people say about agent reliability"
is searched as `agent reliability` — but the reduction is a safety net, not a
strategy: `evals for agents in production` is a better query than the sentence
it came from, and you choose the vocabulary. Every word has to appear
somewhere in a talk, metadata or transcript, for it to rank; when no talk has
all of them, the search drops a word no talk says (a typo) first, then the
commonest, one at a time, and **says so on stderr** (`no talk has every word —
dropped X`) — read that line, because it tells you what the results are
actually about. A short list of abbreviations is expanded for you (`eval` →
`evals`, `evaluation`; `rag`, `mcp`, `k8s`, `llm`, `genai`, `fine-tuning`…);
the expansion is printed on stderr too.

`--brief` prints one block per hit — title, speakers, conference, year,
duration, whether it has a transcript, which layer matched, the description
snippet, the URL. That is what you need in order to *choose*, at about a fifth
of the bytes of `--json`. **It contains nothing quotable**: the snippet is
from the description, and the transcript moments are left out. Reach for
`--json --brief` when you are going to compute something from the results,
`--fields a,b,c` to choose the columns yourself, `--md` for a table, and for
full `--json` — tags, channel, publication date, four transcript moments per
hit — only when the question is about those fields.

Stemming is on (`agents`, `agentic` and `agent` are one word to the index), so
an OR chain should carry **synonyms and adjacent vocabulary, not
inflections**. People say the same thing many ways; cover the vocabulary
**inside one query** rather than by running five:

```bash
python3 tools/query.py 'evals OR guardrails OR "human in the loop" OR fine-tuning' -n 20 --brief
```

FTS5 ranks the union, so a talk that hits several of those terms rises to the
top by itself — and you pay for one result set instead of five overlapping
ones. Hyphenated and punctuated terms (`fine-tuning`, `gpt-4`, `c++`) are
safe inside an OR chain. The loop that works: search once, read the snippets
for the words the corpus itself uses for the thing — the product names, the
jargon, the phrase every third speaker reaches for — and re-query with those.
That second query is the one to build the answer on.

The rest of the syntax, when the question has a shape:

* `NEAR(agents memory, 10)` — "X in the context of Y": both words within ten
  of each other, which a bare `agents memory` (anywhere in the talk) is not.
* `-word` excludes talks that say it: `"agents -rag"` (quote the query, or
  let the shell split it; both work).
* Column filters: `title:agents`, `speakers:"harrison chase"`, `{title
  tags}:rag`, `transcript:kubernetes` — the last scopes a word to what was
  *said* rather than what the channel wrote.
* `"exact phrase"`, `prefix*`, `AND`/`OR`/`NOT` as in FTS5.

Filters: `--conference langchain-interrupt` (repeatable), `--category "AI
security"`, `--year 2026` (repeatable), `--min-year` / `--max-year`,
`--since` / `--before YYYY-MM-DD`, `--speaker NAME` (part of a name is
enough), `--min-duration` / `--max-duration MIN`, `--transcript`,
`--exact-timing`. `--sort newest|oldest|duration|title` reorders the
best-scoring candidates; with no query at all the filters simply list the
corpus, newest first, and `--random --seed N` draws from it.

**To compare conferences or years, do not run one query per conference.**
`--per-conference K` and `--per-year K` give the best K of each in one ranked
set, and `--facets` first tells you which of them have anything to give:

```bash
python3 tools/query.py "agent memory" --facets
python3 tools/query.py "agent memory" --per-conference 3 --transcript --brief
python3 tools/query.py "agent memory" --per-year 5 --brief         # "how did the framing change"
```

A title that was uploaded two or three times — same conference, same talk —
comes back as one hit with `(also: id, id)` under it. That is one talk, not
several speakers agreeing.

`--explain` shows each hit's per-layer scores when a ranking surprises you.
`--ids` prints only the video ids, one per line, which is what `excerpt.py`
takes; `--excerpt` skips that hand-off and prints the excerpts for the hits
after the list, `--passages N` setting their budget (see the next step). With
`--excerpt` the relaxation and semantic-layer notes move from stderr into the
output, as `_note: …_` lines.

### 2. Read what those talks actually say

`query.py` ranks and snippets; it does not give you the argument. `excerpt.py`
does, for as many talks at once as you like, and `query.py --excerpt` does the
same for a result set in one call:

```bash
python3 tools/excerpt.py O72p-rBb2bA 5ID22ACI7IM -q "eval driven development"
python3 tools/query.py "agent memory" -n 6 --transcript --excerpt
python3 tools/query.py "agent memory" -n 6 --transcript --ids | xargs python3 tools/excerpt.py -q "agent memory"
```

It prints each talk's metadata, its description, its **opening** — where a
speaker states what they are about to argue — and a window of continuous
speech around each passage that matched, deep-linked to the second. It closes
with how much of the transcript you have seen, so a thin excerpt is visible as
one. Anything it had to decide for you — the query relaxed, nothing matched,
a budget ran out — is printed **in the output** as `_note: …_`, not on stderr,
so read the notes before the passages.

Give `-q` the same topic you searched for. Inside one talk a multi-word `-q`
falls back to the OR of its words when no 25-word passage holds all of them,
and the passages then rank by the rarest word — so if the excerpts are about
the wrong word, narrow `-q` rather than widen `-n`. Then choose the view by
what you need and what it costs (measured on 30-40 minute talks, ±30%):

| view | what you get | cost a talk |
|---|---|---|
| default (`-n 6`) | header, opening, ~6 windows of 80 s merged where they touch | ~1,100 tokens (median 850) |
| `-n 3` | the same header and opening, fewer windows | ~1,000 — the fixed part is ~450 of either |
| `-n 10 --window 90` | the argument in full, for the one talk that is the answer | ~1,900 |
| `--quotes` | only the sentence holding a query word, one line a hit, timestamped | ~30 a quote, ~200 a talk |
| `--outline` | the talk in 2-minute buckets: the query's density and the bucket's words | ~17 a bucket: ~370 for 35 min, ~500 for an hour |
| `--full` | the whole transcript | ~8,000 |

* **`-n` is a budget of speech, not a count of quotes.** `-n 3` buys three
  windows' worth of transcript, which the merge may hand back as one wide
  passage or three narrow ones. On a typical talk the hits are few enough
  that `-n 3` and `-n 6` show the same passages; `-n` matters on the dense
  talk, where it is what keeps six windows from growing into the transcript.
* **`--quotes`** when you need the exact words and their timestamp and
  nothing else — the citation view. Each line is the sentence that holds the
  query word (split on `.?!` across the hit and its neighbouring tiles; an
  unpunctuated ASR transcript falls back to the 25-word tile). `-n` is a
  count of quotes here. Cheap enough to run over twenty talks.
* **`--outline`** when a talk is long and you do not know where the topic
  is: the `#` column counts the query's words per bucket and is the reliable
  part; the words are the bucket's most distinctive stems by tf-idf within
  the talk, a hint at the subject, not a summary. Aim a second `-q`, or an
  `--at`, at the dense buckets.
* **`--at m:ss`** (repeatable, or comma-separated) reads a window at a
  moment, with or instead of `-q` — for an outline bucket, a timestamp from
  a `query.py` moment, or a semantic hit that says the thing without saying
  the words. With `--quotes` it gives the sentence under that moment.
* **`--words N` / `--total-words N`** when you are budgeting in tokens
  rather than seconds (a word is ~1.3 tokens): a cap per talk, or a cap
  across every talk on the command line, shared out in order. The tighter of
  `-n` and `--words` wins.
* `--full` for the whole transcript. Justified when the user asks about one
  named talk end to end; never as the default, and never for several talks at
  once.
* `--json` when you need the passages, quotes or outline as data.

Reading the markdown file directly is for when you want the record itself — its
frontmatter, its tags — not for finding a quote. `excerpt.py` accepts the
markdown path, a YouTube URL, and ids that start with a hyphen (about one in
thirty do) as well as the plain id.

### The optional semantic layer

`tools/install_semantic.sh` builds a small static-embedding index (model2vec,
no torch) in a separate virtualenv; nothing else in the repo needs it. When
it is present `query.py` uses it automatically for bare queries, fusing its
ranking with FTS5's as a union, so a talk that means the question without
saying its words can appear, and says on stderr how many it added that way.
`--semantic` insists on it (and errors if it is missing), `--no-semantic`
turns it off; when it is simply not installed the search runs on FTS5 alone
and silently (`--explain` prints why). A hit that came only from the semantic
side is marked `(semantic match: none of the query's words, near it in
meaning)` and **carries no snippet or moments** — none of the query's words
are in it. `query.py --excerpt` handles that by itself, centring the excerpt
on the passages nearest the query's meaning; if you go through `excerpt.py`
by hand, give it `--at m:ss` from an `--outline` or a `query.py` moment, or
a `-q` in the talk's own vocabulary, rather than the `-q` you searched with,
which will find nothing and show the opening.

### 3. Synthesize

For "what do people think about X" questions, structure the answer around
**positions, not talks**:

- Group speakers who broadly agree; name the axis they disagree on.
- Attribute every claim to a named speaker and the conference they said it at.
  Speaker names are extracted from titles and descriptions and are missing on
  about two fifths of the talks — say "a speaker at <conference>" rather than
  guessing a name.
- Quote only from transcripts, never from descriptions (a YouTube description
  is a promise written by a marketing team, not a statement). `--quotes` is
  the view built for this.
- Link each point to the recording, using the talk's `url`. For a YouTube
  talk, deep-link with `&t=<seconds>s`; an InfoQ page takes no timestamp
  parameter, so give the time in words. A timestamp printed as `~12:34` is
  **interpolated from word position**, not measured — cite it as approximate
  ("around 12 minutes in"), never to the second.
- Say plainly when the corpus is thin: if only two talks touch the topic, or if
  none of the matching talks has a transcript, that is part of the answer —
  and say when the spread you found is the corpus's (all 2026, one
  conference) rather than the field's.

### What a question should cost

A one-sentence question is one search and a handful of excerpts — on the order
of 15k tokens, not 150k: `--brief -n 15` is about 1.5k tokens, six default
excerpts about 7k, `--quotes` over the same six about 1.2k. Past that you are
almost certainly reading transcript you did not need. Widen deliberately
instead: another `-q` against the talks you already have is cheaper, and
likelier to be relevant, than another talk read end to end.

### Fetching what is missing

If the question turns on a talk whose transcript has not been fetched, you can
get it — but it is metered, so ask before spending it:

```bash
python3 tools/fetch_transcripts.py --probe                 # is this network usable?
python3 tools/fetch_transcripts.py -c ai-engineer --limit 10 --source exact
python3 tools/sync_catalog.py && python3 tools/build_index.py    # fold it in
```

`--limit` runs one round and returns, so it disables `--retry-after`; the
fetcher says so when both are given. An `iq-` talk is never fetched — its
transcript came with its page.
