# Contributing

Thanks for looking. The most useful contribution is a conference the corpus
does not have yet; the recipe is below and needs no credentials. Bug fixes,
search improvements and doc corrections are welcome too. Everything here is
distilled from [`specs/publishing.md`](specs/publishing.md), which stays the
source of truth if the two ever disagree.

## Ground rules

- Open an issue before a large change so the approach can be agreed first.
  Small fixes can go straight to a pull request.
- Never commit secrets. API keys are read from environment variables and the
  tools degrade to free routes without them.
- Never commit derived artefacts: `data/talks.db`, `_site/`,
  `data/embeddings/`, any virtualenv. `.gitignore` covers them; check
  `git status --porcelain` after a rebuild.
- Do not fetch transcripts from CI or a cloud machine. YouTube meters the
  caption endpoint per IP and blocks cloud ranges. Fetch locally.
- Be kind. The [code of conduct](CODE_OF_CONDUCT.md) applies everywhere in
  this project.

## Local setup

Python 3.12 (CI pins it) and, for enumeration, `yt-dlp` on `PATH`. The
search CLI and the offline test suites need nothing else.

```bash
python3 -m venv tools/.venv && source tools/.venv/bin/activate
pip install -r tools/requirements.txt        # fetcher deps; yt-dlp also enumerates
cd tools/uitest && npm install && cd -       # Playwright + Chromium, only for the browser tests
tools/install_semantic.sh                    # optional embedding layer, see specs/semantic.md
```

Optional keys, both free tiers: `YOUTUBE_API_KEY` for descriptions and dates
(`docs/GUIDE.md` has the console recipe), `SUPADATA_API_KEY` for transcripts
from any network. Export them in your shell; nothing in the repo reads a file
for them.

## Adding a conference

1. Add a block to `ai-conferences.md` saying what the conference is, where its
   recordings live and why it belongs, and a matching entry to
   `conferences.json`. The `fields` object at the top of the JSON documents
   the non-obvious keys; copy a neighbouring entry for the shape.
2. Prefer per-edition playlists over a whole channel when the channel
   publishes far more than the conference. Use `"scope": "ai"` for a general
   conference with AI tracks, `"scope": "all"` for a dedicated one.
3. Run it:

   ```bash
   cd tools
   python3 check_registry.py                   # the two files must agree
   python3 sync_catalog.py --refresh -c <slug> # enumerate just this one
   python3 build_index.py
   python3 query.py --conference <slug> -n 5   # does it look right?
   ```

4. Commit `conferences.json`, `ai-conferences.md`, the new `data/catalog/`
   file, and the regenerated `data/talks.*`, `talks/`, `data/search-meta.json`
   and `data/tindex/`. Do not fetch transcripts in the same pull request.

If the recordings are unlisted on YouTube, enumeration cannot see them; read
"Adding a conference" in `docs/GUIDE.md` for the seed-file route.

## Verifying a change

In this order. A failure at one step stops the run.

1. `cd tools && python3 check_registry.py`
2. The offline suites, all under a few seconds except `test_stem.py`:

   ```bash
   python3 test_query.py && python3 test_excerpt.py && python3 test_infoq.py && \
   python3 test_speakers.py && python3 test_topics.py && python3 test_semantic.py && \
   python3 test_fetch_transcripts.py && python3 test_stem.py
   ```

   CI runs these on every pull request, plus `ruff check`.
3. If the corpus or the index changed, prove idempotence: run
   `python3 sync_catalog.py && python3 build_index.py` twice and confirm
   `git status --porcelain` is empty after the second run.
4. If you touched `index.html`, `build_index.py` or the site assembly:
   `cd tools/uitest && node run.js`. About four minutes. Read the skip count
   as well as the failures.
5. If you changed what `index.html` fetches, change `tools/assemble_site.sh`
   in the same commit. Nothing else publishes it.

The pull request template repeats this list as checkboxes.

## Docs and numbers

- Never quote corpus counts from memory. `python3 query.py --stats` computes
  them; `specs/publishing.md` lists which files carry which numbers.
- Specs in `specs/` are the source of truth for an agent working on the
  repo. If your change makes a spec wrong, fix the spec in the same pull
  request.
- Finished items in `docs/TODO.md` are deleted, and their write-up goes into
  `docs/HISTORY.md` under a dated section.
- User-visible changes get a line under *Unreleased* in `CHANGELOG.md`.

## Git conventions

- Subject lines are full sentences in the imperative, no type prefix, no
  trailing period: *Publish only what the browser fetches, not the whole
  repository*. Doc-only commits may prefix the file: *STATE.md: …*.
- One branch per piece of work, merged with an explicit merge commit.
- Never base work on `automation/kb-refresh` (rewritten weekly by the bot)
  or `gh-pages` (one orphan commit, rewritten on every deploy).
