#!/usr/bin/env python3
"""Offline checks for fetch_transcripts.py — no network, no API key, no proxies.

What is worth testing here is not the HTTP calls but the bookkeeping around
them, because every mistake in it is expensive and quiet: a block recorded as a
miss loses a talk permanently, an estimate returned under --source exact
mislabels one, and a talk dropped on a benched identity costs a fetch nobody
notices. So the egress pool runs against fake allowances and the supadata route
against a faked HTTP layer, and both run in under a second.

    cd tools && python3 test_fetch_transcripts.py
"""

import argparse
import contextlib
import io
import json
import sys
import threading
import time
import types
import urllib.error
import urllib.request

sys.path.insert(0, ".")
import fetch_transcripts as F

# F.time is the time module itself, so this fakes sleeping everywhere — which
# is what we want for backoff and job polling, and not what we want for the
# one check that has to watch a bench deadline actually expire.
_REAL_SLEEP, _REAL_URLOPEN = time.sleep, urllib.request.urlopen
F.time.sleep = lambda s: None

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


print("\n-- enrich.py: what counts as a block --")
import enrich as EN
def enrich_marks(err):
    return any(m.lower() in err.lower() for m in EN.BLOCK_MARKERS)
check("a bot wall is a block", enrich_marks("ERROR: Sign in to confirm you're not a bot"))
check("a 429 is a block", enrich_marks("ERROR: HTTP Error 429: Too Many Requests"))
check("a geo-restricted video is not a block",
      not enrich_marks("ERROR: Video unavailable. The uploader has not made this video available "
                       "in your country — blocked in your country"))
check("a video about robots is not a block", not enrich_marks("ERROR: chatbot video is private"))

print("\n-- proxy parsing and redaction --")
check("url passthrough", F.normalise_proxy("http://a:b@h:1") == "http://a:b@h:1")
check("host:port", F.normalise_proxy("1.2.3.4:8080") == "http://1.2.3.4:8080")
check("webshare host:port:user:pass", F.normalise_proxy("1.2.3.4:8080:us er:p@ss")
      == "http://us%20er:p%40ss@1.2.3.4:8080", F.normalise_proxy("1.2.3.4:8080:us er:p@ss"))
check("redact creds", F.redact("http://user:secret@1.2.3.4:8080") == "http://1.2.3.4:8080")
check("label hides creds", "secret" not in F.Egress("http://u:secret@h:1").label)

print("\n-- pool leasing --")
p = F.Pool([None, "http://a:1", "http://b:2"], cooldown_min=0.01)
a, b, c = p.acquire(), p.acquire(), p.acquire()
check("leases each identity once", len({id(a), id(b), id(c)}) == 3)
check("exclusive lease", a is not b is not c)
for e in (a, b, c): p.release(e); p.bench(e)
check("all benched", p.all_benched())
check("acquire returns None when all benched", p.acquire() is None)
check("recovers_in positive", 0 < p.recovers_in() <= 0.6)
_REAL_SLEEP(0.7)
check("unbenched after cooldown", p.acquire() is not None)

# a blocked identity does not stop the others
p2 = F.Pool(["http://a:1", "http://b:2"], cooldown_min=10)
x = p2.acquire(); p2.release(x); p2.bench(x)
y = p2.acquire()
check("survivor still leasable", y is not None and y is not x)
check("not all benched with one alive", not p2.all_benched())

print("\n-- selection: the year filter --")
# The corpus keeps every year on purpose; what these flags scope is which of it
# is worth a metered fetch. A talk with no year yet is the interesting case:
# excluding it by default is what keeps --min-year honest here, and including it
# on demand is what makes the same flags usable on enrich.py.
# Eleven-character ids, because select() now refuses anything that is not a
# YouTube id — an InfoQ-only talk has no video to fetch a caption track from.
CORPUS = [{"id": f"v{y}aaaaaa", "title": str(y), "conference": "x", "priority": 1,
           "duration_min": 30, "duration_s": 1800, "year": y}
          for y in (2024, 2025, 2026)]
CORPUS.append({"id": "vnoneaaaaaa", "title": "undated", "conference": "x", "priority": 1,
               "duration_min": 30, "duration_s": 1800, "year": None})
CORPUS.append({"id": "iq-a-talk-only-on-infoq", "title": "infoq", "conference": "x", "priority": 1,
               "duration_min": 30, "duration_s": 1800, "year": 2026})
ALL = ["v2024aaaaaa", "v2025aaaaaa", "v2026aaaaaa", "vnoneaaaaaa"]


def sel(**kw):
    a = types.SimpleNamespace(only=[], priority=None, min_duration=0,
                              year=None, min_year=None, include_unknown_year=False)
    a.__dict__.update(kw)
    return [t["id"] for t in F.select(CORPUS, a, {})]


check("no year flags selects everything", sel() == ALL, sel())
check("--year takes that year only", sel(year=[2026]) == ["v2026aaaaaa"], sel(year=[2026]))
check("--year repeated is a set", sel(year=[2024, 2026]) == ["v2024aaaaaa", "v2026aaaaaa"],
      sel(year=[2024, 2026]))
check("--min-year takes that year onwards", sel(min_year=2025) == ["v2025aaaaaa", "v2026aaaaaa"],
      sel(min_year=2025))
check("unknown year is excluded by default", sel(min_year=2026) == ["v2026aaaaaa"],
      sel(min_year=2026))
check("--include-unknown-year keeps it",
      sel(min_year=2026, include_unknown_year=True) == ["v2026aaaaaa", "vnoneaaaaaa"],
      sel(min_year=2026, include_unknown_year=True))
check("--include-unknown-year alone widens nothing",
      sel(include_unknown_year=True) == ALL, sel(include_unknown_year=True))
