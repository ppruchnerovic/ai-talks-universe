#!/usr/bin/env python3
"""Search the AI talk knowledge base from the command line.

Two layers are searched and merged:
  * talk metadata + YouTube descriptions (always available)
  * transcript passages (only for talks whose transcript has been fetched),
    which also gives the timestamp — and a deep link — for each hit.

    python3 query.py "context engineering"
    python3 query.py "prompt injection" --category security   # one word of a label suffices
    python3 query.py "agents" --category security --topic agents   # security-conference speakers on agents
    python3 query.py "agent memory" --topic "RAG, retrieval & knowledge"
    python3 query.py "agents in production" --conference langchain-interrupt
    python3 query.py "evals" --year 2026 -n 20
    python3 query.py "agents -rag"             # every word but that one
    python3 query.py 'speakers:"harrison chase"'   # one column only
    python3 query.py "agents" --sort newest --since 2026-01-01
    python3 query.py "agents" --per-conference 2 --facets
    python3 query.py --speaker "harrison chase" --sort newest   # no query: a listing
    python3 query.py --random --transcript     # a talk to read, at random
    python3 query.py "agent memory" -n 6 --excerpt   # the list, then what each says
    python3 query.py "mcp" --json              # for scripts and agents
    python3 query.py "mcp" --json --brief      # the same, at a third of the bytes
    python3 query.py --list-conferences        # what --conference accepts
    python3 query.py --list-categories         # what --category accepts
    python3 query.py --list-topics             # what --topic accepts, with counts

FTS5 syntax works: quoted "exact phrase", OR, NOT, prefix*, and column filters
(`title:agents`, `speakers:"harrison chase"`, `{title tags}:rag`,
`transcript:kubernetes` — no space after the colon). A query written in that
syntax is run exactly as typed. A bare query is read as its content words —
"how do you evaluate agents in production" is `evaluate agents production` —
and a talk is a hit when every one of those words appears somewhere in it, in
its metadata or in what was said. When no talk has all of them, the commonest
word is dropped and the search retried, one word at a time, and stderr says
which words were dropped. That is what makes a natural-language question
answerable without letting its filler words rank the answer. A word written
`-word` is an exclusion: talks saying it leave the pool, and nothing else
changes.
"""

from __future__ import annotations

import argparse
import difflib
import json
import math
import os
import random
import re
import sqlite3
import sys
from collections import Counter
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

# A --sort other than relevance is applied to a wider candidate set than the
# limit — the top 5×limit, at least 100 — and only to the part of it that
# scores at least this fraction of the best hit. Without the floor, "newest"
# over a common word is the newest talk that mentions it once in passing;
# without the wider set, it is only the top ten re-ordered. 0.3 keeps every
# talk whose metadata answers the query at all (a title match alone scores
# about 1.0 of a possible 1.7) and drops the ones that merely say a word in
# one passage. The same floor bounds --random and --per-conference/--per-year.
SORT_SCORE_FLOOR = 0.3
SORT_WIDTH = 5
SORT_MIN_WIDTH = 100

# 128 + SIGPIPE and 128 + SIGINT, which is what a shell reports for a process
# killed by either signal — the closest thing to a right answer for `| head`.
EXIT_SIGPIPE = 141
EXIT_SIGINT = 130


def warn(msg: str) -> None:
    """Everything advisory goes to stderr, so --json stays machine-readable."""
    print(msg, file=sys.stderr)


# ── the query ────────────────────────────────────────────────────────────────

OPERATORS = {"AND", "OR", "NOT", "NEAR"}

# FTS5 column filters — `title:agents`, `{title tags}:rag` — and the one this
# tool adds, `transcript:`, which is the passage layer's only column. Only these
# names (and a few aliases) are read as a filter, and only with the colon glued
# to the term, so "agents: what works" and "conference: any" stay bare
# questions. Every other prefix goes through FTS5 as a term, as it did before.
COLUMNS = {
    "title": "title", "description": "description", "desc": "description",
    "tags": "tags", "tag": "tags", "speakers": "speakers", "speaker": "speakers",
    "conference": "conference_name", "conf": "conference_name",
    "conference_name": "conference_name", "transcript": "transcript",
}
PREFIX_RE = re.compile(r"^(\{[^}]*\}|[A-Za-z_]\w*):(.*)$", re.S)
EXPLICIT_RE = re.compile(
    r'["*]|\b(?:OR|NOT|AND|NEAR)\b|(?:\{[^}]*\}|\b(?:' + "|".join(COLUMNS) + r"))(?=:\S)", re.I)
WORD_RE = re.compile(r"[\w'+#.-]+")
# A column-prefixed term (its phrase kept attached, so the prefix and what it
# scopes stay one item), a quoted phrase (optionally prefixed), a parenthesis
# or comma of NEAR(), or a bare term — which covers `agent*`, `gpt-4`, `c#`
# and the operators alike.
SCAN_RE = re.compile(
    r'(?:\{[^}]*\}|[^\s()",:]+):(?:"[^"]*"\*?|[^\s()",]*)|"[^"]*"\*?|[()]|,|[^\s()",]+')


def is_stop(word: str) -> bool:
    w = word.lower()
    return w in atu.STOPWORDS or w in QUERY_STOPWORDS


def quoted(word: str) -> str:
    return '"' + word.replace('"', '""') + '"'


def group_expr(members: tuple[str, ...]) -> str:
    """One gate term as FTS5 sees it: a word, or the OR of its synonyms."""
    if len(members) == 1:
        return quoted(members[0])
    return "(" + " OR ".join(quoted(m) for m in members) + ")"


class Parsed(NamedTuple):
    """What was typed, as FTS5 will see it.

    `strict` is the expression run as typed for explicit syntax, and the AND
    of the content words for a bare query. `terms` are those content words —
    empty for explicit syntax, which is never relaxed because it says what it
    wants. `groups` is, per term, the words that count as saying it: the term
    itself and its synonyms from atu.SYNONYMS. A group is one gate term — a
    talk passes on any member, relaxation drops the whole group. `excluded`
    are the `-word`s. `relaxed` is the OR of everything, which excerpt.py
    falls back to inside one talk, where a ~25-word passage rarely holds all
    of a question's words.

    For explicit syntax with column filters, `meta` and `seg` are the
    expression each layer runs — `transcript:` terms are for the passage
    layer only, every other filter names a talks_fts column — and `gate`, for
    a flat AND chain, is the items every talk must match somewhere. Both are
    the whole of `strict` when no filter was typed. `strict == ""` is a
    listing: no query, just filters.
    """
    strict: str
    terms: tuple[str, ...]
    groups: tuple[tuple[str, ...], ...] = ()
    excluded: tuple[str, ...] = ()
    meta: str | None = None
    seg: str | None = None
    gate: tuple[str, ...] = ()

    @property
    def relaxed(self) -> str | None:
        members = [m for g in self.groups for m in g]
        return " OR ".join(quoted(m) for m in members) if len(self.terms) > 1 else None


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
BAREWORD_RE = re.compile(r"^[\w-\U0010ffff]+\*?$")


def column_spec(prefix: str) -> str | None:
    """`title` → `title`, `speaker` → `speakers`, `{title tag}` → `{title tags}`.

    None when the name is not a column, so `12:30` and `https://…` stay terms.
    """
    if prefix.startswith("{"):
        names = [COLUMNS.get(n.lower()) for n in prefix[1:-1].split()]
        return "{" + " ".join(names) + "}" if names and all(names) else None
    return COLUMNS.get(prefix.lower())


