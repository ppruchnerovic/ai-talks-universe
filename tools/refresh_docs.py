#!/usr/bin/env python3
"""Rewrite the corpus counts the docs quote, from the index, not from memory.

    python3 refresh_docs.py            # patch README.md, docs/GUIDE.md, docs/STATE.md
    python3 refresh_docs.py --check    # exit 1 if any of them is stale, write nothing

The publishing spec's "Numbers to refresh" table lists which document holds
which number. This script owns the ones that are a pure function of the
corpus: talks, transcripts, conferences, videos enumerated, the survivors of
the year floor, the InfoQ-only presentations, and the 2026 scope with its
transcribed share. Every one is written by a regular expression that must
match exactly once; a sentence that has been reworded fails loudly here
rather than drifting silently, and the fix is to update the pattern below.

The state table in docs/STATE.md is prose with history in it (what changed
on which day and why) and is deliberately not touched: that is a write-up,
and belongs to whoever reviews the refresh pull request.
"""
import argparse
import glob
import json
import re
import sys

import atu
import query

YEAR = 2026


def numbers() -> dict:
    con = atu.connect()
    st = query.stats(con)
    talks = atu.load_talks()
    infoq_only = sum(1 for t in talks if not t.get("youtube_url"))
    enumerated = sum(json.load(open(f))["count"]
                     for f in glob.glob(str(atu.ROOT / "data" / "catalog" / "*.json")))
    scope = next((y for y in st["years"] if y["year"] == YEAR), {"talks": 0, "transcripts": 0})
    return {
        "talks": st["talks"],
        "transcripts": st["transcripts"],
        "conferences": st["conferences"],
        "enumerated": enumerated,
        "survive": st["talks"] - infoq_only,
        "infoq_only": infoq_only,
        "scope_talks": scope["talks"],
        "scope_transcripts": scope["transcripts"],
    }


def fmt(n: int) -> str:
    return f"{n:,}"


# (file, pattern, replacement). \s+ where the docs wrap the sentence, so a
# reflow does not break the match; every group is a number this script owns.
RULES = [
    ("README.md",
     r"\*\*[\d,]+ talks from \d+ conferences, [\d,]+ of them with a full transcript\.\*\*",
     lambda n: f"**{fmt(n['talks'])} talks from {n['conferences']} conferences, "
               f"{fmt(n['transcripts'])} of them with a full transcript.**"),
    ("docs/GUIDE.md",
     r"\*\*[\d,]+ talks from \d+ conferences, [\d,]+ of them with a full transcript\.\*\*",
     lambda n: f"**{fmt(n['talks'])} talks from {n['conferences']} conferences, "
               f"{fmt(n['transcripts'])} of them with a full transcript.**"),
    ("docs/GUIDE.md",
     r"Of [\d,]+ videos enumerated, [\d,]+ survive; with the [\d,]+ presentations that(\s+)"
     r"exist only on infoq\.com the corpus is [\d,]+\.",
     lambda n: f"Of {fmt(n['enumerated'])} videos enumerated, {fmt(n['survive'])} survive; "
               f"with the {fmt(n['infoq_only'])} presentations that\\1"
               f"exist only on infoq.com the corpus is {fmt(n['talks'])}."),
    ("docs/GUIDE.md",
     rf"[\d,]+ of the [\d,]+ talks are {YEAR},(\s+)of which [\d,]+ have a transcript",
     lambda n: f"{fmt(n['scope_talks'])} of the {fmt(n['talks'])} talks are {YEAR},\\1"
               f"of which {fmt(n['scope_transcripts'])} have a transcript"),
    ("docs/STATE.md",
     r"[\d,]+ talks / [\d,]+ transcripts / \d+ conferences / [\d,]+ enumerated",
     lambda n: f"{fmt(n['talks'])} talks / {fmt(n['transcripts'])} transcripts / "
               f"{n['conferences']} conferences / {fmt(n['enumerated'])} enumerated"),
]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="report stale numbers, write nothing")
    args = ap.parse_args(argv)

    n = numbers()
    print("corpus: " + ", ".join(f"{k} {v:,}" for k, v in n.items()))
    stale = 0
    for rel in dict.fromkeys(r[0] for r in RULES):
        path = atu.ROOT / rel
        before = path.read_text(encoding="utf-8")
        after = before
        for rule_rel, pattern, repl in RULES:
            if rule_rel != rel:
                continue
            hits = re.findall(pattern, after)
            if len(hits) != 1:
                print(f"{rel}: pattern matched {len(hits)} times, expected 1 — "
                      f"the sentence was reworded; update RULES in {__file__}", file=sys.stderr)
                return 2
            after = re.sub(pattern, lambda m, repl=repl: repl(n).replace("\\1", m.group(1) if m.groups() else ""), after)
        if after != before:
            stale += 1
            if args.check:
                print(f"{rel}: stale")
            else:
                path.write_text(after, encoding="utf-8")
                print(f"{rel}: updated")
        else:
            print(f"{rel}: current")
    if args.check and stale:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
