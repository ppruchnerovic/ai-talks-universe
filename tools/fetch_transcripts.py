#!/usr/bin/env python3
"""Fetch YouTube transcripts for talks in the knowledge base.

Four routes, tried cheapest first:

  1. youtube-transcript-api — real caption timings ("timing": "exact"), so a
     search hit deep-links to the precise second. Only works from an IP YouTube
     has not flagged, which in practice means a normal home connection: from CI
     runners and cloud containers it returns 429 / "Sign in to confirm you're
     not a bot". A corporate proxy counts as a datacenter IP too.

  2. yt-dlp — also exact, and reaches the caption track through a different
     Innertube client, so it sometimes works when route 1 is refused.

  3. supadata.ai — exact timings fetched from *their* IPs, so the per-IP quota
     below does not apply. Needs SUPADATA_API_KEY and costs a credit a talk.

  4. kome.ai — also fetches server-side, free, but returns plain text with no
     timing. Starts are interpolated from word position ("timing":
     "estimated"), which lands you near a quote rather than exactly on it.

READ THIS BEFORE A BIG RUN. YouTube meters the caption endpoint per egress IP
with an allowance that refills over hours; a consumer connection yields roughly
20-25 talks before it closes, and slowing down does not raise that number. Only
two things do: more egress IPs, or a route that egresses from somebody else's.

    python3 fetch_transcripts.py --probe                  # is this network usable?
    python3 fetch_transcripts.py --priority 1 --limit 25  # ration a sitting
    python3 fetch_transcripts.py --min-year 2026          # spend it on this year
    python3 fetch_transcripts.py --proxy-file ~/proxies.txt --priority 1
    python3 fetch_transcripts.py --source supadata --priority 1
    python3 fetch_transcripts.py --retry-after 20         # park on a block, resume

Given proxies, the fetcher treats each one as a separate identity with its own
allowance: a block benches that identity for --proxy-cooldown minutes and the
run carries on down the others, so N usable IPs is worth roughly N sittings.

A block is *not* recorded as a miss — it says nothing about the video — so a
plain rerun picks the remaining talks straight back up.
data/transcripts/_misses.json means "this video has no captions";
`--retry-misses` forces another attempt.

Re-running will NOT upgrade an estimated transcript to an exact one — it skips
talks already fetched. Delete the ones you want redone first.

Every route asks for LANGUAGES and takes the best track the video offers. A
video whose only captions are off that list is still fetched and filed under
its real language — it has captions, so it is never recorded as a miss — and
the run says so as it saves.

Output: data/transcripts/<video_id>.json
    {"video_id":"...","title":"...","language":"en","timing":"exact",
     "word_count":4210,"segments":[{"start":12.3,"duration":4.1,"text":"..."}]}
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

import atu

KOME_API = "https://kome.ai/api/transcript"
SUPADATA_API = "https://api.supadata.ai/v1/transcript"
# Default parallelism for a run that egresses from somebody else's IPs. Their
# rate limit is not published, so 429 backs off and retries rather than being
# fatal, and this is a starting point to raise with --workers, not a ceiling.
OFF_IP_WORKERS = 8
# Sent to supadata and kome — both plain HTTP APIs, neither of them YouTube, so
# there is nothing here a browser string buys. It costs, though: a corporate
# TLS-inspecting proxy (Zscaler here) reads a Chrome UA on an API call as web
# browsing and answers with an HTML "Browser Isolation" interstitial at HTTP
# 200, which arrives as a JSONDecodeError and retires the route. Name the client
# honestly and the same request is passed through untouched. The YouTube routes
# do not use this: youtube-transcript-api and yt-dlp bring their own.
UA = "ai-talks-universe/1.0 (+https://github.com/ppruchnerovic/ai-talks-universe)"

MISSES = atu.TRANSCRIPTS / "_misses.json"

# Preference order. `en` variants first, then the majors these conferences use.
LANGUAGES = ["en", "en-US", "en-GB", "de", "es", "fr", "pt", "it", "nl", "ja", "pl", "uk"]
# Same list for yt-dlp, whose --sub-langs takes patterns. `en.*` catches the
# auto track YouTube names `en-orig`.
YTDLP_SUB_LANGS = "en.*,en,de,es,fr,pt,it,nl,ja,pl,uk"


def base_lang(code: str | None) -> str:
    """'en-US' / 'en-orig' / 'EN' -> 'en'. Nothing in, nothing out.

    Every route names languages differently — youtube-transcript-api returns
    BCP-47 ("en-GB"), yt-dlp names the file after the track ("en-orig"), and
    supadata takes and returns bare ISO 639-1 ("en") — so anything that
    compares them has to compare the base tag.
    """
    return re.split(r"[-_]", (code or "").strip().lower(), maxsplit=1)[0]


# The base tags of LANGUAGES, first occurrence winning, so a comparison against
# a route's own spelling is a dict lookup rather than a scan.
LANG_RANK: dict[str, int] = {}
for _i, _l in enumerate(LANGUAGES):
    LANG_RANK.setdefault(base_lang(_l), len(LANG_RANK))


# What a route says when it cannot name the language. supadata answers "none"
# for a caption track it served but could not identify — ten transcripts in this
# corpus are filed that way — and the rest are the usual placeholders. All of
# them mean the same thing, and "und" is the code that says it.
UNNAMED_LANGS = {"", "none", "null", "nil", "unknown", "und", "zxx"}


def named_lang(code: str | None) -> str:
    """The language as it should be recorded: verbatim, or 'und' if unnameable."""
    code = str(code or "").strip()
    return "und" if code.lower() in UNNAMED_LANGS else code


def lang_ok(code: str | None) -> bool:
    """Is this one of the languages LANGUAGES asks for?

    LANGUAGES is a *preference order for choosing among the tracks a video
    offers*, not a list of what the corpus may hold. So this decides which
    track to ask for and which to prefer on a retry — never whether a talk is
    worth keeping. A video whose only captions are off this list still has
    captions, and writing it to _misses.json would be a lie; see save().
    """
    return base_lang(code) in LANG_RANK


class BlockedError(Exception):
    """YouTube refused this IP, rather than this video."""


class AccountError(Exception):
    """A route refused the account, rather than this video.

    An empty balance or a bad key is not a fact about the talk, and unlike a
    block it is not something another identity would answer differently — so
    it neither benches an egress nor gets cached as a miss.
    """


class TransientError(Exception):
    """The route broke in a way that will probably work next time.

    A timeout, a run of 5xx, a job that never finished. None of them is a
    verdict on the video, so the talk goes back in the queue. Unlike a block it
    benches nothing: what failed was the far end, and our own identities are
    fine.
    """


def is_block(e: Exception) -> bool:
    """A network verdict, not a fact about the talk — so never cached as a miss."""
    if isinstance(e, BlockedError):
        return True
    name = type(e).__name__
    return any(k in name for k in ("IpBlocked", "TooManyRequests", "RequestBlocked"))


def about_the_video(e: Exception) -> bool:
    """Is this failure a verdict on the talk, and so safe to write to _misses.json?

    That file means "this video has no captions" and `select()` skips every id
    in it on all later runs, so anything recorded there is lost until someone
    passes --retry-misses. A refusal aimed at our IP, at our account, or at
    nobody in particular says nothing about the video and must stay retryable.
    """
    return not is_block(e) and not isinstance(e, (AccountError, TransientError))


# --- egress identities -------------------------------------------------------

def redact(url: str) -> str:
    """Proxy URLs carry credentials, and this script prints its egress a lot."""
    return re.sub(r"//[^/@]*@", "//", url)


def normalise_proxy(s: str) -> str:
    """Accept what proxy vendors actually hand you.

    Webshare and most residential pools export `host:port:user:pass` a line at
    a time; typing that back out as a URL by hand is exactly the sort of thing
    that silently produces an unauthenticated proxy and a mystifying 407.
    """
    s = s.strip()
    if "://" in s:
        return s
    parts = s.split(":")
    if len(parts) == 4:
        host, port, user, pw = parts
        user, pw = (urllib.parse.quote(x, safe="") for x in (user, pw))
        return f"http://{user}:{pw}@{host}:{port}"
    return f"http://{s}"


class Egress:
    """One identity to fetch from: a proxy URL, or None for this machine's IP.

    What YouTube meters is an allowance per egress IP, so strikes, fetch count
    and the bench deadline live here rather than in a module global. A blocked
    identity costs the run that identity's remaining share of the round, and
    nothing more.
    """

    def __init__(self, url: str | None):
        self.url = url
        self.label = "direct" if url is None else redact(url)
        self.strikes = 0            # consecutive route-1 failures
        self.fetched = 0
        self.blocked_until = 0.0
        self._api = None

    @property
    def api(self):
        # Built on first use: a pool of 20 proxies should not construct 20
        # sessions for a run that gets blocked after two.
        if self._api is None:
            self._api = build_api(self.url)
        return self._api

    def available(self) -> bool:
        return time.time() >= self.blocked_until


class Pool:
    """The set of egress identities, leased one thread at a time.

    Two parallel requests down the same IP spend that IP's allowance twice as
    fast for no extra throughput — spreading the load is the entire point — so
    an identity is leased exclusively and `--workers` above the pool size just
    queues.
    """

    def __init__(self, urls: list[str | None], cooldown_min: float):
        self.entries = [Egress(u) for u in urls]
        self.cooldown = cooldown_min * 60
        self._cond = threading.Condition()
        self._busy: set[int] = set()

    def acquire(self) -> Egress | None:
        """An idle, unbenched identity. None means every one of them is benched."""
        with self._cond:
            while True:
                free = [e for e in self.entries
                        if e.available() and id(e) not in self._busy]
                if free:
                    e = min(free, key=lambda e: e.fetched)
                    self._busy.add(id(e))
                    return e
                if self.all_benched():
                    return None
                self._cond.wait(timeout=5)      # also re-checks bench expiry

    def release(self, e: Egress) -> None:
        with self._cond:
            self._busy.discard(id(e))
            self._cond.notify_all()

    def bench(self, e: Egress) -> None:
        with self._cond:
            e.blocked_until = time.time() + self.cooldown
            e.strikes = 0
            self._cond.notify_all()

    def all_benched(self) -> bool:
        return all(not e.available() for e in self.entries)

    def recovers_in(self) -> float:
        soonest = min((e.blocked_until for e in self.entries), default=0.0)
        return max(0.0, soonest - time.time())


# --- route 4: kome.ai --------------------------------------------------------

def kome_length_seconds(s: str) -> float:
    """kome.ai reports '26m 12s' / '1h 2m 3s'. Returns 0 if unparseable."""
    m = re.fullmatch(r"\s*(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?\s*", s or "")
    if not m or not (s or "").strip():
        return 0.0
    h, mn, sec = (int(g) if g else 0 for g in m.groups())
    return h * 3600 + mn * 60 + sec


def fetch_kome(video_id: str) -> tuple[list[dict], str, float]:
    """Server-side caption fetch, used when YouTube has flagged this IP.

    Returns plain text with no timing, so starts are interpolated from word
    position across the runtime. Good enough to jump near a quote; not frame
    accurate. Marked timing='estimated' so nothing downstream presents it
    as exact.
    """
    req = urllib.request.Request(
        KOME_API,
        data=json.dumps({"video_id": atu.WATCH.format(vid=video_id),
                         "format": True}).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": UA},
        method="POST",
    )
    last = None
    for attempt in range(4):
        if attempt:
            time.sleep(2 ** attempt + random.uniform(0, 1.5))
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            break
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            last = e
    else:
        raise last

    text = (data.get("transcript") or "").strip()
    if not text:
        raise LookupError("kome returned an empty transcript")
    if data.get("hasMore"):
        # A truncated transcript silently misrepresents the talk — refuse it.
        raise LookupError("kome returned a truncated transcript (hasMore)")

    total = kome_length_seconds(str(data.get("length") or ""))
    lines = [l for l in text.splitlines() if l.strip()] or [text]
    # Shared with infoq.py, the other route whose text arrives without timings.
    return atu.segment_plain_text(lines, total), "en", total


# --- route 3: supadata.ai ----------------------------------------------------

_supadata_off: list[str] = []   # non-empty once the account's credits ran out


def supadata_key() -> str | None:
    return (os.environ.get("SUPADATA_API_KEY") or "").strip() or None


def _supadata_get(url: str, key: str) -> tuple[int, dict]:
    req = urllib.request.Request(url, headers={"x-api-key": key, "User-Agent": UA})
    last = None
    for attempt in range(4):
        if attempt:
            time.sleep(2 ** attempt + random.uniform(0, 1.5))
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read().decode("utf-8")
                if body.lstrip()[:9].lower().startswith(("<!doctype", "<html")):
                    # HTML at HTTP 200 from a JSON API is not supadata
                    # answering: it is something between here and there
                    # answering for it. Say so once, rather than retrying an
                    # interstitial four times and reporting a parse error.
                    raise TransientError(
                        "supadata: an intercepting proxy returned HTML, not the "
                        "API's JSON — see the UA note at the top of this file")
                return resp.status, (json.loads(body) if body.strip() else {})
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # The one account-level refusal that waiting *does* fix, and
                # with several workers on one key it is the expected way to
                # find the ceiling. Back off and retry; retiring the route on
                # it would let one busy moment cost the rest of the run.
                last = e
                continue
            if e.code in (401, 402):
                # Account-level, not IP-level: no other proxy and no amount of
                # waiting inside this run fixes it, so retire the route rather
                # than spend a failed request on every remaining talk.
                why = {401: "bad API key", 402: "out of credits"}[e.code]
                if not _supadata_off:
                    print(f"   (supadata: {why} — dropping that route for this run)")
                _supadata_off.append(why)
                # AccountError, not LookupError: retiring the route is about
                # the account, and the talk in flight when the balance hit zero
                # has told us nothing about its captions. As a LookupError it
                # went to _misses.json as "no captions", permanently, and with
                # --workers 32 every request in flight at that moment went with
                # it.
                raise AccountError(f"supadata: {why}")
            if e.code < 500:
                detail = " ".join(e.read().decode("utf-8", "replace").split())[:160]
                raise LookupError(f"supadata: HTTP {e.code} {detail}")
            last = e
        except (urllib.error.URLError, TimeoutError, ConnectionError,
                json.JSONDecodeError) as e:
            last = e
    if isinstance(last, urllib.error.HTTPError) and last.code == 429:
        # Outlasted the backoff. That is a verdict on how hard we are pushing,
        # not on the video, so the talk goes back in the queue rather than into
        # _misses.json — and the route stays on for everybody else.
        raise BlockedError("supadata: rate limited after 4 attempts")
    # Four attempts of 5xx, timeouts, dropped connections or unreadable JSON.
    # Raised bare, these reached the runners as an HTTPError or a URLError,
    # which about_the_video() would wave through into _misses.json — a supadata
    # outage would have cost a talk each, permanently.
    raise TransientError(f"supadata: {type(last).__name__} after 4 attempts "
                         f"({str(last)[:120]})")


def _supadata_once(video_id: str, key: str,
                   lang: str) -> tuple[list[dict], str, list[str]]:
    """One transcript request, polled to completion. Costs one credit.

    Returns the segments, the language the text actually came back in, and the
    other languages the video offers.
    """
    q = urllib.parse.urlencode({"url": atu.WATCH.format(vid=video_id),
                                "lang": lang,
                                "mode": "native"})
    status, data = _supadata_get(f"{SUPADATA_API}?{q}", key)

    if status == 202 and data.get("jobId"):
        job = str(data["jobId"])
        deadline = time.time() + 900
        while True:
            time.sleep(6)
            _s, data = _supadata_get(f"{SUPADATA_API}/{urllib.parse.quote(job)}", key)
            state = data.get("status")
            if state == "completed":
                break
            if state == "failed":
                raise LookupError(f"supadata: job failed "
                                  f"({str(data.get('error'))[:120]})")
            if time.time() > deadline:
                # Their queue was slow, which says nothing about the captions —
                # and the credit is already spent, so the talk must stay
                # fetchable rather than be written off as having none.
                raise TransientError("supadata: job still running after 15 minutes")

    content = data.get("content")
    if not content or isinstance(content, str):
        # 206 lands here too: the account was charged, the video has no captions.
        raise LookupError("supadata: no timed transcript for this video")

    segments = []
    for c in content:
        text = " ".join(str(c.get("text") or "").split())
        if not text:
            continue
        segments.append({"start": round(float(c.get("offset") or 0) / 1000.0, 2),
                         "duration": round(max(float(c.get("duration") or 0) / 1000.0,
                                               0.5), 2),
                         "text": text})
    if not segments:
        raise LookupError("supadata returned an empty transcript")
    got = data.get("lang") or content[0].get("lang") or lang
    available = [str(a) for a in (data.get("availableLangs") or []) if a]
    return segments, got, available


def fetch_supadata(video_id: str, key: str) -> tuple[list[dict], str]:
    """Exact timings from a third party's IPs, so the per-IP quota does not bind.

    `mode=native` asks only for captions YouTube already has — one credit, and
    a video with none comes back 206 rather than being transcribed from audio
    at two credits a minute. Anything over 20 minutes is handed back as a job
    to poll, which here is most of the corpus: it fetches longest talks first.

    `lang` is the parameter that decides *which* track, and omitting it is how
    ten English-language talks came back as Devanagari transliterations that
    then indexed as though they were the talk. Supadata does not fail when the
    preferred language is absent — it "will return a transcript in the first
    available language and a list of other available languages" — so asking is
    only half of it: the answer has to be checked, and `availableLangs` is what
    the documented remedy re-requests against. That second request costs a
    second credit, so it is made only when the first answer is off LANGUAGES
    *and* the video demonstrably offers something on it — never on the happy
    path, and never more than once.
    """
    want = base_lang(LANGUAGES[0])
    segments, got, available = _supadata_once(video_id, key, want)
    if lang_ok(got):
        return segments, got

    alt = min((a for a in available
               if lang_ok(a) and base_lang(a) != base_lang(got)),
              key=lambda a: LANG_RANK[base_lang(a)], default=None)
    if alt is None:
        # The video's only captions are in a language this corpus does not ask
        # for. That is not "no captions" and must never be recorded as one —
        # see save(), which keeps the track and files it under its real
        # language.
        return segments, got
    segments, got, _ = _supadata_once(video_id, key, base_lang(alt))
    return segments, got


# --- route 2: yt-dlp ---------------------------------------------------------

def ytdlp_binary() -> str | None:
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    return local if os.path.exists(local) else shutil.which("yt-dlp")


def parse_json3(path: str) -> list[dict]:
    """YouTube's json3 caption format -> our segment shape.

    Auto-generated tracks carry the text twice: real events, plus 'aAppend'
    rollup events that repeat the previous line so the caption box can scroll.
    Keeping those would duplicate most of the transcript.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    out = []
    for ev in data.get("events") or []:
        if ev.get("aAppend"):
            continue
        text = " ".join("".join(s.get("utf8", "") for s in (ev.get("segs") or [])).split())
        if not text:
            continue
        out.append({"start": round(float(ev.get("tStartMs", 0)) / 1000.0, 2),
                    "duration": round(max(float(ev.get("dDurationMs", 0)) / 1000.0, 0.5), 2),
                    "text": text})
    return out


