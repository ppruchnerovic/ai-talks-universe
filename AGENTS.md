# For AI agents working on this repository

Read [`specs/README.md`](specs/README.md) first. It is the spec map: what
the app is, which spec covers which files, how to route a task, and the
cross-cutting rules. Then read the one spec that covers the domain you are
touching, and do the task. Specs are the source of truth; if a spec is wrong,
fix the spec in the same change.

The rules that bite most often:

- Derive and index-build are offline and byte-identical. Run
  `sync_catalog.py` (no `--refresh`) and `build_index.py` twice and diff.
- Never quote corpus counts from memory. `python3 tools/query.py --stats`
  computes them.
- Edit `conferences.json` and `ai-conferences.md` together;
  `check_registry.py` verifies they agree.
- Never fetch transcripts from a cloud machine, and never commit a derived
  artefact. `CONTRIBUTING.md` has the verification order.
- Secrets are environment variables. Never write a value into the repo.

The Claude Code skill for *querying* the corpus, as opposed to working on
it, is `.claude/skills/ai-conference-talks/`.