def quote_term(term: str) -> str:
    """A bare term made safe for FTS5, with a trailing `*` kept outside.

    `gpt-4*` becomes `"gpt-4"*`, which is the same prefix query written the way
    FTS5 can parse it; a single token in quotes means what the bare token
    means, so this never changes what a query asks — only whether it runs. A
    column filter is passed through unquoted with its term quoted the same
    way: `speakers:"harrison chase"` stays a filter, `title:gpt-4` becomes
    `title:"gpt-4"`. Quoting the prefix used to turn the filter into a phrase
    that matched nothing.
    """
    if term.startswith('"') or term in OPERATORS or term in ("(", ")", ","):
        return term
    m = PREFIX_RE.match(term)
    if m and column_spec(m.group(1)):
        body = m.group(2)
        return column_spec(m.group(1)) + ":" + (quote_term(body) if body else "")
    if BAREWORD_RE.match(term):
        return term
    prefix = term.endswith("*")
    body = term[:-1] if prefix else term
    return '"' + body.replace('"', '""') + '"' + ("*" if prefix else "")


def explicit_items(raw: str) -> tuple[list[str], str | None]:
    """The query as FTS5 items, and the operator if it is a flat chain.

    Every bare term that FTS5 would misread is quoted — see quote_term() — and
    a stray comma, which is syntax only inside NEAR(), is dropped. Both are
    meaning-preserving, so they apply to every query.

    De-duplication and the cap apply only to a flat chain joined by one
    operator: AND and OR are idempotent, so dropping a repeat is a no-op and
    truncating leaves a valid expression. Anything with parentheses, NEAR, NOT
    or a mix of operators — where dropping a term would change what the query
    asks — is passed through with its terms quoted and nothing else touched;
    the operator returned is then None. For a flat chain it is "AND", "OR", or
    "" for the implicit AND of terms written side by side.
    """
    items = [quote_term(it) for it in SCAN_RE.findall(raw)]
    if "NEAR" not in items:
        items = [it for it in items if it != ","]
    if any(it in ("(", ")", ",", "NEAR") for it in items):
        return items, None
    ops = {it for it in items if it in OPERATORS}
    if len(ops) > 1 or ops - {"AND", "OR"}:
        return items, None
    terms = [it for it in items if it not in OPERATORS]
    if not terms:
        raise SystemExit("empty query")
    return cap(dedupe(terms, key=lambda t: " ".join(t.lower().split()))), (ops.pop() if ops else "")


def explicit_query(raw: str) -> str:
    """Make a typed FTS5 query runnable — the expression as one string."""
    if raw.count('"') % 2:  # unbalanced: let FTS5 report its own error
        return raw
    items, op = explicit_items(raw)
    return (f" {op} " if op else " ").join(items) if op is not None else " ".join(items)


def item_scope(item: str) -> str:
    """Which layer an FTS5 item can match on: "meta", "seg" or "both"."""
    m = PREFIX_RE.match(item)
    if not m or m.group(1) == "":
        return "both"
    return "seg" if m.group(1) == "transcript" else "meta"


def strip_prefix(item: str) -> str:
    m = PREFIX_RE.match(item)
    return m.group(2) if m else item


def split_layers(items: list[str], op: str | None) -> tuple[str | None, str | None, tuple[str, ...]]:
    """The expression each layer runs, and what to gate on, for column filters.

    talks_fts has the metadata columns; segments_fts has one column, the
    passage text, which `transcript:` names. A filter is therefore meaningful
    on one layer only, and an expression using one cannot simply be run on
    both — `speakers:"harrison chase"` on the passage layer would either fail
    or, stripped, find every passage in which someone *says* his name.

    In a flat OR chain each layer takes the items it can match: the union is
    what OR means. In a flat AND chain each layer likewise takes its own
    items, and every item becomes a gate — a talk must match all of them, each
    in the column it names — so `speakers:"harrison chase" agents` is his
    talks about agents, ranked on both layers, rather than his talks plus
    every talk that says "agents" on stage. That is the same gate a bare query
    goes through. Anything with parentheses, NEAR or NOT runs on a layer only
    if none of its items is foreign to that layer, since a term cannot be
    removed from such an expression without changing what it asks.
    """
    scopes = [item_scope(it) for it in items]
    joined = (f" {op} " if op else " ").join if op is not None else " ".join
    if all(s == "both" for s in scopes):
        expr = joined(items)
        return expr, expr, ()
    if op is None:
        meta = joined(items) if "seg" not in scopes else None
        seg = joined([strip_prefix(it) for it in items]) if "meta" not in scopes else None
        if meta is None and seg is None:
            raise SystemExit("a query with parentheses, NEAR or NOT cannot mix transcript: "
                             "with the other column filters — split it into two searches")
        return meta, seg, ()
    meta_items = [it for it, s in zip(items, scopes) if s != "seg"]
    seg_items = [strip_prefix(it) for it, s in zip(items, scopes) if s != "meta"]
    meta = joined(meta_items) if meta_items else None
    seg = joined(seg_items) if seg_items else None
    gate = tuple(items) if op != "OR" else ()
    return meta, seg, gate


def parse_explicit(raw: str) -> Parsed:
    if raw.count('"') % 2:  # unbalanced: let FTS5 report its own error
        return Parsed(raw, (), meta=raw, seg=raw)
    items, op = explicit_items(raw)
    strict = (f" {op} " if op else " ").join(items) if op is not None else " ".join(items)
    meta, seg, gate = split_layers(items, op)
    return Parsed(strict, (), meta=meta, seg=seg, gate=gate)


def synonyms(word: str) -> tuple[str, ...]:
    """The word and, when it belongs to a group of atu.SYNONYMS, the others.

    Membership is by stem, as the browser tests it: "databases" is in the
    `db` group because it stems to what "database" stems to. The members are
    passed to FTS5 as words, not stems, because FTS5 stems the query itself
    and Porter is not idempotent — "database" → "databas" → "databa" — so a
    stem sent as a query would not always find the documents it was cut from.
    Both rankers still match the same talks: the browser looks up
    stem(member) in an index keyed on the same stems FTS5 produces.
    """
    s = atu.stem(word.lower())
    for group in atu.SYNONYMS:
        if any(atu.stem(m) == s for m in group):
            return (word,) + tuple(m for m in group if atu.stem(m) != s)
    return (word,)


def parse_query(raw: str) -> Parsed:
    """Turn what was typed into the words to search for.

    Explicit FTS5 syntax is run as typed — never expanded, never relaxed. A
    bare query is reduced to its content words — the stopwords are dropped
    *before* the strict form is built, not only from the relaxed one, because
    "how do you evaluate agents in production" ANDed whole matched four
    metadata-only talks on "how", "do", "you" and "in" and never reached the
    transcripts, where seven words never share a 25-word passage. Only when
    every word is a stopword are they all kept, so a search for "the thing"
    still searches for something. A `-word` is taken out as an exclusion
    before any of that. Nothing at all — no words, or only exclusions — is a
    listing, and returns with `strict == ""`.
    """
    if EXPLICIT_RE.search(raw):
        return parse_explicit(raw)
    words = cap(dedupe(WORD_RE.findall(raw)))
    excluded = tuple(dedupe([w.lstrip("-") for w in words if w.startswith("-") and w.lstrip("-")]))
    words = [w for w in words if not w.startswith("-")]
    if not words:
        return Parsed("", (), excluded=excluded)
    content = [w for w in words if not is_stop(w)] or words
    groups = tuple(synonyms(w) for w in content)
    return Parsed(" AND ".join(group_expr(g) for g in groups), tuple(content), groups, excluded)