def fetch_ytdlp(video_id: str, proxy: str | None = None) -> tuple[list[dict], str]:
    exe = ytdlp_binary()
    if not exe:
        raise LookupError("yt-dlp is not installed")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [exe, "--skip-download", "--write-auto-subs", "--write-subs",
               "--sub-langs", YTDLP_SUB_LANGS, "--sub-format", "json3",
               "--no-warnings", "--no-progress",
               "-o", os.path.join(tmp, "%(id)s.%(ext)s"),
               atu.WATCH.format(vid=video_id)]
        if proxy:
            cmd += ["--proxy", proxy]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        found = sorted(glob.glob(os.path.join(tmp, "*.json3")))
        if not found:
            err = (proc.stderr or proc.stdout or "").strip().splitlines()
            detail = err[-1][:160] if err else "no caption file written"
            # yt-dlp reports a throttle in stderr rather than its exit code, so
            # surface it under the name the block handling looks for.
            if "429" in detail or "Too Many Requests" in detail or "not a bot" in detail:
                raise BlockedError(f"yt-dlp: {detail}")
            raise LookupError(f"yt-dlp: {detail}")

        def rank(p: str) -> int:
            tag = os.path.basename(p).split(".")[-2].lower()
            for i, want in enumerate(LANGUAGES):
                if tag == want.lower() or tag.startswith(want.lower()):
                    return i
            return len(LANGUAGES)

        best = min(found, key=rank)
        segments = parse_json3(best)
        if not segments:
            raise LookupError("yt-dlp: caption file had no usable events")
        return segments, os.path.basename(best).split(".")[-2].replace("-orig", "")