check("year filter does not disturb the priority/duration sort",
      sel(min_year=2024) == ALL[:3], sel(min_year=2024))
check("an InfoQ-only talk is never selected for a YouTube fetch",
      not any(i.startswith("iq-") for i in sel()), sel())

ap = argparse.ArgumentParser(prog="t")
F.atu.add_year_args(ap)
check("--year parses repeatable ints", ap.parse_args(["--year", "2026", "--year", "2025"]).year
      == [2026, 2025])
err = io.StringIO()
with contextlib.redirect_stderr(err):
    try:
        ap.parse_args(["--year", "2026", "--min-year", "2025"])
        code = None
    except SystemExit as e:
        code = e.code
check("--year and --min-year are mutually exclusive",
      code == 2 and "not allowed with" in err.getvalue(), (code, err.getvalue()))

print("\n-- fetch_one route planning --")
calls = []
def fake(name, exc=None, timing="exact"):
    def run(*a, **k):
        calls.append(name)
        if exc: raise exc
        return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, timing
    return run

eg = F.Egress("http://a:1")
BLOCK = F.BlockedError("429")
MISS = LookupError("no captions")

def patch(yta=None, ytdlp=None, supa=None, kome=None):
    F._route_yta   = (lambda e,v: yta())   if yta else fake("yt")
    F._route_ytdlp = (lambda e,v: ytdlp()) if ytdlp else fake("ytdlp")
    F._route_supadata = (lambda k,v: supa()) if supa else fake("supa")
    F._route_kome  = (lambda v: kome())    if kome else fake("kome", timing="estimated")

# 1. happy path stops at route 1
calls.clear(); patch()
r = F.fetch_one(eg, "v", "auto", "KEY")
check("auto stops at yt", calls == ["yt"] and r[4] == "yt", calls)

# 2. block on route 1 skips route 2 (same IP) and goes to supadata
calls.clear(); patch(yta=fake("yt", BLOCK))
r = F.fetch_one(eg, "v", "auto", "KEY")
check("block skips same-IP route, uses supadata", calls == ["yt","supa"] and r[4]=="supa", calls)

# 3. no key -> block falls to kome (estimated)
calls.clear(); patch(yta=fake("yt", BLOCK))
r = F.fetch_one(eg, "v", "auto", None)
check("block -> kome when no key", calls == ["yt","kome"] and r[3]=="estimated", calls)

# 4. --source exact with no key: block propagates so caller benches the IP
calls.clear(); patch(yta=fake("yt", BLOCK))
try:
    F.fetch_one(eg, "v", "exact", None); check("exact re-raises block", False)
except Exception as e:
    check("exact re-raises block", F.is_block(e) and calls == ["yt"], calls)

# 5. genuine miss on route 1 tries route 2 (not a block)
calls.clear(); patch(yta=fake("yt", MISS))
r = F.fetch_one(eg, "v", "exact", None)
check("miss falls through to ytdlp", calls == ["yt","ytdlp"] and r[4]=="ytdlp", calls)

# 6. no egress left: supadata still runs
calls.clear(); patch()
r = F.fetch_one(None, "v", "exact", "KEY")
check("benched pool still fetches via supadata", calls == ["supa"], calls)

# 7. no egress, no key, exact -> BlockedError not a miss
calls.clear(); patch()
try:
    F.fetch_one(None, "v", "exact", None); check("no route -> BlockedError", False)
except Exception as e:
    check("no route -> BlockedError", F.is_block(e) and calls == [], calls)

# 8. strikes: 3 route-1 failures drop it for auto
eg2 = F.Egress(None); calls.clear(); patch(yta=fake("yt", MISS))
for _ in range(3):
    try: F.fetch_one(eg2, "v", "auto", None)
    except Exception: pass
check("strikes accumulate", eg2.strikes >= 3, eg2.strikes)
calls.clear()
F.fetch_one(eg2, "v", "auto", None)
check("route 1 dropped after 3 strikes", "yt" not in calls, calls)

# 9. never silently estimates under --source exact
calls.clear(); patch(yta=fake("yt", MISS), ytdlp=fake("ytdlp", MISS), supa=fake("supa", MISS))
try:
    F.fetch_one(eg, "v", "exact", "KEY"); check("exact never returns kome", False)
except Exception:
    check("exact never returns kome", "kome" not in calls, calls)

# 10. our IP blocked, then supadata says "no captions": the verdict wins, and
# the block rides along so the identity is still benched.
calls.clear(); patch(yta=fake("yt", BLOCK), supa=fake("supa", MISS))
try:
    F.fetch_one(eg, "v", "exact", "KEY"); check("verdict after block raises", False)
except Exception as e:
    check("an off-IP verdict beats an earlier block",
          isinstance(e, LookupError) and F.about_the_video(e), type(e).__name__)
    check("and carries the block along for benching",
          F.is_block(getattr(e, "egress_blocked", None)), getattr(e, "egress_blocked", None))
# ...but a same-IP verdict after a block is still the block: the yt-dlp
# "no captions" came through an identity that was refused a moment earlier.
calls.clear(); patch(yta=fake("yt", BLOCK), ytdlp=fake("ytdlp", MISS))
try:
    F.fetch_one(eg, "v", "exact", None); check("same-IP verdict after block raises", False)
except Exception as e:
    check("a block is not overridden by a same-IP route", F.is_block(e), type(e).__name__)

# 11. the account being refused is not a block: under auto the talk falls
# through to kome (estimated); under exact it propagates and ends the round.
NOCREDIT = F.AccountError("402 payment required")
calls.clear(); patch(yta=fake("yt", MISS), ytdlp=fake("ytdlp", MISS), supa=fake("supa", NOCREDIT))
r = F.fetch_one(eg, "v", "auto", "KEY")
check("auto: AccountError falls through to kome",
      calls == ["yt","ytdlp","supa","kome"] and r[4] == "kome" and r[3] == "estimated", calls)
