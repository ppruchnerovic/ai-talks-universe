# Spec: the Claude Code skill `ai-conference-talks`

## What

`.claude/skills/ai-conference-talks/SKILL.md` is the prompt Claude Code loads
when a session started at the repo root gets a question about what was said at
an AI conference. It is the only file in the skill, the only tracked file
under `.claude/`, and it is prose for a model, not code: it never runs.

Its job is to make a model answer **from the corpus, cheaply**. It does that
by prescribing a retrieval ladder with a token price on each rung, and by
saying what the corpus is and is not (partial transcripts, promotional
descriptions, `year` is edition year, InfoQ talks have no YouTube URL).

Responsibilities:

- Trigger correctly (the frontmatter `description` is the activation text).
- Tell the model which CLI to run, with which flags, from which directory,
  and what each call costs in tokens.
- Tell the model how to cite (the `url` field, `&t=<seconds>s`, `~` means
  interpolated) and how to synthesize (positions, attributed, transcript-only
  quotes, say when the corpus is thin).
- Say what it must NOT do: answer from memory, `cat` a talk markdown to find a
  quote, quote coverage numbers from memory, quote descriptions, guess a
  missing speaker name, run one query per conference, carry `-n 15` from
  `query.py` into `excerpt.py`, fetch transcripts without asking (metered),
  or answer about talks outside the corpus.

Not responsible for: the search itself (`search-cli.md`, `semantic.md`), the
data (`data-model.md`, `transcripts.md`), the browser (`search-browser.md`).
The skill documents the tools; when they change, it is edited *last*
(HISTORY.md:1177 "Edit SKILL.md last, once the tools exist").

Cost anchor, measured (HISTORY.md:799 "Making the skill affordable"): the
pre-2026-09-01 skill said `cat talks/**.md` and cost ~150k tokens a question;
the ladder costs ~15-17k (`--brief -n 15` ~1.5k, six default excerpts ~7k,
`--quotes` over the same six ~1.2k). ARCHITECTURE.md:586 has the sequence
diagram.

## Where