# --- route 1: youtube-transcript-api ----------------------------------------

def build_api(proxy: str | None):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        sys.exit("youtube-transcript-api is not installed:\n"
                 "    pip install -r tools/requirements.txt")
    if proxy:
        from youtube_transcript_api.proxies import GenericProxyConfig

        return YouTubeTranscriptApi(proxy_config=GenericProxyConfig(http_url=proxy,
                                                                    https_url=proxy))
    return YouTubeTranscriptApi()


def pick_and_fetch(api, video_id: str):
    """Return (raw segments, language, is_generated). Prefers a manual track.

    The language returned is the language of the text that was actually
    fetched, not of the track it came from. The last-resort branch translates,
    and reporting the source track's code there would file a talk under a
    language its transcript is not in — the `language` field is the only record
    of what a file contains, so it has to be the one thing that cannot drift.

    That branch also has to be careful in the other direction: a video with a
    track that will not translate into English still has captions, so a failed
    translation falls back to the untranslated track rather than raising. Left
    to propagate, `TranslationLanguageNotAvailable` is neither a block, an
    account refusal nor a transient — so about_the_video() waves it into
    _misses.json as "this video has no captions", which it demonstrably has.
    """
    listing = api.list(video_id)
    transcript = None
    language = None
    try:
        transcript = listing.find_manually_created_transcript(LANGUAGES)
    except Exception:
        try:
            transcript = listing.find_generated_transcript(LANGUAGES)
        except Exception:
            # Nothing on the preference list. A track that translates into it
            # beats one that does not, whatever order the listing is in.
            tracks = list(listing)
            want = base_lang(LANGUAGES[0])
            t = next((t for t in tracks if t.is_translatable),
                     tracks[0] if tracks else None)
            if t is not None:
                transcript, language = t, t.language_code
                if t.is_translatable:
                    try:
                        transcript, language = t.translate(want), want
                    except Exception:
                        pass
    if transcript is None:
        raise LookupError("no transcript tracks")
    fetched = transcript.fetch()
    raw = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
    return raw, language or transcript.language_code, transcript.is_generated


