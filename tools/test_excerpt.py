#!/usr/bin/env python3
"""Offline checks for excerpt.py — no database, no network.

What is worth testing here is the budget, because the failure it prevents is
silent and expensive: a query whose terms are spread through a long talk used
to chain every window into one span, and the "excerpt" came back as the whole
transcript — 8,500 tokens where 1,500 was asked for, with nothing in the
output saying so. The selection and the merge are pure functions of the hit
times, so they are testable without a corpus, and that is what is tested.

    cd tools && python3 test_excerpt.py
"""

import sys

sys.path.insert(0, ".")
import excerpt as E

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


def secs(spans):
    return sum(hi - lo for lo, hi in spans)


print("\n-- merging --")
check("disjoint windows stay separate", E.merge([(0, 10), (50, 60)]) == [(0, 10), (50, 60)])
check("overlapping windows become one", E.merge([(0, 60), (40, 100)]) == [(0, 100)])
check("touching windows become one", E.merge([(0, 60), (60, 100)]) == [(0, 100)])
check("out of order input comes back in time order",
      E.merge([(90, 100), (0, 10)]) == [(0, 10), (90, 100)])
check("a window inside another is absorbed", E.merge([(0, 100), (20, 30)]) == [(0, 100)])

print("\n-- the budget --")
# A hit every 30 seconds through a 40-minute talk: the shape that used to
# return the transcript.
dense = [float(t) for t in range(0, 2400, 30)]
sp = E.spans_for(dense, window=40, limit=6)
check("a talk that matches throughout stays within budget", secs(sp) <= 6 * 2 * 40 + 80,
      f"{secs(sp)}s of a possible 2400")
check("and does not come back as the whole talk", secs(sp) < 2400 * 0.5, secs(sp))

spread = [100.0, 900.0, 1800.0, 2500.0]
sp = E.spans_for(spread, window=40, limit=6)
check("well-separated hits each get their own passage", len(sp) == 4, sp)
check("each is the hit plus its window either side", secs(sp) == 4 * 80, secs(sp))

check("a hit at the very start is not given negative time",
      E.spans_for([5.0], window=40, limit=6)[0][0] == 0.0)

# Rank order is what the budget is spent in, so an unranked hit past the
# budget must not displace a better one that came first.
sp = E.spans_for([100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 5000.0],
                 window=40, limit=2)
check("the budget is spent on the best-ranked hits first",
      sp[0][0] == 60.0 and all(hi <= 400 for _, hi in sp), sp)

check("more windows than hits costs only the hits",
      secs(E.spans_for([100.0], window=40, limit=6)) == 80)

print("\n-- what --window and -n buy --")
check("a wider window buys more speech per hit",
      secs(E.spans_for([500.0], window=90, limit=6)) == 180)
# On a talk that matches throughout, the windows are contiguous, so what -n
# buys is a longer passage rather than more of them — and it must buy it.
check("a bigger -n buys more speech",
      secs(E.spans_for(dense, window=40, limit=2)) < secs(E.spans_for(dense, window=40, limit=8)))
check("well-separated hits, though, come back as separate passages",
      len(E.spans_for(spread, window=40, limit=6)) == 4)

print("\n-- --words: the trim --")
# Three passages: an opening, a hit in the middle, a hit near the end. The
# tiles come off the ends farthest from any anchor, never out of the middle.
tiles = [[(0.0, "a b c"), (10.0, "d e f"), (20.0, "g h i")],
         [(500.0, "j k l"), (510.0, "m n o"), (520.0, "p q r")],
         [(900.0, "s t u"), (910.0, "v w x")]]
cut = E.trim_to_words(tiles, [0.0, 510.0, 910.0], 12)
check("the trim meets the budget to within one tile",
      sum(E.words_in(p) for p in cut) <= 12 + 3, sum(E.words_in(p) for p in cut))
check("the hit tiles survive",
      any(t[0] == 510.0 for p in cut for t in p) and any(t[0] == 910.0 for p in cut for t in p), cut)
check("each passage stays contiguous — tiles come off the ends only",
      all([t[0] for t in p] == sorted(t[0] for t in p) and
          all(b - a == 10.0 for a, b in zip([t[0] for t in p], [t[0] for t in p][1:]))
          for p in cut), cut)
check("a budget of nothing leaves nothing", E.trim_to_words(tiles, [0.0], 0) == [])
check("a generous budget changes nothing", E.trim_to_words(tiles, [0.0], 1000) == tiles)

print("\n-- --quotes: the sentence splitter --")
S = E.sentences
tw = [("Hello.", 0.0), ("This", 1.0), ("is", 2.0), ("it?", 3.0), ("Yes!\"", 4.0), ("and", 5.0), ("so", 6.0)]
sents = S(tw)
check("splits at . ? and ! including a closing quote",
      [" ".join(w for w, _ in s) for s in sents] == ["Hello.", "This is it?", "Yes!\"", "and so"], sents)
check("a sentence keeps the time of its first word", sents[1][0][1] == 1.0)
check("the trailing fragment without a full stop is the last sentence", sents[-1][0][0] == "and")
check("no words, no sentences", S([]) == [])
check("a decimal is not a full stop",
      len(S([("version", 0.0), ("2.5", 1.0), ("shipped.", 2.0)])) == 1)

tiles3 = [(0.0, 0, "one two three. four five"), (10.0, 5, "six seven eight. nine ten"),
          (20.0, 10, "eleven twelve")]
tw = E.timed_words(tiles3)
check("timed words run in one global position sequence", [p for _, p, _ in tw] == list(range(12)))
check("a word's time is interpolated inside its tile",
      [t for _, _, t in tw][:5] == [0.0, 2.0, 4.0, 6.0, 8.0], [t for _, _, t in tw][:5])
