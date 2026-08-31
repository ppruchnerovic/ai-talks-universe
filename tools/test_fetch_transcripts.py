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
CORPUS = [{"id": f"v{y}", "title": str(y), "conference": "x", "priority": 1,
           "duration_min": 30, "duration_s": 1800, "year": y}
          for y in (2024, 2025, 2026)]
CORPUS.append({"id": "vnone", "title": "undated", "conference": "x", "priority": 1,
               "duration_min": 30, "duration_s": 1800, "year": None})
ALL = ["v2024", "v2025", "v2026", "vnone"]


def sel(**kw):
    a = types.SimpleNamespace(only=[], priority=None, min_duration=0,
                              year=None, min_year=None, include_unknown_year=False)
    a.__dict__.update(kw)
    return [t["id"] for t in F.select(CORPUS, a, {})]


check("no year flags selects everything", sel() == ALL, sel())
check("--year takes that year only", sel(year=[2026]) == ["v2026"], sel(year=[2026]))
check("--year repeated is a set", sel(year=[2024, 2026]) == ["v2024", "v2026"],
      sel(year=[2024, 2026]))
check("--min-year takes that year onwards", sel(min_year=2025) == ["v2025", "v2026"],
      sel(min_year=2025))
check("unknown year is excluded by default", sel(min_year=2026) == ["v2026"],
      sel(min_year=2026))
check("--include-unknown-year keeps it",
      sel(min_year=2026, include_unknown_year=True) == ["v2026", "vnone"],
      sel(min_year=2026, include_unknown_year=True))
check("--include-unknown-year alone widens nothing",
      sel(include_unknown_year=True) == ALL, sel(include_unknown_year=True))
check("year filter does not disturb the priority/duration sort",
      sel(min_year=2024) == ALL[:3], sel(min_year=2024))

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

print("\n-- supadata: 402 retires the route for the rest of the run --")
F._supadata_off.clear()
serve([("mode=native", http(402))])
try: F.fetch_supadata("V","K")
except LookupError as e: check("402 message", "out of credits" in str(e), str(e))
check("402 retires route", bool(F._supadata_off) and not F.off_ip_sources("supadata","K"))
check("kome still counts as off-ip", F.off_ip_sources("auto", None))
F._supadata_off.clear()

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

print("\n-- supadata: a 429 that outlasts the retries is a block, never a miss --")
F._supadata_off.clear()
serve([("mode=native", http(429))] * 4)
try:
    F.fetch_supadata("V", "K")
    check("persistent 429 raises", False)
except Exception as e:
    check("persistent 429 is a block", F.is_block(e), f"{type(e).__name__}: {e}")
check("persistent 429 leaves the route on", not F._supadata_off)

print("\n-- supadata: 404 is a per-video miss, route stays on --")
serve([("mode=native", http(404, b'{"error":"video-not-found"}'))])
try: F.fetch_supadata("V","K")
except LookupError as e: check("404 detail surfaced", "404" in str(e) and "video-not-found" in str(e), str(e))
check("404 does not retire route", not F._supadata_off)

urllib.request.urlopen = _REAL_URLOPEN
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


print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else
              f"all checks passed"))
sys.exit(1 if FAILS else 0)