def _route_yta(eg: Egress, vid: str):
    raw, lang, generated = pick_and_fetch(eg.api, vid)
    segments = [
        {"start": round(float(s["start"]), 2),
         "duration": round(float(s["duration"]), 2),
         "text": " ".join(str(s["text"]).split())}
        for s in raw if str(s.get("text", "")).strip()
    ]
    if not segments:
        raise LookupError("caption track was empty")
    return segments, lang, generated, "exact"


def _route_ytdlp(eg: Egress, vid: str):
    segments, lang = fetch_ytdlp(vid, eg.url)
    return segments, lang, True, "exact"


def _route_supadata(key: str, vid: str):
    segments, lang = fetch_supadata(vid, key)
    return segments, lang, True, "exact"


def _route_kome(vid: str):
    segments, lang, _total = fetch_kome(vid)
    return segments, lang, True, "estimated"


def uses_our_ip(source: str) -> bool:
    """Could any route this source allows egress from this machine at all?

    `supadata` and `kome` fetch from somebody else's infrastructure, so a run
    restricted to them has no IP allowance to ration and nothing to lease.
    """
    return source in ("auto", "exact", "youtube", "ytdlp")


def off_ip_sources(source: str, key: str | None) -> bool:
    """Is any route available that does not spend this machine's IP allowance?"""
    if source in ("auto", "kome"):
        return True
    return bool(key) and not _supadata_off and source in ("auto", "exact", "supadata")


