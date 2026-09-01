#!/usr/bin/env python3
"""Read a talk without reading the whole talk.

`query.py` ranks talks and shows a ~26-word snippet per hit; the answer to
"what did this speaker actually argue" is longer than that. The obvious next
step is `cat talks/<conf>/<id>-<slug>.md`, and it is the expensive one: a
transcript-bearing file here averages 33 KB — roughly 8,500 tokens — and a
long workshop reaches 420 KB. Reading ten of them to answer one question
costs more context than the question is worth, and most of what it buys is
the parts of the talk that have nothing to do with the question.

So this prints the parts that do: the talk's own metadata, its opening —
where the thesis nearly always is — and a window of continuous speech either
side of each passage that matched, merged where those windows overlap, with a
deep link on each. Typically 1-2 K tokens instead of 8-9 K, and what is left
out is stated rather than silently dropped, so a thin excerpt is visible as
one and `--full` is a keystroke away.

    python3 excerpt.py O72p-rBb2bA -q "eval driven development"
    python3 excerpt.py O72p-rBb2bA 5ID22ACI7IM -q evals --window 60 -n 8
    python3 excerpt.py O72p-rBb2bA --full          # the whole transcript
    python3 excerpt.py O72p-rBb2bA -q evals --json
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys

import re

import atu
import query

# A YouTube id is 11 characters of [A-Za-z0-9_-] and about one in thirty starts
# with a hyphen — `-stDHMwbBRw` is a talk in this corpus. argparse reads such a
# token as an unknown option and refuses the run, which is exactly what
# `query.py --ids | xargs excerpt.py` produces sooner or later. So ids are
# lifted out of argv before argparse sees it.
ID_RE = re.compile(r"^-[A-Za-z0-9_-]{10}$")

# The options that take a value, so their value is never mistaken for an id.
TAKES_VALUE = {"-q", "--query", "-n", "--passages", "--window", "--opening"}

# Seconds either side of a matching segment. A segment is ~25 words, which is
# a sentence fragment; 40 seconds either side is ~200 words of context, which
# is a point being made rather than a phrase being said.
WINDOW = 40

# The opening is always included when there is a query, because a speaker
# states what they are arguing in the first minute and then argues it — a
# passage lifted from minute 34 is much harder to attribute without it.
OPENING = 60

PASSAGES = 6

# Candidates to rank before selecting: neighbouring hits collapse into one
# passage, so more raw hits than passages is what gives the selection below
# something to choose between.
OVERSAMPLE = 4

# What `-n` actually buys: n windows' worth of speech, which the merge may
# hand back as fewer and wider passages. A budget rather than a count, because
# counting passages bounds nothing — on a talk that says the query word every
# other minute, six windows that each grow to meet their neighbours are the
# whole transcript again, which is the thing being avoided.


def split_ids(argv: list[str]) -> tuple[list[str], list[str]]:
    """argv, with hyphen-leading video ids pulled out of it."""
    rest, ids, i = [], [], 0
    while i < len(argv):
        a = argv[i]
        if a in TAKES_VALUE:
            rest += argv[i:i + 2]
            i += 2
        elif ID_RE.match(a):
            ids.append(a)
            i += 1
        else:
            rest.append(a)
            i += 1
    return rest, ids


def die(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 1


COLS = ("n id title speakers conference conference_name category edition year "
        "duration_min url youtube_url page_url description has_transcript "
        "transcript_words").split()


def ids_in_filename(name: str) -> list[str]:
    """The ids a talks/<conf>/<id>-<slug>.md file name could be carrying.

    The id is everything before the slug, and the slug is joined on with a
    hyphen — the same character one YouTube id in six contains and one in
    thirty starts with (`O72p-rBb2bA`, `-stDHMwbBRw`), and the one an InfoQ
    id is made of (`iq-qcon-london-2026-…`). Cutting at the first hyphen was
    wrong for all three. A YouTube id is exactly the first eleven characters;
    anything else is tried as every hyphen-delimited prefix, longest first, so
    the InfoQ slug wins over the shorter prefixes it contains.
    """
    if name.endswith(".md"):
        name = name[:-3]
    out = []
    if atu.is_youtube_id(name[:11]):
        out.append(name[:11])
    parts = name.split("-")
    for i in range(len(parts), 0, -1):
        cand = "-".join(parts[:i])
        if cand and cand not in out:
            out.append(cand)
    return out


def find_talk(con, ident: str) -> dict | None:
    """Accept a video id, a YouTube URL, or the id embedded in a markdown path."""
    vid = atu.video_id(ident) or ident.strip()
    candidates = [vid]
    if "/" in vid or vid.endswith(".md"):  # talks/<conf>/<id>-<slug>.md
        candidates = ids_in_filename(vid.rsplit("/", 1)[-1])
    sql = f"SELECT {','.join(COLS)} FROM talks WHERE id=?"
    for cand in candidates:
        row = con.execute(sql, (cand,)).fetchone()
        if row:
            return dict(zip(COLS, row))
    return None


def spans_for(starts: list[float], window: float, limit: int) -> list[tuple[float, float]]:
    """Windows around the best-ranked hits, up to a fixed budget of speech.

    Best hit first, each contributing ±`window` seconds, until the union of
    what has been taken reaches `limit` windows' worth. Neighbouring hits
    therefore cost almost nothing — their windows overlap — and a hit in a
    part of the talk already shown costs nothing at all, so the budget is
    spent on distinct passages rather than on the same one repeatedly.
    """
    budget = limit * 2 * window
    spans: list[tuple[float, float]] = []
    for s in starts:
        if spans and covered(spans) >= budget:
            break
        spans.append((max(0.0, s - window), s + window))
    return merge(spans)


def covered(spans: list[tuple[float, float]]) -> float:
    return sum(hi - lo for lo, hi in merge(spans))


def merge(spans: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Union of overlapping windows, in time order.

    Two windows that touch are one passage, not two — printing them separately
    would repeat the speech between them and read as though the speaker said
    it twice.
    """
    out: list[list[float]] = []
    for lo, hi in sorted(spans):
        if out and lo <= out[-1][1]:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return [(lo, hi) for lo, hi in out]


