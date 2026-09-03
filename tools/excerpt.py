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

Three cheaper views exist for when even that is too much. `--quotes` prints
only the sentence that holds a query word, ~30 tokens a quote against ~200 a
window, ~200 a talk in all. `--outline` prints the talk in two-minute buckets
— the words each bucket is about and how often it says the query — ~17
tokens a bucket, so ~370 for a 35-minute talk and ~500 for an hour, which is
enough to see where to aim a second `-q` or an `--at`. `--words` and
`--total-words` bound the output in the unit a model actually reasons in.

    python3 excerpt.py O72p-rBb2bA -q "eval driven development"
    python3 excerpt.py O72p-rBb2bA 5ID22ACI7IM -q evals --window 60 -n 8
    python3 excerpt.py O72p-rBb2bA -q evals --quotes         # one sentence a hit
    python3 excerpt.py O72p-rBb2bA -q evals --outline        # where in the talk
    python3 excerpt.py O72p-rBb2bA --at 12:00 --at 34:10     # these moments
    python3 excerpt.py O72p-rBb2bA --full                    # the whole transcript
    python3 excerpt.py O72p-rBb2bA -q evals --json

Nothing here is coloured: every byte this prints is meant to be read by a
program or a model as often as by a person, so there is no ANSI to strip and
no TTY to test for. Keep it that way.
"""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
import sys

import re
from collections import Counter

import atu
import query

# A YouTube id is 11 characters of [A-Za-z0-9_-] and about one in thirty starts
# with a hyphen — `-stDHMwbBRw` is a talk in this corpus. argparse reads such a
# token as an unknown option and refuses the run, which is exactly what
# `query.py --ids | xargs excerpt.py` produces sooner or later. So ids are
# lifted out of argv before argparse sees it.
ID_RE = re.compile(r"^-[A-Za-z0-9_-]{10}$")

# The options that take a value, so their value is never mistaken for an id.
TAKES_VALUE = {"-q", "--query", "-n", "--passages", "--window", "--opening",
               "--at", "--words", "--total-words"}

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
#
# Measured 2026-09-02 over thirty 30-40 minute talks (bytes/4): the default
# `-n 6` comes to about 1,100 tokens a talk (median 850, a dense talk 2,800),
# `-n 3` to about 1,000 (median 850) — the header, description and opening
# are ~450 of either, and on a typical talk the hits are few enough that the
# two budgets buy the same passages. `-n 10 --window 90` is about 1,900;
# `--full` about 8,000. `--words` is the same budget in words, for a reader
# who thinks in tokens rather than seconds; a word is ~1.3 tokens.

# A sentence longer than this has no punctuation to speak of — an ASR
# transcript without full stops — and the quote falls back to the hit tile.
MAX_QUOTE_WORDS = 60

# The width of an --outline bucket. Two minutes is the grain at which a talk
# changes subject; an hour is thirty lines.
OUTLINE_BUCKET = 120
OUTLINE_TERMS = 5

# Words that carry no subject in speech, on top of atu.STOPWORDS (grammar) and
# query.QUERY_STOPWORDS (the vocabulary of asking). Applied to the outline
# only: they are what every bucket of every talk is about, so tf-idf within
# one talk cannot always demote them and a bucket's five words would
# otherwise be "know want one see go".
OUTLINE_STOPWORDS = set("""
um uh uhm hmm mhm know knows knew want wants wanted need needs needed see sees seen saw
go goes went gone come comes came take takes took put puts use uses used using
one two three first second next last new old big small little bit lots good bad
great nice cool awesome interesting important sure pretty much many another thing
stuff someone everybody nobody yes yep nope maybe probably obviously definitely
mean means meant look looks looked let lets try tries tried start starts started
end ends ended time times today back forward here there ago later still already
different same kind sorts guys folks hello hi hey thanks thank welcome question
questions example examples case cases point points part parts side sides
""".split())


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
        "transcript_words timing").split()


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


# ── timestamps ───────────────────────────────────────────────────────────────

TS_RE = re.compile(r"^(?:(\d+):)?(\d{1,2}):(\d{2})(?:\.\d+)?$")


def parse_at(values: list[str]) -> list[float]:
    """`--at` values as seconds: `600`, `10:00`, `1:02:03`, or a comma list.

    The outline prints `m:ss`, so that is what gets pasted back in.
    """
    out = []
    for v in values:
        for tok in v.split(","):
            tok = tok.strip()
            if not tok:
                continue
            m = TS_RE.match(tok)
            if m:
                h, mnt, s = m.groups()
                secs = (int(h or 0) * 3600) + int(mnt) * 60 + int(s)
            else:
                try:
                    secs = float(tok)
                except ValueError:
                    raise argparse.ArgumentTypeError(
                        f"--at wants seconds or m:ss, not {tok!r}")
            if secs < 0:
                raise argparse.ArgumentTypeError(f"--at cannot be negative: {tok}")
            out.append(float(secs))
    return out


# ── the budget ───────────────────────────────────────────────────────────────


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


def tiles_in(segs: list[tuple[float, str]], spans: list[tuple[float, float]]
             ) -> list[list[tuple[float, str]]]:
    """The primary tiles each span covers, one list per span, empties dropped."""
    out = []
    for lo, hi in spans:
        tiles = [(st, t) for st, t in segs if lo <= st < hi]
        if tiles:
            out.append(tiles)
    return out


def words_in(tiles: list[tuple[float, str]]) -> int:
    return sum(len(t.split()) for _, t in tiles)


def trim_to_words(parts: list[list[tuple[float, str]]], anchors: list[float],
                  limit: int) -> list[list[tuple[float, str]]]:
    """Cut passages down to `limit` words, outermost context first.

    A window is 40 seconds either side of a hit, so the words farthest from
    any hit are the ones least likely to be about it. Tiles come off the ends
    of passages only — never the middle, which would print one passage as two
    and repeat nothing — and always the end tile farthest from the nearest
    anchor across every passage, so the trim is spread over the excerpt
    rather than taken from whichever passage came last. Met to within one
    tile, ~25 words.
    """
    parts = [list(p) for p in parts]
    anchors = anchors or [0.0]

    def distance(tile):
        return min(abs(tile[0] - a) for a in anchors)

    while parts and sum(words_in(p) for p in parts) > limit:
        best = None
        for i, p in enumerate(parts):
            for j in (0, len(p) - 1):
                d = distance(p[j])
                if best is None or d > best[0]:
                    best = (d, i, j)
        _, i, j = best
        del parts[i][j]
        if not parts[i]:
            del parts[i]
    return parts


# ── the hits ─────────────────────────────────────────────────────────────────


def hits_for(con, talk_n: int, parsed, limit: int) -> tuple[list[dict], bool]:
    """Where in this talk the query was said, best passage first.

    Relaxed exactly as `query.py` relaxes: a segment is ~25 words, so a
    three-word question almost never has all three in one of them, and the
    strict AND that ranks talks correctly finds nothing inside one. Without
    the fallback every multi-word query would come back empty here. The
    second value says whether the fallback fired, because the reader must
    be told: passages then match *any* of the words, ranked by the rarest.
    """
    sql = ("SELECT s.start, s.pos, s.bridge, s.text FROM segments_fts "
           "JOIN segments s ON s.rowid = segments_fts.rowid "
           "WHERE segments_fts MATCH ? AND s.talk_n = ? "
           "ORDER BY bm25(segments_fts) LIMIT ?")
    for relaxed, expr in ((False, parsed.strict), (True, parsed.relaxed)):
        if not expr:
            continue
        try:
            rows = con.execute(sql, (expr, talk_n, limit)).fetchall()
        except sqlite3.OperationalError as e:
            raise SystemExit(f"bad query: {e}")
        if rows:
            return [dict(zip(("start", "pos", "bridge", "text"), r)) for r in rows], relaxed
    return [], False


def hit_starts(con, talk_n: int, parsed, limit: int) -> list[float]:
    rows, _ = hits_for(con, talk_n, parsed, limit)
    return [r["start"] for r in rows]


def relaxed_note(talk: dict, parsed) -> str:
    return (f"no 25-word passage in {talk['id']} holds all of "
            f"{', '.join(parsed.terms)}; passages match any of them, "
            f"ranked by the rarest word — narrow -q if they are about the wrong one")


QUERY_WORD_RE = re.compile(r"[\w][\w'+#.\-]*")


def query_stems(parsed) -> set[str]:
    """The stems a passage matched on, for finding the sentence that did.

    A bare query keeps its content words; explicit FTS5 syntax is scanned for
    its barewords and phrase words, minus the operators and NEAR's distance.
    Stemmed with the same Porter as the index, so "evals" finds "evaluation".
    """
    if parsed is None:
        return set()
    # A bare query's groups carry each word's synonyms as well — the passage
    # that matched on "evaluation" for `-q eval` must count as a hit here too.
    words = [w for g in getattr(parsed, "groups", ()) for w in g] or list(parsed.terms) or [
        w for w in QUERY_WORD_RE.findall(parsed.strict)
        if w.upper() not in query.OPERATORS and not w.isdigit()]
    out = set()
    for w in words:
        out.update(atu.stems(w))
    return out


def primary_tiles(con, talk_n: int) -> list[tuple[float, int, str]]:
    """(start, pos, text) of the non-overlapping tiling, in order.

    The bridge passages overlap it, and read back in sequence they would say
    everything twice.
    """
    return con.execute(
        "SELECT start, pos, text FROM segments WHERE talk_n=? AND bridge=0 ORDER BY pos",
        (talk_n,)).fetchall()


def tile_at(tiles: list[tuple[float, int, str]], sec: float) -> dict | None:
    """The primary tile being spoken at `sec`, as a hit-shaped dict.

    Marked `anchor` so that a quote taken here is the sentence under the
    moment asked for, not one that happens to hold a query word.
    """
    hit = None
    for st, pos, text in tiles:
        if st <= sec:
            hit = {"start": st, "pos": pos, "bridge": 0, "text": text, "anchor": True}
        else:
            break
    return hit


# ── passages ─────────────────────────────────────────────────────────────────


def passages(con, talk: dict, parsed, window: float, limit: int, opening: float,
             anchors: list[float] = (), words: int | None = None
             ) -> tuple[list[dict], int, list[str]]:
    """The windows worth printing, how many words the transcript has, notes.

    `anchors` are timestamps to centre a window on regardless of the query —
    what `--at` supplies, and what a caller that found the talk some other
    way than by these words (a semantic hit, an outline bucket) needs so
    that a query matching nothing here does not fall through to the opening.
    They are spent first, then the ranked hits. `words` is a budget in words
    that wins over `limit` when it is the tighter of the two.
    """
    notes: list[str] = []
    rows = primary_tiles(con, talk["n"])
    if not rows:
        return [], 0, notes
    segs = [(st, t) for st, _, t in rows]
    total = sum(len(t.split()) for _, t in segs)
    end = segs[-1][0] + 30

    starts = list(anchors)
    if parsed:
        # Ranked by the same bm25 as query.py, restricted to this talk, so the
        # passage shown here is the passage that put the talk in the results.
        hits, relaxed = hits_for(con, talk["n"], parsed, limit * OVERSAMPLE)
        if relaxed:
            notes.append(relaxed_note(talk, parsed))
        if not hits and not starts:
            # The talk is in the results on its metadata alone. The opening is
            # the honest answer — never the whole transcript, which is what a
            # query matching nothing must not silently cost.
            notes.append(f"nothing in {talk['id']}'s transcript matches "
                         f"{parsed.strict} — showing the opening")
            span = (0.0, opening or 60)
            parts = tiles_in(segs, [span])
            if words:
                parts = trim_to_words(parts, [0.0], words)
            return as_passages(parts, [span]), total, notes
        if not hits and starts:
            notes.append(f"nothing in {talk['id']}'s transcript matches "
                         f"{parsed.strict} — showing the --at moments only")
        starts += [h["start"] for h in hits]

    spans: list[tuple[float, float]] = []
    if starts:
        spans = spans_for(starts, window, limit)
    if opening > 0:
        spans.append((0.0, opening))
    if not spans:
        spans = [(0.0, end)]
    spans = merge(spans)

    parts = tiles_in(segs, spans)
    if words is not None:
        parts = trim_to_words(parts, starts + ([0.0] if opening > 0 else []), words)
    return as_passages(parts, spans), total, notes


def as_passages(parts: list[list[tuple[float, str]]],
                spans: list[tuple[float, float]]) -> list[dict]:
    """Tile runs as {start, end, text, words}, start being the first word's."""
    out = []
    for tiles in parts:
        lo = tiles[0][0]
        hi = next((h for l, h in spans if l <= lo < h), tiles[-1][0] + 10)
        text = " ".join(" ".join(t for _, t in tiles).split())
        out.append({"start": lo, "end": hi, "text": text, "words": len(text.split())})
    return out