def fetch_one(eg: Egress | None, vid: str, source: str, key: str | None = None):
    """Walk the routes, cheapest first, exact timings before estimates.

    A block is remembered rather than swallowed: the routes that egress from
    somebody else's IP still get their turn, and if none is configured the
    block is re-raised so the caller can bench that identity. The two routes
    that share our IP are skipped once one of them is blocked — the second
    would only spend a request to be told the same thing. What must never
    happen is a block quietly becoming an estimate: an unfetched talk is
    recoverable, a mislabelled transcript is not.
    """
    plan = []   # (name, uses_our_ip, thunk)
    if eg is not None and source in ("auto", "exact", "youtube"):
        if not (source == "auto" and eg.strikes >= 3):
            plan.append(("yt", True, lambda: _route_yta(eg, vid)))
    if eg is not None and source in ("auto", "exact", "ytdlp"):
        plan.append(("ytdlp", True, lambda: _route_ytdlp(eg, vid)))
    if key and not _supadata_off and source in ("auto", "exact", "supadata"):
        plan.append(("supa", False, lambda: _route_supadata(key, vid)))
    if source in ("auto", "kome"):
        plan.append(("kome", False, lambda: _route_kome(vid)))
    if not plan:
        raise BlockedError("every egress is blocked and no off-IP route is configured")

    blocked = last = None
    for name, ours, run in plan:
        if blocked is not None and ours:
            continue
        try:
            segments, lang, generated, timing = run()
            if name == "yt" and eg is not None:
                eg.strikes = 0
            return segments, lang, generated, timing, name
        except Exception as e:
            if len(plan) == 1:
                raise
            if is_block(e):
                blocked = e
                continue
            if name == "yt" and eg is not None:
                eg.strikes += 1
                if eg.strikes == 3:
                    print(f"   ({eg.label}: youtube-transcript-api keeps failing "
                          f"— yt-dlp from here on)")
            last = e
    raise blocked or last


# --- selection and bookkeeping ----------------------------------------------