calls.clear(); patch(yta=fake("yt", MISS), ytdlp=fake("ytdlp", MISS), supa=fake("supa", NOCREDIT))
try:
    F.fetch_one(eg, "v", "exact", "KEY"); check("exact: AccountError propagates", False)
except Exception as e:
    check("exact: AccountError propagates",
          isinstance(e, F.AccountError) and not F.is_block(e) and not F.about_the_video(e)
          and "kome" not in calls, (type(e).__name__, calls))

print("\n-- supadata: response shapes and error classes --")
class Resp:
    def __init__(self, status, body): self.status, self._b = status, json.dumps(body).encode()
    def read(self): return self._b
    def __enter__(self): return self
    def __exit__(self, *a): return False

def serve(script):
    """script: list of (expected-url-substring, Resp | HTTPError)"""
    seen = []
    def fake(req, timeout=None):
        url = req.full_url; seen.append(url)
        want, out = script.pop(0)
        assert want in url, f"expected {want!r} in {url!r}"
        assert req.get_header("X-api-key") == "K", req.headers
        if isinstance(out, Exception): raise out
        return out
    urllib.request.urlopen = fake
    return seen

def http(code, body=b"{}"):
    return urllib.error.HTTPError("u", code, "err", {}, io.BytesIO(body))

print("\n-- supadata: short video: 200 straight away, ms -> seconds --")
F._supadata_off.clear()
seen = serve([("mode=native", Resp(200, {"lang":"en","content":[
    {"text":"Never gonna","offset":18400,"duration":2040,"lang":"en"},
    {"text":"  give you   up ","offset":20440,"duration":100,"lang":"en"},
    {"text":"","offset":21000,"duration":900}]}))])
segs, lang = F.fetch_supadata("VID", "K")
check("ms -> seconds", segs[0] == {"start":18.4,"duration":2.04,"text":"Never gonna"}, segs[0])
check("whitespace squashed", segs[1]["text"] == "give you up", segs[1])
check("min duration floor", segs[1]["duration"] == 0.5, segs[1])
check("empty text dropped", len(segs) == 2 and lang == "en", (len(segs), lang))
check("url encoded watch link", "watch%3Fv%3DVID" in seen[0], seen[0])

print("\n-- supadata: long video: 202 job, poll until completed --")
F._supadata_off.clear()
seen = serve([
    ("mode=native", Resp(202, {"jobId":"job-1"})),
    ("transcript/job-1", Resp(200, {"status":"queued"})),
    ("transcript/job-1", Resp(200, {"status":"active"})),
    ("transcript/job-1", Resp(200, {"status":"completed","lang":"de",
                                    "content":[{"text":"hallo","offset":1000,"duration":500}]})),
])
segs, lang = F.fetch_supadata("VID", "K")
check("polls job to completion", len(seen) == 4 and segs[0]["start"] == 1.0 and lang == "de", (seen, segs))

print("\n-- supadata: failed job is a miss, not a crash --")
F._supadata_off.clear()
serve([("mode=native", Resp(202, {"jobId":"j2"})),
       ("transcript/j2", Resp(200, {"status":"failed","error":"no captions"}))])
try: F.fetch_supadata("V","K"); check("failed job raises", False)
except LookupError as e: check("failed job raises LookupError", "job failed" in str(e), str(e))

print("\n-- supadata: 206: charged, but no captions -> a real miss, never a block --")
F._supadata_off.clear()
serve([("mode=native", Resp(206, {"content":None}))])
try: F.fetch_supadata("V","K"); check("206 raises", False)
except Exception as e:
    check("206 is a miss not a block", isinstance(e, LookupError) and not F.is_block(e), type(e))

print("\n-- supadata: text=true style string content is refused (we need timings) --")
F._supadata_off.clear()
serve([("mode=native", Resp(200, {"content":"plain text","lang":"en"}))])
try: F.fetch_supadata("V","K"); check("string content refused", False)
except LookupError: check("string content refused", True)

print("\n-- supadata: 402 retires the route, and is never a fact about the video --")
F._supadata_off.clear()
serve([("mode=native", http(402))])
try:
    F.fetch_supadata("V","K")
    check("402 raises", False)
except Exception as e:
    check("402 message", "out of credits" in str(e), str(e))
    # The whole point of the class: run_parallel/run_serial ask
    # about_the_video() before writing _misses.json, and "your account is out
    # of credits" is a fact about the account. As a LookupError this wrote the
    # talk in flight to _misses.json as "no captions", permanently.
    check("402 is an AccountError", isinstance(e, F.AccountError), type(e).__name__)
    check("402 is not about the video", not F.about_the_video(e), type(e).__name__)
    check("402 is not an IP block either", not F.is_block(e), type(e).__name__)
check("402 retires route", bool(F._supadata_off) and not F.off_ip_sources("supadata","K"))
check("kome still counts as off-ip", F.off_ip_sources("auto", None))
F._supadata_off.clear()

print("\n-- supadata: 401 is the same class of refusal as 402 --")
serve([("mode=native", http(401))])
try:
    F.fetch_supadata("V","K")
    check("401 raises", False)
except Exception as e:
    check("401 is an AccountError, not a miss",
          isinstance(e, F.AccountError) and not F.about_the_video(e), type(e).__name__)
F._supadata_off.clear()

# A 206 or a 404 still is a verdict on the video, and must stay one.
check("a real miss is still about the video",
      F.about_the_video(LookupError("no timed transcript for this video")))