# ── quotes ───────────────────────────────────────────────────────────────────

SENTENCE_END_RE = re.compile(r"[.?!]+[\"'”’)\]]*$")


def sentences(words: list[tuple[str, float]]) -> list[list[tuple[str, float]]]:
    """Split (word, start) pairs into sentences at a word ending in [.?!].

    Timed words, not a string, so that a sentence knows when it was said. A
    trailing fragment with no full stop is a sentence too — the last one.
    """
    out, cur = [], []
    for w, st in words:
        cur.append((w, st))
        if SENTENCE_END_RE.search(w):
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def timed_words(tiles: list[tuple[float, int, str]]) -> list[tuple[str, int, float]]:
    """(word, global position, start) for a run of consecutive primary tiles.

    A tile carries one timestamp for ~24 words; a word's own time is
    interpolated between its tile's start and the next tile's, so that a
    quote taken from the end of a tile links ten seconds later than one
    taken from its start, as it should.
    """
    out = []
    for i, (st, pos, text) in enumerate(tiles):
        ws = text.split()
        nxt = tiles[i + 1][0] if i + 1 < len(tiles) else st + 10.0
        for j, w in enumerate(ws):
            out.append((w, pos + j, st + (nxt - st) * j / max(len(ws), 1)))
    return out


def quote_for(tiles: list[tuple[float, int, str]], hit: dict, stems: set[str]) -> dict:
    """The sentence in the hit tile that holds a query word, with its time.

    `tiles` are the primary tiles around the hit (the hit's own ±1, so a
    sentence can start before the tile and end after it). The first sentence
    overlapping the hit that contains a query stem wins; with no stems (an
    `--at` anchor) the sentence under the middle of the hit does. When the
    speech has no punctuation to split on — a sentence longer than
    MAX_QUOTE_WORDS — or nothing qualifies, the hit tile itself is the quote:
    24 words is still a quarter of a window.
    """
    lo, hi = hit["pos"], hit["pos"] + len(hit["text"].split())
    tw = timed_words(tiles)
    mid = (lo + hi) // 2
    # sentences() sees (word, start) pairs; positions run parallel to tw, so
    # a sentence's first and last position are recovered by index.
    pos_of = {i: p for i, (_, p, _) in enumerate(tw)}
    idx = 0
    for sent in sentences([(w, st) for w, _, st in tw]):
        first, last = pos_of[idx], pos_of[idx + len(sent) - 1]
        idx += len(sent)
        if last < lo or first >= hi:
            continue
        text = " ".join(w for w, _ in sent)
        if len(sent) > MAX_QUOTE_WORDS:
            break
        ok = (any(s in stems for s in atu.stems(text)) if stems
              else first <= mid <= last)
        if ok:
            return {"start": round(sent[0][1], 1), "text": text, "words": len(sent),
                    "sentence": True}
    return {"start": hit["start"], "text": " ".join(hit["text"].split()),
            "words": len(hit["text"].split()), "sentence": False}