def load_misses() -> dict:
    if MISSES.exists():
        with MISSES.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(t: dict, segments, lang, generated, timing, source) -> int:
    """Write one transcript, filed under the language it is actually in.

    A track in a language LANGUAGES does not ask for is kept, not discarded and
    not written to _misses.json. Three reasons, and the first is the only one
    that has to hold:

      * it would be a lie. _misses.json means "this video has no captions" and
        select() skips every id in it forever; a video with a Hindi-only track
        has captions, and cached as a miss it is lost.
      * "come back later" is a promise nobody can keep. A retryable non-verdict
        re-selects the talk on every run and spends a credit on it every time,
        and next month's answer is the same track — it never converges, and the
        cost is unbounded.
      * the corpus already holds twelve languages on purpose, so there is no
        line between "de" and "hi" except the preference list, which is about
        *which track to ask for*, not about which talks are worth having.

    So the language is recorded as it came back, and an off-list one is said
    out loud: the field is then the handle for finding these again
    (`language` not matching ^en over data/transcripts/), which a silently
    dropped talk would not have.
    """
    lang = named_lang(lang)    # "und", never a guessed "en"
    if not lang_ok(lang):
        print(f"   ({t['id']}: only a '{lang}' caption track — kept, filed as '{lang}')")
    words = sum(len(s["text"].split()) for s in segments)
    atu.write_json(atu.transcript_path(t["id"]), {
        "video_id": t["id"],
        "title": t["title"],
        "conference": t["conference"],
        "language": lang,
        "auto_generated": bool(generated),
        "source": source,
        "timing": timing,          # "exact" or "estimated"
        "word_count": words,
        "segments": segments,
    }, compact=True)
    return words


def select(talks: list[dict], args, misses: dict) -> list[dict]:
    out = []
    for t in talks:
        if args.only and t["conference"] not in args.only:
            continue
        if args.priority and t["priority"] > args.priority:
            continue
        if args.min_duration and (t["duration_min"] or 0) < args.min_duration:
            continue
        if not atu.year_wanted(t.get("year"), args):
            continue
        if atu.transcript_path(t["id"]).exists() or t["id"] in misses:
            continue
        out.append(t)
    # Highest-priority conferences first, then longest talks: a 45-minute
    # session carries more of what this corpus exists to find than a 6-minute
    # product spot, and the quota is the scarce thing.
    out.sort(key=lambda t: (t["priority"], -(t["duration_s"] or 0)))
    return out


BLOCK_ADVICE = (
    "\n!! Every egress is rate limited. Stopping so the rest stay retryable.\n"
    "   Wait a few hours, switch networks (a phone hotspot resets it), or add\n"
    "   IPs with --proxy / --proxy-file. A corporate VPN egresses from a\n"
    "   datacenter range and is blocked hardest — drop it before retrying.\n"
    "   SUPADATA_API_KEY buys exact timings that ignore the IP quota entirely.\n"
    "   Blocked talks are NOT recorded as misses, so a plain rerun picks\n"
    "   them up.\n"
)

ACCOUNT_ADVICE = (
    "\n!! The off-IP route refused the account ({why}). Stopping so the rest\n"
    "   stay retryable — nothing here was recorded as a miss.\n"
    "   Top up the supadata account, or run the free routes with\n"
    "   --source exact; those spend this machine's IP allowance instead.\n"
)


def stop_advice(e: Exception) -> str:
    """What to print when a round ends with nothing left to fetch with."""
    return ACCOUNT_ADVICE.format(why=e) if isinstance(e, AccountError) else BLOCK_ADVICE


def attempt(pool: Pool, t: dict, args, key: str | None, tries: int | None = None):
    """One talk, on one leased identity. Returns (words, timing, source).

    A block says nothing about the talk, so while any other identity is still
    standing the talk is retried there rather than deferred to the next round.
    Otherwise each identity, as it hits its limit, would cost a talk it never
    actually refused — with a pool of twenty that is twenty talks a round.
    """
    # One shot per identity, plus one for the routes that need none. Capped,
    # because a talk that has been refused by eight IPs is better left to the
    # next round than allowed to walk the whole pool.
    #
    # A source that cannot touch our IP has nothing to lease. The pool exists
    # so that two workers never spend one IP's allowance at once; supadata
    # spends somebody else's, so leasing anyway would pin the whole run to the
    # single direct identity and make --workers a lie. It is also the reason
    # not to pace: --min-delay meters an allowance this route does not draw on.
    off_ip_only = not uses_our_ip(args.source)
    tries = tries or (1 if off_ip_only else min(len(pool.entries) + 1, 8))
    for remaining in range(tries - 1, -1, -1):
        eg = None if off_ip_only else pool.acquire()   # None: every one benched
        try:
            if eg is not None:
                time.sleep(random.uniform(args.min_delay, args.max_delay))
            try:
                segments, lang, generated, timing, source = fetch_one(
                    eg, t["id"], args.source, key)
            except Exception as e:
                if eg is not None and is_block(e):
                    pool.bench(eg)
                    print(f"   {eg.label} rate limited after {eg.fetched} fetched "
                          f"— benched {args.proxy_cooldown:g} min")
                    if remaining and not spent(pool, args, key):
                        continue
                raise
            if eg is not None and source in ("yt", "ytdlp"):
                eg.fetched += 1
            return save(t, segments, lang, generated, timing, source), timing, source
        finally:
            if eg is not None:
                pool.release(eg)