| Path | What it is |
|---|---|
| `.claude/skills/ai-conference-talks/SKILL.md` (~340 lines) | The skill. Frontmatter + body, sections listed below. |
| `.claude/worktrees/` | Empty, untracked dir Claude Code uses for `isolation: worktree` agents. Not part of the skill; ignore. |
| `tools/query.py:1424-1502` | `main()` + argparse: every `query.py` flag the skill cites. |
| `tools/query.py:1235-1287` | `render()`: the text output the skill describes (`· transcript`, `· match:`, `(also: …)`, `topics:`, semantic-match label, moments with `&t=`, url line). |
| `tools/query.py:1560-1590` | The relaxation/expansion/semantic notes; stderr normally, stdout as `_note: …_` only under `--excerpt` (not `--json`/`--ids`). |
| `tools/query.py:1194-1211` | Colour gating: off when piped or under `NO_COLOR` (the skill's "plain text when piped"). |
| `tools/query.py:1215` | `fmt_ts`: `~m:ss` when the position is interpolated. |
| `tools/query.py:756-800` | `semantic_layer()`: lazy `import semantic`; auto when vectors exist, `--semantic` insists, `--no-semantic` off. |
| `tools/query.py:1073` | `resolve()`: one word of a label resolves a `--topic`/`--category`/`--conference` (`evals`, `security`, `build`). |
| `tools/excerpt.py:818-850` | `main()` + argparse: every `excerpt.py` flag the skill cites. |
| `tools/excerpt.py:174` | `find_talk()`: accepts id, `talks/<conf>/<id>-<slug>.md`, YouTube URL, hyphen-leading ids. |
| `tools/excerpt.py:689-694` | `print_notes()`: `_note: …_` lines in stdout. `:432` the "showing the opening" note. |
| `tools/excerpt.py:679` | `[m:ss](url&t=Ns)` deep links; `~m:ss` when guessed. |
| `tools/fetch_transcripts.py:994-1030` | `--probe`, `-c/--conference`, `--limit`, `--source exact`, `--retry-after` — the "Fetching what is missing" rung. |
| `tools/install_semantic.sh`, `tools/semantic.py`, `tools/build_embeddings.py` | The optional layer the skill's "semantic" section describes. See `semantic.md`. |
| `README.md:456` "With Claude Code" | The user-facing two-paragraph description and the canonical example question. |
| `ARCHITECTURE.md:586` | "The skill — a retrieval ladder with a price on it": sequence diagram, the 2026-09-02 rungs. |
| `HISTORY.md:799`, `HISTORY.md:1175-1195` | Why the ladder exists; section F, the 2026-09-02 revision list. |
| `STATE.md:41` | One-line status of the skill and its revision dates. |

### SKILL.md, section by section

| Section | Content |
|---|---|
| Frontmatter | `name: ai-conference-talks`; `description:` a block scalar naming the corpus (conferences, fields) and the triggers: what was said at a conference, who talked about X, compare/synthesize positions across speakers or vendors, which talks to watch, coverage across conferences/years, a specific talk's link/description/conference. Ends "Do NOT use it for talks outside this corpus." No other frontmatter keys. |
| Preamble | Repo layout table; run everything as `python3 tools/query.py …` **from the repo root** (subagent cwd resets); clone URL for other checkouts; output is plain text when piped. |
| "Know what the corpus is before you trust it" | Rung 0: `--stats`, `"q" --facets`. Four properties: transcript coverage is uneven by year and conference, read the `--stats` tables (`--transcript`, `has_transcript`, `· transcript`); descriptions are YouTube blurbs except InfoQ/WeAreDevelopers; `year` = edition year, `--since/--before` = publish date; `url` vs nullable `youtube_url` (`iq-` ids). Non-English/mislabelled-Hindi transcripts caveat. |
| "How to answer" | Always retrieve, never from memory. Never `cat` a talk markdown to find a quote (it costs what `--full` costs, more for a long talk). |
| 1. Find the talks | `query.py "topic words" -n 15 --brief`. `-n` = result count here. Search the topic's words, not the question; read the stderr `dropped X` / `expanded` line. `--brief` is for choosing and contains nothing quotable; `--json --brief`, `--fields`, `--md`, full `--json` when needed. Stemming on, so OR chains carry synonyms; search once, harvest the corpus's own vocabulary, re-query. Syntax: `NEAR()`, `-word`, column filters, phrases, prefixes. All filters. `--category` (venue type) crosses `--topic` (subject); `--topic X --facets` for the split. `--per-conference K` / `--per-year K` after `--facets`. `(also: id, id)` = re-uploads, one talk. `--explain`, `--ids`, `--excerpt`, `--passages N`. |
| 2. Read what those talks say | `excerpt.py IDS -q "topic"`, or `query.py … --excerpt`, or `--ids \| xargs`. Prints header, description, opening, matched windows deep-linked, closing coverage line; `_note: …_` in stdout. `-n` here = passage budget. Cost table per view (default `-n 6` ~1,100 tokens; `-n 3` ~1,000; `-n 10 --window 90` ~1,900; `--quotes` ~200/talk; `--outline` ~370-500; `--full` ~8,000). Bullets on `--quotes`, `--outline`, `--at m:ss`, `--words`/`--total-words`, `--full` (one named talk only), `--json`. Markdown file only for the record's frontmatter/tags. |
| The optional semantic layer | `install_semantic.sh`; auto for bare queries when present; `--semantic`/`--no-semantic`; semantic-only hits carry no snippet/moments; `query.py --excerpt` centres on meaning, hand `excerpt.py` needs `--at` or a `-q` in the talk's own words. |
| 3. Synthesize | Positions not talks; attribute to named speaker + conference, "a speaker at <conf>" when the name is missing; quote transcripts only; link `url`, `&t=<seconds>s` for YouTube, time in words for InfoQ; `~12:34` is interpolated, cite as approximate; say when the corpus is thin or the spread is the corpus's. |
| What a question should cost | ~15k tokens, not 150k; widen with another `-q` against talks already in hand. |
| Fetching what is missing | `fetch_transcripts.py --probe`, `-c CONF --limit N --source exact`, then `sync_catalog.py && build_index.py`. Ask before spending; `--limit` disables `--retry-after`; `iq-` talks are never fetched. |

### The ladder, as the skill prescribes it

| Rung | Command | Cost | Climb when |
|---|---|---|---|
| 0 | `query.py --stats`; `query.py "q" --facets` | ~0.5k | Always before quoting coverage or choosing a `--year`/`--conference` slice. |
| 1 | `query.py "topic words" -n 15 --brief` (+ filters, `--per-conference K`, `--transcript`) | ~1.5k | Always. Answers "which talks". Nothing quotable. |
| 2 | `excerpt.py IDS -q "topic"` or `query.py … --excerpt`; `--quotes` for citations, `--outline` then `--at` for long talks | ~1.1k/talk (`--quotes` ~0.2k) | Whenever the answer states what a speaker argued. Widen with another `-q`, not another talk. |
| 3 | `excerpt.py ID --full`, or the `talks/<conf>/<id>-<slug>.md` file | ~8k+/talk | One named talk end to end (`--full`), or the record's frontmatter/tags (the file). Never several at once, never to find a quote. |
| side | semantic layer inside rung 1 | free when installed | Automatic; not a rung the model climbs. Absent on this machine (`semantic.py --status`: `venv=False`). |

## How

### Couplings: what in SKILL.md must change when a tool changes

The skill quotes flag names and output strings verbatim; there is no test that
checks SKILL.md against argparse (`test_query.py`/`test_excerpt.py` cover the
flags themselves). Verified 2026-09-03: every flag below exists. When you
rename or reformat any of these, grep SKILL.md for the old string.

| Tool | Flags the skill cites | Output strings the skill describes |
|---|---|---|
| `query.py` | `-n`, `--brief`, `--json`, `--md`, `--fields`, `--ids`, `--excerpt`, `--passages`, `--stats`, `--facets`, `--list-conferences`, `--list-categories`, `--list-topics`, `--conference`, `--category`, `--topic`, `--year`, `--min-year`, `--max-year`, `--since`, `--before`, `--speaker`, `--min-duration`, `--max-duration`, `--transcript`, `--exact-timing`, `--sort newest\|oldest\|duration\|title`, `--random`, `--seed`, `--per-conference`, `--per-year`, `--explain`, `--semantic`/`--no-semantic` | `· transcript`; `· match: …`; `(also: id, id)`; `topics: …`; `(semantic match: none of the query's words, near it in meaning)`; stderr `no talk has every word — dropped X`, `expanded X → …`, `semantic layer on: N talks found by meaning alone`; `_note: …_` under `--excerpt`; `~m:ss`; `&t=<seconds>s`; `--stats` per year/per conference/per topic tables; `--brief` field list (title, speakers, conference, year, duration, transcript, matched layer, topics, description snippet, url); JSON fields `url`, `youtube_url`, `has_transcript`, `matched`, `year` |
| `excerpt.py` | positional id / md path / YouTube URL / hyphen id, `-q`, `-n`, `--window`, `--at` (seconds or `m:ss`, repeatable/comma-separated), `--words`, `--total-words`, `--quotes`, `--outline`, `--full`, `--json` | `_note: …_`; "showing the opening"; the closing coverage line (`N of M words`, `N of M matching passages quoted`); `[m:ss](url&t=Ns)` and `~m:ss`; the `#` density column of `--outline`; 2-minute buckets; 80 s windows; 25-word tiles |
| `fetch_transcripts.py` | `--probe`, `-c`, `--limit`, `--source exact`, `--retry-after` | the "`--limit` disables `--retry-after`" message |
| `sync_catalog.py`, `build_index.py`, `install_semantic.sh` | invoked bare | — |

Not cited by the skill (safe to change without touching it): `query.py
--no-moments`, `--color`; `excerpt.py --opening`; all of `semantic.py`'s own
CLI (`--status`, `--chunks`, `--embed-query`, `--serve`).

The cost table (SKILL.md "2. Read…" and "What a question should cost") is
measured, not derived: if `WINDOW`, `OPENING`, `PASSAGES` (`excerpt.py:65-94`)
or the `--brief` field set change, re-measure on a 30-40 minute talk and update
the numbers. `HISTORY.md:799` records how they were measured, and
`excerpt.py`'s argparse epilog (`excerpt.py:821-824`) states the same figures
— keep the two in step.

### No corpus counts in SKILL.md

The skill tells the model never to quote coverage numbers from memory, so it
carries none itself (removed 2026-09-03): coverage is "read the `--stats`
tables", the security-topic/security-conference split is "`--topic security
--facets`", the topic count is "`--list-topics` prints them", missing
speakers, missing dates, hyphen-leading ids and mislabelled-Hindi transcripts
are described in words without a fraction. The token figures that remain
(cost table, "What a question should cost") are budgets, not corpus facts.
When a new corpus property is worth telling the model, phrase it as the
command that shows it, not as today's number.

### Status

As of `8b06088dc` (merge of `a54819aa3` "Enrich search on all three surfaces,
add the optional semantic layer", on top of `edcece352` "Tell the skill to ask
the index" and `0a57a43bb`/`1e72c1742`, topic facet and conference type) the
skill prescribes the full ladder above and every command in it runs as
written from the repo root: plain-text output when piped, `--stats` and
`--facets` as rung 0, `--brief`/`--ids`/`--excerpt`/`--passages` in rung 1,
`--per-conference`/`--per-year` for cross-conference and cross-year
questions, `--max-year`, the `(also: id, id)` duplicate collapse,
`excerpt.py --quotes`/`--outline`/`--at`/`--words`/`--total-words` in rung 2,
and the opt-in semantic layer (model2vec, union + RRF fusion, silent FTS5
fallback; `semantic.md`).

Two items the skill would use are still open and are tracked in `TODO.md`,
not here:

- `--related <id>` (more like this talk) — not in argparse; the skill does not
  mention it.
- The `--year A-B` range form — not in argparse; the skill tells the model to
  use `--min-year`/`--max-year` or a repeated `--year` instead.

When either lands, add the flag to the couplings table and to the skill.

### Testing the skill by hand

There is no automated skill test; the tools' tests are `cd tools && python3
test_query.py`, `test_excerpt.py`, `test_semantic.py` (README.md:824-853).
To test the skill, start Claude Code at the repo root and ask:

1. *"What do people at different conferences say about agent reliability?"*
   (README.md:460, ARCHITECTURE.md:595). Good: it runs `--stats` or
   `--facets`, one `--brief` search (maybe `--per-conference`), `excerpt.py`
   or `--excerpt` on a handful of ids; the answer is grouped by position,
   every claim names a speaker (or "a speaker at <conf>") and a conference,
   quotes come from transcripts with `&t=` links, `~` times are "around N
   minutes in", and it says the spread is mostly 2026 because that is where
   the transcripts are. Roughly 15-20k tokens; no `cat talks/…`.
2. *"Give me the recording link for the Trust Lifecycle talk at QCon."*
   Good: one `query.py` call, the `url` (`https://www.youtube.com/watch?v=0lKSZs38Jq8`), no excerpt.
3. A talk not in the corpus (e.g. a 2019 TED talk). Good: it searches, finds
   nothing, and says the corpus does not have it rather than answering from
   memory.

Watch the transcript for the failure modes the skill was written against:
`cat` on a markdown file, `-n 15` passed to `excerpt.py`, five near-identical
queries, a speaker name that is not in the output, a `~` timestamp cited to
the second, a quote whose words are in a description but not a transcript.

### Editing rules

- Edit SKILL.md **after** the tool change is merged, never before; every
  command in it must run as written from the repo root.
- Keep it under 500 lines (Claude Code's guidance; it is ~340). Add to the
  cost table or the couplings above rather than adding prose.
- Do not add a `cd tools` anywhere: subagent cwd resets between calls.
- Where SKILL.md and argparse disagree, argparse wins; fix the skill.
