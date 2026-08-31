#!/usr/bin/env python3
"""Fill in the descriptions, publish dates and tags a flat listing does not carry.

A flat playlist listing gives id / title / duration for a page of 100 at a time
and nothing else. Descriptions matter — they are this corpus's equivalent of a
conference abstract, and for many channels they are where the speaker's name
is written — so they are collected separately, cached in
data/catalog/<slug>.json next to the video they belong to, and folded into the
corpus by the next sync_catalog.py run.

Two routes:

  1. YouTube Data API v3 — set YOUTUBE_API_KEY. 50 videos per request, 1 quota
     unit per request against a 10,000/day default, so the entire corpus costs
     well under 1% of a day's quota. Use this if you have a key; getting one is
     free (console.cloud.google.com -> enable "YouTube Data API v3").

  2. yt-dlp — no key, but a full extraction per video (~1.4s) against the same
     IP reputation the transcript fetch depends on. Paced and resumable, and it
     stops on the first sign of a block rather than burning the rest.

    python3 enrich.py                       # the current corpus, missing details only
    python3 enrich.py -c langchain-interrupt
    python3 enrich.py --all --priority 1    # everything cached for priority-1 conferences
    python3 enrich.py --limit 200 --workers 2
    python3 enrich.py --min-year 2026 --include-unknown-year   # this year's talks

Afterwards:  python3 sync_catalog.py && python3 build_index.py

`--include-unknown-year` belongs on any year-scoped run here: enrichment is what
resolves an unknown year, so without it a `--min-year 2026` run can only ever
re-select videos whose year is already known.

`--all` matters for conferences registered with scope "ai": their AI-relevance
filter reads the description, so a talk whose title does not say "AI" is dropped
before it is ever enriched. With an API key, enrich `--all` first, then sync.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import atu

API = "https://www.googleapis.com/youtube/v3/videos"


class BlockedError(Exception):
    """YouTube refused this IP, rather than this video."""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


ISO_DUR = re.compile(r"P(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


def iso_seconds(s: str | None) -> int | None:
    m = ISO_DUR.fullmatch(s or "")
    if not m:
        return None
    d, h, mi, sec = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + sec


def fetch_api(ids: list[str], key: str) -> dict[str, dict]:
    q = urllib.parse.urlencode({"part": "snippet,contentDetails", "id": ",".join(ids), "key": key})
    req = urllib.request.Request(f"{API}?{q}", headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        if e.code == 403:
            raise SystemExit(f"YouTube API refused the key (quota or restrictions):\n{body}")
        raise SystemExit(f"YouTube API error {e.code}:\n{body}")
    out = {}
    for it in data.get("items", []):
        sn = it.get("snippet") or {}
        out[it["id"]] = {
            "description": sn.get("description") or "",
            "published_at": sn.get("publishedAt"),
            "tags": sn.get("tags") or [],
            "duration_s": iso_seconds((it.get("contentDetails") or {}).get("duration")),
            "channel": sn.get("channelTitle"),
        }
    return out


def ytdlp_binary() -> str:
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    if os.path.exists(local):
        return local
    found = shutil.which("yt-dlp")
    if not found:
        sys.exit("yt-dlp is not installed and YOUTUBE_API_KEY is not set")
    return found


BLOCK_MARKERS = ("Sign in to confirm", "429", "Too Many Requests", "blocked", "bot")


def fetch_ytdlp(vid: str) -> dict:
    cmd = [ytdlp_binary(), "-J", "--skip-download", "--no-warnings",
           atu.WATCH.format(vid=vid)]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0 or not proc.stdout.strip():
        err = (proc.stderr or "").strip()
        if any(m.lower() in err.lower() for m in BLOCK_MARKERS):
            raise BlockedError(err.splitlines()[-1][:160] if err else "refused")
        raise LookupError(err.splitlines()[-1][:160] if err else "no metadata returned")
    d = json.loads(proc.stdout)
    up = d.get("upload_date")
    return {
        "description": d.get("description") or "",
        "published_at": (f"{up[:4]}-{up[4:6]}-{up[6:8]}T00:00:00Z" if up else None),
        "tags": d.get("tags") or [],
        "duration_s": int(d["duration"]) if d.get("duration") else None,
        "channel": d.get("channel") or d.get("uploader"),
    }


def select(reg: dict, args) -> tuple[dict[str, list[str]], int]:
    """conference slug -> video ids needing details, highest priority first.

    Every run of any size is a partial run — the yt-dlp route is refused after a
    few hundred videos on a normal connection — so the order decides what a
    blocked run leaves behind. Conferences are taken whole, in priority order,
    rather than a slice of each: "what was said at AI Engineer" is answerable
    from one conference that is finished, and not from forty that are 6% done.

    Also returns how many videos the year filter dropped, so a run scoped to
    2026 says so rather than silently enriching a fortieth of the catalogue.
    """
    order = sorted(reg["conferences"], key=lambda c: (c["priority"], c["slug"]))
    confs = {c["slug"]: c for c in order}
    rank = {c["slug"]: i for i, c in enumerate(order)}
    wanted = collections.OrderedDict()
    off_year = 0

    if args.all:
        pool = [(slug, vid, v)
                for slug in confs
                for vid, v in atu.load_catalog(slug).get("videos", {}).items()]
    else:
        pool = []
        cats = {}
        for t in atu.load_talks():
            cats.setdefault(t["conference"], atu.load_catalog(t["conference"]))
            v = cats[t["conference"]].get("videos", {}).get(t["id"])
            if v is not None:
                pool.append((t["conference"], t["id"], v))

    for slug, vid, v in pool:
        c = confs.get(slug)
        if not c:
            continue
        if args.only and slug not in args.only:
            continue
        if args.priority and c["priority"] > args.priority:
            continue
        if v.get("details_at") and not args.refetch:
            continue
        # Prunes within a conference; the priority order above is untouched.
        if not atu.year_wanted(atu.year_of(v), args):
            off_year += 1
            continue
        wanted.setdefault(slug, []).append(vid)
    return collections.OrderedDict(sorted(wanted.items(), key=lambda kv: rank[kv[0]])), off_year


def apply_details(cat: dict, vid: str, det: dict) -> None:
    v = cat["videos"][vid]
    v["description"] = det.get("description") or ""
    v["published_at"] = det.get("published_at")
    v["tags"] = det.get("tags") or []
    if det.get("duration_s"):
        v["duration_s"] = det["duration_s"]
    if det.get("channel"):
        v["channel"] = det["channel"]
    v["details_at"] = now()
    cat["videos"][vid] = v


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--conference", action="append", dest="only", default=[])
    ap.add_argument("--all", action="store_true",
                    help="every cached video, not only the ones that survived filtering")
    ap.add_argument("--priority", type=int, help="only conferences at or above this priority")
    ap.add_argument("--limit", type=int, help="stop after N videos")
    ap.add_argument("--refetch", action="store_true", help="re-fetch details already cached")
    atu.add_year_args(ap)
    ap.add_argument("--workers", type=int, default=2, help="parallel yt-dlp extractions")
    ap.add_argument("--min-delay", type=float, default=0.6)
    ap.add_argument("--max-delay", type=float, default=1.8)
    ap.add_argument("--api-key", default=os.environ.get("YOUTUBE_API_KEY"))
    args = ap.parse_args()

    reg = atu.load_registry()
    wanted, off_year = select(reg, args)
    total = sum(len(v) for v in wanted.values())
    if args.limit:
        trimmed, n = collections.OrderedDict(), 0
        for slug, ids in wanted.items():
            if n >= args.limit:
                break
            take = ids[: args.limit - n]
            trimmed[slug] = take
            n += len(take)
        wanted, total = trimmed, n
    year_note = f" · {off_year} dropped by the year filter" if off_year else ""
    if not total:
        print(f"nothing to enrich — every selected video already has details{year_note}")
        return

    route = "YouTube Data API" if args.api_key else "yt-dlp"
    print(f"{total} videos to enrich over {len(wanted)} conferences · "
          f"route: {route}{year_note}\n")

    ok = fail = 0
    for slug, ids in wanted.items():
        cat = atu.load_catalog(slug)
        got = 0
        if args.api_key:
            for i in range(0, len(ids), 50):
                batch = ids[i:i + 50]
                for vid, det in fetch_api(batch, args.api_key).items():
                    apply_details(cat, vid, det)
                    got += 1
                # Videos the API did not return are private, deleted or region
                # blocked; mark them so they are not retried on every run.
                for vid in batch:
                    if not cat["videos"][vid].get("details_at"):
                        cat["videos"][vid]["details_at"] = now()
                        cat["videos"][vid].setdefault("description", "")
        else:
            got, blocked = enrich_ytdlp(cat, ids, args)
            if blocked:
                atu.write_json(atu.catalog_path(slug), cat)
                print("\n!! YouTube is refusing this IP. Stopping — rerun later or set "
                      "YOUTUBE_API_KEY.\n   Everything fetched so far is saved.")
                ok += got
                break
        atu.write_json(atu.catalog_path(slug), cat)
        ok += got
        fail += len(ids) - got
        print(f"  {got:>4}/{len(ids):<4} {slug}")

    print(f"\ndone: {ok} enriched, {fail} unavailable")
    print("Next:  python3 sync_catalog.py && python3 build_index.py")


def enrich_ytdlp(cat: dict, ids: list[str], args) -> tuple[int, bool]:
    """Threaded, paced extraction. Stops the whole run on the first block."""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    blocked = threading.Event()
    got = 0

    def work(vid):
        if blocked.is_set():
            raise BlockedError("skipped")
        time.sleep(random.uniform(args.min_delay, args.max_delay))
        return vid, fetch_ytdlp(vid)

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(work, v) for v in ids]
        try:
            for fut in as_completed(futures):
                try:
                    vid, det = fut.result()
                except BlockedError:
                    blocked.set()
                    continue
                except Exception:
                    continue
                apply_details(cat, vid, det)
                got += 1
        except KeyboardInterrupt:
            pool.shutdown(wait=False, cancel_futures=True)
            print("\ninterrupted — what was fetched is saved")
    return got, blocked.is_set()


if __name__ == "__main__":
    main()
