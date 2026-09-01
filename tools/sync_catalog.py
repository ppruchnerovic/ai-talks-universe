#!/usr/bin/env python3
"""Enumerate every conference in conferences.json into the knowledge base.

There is no agenda API here — the corpus is 46 conferences whose only public,
machine-readable programme is their YouTube channel or per-edition playlists.
So this script does the same job in two stages:

  1. ENUMERATE (cheap, unmetered). yt-dlp reads the playlist/channel page, not
     the caption endpoint, so it costs nothing against the transcript quota.
     One page request per 100 videos. Results are cached per conference in
     data/catalog/<slug>.json, which is also where enrich.py writes the
     descriptions and publish dates it collects.

     A source of type "videos" is enumerated from a file in data/seeds/ instead
     — for a conference whose recordings exist on YouTube but are not listed on
     any channel or playlist, so no amount of paging will find them. That costs
     no network at all, so it is folded in on every run, --refresh or not.

  2. DERIVE. Filters (duration, year floor, title regex, and for general
     conferences the AI-relevance test) turn the raw catalogue into the corpus:

       data/talks.json              canonical records — the source of truth
       data/talks.csv               spreadsheet view
       talks/<conf>/<vid>-<slug>.md one readable file per talk

Idempotent: re-running without --refresh rebuilds byte-identical output from
the cache, so a git diff shows exactly what the conferences changed. That
includes talks.json's "generated_at", which records when the corpus last
changed rather than when this run happened — see generated_at().

    python3 sync_catalog.py                    # rebuild from cache (offline)
    python3 sync_catalog.py --refresh          # re-enumerate every source
    python3 sync_catalog.py --refresh -c dotai -c ai-engineer
    python3 sync_catalog.py --no-ai-filter     # keep non-AI talks too
    python3 sync_catalog.py --no-min-year      # keep the pre-2023 talks too
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time

import atu


# --- enumeration -------------------------------------------------------------

def ytdlp_binary() -> str:
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    if os.path.exists(local):
        return local
    found = shutil.which("yt-dlp")
    if not found:
        sys.exit("yt-dlp is not installed:\n    pip install yt-dlp")
    return found


def enumerate_source(src: dict, timeout: int = 600) -> list[dict]:
    """Flat-list one playlist or channel. No media and no captions are touched.

    Flat mode is the whole point: it returns id/title/duration for a page of 100
    at a time, where a full extraction costs ~1.4s per video and draws on the
    same IP reputation the transcript fetch depends on. Descriptions and publish
    dates are not in a flat listing — enrich.py fills those in separately, for
    the talks that survive filtering.
    """
    cmd = [ytdlp_binary(), "--flat-playlist", "--dump-json",
           "--no-warnings", "--ignore-errors"]
    if src.get("first"):
        cmd += ["--playlist-end", str(src["first"])]
    cmd.append(src["url"])
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f"    ! timed out after {timeout}s")
        return []

    out = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        vid = e.get("id")
        # A channel URL can yield nested playlist entries; those have no video id
        # of their own and would otherwise land in the corpus as phantom talks.
        if not vid or e.get("_type") == "playlist" or len(vid) != 11:
            continue
        out.append({
            "video_id": vid,
            "title": " ".join((e.get("title") or "").split()),
            "duration_s": int(e["duration"]) if e.get("duration") else None,
            "channel": e.get("channel") or e.get("uploader"),
            "label": src.get("label"),
            "year": src.get("year"),
            "source_url": src["url"],
        })
    if not out:
        err = (proc.stderr or "").strip().splitlines()
        print(f"    ! nothing returned{': ' + err[-1][:120] if err else ''}")
    return out


SEEDS = atu.DATA / "seeds"

# The keys a seed may carry beyond what a flat listing has. They come from a
# conference's own agenda rather than from YouTube, which is the point of a
# seed: descriptions written by the programme committee, the speakers stated
# rather than guessed from the title, and the session's own page.
SEED_FIELDS = ("description", "speakers", "tags", "published_at", "session_page")


def enumerate_seed(src: dict, conf: dict) -> list[dict]:
    """Read one seed file — a source that is a list of video ids, not a listing.

    Unlisted recordings are invisible to enumeration however deep it pages, so
    for those the registry points at a file instead of a URL. import_kb.py
    writes it; this reads it, and the merge below is the same one every other
    source gets, so the two kinds of source compose.
    """
    path = SEEDS / src["seed"]
    if not path.exists():
        print(f"    ! seed not found: {path.relative_to(atu.ROOT)}")
        return []
    with path.open(encoding="utf-8") as f:
        seed = json.load(f)
    out = []
    for r in seed.get("videos", []):
        vid = r.get("video_id")
        if not vid or len(vid) != 11:
            continue
        rec = {
            "video_id": vid,
            "title": " ".join((r.get("title") or "").split()),
            "duration_s": r.get("duration_s"),
            "channel": r.get("channel") or seed.get("channel"),
            "label": r.get("label") or src.get("label") or seed.get("label"),
            "year": r.get("year") or src.get("year") or seed.get("year"),
            "source_url": src["url"],
            # A seed is already a details fetch, done better: enrich.py skips
            # anything stamped, so the agenda abstract is not later overwritten
            # with the channel boilerplate YouTube carries under these talks.
            "details_at": seed.get("generated_at"),
        }
        for k in SEED_FIELDS:
            if r.get(k):
                rec[k] = r[k]
        out.append(rec)
    return out


INFOQ_CACHE = atu.DATA / "infoq"

# The keys infoq.py resolves that a YouTube listing has no way to know: the
# edition a talk was given at (not the month InfoQ got round to posting it),
# the speakers as InfoQ names them, and the abstract as its programme wrote it.
INFOQ_FIELDS = ("description", "speakers", "published_at", "page_url", "video_url")


def enumerate_infoq(src: dict) -> list[dict]:
    """Read what infoq.py cached — the presentations YouTube never listed.

    A source of type "infoq" is not a listing this script can page: the pages
    are on infoq.com, they carry transcripts, and fetching them is metered by a
    crawl delay, so infoq.py owns that stage the way enrich.py and
    fetch_transcripts.py own theirs. This is the offline half, folded in on
    every run like a seed.

    Talks infoq.py matched to a video already in the catalogue are *not* here.
    Those keep their YouTube id and were written straight onto their existing
    record, so a merged talk stays one talk with one watchable video — emitting
    them again is exactly the duplicate this route exists to avoid.
    """
    out = []
    for path in sorted(INFOQ_CACHE.glob("*.json")):
        with path.open(encoding="utf-8") as f:
            ed = json.load(f)
        for r in ed.get("talks", {}).values():
            if r.get("matched_youtube") or not r.get("id") or not r.get("title"):
                continue
            rec = {
                "video_id": r["id"],
                "title": " ".join(r["title"].split()),
                "duration_s": r.get("duration_s"),
                "channel": "InfoQ",
                "label": ed.get("name") or r.get("edition_name"),
                "year": ed.get("year") or r.get("year"),
                "source_url": src["url"],
                # The page fetch already collected everything enrich.py would go
                # looking for, and from a better source than the channel.
                "details_at": r.get("fetched_at") or ed.get("fetched_at"),
            }
            for k in INFOQ_FIELDS:
                if r.get(k):
                    rec[k] = r[k]
            out.append(rec)
    return out


def sync_infoq(reg: dict) -> None:
    """Fold every "infoq" source into its catalogue. Offline, so unconditional."""
    for conf in reg["conferences"]:
        srcs = [s for s in conf["sources"] if s.get("type") == "infoq"]
        if not srcs:
            continue
        cat = atu.load_catalog(conf["slug"])
        before = json.dumps(cat, ensure_ascii=False, sort_keys=True)
        videos = cat.setdefault("videos", {})
        meta = [m for m in cat.get("sources", [])
                if m.get("url") not in {s["url"] for s in srcs}]
        for src in srcs:
            found = enumerate_infoq(src)
            merge_source(videos, src, found)
            meta.append({"url": src["url"], "label": src.get("label"),
                         "year": src.get("year"), "count": len(found), "type": "infoq"})
        cat.update({"slug": conf["slug"], "name": conf["name"], "sources": meta,
                    "count": len(videos), "videos": dict(sorted(videos.items()))})
        if json.dumps(cat, ensure_ascii=False, sort_keys=True) != before:
            atu.write_json(atu.catalog_path(conf["slug"]), cat)
            print(f"  infoq {conf['slug']}: {cat['count']} videos cached")


def merge_source(videos: dict, src: dict, found: list[dict]) -> None:
    """Fold one source's listing into the cached catalogue, in place.

    Everything this source used to hold that it no longer lists is gone —
    unlisted, deleted or moved. Other sources' videos are untouched. What a
    previous run collected about a video that is still listed survives, so
    enrichment is not undone by a re-enumeration; a seed's own fields win over
    it, because there the agenda is the better source and not a guess.
    """
    ids = {f["video_id"] for f in found}
    for vid, v in list(videos.items()):
        if v.get("source_url") == src["url"] and vid not in ids:
            del videos[vid]
    for f in found:
        prev = videos.get(f["video_id"], {})
        carried = {k: prev[k] for k in ("description", "published_at", "tags", "details_at")
                   if k in prev and k not in f}
        videos[f["video_id"]] = {**f, **carried}


def sync_seeds(reg: dict) -> None:
    """Fold every "videos" source into its catalogue. Offline, so unconditional.

    Written only when something changed, which keeps a plain rebuild
    byte-identical and keeps a sync that runs alongside a transcript fetch from
    touching files nobody asked it to.
    """
    for conf in reg["conferences"]:
        seeds = [s for s in conf["sources"] if s.get("type") == "videos"]
        if not seeds:
            continue
        cat = atu.load_catalog(conf["slug"])
        before = json.dumps(cat, ensure_ascii=False, sort_keys=True)
        videos = cat.setdefault("videos", {})
        meta = [m for m in cat.get("sources", [])
                if m.get("url") not in {s["url"] for s in seeds}]
        for src in seeds:
            found = enumerate_seed(src, conf)
            merge_source(videos, src, found)
            meta.append({"url": src["url"], "label": src.get("label"),
                         "year": src.get("year"), "count": len(found), "type": "videos"})
        cat.update({"slug": conf["slug"], "name": conf["name"], "sources": meta,
                    "count": len(videos), "videos": dict(sorted(videos.items()))})
        if json.dumps(cat, ensure_ascii=False, sort_keys=True) != before:
            atu.write_json(atu.catalog_path(conf["slug"]), cat)
            print(f"  seeded {conf['slug']}: {cat['count']} videos cached")


def refresh_conference(conf: dict, pace: float) -> dict:
    """Re-enumerate every source and merge into the cached catalogue.

    Merging rather than replacing is deliberate in two directions: the
    descriptions enrich.py collected are kept, and a source that comes back
    empty (a deleted playlist, a throttled request, a renamed channel) leaves
    its previous videos in place instead of silently deleting a conference.
    """
    cached = atu.load_catalog(conf["slug"])
    videos: dict[str, dict] = cached.get("videos", {})
    sources_meta = []

    for src in conf["sources"]:
        if src.get("type") in ("videos", "infoq"):
            continue                      # offline; sync_seeds/sync_infoq fold these in
        time.sleep(random.uniform(0, pace))
        found = enumerate_source(src)
        print(f"    {len(found):>4}  {src.get('label') or src['url']}")
        if not found:
            kept = sum(1 for v in videos.values() if v.get("source_url") == src["url"])
            sources_meta.append({"url": src["url"], "label": src.get("label"),
                                 "year": src.get("year"), "count": kept, "stale": True})
            continue
        merge_source(videos, src, found)
        sources_meta.append({"url": src["url"], "label": src.get("label"),
                             "year": src.get("year"), "count": len(found)})

    out = {
        "slug": conf["slug"],
        "name": conf["name"],
        "enumerated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "sources": sources_meta,
        "count": len(videos),
        "videos": dict(sorted(videos.items())),
    }
    atu.write_json(atu.catalog_path(conf["slug"]), out)
    return out


# --- speakers ----------------------------------------------------------------

SPLIT_RE = re.compile(r"\s+[|•·—–]\s+|\s+[-]\s+|\s*\|\s*")

# Words that make a segment a conference/brand/topic label rather than a person.
NOT_A_NAME = set("""
conference conferences summit congress con expo forum festival keynote keynotes talk talks
session sessions track day days stage live stream livestream panel fireside chat interview
workshop tutorial demo demos webinar meetup edition part recap highlights opening closing
welcome intro introduction announcement announcements q&a qa ama sponsored sponsor partner
ai ml llm llms genai gpt agents agent copilot cloud data devops security engineering software
developer developers dev tech technology university institute labs lab inc llc ltd gmbh corp
the and with for from how why what when where new your our their best guide deep dive
applications application systems system models model learning networks network research
science medicine health healthcare robotics energy climate industry education future ethics
design city cities transport mobility aviation retail finance banking insurance manufacturing
platform platforms tools tooling infrastructure production scale scaling practice practices
""".split())

PARTICLES = {"van", "von", "de", "der", "den", "del", "di", "da", "le", "la", "el", "bin",
             "al", "dos", "das", "ter", "ten", "op", "of"}

DESC_SPEAKER_RE = re.compile(
    r"^\s*(?:speakers?|presenters?|presented by|speaker\(s\)|by)\s*[:\-–]\s*(.{3,160})$",
    re.I | re.M)


def name_like(seg: str, blocked: set[str]) -> str | None:
    """Is this title segment a person's name? Conservative on purpose.

    A false positive is worse than a miss: it puts a conference's brand into the
    speaker field of every one of its talks, and the speaker field is weighted
    heavily in search.
    """
    seg = seg.strip().strip(",;:")
    # "Name, Company" and "Name (Company)" — keep the part before the comma.
    seg = re.split(r"\s*[(,]\s*", seg, 1)[0].strip()
    if not (3 <= len(seg) <= 42) or any(ch.isdigit() for ch in seg):
        return None
    words = seg.split()
    if not (2 <= len(words) <= 4):
        return None
    low = [w.lower().strip(".") for w in words]
    if any(w in blocked or w in NOT_A_NAME for w in low):
        return None
    for i, w in enumerate(words):
        if low[i] in PARTICLES and i:            # "van der Berg"
            continue
        # Initials ("J.") and ordinary capitalised names only; no ALLCAPS brands.
        if not re.fullmatch(r"[A-ZÀ-Þ][a-zà-ÿ'’\-]*\.?", w):
            return None
    return seg


def speakers_from_title(title: str, blocked: set[str]) -> list[str]:
    segs = [s for s in SPLIT_RE.split(title) if s.strip()]
    if len(segs) < 2:
        return []
    out = []
    for s in segs:
        n = name_like(s, blocked)
        if n and n not in out:
            out.append(n)
    return out


def speakers_from_description(desc: str, blocked: set[str]) -> list[str]:
    for m in DESC_SPEAKER_RE.finditer(desc or ""):
        names = []
        for part in re.split(r"\s*(?:,|&|\band\b)\s*", m.group(1)):
            n = name_like(part, blocked)
            if n and n not in names:
                names.append(n)
        if names:
            return names
    return []


def blocked_words(conf: dict) -> set[str]:
    """Every word of the conference's own name, its labels and its channel.

    "LangChain Interrupt" is shaped exactly like "Firstname Lastname"; the only
    thing that tells them apart is knowing whose conference this is.
    """
    bits = [conf["name"], conf["slug"].replace("-", " ")]
    bits += [s.get("label") or "" for s in conf["sources"]]
    words = set()
    for b in bits:
        for w in re.split(r"[^A-Za-z]+", b):
            if len(w) > 1:
                words.add(w.lower())
    return words


# --- deriving the corpus -----------------------------------------------------

def clean_description(desc: str | None) -> str:
    """Strip the boilerplate every conference channel pads its descriptions with.

    Left in, "Subscribe · Follow us on X · #ai #tech" is indexed as if the
    speaker had said it, and it is the same text under every talk on the
    channel — pure noise with a high term frequency.
    """
    if not desc:
        return ""
    keep = []
    for line in desc.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if not s:
            keep.append("")
            continue
        # A line that is mostly a URL, or a wall of hashtags, says nothing.
        if re.fullmatch(r"(?:https?://\S+\s*)+", s):
            continue
        if re.fullmatch(r"(?:#\w[\w'-]*\s*){2,}", s):
            continue
        if re.match(r"^(?:subscribe|follow us|connect with us|learn more|sign up|"
                    r"join us on|watch more|check out|website|twitter|linkedin|"
                    r"instagram|facebook|tiktok|discord|slack|github)\b.{0,80}$", s, re.I):
            continue
        keep.append(s)
    out = "\n".join(keep)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def clean_tags(tags) -> list[str]:
    r"""Fold the whitespace inside each tag and drop the empties.

    Titles get this from enumerate_source()/enumerate_seed() and descriptions
    from clean_description(); tags were the one field copied through verbatim,
    which is exactly why no title was ever corrupted while three tags were — a
    raw \r inside a YouTube tag split a line in the rendered markdown, and two
    others arrived with a newline in them.

    Doing it here, on every derivation, is what makes it self-healing: a
    hand-edit of data/catalog/ is undone by the next enrich.py run, and this is
    not. It folds rather than splits on purpose — one tag in, one tag out —
    because splitting would invent tags ("Tags:", "5") out of a source's
    formatting accident.
    """
    out = []
    for t in tags or []:
        if t is None:
            continue
        s = " ".join(str(t).split())
        if s:
            out.append(s)
    return out


def keep_video(v: dict, conf: dict, ai_filter: bool, src: dict | None = None,
               floor: int | None = None) -> tuple[bool, str]:
    """Filter one video. A source may override any of the conference's rules.

    The rules exist because a channel listing is a mixed bag — a general
    conference's AI sessions buried in its other four fifths, and stings,
    trailers and sponsor spots mixed in with the talks. A curated source is not
    that: every record in a seed is a session someone put on a programme, so
    `wearedevelopers`' World Congress seed carries `"scope": "all"` and keeps
    its five-minute lightning talks, while the same conference's channel
    listing keeps the AI filter it has always had.

    `floor` is the registry's corpus-wide `min_year`, overridable the same way
    and by the same argument: a topic filter is a property of the source before
    it is a property of the corpus. On AI topics 2022 and earlier is a different
    subject — applied ML and data engineering — but at an AI *security*
    conference the pre-LLM back catalogue is the same subject, so those three
    are registered `"min_year": null`.
    """
    def rule(key):
        return src.get(key, conf.get(key)) if src else conf.get(key)

    def year_floor():
        # Three levels, and `null` has to mean "no floor" rather than "unset",
        # which is what the security conferences are registered with — so this
        # asks whether the key is present, not what rule() would return for it.
        for rules in (src, conf):
            if rules and "min_year" in rules:
                return rules["min_year"]
        return floor

    # A record with no title is a hollow one. When the Data API does not return
    # a video — private, deleted, region blocked — enrich.py stamps details_at
    # anyway so it is not re-fetched every run, which leaves a permanent shell:
    # no title, no duration, no channel, and has_details: true. The playlist
    # still lists it, so re-enumeration puts it back; only a filter keeps it out
    # of the corpus for good. Nothing downstream can use it either — the slug,
    # the markdown filename and every search field are derived from the title.
    if not str(v.get("title") or "").strip():
        return False, "untitled"
    d = v.get("duration_s")
    if rule("min_duration") and (d is None or d < rule("min_duration")):
        # An unknown duration does not pass a minimum-duration rule. The rule is
        # an assertion the record has to support, and every listing route
        # (yt-dlp's flat playlist, the Data API) returns a duration, so a record
        # without one is degraded rather than merely undocumented. Where an
        # unknown duration would be legitimate — a curated agenda that lists
        # sessions but not runtimes — the source says so by setting
        # "min_duration": 0, which switches this whole check off; the
        # wearedevelopers World Congress seed already does.
        return False, "short" if d is not None else "no-duration"
    hay = f"{v.get('title','')}\n{v.get('description','') or ''}"
    if rule("match") and not re.search(rule("match"), hay, re.I):
        return False, "match"
    if rule("exclude") and re.search(rule("exclude"), v.get("title", ""), re.I):
        return False, "exclude"
    if ai_filter and rule("scope") == "ai":
        if not atu.looks_ai(v.get("title"), v.get("description"), " ".join(v.get("tags") or [])):
            return False, "not-ai"
    # The corpus floor, checked last so its count in the drop report is what the
    # floor actually cost — the talks that would otherwise have been kept, not
    # every old video the AI filter was going to reject anyway (1,618 against
    # 503 here). Unlike the duration rule above, an *unknown* year passes:
    # enrichment is what resolves a year, so dropping the undated would hide
    # every talk a fresh enumeration found until the next enrich run, and hide it
    # from refresh_report.py, which is what reads the difference. The floor is a
    # claim about talks proven old, not about talks not yet dated.
    low, y = year_floor(), atu.year_of(v)
    if low and y and y < low:
        return False, f"pre-{low}"
    return True, ""


def build_talks(reg: dict, only: list[str], ai_filter: bool,
                floor: int | None) -> tuple[list[dict], dict]:
    confs = [c for c in reg["conferences"] if not only or c["slug"] in only]
    talks: list[dict] = []
    stats: dict[str, collections.Counter] = {}
    seen: dict[str, str] = {}          # video_id -> conference that claimed it
    dupes = 0

    for conf in confs:
        cat = atu.load_catalog(conf["slug"])
        drop = collections.Counter()
        blocked = blocked_words(conf)
        candidates = []
        by_url = {s["url"]: s for s in conf["sources"]}
        infoq_src = next((s for s in conf["sources"] if s.get("type") == "infoq"), None)

        for vid, v in cat.get("videos", {}).items():
            # A record's rules come from the source that listed it — except
            # where a better source has since claimed the same talk. `infoq_at`
            # means infoq.py found this video on InfoQ's own programme and
            # merged its transcript in, and a talk on the programme is governed
            # by the programme's rules however it was first enumerated.
            # Without this, one QCon London 2025 session is kept and the
            # session in the next room is dropped, purely because one of them
            # also happened to reach the YouTube channel.
            src = infoq_src if (v.get("infoq_at") and infoq_src) \
                else by_url.get(v.get("source_url"))
            ok, why = keep_video(v, conf, ai_filter, src, floor)
            if not ok:
                drop[why] += 1
                continue
            # The same video can sit in two registries — an InfoQ talk in both
            # the QCon channel and a QCon AI playlist, say. First conference in
            # registry order keeps it, so the outcome does not depend on dict
            # iteration.
            if vid in seen:
                drop["duplicate"] += 1
                continue
            seen[vid] = conf["slug"]
            candidates.append((vid, v))

        # Speakers, in two passes. The second pass is what makes the first one
        # safe, because no per-title rule can tell "Lian Li" from "Rare Disease
        # Applications" — both are two or three capitalised words. What tells
        # them apart is the rest of the conference: a "name" that shows up
        # across a tenth of it is the host, the brand or the series, and a
        # *word* that shows up across a tenth of its candidate names is a topic
        # label, because real names do not share vocabulary.
        raw = {}
        stated = {}          # video_id -> names the source states outright
        counts = collections.Counter()
        word_counts = collections.Counter()
        for vid, v in candidates:
            # A seeded talk carries its agenda's own speaker list. Guessing over
            # that would be strictly worse, and the two filters below exist only
            # to make guesses safe — a real name that happens to appear on ten
            # talks is a prolific speaker, not a brand.
            if v.get("speakers"):
                stated[vid] = [n for n in v["speakers"] if n]
                raw[vid] = []
                continue
            names = speakers_from_description(v.get("description"), blocked) \
                or speakers_from_title(v.get("title", ""), blocked)
            raw[vid] = names
            counts.update(names)
            for n in set(names):
                word_counts.update({w.lower() for w in n.split()})
        ceiling = max(4, int(0.10 * len(candidates)))
        n_names = sum(len(v) for v in raw.values()) or 1
        word_ceiling = max(5, int(0.06 * n_names))
        hot = {w for w, c in word_counts.items() if c > word_ceiling}
        overused = {n for n, c in counts.items() if c > ceiling}
        overused |= {n for n in counts if any(w.lower() in hot for w in n.split())}

        for vid, v in candidates:
            names = stated.get(vid) or [n for n in raw[vid] if n not in overused]
            desc = clean_description(v.get("description"))
            talks.append({
                "id": vid,
                "video_id": vid,
                "slug": atu.slugify(v.get("title") or ""),
                "title": v.get("title") or "",
                "description": desc,
                "speakers": names,
                "conference": conf["slug"],
                "conference_name": conf["name"],
                "category": conf["category"],
                "edition": v.get("label"),
                "year": atu.year_of(v),
                "channel": v.get("channel"),
                "duration_min": round(v["duration_s"] / 60) if v.get("duration_s") else None,
                "duration_s": v.get("duration_s"),
                "published_at": v.get("published_at"),
                "tags": clean_tags(v.get("tags")),
                # Not every record is a YouTube one any more. `url` is the
                # canonical link — the video where there is a video, the talk's
                # own page where InfoQ is all there is — and `youtube_url` says
                # only what it claims to, so a reader that wants to build
                # `&t=`, an embed or a thumbnail can tell whether it may.
                "youtube_url": atu.WATCH.format(vid=vid) if atu.is_youtube_id(vid) else None,
                "url": atu.watch_url(vid, v.get("page_url")),
                "page_url": v.get("page_url"),
                "conference_site": conf["site"],
                "availability": conf["availability"],
                "priority": conf["priority"],
                "source_url": v.get("source_url"),
                "has_details": bool(v.get("details_at")),
            })
        drop["overused_speaker_names"] = len(overused)
        stats[conf["slug"]] = drop
        dupes += drop["duplicate"]

    # Stable order: conference as registered, then newest first, then title.
    order = {c["slug"]: i for i, c in enumerate(reg["conferences"])}
    talks.sort(key=lambda t: (order.get(t["conference"], 999),
                              -(t["year"] or 0), t["title"].lower(), t["id"]))
    return talks, stats


# --- output ------------------------------------------------------------------

MD_TEMPLATE = """---
id: {id}
title: {title_q}
slug: {slug}
conference: {conference}
conference_name: {conference_name_q}
category: {category_q}
edition: {edition_q}
year: {year}
speakers: {speakers_json}
channel: {channel_q}
duration_min: {duration_min}
published_at: {published_at}
video_id: {video_id}
url: {url}
youtube_url: {youtube_url}
tags: {tags_json}
transcript: {has_transcript}
---