print("\n-- supadata: 5xx retried, then succeeds --")
serve([("mode=native", http(500)), ("mode=native", http(503)),
       ("mode=native", Resp(200, {"lang":"en","content":[{"text":"x","offset":0,"duration":1000}]}))])
segs, _ = F.fetch_supadata("V","K")
check("retries 5xx", segs == [{"start":0.0,"duration":1.0,"text":"x"}], segs)

print("\n-- supadata: 429 is backed off and retried, not fatal --")
F._supadata_off.clear()
serve([("mode=native", http(429)), ("mode=native", http(429)),
       ("mode=native", Resp(200, {"lang":"en","content":[{"text":"x","offset":0,"duration":1000}]}))])
segs, _ = F.fetch_supadata("V", "K")
check("429 retried then succeeds", segs == [{"start":0.0,"duration":1.0,"text":"x"}], segs)
check("429 does not retire the route", not F._supadata_off)

print("\n-- supadata: a 429 that outlasts the retries is transient — never a miss, never a bench --")
# A BlockedError benches the identity the request went through, and a supadata
# request goes through supadata's IPs: raised as a block, a busy moment on
# their side benched this machine's own IP for 45 minutes.
F._supadata_off.clear()
serve([("mode=native", http(429))] * 4)
try:
    F.fetch_supadata("V", "K")
    check("persistent 429 raises", False)
except Exception as e:
    check("persistent 429 is RateLimited, a TransientError",
          isinstance(e, F.RateLimited) and isinstance(e, F.TransientError), type(e).__name__)
    check("persistent 429 is not an IP block", not F.is_block(e), type(e).__name__)
    check("persistent 429 is not about the video", not F.about_the_video(e), type(e).__name__)
check("persistent 429 leaves the route on", not F._supadata_off)

print("\n-- supadata: Retry-After is honoured, and the 429 is printed --")
slept = []
F.time.sleep = lambda n: slept.append(n)
out = io.StringIO()
with contextlib.redirect_stdout(out):
    serve([("mode=native", urllib.error.HTTPError("u", 429, "err", {"Retry-After": "7"}, io.BytesIO(b""))),
           ("mode=native", Resp(200, {"lang":"en","content":[{"text":"x","offset":0,"duration":1000}]}))])
    F.fetch_supadata("V", "K")
check("Retry-After's seconds are slept", 7 in slept, slept)
check("the 429 is visible in the log", "429" in out.getvalue(), out.getvalue())
check("a Retry-After beyond the cap is capped",
      F.retry_after_seconds(urllib.error.HTTPError("u", 429, "e", {"Retry-After": "3600"}, None))
      == F.MAX_RETRY_AFTER)
check("an HTTP-date Retry-After falls back to the backoff",
      F.retry_after_seconds(urllib.error.HTTPError("u", 429, "e", {"Retry-After": "Wed, 21 Oct"}, None)) == 0)
F.time.sleep = lambda n: None

print("\n-- yt-dlp: the network failing is not the video failing --")
# Every one of these used to be a LookupError — or, for the timeout, a bare
# SubprocessError — and about_the_video() waved all of them into _misses.json.
import subprocess as _sp

class FakeProc:
    def __init__(self, stderr): self.stderr, self.stdout, self.returncode = stderr, "", 1

def ytdlp_with(stderr=None, exc=None):
    saved = _sp.run
    def fake_run(cmd, **kw):
        if exc: raise exc
        return FakeProc(stderr)
    _sp.run = fake_run
    F.ytdlp_binary = lambda: "/bin/true"
    try:
        F.fetch_ytdlp("VID")
        return None
    except Exception as e:
        return e
    finally:
        _sp.run = saved

e = ytdlp_with(exc=_sp.TimeoutExpired("yt-dlp", 300))
check("a yt-dlp timeout is transient", isinstance(e, F.TransientError), type(e).__name__)
e = ytdlp_with("ERROR: Unable to download webpage: <urlopen error [Errno -3] Temporary failure in name resolution>")
check("a DNS failure is transient", isinstance(e, F.TransientError), f"{type(e).__name__}: {e}")
e = ytdlp_with("ERROR: Unable to download webpage: Tunnel connection failed: 407 Proxy Authentication Required")
check("a dead proxy is transient", isinstance(e, F.TransientError), f"{type(e).__name__}: {e}")
e = ytdlp_with("ERROR: [youtube] VID: Sign in to confirm you're not a bot.")
check("a bot wall is still a block", F.is_block(e), f"{type(e).__name__}: {e}")
e = ytdlp_with("ERROR: [youtube] VID: Video unavailable. This video is private")
check("a private video is still a verdict on the video",
      isinstance(e, LookupError) and F.about_the_video(e), f"{type(e).__name__}: {e}")
e = ytdlp_with("")
check("no caption file at all is still a verdict", isinstance(e, LookupError), type(e).__name__)

print("\n-- kome: an outage is not a verdict on the video --")
def kome_with(*outs):
    script = list(outs)
    def fake(req, timeout=None):
        out = script.pop(0)
        if isinstance(out, Exception): raise out
        return out
    urllib.request.urlopen = fake
    try:
        F.fetch_kome("VID"); return None
    except Exception as e:
        return e

e = kome_with(*[urllib.error.URLError("[Errno -3] Temporary failure in name resolution")] * 4)
check("four failed connections are transient", isinstance(e, F.TransientError), f"{type(e).__name__}: {e}")
e = kome_with(*[http(503)] * 4)
check("a run of 5xx is transient", isinstance(e, F.TransientError), f"{type(e).__name__}: {e}")
e = kome_with(http(404))
check("a 404 is a verdict on the video", isinstance(e, LookupError) and F.about_the_video(e),
      f"{type(e).__name__}: {e}")