# ── the search ───────────────────────────────────────────────────────────────


class Filters(NamedTuple):
    """The WHERE fragment for the talks table, aliased `t`, and its binds."""
    clause: str
    params: dict


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def build_filters(conference=None, category=None, year=None, min_year=None, max_year=None,
                  transcript=False, speaker=None, min_duration=None, max_duration=None,
                  since=None, before=None, exact_timing=False, topic=None) -> Filters:
    """Every --flag that narrows the talks table, as one WHERE fragment.

    A date bound compares `published_at` as text — it is ISO 8601, which sorts
    as it reads — and for the fifth of the corpus that has no publication
    date falls back to the year, which every talk has: a 2025 talk with no
    date is inside `--since 2025-06-01`, since all we know is its year and
    the year qualifies. `--speaker` is a case-insensitive substring of the
    comma-joined speakers column (ASCII case only — SQLite's LIKE). Topics
    are multi-valued, so `--topic` is membership in the join table, and
    several values are OR-ed as several `--conference` values are.
    """
    where, params = [], {}
    for col, vals in (("conference", conference), ("category", category), ("year", year)):
        vals = [v for v in (vals or []) if v is not None and v != ""]
        if vals:
            keys = [f"{col}{i}" for i in range(len(vals))]
            where.append(f"t.{col} IN ({', '.join(':' + k for k in keys)})")
            params.update(zip(keys, vals))
    for key, val, cond in (("min_year", min_year, "t.year >= :min_year"),
                           ("max_year", max_year, "t.year <= :max_year"),
                           ("min_duration", min_duration, "t.duration_min >= :min_duration"),
                           ("max_duration", max_duration, "t.duration_min <= :max_duration")):
        if val is not None:
            where.append(cond)
            params[key] = val
    for key, val, cmp in (("since", since, ">="), ("before", before, "<=")):
        if val:
            if not DATE_RE.match(val):
                raise SystemExit(f"--{key} wants YYYY-MM-DD, not {val!r}")
            where.append(f"((t.published_at IS NOT NULL AND substr(t.published_at, 1, 10) {cmp} :{key})"
                         f" OR (t.published_at IS NULL AND t.year {cmp} :{key}_year))")
            params[key] = val
            params[f"{key}_year"] = int(val[:4])
    if speaker:
        where.append("t.speakers LIKE :speaker ESCAPE '\\'")
        params["speaker"] = "%" + re.sub(r"([%_\\])", r"\\\1", speaker) + "%"
    # Topics are multi-valued, so the test is membership in the join table
    # rather than equality on a column. Several --topic values are OR-ed, as
    # several --conference values are: any of them admits the talk.
    topics = [v for v in (topic or []) if v]
    if topics:
        keys = [f"topic{i}" for i in range(len(topics))]
        where.append("t.n IN (SELECT talk_n FROM talk_topics WHERE topic IN "
                     f"({', '.join(':' + k for k in keys)}))")
        params.update(zip(keys, topics))
    if transcript:
        where.append("t.has_transcript = 1")
    if exact_timing:
        where.append("t.timing = 'exact'")
    return Filters((" AND " + " AND ".join(where)) if where else "", params)


def talks_matching(con, expr: str, scope: str = "both") -> set[int]:
    """Every talk matching an FTS5 expression on one layer, or on either."""
    ids: set[int] = set()
    try:
        if scope != "seg":
            ids |= {r[0] for r in con.execute(
                "SELECT rowid FROM talks_fts WHERE talks_fts MATCH ?", (expr,))}
        if scope != "meta":
            ids |= {r[0] for r in con.execute(
                "SELECT DISTINCT talk_n FROM segments WHERE rowid IN "
                "(SELECT rowid FROM segments_fts WHERE segments_fts MATCH ?)",
                (strip_prefix(expr) if scope == "seg" else expr,))}
    except sqlite3.OperationalError as e:
        raise SystemExit(f"bad query: {e}")
    return ids


def talks_saying(con, term: str) -> set[int]:
    """Every talk in which this word appears — in its metadata or on stage.

    This is the gate index.html applies ("every query term must appear
    somewhere"), and it is what lets both layers be scored on the OR of the
    words without a common word pulling in the whole corpus: the OR ranks,
    the gate decides who is ranked. Two lookups a word, under 30 ms each on
    the commonest words in the corpus.
    """
    return talks_matching(con, quoted(term))


class Result(NamedTuple):
    """Every scored talk, best first, and how the query got there.

    `hits` is the whole pool, not the top n: --sort, --random, --facets and
    --per-conference all need to see past the limit, so the cut is made
    later, by arrange(). A hit here has its scores and moments but not yet
    its columns or snippets — add_columns() and add_snippets() fill those in
    for the hits that will actually be shown. `meta_q` and `seg_q` are what
    each layer was scored on, which the snippets are cut on too.
    """
    hits: list[dict]
    dropped: tuple[str, ...]      # words relaxed away, commonest first
    meta_q: str | None = None
    seg_q: str | None = None
    # The talks the --flags admit (None: all of them) and the ones a `-word`
    # threw out — what a second ranker over the same corpus must respect too.
    allowed: set[int] | None = None
    banned: frozenset = frozenset()


def admitted(con, filters: Filters) -> set[int] | None:
    """The talks the filters let through, or None when there are no filters."""
    if not filters.clause:
        return None
    return {r[0] for r in con.execute(f"SELECT t.n FROM talks t WHERE 1=1{filters.clause}",
                                      filters.params)}


def listing(con, filters: Filters, banned: set[int] = frozenset()) -> Result:
    """Every talk the filters admit, unscored — for --sort and --random alone."""
    rows = con.execute(f"SELECT t.n FROM talks t WHERE 1=1{filters.clause}", filters.params)
    hits = [{"n": n, "meta": 0.0, "seg": 0.0, "moments": [], "score": None}
            for n, in rows if n not in banned]
    return Result(hits, (), banned=frozenset(banned))


def search(con, parsed: Parsed, filters: Filters) -> Result:
    """Rank the talks that answer the query, relaxing it one word at a time.

    Explicit FTS5 syntax is run as typed on both layers: it says what it
    wants and is never relaxed. A bare query is its content words, and a talk
    qualifies when every word appears somewhere in it. When no talk has all
    of them, the word present in the most talks is dropped and the gate
    re-applied — a single wrong word in a question then costs that word, not
    the whole question, and the OR-of-everything cliff that once ranked "Your
    People Are The Future Of Your Brand" first for "what do people say about
    agent reliability" is gone. What was dropped is returned, to be said.

    An excluded word subtracts its talks from the pool and touches nothing
    else: the words that remain are gated, relaxed and ranked as if it had
    not been typed. Synonyms are gated as one term — any member admits a talk
    — and dropped as one.
    """
    banned = frozenset().union(*(talks_saying(con, x) for x in parsed.excluded))
    if not parsed.strict:
        return listing(con, filters, banned)
    allowed = admitted(con, filters)

    if not parsed.terms:
        pool = None
        if parsed.gate:
            pool = set.intersection(*(talks_matching(con, it, item_scope(it)) for it in parsed.gate))
        elif banned:
            pool = talks_matching(con, parsed.strict)
        if pool is not None:
            pool -= banned
        hits = rank(con, parsed.meta, parsed.seg, None, pool, filters)
        return Result(hits, (), parsed.meta, parsed.seg, allowed, banned)

    present = {}
    for term, group in zip(parsed.terms, parsed.groups):
        present[term] = set().union(*(talks_saying(con, m) for m in group))
    if allowed is not None:
        present = {t: ids & allowed for t, ids in present.items()}
    if banned:
        present = {t: ids - banned for t, ids in present.items()}
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
        return Result([], tuple(dropped), allowed=allowed, banned=banned)
    groups = [g for t, g in zip(parsed.terms, parsed.groups) if t in kept]
    expr = " OR ".join(quoted(m) for g in groups for m in g)
    together = " AND ".join(group_expr(g) for g in groups) if len(groups) > 1 else None
    return Result(rank(con, expr, expr, together, pool, filters), tuple(dropped), expr, expr,
                  allowed, banned)


