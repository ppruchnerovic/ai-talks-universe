#!/usr/bin/env python3
"""Fetch InfoQ's own presentation pages — the transcripts YouTube does not carry.

Every other conference in this corpus is enumerated from YouTube, because
YouTube is the only machine-readable programme it has. InfoQ is the exception:
it publishes its own presentation pages, and each one carries a full
human-edited transcript in the HTML, free, to an anonymous client. That is
worth a separate route, because the YouTube side of the same conference has
353 talks and not one transcript — and every transcript fetched here is a
Supadata credit not spent.

Three things this route does that the YouTube one cannot:

  * EDITIONS, not publish dates. InfoQ drips a conference's recordings out for
    a year afterwards, so `datePublished` is when the video went up, not when
    the talk was given: of ten presentations posted in 2026, nine were recorded
    at QCon San Francisco 2025, QCon London 2025 or QCon AI New York 2025. The
    year of a talk here is the year of the edition it was listed under —
    /qcon-london-2026/presentations/ — which is a fact about the programme
    rather than about InfoQ's publishing queue.

  * TRANSCRIPTS, free. In div#presentationNotes, as prose paragraphs under the
    talk's own section headings. There are no caption timings, so starts are
    interpolated from word position across the runtime exactly as the kome.ai
    route does, and marked "estimated" so nothing downstream presents them as
    exact.

  * DEDUP against what YouTube already gave us. A talk that InfoQ also put on
    its channel is not a second corpus record: it keeps its YouTube id, so the
    video stays watchable and its transcript stays upgradable to exact timings,
    and this run writes the transcript and the better metadata onto the record
    that is already there — the same thing enrich.py does, from a better
    source. Only a talk YouTube never listed becomes a new record, under an
    `iq-` id.

    python3 infoq.py --year 2026              # the 2026 editions, metadata + transcripts
    python3 infoq.py --list                    # what editions exist, and how big
    python3 infoq.py --edition qcon-london-2026
    python3 infoq.py --year 2026 --limit 5     # a taste before the full run
    python3 infoq.py --year 2026 --dry-run     # enumerate and match, fetch nothing

Afterwards:  python3 sync_catalog.py && python3 build_index.py

robots.txt allows /presentations/ and asks for Crawl-delay: 3, which is the
default pace here. Please do not lower it.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html as htmllib
import json
import random
import re
import sys
import time
import urllib.error
import urllib.request

import atu

BASE = "https://www.infoq.com"
INDEX = f"{BASE}/presentations/"
CACHE = atu.DATA / "infoq"

# The conference this route feeds. InfoQ's presentations *are* QCon's and the
# Dev Summits' recordings, so they belong to the registry entry that already
# holds them rather than to a second one that would split the same programme.
CONF = "qcon-infoq"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")

# robots.txt: "Crawl-delay: 3". This is a courtesy floor, not a rate limit to
# tune down — the whole 2026 run is ~200 requests either way.
PACE = 3.0


def get(url: str, tries: int = 4, timeout: int = 60) -> str:
    """One GET, retried on the transient failures, decoded as text."""
    last: Exception | None = None
    for attempt in range(tries):
        if attempt:
            time.sleep(2 ** attempt + random.uniform(0, 1.5))
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            })
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                raise                      # a real answer; retrying cannot help
            last = e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
    raise last if last else RuntimeError(f"unreachable: {url}")


# --- turning markup into text ------------------------------------------------

def text_of(fragment: str) -> str:
    """Tag soup to a single line of readable text."""
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", fragment, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return " ".join(htmllib.unescape(s).split())


def div_inner(page: str, start: int) -> str:
    """The inner HTML of the <div> opening at `start`, matching nested divs.

    A regex to the next </div> stops at the first nested one, which on these
    pages truncates the transcript at its first blockquote or figure.
    """
    i = page.index(">", start) + 1
    depth = 1
    for m in re.finditer(r"<(/?)div\b", page[i:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return page[i:i + m.start()]
    return page[i:]


def div_by_class(page: str, cls: str) -> str | None:
    m = re.search(r'<div\b[^>]*\bclass="[^"]*\b' + re.escape(cls) + r'\b[^"]*"', page)
    return div_inner(page, m.start()) if m else None


def div_by_id(page: str, ident: str) -> str | None:
    m = re.search(r'<div\b[^>]*\bid="' + re.escape(ident) + r'"', page)
    return div_inner(page, m.start()) if m else None


# --- editions ----------------------------------------------------------------

# The index page carries the edition filter list: one tag per conference
# edition, newest first, each linking to its own presentations listing.
EDITION_TAG_RE = re.compile(
    r"""href=['"]/([a-z0-9-]+)/presentations/['"]\s+class="tag">\s*([^<]+?)\s*<""")