def hit_starts(con, talk_n: int, parsed, limit: int) -> list[float]:
    """Where in this talk the query was said, best passage first.

    Relaxed exactly as `query.py` relaxes: a segment is ~25 words, so a
    three-word question almost never has all three in one of them, and the
    strict AND that ranks talks correctly finds nothing inside one. Without
    the fallback every multi-word query would come back empty here.
    """
    sql = ("SELECT s.start FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid "
           "WHERE segments_fts MATCH ? AND s.talk_n = ? "
           "ORDER BY bm25(segments_fts) LIMIT ?")
    for expr in (parsed.strict, parsed.relaxed):
        if not expr:
            continue
        try:
            rows = con.execute(sql, (expr, talk_n, limit)).fetchall()
        except sqlite3.OperationalError as e:
            raise SystemExit(f"bad query: {e}")
        if rows:
            return [r[0] for r in rows]
    return []


def passages(con, talk: dict, parsed, window: float, limit: int,
             opening: float) -> tuple[list[dict], int]:
    """The windows worth printing, and how many words the transcript has."""
    segs = con.execute(
        "SELECT start, text FROM segments WHERE talk_n=? ORDER BY start", (talk["n"],)
    ).fetchall()
    if not segs:
        return [], 0
    total = sum(len(t.split()) for _, t in segs)
    end = segs[-1][0] + 30

    spans: list[tuple[float, float]] = []
    if parsed:
        # Ranked by the same bm25 as query.py, restricted to this talk, so the
        # passage shown here is the passage that put the talk in the results.
        starts = hit_starts(con, talk["n"], parsed, limit * OVERSAMPLE)
        if not starts:
            # The talk is in the results on its metadata alone. The opening is
            # the honest answer — never the whole transcript, which is what a
            # query matching nothing must not silently cost.
            return [{"start": 0.0, "end": opening or 60,
                     "text": " ".join(" ".join(t for st, t in segs if st < (opening or 60)).split()),
                     "words": 0, "note": "nothing in the transcript matched"}], total
        spans = spans_for(starts, window, limit)
    if opening > 0:
        spans.append((0.0, opening))
    if not spans:
        spans = [(0.0, end)]

    out = []
    for lo, hi in merge(spans):
        text = " ".join(t for st, t in segs if lo <= st < hi)
        if text:
            out.append({"start": lo, "end": hi, "text": " ".join(text.split()),
                        "words": len(text.split())})
    return out, total