def kept_query(parsed: Parsed, dropped: tuple[str, ...]) -> Parsed:
    """The bare query as it was actually searched: the groups relaxation kept.

    What excerpt.py should look for inside a talk — a dropped word is one no
    talk in the pool says, so searching a passage for it is wasted, and
    excerpt.py's own fallback to the OR of everything would then say the
    passages match "any of" a word list that includes the dropped one.
    """
    if not dropped or not parsed.terms:
        return parsed
    kept = [(t, g) for t, g in zip(parsed.terms, parsed.groups) if t not in dropped]
    return Parsed(" AND ".join(group_expr(g) for _, g in kept), tuple(t for t, _ in kept),
                  tuple(g for _, g in kept), parsed.excluded)


def rank(con, meta_q: str | None, seg_q: str | None, together_q: str | None,
         pool: set[int] | None, filters: Filters) -> list[dict]:
    """Score both layers, blend, and return every hit best first.

    `pool`, when given, is the set of talks the gate admitted; rows outside it
    are discarded. `together_q` is the AND of the words, counted per talk over
    the passages, which is what promotes a talk that says them in one breath.
    A layer whose expression is None — a column filter meant for the other
    one — is skipped.
    """
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
    rows = []
    if meta_q:
        try:
            rows = con.execute(meta_sql, {"q": meta_q, **filters.params}).fetchall()
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
    seg_rows = []
    if seg_q:
        try:
            seg_rows = con.execute(seg_sql, {"q": seg_q, **filters.params}).fetchall()
        except sqlite3.OperationalError as e:
            if meta_q is None:
                raise SystemExit(f"bad query: {e}")

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
        # The two normalised, weighted contributions — kept for --explain,
        # where "why is this first?" needs the parts and not just the sum.
        h["meta_score"] = round(W_META * h["meta"] / top_meta, 4)
        h["seg_score"] = round(W_SEG * h["seg"] / top_seg, 4)
        h["score"] = round(h["meta_score"] + h["seg_score"], 4)

    return sorted(hits.values(), key=lambda h: -h["score"])


def collapse_dupes(con, hits: list[dict]) -> list[dict]:
    """One entry per title: a re-upload folds into the first, as `also`.

    Some eighty titles occur two or three times — the same recording posted
    twice by one channel, or once by each of two — and a reader counting
    talks reads them as two talks agreeing. The best-placed one keeps its
    place and carries the others' ids; the count, the facets and -n then
    speak of distinct talks. Titles are compared folded, as norm() folds
    them, and the whole pool is looked at, so the fold is the same whichever
    page or order is shown.
    """
    add_columns(con, hits)
    first: dict[str, dict] = {}
    out = []
    for h in hits:
        key = norm(h["title"] or "")
        kept = first.get(key) if key else None
        if kept is None:
            first[key] = h
            h["also"] = []
            out.append(h)
        else:
            kept["also"].append(h["id"])
    return out


# ── the semantic layer ───────────────────────────────────────────────────────
#
# Optional, and not needed by anything here: tools/semantic.py, vectors built
# by tools/install_semantic.sh. Fused with the lexical ranking by reciprocal
# rank, as a union — see fuse_semantic() — for bare queries only. Explicit
# FTS5 syntax says exactly what it wants and is run as typed, like everywhere
# else in this file.

# How many talks the vectors bring to the fusion: three pages' worth, at
# least this many. The lexical side is passed whole — see fuse_semantic().
SEMANTIC_WIDTH = 3
SEMANTIC_MIN_K = 50


def semantic_layer(want: bool | None, explain: bool):
    """The semantic module when it is to be used, else None.

    `want` is --semantic, --no-semantic or unset. Unset means: use the layer
    when its vectors exist and are current, and say nothing when they are
    not — the reason is printed only under --explain. Asked for by name and
    unavailable, the reason is the error.
    """
    if want is False:
        return None
    import semantic  # lazily: nothing here is needed unless asked for
    why = semantic.why_unavailable()
    if why is None:
        return semantic
    if want:
        raise SystemExit(f"--semantic: {why}")
    if explain:
        warn(f"semantic layer off: {why}")
    return None


def semantic_text(raw: str) -> str:
    """What the vectors embed: the question as asked, minus its `-word`s.

    The stopwords the lexical side strips are meaning to an embedding — "how
    do you keep agents on the rails" says more than "keep agents rails".
    """
    return " ".join(w for w in raw.split() if not (w.startswith("-") and len(w) > 1))


def fuse_semantic(con, sem, res: Result, text: str, k: int) -> list[dict]:
    """The lexical ranking fused with the vectors' by reciprocal rank.

    The top k lexical hits and the k talks nearest the query by vector —
    drawn from the same pool, so a --conference or a `-word` binds both
    sides — go through semantic.fuse_rrf(): a talk on both lists rises, a
    talk on one list alone stays, which is the recall the layer exists for.
    The lexical side is cut to k on purpose. Passed whole, a talk ranked
    300th on its words that the vectors put first outscores the talk whose
    title *is* the query, and the top ten becomes the vectors' list with a
    lexical garnish — measured on "agent evaluation": one of the fused top
    ten was in the lexical top forty. Cut to k, the two lists interleave.

    Scores are the fused ones, scaled so the best is 1.0. The lexical hits
    beyond k follow in their own order, scaled to sit below the fused ones,
    so the score floor --sort and --random apply still means "near the top";
    one of them the vectors also found is one entry, the lexical one, and
    keeps its moments. A hit only the vectors found has no bm25, no moments
    and no snippet. `via` says which side found each hit; `cosine` is kept
    for --explain.
    """
    pool = res.allowed
    if res.banned:
        pool = (pool if pool is not None else {n for n, in con.execute("SELECT n FROM talks")})
        pool = pool - res.banned
    add_columns(con, res.hits)
    by_id = {h["id"]: h for h in res.hits}
    head = res.hits[:k]
    nearest = sem.search_talks(text, k=k, pool=pool)
    cosine = dict(nearest)
    fused = sem.fuse_rrf([h["id"] for h in head], [vid for vid, _ in nearest])
    new = [vid for vid, _ in fused if vid not in by_id]
    n_of: dict[str, int] = {}
    for ids in chunks(new):
        n_of.update(con.execute(
            f"SELECT id, n FROM talks WHERE id IN ({','.join('?' * len(ids))})", ids).fetchall())
    top = fused[0][1] if fused else 1.0
    out = []
    for vid, score in fused:
        h = by_id.get(vid)
        if h is None:
            if vid not in n_of:   # the vectors know a talk the index does not
                continue
            h = {"n": n_of[vid], "meta": 0.0, "seg": 0.0, "moments": [], "via": "semantic"}
        else:
            h["via"] = "both" if vid in cosine else "lexical"
        h["score"] = round(score / top, 4)
        if vid in cosine:
            h["cosine"] = round(cosine[vid], 4)
        out.append(h)
    taken = {h["n"] for h in out}
    tail = [h for h in res.hits[k:] if h["n"] not in taken]
    if tail and out:
        first, below = tail[0]["score"] or 1.0, out[-1]["score"] * 0.99
        for h in tail:
            h["via"] = "lexical"
            h["score"] = round(below * h["score"] / first, 4)
    return out + tail