# An edition slug ends in its year. `qcon` and `infoq-editors` are topic tags
# that sit in the same list and are not editions; requiring the year is what
# tells them apart, and it is also where the year of every talk comes from.
EDITION_YEAR_RE = re.compile(r"-(20\d\d)$")


def editions() -> list[dict]:
    page = get(INDEX)
    out, seen = [], set()
    for slug, name in EDITION_TAG_RE.findall(page):
        m = EDITION_YEAR_RE.search(slug)
        if not m or slug in seen:
            continue
        seen.add(slug)
        out.append({"slug": slug, "name": htmllib.unescape(name), "year": int(m.group(1))})
    return out


# One <li> per listed presentation. `data-transcript` is InfoQ's own flag for
# "this one has a transcript", so a listing tells us what a run is worth before
# it costs a single page fetch.
ITEM_RE = re.compile(
    r'<li\b[^>]*\bdata-path="/presentations/([a-z0-9-]+)"([^>]*)>')


def enumerate_edition(slug: str, pace: float) -> list[dict]:
    """Every presentation listed under one edition, paging 12 at a time.

    Pages past the end still render — with the surrounding furniture and no
    items — so the loop stops when a page adds nothing new rather than on a
    404 that never comes.
    """
    found: dict[str, dict] = {}
    offset = 0
    while True:
        url = f"{BASE}/{slug}/presentations/" + (f"{offset}/" if offset else "")
        page = get(url)
        new = 0
        for talk_slug, attrs in ITEM_RE.findall(page):
            if talk_slug in found:
                continue
            found[talk_slug] = {
                "slug": talk_slug,
                "page_url": f"{BASE}/presentations/{talk_slug}/",
                "has_transcript": "data-transcript" in attrs,
            }
            new += 1
        if not new:
            return list(found.values())
        offset += 12
        time.sleep(pace)


# --- one presentation page ---------------------------------------------------

ISO_DUR_RE = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


def iso_duration_s(s: str | None) -> int | None:
    if not s:
        return None
    m = ISO_DUR_RE.fullmatch(s.strip())
    if not m:
        return None
    h, mi, sec = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + sec or None


def og(page: str, prop: str) -> str | None:
    m = re.search(r'<meta property="og:' + prop + r'" content="(.*?)"\s*/?>', page, re.S)
    return htmllib.unescape(m.group(1)).strip() if m else None


def ld_json(page: str) -> dict:
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
        try:
            d = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(d, dict) and d.get("headline"):
            return d
    return {}


# InfoQ's own furniture, inside the transcript container and not part of the
# talk. Indexed as speech it is the same sentence under every presentation on
# the site — noise with a high term frequency, and it would be quoted back as
# if the speaker had said it.
FURNITURE_RE = re.compile(
    r"^(see more presentations(?: with transcripts)?|recorded at:.*|"
    r"this content is in the .* topic)$", re.I)

