#!/usr/bin/env python3
"""Build the search indexes from data/talks.json + data/transcripts/.

Two independent indexes from the same corpus:

  data/talks.db          SQLite + FTS5, used by query.py and by anything that
                         can open a database. Includes a per-passage index, so
                         a hit points at the exact second in the video.

  data/search-meta.json  Every talk's metadata + description, compact keys.
  data/tindex/*.json     Small enough for a browser to load up front. The
  data/tindex/_manifest  transcript inverted index is sharded by the first two
                         letters of a term and fetched lazily, so the site
                         needs no backend.

    python3 build_index.py             # rebuild both indexes into data/
    python3 build_index.py --help      # the flags, without rebuilding anything
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import pathlib
import shutil
import sqlite3
import sys

import atu

# Talks are keyed by YouTube video id — an 11-character string. FTS5 needs an
# integer rowid, and repeating a string id in every posting would roughly treble
# the browser index, so the build assigns a dense integer `n` (position in
# talks.json order, which sync_catalog.py sorts deterministically). Everything
# on disk that outlives a build — transcripts, markdown — stays keyed by video
# id; `n` never leaves the index it was built for, and both halves are always
# rebuilt together.

SCHEMA = """
PRAGMA journal_mode = OFF;
DROP TABLE IF EXISTS talks;
DROP TABLE IF EXISTS talks_fts;
DROP TABLE IF EXISTS segments;
DROP TABLE IF EXISTS segments_fts;

CREATE TABLE talks (
    n INTEGER PRIMARY KEY, id TEXT UNIQUE, title TEXT, description TEXT,
    speakers TEXT, conference TEXT, conference_name TEXT, category TEXT,
    edition TEXT, year INTEGER, channel TEXT, tags TEXT, duration_min INTEGER,
    published_at TEXT, youtube_url TEXT, availability TEXT, priority INTEGER,
    has_transcript INTEGER, transcript_words INTEGER
);
CREATE INDEX idx_talks_conf ON talks(conference);

-- Content-carrying so snippet()/highlight() work. Metadata and descriptions
-- only; transcript text lives in `segments` and is searched through
-- segments_fts, which is what gives every hit a timestamp.
CREATE VIRTUAL TABLE talks_fts USING fts5(
    title, description, tags, speakers, conference_name,
    tokenize='porter unicode61'
);

CREATE TABLE segments (
    rowid INTEGER PRIMARY KEY, talk_n INTEGER, start REAL, text TEXT
);
CREATE INDEX idx_segments_talk ON segments(talk_n);

