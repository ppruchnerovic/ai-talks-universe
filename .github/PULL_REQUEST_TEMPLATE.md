## What

<!-- One or two sentences. Link the issue if there is one. -->

## Checklist

From "Verifying a change" in CONTRIBUTING.md. Tick what applies; delete what does not.

- [ ] `python3 check_registry.py` passes
- [ ] The offline suites pass (`test_query`, `test_excerpt`, `test_infoq`, `test_speakers`, `test_topics`, `test_semantic`, `test_fetch_transcripts`, `test_stem`)
- [ ] Corpus or index changed: `sync_catalog.py` and `build_index.py` run twice leave `git status --porcelain` empty
- [ ] `index.html`, `build_index.py` or site assembly changed: `cd tools/uitest && node run.js` passes, skip count read
- [ ] `index.html` fetches something new: `tools/assemble_site.sh` updated in the same commit
- [ ] No derived artefact committed (`talks.db`, `_site/`, `data/embeddings/`, a venv)
- [ ] Specs in `specs/` still true, or fixed here
- [ ] Corpus counts, if quoted, come from `query.py --stats`
- [ ] User-visible change noted under *Unreleased* in `CHANGELOG.md`
