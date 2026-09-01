#!/usr/bin/env python3
"""Check conferences.json against ai-conferences.md.

Two files describe the same set of conferences: the markdown is the human
curation — why a source is worth having, what is gated, what was rejected — and
the JSON is what the pipeline reads. They drift silently otherwise: a playlist
added to one and not the other produces either a conference nobody documented
or a documented conference with no talks.

Matching is per conference block (a `### ` heading in the markdown) rather than
per URL. A block usually lists both a channel and the per-edition playlists on
it, and the registry deliberately takes only one of the two — the playlists for
a vendor channel that publishes far more than its conference, the channel
itself for a dedicated one. Demanding every URL be registered would flag all of
those. What is worth flagging is a documented conference the pipeline reads
*nothing* from, and a registered source nobody documented.

    python3 check_registry.py          # exits non-zero on drift
    python3 check_registry.py --quiet  # only the summary
"""

from __future__ import annotations

import argparse
import re
import sys

import atu

MD = atu.ROOT / "ai-conferences.md"
YT_URL = re.compile(r"https://www\.youtube\.com/[^\s)\]]+")
SKIP_SECTION = re.compile(r"^##\s+(Checked but weak sources|Academic research)", re.I)


def markdown_blocks() -> dict[str, set[str]]:
    """`### heading` -> the YouTube URLs under it, minus the skipped sections."""
    blocks: dict[str, set[str]] = {}
    skipping, head = False, None
    for line in MD.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            skipping = bool(SKIP_SECTION.match(line))
            head = None
        elif line.startswith("### "):
            head = line[4:].strip()
            if not skipping:
                blocks.setdefault(head, set())
        if skipping or head is None:
            continue
        blocks[head].update(YT_URL.findall(line))
    return blocks


def key(url: str) -> str:
    """A playlist id, or a channel handle — the identity, not the exact URL.

    The markdown writes `@GOTO-/videos` where the registry may write
    `@GOTO-/videos` or a bare channel URL, and playlist links carry tracking
    query strings.
    """
    m = re.search(r"[?&]list=([\w-]+)", url)
    if m:
        return f"list:{m.group(1)}"
    m = re.search(r"youtube\.com/(@[\w.-]+|channel/[\w-]+|c/[\w.-]+)", url)
    if m:
        return f"chan:{m.group(1).lower()}"
    # The old vanity form, `youtube.com/infoq`, is the same channel as `@infoq`.
    m = re.search(r"youtube\.com/([\w.-]+)/?$", url)
    return f"chan:@{m.group(1).lower()}" if m else f"url:{url}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    reg = atu.load_registry()
    in_reg: dict[str, list[str]] = {}
    for c in reg["conferences"]:
        for s in c["sources"]:
            # A "videos" source is a file in data/seeds/ and an "infoq" one is
            # infoq.com's own presentation pages — neither is a YouTube
            # listing, so there is no channel or playlist for the markdown to
            # link to. The prose in the conference's block is where they are
            # documented.
            if s.get("type") in ("videos", "infoq"):
                continue
            in_reg.setdefault(key(s["url"]), []).append(c["slug"])

    blocks = markdown_blocks()
    documented = {k for urls in blocks.values() for k in map(key, urls)}

    unread = sorted(h for h, urls in blocks.items()
                    if urls and not any(key(u) in in_reg for u in urls))
    unlisted = sorted(k for k in in_reg if k not in documented)

    if not args.quiet:
        for h in unread:
            print(f"  documented but the pipeline reads nothing from it:  {h}")
        for k in unlisted:
            print(f"  registered but not in ai-conferences.md:  {k}  ({', '.join(in_reg[k])})")

    covered = len(blocks) - len(unread)
    print(f"\n{len(in_reg)} sources registered over {len(reg['conferences'])} conferences · "
          f"{covered}/{len(blocks)} documented conferences are read · "
          f"{len(unlisted)} registered sources are undocumented")
    sys.exit(1 if (unread or unlisted) else 0)


if __name__ == "__main__":
    main()