e = kome_with(http(500), Resp(200, {"transcript": "hello there", "length": "1m 0s"}))
check("one 5xx is retried", e is None, e)
# kome names no caption track, so the language is assumed rather than read:
# the docstring says so, and this pins it so a change there is deliberate.
urllib.request.urlopen = lambda req, timeout=None: Resp(
    200, {"transcript": "hello there\nsecond line", "length": "1m 0s"})
segs_k, lang_k, total_k = F.fetch_kome("VID")
check("kome reports the assumed 'en', never a read track",
      lang_k == "en" and total_k == 60.0 and len(segs_k) >= 1, (lang_k, total_k))

print("\n-- supadata: 404 is a per-video miss, route stays on --")
serve([("mode=native", http(404, b'{"error":"video-not-found"}'))])
try: F.fetch_supadata("V","K")
except LookupError as e: check("404 detail surfaced", "404" in str(e) and "video-not-found" in str(e), str(e))
check("404 does not retire route", not F._supadata_off)

print("\n-- supadata: a run of 5xx is the far end failing, not a video --")
# Raised bare these were an HTTPError / URLError, which is neither a block nor
# an AccountError — so about_the_video() waved them into _misses.json and a
# supadata outage cost a talk each, permanently.
F._supadata_off.clear()
serve([("mode=native", http(500))] * 4)
try:
    F.fetch_supadata("V","K")
    check("persistent 5xx raises", False)
except Exception as e:
    check("persistent 5xx is transient, not a miss",
          isinstance(e, F.TransientError) and not F.about_the_video(e), type(e).__name__)
    check("persistent 5xx is not an IP block", not F.is_block(e), type(e).__name__)
    check("persistent 5xx says what failed", "HTTPError" in str(e), str(e))
check("persistent 5xx leaves the route on", not F._supadata_off)

serve([("mode=native", urllib.error.URLError("connection reset"))] * 4)
try:
    F.fetch_supadata("V","K")
    check("persistent timeout raises", False)
except Exception as e:
    check("a dropped connection is transient, not a miss",
          isinstance(e, F.TransientError) and not F.about_the_video(e), type(e).__name__)

print("\n-- supadata: a job that never finishes is retryable, not a miss --")
# The credit is already spent and the captions may well exist; writing the talk
# off as having none would lose it and the credit.
F._supadata_off.clear()
serve([("mode=native", Resp(202, {"jobId":"j3"}))]
      + [("transcript/j3", Resp(200, {"status":"active"}))] * 3)
clock = [1000.0]
_REAL_TIME = F.time.time
F.time.time = lambda: clock[0]
F.time.sleep = lambda s: clock.__setitem__(0, clock[0] + 600)   # 10 min a poll
try:
    F.fetch_supadata("V","K")
    check("stalled job raises", False)
except Exception as e:
    check("a stalled job is transient, not a miss",
          isinstance(e, F.TransientError) and not F.about_the_video(e), type(e).__name__)
F.time.time, F.time.sleep = _REAL_TIME, lambda s: None

# A job that comes back *failed* is still the video's problem, and stays one.
F._supadata_off.clear()
serve([("mode=native", Resp(202, {"jobId":"j4"})),
       ("transcript/j4", Resp(200, {"status":"failed","error":"no captions"}))])
try:
    F.fetch_supadata("V","K")
    check("failed job still raises", False)
except Exception as e:
    check("a failed job is still about the video", F.about_the_video(e), type(e).__name__)

print("\n-- language tags: LANGUAGES is a preference, not a gate --")
# Every route spells a language differently, so anything comparing them has to
# compare base tags: BCP-47 from youtube-transcript-api, a file suffix from
# yt-dlp, bare ISO 639-1 from supadata.
check("regional variant folds to its base", F.base_lang("en-US") == "en", F.base_lang("en-US"))
check("yt-dlp's -orig suffix folds too", F.base_lang("en-orig") == "en", F.base_lang("en-orig"))
check("case and padding fold", F.base_lang("  PT_BR ") == "pt", F.base_lang("  PT_BR "))
check("nothing in, nothing out", F.base_lang(None) == "" and F.base_lang("") == "")
check("a variant of a wanted language is wanted", F.lang_ok("en-GB") and F.lang_ok("de"))
check("a language off the list is not", not F.lang_ok("hi") and not F.lang_ok(None))
# supadata answers "none" for a track it served but could not identify; ten
# transcripts in this corpus are filed under it. It is not a language code.
check("an unnameable language becomes 'und'",
      F.named_lang("none") == F.named_lang("") == F.named_lang(None) == "und",
      (F.named_lang("none"), F.named_lang("")))
check("a real code is recorded verbatim",
      F.named_lang("en-GB") == "en-GB" and F.named_lang(" hi ") == "hi")
check("preference order survives the fold",
      F.LANG_RANK["en"] < F.LANG_RANK["de"] < F.LANG_RANK["fr"] < F.LANG_RANK["uk"],
      F.LANG_RANK)

print("\n-- supadata asks for a language, then checks the answer --")
# Sending no `lang` at all is how ten English talks acquired Devanagari
# transcripts that indexed as though they were the talk. Asking is half of it:
# supadata answers an unavailable language with "the first available language
# and a list of other available languages" rather than an error, so the answer
# has to be read.
F._supadata_off.clear()
seen = serve([("mode=native", Resp(200, {"lang": "en", "content": [
    {"text": "hello", "offset": 0, "duration": 1000}]}))])
segs, lang = F.fetch_supadata("VID", "K")
check("the request states a language", "lang=en&" in seen[0] or "&lang=en" in seen[0], seen[0])
check("an English answer costs one credit", len(seen) == 1 and lang == "en", (seen, lang))

