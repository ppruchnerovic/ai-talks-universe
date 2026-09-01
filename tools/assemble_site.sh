#!/usr/bin/env bash
# Assemble the published site: only what index.html fetches, and nothing else.
#
#     tools/assemble_site.sh _site        # from the repo root, or anywhere
#
# pages.yml used to force-push `main` to `gh-pages`, so the site was every
# byte of the repository — 411 MB, 41% of GitHub Pages' 1 GB ceiling, of which
# 169 MB (the markdown, the catalogues, talks.json, the CSV) no browser ever
# requests. Transcripts are ~62 KB each and cover a third of the talks, so at
# full coverage the mirror would have been ~850 MB. The browser needs exactly
# four things, and this copies exactly those:
#
#     index.html, .nojekyll              the page
#     data/search-meta.json              the catalogue it loads up front
#     data/tindex/                       the transcript index, fetched by shard
#     data/transcripts/<id>.json         one file per "Find this in the talk"
#
# plus ai-conferences.md, which the footer links to. The `du` at the end is the
# size report: read it on every deploy, because build_index.py's 6 MiB trigger
# watches the up-front payload, not the site.
#
# The uitest `navigation` suite runs this and serves the result, so a path the
# page needs that this script forgets fails a test rather than a visitor.
set -euo pipefail

out="${1:?usage: assemble_site.sh OUT_DIR}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

rm -rf "$out"
mkdir -p "$out/data"
cp "$root/index.html" "$root/.nojekyll" "$root/ai-conferences.md" "$out/"
cp "$root/data/search-meta.json" "$out/data/"
cp -r "$root/data/tindex" "$out/data/tindex"
cp -r "$root/data/transcripts" "$out/data/transcripts"
rm -f "$out/data/transcripts/_misses.json"    # fetcher bookkeeping, not content

du -sh "$out"/data/* "$out"/index.html && du -sh "$out"
