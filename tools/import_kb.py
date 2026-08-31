#!/usr/bin/env python3
"""Import a conference that YouTube enumeration cannot see.

The WeAreDevelopers World Congress recordings are on the `@_wearedevs` channel
but not on its `/videos` tab, so the flat listing `sync_catalog.py` runs never
returns them: of 358 congress talks, exactly one is in the 700 videos that
enumeration found. What *does* know about them is the congress agenda API, and
that was already harvested — titles, abstracts, speakers, tracks and a
`recording_url` per session — into the corpus at `../presentations/kb`, together
with an exact-timing transcript for all 358.

So this is a metadata import, not a fetch. It touches no network, spends no
Supadata credit and draws nothing from the per-IP caption allowance:

    data/seeds/<name>.json          one seed record per talk, read by
                                    sync_catalog.py's "videos" source type
    data/transcripts/<vid>.json     the kb transcripts, re-keyed from the kb's
                                    own talk id to the YouTube video id

The seed is what makes the import survive: `sync_catalog.py --refresh` deletes
whatever a source no longer lists, so imported videos need a source of their own
rather than being written into the catalogue by hand.

    python3 import_kb.py --dry-run
    python3 import_kb.py

Rerunning is safe. It never overwrites a transcript that already exists, since
the fetcher may have collected a better one, and the seed it writes is a pure
function of the kb corpus.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import sys

import atu

DEFAULT_KB = atu.ROOT.parent / "presentations" / "kb"
SEEDS = atu.DATA / "seeds"


def read_kb(kb: pathlib.Path) -> tuple[list[dict], pathlib.Path]:
    talks_json = kb / "data" / "talks.json"
    if not talks_json.exists():
        sys.exit(f"no kb corpus at {kb} (expected {talks_json})")
    with talks_json.open(encoding="utf-8") as f:
        doc = json.load(f)
    talks = doc["talks"] if isinstance(doc, dict) else doc
    return talks, kb / "data" / "transcripts"


def duration_s(talk: dict, tr: dict | None) -> int | None:
    """Where the video actually ends, falling back to the scheduled slot.

    The agenda's `duration_min` is the slot the session was given, which
    includes the changeover and rounds to 15 minutes; the last caption cue is a
    close lower bound on the recording itself, and every one of these talks has
    captions. `min_duration` in the registry filters on this, so the slot length
    would keep a five-minute lightning talk that was given a half-hour slot.
    """
    if tr and tr.get("segments"):
        end = max(s["start"] + s.get("duration", 0) for s in tr["segments"])
        return round(end)
    return round(talk["duration_min"] * 60) if talk.get("duration_min") else None


def speaker_names(talk: dict) -> list[str]:
    """The agenda API states who spoke, so the title heuristics are not needed.

    `sync_catalog.speakers_from_title` exists because a YouTube title is all
    there is for most of this corpus; here the field is authoritative, which is
    also why these names bypass the "overused name" filter downstream.
    """
    out = []
    for s in talk.get("speakers") or []:
        name = " ".join((s.get("name") or "").split()) if isinstance(s, dict) else str(s)
        if name and name not in out:
            out.append(name)
    return out


def seed_record(talk: dict, tr: dict | None) -> dict:
    return {
        "video_id": talk["video_id"],
        "title": " ".join(talk["title"].split()),
        "duration_s": duration_s(talk, tr),
        "description": (talk.get("description") or "").strip() or None,
        "speakers": speaker_names(talk),
        # The agenda's tracks and topic tags. They read like YouTube tags to
        # everything downstream, and the AI-relevance test matches on them.
        "tags": [t for t in ([talk.get("track")] + list(talk.get("tags") or [])) if t],
        # When the talk was *given*. Not a YouTube upload timestamp, which the
        # agenda API does not know — see STATE.md.
        "published_at": talk.get("starts_at"),
        "session_page": talk.get("session_page"),
    }


def convert_transcript(src: dict, talk: dict, conference: str, origin: str) -> dict:
    """kb's schema keyed by its own talk id -> this repo's, keyed by video id."""
    return {
        "video_id": talk["video_id"],
        "title": " ".join(talk["title"].split()),
        "conference": conference,
        "language": src.get("language", "en"),
        "auto_generated": src.get("auto_generated", True),
        "source": src.get("source", "yt"),
        "timing": src.get("timing", "exact"),
        "word_count": src.get("word_count", 0),
        "imported_from": origin,
        "segments": src["segments"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=pathlib.Path, default=DEFAULT_KB,
                    help=f"the corpus to import from (default: {DEFAULT_KB})")
    ap.add_argument("--conference", default="wearedevelopers",
                    help="registry slug the talks belong to")
    ap.add_argument("--name", default="wearedevelopers-wwc26",
                    help="seed file name, without .json")
    ap.add_argument("--label", default="World Congress 2026",
                    help="edition label carried onto every imported talk")
    ap.add_argument("--year", type=int, default=2026)
    ap.add_argument("--channel",
                    help="YouTube channel to record (default: whichever one the "
                         "conference's already-enumerated videos come from)")
    ap.add_argument("--origin", default="presentations/kb (WeAreDevelopers agenda API)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    reg = atu.load_registry()
    if args.conference not in {c["slug"] for c in reg["conferences"]}:
        sys.exit(f"unknown conference slug: {args.conference}")

    # The seeded talks are on the same channel as the rest of the conference —
    # they are simply not on its /videos tab. Reading it off the catalogue keeps
    # the field consistent without hard-coding a channel name in a generic tool.
    channel = args.channel
    if not channel:
        seen = collections.Counter(v.get("channel") for v
                                   in atu.load_catalog(args.conference).get("videos", {}).values()
                                   if v.get("channel"))
        channel = seen.most_common(1)[0][0] if seen else None

    talks, tr_dir = read_kb(args.kb)
    records, copied, kept, no_transcript = [], 0, 0, 0

    for talk in talks:
        vid = talk.get("video_id") or atu.video_id(talk.get("recording_url"))
        if not vid:
            continue
        talk = {**talk, "video_id": vid}

        src_path = tr_dir / f"{talk['id']}.json"
        tr = None
        if src_path.exists():
            with src_path.open(encoding="utf-8") as f:
                tr = json.load(f)
        else:
            no_transcript += 1

        records.append(seed_record(talk, tr))

        if not tr or not tr.get("segments"):
            continue
        dest = atu.transcript_path(vid)
        if dest.exists():
            # Somebody — the fetcher, or an earlier import — already has this
            # one. Ours is not better by construction, and overwriting would
            # silently discard an exact transcript for another exact one.
            kept += 1
            continue
        if not args.dry_run:
            atu.write_json(dest, convert_transcript(tr, talk, args.conference, args.origin))
        copied += 1

    records.sort(key=lambda r: r["video_id"])
    seed = {
        "conference": args.conference,
        "channel": channel,
        "label": args.label,
        "year": args.year,
        "source": args.origin,
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "count": len(records),
        "videos": records,
    }
    path = SEEDS / f"{args.name}.json"
    if not args.dry_run:
        atu.write_json(path, seed)

    dur = sum(1 for r in records if r["duration_s"])
    print(f"{len(records)} talks from {args.kb} · channel {channel or 'unknown'}")
    print(f"  {sum(1 for r in records if r['description'])} with a description · "
          f"{sum(1 for r in records if r['speakers'])} with speakers · "
          f"{dur} with a duration")
    print(f"  {copied} transcripts copied · {kept} already present · "
          f"{no_transcript} talks had none")
    print(f"  {'would write' if args.dry_run else 'wrote'} {path.relative_to(atu.ROOT)}")
    print("\nnext: register the seed as a source in conferences.json, then\n"
          "      python3 sync_catalog.py && python3 build_index.py")


if __name__ == "__main__":
    main()