# Off-list answer, English on offer: the documented remedy is to re-request
# against availableLangs, and that is worth the second credit.
F._supadata_off.clear()
seen = serve([
    ("lang=en", Resp(200, {"lang": "hi", "availableLangs": ["hi", "en"],
                           "content": [{"text": "थैंक यू", "offset": 0, "duration": 1000}]})),
    ("lang=en", Resp(200, {"lang": "en", "availableLangs": ["hi", "en"],
                           "content": [{"text": "thank you", "offset": 0, "duration": 1000}]})),
])
segs, lang = F.fetch_supadata("VID", "K")
check("a fallback answer is re-requested against availableLangs", len(seen) == 2, seen)
check("and the English text is what is kept",
      lang == "en" and segs[0]["text"] == "thank you", (lang, segs))

# The retry picks by LANGUAGES order, not by the order the video lists.
F._supadata_off.clear()
seen = serve([
    ("lang=en", Resp(200, {"lang": "hi", "availableLangs": ["fr", "de", "hi"],
                           "content": [{"text": "x", "offset": 0, "duration": 1000}]})),
    ("lang=de", Resp(200, {"lang": "de",
                           "content": [{"text": "hallo", "offset": 0, "duration": 1000}]})),
])
segs, lang = F.fetch_supadata("VID", "K")
check("the retry follows LANGUAGES order", lang == "de" and len(seen) == 2, (lang, seen))

# Nothing on the list is on offer. This is the whole point: it is not an error,
# not a block and above all not a miss — the video has captions.
F._supadata_off.clear()
seen = serve([("lang=en", Resp(200, {"lang": "hi", "availableLangs": ["hi", "ta"],
                                     "content": [{"text": "थैंक यू", "offset": 0,
                                                  "duration": 1000}]}))])
segs, lang = F.fetch_supadata("VID", "K")
check("a foreign-only track is returned, not raised", lang == "hi" and len(segs) == 1, (lang, segs))
check("and costs no second credit", len(seen) == 1, seen)
check("a foreign-only track is not an error at all",
      not F.is_block(LookupError()) and lang == "hi")

# availableLangs missing entirely (older responses) must not crash the check.
F._supadata_off.clear()
seen = serve([("lang=en", Resp(200, {"lang": "hi",
                                     "content": [{"text": "x", "offset": 0,
                                                  "duration": 1000}]}))])
segs, lang = F.fetch_supadata("VID", "K")
check("no availableLangs is survivable", lang == "hi" and len(seen) == 1, (lang, seen))
F._supadata_off.clear()

urllib.request.urlopen = _REAL_URLOPEN

print("\n-- pick_and_fetch reports the language it actually fetched --")


class FakeTranscript:
    def __init__(self, code, translatable=True, into=("en",)):
        self.language_code, self.is_translatable = code, translatable
        self.is_generated, self._into = True, into

    def translate(self, code):
        if not self.is_translatable or code not in self._into:
            raise RuntimeError("TranslationLanguageNotAvailable")
        return FakeTranscript(code, translatable=False)

    def fetch(self):
        return [{"start": 0.0, "duration": 1.0, "text": "hi"}]


class FakeListing(list):
    def __init__(self, tracks, manual=None, generated=None):
        super().__init__(tracks)
        self._manual, self._generated = manual, generated

    def find_manually_created_transcript(self, langs):
        if self._manual is None:
            raise RuntimeError("no manual track")
        return self._manual

    def find_generated_transcript(self, langs):
        if self._generated is None:
            raise RuntimeError("no generated track")
        return self._generated


def picked(listing):
    api = types.SimpleNamespace(list=lambda vid: listing)
    return F.pick_and_fetch(api, "V")


_raw, lang, _g = picked(FakeListing([], manual=FakeTranscript("en-GB", translatable=False)))
check("a preferred track reports its own code", lang == "en-GB", lang)

_raw, lang, _g = picked(FakeListing([FakeTranscript("hi")]))
check("a translated track reports the language translated into", lang == "en", lang)

_raw, lang, _g = picked(FakeListing([FakeTranscript("hi", translatable=False)]))
check("an untranslatable track reports its own language, honestly", lang == "hi", lang)

# The bug in the other direction: TranslationLanguageNotAvailable is neither a
# block, an account refusal nor a transient, so left to propagate it reaches
# _misses.json as "this video has no captions" — for a video that has them.
_raw, lang, _g = picked(FakeListing([FakeTranscript("hi", into=("fr",))]))
check("a failed translation falls back rather than losing the talk", lang == "hi", lang)

_raw, lang, _g = picked(FakeListing([FakeTranscript("hi", translatable=False),
                                     FakeTranscript("ta")]))
check("a translatable track beats an untranslatable one", lang == "en", lang)

try:
    picked(FakeListing([]))
    check("no tracks at all is still a miss", False)
except LookupError as e:
    check("no tracks at all is still a miss", "no transcript tracks" in str(e), str(e))

print("\n-- save() files a transcript under the language it is in --")
written = {}
_REAL_WRITE = F.atu.write_json
F.atu.write_json = lambda path, obj, compact=False: written.update(obj)
TALK = {"id": "vid1", "title": "T", "conference": "c"}
SEG = [{"start": 0.0, "duration": 1.0, "text": "one two three"}]

out = io.StringIO()
with contextlib.redirect_stdout(out):
    words = F.save(TALK, SEG, "en-GB", True, "exact", "yt")
check("the language it was given is the language it records",
      written["language"] == "en-GB", written.get("language"))
check("word count is the segments' words", words == 3, words)
check("an on-list language is saved without comment", out.getvalue() == "", out.getvalue())

