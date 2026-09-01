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
    python3 query.py "mcp" --json --brief  # the same, at a third of the bytes
    python3 query.py --list-conferences    # what --conference accepts
    python3 query.py --list-categories     # what --category accepts

FTS5 syntax works: quoted "exact phrase", OR, NOT, prefix*. A query written in
that syntax is run exactly as typed. A bare multi-word query is ANDed first and,
only if that matches nothing, retried as an OR of its content words — which is
what makes a natural-language question answerable.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sqlite3
import sys
from typing import NamedTuple

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

# Transcript moments kept per talk. This is now a property of the *talk*, not of
# where the talk happened to fall in a global list: both candidate pools are
# gathered whole, and the segment pool takes each talk's own best MOMENTS
# passages with a window function. A capped pool made the normalisation below
# depend on the cap — a talk near the cut got one moment scored where a talk
# above it got four — so the [0, 1] scaling was over a truncated set. Now every
# talk in the pool is scored on the same basis and the maxima are the real ones.
MOMENTS = 4

# A pasted blob is a real query shape, and FTS5 evaluates every repeated term
# again: `agent` ×400 took over two minutes. Terms are de-duplicated (AND and OR
# are idempotent, so that cannot change a result) and then capped.
MAX_TERMS = 32

# What snippet()/highlight() wrap a match in while we work. Two control
# characters no description can contain, which is what makes "did this column
# actually match?" a reliable test — the `[[`/`]]` of the output could occur in
# the text itself. Swapped for the display markers on the way out.
M0, M1 = "\x02", "\x03"

# The metadata columns of talks_fts, in the order they are indexed, and the
# layer name each one is reported under.
FTS_COLUMNS = ("title", "description", "tags", "speakers", "conference_name")
LAYERS = ("title", "description", "tags", "speakers", "conference")

# 128 + SIGPIPE and 128 + SIGINT, which is what a shell reports for a process
# killed by either signal — the closest thing to a right answer for `| head`.
EXIT_SIGPIPE = 141
EXIT_SIGINT = 130


def warn(msg: str) -> None:
    """Everything advisory goes to stderr, so --json stays machine-readable."""
    print(msg, file=sys.stderr)


# ── the query ────────────────────────────────────────────────────────────────

OPERATORS = {"AND", "OR", "NOT", "NEAR"}
EXPLICIT_RE = re.compile(r'["*]|\b(?:OR|NOT|AND|NEAR)\b')
WORD_RE = re.compile(r"[\w'+#.-]+")
# A quoted phrase (optionally prefixed), a parenthesis or comma of NEAR(), or a
# bare term — which covers `agent*`, `gpt-4`, `c#` and the operators alike.
SCAN_RE = re.compile(r'"[^"]*"\*?|[()]|,|[^\s()",]+')


class Parsed(NamedTuple):
    strict: str
    relaxed: str | None
    relaxed_terms: tuple[str, ...]


def dedupe(items: list[str], key=None) -> list[str]:
    key = key or (lambda s: s.lower())
    seen, out = set(), []
    for it in items:
        k = key(it)
        if k not in seen:
            seen.add(k)
            out.append(it)
    return out


def cap(terms: list[str]) -> list[str]:
    if len(terms) > MAX_TERMS:
        warn(f"query has {len(terms)} terms — searching the first {MAX_TERMS}")
        return terms[:MAX_TERMS]
    return terms


def explicit_query(raw: str) -> str:
    """De-duplicate and cap only where that provably cannot change the result.

    A flat chain joined by one operator is safe: AND and OR are idempotent, so
    dropping a repeat is a no-op and truncating leaves a valid expression.
    Anything with parentheses, NEAR, NOT or a mix of operators — where dropping
    a term would change what the query asks — is passed through as typed.
    """
    if raw.count('"') % 2:  # unbalanced: let FTS5 report its own error
        return raw
    items = SCAN_RE.findall(raw)
    if any(it in ("(", ")", ",", "NEAR") for it in items):
        return raw
    ops = {it for it in items if it in OPERATORS}
    if len(ops) > 1 or ops - {"AND", "OR"}:
        return raw
    terms = [it for it in items if it not in OPERATORS]
    if not terms:
        raise SystemExit("empty query")
    joiner = f" {ops.pop()} " if ops else " "
    return joiner.join(cap(dedupe(terms, key=lambda t: " ".join(t.lower().split()))))


