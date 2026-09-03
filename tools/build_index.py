#!/usr/bin/env python3
"""Build the search indexes from data/talks.json + data/transcripts/.

Two independent indexes from the same corpus:

  data/talks.db          SQLite + FTS5, used by query.py and by anything that
                         can open a database. Includes a per-passage index, so
                         a hit points at the exact second in the video.

  data/search-meta.json  Every talk's metadata + a display clip of its
                         description, compact keys. Small enough for a
                         browser to load up front.
  data/tindex/*.json     The inverted index — transcript passages and the
  data/tindex/_manifest  full descriptions, stemmed — sharded by the first
                         two letters of a term and fetched lazily, so the
                         site needs no backend.

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
    published_at TEXT, url TEXT, youtube_url TEXT, page_url TEXT,
    availability TEXT, priority INTEGER,
    has_transcript INTEGER, transcript_words INTEGER,
    timing TEXT            -- 'exact' or 'estimated'; NULL without a transcript
);
CREATE INDEX idx_talks_conf ON talks(conference);

-- Content-carrying so snippet()/highlight() work. Metadata and descriptions
-- only; transcript text lives in `segments` and is searched through
-- segments_fts, which is what gives every hit a timestamp.
CREATE VIRTUAL TABLE talks_fts USING fts5(
    title, description, tags, speakers, conference_name,
    tokenize='porter unicode61'
);

-- One row per passage. `pos` is the word offset the passage starts at and
-- `bridge` marks the half-stride tiling that overlaps the primary one — see
-- PASSAGE_STRIDE. Readers that want the transcript back whole take bridge = 0.
CREATE TABLE segments (
    rowid INTEGER PRIMARY KEY, talk_n INTEGER, start REAL, pos INTEGER,
    bridge INTEGER, text TEXT
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
#
# Passages are cut on words, not caption lines, at exactly PASSAGE_WORDS, and
# a second tiling is laid over the first at half a passage's offset. A phrase
# or a pair of terms straddling a boundary of one tiling sits inside a passage
# of the other, so what "said together" catches no longer depends on where the
# cut happened to fall. The SQLite index carries both tilings (`bridge` = 1
# for the offset one) and roughly doubles; the browser index keeps counting
# positions in the primary tiling alone, so tindex/ is unchanged.
PASSAGE_WORDS = 24
PASSAGE_STRIDE = PASSAGE_WORDS // 2

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

# How much of a description reaches the browser's up-front payload — for
# display only. The description's *terms* are all in the sharded index (see
# build_browser_index), so this clip decides what a card shows before "Show
# full description", not what a search can find. The full text stays in
# talks.json, the markdown and talks.db; this only caps what every visitor
# downloads before typing anything.
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
# what 600 -> 300 did when seven new conferences took it to 7.8 MiB. Since the
# description terms moved into the shards, halving it costs a shorter card and
# nothing in recall. The run prints where the file stands against this line
# either way.
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


def timed_words(segs: list[dict]) -> list[tuple[float, str]]:
    """Every word of the transcript with a start, interpolated inside its line.

    A caption line is ~6 words over ~3 seconds, so a passage that begins
    mid-line starts within a second of where it should; an InfoQ segment is
    25 words of prose whose timing was already interpolated, so the error is
    the same one it carried in.
    """
    out = []
    for s in segs:
        ws = s["text"].split()
        if not ws:
            continue
        dur = float(s.get("duration") or 0)
        for i, w in enumerate(ws):
            out.append((s["start"] + dur * i / len(ws), w))
    return out


def to_passages(segs: list[dict]) -> list[dict]:
    """The transcript as overlapping passages: {start, pos, bridge, text}.

    Tile k starts at word PASSAGE_STRIDE * k and runs PASSAGE_WORDS words, so
    even tiles are a plain non-overlapping tiling and odd ones (`bridge`) sit
    across their boundaries. A tail shorter than a stride is not emitted as a
    passage of its own — the previous tile already covers it, and a
    three-word document would outscore everything under BM25's length
    normalisation — unless it is the only tile there is.
    """
    words = timed_words(segs)
    out: list[dict] = []
    for k in range(0, max(1, (len(words) + PASSAGE_STRIDE - 1) // PASSAGE_STRIDE)):
        pos = PASSAGE_STRIDE * k
        if pos >= len(words) or (pos and len(words) - pos < PASSAGE_STRIDE):
            break
        chunk = words[pos:pos + PASSAGE_WORDS]
        out.append({"start": round(chunk[0][0], 2), "pos": pos, "bridge": k % 2,
                    "text": " ".join(w for _, w in chunk)})
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


def transcript_text(vid: str, duration_min: int | None = None) -> tuple[str, list[dict], int, str | None, str | None]:
    """Text, passages, word count, timing and language — or five empty values.

    The word count is zeroed along with the text, not kept. It is what reaches
    search-meta.json as `w`, and the browser gates the transcript badge, the
    has-transcript filter and the "Find this in the talk" link on `w` rather
    than on any text it holds; returning a live count with no text would leave a
    deep link into 150 words of fragments.
    """
    tr = atu.load_transcript(vid)
    if not tr:
        return "", [], 0, None, None
    segs = tr.get("segments", [])
    words = tr.get("word_count", 0)
    why = held_back(words, duration_min)
    if why:
        HELD_BACK[vid] = why
        return "", [], 0, None, None
    return (" ".join(s["text"] for s in segs), to_passages(segs), words,
            tr.get("timing") or "exact", tr.get("language"))


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
        text, segs, words, timing, _lang = transcript_text(t["id"], t["duration_min"])
        if text:
            n_tr += 1
        speakers = ", ".join(t["speakers"])
        tags = ", ".join(t["tags"])
        con.execute(
            "INSERT INTO talks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (n, t["id"], t["title"], t["description"], speakers, t["conference"],
             t["conference_name"], t["category"], t["edition"], t["year"], t["channel"],
             tags, t["duration_min"], t["published_at"], t["url"], t["youtube_url"],
             t["page_url"], t["availability"], t["priority"], 1 if text else 0, words,
             timing if text else None),
        )
        con.execute(
            "INSERT INTO talks_fts (rowid, title, description, tags, speakers, conference_name)"
            " VALUES (?,?,?,?,?,?)",
            (n, t["title"], t["description"], tags, speakers, t["conference_name"]),
        )
        con.executemany("INSERT INTO segments VALUES (?,?,?,?,?,?)",
                        [(seg_rowid + i, n, s["start"], s["pos"], s["bridge"], s["text"])
                         for i, s in enumerate(segs, 1)])
        seg_rowid += len(segs)

    con.execute("INSERT INTO segments_fts(segments_fts) VALUES('rebuild')")
    # Stamped last, so a build that died half-way leaves a file atu.db_stale()
    # reports as v0 rather than one that looks finished.
    con.execute(f"PRAGMA user_version = {atu.DB_SCHEMA_VERSION}")
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
    return shard_char(term[0]) + shard_char(term[1])  # atu.stems() keeps len >= 2


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


def meta_stems(t: dict) -> set[str]:
    """Every stem in a talk's metadata, full description included.

    This is the browser's document frequency for the metadata layer, computed
    here because the browser no longer holds the full description: it sees a
    display clip, and the description's terms reach it through the shards.
    The fields are the ones index.html scores, tokenised the same way.
    """
    parts = (t["title"], " ".join(t["tags"]), " ".join(t["speakers"]),
             f'{t["conference_name"]} {t["edition"] or ""}', t["category"] or "",
             t["description"])
    return set(atu.stems(" ".join(p for p in parts if p)))


def build_browser_index(talks: list[dict], desc_chars: int = META_DESC_CHARS) -> dict:
    """search-meta.json and the shards.

    Everything in the shards is keyed on Porter stems — atu.stem(), which
    index.html reproduces — so "evaluate" and "evaluation" are one key, as
    they are in talks.db. A shard entry carries up to three things:

      f, p   transcript idf and postings, [talk n, tf, passage positions]
      d      description postings, [talk n, tf] — the whole description,
             not the display clip search-meta.json carries
      m      how many talks say the term anywhere in their metadata,
             description included: the browser's idf for that layer

    A term said once in one transcript and in no description is left out, as
    before; a term in even one description is kept, since it was findable
    through the clip and must stay so.
    """
    meta = []
    postings: dict[str, dict[int, int]] = collections.defaultdict(dict)
    positions: dict[str, dict[int, list[int]]] = collections.defaultdict(dict)
    desc_post: dict[str, dict[int, int]] = collections.defaultdict(dict)
    meta_df: collections.Counter = collections.Counter()
    doc_len: dict[int, int] = {}

    for n, t in enumerate(talks, 1):
        text, segs, words, timing, lang = transcript_text(t["id"], t["duration_min"])
        meta_df.update(meta_stems(t))
        for term, tf in collections.Counter(atu.stems(t["description"])).items():
            desc_post[term][n] = tf
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
            # Only for the talks whose link the browser cannot build from "v":
            # InfoQ's own pages. Omitted otherwise, because it would repeat
            # youtube.com/watch?v= on 8,000 records of a file that ships to
            # every visitor.
            **({"l": t["url"]} if not t["youtube_url"] and t["url"] else {}),
            # Only for transcripts whose timings are interpolated from word
            # position rather than read off a caption track, so the moments
            # can say "~12:34" rather than claim a second they never measured.
            **({"x": 1} if text and timing == "estimated" else {}),
            # Only when the fetcher read the transcript as something other
            # than English, so the card can badge it. The dozen "hi" ones are
            # English mis-detected, which is why it is labelled "transcript
            # language" and not "language".
            **({"lg": lang} if text and lang and lang != "en" else {}),
        })
        if not text:
            continue
        toks = atu.stems(text)
        doc_len[n] = index_length(toks, words)
        for term, tf in collections.Counter(toks).items():
            postings[term][n] = tf
        # Positions index the primary tiling only, so the browser's postings
        # are the same size and shape as before the bridge passages existed.
        for i, s in enumerate(p for p in segs if not p["bridge"]):
            for term in set(atu.stems(s["text"])):
                positions[term].setdefault(n, []).append(i)

    atu.write_json(atu.SEARCH_META, {"talks": meta}, compact=True)

    if atu.TINDEX.exists():
        shutil.rmtree(atu.TINDEX)
    if not postings and not desc_post:
        return {"terms": 0, "shards": 0, "docs": 0, "desc_terms": 0}

    n_docs = len(doc_len)
    avg_len = sum(doc_len.values()) / n_docs if n_docs else 0

    shards: dict[str, dict] = collections.defaultdict(dict)
    desc_terms = 0
    # Sorted, so the build is byte-identical run to run — a set's order is not.
    for term in sorted(set(postings) | set(desc_post)):
        docs = postings.get(term, {})
        described = desc_post.get(term, {})
        if not described and len(docs) == 1 and max(docs.values()) < 2:
            continue  # a term said once in one talk is noise, not a search key
        entry: dict = {}
        if docs:
            idf = math.log(1 + (n_docs - len(docs) + 0.5) / (len(docs) + 0.5))
            pos = positions.get(term, {})
            entry["f"] = round(idf, 4)
            entry["p"] = [[tid, tf, encode_positions(pos.get(tid, []))]
                          for tid, tf in sorted(docs.items(), key=lambda kv: -kv[1])]
        if described:
            desc_terms += 1
            entry["d"] = [[tid, tf] for tid, tf in sorted(described.items())]
        if meta_df.get(term):
            entry["m"] = meta_df[term]
        shards[shard_key(term)][term] = entry

    for key, terms in shards.items():
        atu.write_json(atu.TINDEX / f"{key}.json", terms, compact=True)

    atu.write_json(atu.TINDEX / "_manifest.json", {
        "shards": sorted(shards),
        "n_docs": n_docs,
        "avg_doc_len": round(avg_len, 2),
        "doc_len": doc_len,
        "stopwords": sorted(atu.STOPWORDS),
        "synonyms": [list(g) for g in atu.SYNONYMS],
        "stemmed": True,
    }, compact=True)
    return {"terms": sum(len(v) for v in shards.values()), "shards": len(shards),
            "docs": n_docs, "desc_terms": desc_terms}


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
    out.mkdir(parents=True, exist_ok=True)
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
              f"{stats['terms']:,} stems — {stats['desc_terms']:,} of them in descriptions, "
              f"transcript postings over {stats['docs']} talks")
    else:
        print("  data/tindex/           (empty — no transcripts fetched yet)")
    print(f"\n{meta_size_report(meta_size, args.desc_chars)}")


if __name__ == "__main__":
    main(sys.argv[1:])