out = io.StringIO()
with contextlib.redirect_stdout(out):
    F.save(TALK, SEG, "hi", True, "exact", "supa")
check("a foreign-only track is written, not discarded", written["language"] == "hi",
      written.get("language"))
check("a foreign-only track is never silent",
      "vid1" in out.getvalue() and "hi" in out.getvalue(), out.getvalue())

with contextlib.redirect_stdout(io.StringIO()):
    F.save(TALK, SEG, "", True, "exact", "supa")
check("an unknown language is 'und', never guessed as 'en'",
      written["language"] == "und", written.get("language"))

with contextlib.redirect_stdout(io.StringIO()):
    F.save(TALK, SEG, "none", True, "exact", "supa")
check("supadata's 'none' is recorded as 'und' too",
      written["language"] == "und", written.get("language"))
F.atu.write_json = _REAL_WRITE

print("\n-- a full round against fake allowances --")
ARGS = types.SimpleNamespace(source="exact", min_delay=0, max_delay=0,
                             proxy_cooldown=45, workers=4, limit=None)
F.save = lambda t, segs, lang, gen, timing, source: 100     # no disk writes

ALLOWANCE = {"http://a:1":5, "http://b:2":5, "http://c:3":5}
used = {}
NOCAP = {"talk-7", "talk-13"}      # two videos genuinely have no captions

def fake_fetch_one(eg, vid, source, key):
    if eg is None: raise F.BlockedError("no egress")
    n = used.get(eg.url, 0)
    if n >= ALLOWANCE[eg.url]: raise F.BlockedError("429 from " + eg.label)
    used[eg.url] = n + 1
    if vid in NOCAP: raise LookupError("no transcript tracks")
    return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, "exact", "yt"

F.fetch_one = fake_fetch_one
todo = [{"id": f"talk-{i}", "title": f"Talk {i}", "conference": "x"} for i in range(30)]

pool = F.Pool(list(ALLOWANCE), cooldown_min=45)
misses = {}
t0 = time.time()
ok, fail, blocked = F.run_parallel(pool, todo, misses, ARGS, None)
print(f"   -> ok={ok} fail={fail} blocked={blocked} in {time.time()-t0:.1f}s")

check("pool multiplies the yield", ok == 15 - len(NOCAP), ok)
check("every identity spent its own allowance", used == ALLOWANCE, used)
check("misses recorded only for real misses", set(misses) == NOCAP, set(misses))
check("blocks never recorded as misses",
      all(m["reason"] != "BlockedError" for m in misses.values()), misses)
check("fail count is misses only", fail == len(NOCAP), fail)
check("round reports blocked once exhausted", blocked is True)
check("all identities benched", pool.all_benched())
check("bench is the cooldown, not forever", 44*60 < pool.recovers_in() <= 45*60)

# one identity blocked, the others carry on
used.clear(); ALLOWANCE.update({"http://a:1":1, "http://b:2":40, "http://c:3":40})
pool2 = F.Pool(list(ALLOWANCE), cooldown_min=45); m2 = {}
ok2, fail2, blocked2 = F.run_parallel(pool2, todo, m2, ARGS, None)
check("one dead IP does not stop the run", ok2 == len(todo) - len(NOCAP), ok2)
check("round not reported blocked", blocked2 is False)
check("dead IP benched, others alive", not pool2.all_benched())

# serial path, same guarantees
used.clear(); ALLOWANCE.update({"http://a:1":2, "http://b:2":2, "http://c:3":2})
pool3 = F.Pool(list(ALLOWANCE), cooldown_min=45); m3 = {}
ARGS.workers = 1
ok3, fail3, blocked3 = F.run_serial(pool3, todo, m3, ARGS, None)
check("serial spends every identity", ok3 == 6 and blocked3 is True, (ok3, blocked3))
check("serial records no block as a miss", not any(r["reason"]=="BlockedError" for r in m3.values()), m3)

# with an off-IP route configured, an exhausted pool is not the end of the round
used.clear(); ALLOWANCE.update({"http://a:1":1, "http://b:2":1, "http://c:3":1})
def fetch_with_supa(eg, vid, source, key):
    if eg is None:
        return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, "exact", "supa"
    return fake_fetch_one(eg, vid, source, key)
F.fetch_one = fetch_with_supa
pool4 = F.Pool(list(ALLOWANCE), cooldown_min=45); m4 = {}
ARGS.workers = 4
ok4, fail4, blocked4 = F.run_parallel(pool4, todo, m4, ARGS, "KEY")
check("supadata carries the round past a spent pool", ok4 == len(todo), ok4)
check("not treated as a blocked round", blocked4 is False)
check("spent() knows supadata is a way out", not F.spent(pool4, ARGS, "KEY") and F.spent(pool4, ARGS, None))

print("\n-- a verdict that rode along with a block still benches the identity --")
def fetch_verdict_after_block(eg, vid, source, key):
    if eg is None:
        raise F.BlockedError("no egress")
    e = LookupError("supadata: no timed transcript for this video")
    e.egress_blocked = F.BlockedError("429 from " + eg.label)
    raise e
F.fetch_one = fetch_verdict_after_block
pool4b = F.Pool(["http://a:1"], cooldown_min=45); m4b = {}
ARGS.workers = 1
ok4b, fail4b, blocked4b = F.run_serial(pool4b, [todo[0]], m4b, ARGS, "KEY")
check("the talk is recorded as the miss supadata said it was", set(m4b) == {todo[0]["id"]}, m4b)
check("and the identity the block came through is benched", pool4b.all_benched())