def render(talk: dict, parts: list[dict], total_words: int, full: bool) -> None:
    vid = talk["id"]
    # `&t=` only means something to YouTube; an InfoQ-only talk keeps its
    # timestamps as text rather than as links that cannot seek.
    yt = talk["youtube_url"]
    print(f"\n## {talk['title']}")
    who = talk["speakers"] or "speaker not recorded"
    edition = talk["edition"] or talk["conference_name"]
    print(f"{who} · {talk['conference_name']} · {edition}"
          + (f" · {talk['year']}" if talk["year"] else "")
          + (f" · {talk['duration_min']} min" if talk["duration_min"] else ""))
    print(talk["url"] or atu.watch_url(vid) or "")

    if talk["description"]:
        desc = " ".join(talk["description"].split())
        # InfoQ's presentation pages carry a real abstract and a speaker bio;
        # a YouTube description is whatever the channel pasted under the video.
        # Saying which one this is tells the reader how much to trust it.
        # A merged talk has both a video and an InfoQ page, and its description
        # is the InfoQ one — so the page, not the absence of a video, is what
        # says where these words came from.
        origin = ("InfoQ's summary and speaker bio" if talk["page_url"]
                  else "YouTube's, not an abstract")
        print(f"\n_Description ({origin}):_ {desc[:500]}"
              + ("…" if len(desc) > 500 else ""))

    if not talk["has_transcript"]:
        print("\n**No transcript.** Title and description are all this talk has — "
              "enough to recommend it, not enough to quote it.")
        return

    shown = sum(p["words"] for p in parts)
    for p in parts:
        ts = query.fmt_ts(p["start"])
        stamp = f"[{ts}]({yt}&t={int(p['start'])}s)" if yt else ts
        print(f"\n**{stamp}** {p['text']}")
    if not full and shown < total_words:
        pct = round(100 * shown / total_words) if total_words else 0
        print(f"\n_{shown} of {total_words} words ({pct}%). "
              f"For the rest: excerpt.py {vid} --full, or another -q._")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Print the parts of a talk that answer a question, not the whole talk.")
    ap.add_argument("ids", nargs="*", metavar="ID",
                    help="video id, YouTube URL, or talks/<conf>/<id>-<slug>.md")
    ap.add_argument("-q", "--query", default="",
                    help="what to excerpt around; FTS5 syntax works, as in query.py")
    ap.add_argument("-n", "--passages", type=query.positive_int, default=PASSAGES,
                    help=f"how many passages to keep (default {PASSAGES})")
    ap.add_argument("--window", type=float, default=WINDOW,
                    help=f"seconds of speech either side of a hit (default {WINDOW})")
    ap.add_argument("--opening", type=float, default=OPENING,
                    help=f"seconds of the start to always include (default {OPENING}; 0 for none)")
    ap.add_argument("--full", action="store_true", help="the whole transcript")
    ap.add_argument("--json", action="store_true")
    argv, hyphenated = split_ids(sys.argv[1:])
    args = ap.parse_args(argv)
    args.ids += hyphenated
    if not args.ids:
        ap.error("at least one video id is required")

    con = atu.connect()
    out, missing = [], []
    for ident in args.ids:
        talk = find_talk(con, ident)
        if not talk:
            missing.append(ident)
            continue
        parsed = query.parse_query(args.query) if args.query and not args.full else None
        parts, total = ([], 0)
        if talk["has_transcript"]:
            parts, total = passages(con, talk, parsed, args.window, args.passages,
                                    0 if args.full else args.opening)
            if parts and parts[0].get("note"):
                print(f"note: nothing in {talk['id']}'s transcript matches "
                      f"{args.query!r} — showing the opening", file=sys.stderr)
                parts[0]["words"] = len(parts[0]["text"].split())
        out.append((talk, parts, total))

    if args.json:
        json.dump([{**{k: t[k] for k in COLS if k != "n"},
                    "speakers": [s for s in (t["speakers"] or "").split(", ") if s],
                    "excerpt_words": sum(p["words"] for p in parts),
                    "passages": parts}
                   for t, parts, total in out], sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        for talk, parts, total in out:
            render(talk, parts, total, args.full)
    for ident in missing:
        die(f"not in the corpus: {ident}")
    return 1 if missing and not out else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(query.EXIT_SIGINT)
    except BrokenPipeError:
        sys.exit(query.EXIT_SIGPIPE)