def quotes(con, talk: dict, parsed, limit: int, anchors: list[float] = (),
           words: int | None = None) -> tuple[list[dict], int, list[str]]:
    """One sentence per hit, best hit first, returned in time order.

    `limit` is a count of quotes here — a quote is one sentence, so counting
    bounds it. `words` caps the total as well when given. Returns the quotes,
    how many distinct quotes there were to choose from, and notes.

    The hits come as overlapping tiles — a primary tile and the bridge tile
    that straddles it usually both match, and both resolve to the same
    sentence — so the count offered as "more" is of distinct sentences, not
    of hits; otherwise every talk would claim twice the quotes it has.
    """
    notes: list[str] = []
    tiles = primary_tiles(con, talk["n"])
    if not tiles:
        return [], 0, notes
    hits: list[dict] = [h for h in (tile_at(tiles, a) for a in anchors) if h]
    if parsed:
        found, relaxed = hits_for(con, talk["n"], parsed, limit * OVERSAMPLE)
        if relaxed:
            notes.append(relaxed_note(talk, parsed))
        if not found and not hits:
            notes.append(f"nothing in {talk['id']}'s transcript matches {parsed.strict}")
        hits += found
    stems = query_stems(parsed)
    distinct: list[dict] = []
    seen: set[str] = set()
    for h in hits:
        lo, hi = h["pos"], h["pos"] + len(h["text"].split())
        ctx = [t for t in tiles if lo - 25 <= t[1] < hi + 25]
        q = quote_for(ctx, h, set() if h.get("anchor") else stems)
        if q["text"] not in seen:
            seen.add(q["text"])
            distinct.append(q)
    out, spent = [], 0
    for q in distinct[:limit]:
        if words is not None and spent + q["words"] > words and out:
            break
        spent += q["words"]
        out.append(q)
    out.sort(key=lambda q: q["start"])
    return out, len(distinct), notes


