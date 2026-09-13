# Spec map

The entry point for a model working on this repo. Read this file, then the
one spec that covers the domain you are touching, then do the task. Specs
are the source of truth: trust them over re-reading the code, and if you
find a spec is wrong, fix the spec in the same change.

Specs define current behavior and rules for changing it. This entry point
provides brief orientation and routing; [ARCHITECTURE.md](ARCHITECTURE.md)
maps system boundaries, artifact ownership and cross-domain contracts.
Domain specs own detailed behavior and their local diagrams. Docs explain
tradeoffs and rationale (`docs/ARCHITECTURE.md`), operation (`docs/GUIDE.md`),
current measurements (`docs/STATE.md`) and provenance (`docs/HISTORY.md`).
A doc's name, diagrams or use of present tense do not determine its role.
Specs never depend on explanatory docs having been read; cite doc sections,
not line numbers. If implementation and a spec disagree, fix the drift in
the same change.

## What the app is

A knowledge base of recorded AI conference talks. Collection tools retain
listings, metadata and transcripts in disk caches. Offline derivation turns
those caches into JSON, CSV and per-talk Markdown; an offline index build
serves the static browser and terminal readers. The Claude Code skill uses
the terminal tools, with optional embeddings available to CLI search.

See [the system boundary diagram](ARCHITECTURE.md#system-boundaries) when
changing how those pieces connect. For a local change, go directly to the
domain below.

## Which spec covers what

| Spec | Read it when you touch | Files it maps |
|---|---|---|
| [ARCHITECTURE.md](ARCHITECTURE.md) | System boundaries, major flows, artifact ownership, cross-domain dependencies | `specs/`, `docs/ARCHITECTURE.md` |
| [data-model.md](data-model.md) | The record/derivation diagrams, registry schema, what a talk record contains, how speakers/topics/year/AI filter are derived, the four corpus representations, shared helpers | `conferences.json`, `ai-conferences.md`, `tools/atu.py`, `tools/check_registry.py`, `talks/`, `data/talks.{json,csv}`, `tools/test_speakers.py`, `tools/test_topics.py` |
| [catalog-sync.md](catalog-sync.md) | The pipeline-stage diagram, enumerating listings, enriching metadata, importing seeds or InfoQ, deriving the corpus, adding a conference | `tools/sync_catalog.py`, `tools/enrich.py`, `tools/infoq.py`, `tools/import_kb.py`, `data/catalog/`, `data/seeds/`, `data/infoq/`, `tools/test_infoq.py` |
| [transcripts.md](transcripts.md) | Fetcher diagrams, fetching captions, the route ladder, the four failure classes, the per-IP quota and egress pool, running an extraction | `tools/fetch_transcripts.py`, `data/transcripts/`, `logs/`, `tools/test_fetch_transcripts.py` |
| [search-cli.md](search-cli.md) | Ranking, index and excerpt diagrams, the query language, ranking, the SQLite schema and `DB_SCHEMA_VERSION`, excerpt budgets, CLI output formats | `tools/query.py`, `tools/excerpt.py`, `data/talks.db`, `tools/test_query.py`, `tools/test_stem.py`, `tools/test_excerpt.py` |
| [search-browser.md](search-browser.md) | The browser request diagram, static page, its ranking and facets, the shard and meta file formats, the index builder, the UI test suites | `index.html`, `tools/build_index.py`, `tools/assemble_site.sh`, `data/search-meta.json`, `data/tindex/`, `tools/uitest/` |
| [semantic.md](semantic.md) | The semantic integration diagram, opt-in embedding layer, its install, how it fuses into `query.py`, graceful absence | `tools/semantic.py`, `tools/build_embeddings.py`, `tools/install_semantic.sh`, `tools/requirements-semantic.txt`, `tools/test_semantic.py`, `data/embeddings/` |
| [skill.md](skill.md) | The retrieval sequence and Claude Code skill: its retrieval ladder, citation rules, and every CLI flag and output string it depends on | `.claude/skills/ai-conference-talks/SKILL.md` |
| [publishing.md](publishing.md) | Publish/refresh diagrams, GitHub Pages publish, the daily local refresh, what is committed vs. ignored, local setup, the verification checklist, which doc holds which numbers, git conventions | `.github/workflows/*.yml`, `tools/check_specs.py`, `tools/refresh_local.sh`, `tools/refresh_docs.py`, `tools/systemd/`, `tools/install_refresh_timer.sh`, `.gitignore`, `tools/refresh_report.py`, `tools/requirements.txt`, `README.md`, `docs/`, `CONTRIBUTING.md` |

## Routing by task

* Change a system boundary or a flow across domains → ARCHITECTURE.md, then the linked contract owner.
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
* `tools/check_specs.py` verifies that every file the table above maps exists and that every script in `tools/` is named by some spec. Run it after adding, moving or deleting a tool.