# Roughly a sentence. InfoQ's paragraphs run to 200+ words, and a segment is
# the unit a search hit is reported at — one 200-word block is a coarse hit and
# a coarse deep link, where the rest of the corpus resolves to about 25 words.
# Splitting on terminal punctuation and letting segment_plain_text regroup gets
# these back to the same granularity as a caption track.
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[\"\u201c\u2018(]?[A-Z0-9])")


def parse_transcript(page: str) -> list[str]:
    """The transcript as lines: the talk's section headings and its sentences.

    The headings are kept because they are the speaker's own structure — a
    chapter list nothing else in this corpus has — and they read as part of the
    text. The leading "Transcript" heading is InfoQ's label for the section,
    not part of it.
    """
    inner = div_by_id(page, "presentationNotes")
    if not inner:
        return []
    lines = []
    for m in re.finditer(r"<(h2|h3|p)\b[^>]*>(.*?)</\1>", inner, re.S | re.I):
        line = text_of(m.group(2))
        if not line or (not lines and line.lower() == "transcript"):
            continue
        if FURNITURE_RE.match(line):
            continue
        lines.extend(part for part in SENTENCE_RE.split(line) if part.strip())
    return lines


def parse_talk(page: str, rec: dict) -> dict:
    d = ld_json(page)
    video = d.get("video") or {}
    speakers = [htmllib.unescape(a["name"]).strip()
                for a in (d.get("author") or []) if isinstance(a, dict) and a.get("name")]

    summary = text_of(div_by_class(page, "summary") or "")
    summary = re.sub(r"^Summary\s+", "", summary)
    bio = text_of(div_by_class(page, "bio") or "")
    bio = re.sub(r"^Bio\s+", "", bio)
    description = og(page, "description") or summary or d.get("description") or ""
    # The bio is the only place many of these pages say who the speaker is and
    # where they work, and this corpus's descriptions are its abstracts.
    if bio:
        description = f"{description}\n\n{bio}".strip()

    return {
        **rec,
        "title": og(page, "title") or htmllib.unescape(d.get("headline") or "").strip(),
        "description": description,
        "speakers": speakers,
        "duration_s": iso_duration_s(video.get("duration")),
        "published_at": d.get("datePublished"),
        "video_url": video.get("contentUrl"),
        "transcript_lines": parse_transcript(page),
    }


# --- matching against what YouTube already gave us ---------------------------

def title_key(title: str) -> str:
    """A title reduced to the thing two sources would agree on.

    Full length, unlike atu.slugify's default — truncating at 60 characters
    would merge two talks that merely open the same way, and these titles are
    long ("Scaling to 100+ as a Director: Lessons from Growing Engineering
    Organizations").
    """
    return atu.slugify(title, max_len=10 ** 6)


# A YouTube title is the InfoQ one plus, often, the speaker and the edition:
# "…Lessons from Growing Engineering Organizations - Thiago Ghisi - QCon". So a
# prefix match counts, provided the shared part is long enough to identify a
# talk on its own. Below this, prefixes are titles like "the-future-of-ai".
MIN_PREFIX = 30


def match_existing(key: str, by_key: dict[str, str]) -> str | None:
    if key in by_key:
        return by_key[key]
    hits = {vid for k, vid in by_key.items()
            if (len(key) >= MIN_PREFIX and k.startswith(key))
            or (len(k) >= MIN_PREFIX and key.startswith(k))}
    # Two different YouTube records matching one InfoQ title means the prefix
    # was not identifying after all. Leaving it unmatched costs a duplicate
    # record; guessing costs the wrong talk's transcript.
    return hits.pop() if len(hits) == 1 else None


