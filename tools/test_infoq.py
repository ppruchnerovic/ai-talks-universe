#!/usr/bin/env python3
"""Offline checks for infoq.py — no network.

What is worth testing here is the two decisions that are expensive and quiet.

Matching is the first: a wrong merge writes one talk's transcript onto another
talk's record, and nothing downstream would ever flag it — the record looks
complete, it just quotes the wrong speaker. A missed merge only costs a
duplicate, so the matcher is allowed to be shy and is not allowed to be wrong.

Parsing is the second: these pages are the only source in the corpus whose
transcript comes out of HTML rather than a caption API, so a template change on
InfoQ's side shows up as an empty or a truncated transcript, and a truncated
one is indistinguishable from a short talk unless something checks.

    cd tools && python3 test_infoq.py
"""

import sys

sys.path.insert(0, ".")
import atu
import infoq as I

FAILS = []


def check(label, cond, detail=None):
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond:
        FAILS.append(label)
        if detail is not None:
            print(f"       {detail!r}")


# --- matching ----------------------------------------------------------------

CAT = {"videos": {
    "aaaaaaaaaaa": {"title": "Scaling to 100+ as a Director: Lessons from Growing "
                             "Engineering Organizations - Thiago Ghisi - QCon"},
    "bbbbbbbbbbb": {"title": "State of Play: AI Coding Assistants"},
    "ccccccccccc": {"title": "The Future of AI"},
    "ddddddddddd": {"title": "The Future of AI Agents"},
    # Long enough to clear MIN_PREFIX, so what these two test is the ambiguity
    # rule and not the length guard.
    "eeeeeeeeeee": {"title": "Building Reliable Distributed Systems - Alice Smith - QCon"},
    "fffffffffff": {"title": "Building Reliable Distributed Systems in Practice - Bob Jones"},
    "iq-already-here": {"title": "State of Play: AI Coding Assistants"},
}}
BY_KEY = I.catalog_index(CAT)

check("an iq- record is never a match target — it is this route's own output",
      "iq-already-here" not in BY_KEY.values(), BY_KEY)

check("an exact title matches",
      I.match_existing(I.title_key("State of Play: AI Coding Assistants"), BY_KEY)
      == "bbbbbbbbbbb")

check("punctuation and case do not matter",
      I.match_existing(I.title_key("state of play — ai coding assistants"), BY_KEY)
      == "bbbbbbbbbbb")

check("a YouTube title with the speaker and conference appended still matches",
      I.match_existing(
          I.title_key("Scaling to 100+ as a Director: Lessons from Growing "
                      "Engineering Organizations"), BY_KEY) == "aaaaaaaaaaa")

check("a title too short to identify a talk does not match on its prefix",
      I.match_existing(I.title_key("The Future"), BY_KEY) is None)

# A prefix of two catalogue titles and an exact match for neither. Merging onto
# either is a coin flip, and the loser gets another talk's transcript.
check("an ambiguous prefix matches nothing rather than guessing",
      I.match_existing(I.title_key("Building Reliable Distributed Systems"), BY_KEY) is None,
      I.match_existing(I.title_key("Building Reliable Distributed Systems"), BY_KEY))

# "The Future of AI" is also a prefix of "The Future of AI Agents", but it is a
# title in its own right and the catalogue holds it exactly. An exact match is
# never given up in favour of an ambiguity.
check("an exact match wins over a prefix that would have been ambiguous",
      I.match_existing(I.title_key("The Future of AI"), BY_KEY) == "ccccccccccc")

check("an unrelated title matches nothing",
      I.match_existing(I.title_key("Rewriting All of Spotify's Code Base"), BY_KEY) is None)

check("title_key does not truncate, so two long titles sharing 60 characters differ",
      I.title_key("Building Reliable Distributed Systems at Enormous Scale: Part One")
      != I.title_key("Building Reliable Distributed Systems at Enormous Scale: Part Two"))


# --- parsing -----------------------------------------------------------------