print("\n-- an off-IP source leases nothing, so --workers is real --")
# The pool exists to stop two workers spending one IP's allowance at once. A
# supadata-only run spends somebody else's, so leasing would pin every worker
# to the single direct identity — which is how a 1,391-talk run came to be
# strictly serial. This is the check that it no longer is.
SUPA_ARGS = types.SimpleNamespace(source="supadata", min_delay=9, max_delay=9,
                                  proxy_cooldown=45, workers=4, limit=None)
leased, inflight, peak = [], [0], [0]
lock = threading.Lock()

def fetch_off_ip(eg, vid, source, key):
    leased.append(eg)
    with lock:
        inflight[0] += 1
        peak[0] = max(peak[0], inflight[0])
    _REAL_SLEEP(0.05)          # real, so overlap is observable
    with lock:
        inflight[0] -= 1
    return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, "exact", "supa"

F.fetch_one = fetch_off_ip
pool5 = F.Pool([None], cooldown_min=45); m5 = {}
ok5, fail5, blocked5 = F.run_parallel(pool5, todo, m5, SUPA_ARGS, "KEY")
check("every talk fetched off-IP", ok5 == len(todo) and not m5, (ok5, m5))
check("no identity was ever leased", all(e is None for e in leased), leased[:3])
check("workers ran concurrently", peak[0] > 1, peak[0])
check("min-delay does not pace an off-IP route", not F.uses_our_ip("supadata"))
# An idle pool must not read as "still has options": with no key there is
# nothing left, and the round has to end rather than spin.
check("spent() ignores an idle pool off-IP",
      F.spent(pool5, SUPA_ARGS, None) and not F.spent(pool5, SUPA_ARGS, "KEY"))

print("\n-- the credits running out mid-flight loses no talk --")
# The failure this pins down: 402 raised LookupError, which run_parallel wrote
# to _misses.json — the file that means "this video has no captions" and that
# select() skips forever. _supadata_off only closes the route for talks not yet
# dispatched, so every request already in flight was poisoned, up to --workers
# of them. Credits ~ talks, so a run ending mid-batch is the expected case.
F._supadata_off.clear()
CREDITS = [4]

def fetch_until_broke(eg, vid, source, key):
    with lock:
        left = CREDITS[0]
        CREDITS[0] -= 1
    if left <= 0:
        F._supadata_off.append("out of credits")     # as the real route does
        raise F.AccountError("supadata: out of credits")
    return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, "exact", "supa"

F.fetch_one = fetch_until_broke
pool6 = F.Pool([None], cooldown_min=45); m6 = {}
ok6, fail6, blocked6 = F.run_parallel(pool6, todo, m6, SUPA_ARGS, "KEY")
check("out of credits is never recorded as a miss", m6 == {}, m6)
check("no talk counted as failed", fail6 == 0, fail6)
check("only the paid-for talks came back", ok6 == 4, ok6)
check("the round stops instead of walking the backlog", blocked6 is True, blocked6)
check("every unfetched talk stays retryable", len(todo) - ok6 == 26 and not m6, (ok6, m6))

# The serial path has to make the same promise.
F._supadata_off.clear(); CREDITS[0] = 2
SERIAL_ARGS = types.SimpleNamespace(**{**vars(SUPA_ARGS), "workers": 1})
pool7 = F.Pool([None], cooldown_min=45); m7 = {}
ok7, fail7, blocked7 = F.run_serial(pool7, todo, m7, SERIAL_ARGS, "KEY")
check("serial records no account refusal as a miss", m7 == {} and fail7 == 0, (m7, fail7))
check("serial stops when the account refuses", ok7 == 2 and blocked7 is True, (ok7, blocked7))
F._supadata_off.clear()

# A transient failure ends nothing: the route is still there and may work on
# the very next talk, so the run carries on and the talk waits for a rerun.
FLAKY = {"talk-3", "talk-9"}

def fetch_flaky(eg, vid, source, key):
    if vid in FLAKY:
        raise F.TransientError("supadata: HTTPError after 4 attempts (500)")
    return [{"start":0.0,"duration":1.0,"text":"hi"}], "en", True, "exact", "supa"

F.fetch_one = fetch_flaky
pool8 = F.Pool([None], cooldown_min=45); m8 = {}
ok8, fail8, blocked8 = F.run_parallel(pool8, todo, m8, SUPA_ARGS, "KEY")
check("a transient failure is never a miss", m8 == {} and fail8 == 0, (m8, fail8))
check("the round carries on past it",
      ok8 == len(todo) - len(FLAKY) and blocked8 is False, (ok8, blocked8))

print("\n-- a video whose only captions are foreign is fetched, never missed --")
# _misses.json means "this video has no captions" and select() skips every id
# in it forever. A Hindi-only track is captions, so writing it there would lose
# the talk on a false verdict — and a "retry later" would spend a credit on it
# every run without ever converging, because the track will still be Hindi next
# month. So it is kept, and kept under its real language.
saved = []
F.save = lambda t, segs, lang, gen, timing, source: (saved.append((t["id"], lang)), 100)[1]
F.fetch_one = lambda eg, vid, source, key: (
    [{"start": 0.0, "duration": 1.0, "text": "थैंक यू फॉर कमिंग"}], "hi", True, "exact", "supa")
pool9 = F.Pool([None], cooldown_min=45); m9 = {}
ok9, fail9, blocked9 = F.run_parallel(pool9, todo, m9, SUPA_ARGS, "KEY")
check("a foreign-only track is never recorded as a miss", m9 == {} and fail9 == 0, (m9, fail9))
check("every one of them is fetched", ok9 == len(todo) and blocked9 is False, (ok9, blocked9))
check("and each is filed under the language it is in",
      {lg for _, lg in saved} == {"hi"} and len(saved) == len(todo), saved[:3])


print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else
              f"all checks passed"))
sys.exit(1 if FAILS else 0)