def parse_query(raw: str) -> Parsed:
    """Turn what was typed into the strict query, and the relaxation to try.

    Explicit FTS5 syntax is never relaxed: it says what it wants. A bare query
    gets the documented AND, plus an OR of its content words to fall back on —
    still ranked, so a talk matching more of them, and matching them close
    together, still wins.
    """
    if EXPLICIT_RE.search(raw):
        return Parsed(explicit_query(raw), None, ())
    words = cap(dedupe(WORD_RE.findall(raw)))
    if not words:
        raise SystemExit("empty query")
    strict = " AND ".join(f'"{w}"' for w in words)
    if len(words) == 1:
        return Parsed(strict, None, ())
    content = [w for w in words if w.lower() not in atu.STOPWORDS] or words
    return Parsed(strict, " OR ".join(f'"{w}"' for w in content), tuple(content))


# ── the search ───────────────────────────────────────────────────────────────


def search(con, q: str, limit: int, filters: dict) -> list[dict]:
    where, params = [], {"q": q}
    for col, val in filters.items():
        if val is not None and val != "":
            where.append(f"t.{col} = :{col}")
            params[col] = val
    clause = (" AND " + " AND ".join(where)) if where else ""

    hits: dict[int, dict] = {}

    # No LIMIT on either pool: the metadata layer is at most one row per talk,
    # and the segment layer is capped per talk rather than globally, so both are
    # cheap to take whole — and taking them whole is what keeps the [0, 1]
    # normalisation below from scaling against a truncated set.
    meta_sql = f"""
        SELECT t.n, bm25(talks_fts, 8.0, 2.0, 4.0, 4.0, 1.5) AS rank
        FROM talks_fts JOIN talks t ON t.n = talks_fts.rowid
        WHERE talks_fts MATCH :q{clause}
    """
    try:
        rows = con.execute(meta_sql, params).fetchall()
    except sqlite3.OperationalError as e:
        raise SystemExit(f"bad query: {e}")
    for n, rank in rows:
        hits[n] = {"n": n, "meta": -rank, "seg": 0.0, "moments": []}

    seg_join = "JOIN talks t ON t.n = s.talk_n" if where else ""
    seg_sql = f"""
        SELECT n, seg, start, rank FROM (
            SELECT n, seg, start, rank,
                   ROW_NUMBER() OVER (PARTITION BY n ORDER BY rank) AS rn
            FROM (
                SELECT s.talk_n AS n, s.rowid AS seg, s.start AS start,
                       bm25(segments_fts) AS rank
                FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid
                {seg_join}
                WHERE segments_fts MATCH :q{clause}
            )
        ) WHERE rn <= {MOMENTS} ORDER BY rank
    """
    try:
        seg_rows = con.execute(seg_sql, params).fetchall()
    except sqlite3.OperationalError:
        seg_rows = []

    for n, seg, start, rank in seg_rows:
        h = hits.setdefault(n, {"n": n, "meta": 0.0, "seg": 0.0, "moments": []})
        h["moments"].append({"start": start, "text": "", "seg": seg})
        # Diminishing returns: the second and third time a phrase is spoken
        # says less than the first, and a long talk should not win on volume.
        h["seg"] += -rank / (len(h["moments"]) ** 0.5)

    top_meta = max((h["meta"] for h in hits.values()), default=0.0) or 1.0
    top_seg = max((h["seg"] for h in hits.values()), default=0.0) or 1.0
    for h in hits.values():
        h["score"] = round(W_META * h["meta"] / top_meta + W_SEG * h["seg"] / top_seg, 4)

    ranked = sorted(hits.values(), key=lambda h: -h["score"])[:limit]
    add_details(con, q, ranked)
    return ranked