PAGE = '''<html><head>
<meta property="og:title" content="Can Claude Fix Itself?"/>
<meta property="og:description" content="A summary sentence." />
<script type="application/ld+json">
{"@type":"NewsArticle","headline":"Can Claude Fix Itself?",
 "datePublished":"2026-08-26T11:00:00+0000",
 "author":[{"@type":"Person","name":"Alex Palcuie"}],
 "video":{"duration":"PT45M17S","contentUrl":"https://videog.infoq.com/x.mp4"}}
</script></head><body>
<div class="summary"><h2 class="heading">Summary</h2><p>A summary sentence.</p></div>
<div data-nosnippet class="bio"><h2 class="heading">Bio</h2><p>Alex works at Anthropic.</p></div>
<div id="presentationNotes">
  <h2 class="expanded">Transcript</h2>
  <p><strong>Alex Palcuie:</strong> I&#39;m Alex.</p>
  <div class="pullquote"><p>A nested block that used to end the scrape early.</p></div>
  <h2 class="expanded">Can Claude Fix Your Incidents?</h2>
  <p>Then you ask the one question. And here is a second sentence in the same
     paragraph. And a third one, so the split has something to do.</p>
  <p>See more presentations with transcripts</p>
</div>
<div class="related">Not part of the transcript.</div>
</body></html>'''

talk = I.parse_talk(PAGE, {"slug": "x", "page_url": "u", "has_transcript": True})

check("the title comes off the page", talk["title"] == "Can Claude Fix Itself?", talk["title"])
check("the speaker comes from ld+json, not a guess at the title",
      talk["speakers"] == ["Alex Palcuie"], talk["speakers"])
check("an ISO 8601 duration becomes seconds",
      talk["duration_s"] == 45 * 60 + 17, talk["duration_s"])
check("the bio is folded into the description, which is this corpus's abstract",
      "Alex works at Anthropic." in talk["description"], talk["description"])
check("the publish date is kept — it is InfoQ's, and is not the talk's year",
      talk["published_at"] == "2026-08-26T11:00:00+0000")

lines = talk["transcript_lines"]
check("InfoQ's own 'Transcript' label is not part of the transcript",
      "Transcript" not in lines, lines)
check("the speaker label survives into the text",
      lines and lines[0] == "Alex Palcuie: I'm Alex.", lines[:1])
check("a nested div does not truncate the transcript — the section after it is kept",
      "Then you ask the one question." in lines, lines)
check("the talk's own section headings are kept as structure",
      "Can Claude Fix Your Incidents?" in lines, lines)
check("markup outside the transcript container stays out",
      not any("Not part of the transcript" in l for l in lines), lines)

check("a page with no transcript container yields no lines, not a crash",
      I.parse_transcript("<html><body><p>nothing</p></body></html>") == [])

# This link sits inside the transcript container on every presentation on the
# site. Indexed as speech it is noise with a high term frequency, and it would
# be quoted back as if the speaker had said it.
check("InfoQ's own footer link is not part of the talk",
      not any("See more presentations" in l for l in lines), lines[-3:])

# InfoQ writes 200-word paragraphs. A segment is the unit a search hit is
# reported at, so one paragraph per segment is a coarse hit and a coarse deep
# link where the rest of the corpus resolves to about 25 words.
check("a multi-sentence paragraph is split, not kept as one 200-word block",
      "Then you ask the one question." in lines
      and "And here is a second sentence in the same paragraph." in lines, lines)
check("and no line is anywhere near a whole paragraph",
      max(len(l.split()) for l in lines) < 40, max(lines, key=lambda l: len(l.split())))

# A real page, end to end: 45:17 of talk, and the last thing said should land
# near the end of it rather than at the start or past the finish.
_real = atu.segment_plain_text(lines, 2717)
check("interpolated starts span the runtime without overrunning it",
      _real and 0.0 == _real[0]["start"] and _real[-1]["start"] < 2717,
      (_real[0]["start"], _real[-1]["start"]) if _real else None)


# --- timings -----------------------------------------------------------------

segs = atu.segment_plain_text(["word " * 40, "other " * 40], 600)
check("untimed prose becomes segments", len(segs) >= 2, len(segs))
check("starts are monotonic", all(a["start"] <= b["start"] for a, b in zip(segs, segs[1:])))
check("the first start is at the top of the talk", segs[0]["start"] == 0.0, segs[0])
check("the last start is inside the runtime", segs[-1]["start"] < 600, segs[-1])
check("no runtime still gives orderable starts rather than a divide by zero",
      [s["start"] for s in atu.segment_plain_text(["a " * 40, "b " * 40], 0)] == [0.0, 40.0],
      atu.segment_plain_text(["a " * 40, "b " * 40], 0))
check("empty input is empty output", atu.segment_plain_text([], 600) == [])