# ── outline ──────────────────────────────────────────────────────────────────


def outline(con, talk: dict, parsed, bucket: int = OUTLINE_BUCKET,
            terms: int = OUTLINE_TERMS) -> list[dict]:
    """The talk in `bucket`-second slices: its words, and the query's count.

    Each slice gets its top tf-idf stems, idf taken across the slices of this
    one talk — so what is printed is what the slice says that the rest of the
    talk does not, and a talk about agents does not print "agent" thirty
    times. Thirty slices is a small collection for idf, and the stems are a
    hint at best. The *density* column is not a hint: it is a count of the
    query's words in that slice, and it is what tells a reader where to aim
    a second `-q` or an `--at`.
    """
    tiles = primary_tiles(con, talk["n"])
    if not tiles:
        return []
    return bucketize([(st, t) for st, _, t in tiles], query_stems(parsed), bucket, terms)


def bucketize(segs: list[tuple[float, str]], stems: set[str], bucket: int = OUTLINE_BUCKET,
              terms: int = OUTLINE_TERMS) -> list[dict]:
    """The pure part of outline(): (start, text) tiles in, buckets out."""
    counts: dict[int, Counter] = {}
    surface: dict[int, dict[str, Counter]] = {}
    hits: Counter = Counter()
    words: Counter = Counter()
    for st, text in segs:
        b = int(st // bucket)
        c = counts.setdefault(b, Counter())
        sf = surface.setdefault(b, {})
        words[b] += len(text.split())
        for tok in atu.tokenize(text):
            if tok in OUTLINE_STOPWORDS or tok in query.QUERY_STOPWORDS or tok.isdigit():
                continue
            s = atu.stem(tok)
            if len(s) < 2:
                continue
            if s in stems:
                hits[b] += 1
            c[s] += 1
            sf.setdefault(s, Counter())[tok] += 1
    if not counts:
        return []
    n = max(counts) + 1
    df: Counter = Counter()
    for c in counts.values():
        df.update(c.keys())
    out = []
    for b in range(n):
        c = counts.get(b, Counter())
        scored = sorted(c.items(), key=lambda kv: (-kv[1] * math.log(1 + n / df[kv[0]]), kv[0]))
        top = [surface[b][s].most_common(1)[0][0] for s, _ in scored[:terms]]
        out.append({"start": float(b * bucket), "end": float((b + 1) * bucket),
                    "words": words[b], "hits": hits[b], "terms": top})
    return out


# ── output ───────────────────────────────────────────────────────────────────


def header(talk: dict, description: bool = True) -> None:
    print(f"\n## {talk['title']}")
    who = talk["speakers"] or "speaker not recorded"
    edition = talk["edition"] or talk["conference_name"]
    print(f"{who} · {talk['conference_name']} · {edition}"
          + (f" · {talk['year']}" if talk["year"] else "")
          + (f" · {talk['duration_min']} min" if talk["duration_min"] else ""))
    print(talk["url"] or atu.watch_url(talk["id"]) or "")

    if description and talk["description"]:
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


def stamp(talk: dict, sec: float) -> str:
    """`[m:ss](url&t=Ns)` for a YouTube talk; `~m:ss` when the time is a guess.

    `&t=` only means something to YouTube; an InfoQ-only talk keeps its
    timestamps as text rather than as links that cannot seek.
    """
    ts = query.fmt_ts(sec, talk.get("timing") or "exact")
    yt = talk["youtube_url"]
    return f"[{ts}]({yt}&t={int(sec)}s)" if yt else ts


def print_notes(notes: list[str]) -> None:
    # On stdout, deliberately: a model reading this through a tool call never
    # sees stderr, and "these passages match any of the words" changes what
    # the passages mean.
    for n in notes:
        print(f"\n_note: {n}_")


def render(talk: dict, parts: list[dict], total_words: int, full: bool,
           notes: list[str] = ()) -> None:
    header(talk)
    if not talk["has_transcript"]:
        return
    print_notes(notes)
    shown = sum(p["words"] for p in parts)
    for p in parts:
        print(f"\n**{stamp(talk, p['start'])}** {p['text']}")
    if not full and shown < total_words:
        pct = round(100 * shown / total_words) if total_words else 0
        print(f"\n_{shown} of {total_words} words ({pct}%). "
              f"For the rest: excerpt.py {talk['id']} --full, or another -q._")


def render_quotes(talk: dict, qs: list[dict], hits: int, notes: list[str] = ()) -> None:
    header(talk, description=False)
    if not talk["has_transcript"]:
        return
    print_notes(notes)
    if qs:
        print()
    for q in qs:
        print(f"- **{stamp(talk, q['start'])}** {q['text']}")
    if hits > len(qs):
        print(f"\n_{len(qs)} of {hits} matching passages quoted; "
              f"-n {min(hits, len(qs) * 2)} --quotes for more, "
              f"or drop --quotes for the speech around them._")
    elif not qs:
        print("\n_No quotes: give -q or --at._")


def render_outline(talk: dict, buckets: list[dict], parsed, bucket: int = OUTLINE_BUCKET) -> None:
    header(talk, description=False)
    if not talk["has_transcript"] or not buckets:
        return
    total = sum(b["hits"] for b in buckets)
    label = f"{bucket // 60}-minute buckets"
    if parsed:
        # The words typed, not the expanded FTS5 expression with its synonyms
        # and quoting, which is three lines for a three-word query.
        said = ", ".join(parsed.terms) if parsed.terms else parsed.strict
        print(f"\n_{label}; `#` is how often the bucket says {said} "
              f"({total} in all), and is the reliable column. The words are the "
              f"bucket's most distinctive stems by tf-idf within this talk — a hint, "
              f"not a summary. Aim `-q` or `--at m:ss` at the dense buckets._")
    else:
        print(f"\n_{label}, each with its most distinctive words by tf-idf within "
              f"this talk — a hint at the subject, not a summary. Give -q to see "
              f"where a topic is dense; `--at m:ss` reads a bucket._")
    width = max(b["hits"] for b in buckets)
    for b in buckets:
        ts = query.fmt_ts(b["start"], talk.get("timing") or "exact")
        bar = "#" * b["hits"] if parsed else ""
        col = f"{bar:<{width}} {b['hits']:>2}  " if parsed else ""
        print(f"{ts:>6}  {col}{', '.join(b['terms'])}")


# ── one talk, any mode ───────────────────────────────────────────────────────


def excerpt_talk(con, talk: dict, parsed, *, mode: str = "passages",
                 window: float = WINDOW, limit: int = PASSAGES, opening: float = OPENING,
                 anchors: list[float] = (), words: int | None = None,
                 full: bool = False, bucket: int = OUTLINE_BUCKET) -> dict:
    """Everything one talk contributes, as data; render_talk() prints it.

    `mode` is "passages", "quotes" or "outline". `parsed` is a query.Parsed
    or None. This is the entry point for a caller that already has a talk —
    query.py --excerpt, say — and wants what the CLI would print without
    going through argv.
    """
    res = {"talk": talk, "mode": mode, "passages": [], "quotes": [], "outline": [],
           "hits": 0, "total_words": 0, "notes": []}
    if not talk["has_transcript"]:
        return res
    if mode == "quotes":
        qs, hits, notes = quotes(con, talk, parsed, limit, anchors, words)
        res.update(quotes=qs, hits=hits, notes=notes)
    elif mode == "outline":
        res["outline"] = outline(con, talk, parsed, bucket)
    else:
        # --full is the whole transcript: no query, no opening, and no
        # anchors either, or an --at would quietly cut it down to one window.
        parts, total, notes = passages(con, talk, None if full else parsed, window, limit,
                                       0 if full else opening, () if full else anchors, words)
        res.update(passages=parts, total_words=total, notes=notes)
    return res


def render_talk(res: dict, full: bool = False, bucket: int = OUTLINE_BUCKET, parsed=None) -> None:
    talk = res["talk"]
    if res["mode"] == "quotes":
        render_quotes(talk, res["quotes"], res["hits"], res["notes"])
    elif res["mode"] == "outline":
        render_outline(talk, res["outline"], parsed, bucket)
    else:
        render(talk, res["passages"], res["total_words"], full, res["notes"])


def as_json(res: dict) -> dict:
    talk = res["talk"]
    out = {**{k: talk[k] for k in COLS if k != "n"},
           "speakers": [s for s in (talk["speakers"] or "").split(", ") if s],
           "mode": res["mode"], "notes": res["notes"]}
    if res["mode"] == "quotes":
        out["quotes"] = res["quotes"]
        out["matching_passages"] = res["hits"]
        out["excerpt_words"] = sum(q["words"] for q in res["quotes"])
    elif res["mode"] == "outline":
        out["outline"] = res["outline"]
    else:
        out["excerpt_words"] = sum(p["words"] for p in res["passages"])
        out["passages"] = res["passages"]
    return out


def used_words(res: dict) -> int:
    return sum(x["words"] for x in res["passages"] + res["quotes"])


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Print the parts of a talk that answer a question, not the whole talk.",
        epilog=("Cost, roughly, for a 30-40 minute talk: -n 6 is about 1,100 tokens, -n 3 "
                "about 1,000 — the header, description and opening are ~450 of either. "
                "--quotes is about 30 tokens a quote, ~200 a talk; --outline about 17 tokens "
                "a bucket, ~370 for the talk and ~500 for an hour; --full about 8,000."))
    ap.add_argument("ids", nargs="*", metavar="ID",
                    help="video id, YouTube URL, or talks/<conf>/<id>-<slug>.md")
    ap.add_argument("-q", "--query", default="",
                    help="what to excerpt around; FTS5 syntax works, as in query.py")
    ap.add_argument("-n", "--passages", type=query.positive_int, default=PASSAGES,
                    help=f"budget: windows of speech per talk, or quotes with --quotes "
                         f"(default {PASSAGES}); not query.py's result limit")
    ap.add_argument("--window", type=float, default=WINDOW,
                    help=f"seconds of speech either side of a hit (default {WINDOW})")
    ap.add_argument("--opening", type=float, default=OPENING,
                    help=f"seconds of the start to always include (default {OPENING}; 0 for none)")
    ap.add_argument("--at", action="append", default=[], metavar="SECONDS",
                    help="centre a window here (seconds or m:ss; repeatable or comma-separated), "
                         "with or instead of -q hits")
    ap.add_argument("--words", type=query.positive_int, metavar="N",
                    help="cap each talk at N words of transcript (~1.3 tokens a word); "
                         "the tighter of -n and --words wins")
    ap.add_argument("--total-words", type=query.positive_int, metavar="N",
                    help="cap all talks together at N words, shared out in the order given")
    ap.add_argument("--quotes", action="store_true",
                    help="only the sentence holding a query word, per hit, with its time")
    ap.add_argument("--outline", action="store_true",
                    help=f"the talk in {OUTLINE_BUCKET // 60}-minute buckets: distinctive words "
                         f"and how often each says the query")
    ap.add_argument("--full", action="store_true", help="the whole transcript")
    ap.add_argument("--json", action="store_true")
    argv, hyphenated = split_ids(sys.argv[1:])
    args = ap.parse_args(argv)
    args.ids += hyphenated
    if not args.ids:
        ap.error("at least one video id is required")
    if sum((args.quotes, args.outline, args.full)) > 1:
        ap.error("--quotes, --outline and --full are different views; pick one")
    try:
        anchors = parse_at(args.at)
    except argparse.ArgumentTypeError as e:
        ap.error(str(e))
    if args.quotes and not (args.query or anchors):
        ap.error("--quotes needs -q or --at: a quote is a sentence that says something")
    mode = "quotes" if args.quotes else "outline" if args.outline else "passages"

    con = atu.connect()
    parsed = query.parse_query(args.query) if args.query else None
    results, missing = [], []
    talks = []
    for ident in args.ids:
        talk = find_talk(con, ident)
        if talk:
            talks.append(talk)
        else:
            missing.append(ident)

    remaining = args.total_words
    with_transcript = sum(1 for t in talks if t["has_transcript"])
    for talk in talks:
        words = args.words
        if remaining is not None and talk["has_transcript"]:
            share = max(remaining, 0) // max(with_transcript, 1)
            words = share if words is None else min(words, share)
            with_transcript -= 1
        res = excerpt_talk(con, talk, parsed, mode=mode, window=args.window,
                           limit=args.passages, opening=args.opening, anchors=anchors,
                           words=words, full=args.full)
        if remaining is not None and talk["has_transcript"]:
            if words == 0:
                res["notes"].append("--total-words budget was spent before this talk")
                res.update(passages=[], quotes=[])
            remaining -= used_words(res)
        results.append(res)

    if args.json:
        json.dump([as_json(r) for r in results], sys.stdout, ensure_ascii=False, indent=2)
        print()
        for ident in missing:
            die(f"not in the corpus: {ident}")
    else:
        for r in results:
            render_talk(r, args.full, parsed=parsed)
        for ident in missing:
            print(f"\n_not in the corpus: {ident}_")
    return 1 if missing and not results else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(query.EXIT_SIGINT)
    except BrokenPipeError:
        sys.exit(query.EXIT_SIGPIPE)