CREATE VIRTUAL TABLE segments_fts USING fts5(
    text, content='segments', content_rowid='rowid', tokenize='porter unicode61'
);
"""

# Both rankers treat a passage as the unit two query terms have to share, so how
# finely a transcript is cut decides what counts as "said together". That has to
# be a property of the index, not of whichever route fetched the transcript:
# YouTube's captions arrive as ~6-word lines, where "spec driven development" is
# spoken across three of them and matches none. Deep links are unaffected — the
# browser reads the raw caption files.
PASSAGE_WORDS = 25

# A transcript that says almost nothing across a long talk is an ASR failure,
# not a transcript. Four files here are YouTube's Hindi mis-detection on English
# audio giving up: 153 to 185 words over 41- to 73-minute talks, 2.5 to 3.7
# words a minute. The next slowest real transcript in the corpus is 19.9, so
# this is a gap rather than a tuning parameter — anything from 5 to 19 catches
# the same four and nothing else. Below MIN_RATED_MINUTES the ratio is noise, so
# it is not applied; the shortest transcribed talk is 5 minutes at 98 wpm.
#
# The file stays on disk. Deleting it would make fetch_transcripts.select()
# re-pick the talk on every future run and refetch the same bytes forever — the
# same non-convergence argument that has the fetcher save a foreign-language
# track rather than treat it as retryable. The file is evidence that we asked
# and this is what exists; what this floor decides is only whether it is content.
MIN_WPM = 10
MIN_RATED_MINUTES = 5

# atu.TOKEN_RE matches [a-z0-9] only, so a Devanagari, Japanese or Arabic
# transcript tokenises to almost nothing — 20 tokens for 6,084 words. len(toks)
# then measures the script rather than the document, and BM25's length
# normalisation reads it as a tiny document in which any stray Latin token (a
# brand name, a number) is overwhelmingly frequent: one such transcript ranked
# first of 76 for "netflix" and first of 4 for "jio" on the strength of eight
# occurrences in what looked like a 20-word talk. Across the transcripts the
# tokeniser can read, tokens per word runs 0.33 to 0.91 with a median of 0.42;
# below TOKEN_SHARE_FLOOR the count is not about the talk, so the corpus median
# is applied to the raw word count instead.
#
# Both rankers stay comparable because BM25 uses only dl/avg: this changes
# nothing for a transcript the tokeniser can read, and it demotes rather than
# removes the ones it cannot — a talk that really does say "netflix" eight times
# should still be findable, just not above the talks about Netflix.
TOKEN_SHARE_FLOOR = 0.25
TOKENS_PER_WORD = 0.42

# How much of a description reaches the browser's up-front payload. The full
# text stays in talks.json, the markdown and talks.db; this only caps what every
# visitor downloads before typing anything. YouTube descriptions run long and
# repetitive (the same channel boilerplate under 400 talks), so the tail is
# mostly cost.
META_DESC_CHARS = 300

# What "too big" means for search-meta.json, spelled out so nobody has to
# measure it again. THE UNIT IS BINARY — mebibytes, 1024-based — and so is
# atu.human_size(), which now labels its output "MiB" rather than dividing by
# 1024 while saying "MB". The two conventions differ enough to matter at this
# size: 6,045,370 bytes is 5.8 MiB but 6.0 decimal MB, i.e. under the line in
# one unit and over it in the other. atu.decimal_size() is there when a vendor
# figure needs comparing; this trigger is not a vendor figure.
#
# Crossing it is not a failure, it is a prompt: halve META_DESC_CHARS. That is
# what 1200 -> 600 did last time, taking the file from 7.3 MiB to 5.4 MiB, and
# what 600 -> 300 did when seven new conferences took it to 7.8 MiB.
# The run prints where the file stands against this line either way.
META_SIZE_TRIGGER_BYTES = 6 * 1024 * 1024  # 6 MiB = 6,291,456 bytes


def mib(n: int) -> str:
    """Two-decimal MiB, for the size report's arithmetic against the trigger.

    atu.human_size() agrees on the unit; this one keeps a second decimal so
    "96% of the trigger" and the margin are legible.
    """
    return f"{n / (1024 * 1024):.2f} MiB"


def meta_size_report(size: int, desc_chars: int) -> str:
    trigger = f"{META_SIZE_TRIGGER_BYTES // (1024 * 1024)} MiB trigger"
    stands = (f"search-meta.json is {mib(size)} ({size:,} bytes), "
              f"{100 * size / META_SIZE_TRIGGER_BYTES:.0f}% of the {trigger} "
              f"({META_SIZE_TRIGGER_BYTES:,} bytes)")
    if size >= META_SIZE_TRIGGER_BYTES:
        over = size - META_SIZE_TRIGGER_BYTES
        return (f"{stands} — OVER by {mib(over)} ({over:,} bytes). "
                f"Halve META_DESC_CHARS (now {desc_chars}) and rebuild.")
    left = META_SIZE_TRIGGER_BYTES - size
    return f"{stands} — under by {mib(left)} ({left:,} bytes)."


def to_passages(segs: list[dict]) -> list[dict]:
    out: list[dict] = []
    texts: list[str] = []
    start, words = 0.0, 0
    for s in segs:
        if not texts:
            start = s["start"]
        texts.append(s["text"])
        words += len(s["text"].split())
        if words >= PASSAGE_WORDS:
            out.append({"start": start, "text": " ".join(texts)})
            texts, words = [], 0
    if texts:
        out.append({"start": start, "text": " ".join(texts)})
    return out


# Video id -> why its transcript was held back, filled by transcript_text() and
# printed by main(). A silent dropper in the index is the failure mode this
# repository keeps getting bitten by — the vacuous UI check, the `channel: null`
# refresh, the shard regex that matched nothing — so what it did has to be said
# out loud, the way sync_catalog.py says what each conference dropped and why.
# Both index halves ask about every talk, hence a dict rather than a list.
HELD_BACK: dict[str, str] = {}


def held_back(words: int, duration_min: int | None) -> str | None:
    """Why this transcript must not be indexed as content, or None."""
    if words and duration_min and duration_min >= MIN_RATED_MINUTES:
        wpm = words / duration_min
        if wpm < MIN_WPM:
            return f"{words} words over {duration_min} min = {wpm:.1f} wpm"
    return None


def index_length(toks: list[str], words: int) -> int:
    """Document length for BM25, in a script the tokeniser may not read."""
    if words and len(toks) < TOKEN_SHARE_FLOOR * words:
        return max(len(toks), round(TOKENS_PER_WORD * words))
    return len(toks)


def transcript_text(vid: str, duration_min: int | None = None) -> tuple[str, list[dict], int]:
    """Text, passages and word count — or three empty values.

    The word count is zeroed along with the text, not kept. It is what reaches
    search-meta.json as `w`, and the browser gates the transcript badge, the
    has-transcript filter and the "Find this in the talk" link on `w` rather
    than on any text it holds; returning a live count with no text would leave a
    deep link into 150 words of fragments.
    """
    tr = atu.load_transcript(vid)
    if not tr:
        return "", [], 0
    segs = tr.get("segments", [])
    words = tr.get("word_count", 0)
    why = held_back(words, duration_min)
    if why:
        HELD_BACK[vid] = why
        return "", [], 0
    return " ".join(s["text"] for s in segs), to_passages(segs), words


def clip(text: str, n: int) -> str:
    if len(text or "") <= n:
        return text or ""
    return text[:n].rsplit(" ", 1)[0].rstrip(" ,.;:-") + "…"


def build_sqlite(talks: list[dict]) -> tuple[int, int]:
    if atu.TALKS_DB.exists():
        atu.TALKS_DB.unlink()
    con = sqlite3.connect(atu.TALKS_DB)
    con.executescript(SCHEMA)

    n_tr = 0
    seg_rowid = 0
    for n, t in enumerate(talks, 1):
        text, segs, words = transcript_text(t["id"], t["duration_min"])
        if text:
            n_tr += 1
        speakers = ", ".join(t["speakers"])
        tags = ", ".join(t["tags"])
        con.execute(
            "INSERT INTO talks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (n, t["id"], t["title"], t["description"], speakers, t["conference"],
             t["conference_name"], t["category"], t["edition"], t["year"], t["channel"],
             tags, t["duration_min"], t["published_at"], t["youtube_url"],
             t["availability"], t["priority"], 1 if text else 0, words),
        )
        con.execute(
            "INSERT INTO talks_fts (rowid, title, description, tags, speakers, conference_name)"
            " VALUES (?,?,?,?,?,?)",
            (n, t["title"], t["description"], tags, speakers, t["conference_name"]),
        )
        for s in segs:
            seg_rowid += 1
            con.execute("INSERT INTO segments VALUES (?,?,?,?)",
                        (seg_rowid, n, s["start"], s["text"]))

    con.execute("INSERT INTO segments_fts(segments_fts) VALUES('rebuild')")
    con.commit()
    con.execute("VACUUM")
    con.close()
    return n_tr, seg_rowid


# --- browser index -----------------------------------------------------------

def shard_char(c: str) -> str:
    """One character of a shard name. Must agree exactly with index.html.

    The two implementations are the same three lines in two languages, and a
    disagreement is silent: the browser asks for a shard the manifest does not
    list, finds nothing, and transcript search quietly returns metadata hits
    only. TOKEN_RE starts every term with [a-z0-9], so only the second
    character ever reaches the fallback — "c++" and "c#" both shard as "c_".
    """
    if "a" <= c <= "z":
        return c
    if "0" <= c <= "9":
        return "0"
    return "_"


def shard_key(term: str) -> str:
    """Two characters, because one letter put every "s" term in a 4 MB file.

    Terms that share a prefix have to share a shard: the browser resolves
    "agent" -> "agentic" by scanning the keys of the one shard it fetched, so
    splitting a prefix across shards would silently stop matching rather than
    fail. Two characters is the deepest split that keeps that guarantee for
    free, since tokenize() drops anything shorter than two characters and the
    shortest possible query term is therefore exactly a whole key.
    """
    return shard_char(term[0]) + shard_char(term[1])


B36 = "0123456789abcdefghijklmnopqrstuvwxyz"


def b36(n: int) -> str:
    if n == 0:
        return "0"
    out = ""
    while n:
        n, r = divmod(n, 36)
        out = B36[r] + out
    return out


def encode_positions(seg_ids: list[int]) -> str:
    """Passage indices as base36 gaps: [3, 5, 12] -> "3.2.7".

    These are what let the browser tell a talk that says the query terms inside
    one passage from a talk that merely says each of them somewhere — the whole
    difference between its ranking and query.py's.
    """
    prev, parts = 0, []
    for i in seg_ids:
        parts.append(b36(i - prev))
        prev = i
    return ".".join(parts)


def build_browser_index(talks: list[dict], desc_chars: int = META_DESC_CHARS) -> dict:
    meta = []
    postings: dict[str, dict[int, int]] = collections.defaultdict(dict)
    positions: dict[str, dict[int, list[int]]] = collections.defaultdict(dict)
    doc_len: dict[int, int] = {}

    for n, t in enumerate(talks, 1):
        text, segs, words = transcript_text(t["id"], t["duration_min"])
        meta.append({
            "i": n,
            "v": t["video_id"],
            "t": t["title"],
            "d": clip(t["description"], desc_chars),
            "s": t["speakers"],
            "c": t["conference_name"],
            "cs": t["conference"],
            "g": t["category"],
            "e": t["edition"],
            "y": t["year"],
            "m": t["duration_min"],
            "a": t["tags"],
            "p": t["published_at"],
            "u": t["conference_site"],
            "w": words,
        })
        if not text:
            continue
        toks = atu.tokenize(text)
        doc_len[n] = index_length(toks, words)
        for term, tf in collections.Counter(toks).items():
            postings[term][n] = tf
        for i, s in enumerate(segs):
            for term in set(atu.tokenize(s["text"])):
                positions[term].setdefault(n, []).append(i)

    atu.write_json(atu.SEARCH_META, {"talks": meta}, compact=True)

    if atu.TINDEX.exists():
        shutil.rmtree(atu.TINDEX)
    if not postings:
        return {"terms": 0, "shards": 0, "docs": 0}

    n_docs = len(doc_len)
    avg_len = sum(doc_len.values()) / n_docs

    shards: dict[str, dict] = collections.defaultdict(dict)
    for term, docs in postings.items():
        if len(docs) == 1 and max(docs.values()) < 2:
            continue  # a term used once in one talk is noise, not a search key
        idf = math.log(1 + (n_docs - len(docs) + 0.5) / (len(docs) + 0.5))
        pos = positions.get(term, {})
        shards[shard_key(term)][term] = {
            "f": round(idf, 4),
            "p": [[tid, tf, encode_positions(pos.get(tid, []))]
                  for tid, tf in sorted(docs.items(), key=lambda kv: -kv[1])],
        }

    for key, terms in shards.items():
        atu.write_json(atu.TINDEX / f"{key}.json", terms, compact=True)

    atu.write_json(atu.TINDEX / "_manifest.json", {
        "shards": sorted(shards),
        "n_docs": n_docs,
        "avg_doc_len": round(avg_len, 2),
        "doc_len": doc_len,
        "stopwords": sorted(atu.STOPWORDS),
    }, compact=True)
    return {"terms": sum(len(v) for v in shards.values()), "shards": len(shards), "docs": n_docs}


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="build_index.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("-o", "--out", metavar="DIR", type=pathlib.Path,
                    help="write talks.db, search-meta.json and tindex/ into DIR instead "
                         "of data/ (the inputs are still read from data/), for building "
                         "a copy to diff against the committed one")
    ap.add_argument("-q", "--quiet", action="store_true",
                    help="print nothing except a search-meta.json that is over its "
                         "size trigger")
    ap.add_argument("--desc-chars", type=int, default=META_DESC_CHARS, metavar="N",
                    help=f"clip descriptions in search-meta.json to N characters "
                         f"(default: {META_DESC_CHARS}); halving it is the remedy when "
                         f"the file crosses the {META_SIZE_TRIGGER_BYTES // (1024 * 1024)}"
                         f" MiB trigger")
    args = ap.parse_args(argv)
    if args.desc_chars < 1:
        ap.error("--desc-chars must be at least 1")
    return args


def redirect_outputs(out: pathlib.Path) -> None:
    """Point the three generated artefacts somewhere other than data/.

    Only the outputs move: talks.json and the transcripts are still read from
    the repository, because the point is to rebuild the same corpus elsewhere
    and compare. Both halves still get built together, which is what keeps the
    dense `n` meaning the same thing in the database and in the browser index.
    """
    atu.TALKS_DB = out / "talks.db"
    atu.SEARCH_META = out / "search-meta.json"
    atu.TINDEX = out / "tindex"


def main(argv: list[str] | None = None) -> None:
    """Build both indexes.

    argv defaults to *no arguments* rather than to sys.argv[1:], because
    query.py imports this module and calls main() to build the index on first
    use — it must not have its own command line parsed here.
    """
    args = parse_args(list(argv or []))
    if args.out:
        redirect_outputs(args.out)

    talks = atu.load_talks()
    n_tr, n_seg = build_sqlite(talks)
    stats = build_browser_index(talks, args.desc_chars)
    meta_size = atu.SEARCH_META.stat().st_size

    if args.quiet:
        if meta_size >= META_SIZE_TRIGGER_BYTES:
            print(meta_size_report(meta_size, args.desc_chars))
        return

    print(f"indexed {len(talks)} talks · {n_tr} with transcripts · {n_seg:,} passages")
    if HELD_BACK:
        print(f"  {len(HELD_BACK)} transcript(s) held back below the {MIN_WPM} wpm floor "
              f"— the files are kept, they are just not indexed as content:")
        for vid in sorted(HELD_BACK):
            print(f"    {vid}  {HELD_BACK[vid]}")
    print(f"  data/talks.db          {atu.human_size(atu.TALKS_DB.stat().st_size)}")
    print(f"  data/search-meta.json  {atu.human_size(meta_size)}")
    if stats["shards"]:
        total = sum(p.stat().st_size for p in atu.TINDEX.glob("*.json"))
        print(f"  data/tindex/           {atu.human_size(total)} in {stats['shards']} shards, "
              f"{stats['terms']:,} terms over {stats['docs']} transcripts")
    else:
        print("  data/tindex/           (empty — no transcripts fetched yet)")
    print(f"\n{meta_size_report(meta_size, args.desc_chars)}")


if __name__ == "__main__":
    main(sys.argv[1:])
