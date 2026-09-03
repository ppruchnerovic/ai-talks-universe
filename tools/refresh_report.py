#!/usr/bin/env python3
"""Compare the corpus in the working tree against the one committed, and say
whether a refresh improved it or hollowed it out.

Written after a scheduled `kb-refresh` run committed straight to `main` and
wrote `channel: null` over ~4,540 talks. Enumeration from a GitHub runner is
throttled by YouTube, and the throttling does not fail the run — it returns
videos with titles and durations and no uploader, which `sync_catalog.py` then
writes over good data.

Neither existing backstop caught it, because both count videos: a source that
comes back empty keeps its cached videos, and the corpus refuses to shrink more
than 10% without `--allow-shrink`. That run returned a plausible *number* of
videos with a field hollowed out, so nothing tripped. What is missing is a
check on how full the records are, not how many there are.

So this reports per field, and treats a populated field going empty as the
regression it is. A refresh is allowed to add talks and fill fields; it is not
allowed to take descriptions, channels, dates or tags away, because nothing
downstream can tell a field that was never collected from one that was lost.

    python3 refresh_report.py                 # markdown to stdout
    python3 refresh_report.py --base HEAD     # against a different commit

Exit codes are meant for CI: 0 clean, 1 could not read a baseline, 2 a field
regressed past --tolerance. The report is written either way — the point is to
make a 4,000-file diff reviewable, not to hide it.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys

import atu

# Fields worth watching. A refresh legitimately adds to all of them; every one
# of them has also been silently emptied by a throttled run.
FIELDS = ("channel", "description", "year", "speakers", "tags", "published_at", "topics")

# Fraction of the corpus a field may lose before the run is called a
# regression. Small non-zero: re-enumeration does drop the occasional video
# whose uploader deleted it, and that legitimately takes its fields with it.
TOLERANCE = 0.02


def committed_talks(ref: str) -> list[dict] | None:
    """The corpus as of `ref`, or None when there is nothing to compare to."""
    try:
        blob = subprocess.run(
            ["git", "show", f"{ref}:data/talks.json"],
            cwd=atu.ROOT, capture_output=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    doc = json.loads(blob)
    return doc["talks"] if isinstance(doc, dict) and "talks" in doc else doc


def filled(talks: list[dict], field: str) -> int:
    return sum(1 for t in talks if t.get(field))


def report(base: list[dict], now: list[dict], tolerance: float) -> tuple[str, bool]:
    """Markdown, and whether anything regressed past the tolerance."""
    base_ids = {t["video_id"] for t in base}
    now_ids = {t["video_id"] for t in now}
    added, dropped = now_ids - base_ids, base_ids - now_ids

    limit = max(1, int(len(base) * tolerance))
    rows, regressed = [], []
    for f in FIELDS:
        was, is_ = filled(base, f), filled(now, f)
        delta = is_ - was
        if delta < -limit:
            regressed.append((f, was, is_))
            mark = "🔴 **lost**"
        elif delta < 0:
            mark = "within tolerance"
        elif delta > 0:
            mark = "gained"
        else:
            mark = "—"
        rows.append(f"| `{f}` | {was:,} | {is_:,} | {delta:+,} | {mark} |")

    out = [
        "## Catalogue refresh",
        "",
        f"**{len(base):,} talks → {len(now):,}** "
        f"({len(added)} added, {len(dropped)} dropped).",
        "",
        "### Field coverage",
        "",
        "| Field | Before | After | Δ | |",
        "|---|---:|---:|---:|---|",
        *rows,
        "",
        f"A field may lose up to {tolerance:.0%} of the corpus "
        f"({limit:,} talks) before it is called a regression.",
    ]

    if regressed:
        out += [
            "",
            "### 🔴 Do not merge as-is",
            "",
            "A refresh that *empties* a field has not found new information — it "
            "has overwritten good records with throttled ones. Nothing "
            "downstream can distinguish a field that was never collected from "
            "one that was lost, so this needs a look before it reaches `main`.",
            "",
            *(f"- `{f}`: {was:,} → {is_:,} (**{is_ - was:+,}**)"
              for f, was, is_ in regressed),
        ]
    else:
        out += ["", "### ✅ No field regressed", ""]

    if added:
        out += ["", "### Talks added", ""]
        by_id = {t["video_id"]: t for t in now}
        for vid in sorted(added)[:40]:
            t = by_id[vid]
            out.append(f"- `{vid}` {t['conference']} — {t['title'][:90]}")
        if len(added) > 40:
            out.append(f"- …and {len(added) - 40} more")

    if dropped:
        out += ["", "### Talks dropped", ""]
        by_id = {t["video_id"]: t for t in base}
        for vid in sorted(dropped)[:40]:
            t = by_id[vid]
            out.append(f"- `{vid}` {t['conference']} — {t['title'][:90]}")
        if len(dropped) > 40:
            out.append(f"- …and {len(dropped) - 40} more")

    return "\n".join(out) + "\n", bool(regressed)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", default="HEAD",
                    help="commit to compare against (default: HEAD)")
    ap.add_argument("--tolerance", type=float, default=TOLERANCE,
                    help=f"fraction a field may lose (default: {TOLERANCE})")
    ap.add_argument("-o", "--out", type=pathlib.Path,
                    help="also write the report here, relative to the cwd")
    args = ap.parse_args()

    base = committed_talks(args.base)
    if base is None:
        print(f"No committed corpus at {args.base} to compare against.",
              file=sys.stderr)
        sys.exit(1)

    text, regressed = report(base, atu.load_talks(), args.tolerance)
    print(text, end="")
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    sys.exit(2 if regressed else 0)


if __name__ == "__main__":
    main()