def semantic_anchors(sem, text: str, hits: list[dict], per_talk: int) -> dict[int, list[float]]:
    """Where in each vector-only hit to excerpt: the nearest transcript windows.

    A talk the vectors found may say none of the query's words, and
    excerpt.py would show its opening; the passage vectors, when they were
    built, say which seconds to show instead. Empty without them.
    """
    only = {h["id"]: h["n"] for h in hits if h.get("via") == "semantic"}
    if not only or not sem.has_chunks():
        return {}
    out: dict[int, list[float]] = {}
    for vid, start, _end, _score in sem.search_chunks(
            text, k=per_talk * len(only), pool=set(only.values()), per_talk=per_talk):
        out.setdefault(only[vid], []).append(start)
    return out


# ── choosing what to show ────────────────────────────────────────────────────

SORTS = ("relevance", "newest", "oldest", "duration", "title")


def date_key(h: dict) -> str:
    """ISO text sorts as it reads; a talk with no date sorts on its year alone,
    which puts it before every dated talk of that year."""
    return (h.get("published_at") or "")[:10] or (str(h["year"]) if h.get("year") else "")


SORT_KEYS = {
    "newest": (lambda h: date_key(h), True),
    "oldest": (lambda h: date_key(h) or "9999", False),
    "duration": (lambda h: h.get("duration_min") or 0, True),   # longest first
    "title": (lambda h: (h.get("title") or "").lower(), False),
}


def above_floor(hits: list[dict], width: int | None) -> list[dict]:
    """The candidates a non-relevance order chooses among — see SORT_SCORE_FLOOR."""
    if not hits or hits[0]["score"] is None:   # a listing: nothing to rank
        return hits
    wide = hits[:width] if width else hits
    floor = SORT_SCORE_FLOOR * hits[0]["score"]
    return [h for h in wide if h["score"] >= floor]


def arrange(con, hits: list[dict], limit: int | None, sort: str = "relevance",
            shuffle: bool = False, seed: int | None = None,
            per: str | None = None, per_k: int = 0) -> list[dict]:
    """From every scored hit, the ones to show, in the order to show them.

    Relevance is the ranking as it came. Any other order is applied to the
    top 5×limit (at least 100) above the score floor, so that sorting by date
    does not lose relevance entirely. --random draws from everything above
    the floor. --per-conference / --per-year keep the best K of each group
    from everything above the floor, groups in order of their best hit, so a
    conference whose best talk is 40th still appears — that is the point —
    and -n, when given, caps the total.
    """
    if per:
        add_columns(con, hits)
        groups: dict = {}
        for h in above_floor(hits, None):
            groups.setdefault(h[per], []).append(h)
        chosen = [h for g in groups.values() for h in g[:per_k]]
        return chosen[:limit] if limit else chosen
    limit = limit or 10
    if shuffle:
        chosen = above_floor(hits, None)
        return random.Random(seed).sample(chosen, min(limit, len(chosen)))
    if sort == "relevance":
        return hits[:limit]
    chosen = above_floor(hits, max(SORT_WIDTH * limit, SORT_MIN_WIDTH))
    add_columns(con, chosen)
    key, reverse = SORT_KEYS[sort]
    return sorted(chosen, key=key, reverse=reverse)[:limit]


def chunks(seq: list, size: int = 400):
    """`rowid IN (…)` one bind variable at a time, within any SQLite's limit."""
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


TALK_COLUMNS = ("id title speakers conference conference_name category edition year channel tags "
                "duration_min published_at url youtube_url has_transcript timing topics").split()


def add_columns(con, hits: list[dict]) -> None:
    """The talks-table columns, for every hit that lacks them. Idempotent."""
    todo = {h["n"]: h for h in hits if "id" not in h}
    for ids in chunks(list(todo)):
        sql = f"SELECT n, {','.join(TALK_COLUMNS)} FROM talks WHERE n IN ({','.join('?' * len(ids))})"
        for row in con.execute(sql, ids):
            todo[row[0]].update(zip(TALK_COLUMNS, row[1:]))
    for h in hits:
        if isinstance(h.get("topics"), str):
            h["topics"] = json.loads(h["topics"] or "[]")


def add_snippets(con, meta_q: str | None, seg_q: str | None, ranked: list[dict]) -> None:
    """The snippets, and which layer each came from, for the hits shown.

    Snippets are cut here rather than in the pool queries, so they cost one
    small lookup per shown result instead of one per candidate — and so every
    indexed column can be asked, which is what tells us what actually matched.
    A listing has no query and gets no snippets.
    """
    add_columns(con, ranked)
    if not ranked:
        return

    # highlight() for the short columns — a title must come back whole, not cut
    # to 24 tokens — and snippet() for the description, which is an essay.
    exprs = ", ".join(f"snippet(talks_fts, {i}, ?, ?, ' … ', 24)" if col == "description"
                      else f"highlight(talks_fts, {i}, ?, ?)"
                      for i, col in enumerate(FTS_COLUMNS))
    meta_snips = {}
    for ids in chunks([h["n"] for h in ranked]) if meta_q else ():
        sql = (f"SELECT rowid, {exprs} FROM talks_fts WHERE talks_fts MATCH ? "
               f"AND rowid IN ({','.join('?' * len(ids))})")
        meta_snips.update({r[0]: r[1:]
                           for r in con.execute(sql, [M0, M1] * len(FTS_COLUMNS) + [meta_q] + ids)})

    seg_snips = {}
    for segs in chunks([m["seg"] for h in ranked for m in h["moments"]]) if seg_q else ():
        sql = (f"SELECT rowid, snippet(segments_fts, 0, ?, ?, ' … ', 26) FROM segments_fts "
               f"WHERE segments_fts MATCH ? AND rowid IN ({','.join('?' * len(segs))})")
        seg_snips.update(con.execute(sql, [M0, M1, seg_q] + segs).fetchall())

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
        if h.get("via") in ("semantic", "both"):
            # Found by meaning. A vector-only hit may still hold some of the
            # words — just not all of them, or the gate would have let it in —
            # and those are highlighted as usual; when it holds none, the
            # layer is named where a column would be.
            matched.append("semantic")
            if h["via"] == "semantic" and not h["snippet"]:
                h["snippet_from"] = "semantic"
        h["matched"] = matched


FACETS = ("conference", "year", "category", "has_transcript")


def count_facets(con, hits: list[dict]) -> dict[str, dict]:
    """How the whole pool — not the page shown — splits by conference, year,
    category and transcript. What the top ten cannot say: that 75% of the
    matches for "agent reliability" are from 2026 because that is where the
    transcripts are, not where the subject is."""
    add_columns(con, hits)
    out = {}
    for f in FACETS:
        c = Counter(h[f] for h in hits)
        if f == "has_transcript":
            c = Counter({"with": c.get(1, 0), "without": c.get(0, 0)})
        out[f] = {str(k if k is not None else "?"): v
                  for k, v in sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0])))}
    return out


# ── the filters ──────────────────────────────────────────────────────────────