def catalog_index(cat: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for vid, v in cat.get("videos", {}).items():
        if not atu.is_youtube_id(vid):
            continue                      # an iq- record from a previous run
        k = title_key(v.get("title") or "")
        if k and k not in out:
            out[k] = vid
    return out


# --- writing -----------------------------------------------------------------

def save_transcript(vid: str, talk: dict) -> int:
    """One transcript, with starts interpolated across the known runtime.

    Same treatment as the kome.ai route: InfoQ's prose has no timings, so the
    positions are estimates and are labelled as such. Doing it here rather than
    storing untimed text is what lets every reader downstream — the markdown
    deep links, query.py's moments, the browser index — work on these
    unchanged.
    """
    segments = atu.segment_plain_text(talk["transcript_lines"], talk.get("duration_s") or 0)
    words = sum(len(s["text"].split()) for s in segments)
    atu.write_json(atu.transcript_path(vid), {
        "video_id": vid,
        "title": talk["title"],
        "conference": CONF,
        "language": "en",
        "auto_generated": False,       # InfoQ's are edited by hand, not ASR
        "source": "infoq",
        "timing": "estimated",
        "word_count": words,
        "segments": segments,
    }, compact=True)
    return words


# What this route writes onto a catalogue record that YouTube already holds.
# The InfoQ page is the better source for every one of these: a real abstract
# instead of channel boilerplate, the speakers stated instead of guessed off
# the title, and the edition the talk was actually given at.
def enrich_existing(rec: dict, talk: dict, edition: dict, stamp: str) -> None:
    rec["description"] = talk["description"] or rec.get("description") or ""
    if talk["speakers"]:
        rec["speakers"] = talk["speakers"]
    rec["label"] = edition["name"]
    rec["year"] = edition["year"]
    rec["page_url"] = talk["page_url"]
    rec["infoq_url"] = talk["page_url"]
    if talk.get("published_at"):
        rec["published_at"] = talk["published_at"]
    if talk.get("duration_s"):
        rec["duration_s"] = talk["duration_s"]
    # enrich.py skips anything stamped, so the agenda's abstract is not later
    # overwritten with the channel's boilerplate.
    rec["details_at"] = stamp
    rec["infoq_at"] = stamp


def cache_path(edition_slug: str):
    return CACHE / f"{edition_slug}.json"


def load_cache(edition_slug: str) -> dict:
    p = cache_path(edition_slug)
    if not p.exists():
        return {}
    with p.open(encoding="utf-8") as f:
        return json.load(f)


# --- the run -----------------------------------------------------------------

def run_edition(edition: dict, args, cat: dict, by_key: dict[str, str]) -> dict:
    print(f"\n{edition['name']}  ({edition['slug']})")
    listing = enumerate_edition(edition["slug"], args.pace)
    print(f"  {len(listing)} presentations listed, "
          f"{sum(1 for t in listing if t['has_transcript'])} flagged with a transcript")

    cached = load_cache(edition["slug"])
    talks = cached.get("talks", {})
    stamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    def needs_fetch(t: dict) -> bool:
        if args.refetch or t["slug"] not in talks:
            return True
        # A cached talk is re-fetched when its transcript is missing — but only
        # when the listing says there is one to get. Without that second
        # condition a presentation InfoQ publishes *without* a transcript is
        # re-fetched on every run forever, and next run's answer is the same
        # answer: no transcript. It never converges, and the cost is unbounded.
        return t["has_transcript"] and not atu.transcript_path(talks[t["slug"]]["id"]).exists()

    todo = [t for t in listing if needs_fetch(t)]
    if args.limit:
        todo = todo[:args.limit]
    print(f"  {len(todo)} to fetch"
          + (f", {len(listing) - len(todo)} already cached" if len(todo) < len(listing) else ""))

    tally = {"new": 0, "merged": 0, "words": 0}
    for i, item in enumerate(todo, 1):
        try:
            page = get(item["page_url"])
        except urllib.error.HTTPError as e:
            print(f"  [{i}/{len(todo)}] !! {item['slug']}: HTTP {e.code}")
            time.sleep(args.pace)
            continue
        talk = parse_talk(page, item)
        if not talk["title"]:
            print(f"  [{i}/{len(todo)}] !! {item['slug']}: no title on the page")
            time.sleep(args.pace)
            continue

        key = title_key(talk["title"])
        vid = match_existing(key, by_key)
        matched = vid is not None
        if not matched:
            vid = atu.INFOQ_ID_PREFIX + item["slug"]

        words = 0
        if talk["transcript_lines"]:
            words = save_transcript(vid, talk)
        rec = {k: v for k, v in talk.items() if k != "transcript_lines"}
        rec.update({"id": vid, "matched_youtube": matched, "edition": edition["slug"],
                    "edition_name": edition["name"], "year": edition["year"],
                    "transcript_words": words, "fetched_at": stamp})
        talks[item["slug"]] = rec

        if matched:
            enrich_existing(cat["videos"][vid], talk, edition, stamp)

        tally["merged" if matched else "new"] += 1
        tally["words"] += words
        flag = f"merged into {vid}" if matched else "new"
        print(f"  [{i}/{len(todo)}] {words:>6,}w  {flag:<22} {talk['title'][:64]}")
        time.sleep(args.pace)

    out = {
        "_tally": tally,
        "edition": edition["slug"],
        "name": edition["name"],
        "year": edition["year"],
        "fetched_at": stamp,
        "count": len(talks),
        "talks": dict(sorted(talks.items())),
    }
    atu.write_json(cache_path(edition["slug"]), {k: v for k, v in out.items()
                                                 if k != "_tally"})
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Fetch InfoQ presentation pages: metadata and transcripts.")
    ap.add_argument("--year", action="append", type=int, metavar="YYYY",
                    help="only editions held this year; repeatable. "
                         "The edition's year, not InfoQ's publish date.")
    ap.add_argument("--edition", action="append", metavar="SLUG",
                    help="only this edition, e.g. qcon-london-2026; repeatable")
    ap.add_argument("--list", action="store_true",
                    help="list the editions InfoQ currently exposes and stop")
    ap.add_argument("--limit", type=int, help="at most this many fetches per edition")
    ap.add_argument("--refetch", action="store_true",
                    help="re-fetch pages already cached (they are skipped otherwise)")
    ap.add_argument("--dry-run", action="store_true",
                    help="enumerate and report, write nothing")
    ap.add_argument("--pace", type=float, default=PACE,
                    help=f"seconds between requests (default {PACE}, robots.txt asks for 3)")
    args = ap.parse_args()

    eds = editions()
    if args.year:
        eds = [e for e in eds if e["year"] in args.year]
    if args.edition:
        eds = [e for e in eds if e["slug"] in set(args.edition)]

    if args.list or not eds:
        for e in editions():
            mark = "*" if e in eds else " "
            print(f" {mark} {e['slug']:34s} {e['year']}  {e['name']}")
        if not eds:
            print("\nNo edition matched. InfoQ's filter list carries only the "
                  "most recent editions; --list shows what is there today.")
            sys.exit(1)
        return

    cat = atu.load_catalog(CONF)
    cat.setdefault("videos", {})
    by_key = catalog_index(cat)
    print(f"{len(by_key)} titles already in data/catalog/{CONF}.json to match against")

    if args.dry_run:
        for e in eds:
            listing = enumerate_edition(e["slug"], args.pace)
            print(f"\n{e['name']}: {len(listing)} listed, "
                  f"{sum(1 for t in listing if t['has_transcript'])} with transcripts")
            for t in listing:
                print(f"    {t['slug']}")
            time.sleep(args.pace)
        return

    total_new = total_merged = total_words = 0
    for e in eds:
        tally = run_edition(e, args, cat, by_key)["_tally"]
        total_new += tally["new"]
        total_merged += tally["merged"]
        total_words += tally["words"]

    atu.write_json(atu.catalog_path(CONF), cat)
    print(f"\n{total_merged} merged into existing YouTube records · {total_new} new to InfoQ · "
          f"{total_words:,} transcript words")
    print("Next:  python3 sync_catalog.py && python3 build_index.py")


if __name__ == "__main__":
    main()