# {title}

**{speaker_line}**

`{conference_name}` · `{edition}`{year_bit} · `{duration}`{tag_line}

[{watch_label}]({url}) · [Conference site]({conference_site})

## Description

{description}
{transcript_block}"""


def yaml_q(s: str | None) -> str:
    return "null" if s is None else json.dumps(s, ensure_ascii=False)


def transcript_block(t: dict) -> str:
    tr = atu.load_transcript(t["id"])
    if not tr or not tr.get("segments"):
        return ""
    lines = ["\n## Transcript\n"]
    lines.append(
        f"*{tr.get('word_count', 0):,} words · source: {tr.get('source', 'youtube')} "
        f"({tr.get('language', 'en')}, {tr.get('timing', 'exact')} timings)*\n")
    # ~45s paragraphs, each deep-linking back into the video where the video
    # accepts a timestamp. An InfoQ-only talk has a page rather than a
    # watch URL, and `?t=` means nothing to it, so those keep the timestamp as
    # plain text: still a position in the talk, just not a link that lies.
    yt = t["youtube_url"]
    bucket, bucket_start = [], None
    for seg in tr["segments"]:
        if bucket_start is None:
            bucket_start = seg["start"]
        bucket.append(seg["text"])
        if seg["start"] - bucket_start >= 45:
            lines.append(_para(bucket, bucket_start, yt))
            bucket, bucket_start = [], None
    if bucket:
        lines.append(_para(bucket, bucket_start or 0, yt))
    return "\n".join(lines)


def _para(texts: list[str], start: float, youtube_url: str | None) -> str:
    body = " ".join(" ".join(texts).split())
    ts = f"{int(start) // 60:d}:{int(start) % 60:02d}"
    stamp = f"[{ts}]({youtube_url}&t={int(start)}s)" if youtube_url else ts
    return f"**{stamp}** {body}\n"


def render_md(t: dict) -> str:
    mins = f"{t['duration_min']} min" if t["duration_min"] else "duration unknown"
    return MD_TEMPLATE.format(
        id=t["id"],
        title=t["title"],
        title_q=yaml_q(t["title"]),
        slug=t["slug"],
        conference=t["conference"],
        conference_name=t["conference_name"],
        conference_name_q=yaml_q(t["conference_name"]),
        category_q=yaml_q(t["category"]),
        edition=t["edition"] or t["conference_name"],
        edition_q=yaml_q(t["edition"]),
        year=t["year"] if t["year"] else "null",
        year_bit=f" · `{t['year']}`" if t["year"] else "",
        speakers_json=json.dumps(t["speakers"], ensure_ascii=False),
        speaker_line=", ".join(t["speakers"]) if t["speakers"] else "Speaker not identified",
        channel_q=yaml_q(t["channel"]),
        duration=mins,
        duration_min=t["duration_min"] if t["duration_min"] else "null",
        published_at=t["published_at"] or "null",
        video_id=t["video_id"],
        url=t["url"] or "",
        watch_label="Watch the recording" if t["url"] else "No recording link",
        youtube_url=t["youtube_url"] or "null",
        conference_site=t["conference_site"],
        tags_json=json.dumps(t["tags"], ensure_ascii=False),
        tag_line=("\n\n" + " ".join(f"`#{x}`" for x in t["tags"])) if t["tags"] else "",
        has_transcript=str(atu.transcript_path(t["id"]).exists()).lower(),
        description=t["description"] or "*No description published on YouTube.*",
        transcript_block=transcript_block(t),
    )


CSV_FIELDS = ["id", "title", "conference", "conference_name", "category", "edition", "year",
              "speakers", "channel", "duration_min", "published_at", "url", "description"]


def csv_row(t: dict) -> dict:
    r = {k: t.get(k) for k in CSV_FIELDS}
    r["speakers"] = ", ".join(t["speakers"])
    return r


def check_not_shrinking(n_new: int, allow_shrink: bool) -> None:
    """Refuse to publish a corpus that suddenly lost most of its talks.

    This can run unattended, and a throttled yt-dlp exits 0 with no entries —
    a successful-looking run that would delete every markdown file and empty the
    index. Per-source staleness handling (refresh_conference) covers the common
    case; this is the backstop for a bad registry edit or a wholesale failure.
    """
    if allow_shrink or not atu.TALKS_JSON.exists():
        return
    try:
        with atu.TALKS_JSON.open(encoding="utf-8") as f:
            n_old = int(json.load(f).get("count") or 0)
    except (OSError, ValueError, TypeError):
        return
    if not n_old or n_new >= n_old * 0.9:
        return
    sys.exit(
        f"\nrefusing to overwrite: {n_new} talks, down from {n_old}.\n"
        f"Nothing was written — talks.json, the markdown and the index are untouched.\n"
        f"If the drop is real, rerun with --allow-shrink.")


def generated_at(body: dict) -> str:
    """When the corpus last *changed*, not when this run happened.

    A rebuild from cache is byte-identical by design — that is the whole point
    of "a git diff shows exactly what the conferences changed" — and a wall
    clock in the file was the one line that broke the promise, dirtying a 15 MB
    tracked file on every no-op run. So the previous stamp is kept verbatim
    when everything else in talks.json would be written unchanged.

    The comparison runs both sides through the same serializer rather than
    comparing objects, so a value that is a tuple here and a list on disk does
    not read as a change. Key order counts: it is what the file will be written
    in.
    """
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    try:
        with atu.TALKS_JSON.open(encoding="utf-8") as f:
            old = json.load(f)
    except (OSError, ValueError):
        return now
    if not isinstance(old, dict):
        return now
    previous = old.pop("generated_at", None)
    if not isinstance(previous, str):
        return now

    def dumped(o) -> str:
        return json.dumps(o, ensure_ascii=False, separators=(",", ":"))

    return previous if dumped(old) == dumped(body) else now


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true",
                    help="re-enumerate the sources (default: rebuild from data/catalog/)")
    ap.add_argument("-c", "--conference", action="append", dest="only", default=[],
                    help="limit to these conference slugs (repeatable)")
    ap.add_argument("--no-ai-filter", action="store_true",
                    help='keep non-AI sessions from conferences registered as scope "ai"')
    ap.add_argument("--no-min-year", action="store_true",
                    help="ignore the registry's corpus year floor, so a rebuild shows "
                         "what it is holding back (enumeration cached it either way)")
    ap.add_argument("--allow-shrink", action="store_true")
    ap.add_argument("--pace", type=float, default=1.5, metavar="SECONDS",
                    help="max jittered wait between source enumerations")
    args = ap.parse_args()

    reg = atu.load_registry()
    known = {c["slug"] for c in reg["conferences"]}
    for s in args.only:
        if s not in known:
            sys.exit(f"unknown conference slug: {s}")

    if args.refresh:
        todo = [c for c in reg["conferences"] if not args.only or c["slug"] in args.only]
        for i, conf in enumerate(todo, 1):
            print(f"[{i}/{len(todo)}] {conf['name']}")
            cat = refresh_conference(conf, args.pace)
            print(f"    = {cat['count']} videos cached")
        print()

    # Seeds and the InfoQ cache are read from disk, so they cost nothing and are
    # always current.
    sync_seeds(reg)
    sync_infoq(reg)

    # The corpus is always derived from every conference, even when only one was
    # refreshed — otherwise a targeted refresh would publish a corpus of one.
    floor = None if args.no_min_year else reg.get("min_year")
    talks, stats = build_talks(reg, [], not args.no_ai_filter, floor)
    check_not_shrinking(len(talks), args.allow_shrink)

    body = {
        "source": "YouTube playlists and channels listed in conferences.json, "
                  "plus InfoQ's own presentation pages",
        "ai_filter": not args.no_ai_filter,
        "min_year": floor,
        "conferences": [{"slug": c["slug"], "name": c["name"], "category": c["category"]}
                        for c in reg["conferences"]],
        "count": len(talks),
        "talks": talks,
    }
    stamp = generated_at(body)
    atu.write_json(atu.TALKS_JSON, {"generated_at": stamp, **body})

    atu.TALKS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with atu.TALKS_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for t in talks:
            w.writerow(csv_row(t))

    # Rebuilt from scratch so renamed or dropped talks don't linger.
    if atu.TALKS_MD.exists():
        shutil.rmtree(atu.TALKS_MD)
    n_tr = n_desc = 0
    for t in talks:
        d = atu.TALKS_MD / t["conference"]
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{t['id']}-{t['slug']}.md").write_text(render_md(t), encoding="utf-8")
        n_tr += atu.transcript_path(t["id"]).exists()
        n_desc += bool(t["description"])

    per_conf = collections.Counter(t["conference"] for t in talks)
    print(f"{len(talks)} talks over {len(per_conf)} conferences "
          f"({n_desc} with descriptions, {n_tr} with transcripts)\n")
    for c in reg["conferences"]:
        d = stats.get(c["slug"], collections.Counter())
        dropped = ", ".join(f"{v} {k}" for k, v in sorted(d.items()) if v and k != "overused_speaker_names")
        print(f"  {per_conf.get(c['slug'], 0):>5}  {c['slug']:<24}"
              + (f"  (dropped {dropped})" if dropped else ""))
    print(f"\n  data/talks.json · data/talks.csv · talks/")


if __name__ == "__main__":
    main()