def chunks(seq: list, size: int = 400):
    """`rowid IN (…)` one bind variable at a time, within any SQLite's limit."""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def add_details(con, q: str, ranked: list[dict]) -> None:
    """Fill in the columns, the snippets and which layer each snippet came from.

    Snippets are cut here rather than in the pool queries, so they cost one
    small lookup per shown result instead of one per candidate — and so every
    indexed column can be asked, which is what tells us what actually matched.
    """
    cols = ("id title speakers conference conference_name category edition year channel tags "
            "duration_min published_at youtube_url has_transcript").split()
    for h in ranked:
        row = con.execute(f"SELECT {','.join(cols)} FROM talks WHERE n=?", (h["n"],)).fetchone()
        h.update(dict(zip(cols, row)))
    if not ranked:
        return

    # highlight() for the short columns — a title must come back whole, not cut
    # to 24 tokens — and snippet() for the description, which is an essay.
    exprs = ", ".join(f"snippet(talks_fts, {i}, ?, ?, ' … ', 24)" if col == "description"
                      else f"highlight(talks_fts, {i}, ?, ?)"
                      for i, col in enumerate(FTS_COLUMNS))
    meta_snips = {}
    for ids in chunks([h["n"] for h in ranked]):
        sql = (f"SELECT rowid, {exprs} FROM talks_fts WHERE talks_fts MATCH ? "
               f"AND rowid IN ({','.join('?' * len(ids))})")
        meta_snips.update({r[0]: r[1:]
                           for r in con.execute(sql, [M0, M1] * len(FTS_COLUMNS) + [q] + ids)})

    seg_snips = {}
    for segs in chunks([m["seg"] for h in ranked for m in h["moments"]]):
        sql = (f"SELECT rowid, snippet(segments_fts, 0, ?, ?, ' … ', 26) FROM segments_fts "
               f"WHERE segments_fts MATCH ? AND rowid IN ({','.join('?' * len(segs))})")
        seg_snips.update(con.execute(sql, [M0, M1, q] + segs).fetchall())

    for h in ranked:
        snips = meta_snips.get(h["n"], ())
        # Which columns carry a mark is which columns matched, in index order —
        # so the title wins over the description, and the snippet shown is the
        # one the reader is being told about.
        cols = [i for i, s in enumerate(snips) if M0 in (s or "")]
        matched = [LAYERS[i] for i in cols]
        h["description_snippet"] = snips[1] if len(snips) > 1 else ""
        h["snippet"] = snips[cols[0] if cols else 1] if snips else ""
        h["snippet_from"] = LAYERS[cols[0]] if cols else ("description" if h["snippet"] else "")
        for m in h["moments"]:
            m["text"] = seg_snips.get(m.pop("seg"), "")
        if h["moments"]:
            matched.append("transcript")
            if not h["snippet"]:
                # Nothing in the metadata matched: the talk is here because of
                # what was said, so show that rather than a blank line.
                h["snippet"] = h["moments"][0]["text"]
                h["snippet_from"] = "transcript"
        h["matched"] = matched


# ── the filters ──────────────────────────────────────────────────────────────


def norm(s) -> str:
    """Fold a slug, a name and whatever the user typed onto one key."""
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def facet(con, col: str) -> list[tuple]:
    """(value, label, count) for every value of a filterable column."""
    label = "max(conference_name)" if col == "conference" else col
    return con.execute(
        f"SELECT {col}, {label}, count(*) FROM talks "
        f"WHERE {col} IS NOT NULL AND {col} <> '' GROUP BY {col} ORDER BY 1"
    ).fetchall()


def print_facet(con, col: str) -> None:
    rows = facet(con, col)
    w = max((len(str(v)) for v, _, _ in rows), default=0)
    for value, label, count in rows:
        line = f"{str(value):<{w}}  {count:>5}"
        if str(label) != str(value):
            line += f"  {label}"
        print(line)


