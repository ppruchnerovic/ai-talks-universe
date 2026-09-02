#!/usr/bin/env python3
"""The two Porter stemmers agree — atu.stem() and the one in index.html.

The browser index is keyed on the Python stemmer's output and the query is
stemmed in JavaScript, so a disagreement on any word is a silent miss: the
shard holds one spelling of the stem and the query asks for the other. This
lifts the JavaScript function out of index.html between its two markers,
runs it under node over the corpus vocabulary — every distinct token in every
title, description and transcript on disk — and diffs. The Porter paper's own
examples are checked on the Python side first, so a shared mistake cannot pass
as agreement.

    cd tools && python3 test_stem.py            # ~10 s; skips the node half if node is missing
"""

import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, ".")
import atu

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


# From Porter (1980), "An algorithm for suffix stripping" — the worked examples.
PAPER = {
    "caresses": "caress", "ponies": "poni", "ties": "ti", "caress": "caress", "cats": "cat",
    "feed": "feed", "agreed": "agre", "plastered": "plaster", "bled": "bled",
    "motoring": "motor", "sing": "sing", "conflated": "conflat", "troubled": "troubl",
    "sized": "size", "hopping": "hop", "tanned": "tan", "falling": "fall", "hissing": "hiss",
    "fizzed": "fizz", "failing": "fail", "filing": "file", "happy": "happi", "sky": "sky",
    "relational": "relat", "conditional": "condit", "rational": "ration", "digitizer": "digit",
    "hopefulness": "hope", "formalize": "formal", "adjustable": "adjust", "dependent": "depend",
    "adoption": "adopt", "controll": "control", "roll": "roll", "cease": "ceas",
    "probate": "probat", "rate": "rate",
    # And the ones this corpus cares about.
    "evaluation": "evalu", "evaluate": "evalu", "agents": "agent", "agentic": "agent",
    "gpt-4": "gpt-4", "c++": "c++", ".net": ".net", "ai": "ai", "rag": "rag",
}
bad = {w: (atu.stem(w), want) for w, want in PAPER.items() if atu.stem(w) != want}
check("atu.stem() reproduces the Porter paper's examples", not bad, repr(bad))

# The corpus vocabulary, surface tokens before stemming.
vocab = set()
for t in atu.load_talks():
    vocab.update(atu.tokenize(t["title"]))
    vocab.update(atu.tokenize(t["description"]))
    vocab.update(atu.tokenize(" ".join(t["speakers"])))
    vocab.update(atu.tokenize(" ".join(t["tags"])))
if atu.TRANSCRIPTS.exists():
    for p in atu.TRANSCRIPTS.glob("*.json"):
        if p.name.startswith("_"):
            continue
        tr = json.loads(p.read_text())
        vocab.update(atu.tokenize(" ".join(s["text"] for s in tr.get("segments", []))))
vocab = sorted(vocab)
check("the vocabulary is large enough to mean something", len(vocab) > 10000, f"{len(vocab)} tokens")

node = shutil.which("node")
if not node:
    print("SKIP the JavaScript half: node is not installed")
else:
    html = (pathlib.Path(__file__).resolve().parent.parent / "index.html").read_text()
    m = re.search(r"// --- porter stemmer ---\n(.*?)// --- end porter stemmer ---", html, re.S)
    check("index.html carries the stemmer between its markers", bool(m))
    if m:
        with tempfile.TemporaryDirectory() as d:
            js = pathlib.Path(d) / "stem.js"
            words = pathlib.Path(d) / "words.json"
            words.write_text(json.dumps(vocab))
            js.write_text(m.group(1) + "\nconst fs = require('fs');\n"
                          "const ws = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));\n"
                          "process.stdout.write(JSON.stringify(ws.map(stem)));\n")
            out = subprocess.run([node, str(js), str(words)], capture_output=True, text=True)
            check("the JavaScript stemmer runs", out.returncode == 0, out.stderr[-300:])
            if out.returncode == 0:
                js_stems = json.loads(out.stdout)
                py_stems = [atu.stem(w) for w in vocab]
                diffs = [(w, a, b) for w, a, b in zip(vocab, py_stems, js_stems) if a != b]
                check(f"both stemmers agree on all {len(vocab):,} corpus tokens",
                      not diffs, repr(diffs[:10]))

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: " + "; ".join(FAILS))
    sys.exit(1)
print("all checks passed")
