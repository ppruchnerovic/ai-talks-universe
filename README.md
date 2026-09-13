# AI talks universe

[![Tests](https://github.com/ppruchnerovic/ai-talks-universe/actions/workflows/tests.yml/badge.svg)](https://github.com/ppruchnerovic/ai-talks-universe/actions/workflows/tests.yml)
[![Deploy](https://github.com/ppruchnerovic/ai-talks-universe/actions/workflows/pages.yml/badge.svg)](https://github.com/ppruchnerovic/ai-talks-universe/actions/workflows/pages.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey.svg)](DATA-NOTICE.md)

A searchable knowledge base of recorded talks from the world's AI conferences:
titles, descriptions, speakers, conference and year, recording links and, where
they have been fetched, full timestamped transcripts.

**9,831 talks from 53 conferences, 3,437 of them with a full transcript.**
More numbers in [`docs/STATS.md`](docs/STATS.md); which conferences and why in
[`ai-conferences.md`](ai-conferences.md).

## Browse it

<https://ppruchnerovic.github.io/ai-talks-universe/>

No install, works on a phone, and the URL carries the search so a link
reproduces the view. Type a subject, filter by conference, conference type,
topic, speaker or year, and click **Find this in the talk** to jump to the
seconds where a phrase is spoken. The search box takes `"phrases"`,
`title:`, `speaker:`, `transcript:`, `-excluded` words, `OR` and `prefix*`.

## Search it from the terminal

Everything below runs on Python 3.12's standard library; nothing to install.

```bash
git clone https://github.com/ppruchnerovic/ai-talks-universe.git
cd ai-talks-universe/tools
python3 query.py "context engineering"
python3 query.py "prompt injection" --category security -n 20
python3 query.py "agent memory" -n 6 --excerpt      # the hits, then what each one says
python3 query.py --speaker "harrison chase" --sort newest
python3 excerpt.py O72p-rBb2bA -q "eval driven development"
python3 query.py --stats                            # what the corpus is, from the index
```

The first query builds a SQLite FTS5 index in about a minute and says so on
stderr. `--json`, `--md`, `--brief` and `--ids` are for scripts; `--help`
lists the rest. The clone is about 450 MB, nearly all of it the corpus
itself, so `--depth 1` saves little.

An optional semantic layer (`tools/install_semantic.sh`, static embeddings,
no torch) adds matching by meaning and is fused into the same ranking.

## Ask it questions with Claude Code

The `ai-conference-talks` skill under `.claude/skills/` loads in any Claude
Code session started in this directory. Ask *what do speakers at different
conferences say about agent reliability* and it searches, reads the matching
passages and compares the positions, citing talk and timestamp.

## What is in the box

```
index.html            the browser UI, published to GitHub Pages
conferences.json      the registry: which channels and playlists to read, and how to filter them
ai-conferences.md     the human curation behind the registry
data/talks.json       the canonical corpus (also talks.csv)
data/transcripts/     one JSON file of timestamped segments per transcribed talk
talks/<conf>/*.md     one readable markdown file per talk, transcript inlined
tools/                the pipeline and the search CLI
docs/                 the long-form documentation
specs/                one spec per domain, written for a model working on the repo
```

## How it is built

```
conferences.json ─► sync_catalog.py ─► data/catalog/     every video the sources list
                         │  enrich.py                    descriptions, dates, tags
                         │  infoq.py                     infoq.com metadata and transcripts
                         ▼
   fetch_transcripts.py ─► data/transcripts/<id>.json   the expensive column
                         ▼  derive (offline, byte-identical from the caches)
              talks/**.md · data/talks.json · data/talks.csv
                         ▼  build_index.py (offline)
              data/talks.db · data/search-meta.json · data/tindex/
                         ▼
      index.html  ·  query.py / excerpt.py  ·  the Claude Code skill
```

Every stage caches to disk and is resumable, so enumeration can be redone
daily for nothing while transcripts accumulate over months. A daily run of
`tools/refresh_local.sh` on the maintainer's machine re-enumerates, enriches,
fetches up to 300 new transcripts and opens a pull request with a coverage
report; merging it is what publishes. It runs locally rather than in CI
because YouTube meters the caption endpoint per IP and blocks cloud ranges.

## Documentation

| Read | For |
|---|---|
| [`docs/GUIDE.md`](docs/GUIDE.md) | The full guide: data sources, what survives into the corpus, search syntax, rebuilding, adding a conference, fetching transcripts, testing |
| [`specs/ARCHITECTURE.md`](specs/ARCHITECTURE.md) | Current system boundaries, data flows, artifact ownership and links to detailed diagrams and contracts |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Design rationale, tradeoffs and historical measurements, alongside links to canonical spec diagrams |
| [`docs/STATE.md`](docs/STATE.md) | Where the corpus and the tools stand today, and the handoff for the next collection run |
| [`docs/STATS.md`](docs/STATS.md) | The corpus by the numbers |
| [`docs/TODO.md`](docs/TODO.md) | Open items |
| [`docs/HISTORY.md`](docs/HISTORY.md) | Dated write-ups of every session's work, kept verbatim |
| [`specs/README.md`](specs/README.md) | The spec map: the entry point for an AI agent working on this repo |
| [`CHANGELOG.md`](CHANGELOG.md) | User-facing changes, by date |

## Contributing

Adding a conference is the most useful contribution and needs no credentials;
[`CONTRIBUTING.md`](CONTRIBUTING.md) has the recipe, the local setup and how
a change is verified. Bug reports and conference requests go through the
issue templates.

## Licence

The code is under the [MIT licence](LICENSE). The curated data, meaning the
registry, the taxonomy and the derived fields, is under
[CC BY 4.0](DATA-NOTICE.md). Transcripts and descriptions belong to the
speakers, conferences and channels that published them; the project claims
nothing over them, and [`DATA-NOTICE.md`](DATA-NOTICE.md) says how to have a
talk removed.