def probe(pool: Pool, talks: list[dict], source: str, key: str | None) -> int:
    """One request per identity, to find out what this sitting is worth."""
    todo = [t for t in talks if not atu.transcript_path(t["id"]).exists()]
    if not todo:
        print("nothing left to fetch")
        return 0

    # An `auto` probe that fell through to kome would report "works" for an IP
    # that is entirely spent, which is the opposite of what a probe is for.
    per_ip = "exact" if source == "auto" else source
    usable = 0
    if per_ip != "supadata":
        for eg, t in zip(pool.entries, todo):
            print(f"{eg.label:<34} probing with: {t['title'][:40]}")
            try:
                segments, lang, _g, timing, src = fetch_one(eg, t["id"], per_ip, None)
            except Exception as e:
                verdict = ("BLOCKED — spent" if is_block(e)
                           else f"failed: {type(e).__name__}")
                print(f"  {verdict}: {str(e)[:120]}")
                continue
            usable += 1
            words = sum(len(s["text"].split()) for s in segments)
            print(f"  ok — {words:,} words via {src} ({timing} timings, {lang})")

    if key and source in ("auto", "exact", "supadata"):
        t = todo[len(pool.entries) % len(todo)]
        print(f"{'supadata':<34} probing with: {t['title'][:40]}  (spends 1 credit)")
        try:
            segments, lang, _g, timing, src = fetch_one(None, t["id"], "supadata", key)
            usable += 1
            words = sum(len(s["text"].split()) for s in segments)
            print(f"  ok — {words:,} words via {src} ({timing} timings, {lang})")
        except Exception as e:
            print(f"  failed: {type(e).__name__}: {str(e)[:120]}")

    print(f"\n{usable} usable route(s). "
          + ("Go." if usable else "Nothing here will fetch — see --help."))
    return 0 if usable else 1


def build_pool(args) -> Pool:
    urls: list[str | None] = [normalise_proxy(p) for p in args.proxy]
    if args.proxy_file:
        with open(os.path.expanduser(args.proxy_file), encoding="utf-8") as f:
            for line in f:
                line = line.split("#")[0].strip()
                if line:
                    urls.append(normalise_proxy(line))
    seen, uniq = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    # With proxies configured, the local IP stays out of it unless asked for:
    # it is usually the one already spent, and the reason to buy IPs is to stop
    # burning it. Without any, it is all there is.
    if not uniq or args.with_direct:
        uniq.insert(0, None)
    return Pool(uniq, args.proxy_cooldown)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source",
                    choices=("auto", "exact", "youtube", "ytdlp", "supadata", "kome"),
                    default="auto",
                    help="auto: exact timings if YouTube allows it, else kome.ai. "
                         "exact: never fall back to estimates")
    ap.add_argument("-c", "--conference", action="append", dest="only", default=[])
    ap.add_argument("--priority", type=int,
                    help="only conferences at or above this registry priority")
    ap.add_argument("--min-duration", type=int, default=0, metavar="MINUTES")
    atu.add_year_args(ap)
    ap.add_argument("--limit", type=int, help="only attempt the first N talks")
    ap.add_argument("--workers", type=int, default=None,
                    help="parallel fetches (default: one per egress identity, min 2, "
                         "max 8). Each identity is still used by one worker at a "
                         "time, so raising this past the pool size only queues")
    ap.add_argument("--retry-misses", action="store_true")
    ap.add_argument("--probe", action="store_true",
                    help="fetch one transcript per egress and report what works")
    ap.add_argument("--proxy", action="append", default=[], metavar="URL",
                    help="http(s) proxy, repeatable. Accepts a URL or the "
                         "host:port:user:pass line proxy vendors export")
    ap.add_argument("--proxy-file", metavar="PATH",
                    help="one proxy per line (# comments allowed); each is a "
                         "separate quota, and a blocked one is benched, not fatal")
    ap.add_argument("--proxy-cooldown", type=float, default=45, metavar="MINUTES",
                    help="how long a blocked identity sits out (default 45)")
    ap.add_argument("--with-direct", action="store_true",
                    help="also use this machine's own IP when proxies are configured")
    ap.add_argument("--min-delay", type=float, default=3.0)
    ap.add_argument("--max-delay", type=float, default=7.0)
    ap.add_argument("--retry-after", type=float, default=0, metavar="MINUTES",
                    help="when every identity is blocked, wait at least this long "
                         "and resume where it stopped. 0 (default) stops")
    ap.add_argument("--max-rounds", type=int, default=24)
    args = ap.parse_args()

    talks = atu.load_talks()
    atu.TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    misses = {} if args.retry_misses else load_misses()
    pool = build_pool(args)
    key = supadata_key()
    if args.workers is None:
        # One worker per identity is right when an IP allowance is the limit.
        # An off-IP-only run is limited by the far end's rate limit instead, so
        # the pool size says nothing about how many requests are sensible.
        args.workers = (OFF_IP_WORKERS if not uses_our_ip(args.source)
                        else max(2, min(len(pool.entries), 8)))

    if args.source == "supadata" and not key:
        sys.exit("--source supadata needs SUPADATA_API_KEY in the environment")
    print(f"egress: {', '.join(e.label for e in pool.entries)}"
          f"{' + supadata' if key else ''} · {args.workers} workers")

    if args.probe:
        sys.exit(probe(pool, select(talks, args, {}), args.source, key))

    total_ok = total_fail = 0
    for rnd in range(1, args.max_rounds + 1):
        # Each round re-derives its work from disk, so a blocked round costs
        # nothing but time — nothing is lost and nothing is refetched.
        todo = select(talks, args, misses)
        have = sum(1 for t in talks if atu.transcript_path(t["id"]).exists())
        off_year = sum(1 for t in talks if not atu.year_wanted(t.get("year"), args))
        label = f"round {rnd}: " if rnd > 1 else ""
        print(f"{label}{len(talks)} talks · {have} already fetched · "
              f"{len(misses)} known misses · "
              f"{f'{off_year} outside the year filter · ' if off_year else ''}"
              f"{len(todo)} selected\n")
        if not todo:
            break
        if args.limit:
            todo = todo[: args.limit]

        runner = run_parallel if args.workers > 1 else run_serial
        ok, fail, blocked = runner(pool, todo, misses, args, key)
        total_ok += ok
        total_fail += fail
        atu.write_json(MISSES, misses)

        if not blocked or not args.retry_after or args.limit:
            break
        if rnd == args.max_rounds:
            print(f"\ngiving up after {rnd} blocked rounds — rerun when the quota recovers")
            break
        # Resuming before the identities come off the bench just spends a round
        # discovering they are still benched.
        wait = max(args.retry_after * 60, pool.recovers_in())
        print(f"waiting {wait / 60:.0f} min for the quota to recover, then resuming "
              f"({total_ok} fetched so far)\n", flush=True)
        try:
            time.sleep(wait)
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            break

    atu.write_json(MISSES, misses)
    print(f"\ndone: {total_ok} fetched, {total_fail} missed. Misses recorded in {MISSES.name}")
    if total_ok:
        print("Next:  python3 sync_catalog.py && python3 build_index.py")


