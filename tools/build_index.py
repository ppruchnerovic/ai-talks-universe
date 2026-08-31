#!/usr/bin/env python3
"""Build the search indexes from data/talks.json + data/transcripts/.

Two independent indexes from the same corpus:

  data/talks.db          SQLite + FTS5, used by query.py and by anything that
                         can open a database. Includes a per-passage index, so
                         a hit points at the exact second in the video.

  data/search-meta.json  Every talk's metadata + description, compact keys.
  data/tindex/*.json     Small enough for a browser to load up front. The
  data/tindex/_manifest  transcript inverted index is sharded by first letter
                         and fetched lazily, so the site needs no backend.

    python3 build_index.py
"""

from __future__ import annotations

import collections
import json
import math
import shutil
import sqlite3

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

# How much of a description reaches the browser's up-front payload. The full
# text stays in talks.json, the markdown and talks.db; this only caps what every
# visitor downloads before typing anything. YouTube descriptions run long and
# repetitive (the same channel boilerplate under 400 talks), so the tail is
# mostly cost.
META_DESC_CHARS = 600


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


def transcript_text(vid: str) -> tuple[str, list[dict], int]:
    tr = atu.load_transcript(vid)
    if not tr:
        return "", [], 0
    segs = tr.get("segments", [])
    return " ".join(s["text"] for s in segs), to_passages(segs), tr.get("word_count", 0)


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
        text, segs, words = transcript_text(t["id"])
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

def shard_key(term: str) -> str:
    c = term[0]
    if c.isalpha():
        return c
    if c.isdigit():
        return "0"
    return "_"


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


def build_browser_index(talks: list[dict]) -> dict:
    meta = []
    postings: dict[str, dict[int, int]] = collections.defaultdict(dict)
    positions: dict[str, dict[int, list[int]]] = collections.defaultdict(dict)
    doc_len: dict[int, int] = {}

    for n, t in enumerate(talks, 1):
        text, segs, words = transcript_text(t["id"])
        meta.append({
            "i": n,
            "v": t["video_id"],
            "t": t["title"],
            "d": clip(t["description"], META_DESC_CHARS),
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
        doc_len[n] = len(toks)
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


def main() -> None:
    talks = atu.load_talks()
    n_tr, n_seg = build_sqlite(talks)
    stats = build_browser_index(talks)

    print(f"indexed {len(talks)} talks · {n_tr} with transcripts · {n_seg:,} passages")
    print(f"  data/talks.db          {atu.human_size(atu.TALKS_DB.stat().st_size)}")
    print(f"  data/search-meta.json  {atu.human_size(atu.SEARCH_META.stat().st_size)}")
    if stats["shards"]:
        total = sum(p.stat().st_size for p in atu.TINDEX.glob("*.json"))
        print(f"  data/tindex/           {atu.human_size(total)} in {stats['shards']} shards, "
              f"{stats['terms']:,} terms over {stats['docs']} transcripts")
    else:
        print("  data/tindex/           (empty — no transcripts fetched yet)")


if __name__ == "__main__":
    main()
