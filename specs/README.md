# Spec map

The entry point for a model working on this repo. Read this file, then the
one spec that covers the domain you are touching, then do the task. Specs
are the source of truth: trust them over re-reading the code, and if you
find a spec is wrong, fix the spec in the same change.

The prose for humans lives in `README.md`; the design rationale in
`ARCHITECTURE.md`; current numbers in `STATE.md`. Specs distil those plus
the code into what a model needs, and record where docs and code disagree
(the code wins).

## What the app is

A knowledge base of recorded talks from AI conferences (about fifty
conferences, tens of thousands of talks, several thousand with full
timestamped transcripts). It is a pipeline that turns a registry of
conferences into a static corpus, and three readers of that corpus.

```
conferences.json ─► sync_catalog.py ─► data/catalog/  (every video ever listed)
                         │  enrich.py    (descriptions, dates, tags via YouTube Data API)
                         │  infoq.py     (infoq.com metadata + transcripts)
                         │  import_kb.py (a conference's own agenda → data/seeds/)
                         ▼
   fetch_transcripts.py ─► data/transcripts/<id>.json   (the expensive column)
                         │
                         ▼  derive (offline, byte-identical from caches)
              talks/**.md · data/talks.json · data/talks.csv
                         │
                         ▼  build_index.py (offline)
              data/talks.db · data/search-meta.json · data/tindex/
                         │
        ┌────────────────┼─────────────────────┐
        ▼                ▼                     ▼
  index.html       query.py · excerpt.py    Claude Code skill
  (GitHub Pages)   (terminal)               ai-conference-talks
                         ▲
                 semantic.py (optional embeddings, RRF-fused into query.py)
```

Two properties carry everything else:

* Every stage caches to disk and is resumable. Derive and index-build
  touch no network and produce byte-identical output from the caches, so
  every derive-time rule (year floor, AI filter, speaker and topic
  extraction) can change without a fetch.
* The transcript is the only expensive column, and the only one with four
  suppliers. Everything about fetching exists to spend the cheapest
  supplier that returns exact timings.

## Which spec covers what

| Spec | Read it when you touch | Files it maps |
|---|---|---|
| [data-model.md](data-model.md) | The registry schema, what a talk record contains, how speakers/topics/year/AI filter are derived, the four corpus representations, shared helpers | `conferences.json`, `ai-conferences.md`, `tools/atu.py`, `tools/check_registry.py`, `talks/`, `data/talks.{json,csv}`, `test_speakers.py`, `test_topics.py` |
| [catalog-sync.md](catalog-sync.md) | Enumerating listings, enriching metadata, importing seeds or InfoQ, deriving the corpus, adding a conference | `tools/sync_catalog.py`, `tools/enrich.py`, `tools/infoq.py`, `tools/import_kb.py`, `data/catalog/`, `data/seeds/`, `data/infoq/`, `test_infoq.py` |
| [transcripts.md](transcripts.md) | Fetching captions, the route ladder, the four failure classes, the per-IP quota and egress pool, running an extraction | `tools/fetch_transcripts.py`, `data/transcripts/`, `logs/`, `test_fetch_transcripts.py` |
| [search-cli.md](search-cli.md) | The query language, ranking, the SQLite schema and `DB_SCHEMA_VERSION`, excerpt budgets, CLI output formats | `tools/query.py`, `tools/excerpt.py`, `data/talks.db`, `test_query.py`, `test_stem.py`, `test_excerpt.py` |
| [search-browser.md](search-browser.md) | The static page, its ranking and facets, the shard and meta file formats, the index builder, the UI test suites | `index.html`, `tools/build_index.py`, `tools/assemble_site.sh`, `data/search-meta.json`, `data/tindex/`, `tools/uitest/` |
| [semantic.md](semantic.md) | The opt-in embedding layer, its install, how it fuses into `query.py`, graceful absence | `tools/semantic.py`, `tools/build_embeddings.py`, `tools/install_semantic.sh`, `tools/requirements-semantic.txt`, `test_semantic.py`, `data/embeddings/` |
| [skill.md](skill.md) | The Claude Code skill: its retrieval ladder, citation rules, and every CLI flag and output string it depends on | `.claude/skills/ai-conference-talks/SKILL.md` |
| [publishing.md](publishing.md) | GitHub Pages publish, the weekly refresh, what is committed vs. ignored, local setup, the verification checklist, which doc holds which numbers, git conventions | `.github/workflows/*.yml`, `.gitignore`, `tools/refresh_report.py`, `tools/requirements.txt`, the six top-level docs |

## Routing by task

* Change what counts as a talk, who spoke, or what it is about → data-model.md, then catalog-sync.md for the rerun.
* Add or fix a conference → data-model.md (registry schema) and catalog-sync.md (recipe).
* Get more transcripts, or a fetch is failing → transcripts.md. Read its quota section before any run.
* Change search results in the terminal or the skill → search-cli.md. If the browser must match, also search-browser.md.
* Change the page, ranking in the browser, or a UI test → search-browser.md.
* Change a CLI flag or output field → search-cli.md, then skill.md for what must be updated in `SKILL.md`.
* Touch embeddings or hybrid ranking → semantic.md.
* CI, publishing, docs numbers, or "how do I verify this change" → publishing.md.

## Cross-cutting rules

* Derive and index-build must stay offline and byte-identical: run
  `sync_catalog.py` (no `--refresh`) and `build_index.py` twice and diff.
  publishing.md has the full checklist.
* Edit `conferences.json` and `ai-conferences.md` together; `check_registry.py` verifies they agree.
* Never quote corpus counts from memory. Compute them with `query.py --stats`, and update the docs listed in publishing.md when they change.
* Secrets are env vars sourced from the shell profile; never write values into the repo.
* Keep each spec 50–500 lines. Split before it grows past that.
