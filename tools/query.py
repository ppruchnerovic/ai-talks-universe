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
that syntax is run exactly as typed. A bare query is read as its content words
— "how do you evaluate agents in production" is `evaluate agents production` —
and a talk is a hit when every one of those words appears somewhere in it, in
its metadata or in what was said. When no talk has all of them, the commonest
word is dropped and the search retried, one word at a time, and stderr says
which words were dropped. That is what makes a natural-language question
answerable without letting its filler words rank the answer.
"""

from __future__ import annotations

import argparse
import difflib
import json
import math
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

# Passages overlap at a half-passage stride (build_index.PASSAGE_STRIDE), so a
# phrase straddling a boundary still shares one passage. The cost is that the
# best moment of a talk usually has a twin covering the same seconds; the
# window function takes a few extra and the overlapping ones are dropped here.
MOMENT_CANDIDATES = MOMENTS * 3

# The segment layer is scored on the OR of the query's words, and a talk that
# says them *together* — inside one passage — is promoted over one that merely
# says each of them somewhere. Same constants as index.html's passageFactor,
# so the two rankers agree on this by construction rather than by test.
PASSAGE_W = 1.6
SATURATE = math.log(4)

# Words that describe the question rather than the topic. atu.STOPWORDS holds
# the grammatical ones ("how", "do", "you", "in"); these are the ones a
# question about a corpus of talks adds — "what do people say about agent
# reliability" is a query about agent reliability. Applied to queries only, so
# the index and the browser are unchanged and a talk titled "People" is still
# findable by an explicit search for it.
QUERY_STOPWORDS = set("""
people say says said saying talk talks talked talking speak speaks spoke spoken think thinks
thought thoughts discuss discusses discussed discussion discussions mention mentions mentioned
cover covers covered speaker speakers presenter presenters presentation presentations session
sessions conference conferences someone anyone somebody anybody something anything everything
everyone opinion opinions view views position positions argue argues argued claim claims
""".split())

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

# Two passages closer than this, in words, cover the same speech — the
# overlap build_index.PASSAGE_STRIDE creates on purpose.
PASSAGE_SPAN = 25

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


def is_stop(word: str) -> bool:
    w = word.lower()
    return w in atu.STOPWORDS or w in QUERY_STOPWORDS


def quoted(word: str) -> str:
    return '"' + word.replace('"', '""') + '"'


class Parsed(NamedTuple):
    """What was typed, as FTS5 will see it.

    `strict` is the expression run as typed for explicit syntax, and the AND
    of the content words for a bare query. `terms` are those content words —
    empty for explicit syntax, which is never relaxed because it says what it
    wants. `relaxed` is their OR, which excerpt.py falls back to inside one
    talk, where a ~25-word passage rarely holds all of a question's words.
    """
    strict: str
    terms: tuple[str, ...]

    @property
    def relaxed(self) -> str | None:
        return " OR ".join(quoted(t) for t in self.terms) if len(self.terms) > 1 else None


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


# What FTS5 accepts unquoted: letters, digits, underscore and anything
# non-ASCII. Everything else in a bare term — the hyphen in `gpt-4`, the plus
# in `c++`, the apostrophe in `don't` — is read as syntax, and the error it
# produces ("no such column: 4") names a column nobody typed.
BAREWORD_RE = re.compile(r"^[\w\u0080-\U0010ffff]+\*?$")


def quote_term(term: str) -> str:
    """A bare term made safe for FTS5, with a trailing `*` kept outside.

    `gpt-4*` becomes `"gpt-4"*`, which is the same prefix query written the way
    FTS5 can parse it; a single token in quotes means what the bare token
    means, so this never changes what a query asks — only whether it runs.
    """
    if term.startswith('"') or term in OPERATORS or term in ("(", ")", ",") \
            or BAREWORD_RE.match(term):
        return term
    prefix = term.endswith("*")
    body = term[:-1] if prefix else term
    return '"' + body.replace('"', '""') + '"' + ("*" if prefix else "")


def explicit_query(raw: str) -> str:
    """Make a typed FTS5 query runnable; de-duplicate and cap where that is safe.

    Every bare term that FTS5 would misread is quoted — see quote_term() — and
    a stray comma, which is syntax only inside NEAR(), is dropped. Both are
    meaning-preserving, so they apply to every query.

    De-duplication and the cap apply only to a flat chain joined by one
    operator: AND and OR are idempotent, so dropping a repeat is a no-op and
    truncating leaves a valid expression. Anything with parentheses, NEAR, NOT
    or a mix of operators — where dropping a term would change what the query
    asks — is passed through with its terms quoted and nothing else touched.
    """
    if raw.count('"') % 2:  # unbalanced: let FTS5 report its own error
        return raw
    items = [quote_term(it) for it in SCAN_RE.findall(raw)]
    if "NEAR" not in items:
        items = [it for it in items if it != ","]
    if any(it in ("(", ")", ",", "NEAR") for it in items):
        return " ".join(items)
    ops = {it for it in items if it in OPERATORS}
    if len(ops) > 1 or ops - {"AND", "OR"}:
        return " ".join(items)
    terms = [it for it in items if it not in OPERATORS]
    if not terms:
        raise SystemExit("empty query")
    joiner = f" {ops.pop()} " if ops else " "
    return joiner.join(cap(dedupe(terms, key=lambda t: " ".join(t.lower().split()))))


def parse_query(raw: str) -> Parsed:
    """Turn what was typed into the words to search for.

    Explicit FTS5 syntax is run as typed. A bare query is reduced to its
    content words — the stopwords are dropped *before* the strict form is
    built, not only from the relaxed one, because "how do you evaluate agents
    in production" ANDed whole matched four metadata-only talks on "how",
    "do", "you" and "in" and never reached the transcripts, where seven words
    never share a 25-word passage. Only when every word is a stopword are
    they all kept, so a search for "the thing" still searches for something.
    """
    if EXPLICIT_RE.search(raw):
        return Parsed(explicit_query(raw), ())
    words = cap(dedupe(WORD_RE.findall(raw)))
    if not words:
        raise SystemExit("empty query")
    content = [w for w in words if not is_stop(w)] or words
    return Parsed(" AND ".join(quoted(w) for w in content), tuple(content))


# ── the search ───────────────────────────────────────────────────────────────


class Filters(NamedTuple):
    """The WHERE fragment for the talks table, aliased `t`, and its binds."""
    clause: str
    params: dict


def build_filters(conference=None, category=None, year=None, min_year=None,
                  transcript=False) -> Filters:
    where, params = [], {}
    for col, vals in (("conference", conference), ("category", category), ("year", year)):
        vals = [v for v in (vals or []) if v is not None and v != ""]
        if vals:
            keys = [f"{col}{i}" for i in range(len(vals))]
            where.append(f"t.{col} IN ({', '.join(':' + k for k in keys)})")
            params.update(zip(keys, vals))
    if min_year:
        where.append("t.year >= :min_year")
        params["min_year"] = min_year
    if transcript:
        where.append("t.has_transcript = 1")
    return Filters((" AND " + " AND ".join(where)) if where else "", params)


def talks_saying(con, term: str) -> set[int]:
    """Every talk in which this word appears — in its metadata or on stage.

    This is the gate index.html applies ("every query term must appear
    somewhere"), and it is what lets both layers be scored on the OR of the
    words without a common word pulling in the whole corpus: the OR ranks,
    the gate decides who is ranked. Two lookups a word, under 30 ms each on
    the commonest words in the corpus.
    """
    q = quoted(term)
    ids = {r[0] for r in con.execute("SELECT rowid FROM talks_fts WHERE talks_fts MATCH ?", (q,))}
    ids |= {r[0] for r in con.execute(
        "SELECT DISTINCT talk_n FROM segments WHERE rowid IN "
        "(SELECT rowid FROM segments_fts WHERE segments_fts MATCH ?)", (q,))}
    return ids


class Result(NamedTuple):
    hits: list[dict]
    dropped: tuple[str, ...]      # words relaxed away, commonest first


def search(con, parsed: Parsed, limit: int, filters: Filters) -> Result:
    """Rank the talks that answer the query, relaxing it one word at a time.

    Explicit FTS5 syntax is run as typed on both layers: it says what it
    wants and is never relaxed. A bare query is its content words, and a talk
    qualifies when every word appears somewhere in it. When no talk has all
    of them, the word present in the most talks is dropped and the gate
    re-applied — a single wrong word in a question then costs that word, not
    the whole question, and the OR-of-everything cliff that once ranked "Your
    People Are The Future Of Your Brand" first for "what do people say about
    agent reliability" is gone. What was dropped is returned, to be said.
    """
    if not parsed.terms:
        return Result(rank(con, parsed.strict, None, None, limit, filters), ())

    present = {t: talks_saying(con, t) for t in parsed.terms}
    if filters.clause:
        allowed = {r[0] for r in con.execute(f"SELECT t.n FROM talks t WHERE 1=1{filters.clause}",
                                             filters.params)}
        present = {t: ids & allowed for t, ids in present.items()}
    kept, dropped = list(parsed.terms), []
    pool = set.intersection(*(present[t] for t in kept))
    while not pool and len(kept) > 1:
        # A word no talk says at all — a typo, usually — cannot narrow anything
        # and only empties the gate, so it goes first. After that the word
        # present in the most talks goes, since it is the likeliest to be the
        # question's furniture rather than its subject.
        absent = [t for t in kept if not present[t]]
        drop = absent[0] if absent else max(kept, key=lambda t: len(present[t]))
        kept.remove(drop)
        dropped.append(drop)
        pool = set.intersection(*(present[t] for t in kept))
    if not pool:
        return Result([], tuple(dropped))
    expr = " OR ".join(quoted(t) for t in kept)
    together = " AND ".join(quoted(t) for t in kept) if len(kept) > 1 else None
    return Result(rank(con, expr, together, pool, limit, filters), tuple(dropped))


def rank(con, q: str, together_q: str | None, pool: set[int] | None, limit: int,
         filters: Filters) -> list[dict]:
    """Score both layers on `q`, blend, and return the top `limit` with details.

    `pool`, when given, is the set of talks the gate admitted; rows outside it
    are discarded. `together_q` is the AND of the words, counted per talk over
    the passages, which is what promotes a talk that says them in one breath.
    """
    params = {"q": q, **filters.params}
    clause = filters.clause
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
    for n, r in rows:
        if pool is None or n in pool:
            hits[n] = {"n": n, "meta": -r, "seg": 0.0, "moments": []}

    seg_join = "JOIN talks t ON t.n = s.talk_n" if clause else ""
    seg_sql = f"""
        SELECT n, seg, start, pos, rank FROM (
            SELECT n, seg, start, pos, rank,
                   ROW_NUMBER() OVER (PARTITION BY n ORDER BY rank) AS rn
            FROM (
                SELECT s.talk_n AS n, s.rowid AS seg, s.start AS start, s.pos AS pos,
                       bm25(segments_fts) AS rank
                FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid
                {seg_join}
                WHERE segments_fts MATCH :q{clause}
            )
        ) WHERE rn <= {MOMENT_CANDIDATES} ORDER BY rank
    """
    try:
        seg_rows = con.execute(seg_sql, params).fetchall()
    except sqlite3.OperationalError:
        seg_rows = []

    taken: dict[int, list[int]] = {}
    for n, seg, start, pos, r in seg_rows:
        if pool is not None and n not in pool:
            continue
        h = hits.setdefault(n, {"n": n, "meta": 0.0, "seg": 0.0, "moments": []})
        if len(h["moments"]) >= MOMENTS:
            continue
        # An overlapping passage is the same moment said twice.
        if any(abs(pos - p) < PASSAGE_SPAN for p in taken.get(n, ())):
            continue
        taken.setdefault(n, []).append(pos)
        h["moments"].append({"start": start, "text": "", "seg": seg})
        # Diminishing returns: the second and third time a phrase is spoken
        # says less than the first, and a long talk should not win on volume.
        h["seg"] += -r / (len(h["moments"]) ** 0.5)

    if together_q and hits:
        counts = dict(con.execute(
            "SELECT s.talk_n, count(*) FROM segments_fts JOIN segments s "
            "ON s.rowid = segments_fts.rowid WHERE segments_fts MATCH ? GROUP BY s.talk_n",
            (together_q,)).fetchall())
        for n, h in hits.items():
            h["together"] = counts.get(n, 0)
            h["seg"] *= 1 + PASSAGE_W * min(1.0, math.log1p(h["together"]) / SATURATE)

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
            "duration_min published_at url youtube_url has_transcript timing").split()
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


def stats(con) -> dict:
    """What the corpus is, counted from the index rather than remembered.

    The skill used to quote "2,942 of 8,822" and was wrong within a week; a
    number a model reads should come from the data it is about to search.
    Transcripts are counted as talks.db counts them — a file below the wpm
    floor is on disk but is not content, and is not counted here either.
    """
    total, with_tr = con.execute("SELECT count(*), sum(has_transcript) FROM talks").fetchone()
    exact, = con.execute("SELECT count(*) FROM talks WHERE timing = 'exact'").fetchone()
    years = [{"year": y, "talks": n, "transcripts": t} for y, n, t in con.execute(
        "SELECT year, count(*), sum(has_transcript) FROM talks GROUP BY year "
        "ORDER BY year IS NULL, year DESC")]
    confs = [{"conference": c, "name": name, "talks": n, "transcripts": t} for c, name, n, t in con.execute(
        "SELECT conference, max(conference_name), count(*), sum(has_transcript) FROM talks "
        "GROUP BY conference ORDER BY count(*) DESC, conference")]
    return {"talks": total, "transcripts": with_tr, "transcripts_exact_timing": exact,
            "transcripts_estimated_timing": with_tr - exact,
            "conferences": len(confs), "years": years, "by_conference": confs}


def print_stats(con) -> None:
    st = stats(con)
    ys = [y["year"] for y in st["years"] if y["year"]]
    print(f"{st['talks']:,} talks · {st['transcripts']:,} with a transcript "
          f"({st['transcripts_exact_timing']:,} exact timings, "
          f"{st['transcripts_estimated_timing']:,} estimated) · "
          f"{st['conferences']} conferences · {min(ys)}–{max(ys)}")
    print("\nyear    talks  transcripts")
    for y in st["years"]:
        print(f"{str(y['year'] or '?'):<6} {y['talks']:>6}  {y['transcripts']:>6}")
    print("\nconference                    talks  transcripts")
    for c in st["by_conference"]:
        print(f"{c['conference']:<28} {c['talks']:>6}  {c['transcripts']:>6}")


# ── output ───────────────────────────────────────────────────────────────────


BOLD, DIM, YELLOW, CYAN, OFF = (
    "\033[1m", "\033[2m", "\033[33m", "\033[36m", "\033[0m")


def fmt_ts(sec: float, timing: str | None = "exact") -> str:
    """m:ss — prefixed `~` when the position is interpolated, not measured.

    InfoQ's transcripts and kome.ai's arrive as prose with no caption timings,
    and their starts are estimated from word position across the runtime. A
    reader citing "at 12:34" from one of those is citing a guess; the marker
    is what tells them so.
    """
    stamp = f"{int(sec) // 60}:{int(sec) % 60:02d}"
    return f"~{stamp}" if timing == "estimated" else stamp


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
                print(f"   {CYAN}{fmt_ts(m['start'], h['timing'])}{OFF} {clean_snip(m['text'])}")
                # `&t=` is a YouTube parameter. An InfoQ presentation page
                # ignores it, so that hit gets the page and the timestamp above
                # it rather than a link that pretends to seek.
                if h["youtube_url"]:
                    print(f"        {h['youtube_url']}&t={int(m['start'])}s")
        print(f"   {h['url'] or h['youtube_url'] or ''}")


# What --brief keeps. The rest of the record is one lookup away by id, and a
# reader that is deciding *which* talks to open does not need the channel, the
# tags, the publication timestamp or a second snippet of the same description
# — on a 12-hit result set those fields are most of the bytes and none of the
# decision.
BRIEF = ("id title speakers conference year duration_min url "
         "has_transcript timing score snippet snippet_from matched").split()

# Moments shown per hit under --brief. One passage says whether the talk is
# about the query; the fourth says it again.
BRIEF_MOMENTS = 2


def emit_json(hits: list[dict], brief: bool = False) -> None:
    for h in hits:
        for k in ("n", "meta", "seg", "together"):
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
    ap.add_argument("--conference", action="append",
                    help="conference slug or name, e.g. ai-engineer; repeatable")
    ap.add_argument("--category", action="append", help='e.g. "AI security"; repeatable')
    ap.add_argument("--year", type=year_int, action="append", help="repeatable")
    ap.add_argument("--min-year", type=year_int, metavar="YYYY", help="this year onwards")
    ap.add_argument("--transcript", action="store_true",
                    help="only talks with a transcript — the ones that can be quoted")
    ap.add_argument("--list-conferences", action="store_true",
                    help="print the conferences --conference accepts, and exit")
    ap.add_argument("--list-categories", action="store_true",
                    help="print the categories --category accepts, and exit")
    ap.add_argument("--stats", action="store_true",
                    help="how many talks, transcripts, conferences and years the corpus "
                         "has, per year and per conference, and exit (--json for data)")
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--brief", action="store_true",
                    help="the fields and passages needed to choose a talk, and no more")
    ap.add_argument("--ids", action="store_true",
                    help="print only the video ids, one per line — feeds excerpt.py")
    args = ap.parse_args()

    # The index is derived and not committed: built on first use, and rebuilt
    # when the schema or the corpus has moved on — see atu.db_stale().
    con = atu.connect()

    if args.stats:
        if args.json:
            json.dump(stats(con), sys.stdout, indent=1)
            print()
        else:
            print_stats(con)
        return
    if args.list_conferences or args.list_categories:
        print_facet(con, "conference" if args.list_conferences else "category")
        return
    if not args.query:
        ap.error("a query is required "
                 "(or --stats / --list-conferences / --list-categories to see the corpus)")

    filters = build_filters(
        conference=[resolve(con, "conference", c, "--list-conferences") for c in args.conference or []],
        category=[resolve(con, "category", c, "--list-categories") for c in args.category or []],
        year=[resolve(con, "year", y, None) for y in args.year or []],
        min_year=args.min_year,
        transcript=args.transcript,
    )
    parsed = parse_query(" ".join(args.query))
    hits, dropped = search(con, parsed, args.limit, filters)
    if dropped:
        kept = [t for t in parsed.terms if t not in dropped]
        warn(f"no talk has every word — dropped {', '.join(dropped)} (the commonest); "
             f"searched for: {' '.join(kept)}")

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