check("the last tile is taken as ten seconds long", tw[-1][2] == 25.0, tw[-1])

hit = {"start": 10.0, "pos": 5, "bridge": 0, "text": "six seven eight. nine ten"}
q = E.quote_for(tiles3, hit, set(E.atu.stems("eight")))
check("the quote is the sentence holding the query word, even across a tile boundary",
      q["text"] == "four five six seven eight." and q["sentence"], q)
check("and it is timed from where that sentence starts, not where the tile does",
      q["start"] == 6.0, q["start"])
q = E.quote_for(tiles3, hit, set(E.atu.stems("nine")))
check("a later sentence in the hit wins when it is the one with the word",
      q["text"].startswith("nine ten"), q)
q = E.quote_for(tiles3, hit, set())
check("with no query (an --at anchor) the sentence under the middle of the hit is the quote",
      q["sentence"] and "eight." in q["text"], q)
q = E.quote_for(tiles3, hit, set(E.atu.stems("zebra")))
check("no sentence holds the word: the hit tile itself, marked as not a sentence",
      q["text"] == "six seven eight. nine ten" and not q["sentence"] and q["start"] == 10.0, q)
long = [(0.0, 0, " ".join(["word"] * 40)), (10.0, 40, " ".join(["word"] * 20) + " target " + " ".join(["word"] * 4))]
q = E.quote_for(long, {"start": 10.0, "pos": 40, "bridge": 0, "text": long[1][2]}, set(E.atu.stems("target")))
check("speech with no punctuation falls back to the tile rather than quoting 60+ words",
      not q["sentence"] and q["words"] == 25, q)

print("\n-- query stems --")
P = E.query.parse_query
check("a bare query's stems include its synonyms, so a passage that said 'evaluation' counts",
      {"eval", "evalu"} <= E.query_stems(P("evals agents")), E.query_stems(P("evals agents")))
check("explicit syntax is scanned for its words, minus operators and NEAR's distance",
      E.query_stems(P("NEAR(eval production, 10)")) >= {"eval", "product"}
      and not E.query_stems(P("NEAR(eval production, 10)")) & {"near", "10"},
      E.query_stems(P("NEAR(eval production, 10)")))
check("no query, no stems", E.query_stems(None) == set())

print("\n-- --outline: bucketing --")
segs = [(0.0, "agents memory memory"), (30.0, "and memory"), (130.0, "agents kubernetes kubernetes"),
        (400.0, "agents")]
out = E.bucketize(segs, set(E.atu.stems("memory")), bucket=120, terms=3)
check("one bucket per two minutes up to the last tile, empty ones included",
      [b["start"] for b in out] == [0.0, 120.0, 240.0, 360.0], [b["start"] for b in out])
check("a bucket ends where the next begins", all(b["end"] - b["start"] == 120.0 for b in out))
check("hits count the query's stems in the bucket, over all its tiles",
      [b["hits"] for b in out] == [3, 0, 0, 0], [b["hits"] for b in out])
check("words are the bucket's word count, stopwords and all",
      [b["words"] for b in out] == [5, 3, 0, 1], [b["words"] for b in out])
check("an empty bucket has no terms", out[2]["terms"] == [])
check("a word the whole talk says ranks below the bucket's own word",
      out[0]["terms"][0] == "memory" and out[1]["terms"][0] == "kubernetes", [b["terms"] for b in out])
check("at most `terms` terms a bucket", all(len(b["terms"]) <= 3 for b in out))
check("terms are surface forms, not stems", "kubernetes" in out[1]["terms"], out[1]["terms"])
check("a bucket that says the word but not the query still counts zero", out[1]["hits"] == 0)
check("no query: no hits, same buckets",
      [b["hits"] for b in E.bucketize(segs, set(), 120, 3)] == [0, 0, 0, 0])
check("no tiles, no outline", E.bucketize([], set()) == [])
filler = [(0.0, "um uh you know I mean kind of thing stuff")]
check("filler words never make the outline", E.bucketize(filler, set(), 120, 5)[0]["terms"] == [],
      E.bucketize(filler, set(), 120, 5)[0]["terms"])
check("the default bucket is two minutes and an hour is thirty lines",
      len(E.bucketize([(float(s), "word") for s in range(0, 3600, 60)], set())) == 30)

print("\n-- --at --")
check("seconds, m:ss, h:mm:ss and comma lists all parse",
      E.parse_at(["600", "10:00", "1:02:03", "12:00,34:10"]) == [600.0, 600.0, 3723.0, 720.0, 2050.0])
check("a fractional second is accepted", E.parse_at(["12:00.5"]) == [720.0])
for bad in (["-5"], ["12:xx"], ["12:00:00:00"]):
    try:
        E.parse_at(bad)
        check(f"{bad[0]!r} is refused", False)
    except E.argparse.ArgumentTypeError:
        check(f"{bad[0]!r} is refused", True)

print("\n-- ids that start with a hyphen --")
rest, ids = E.split_ids(["-stDHMwbBRw", "-q", "-abc", "--at", "-1:00", "-n", "3", "O72p-rBb2bA", "--quotes"])
check("a hyphen-leading id is lifted out before argparse sees it", ids == ["-stDHMwbBRw"], ids)
check("and an option's value that looks like one is left alone",
      rest == ["-q", "-abc", "--at", "-1:00", "-n", "3", "O72p-rBb2bA", "--quotes"], rest)

print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else "all checks passed"))
sys.exit(1 if FAILS else 0)