def spent(pool: Pool, args, key: str | None) -> bool:
    """Nothing left to fetch with: every IP benched and no route off them.

    When the source never uses our IP the pool is not evidence of anything —
    its identities are idle rather than working, so asking whether they are all
    benched would answer "no" forever and the round would never end.
    """
    if not uses_our_ip(args.source):
        return not off_ip_sources(args.source, key)
    return pool.all_benched() and not off_ip_sources(args.source, key)


def run_parallel(pool, todo, misses, args, key):
    """Threads spend nearly all their time waiting on the network.

    Each worker sleeps before its request, so the request rate per identity is
    roughly 1 / mean-delay however many workers there are.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    blocked = threading.Event()
    ok = fail = done = 0

    def work(t):
        if blocked.is_set():
            raise BlockedError("skipped — run already stopped by a block")
        return attempt(pool, t, args, key)

    with ThreadPoolExecutor(max_workers=args.workers) as pool_ex:
        futures = {pool_ex.submit(work, t): t for t in todo}
        try:
            # This loop is the only thread touching the counters, so no lock.
            for fut in as_completed(futures):
                t = futures[fut]
                try:
                    words, timing, source = fut.result()
                except Exception as e:
                    if not about_the_video(e):
                        # A refusal aimed at our IP or our account says nothing
                        # about this video, so it is neither a miss nor an
                        # attempt. One identity being benched is normal and the
                        # run continues; nothing left to fetch with — every
                        # identity benched, or the off-IP route retired — ends
                        # the round.
                        if not is_block(e):
                            # A block is normal and is reported once, in
                            # BLOCK_ADVICE. The other two are rare enough that
                            # skipping silently would read as a talk that
                            # somehow never ran.
                            print(f"[{done}/{len(todo)}] LEFT {type(e).__name__:<24} "
                                  f"{t['title'][:48]}")
                        if spent(pool, args, key) and not blocked.is_set():
                            blocked.set()
                            print(stop_advice(e))
                        continue
                    done += 1
                    fail += 1
                    misses[t["id"]] = {"conference": t["conference"],
                                       "reason": type(e).__name__, "detail": str(e)[:200]}
                    print(f"[{done}/{len(todo)}] MISS {type(e).__name__:<24} {t['title'][:48]}")
                    continue
                done += 1
                ok += 1
                print(f"[{done}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} "
                      f"{t['title'][:48]}")
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            pool_ex.shutdown(wait=False, cancel_futures=True)
            return ok, fail, False
    return ok, fail, blocked.is_set()


def run_serial(pool, todo, misses, args, key):
    ok = fail = 0
    blocked = False
    for i, t in enumerate(todo, 1):
        label = t["title"][:52]
        try:
            words, timing, source = attempt(pool, t, args, key)
            ok += 1
            print(f"[{i}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {label}")
        except KeyboardInterrupt:
            print("\ninterrupted — progress is saved, rerun to continue")
            break
        except Exception as e:
            if not about_the_video(e):
                kind = ("BLOCKED" if is_block(e) else
                        "REFUSED" if isinstance(e, AccountError) else "LEFT")
                print(f"[{i}/{len(todo)}] {kind}  {label}")
                if spent(pool, args, key):
                    print(stop_advice(e))
                    blocked = True
                    break
                continue
            fail += 1
            misses[t["id"]] = {"conference": t["conference"],
                               "reason": type(e).__name__, "detail": str(e)[:200]}
            print(f"[{i}/{len(todo)}] MISS {type(e).__name__:<28} {label}")
    return ok, fail, blocked


if __name__ == "__main__":
    main()
