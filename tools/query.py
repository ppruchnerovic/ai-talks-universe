#!/usr/bin/env python3
"""Search the AI talk knowledge base from the command line.

Two layers are searched and merged:
  * talk metadata + YouTube descriptions (always available)
  * transcript passages (only for talks whose transcript has been fetched),
    which also gives the timestamp — and a deep link — for each hit.

    python3 query.py "context engineering"
    python3 query.py "prompt injection" --category "AI security"
    python3 query.py "agents in production" --conference langchain-interrupt
    python3 query.py "evals" --year 2026 -n 20
    python3 query.py "mcp" --json          # for scripts and agents

FTS5 syntax works: quoted "exact phrase", OR, NOT, prefix*.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys

import atu

# The two layers are blended after each is normalised to [0, 1] across the
# result set, not by adding their raw bm25 values together.
#
# That is not a refinement, it is a correctness fix. `bm25()` is only
# comparable within one table, and a passage is a ~25-word document: almost any
# match in one scores near the maximum, so a raw passage score (~8) lands on top
# of the best possible title score (~9) and then accumulates over four moments.
# Blended raw, every query returned the same handful of long workshops — the
# talks that happen to have been transcribed — however well another talk's
# title answered it. Normalising first makes the weights below mean what they
# say: a talk's own metadata leads, and what was said on stage is strong
# corroborating evidence rather than an override.
W_META = 1.0
W_SEG = 0.7


def fts_query(raw: str) -> str:
    """Pass FTS5 operators through, otherwise AND the bare words together."""
    if re.search(r'["*]|\b(OR|NOT|AND|NEAR)\b', raw):
        return raw
    words = [w for w in re.findall(r"[\w'+#.-]+", raw) if w]
    if not words:
        raise SystemExit("empty query")
    return " AND ".join(f'"{w}"' for w in words)


def search(con, q: str, limit: int, filters: dict) -> list[dict]:
    where, params = [], {"q": q}
    for col, val in filters.items():
        if val:
            where.append(f"t.{col} = :{col}")
            params[col] = val
    clause = (" AND " + " AND ".join(where)) if where else ""

    hits: dict[int, dict] = {}

    meta_sql = f"""
        SELECT t.n, bm25(talks_fts, 8.0, 2.0, 4.0, 4.0, 1.5) AS rank,
               snippet(talks_fts, 1, '[[', ']]', ' … ', 24) AS snip
        FROM talks_fts JOIN talks t ON t.n = talks_fts.rowid
        WHERE talks_fts MATCH :q{clause}
        ORDER BY rank LIMIT 600
    """
    try:
        rows = con.execute(meta_sql, params).fetchall()
    except sqlite3.OperationalError as e:
        raise SystemExit(f"bad query: {e}")
    for n, rank, snip in rows:
        hits[n] = {"n": n, "meta": -rank, "seg": 0.0,
                   "description_snippet": snip, "moments": []}

    seg_sql = f"""
        SELECT s.talk_n, s.start, bm25(segments_fts) AS rank,
               snippet(segments_fts, 0, '[[', ']]', ' … ', 26) AS snip
        FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid
        JOIN talks t ON t.n = s.talk_n
        WHERE segments_fts MATCH :q{clause}
        ORDER BY rank LIMIT 2000
    """
    try:
        seg_rows = con.execute(seg_sql, params).fetchall()
    except sqlite3.OperationalError:
        seg_rows = []

    for n, start, rank, snip in seg_rows:
        h = hits.setdefault(n, {"n": n, "meta": 0.0, "seg": 0.0,
                                "description_snippet": "", "moments": []})
        if len(h["moments"]) < 4:
            h["moments"].append({"start": start, "text": snip})
            # Diminishing returns: the second and third time a phrase is spoken
            # says less than the first, and a long talk should not win on volume.
            h["seg"] += -rank / (len(h["moments"]) ** 0.5)

    top_meta = max((h["meta"] for h in hits.values()), default=0.0) or 1.0
    top_seg = max((h["seg"] for h in hits.values()), default=0.0) or 1.0
    for h in hits.values():
        h["score"] = round(W_META * h["meta"] / top_meta + W_SEG * h["seg"] / top_seg, 4)

    ranked = sorted(hits.values(), key=lambda h: -h["score"])[:limit]

    cols = ("id title speakers conference conference_name category edition year channel tags "
            "duration_min published_at youtube_url has_transcript").split()
    for h in ranked:
        row = con.execute(f"SELECT {','.join(cols)} FROM talks WHERE n=?", (h["n"],)).fetchone()
        h.update(dict(zip(cols, row)))
    return ranked


def fmt_ts(sec: float) -> str:
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def clean_snip(s: str) -> str:
    return " ".join((s or "").split()).replace("[[", "\033[33m").replace("]]", "\033[0m")


def render(hits: list[dict], show_moments: bool) -> None:
    if not hits:
        print("no matches")
        return
    for i, h in enumerate(hits, 1):
        print(f"\n\033[1m{i}. {h['title']}\033[0m")
        print(f"   {h['speakers'] or '—'}")
        edition = h["edition"] or h["conference_name"]
        print(f"   {h['conference_name']} · {edition}"
              + (f" · {h['year']}" if h["year"] else "")
              + (f" · {h['duration_min']}min" if h["duration_min"] else "")
              + ("  · transcript" if h["has_transcript"] else ""))
        if h["description_snippet"]:
            print(f"   \033[2m{clean_snip(h['description_snippet'])}\033[0m")
        if show_moments and h["moments"]:
            for m in h["moments"]:
                print(f"   \033[36m{fmt_ts(m['start'])}\033[0m {clean_snip(m['text'])}")
                print(f"        {h['youtube_url']}&t={int(m['start'])}s")
        print(f"   {h['youtube_url']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", "--limit", type=int, default=10)
    ap.add_argument("--conference", help="conference slug, e.g. ai-engineer")
    ap.add_argument("--category", help='e.g. "AI security"')
    ap.add_argument("--year", type=int)
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not atu.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()

    con = sqlite3.connect(f"file:{atu.TALKS_DB}?mode=ro", uri=True)
    q = fts_query(" ".join(args.query))
    hits = search(con, q, args.limit, {
        "conference": args.conference, "category": args.category, "year": args.year,
    })

    if args.json:
        for h in hits:
            for k in ("n", "meta", "seg"):
                h.pop(k, None)
            h["tags"] = [x for x in (h["tags"] or "").split(", ") if x]
            h["speakers"] = [x for x in (h["speakers"] or "").split(", ") if x]
            h["description_snippet"] = " ".join((h["description_snippet"] or "").split())
        json.dump(hits, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        render(hits, args.moments)


if __name__ == "__main__":
    main()