def norm(s) -> str:
    """Fold a slug, a name and whatever the user typed onto one key."""
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def facet(con, col: str) -> list[tuple]:
    """(value, label, count) for every value of a filterable column.

    `topic` is not a column but a join table, since a talk carries several;
    its counts are talks per topic, and they sum to more than the corpus.
    """
    if col == "topic":
        return con.execute(
            "SELECT topic, topic, count(*) FROM talk_topics GROUP BY topic ORDER BY 1"
        ).fetchall()
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
    # One word of a longer label is enough when it names exactly one value:
    # `--topic evals` is "Evals, observability & reliability", `--conference
    # build` is Microsoft Build. Said on stderr, so --json output stays clean
    # and nobody wonders what "evals" was taken to mean.
    partial = {v for k, v in index.items() if want in k.split() or k.startswith(want)}
    if len(partial) > 1:
        # "agents" is in two topic names; the one it *heads* is the one it
        # names. "Agents & orchestration", not "Coding assistants & agents".
        partial = {v for k, v in index.items() if k.startswith(want)}
    if len(partial) == 1:
        found = partial.pop()
        if norm(found) != want:
            warn(f"--{col.replace('_', '-')} {value!r} taken as {found!r}")
        return found

    lines = [f"--{col.replace('_', '-')} {value!r} matches nothing"]
    close = difflib.get_close_matches(want, list(index), n=3, cutoff=0.55)
    if close:
        lines.append("did you mean: " + ", ".join(dict.fromkeys(str(index[c]) for c in close)))
    elif len(rows) <= 20:
        lines.append("valid values: " + ", ".join(str(v) for v, _, _ in rows))
    if listing:
        lines.append(f"all {len(rows)} of them: query.py {listing}")
    raise SystemExit("\n".join(lines))


def speaker_names(con) -> Counter:
    """Every name in the speakers column, with how many talks it is on."""
    c: Counter = Counter()
    for s, in con.execute("SELECT speakers FROM talks WHERE speakers IS NOT NULL AND speakers <> ''"):
        c.update(x for x in s.split(", ") if x)
    return c


def check_speaker(con, name: str) -> None:
    """Fail a --speaker that matches nobody, with the nearest names.

    Same reasoning as resolve(): 5,510 distinct names and no listing anyone
    could read, so a substring that hits nothing is far likelier a spelling
    than an absence. Whole names are compared, so "harrisn chase" finds
    Harrison Chase; a first name alone is a substring and never gets here.
    """
    pattern = "%" + re.sub(r"([%_\\])", r"\\\1", name) + "%"
    n, = con.execute("SELECT count(*) FROM talks WHERE speakers LIKE ? ESCAPE '\\'", (pattern,)).fetchone()
    if n:
        return
    names = speaker_names(con)
    by_key = {}
    for nm in names:
        by_key.setdefault(norm(nm), nm)
    lines = [f"--speaker {name!r} matches nobody"]
    close = difflib.get_close_matches(norm(name), list(by_key), n=5, cutoff=0.6)
    if close:
        lines.append("did you mean: " + ", ".join(
            f"{by_key[c]} ({names[by_key[c]]})" for c in close))
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
    topics = [{"topic": tp, "talks": n} for tp, n in con.execute(
        "SELECT topic, count(*) FROM talk_topics GROUP BY topic ORDER BY count(*) DESC, topic")]
    untopical, = con.execute("SELECT count(*) FROM talks WHERE topics = '[]'").fetchone()
    return {"talks": total, "transcripts": with_tr, "transcripts_exact_timing": exact,
            "transcripts_estimated_timing": with_tr - exact,
            "conferences": len(confs), "years": years, "by_conference": confs,
            "by_topic": topics, "talks_without_topic": untopical}


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
    print(f"\ntopic (a talk may carry several; {st['talks_without_topic']:,} carry none)   talks")
    for tp in st["by_topic"]:
        print(f"{tp['topic']:<44} {tp['talks']:>6}")


# ── output ───────────────────────────────────────────────────────────────────

# Colour is decided once, in main(): on for a terminal, off for a pipe or a
# file, off under NO_COLOR (https://no-color.org), and --color / --no-color
# override both. The escape codes were 13% of what a model read through the
# skill before the check existed.
BOLD = DIM = YELLOW = CYAN = OFF = ""


def set_color(enabled: bool) -> None:
    global BOLD, DIM, YELLOW, CYAN, OFF
    BOLD, DIM, YELLOW, CYAN, OFF = (
        ("\033[1m", "\033[2m", "\033[33m", "\033[36m", "\033[0m") if enabled else ("",) * 5)


def want_color(override: bool | None) -> bool:
    if override is not None:
        return override
    if os.environ.get("NO_COLOR"):
        return False
    return bool(getattr(sys.stdout, "isatty", lambda: False)())


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


def render(hits: list[dict], show_moments: bool, explain: bool = False) -> None:
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
        if h.get("also"):
            print(f"   {DIM}(also: {', '.join(h['also'])}){OFF}")
        if h["topics"]:
            print(f"   {DIM}topics: {' · '.join(h['topics'])}{OFF}")
        if explain and h["score"] is not None:
            if "via" in h:
                print(f"   {DIM}score {h['score']:.3f} fused by rank, via {h['via']}"
                      + (f", cosine {h['cosine']:.3f}" if "cosine" in h else "")
                      + f"; meta bm25 {h['meta']:.2f} + transcript bm25 {h['seg']:.2f} "
                      f"({len(h['moments'])} moments"
                      + (f", {h['together']} passages say it all" if "together" in h else "")
                      + f"){OFF}")
            else:
                print(f"   {DIM}score {h['score']:.3f} = meta {h['meta_score']:.3f} "
                      f"(bm25 {h['meta']:.2f}) + transcript {h['seg_score']:.3f} "
                      f"(bm25 {h['seg']:.2f}, {len(h['moments'])} moments"
                      + (f", {h['together']} passages say it all" if "together" in h else "")
                      + f"){OFF}")
        label, body = h["snippet_from"], h["snippet"]
        if label == "title":  # already shown; fall back to the description
            body = h["description_snippet"]
            label = "description" if M0 in body else ""
        if body:
            print(f"   {DIM}{f'[{label}] ' if label else ''}{clean_snip(body, DIM)}{OFF}")
        elif h["snippet_from"] == "semantic":
            print(f"   {DIM}(semantic match: none of the query's words, near it in meaning){OFF}")
        if show_moments and h["moments"]:
            for m in h["moments"]:
                print(f"   {CYAN}{fmt_ts(m['start'], h['timing'])}{OFF} {clean_snip(m['text'])}")
                # `&t=` is a YouTube parameter. An InfoQ presentation page
                # ignores it, so that hit gets the page and the timestamp above
                # it rather than a link that pretends to seek.
                if h["youtube_url"]:
                    print(f"        {h['youtube_url']}&t={int(m['start'])}s")
        print(f"   {h['url'] or h['youtube_url'] or ''}")


def render_facets(total: int, facets: dict[str, dict], top: int = 12) -> None:
    print(f"\n{DIM}{total:,} matching talks{OFF}")
    for name, counts in facets.items():
        items = list(counts.items())
        line = " · ".join(f"{k} {v}" for k, v in items[:top])
        if len(items) > top:
            line += f" · … {len(items) - top} more"
        print(f"   {DIM}{name:<15}{OFF} {line}")


# What --brief keeps. The rest of the record is one lookup away by id, and a
# reader that is deciding *which* talks to open does not need the channel, the
# tags, the publication timestamp or a second snippet of the same description
# — on a 12-hit result set those fields are most of the bytes and none of the
# decision.
BRIEF = ("id title speakers conference year topics duration_min url "
         "has_transcript timing score snippet snippet_from matched also via").split()

# Moments shown per hit under --brief. One passage says whether the talk is
# about the query; the fourth says it again.
BRIEF_MOMENTS = 2