# --- the id namespace --------------------------------------------------------

# Both of these are real InfoQ slugs, and both land on exactly 11 characters of
# the URL-safe alphabet — which is precisely what a YouTube id looks like. They
# were each handed a youtube.com/watch?v=iq-green-it that leads nowhere.
check("a short InfoQ id is not mistaken for a YouTube id, at 11 characters",
      len("iq-rag-vllm") == 11 and not atu.is_youtube_id("iq-rag-vllm")
      and not atu.is_youtube_id("iq-green-it"))
check("so it gets its own page as a link, never a watch URL",
      atu.watch_url("iq-green-it", "https://www.infoq.com/presentations/green-it/")
      == "https://www.infoq.com/presentations/green-it/")
check("and a real YouTube id still resolves to a watch URL",
      atu.watch_url("-1_KvpNDC6k") == "https://www.youtube.com/watch?v=-1_KvpNDC6k")
check("a record with neither an id nor a page has no link, not a broken one",
      atu.watch_url("iq-whatever") is None)


# --- the edition year, which is the whole point of this route ----------------

check("an edition slug's trailing year is the year of every talk under it",
      I.EDITION_YEAR_RE.search("qcon-london-2026").group(1) == "2026")
check("a topic tag that is not an edition carries no year and is skipped",
      I.EDITION_YEAR_RE.search("infoq-editors") is None
      and I.EDITION_YEAR_RE.search("qcon") is None)

TAGS = '''<a href='/qcon-ai-boston-2026/presentations/' class="tag">QCon AI Boston 2026</a>
<a href='/qcon/presentations/' class="tag">QCon</a>
<a href='/infoq-live-june-2026/presentations/' class="tag">InfoQ Live - June 2026</a>'''
found = [(s, n) for s, n in I.EDITION_TAG_RE.findall(TAGS)]
check("the edition list parses off the index page", len(found) == 3, found)
check("and the display name is kept — 'qcon-ai-2025' is 'QCon AI New York 2025'",
      found[0][1] == "QCon AI Boston 2026", found[0])


# --- folding the cache into the catalogue: sync_catalog's half -------------
#
# Three ways the fold-in was fragile, each verified in the 2026-09-02 review:
# a channel refresh stripped what infoq.py had written onto a matched record,
# a missing cache directory deleted every iq- record, and a talk fetched as
# iq- that later reached the YouTube channel stayed a permanent duplicate.

import json
import tempfile
import pathlib
import sync_catalog as S

SRC = {"url": "https://www.youtube.com/@InfoQ", "label": "InfoQ channel", "year": None}
prev = {"video_id": "aaaaaaaaaaa", "title": "Scaling to 100+ - Thiago Ghisi - QCon",
        "source_url": SRC["url"], "label": "InfoQ channel", "year": None,
        "description": "InfoQ's abstract", "speakers": ["Thiago Ghisi"],
        "label": "QCon San Francisco 2025", "year": 2025, "page_url": "https://www.infoq.com/p/x/",
        "infoq_url": "https://www.infoq.com/p/x/", "infoq_at": "2026-09-01T00:00:00+00:00",
        "details_at": "2026-09-01T00:00:00+00:00", "published_at": "2026-02-01T00:00:00Z"}
videos = {"aaaaaaaaaaa": dict(prev)}
listing = [{"video_id": "aaaaaaaaaaa", "title": "Scaling to 100+ - Thiago Ghisi - QCon",
            "duration_s": 3000, "channel": "InfoQ", "label": "InfoQ channel", "year": None,
            "source_url": SRC["url"]}]
S.merge_source(videos, SRC, listing)
after = videos["aaaaaaaaaaa"]
check("a channel refresh keeps the edition infoq.py resolved, not the listing's label",
      after["label"] == "QCon San Francisco 2025" and after["year"] == 2025, after)
check("and keeps the speakers, the page and the claim stamp",
      after["speakers"] == ["Thiago Ghisi"] and after["page_url"] == prev["page_url"]
      and after["infoq_at"] == prev["infoq_at"] and after["description"] == "InfoQ's abstract",
      after)
check("while the listing still refreshes what it is the source for",
      after["duration_s"] == 3000 and after["channel"] == "InfoQ", after)

plain = {"bbbbbbbbbbb": {"video_id": "bbbbbbbbbbb", "title": "Unclaimed", "source_url": SRC["url"],
                         "label": "old label", "year": 2024, "description": "enriched"}}