def resolve(con, col: str, value, listing: str | None):
    """Match a filter value case- and separator-insensitively, or say what would.

    A filter that matches nothing is a typo far more often than it is a real
    empty result, and "no matches" cannot tell those apart — so this fails with
    the values that do exist instead of returning an empty search.
    """
    if value is None:
        return None
    rows = facet(con, col)
    index: dict[str, object] = {}
    for v, label, _ in rows:
        index.setdefault(norm(v), v)
        index.setdefault(norm(label), v)
    want = norm(value)
    if want in index:
        return index[want]

    lines = [f"--{col.replace('_', '-')} {value!r} matches nothing"]
    close = difflib.get_close_matches(want, list(index), n=3, cutoff=0.55)
    if close:
        lines.append("did you mean: " + ", ".join(dict.fromkeys(str(index[c]) for c in close)))
    elif len(rows) <= 20:
        lines.append("valid values: " + ", ".join(str(v) for v, _, _ in rows))
    if listing:
        lines.append(f"all {len(rows)} of them: query.py {listing}")
    raise SystemExit("\n".join(lines))


# ── output ───────────────────────────────────────────────────────────────────


BOLD, DIM, YELLOW, CYAN, OFF = (
    "\033[1m", "\033[2m", "\033[33m", "\033[36m", "\033[0m")


def fmt_ts(sec: float) -> str:
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def clean_snip(s: str, base: str = "") -> str:
    """Colour the matches, and restore whatever styling encloses them."""
    return " ".join((s or "").split()).replace(M0, YELLOW).replace(M1, OFF + base)


def for_json(s: str) -> str:
    return " ".join((s or "").split()).replace(M0, "[[").replace(M1, "]]")


def render(hits: list[dict], show_moments: bool) -> None:
    if not hits:
        print("no matches")
        return
    for i, h in enumerate(hits, 1):
        # A title that matched is highlighted in place — printing the title
        # snippet underneath it as well would just say the same thing twice.
        title = clean_snip(h["snippet"], BOLD) if h["snippet_from"] == "title" else h["title"]
        print(f"\n{BOLD}{i}. {title}{OFF}")
        print(f"   {h['speakers'] or '—'}")
        edition = h["edition"] or h["conference_name"]
        print(f"   {h['conference_name']} · {edition}"
              + (f" · {h['year']}" if h["year"] else "")
              + (f" · {h['duration_min']}min" if h["duration_min"] else "")
              + ("  · transcript" if h["has_transcript"] else "")
              + (f"  {DIM}· match: {', '.join(h['matched'])}{OFF}" if h["matched"] else ""))
        label, body = h["snippet_from"], h["snippet"]
        if label == "title":  # already shown; fall back to the description
            body = h["description_snippet"]
            label = "description" if M0 in body else ""
        if body:
            print(f"   {DIM}{f'[{label}] ' if label else ''}{clean_snip(body, DIM)}{OFF}")
        if show_moments and h["moments"]:
            for m in h["moments"]:
                print(f"   {CYAN}{fmt_ts(m['start'])}{OFF} {clean_snip(m['text'])}")
                print(f"        {h['youtube_url']}&t={int(m['start'])}s")
        print(f"   {h['youtube_url']}")


# What --brief keeps. The rest of the record is one lookup away by id, and a
# reader that is deciding *which* talks to open does not need the channel, the
# tags, the publication timestamp or a second snippet of the same description
# — on a 12-hit result set those fields are most of the bytes and none of the
# decision.
BRIEF = ("id title speakers conference year duration_min youtube_url "
         "has_transcript score snippet snippet_from matched").split()

# Moments shown per hit under --brief. One passage says whether the talk is
# about the query; the fourth says it again.
BRIEF_MOMENTS = 2