# The per-layer working that rank() leaves on a hit. Popped from the output
# unless --explain asks for it, when it is the answer to "why is this first?".
EXPLAIN = ("meta", "seg", "together", "meta_score", "seg_score", "cosine")

# Every key a hit can carry, for --fields to check against. `also` is the ids
# of re-uploads folded into this hit; `via` is present only when the semantic
# layer took part; `excerpt` only under --excerpt.
HIT_FIELDS = TALK_COLUMNS + ["score", "snippet", "snippet_from", "description_snippet",
                             "matched", "moments", "also", "via", "excerpt"] + list(EXPLAIN)


def parse_fields(spec: str | None, brief: bool) -> list[str] | None:
    """The keys to emit: --fields a,b,c, or --brief's preset, or everything."""
    if spec:
        fields = [f.strip() for f in spec.split(",") if f.strip()]
        bad = [f for f in fields if f not in HIT_FIELDS]
        if bad:
            raise SystemExit(f"--fields: no such field {', '.join(bad)}; "
                             f"fields are: {', '.join(HIT_FIELDS)}")
        return fields
    return BRIEF + ["moments"] if brief else None


def shape(hits: list[dict], fields: list[str] | None, brief: bool, explain: bool) -> list[dict]:
    """A hit as data: lists for the comma-joined columns, markers for the
    matches, the working popped unless asked for, and only the fields wanted."""
    out = []
    for h in hits:
        h = dict(h)
        h.pop("n", None)
        if not explain:
            for k in EXPLAIN:
                h.pop(k, None)
        h["tags"] = [x for x in (h["tags"] or "").split(", ") if x]
        h["speakers"] = [x for x in (h["speakers"] or "").split(", ") if x]
        for k in ("snippet", "description_snippet"):
            h[k] = for_json(h[k])
        moments = [{"start": m["start"], "text": for_json(m["text"])} for m in h["moments"]]
        h["moments"] = moments[:BRIEF_MOMENTS] if brief else moments
        if fields:
            # An excerpt was asked for by its own flag; no field list drops it.
            h = {k: h[k] for k in fields + (["excerpt"] if "excerpt" in h else []) if k in h}
        out.append(h)
    return out


def emit_json(hits: list[dict], brief: bool = False, fields: list[str] | None = None,
              explain: bool = False, envelope: dict | None = None) -> None:
    """The hits as JSON — a bare array, as every consumer expects.

    The skill and the browser's ranking suite both parse stdout as a list of
    hits, so the shape cannot change under them: relaxation and expansion
    notes stay on stderr, where they always were. Only --facets, which has
    no place in a list, wraps the output in an object — {"total", "hits",
    "facets", "notes"} — and that object is where the notes also appear, so a
    caller who opts into the envelope gets everything in one stream.
    """
    data = shape(hits, fields, brief, explain)
    if envelope is not None:
        data = {**envelope, "hits": data}
    json.dump(data, sys.stdout, ensure_ascii=False, indent=None if brief else 2)
    print()


MD_FIELDS = "title speakers conference year duration_min score url".split()


def md_cell(v) -> str:
    if isinstance(v, list):
        v = ", ".join(str(x) if not isinstance(x, dict) else f"{fmt_ts(x['start'])} {x['text']}"
                      for x in v)
    if isinstance(v, float):
        v = f"{v:.3f}"
    return " ".join(str("" if v is None else v).split()).replace("|", "\\|")


def emit_md(hits: list[dict], fields: list[str] | None, explain: bool) -> None:
    """A markdown table: one row a hit, --fields choosing the columns."""
    cols = fields or MD_FIELDS
    rows = shape(hits, cols, False, explain)
    print("| # | " + " | ".join(cols) + " |")
    print("|---|" + "|".join("---" for _ in cols) + "|")
    for i, r in enumerate(rows, 1):
        print(f"| {i} | " + " | ".join(md_cell(r.get(c)) for c in cols) + " |")


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