S.merge_source(plain, SRC, [{"video_id": "bbbbbbbbbbb", "title": "Unclaimed", "label": "new label",
                             "year": 2025, "source_url": SRC["url"]}])
check("a record infoq.py never claimed takes the listing's label and year as before",
      plain["bbbbbbbbbbb"]["label"] == "new label" and plain["bbbbbbbbbbb"]["year"] == 2025
      and plain["bbbbbbbbbbb"]["description"] == "enriched", plain)

# The stale guard: an empty cache directory keeps what it previously gave.
with tempfile.TemporaryDirectory() as tmp:
    saved_cache, saved_catalog = S.INFOQ_CACHE, atu.CATALOG
    S.INFOQ_CACHE = pathlib.Path(tmp) / "infoq-missing"
    atu.CATALOG = pathlib.Path(tmp) / "catalog"
    atu.CATALOG.mkdir()
    isrc = {"type": "infoq", "url": "https://www.infoq.com/presentations/", "label": "InfoQ"}
    reg = {"conferences": [{"slug": "qcon-infoq", "name": "QCon", "sources": [isrc]}]}
    atu.write_json(atu.catalog_path("qcon-infoq"), {"slug": "qcon-infoq", "videos": {
        "iq-kept-talk": {"video_id": "iq-kept-talk", "title": "Kept", "source_url": isrc["url"]},
        "ccccccccccc": {"video_id": "ccccccccccc", "title": "Channel", "source_url": SRC["url"]}}})
    S.sync_infoq(reg)
    cat = atu.load_catalog("qcon-infoq")
    check("a missing InfoQ cache keeps the iq- records it previously contributed",
          "iq-kept-talk" in cat["videos"], sorted(cat["videos"]))
    check("and marks the source stale rather than counting zero",
          any(m.get("stale") and m.get("type") == "infoq" for m in cat["sources"]), cat["sources"])
    S.INFOQ_CACHE, atu.CATALOG = saved_cache, saved_catalog

# Two-way dedupe: an iq- record whose talk has since reached the channel.
with tempfile.TemporaryDirectory() as tmp:
    saved_tr = atu.TRANSCRIPTS
    atu.TRANSCRIPTS = pathlib.Path(tmp)
    atu.write_json(atu.transcript_path("iq-late-talk"),
                   {"video_id": "iq-late-talk", "timing": "estimated", "word_count": 2,
                    "segments": [{"start": 0, "duration": 1, "text": "hello there"}]}, compact=True)
    vids = {"ddddddddddd": {"video_id": "ddddddddddd", "source_url": SRC["url"],
                            "title": "A Talk That Reached YouTube Later - Some Speaker - QCon",
                            "label": "InfoQ channel", "year": None}}
    found = [{"video_id": "iq-late-talk", "title": "A Talk That Reached YouTube Later",
              "description": "the abstract", "speakers": ["Some Speaker"], "label": "QCon London 2026",
              "year": 2026, "page_url": "https://www.infoq.com/presentations/late/",
              "source_url": isrc["url"], "details_at": "2026-09-02T00:00:00+00:00"},
             {"video_id": "iq-still-only-infoq", "title": "Nothing Like It On The Channel",
              "label": "QCon London 2026", "year": 2026, "source_url": isrc["url"]}]
    kept, claimed = S.claim_for_infoq(vids, found)
    check("an iq- talk that later reached the channel is folded onto the YouTube record",
          claimed == 1 and [r["video_id"] for r in kept] == ["iq-still-only-infoq"], kept)
    yt = vids["ddddddddddd"]
    check("which then carries the page's abstract, speakers and edition",
          yt.get("description") == "the abstract" and yt.get("speakers") == ["Some Speaker"]
          and yt.get("label") == "QCon London 2026" and yt.get("year") == 2026
          and yt.get("infoq_at"), yt)
    check("and its transcript, re-keyed to the video id",
          atu.transcript_path("ddddddddddd").exists()
          and json.loads(atu.transcript_path("ddddddddddd").read_text())["video_id"] == "ddddddddddd")
    kept2, claimed2 = S.claim_for_infoq(vids, found)
    check("running it again changes nothing", claimed2 == 1 and len(kept2) == 1
          and vids["ddddddddddd"] == yt)
    atu.TRANSCRIPTS = saved_tr


print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else "all checks passed"))
sys.exit(1 if FAILS else 0)