def emit_json(hits: list[dict], brief: bool = False) -> None:
    for h in hits:
        for k in ("n", "meta", "seg"):
            h.pop(k, None)
        h["tags"] = [x for x in (h["tags"] or "").split(", ") if x]
        h["speakers"] = [x for x in (h["speakers"] or "").split(", ") if x]
        for k in ("snippet", "description_snippet"):
            h[k] = for_json(h[k])
        for m in h["moments"]:
            m["text"] = for_json(m["text"])
    if brief:
        hits = [{**{k: h[k] for k in BRIEF if k in h},
                 "moments": [{"start": m["start"], "text": m["text"]}
                             for m in h["moments"][:BRIEF_MOMENTS]]}
                for h in hits]
    json.dump(hits, sys.stdout, ensure_ascii=False, indent=None if brief else 2)
    print()


# ── the CLI ──────────────────────────────────────────────────────────────────


def positive_int(s: str) -> int:
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{s!r} is not a whole number")
    if v < 1:
        raise argparse.ArgumentTypeError(f"must be 1 or more, not {v}")
    return v


def year_int(s: str) -> int:
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{s!r} is not a year")
    if not 1900 <= v <= 2100:
        raise argparse.ArgumentTypeError(f"must be a four-digit year, not {v}")
    return v


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Ranked search over the AI conference talk knowledge base.")
    ap.add_argument("query", nargs="*", help='what to search for; FTS5 syntax works')
    ap.add_argument("-n", "--limit", type=positive_int, default=10,
                    help="how many results to show (default 10)")
    ap.add_argument("--conference", help="conference slug or name, e.g. ai-engineer")
    ap.add_argument("--category", help='e.g. "AI security"')
    ap.add_argument("--year", type=year_int)
    ap.add_argument("--list-conferences", action="store_true",
                    help="print the conferences --conference accepts, and exit")
    ap.add_argument("--list-categories", action="store_true",
                    help="print the categories --category accepts, and exit")
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--brief", action="store_true",
                    help="the fields and passages needed to choose a talk, and no more")
    ap.add_argument("--ids", action="store_true",
                    help="print only the video ids, one per line — feeds excerpt.py")
    args = ap.parse_args()

    if not atu.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()

    con = sqlite3.connect(f"file:{atu.TALKS_DB}?mode=ro", uri=True)

    if args.list_conferences or args.list_categories:
        print_facet(con, "conference" if args.list_conferences else "category")
        return
    if not args.query:
        ap.error("a query is required "
                 "(or --list-conferences / --list-categories to see the filters)")

    filters = {
        "conference": resolve(con, "conference", args.conference, "--list-conferences"),
        "category": resolve(con, "category", args.category, "--list-categories"),
        "year": resolve(con, "year", args.year, None),
    }
    parsed = parse_query(" ".join(args.query))
    hits = search(con, parsed.strict, args.limit, filters)
    if not hits and parsed.relaxed:
        warn("nothing matches every term — relaxed to any of: "
             + ", ".join(parsed.relaxed_terms))
        hits = search(con, parsed.relaxed, args.limit, filters)

    if args.ids:
        # So that reading the hits is a pipe rather than eight ids retyped:
        #   query.py "…" --ids | xargs python3 excerpt.py -q "…"
        for h in hits:
            print(h["id"])
    elif args.json:
        emit_json(hits, args.brief)
    else:
        render(hits, args.moments and not args.brief)


def run() -> int:
    try:
        main()
        if sys.stdout is not None:  # None when the shell handed us a closed fd
            sys.stdout.flush()
    except BrokenPipeError:
        # `| head`, or quitting `less` early. Point what is left of stdout at
        # /dev/null before returning: the interpreter flushes it again on the
        # way out, and that second failure is uncatchable — it prints
        # "Exception ignored in: <_io.TextIOWrapper …>" after main has returned.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        return EXIT_SIGPIPE
    except KeyboardInterrupt:
        return EXIT_SIGINT
    return 0


if __name__ == "__main__":
    sys.exit(run())
