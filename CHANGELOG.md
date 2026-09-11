# Changelog

User-visible changes, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). There are no version
numbers: the corpus is continuous, so entries are dated. The detailed,
session-by-session record with numbers and provenance is
[`docs/HISTORY.md`](docs/HISTORY.md).

## Unreleased

### Added
- MIT licence for the code and a CC BY 4.0 notice for the curated data
  (`DATA-NOTICE.md`), with a takedown route.
- `CONTRIBUTING.md`, code of conduct, security policy, issue and pull request
  templates, this changelog.
- A tests workflow: the registry check, the eight offline suites and `ruff`
  on every push and pull request.
- `AGENTS.md` as the entry point for AI agents, pointing at the spec map.

### Changed
- The README is now a landing page. The long-form guide moved to
  `docs/GUIDE.md`, alongside `ARCHITECTURE`, `STATE`, `STATS`, `TODO` and
  `HISTORY`.

## 2026-09-06

### Changed
- Catalogue refresh: 749 new talks and 235 new transcripts; the 2026 scope is
  fully transcribed again.
- Talks that fall past a channel's `first: N` window are kept rather than
  dropped when the channel stops naming them.

## 2026-09-02

### Added
- InfoQ route: QCon and InfoQ Dev Summit presentations with their hand-edited
  transcripts, read from infoq.com at its crawl delay.
- Topic facet: fifteen per-talk topics in the browser and the CLI
  (`--topic`), crossing with the conference type (`--category`).
- Search enrichment in both rankers: whole-description postings, synonym
  groups, field filters, exclusions, `OR`, prefixes.
- Optional semantic layer (`tools/install_semantic.sh`) fused into
  `query.py` by reciprocal rank.
- Only what the browser fetches is published to GitHub Pages.

## 2026-09-01

### Added
- Seven conferences.
- `excerpt.py`: the passages of a talk that answer a question, with a budget.
- The Claude Code skill rewritten around a retrieval ladder.

### Changed
- Corpus floor set to 2023; the security conferences keep their back
  catalogue.

## 2026-08-31

### Added
- First public corpus: registry, enumeration, enrichment, transcript fetcher
  with four routes, SQLite and browser indexes, static search page, weekly
  refresh workflow.
- WeAreDevelopers World Congress 2026 imported from a seed file.

### Changed
- The weekly refresh proposes a review branch instead of committing to
  `main`, after a throttled run overwrote good records.