# What a leftover argument may look like to be read as part of the query
# rather than as a mistyped option: `-rag`, an exclusion. `--rag` is an error.
EXCLUSION_ARG_RE = re.compile(r"^-[^\s-]\S*$")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Ranked search over the AI conference talk knowledge base.",
        epilog='FTS5 syntax works: "exact phrase", OR, NOT, prefix*, and column filters — '
               'title:agents, speakers:"harrison chase", {title tags}:rag, transcript:kubernetes. '
               'A bare query is its content words, all required, relaxed one word at a time '
               'when nothing has them all; -word excludes talks saying it. Quote the query '
               '("agents -rag") or let the shell split it — both work. '
               "With no query, the filters list the corpus, newest first.")
    ap.add_argument("query", nargs="*", help="what to search for; FTS5 syntax works")
    ap.add_argument("-n", "--limit", type=positive_int, default=None,
                    help="how many results to show (default 10; with --per-conference / "
                         "--per-year, no cap)")
    ap.add_argument("--conference", action="append",
                    help="conference slug or name, e.g. ai-engineer; repeatable")
    ap.add_argument("--category", action="append",
                    help='conference type, the kind of venue a talk was given at — one of '
                         'five registry labels, e.g. "Security conferences" or just '
                         '"security"; repeatable. For what a talk is *about*, see --topic')
    ap.add_argument("--topic", action="append",
                    help='a per-talk topic, e.g. "evals" or "RAG, retrieval & knowledge"; '
                         'repeatable, any of them admits a talk — see --list-topics')
    ap.add_argument("--year", type=year_int, action="append", help="repeatable")
    ap.add_argument("--min-year", type=year_int, metavar="YYYY", help="this year onwards")
    ap.add_argument("--max-year", type=year_int, metavar="YYYY", help="up to this year")
    ap.add_argument("--since", metavar="YYYY-MM-DD",
                    help="published on or after; a talk with no date goes by its year")
    ap.add_argument("--before", metavar="YYYY-MM-DD",
                    help="published on or before; a talk with no date goes by its year")
    ap.add_argument("--speaker", metavar="NAME",
                    help="a speaker's name, or part of it, case-insensitively")
    ap.add_argument("--min-duration", type=positive_int, metavar="MIN", help="at least this many minutes")
    ap.add_argument("--max-duration", type=positive_int, metavar="MIN", help="at most this many minutes")
    ap.add_argument("--transcript", action="store_true",
                    help="only talks with a transcript — the ones that can be quoted")
    ap.add_argument("--exact-timing", action="store_true",
                    help="only talks whose transcript timestamps were measured, not estimated")
    ap.add_argument("--sort", choices=SORTS, default=None,
                    help="relevance (default with a query), newest (default without), oldest, "
                         "duration (longest first), title — applied to the best-scoring candidates")
    ap.add_argument("--random", action="store_true", help="a random draw from the matches")
    ap.add_argument("--seed", type=int, help="make --random repeatable")
    ap.add_argument("--per-conference", type=positive_int, metavar="K",
                    help="the best K of every conference in the results")
    ap.add_argument("--per-year", type=positive_int, metavar="K",
                    help="the best K of every year in the results")
    ap.add_argument("--facets", action="store_true",
                    help="count every match by conference, year, category and transcript")
    ap.add_argument("--list-conferences", action="store_true",
                    help="print the conferences --conference accepts, and exit")
    ap.add_argument("--list-categories", action="store_true",
                    help="print the conference types --category accepts, and exit")
    ap.add_argument("--list-topics", action="store_true",
                    help="print the topics --topic accepts, with how many talks carry "
                         "each, and exit")
    ap.add_argument("--stats", action="store_true",
                    help="how many talks, transcripts, conferences and years the corpus "
                         "has, per year and per conference, and exit (--json for data)")
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--explain", action="store_true",
                    help="show each hit's per-layer scores")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--md", action="store_true", help="a markdown table")
    ap.add_argument("--brief", action="store_true",
                    help="the fields and passages needed to choose a talk, and no more")
    ap.add_argument("--fields", metavar="A,B,C",
                    help="which fields --json and --md carry (--brief is a preset of these)")
    ap.add_argument("--ids", action="store_true",
                    help="print only the video ids, one per line — feeds excerpt.py")
    ap.add_argument("--color", action=argparse.BooleanOptionalAction, default=None,
                    help="force colour on or off (default: on for a terminal, off for a "
                         "pipe or under NO_COLOR)")
    ap.add_argument("--excerpt", action="store_true",
                    help="after the list, what each hit says about the query — excerpt.py's "
                         "passages, without the second command; notes then go to stdout")
    ap.add_argument("--passages", type=positive_int, default=None, metavar="N",
                    help="windows of speech per talk under --excerpt (default excerpt.py's)")
    ap.add_argument("--semantic", action=argparse.BooleanOptionalAction, default=None,
                    help="fuse a bare query's ranking with the optional vector layer "
                         "(default: when its vectors exist — tools/install_semantic.sh)")
    args, extra = ap.parse_known_args()
    # argparse reads `-rag` as an option it does not know. An exclusion is the
    # one thing a bare query starts with a dash for, so leftovers of that
    # shape — and the plain words argparse stops collecting after one — go
    # back into the query; anything else unknown is the error it always was.
    for a in extra:
        if EXCLUSION_ARG_RE.match(a) or not a.startswith("-"):
            args.query.append(a)
        else:
            ap.error(f"unrecognized arguments: {a}")
    set_color(want_color(args.color))

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
    if args.list_conferences or args.list_categories or args.list_topics:
        print_facet(con, "conference" if args.list_conferences
                    else "category" if args.list_categories else "topic")
        return
    if args.per_conference and args.per_year:
        ap.error("--per-conference and --per-year are one or the other")
    if args.seed is not None and not args.random:
        ap.error("--seed only means something with --random")

    if args.speaker:
        check_speaker(con, args.speaker)
    filters = build_filters(
        conference=[resolve(con, "conference", c, "--list-conferences") for c in args.conference or []],
        category=[resolve(con, "category", c, "--list-categories") for c in args.category or []],
        year=[resolve(con, "year", y, None) for y in args.year or []],
        min_year=args.min_year, max_year=args.max_year, transcript=args.transcript,
        speaker=args.speaker, min_duration=args.min_duration, max_duration=args.max_duration,
        since=args.since, before=args.before, exact_timing=args.exact_timing,
        topic=[resolve(con, "topic", t, "--list-topics") for t in args.topic or []],
    )
    raw = " ".join(args.query)
    parsed = parse_query(raw)
    if not parsed.strict and not filters.clause and not parsed.excluded and not args.random:
        ap.error("a query, a filter or --random is required "
                 "(or --stats / --list-conferences / --list-categories to see the corpus)")
    if args.passages and not args.excerpt:
        ap.error("--passages only means something with --excerpt")

    # The vector layer, for a bare query: not for explicit syntax, which is
    # run as typed, and not for a listing, which has nothing to embed.
    sem = None
    if parsed.terms:
        sem = semantic_layer(args.semantic, args.explain)
    elif args.semantic:
        warn("--semantic applies to a bare query; explicit FTS5 syntax and listings run as typed")

    # Notes on what the search did to the query. On stderr, so --json stays a
    # bare list (they are repeated inside the --facets envelope, see
    # emit_json) — except under --excerpt, whose reader is a model reading a
    # tool's stdout, where "these passages match any of the words" changes
    # what the passages mean. There they go to stdout, as excerpt.py's do.
    notes = []
    for g in parsed.groups:
        if len(g) > 1:
            notes.append(f"expanded {g[0]} → {' OR '.join(g)}")
    res = search(con, parsed, filters)
    hits, dropped, meta_q, seg_q = res.hits, res.dropped, res.meta_q, res.seg_q
    if dropped:
        kept = [t for t in parsed.terms if t not in dropped]
        notes.append(f"no talk has every word — dropped {', '.join(dropped)} (the commonest); "
                     f"searched for: {' '.join(kept)}")
    text = semantic_text(raw)
    if sem:
        hits = fuse_semantic(con, sem, res, text, max(SEMANTIC_WIDTH * (args.limit or 10),
                                                       SEMANTIC_MIN_K))
        found = sum(1 for h in hits if h.get("via") == "semantic")
        notes.append(f"semantic layer on: {found} talks found by meaning alone, "
                     f"ranked by fused rank")
    hits = collapse_dupes(con, hits)
    stdout_notes = args.excerpt and not args.json and not args.ids
    for note in notes:
        print(f"_note: {note}_") if stdout_notes else warn(note)

    total = len(hits)
    facets = count_facets(con, hits) if args.facets else None
    sort = args.sort or ("relevance" if parsed.strict else "newest")
    per = "conference" if args.per_conference else "year" if args.per_year else None
    chosen = arrange(con, hits, args.limit, sort, args.random, args.seed,
                     per, args.per_conference or args.per_year or 0)
    add_snippets(con, meta_q, seg_q, chosen)

    excerpts = []
    if args.excerpt and not args.ids:
        # Lazily: excerpt.py imports this module, so the import at the top
        # would be circular. Its own functions do the work; this only feeds
        # them the hits and the query as it was actually searched.
        import excerpt
        eq = excerpt_query(parsed, dropped)
        limit = args.passages or excerpt.PASSAGES
        anchors = semantic_anchors(sem, text, chosen, limit) if sem else {}
        for h in chosen:
            talk = excerpt.find_talk(con, h["id"])
            excerpts.append(excerpt.excerpt_talk(con, talk, eq, limit=limit,
                                                 anchors=anchors.get(h["n"], ())))
        if args.json:
            for h, r in zip(chosen, excerpts):
                h["excerpt"] = {k: v for k, v in excerpt.as_json(r).items()
                                if k not in excerpt.COLS and k != "speakers"}

    fields = parse_fields(args.fields, args.brief)
    if args.ids:
        # So that reading the hits is a pipe rather than eight ids retyped:
        #   query.py "…" --ids | xargs python3 excerpt.py -q "…"
        for h in chosen:
            print(h["id"])
    elif args.json:
        envelope = {"total": total, "facets": facets, "notes": notes} if args.facets else None
        emit_json(chosen, args.brief, fields, args.explain, envelope)
    elif args.md:
        emit_md(chosen, fields, args.explain)
    else:
        render(chosen, args.moments and not args.brief, args.explain)
        if facets is not None:
            render_facets(total, facets)
    if excerpts and not args.json:
        import excerpt
        print(f"\n{'─' * 72}")
        for r in excerpts:
            excerpt.render_talk(r, parsed=eq)


def excerpt_query(parsed: Parsed, dropped: tuple[str, ...]) -> Parsed | None:
    """What --excerpt looks for inside a talk: the query as the search ran it.

    A bare query is its kept groups, see kept_query(). Explicit syntax is
    passed whole when it has no column filter, and as its passage-layer part
    when it has — `speakers:` names a column the passages do not have, and a
    query made only of such filters excerpts the opening, which is all it
    can honestly do.
    """
    if parsed.terms:
        return kept_query(parsed, dropped)
    if not parsed.strict:
        return None
    if parsed.seg == parsed.strict:
        return parsed
    return Parsed(parsed.seg, ()) if parsed.seg else None


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
