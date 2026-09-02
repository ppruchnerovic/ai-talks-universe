#!/usr/bin/env python3
"""Offline checks for query.py's query parsing — no database, no network.

parse_query() and explicit_query() are pure functions of the text typed, and
every mistake in them is one the user sees as SQLite's error rather than as a
result: `gpt-4 OR claude` used to die with "no such column: 4", `c++ OR rust`
with a syntax error, and a comma anywhere in an explicit query with either.
The skill recommends exactly these OR-chains, so they are checked here, along
with the id resolution excerpt.py does on a markdown path — one in six video
ids contains the hyphen that used to cut them short.

    cd tools && python3 test_query.py
"""

import sys

sys.path.insert(0, ".")
import query as Q
import excerpt as E

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


def strict(raw):
    return Q.parse_query(raw).strict


print("\n-- explicit queries: terms FTS5 would misread are quoted --")
check("hyphen: gpt-4 OR claude", strict("gpt-4 OR claude") == '"gpt-4" OR claude',
      strict("gpt-4 OR claude"))
check("hyphen: fine-tuning OR rag", strict("fine-tuning OR rag") == '"fine-tuning" OR rag',
      strict("fine-tuning OR rag"))
check("plus: c++ OR rust", strict("c++ OR rust") == '"c++" OR rust', strict("c++ OR rust"))
check("a comma outside NEAR is dropped",
      strict("evals OR guardrails, jailbreak") == "evals OR guardrails OR jailbreak",
      strict("evals OR guardrails, jailbreak"))
check("a prefix star stays outside the quotes",
      strict("gpt-4* OR agent*") == '"gpt-4"* OR agent*', strict("gpt-4* OR agent*"))
check("an already-quoted phrase is left alone",
      strict('"prompt injection" OR jailbreak') == '"prompt injection" OR jailbreak')
check("a bareword is left bare", strict("evals OR guardrails") == "evals OR guardrails")
check("non-ASCII is a bareword", strict("über OR agent") == "über OR agent", strict("über OR agent"))
check("an apostrophe makes a term quoted", strict("don't OR cannot") == '"don\'t" OR cannot',
      strict("don't OR cannot"))

print("\n-- explicit queries: structure is preserved --")
check("NEAR keeps its parentheses and comma",
      strict("NEAR(agent memory, 5)") == "NEAR ( agent memory , 5 )", strict("NEAR(agent memory, 5)"))
check("parentheses pass through, terms still quoted",
      strict("(gpt-4 OR claude) AND evals") == '( "gpt-4" OR claude ) AND evals',
      strict("(gpt-4 OR claude) AND evals"))
check("NOT passes through", strict("agents NOT langchain") == "agents NOT langchain")
check("a flat OR chain is de-duplicated",
      strict("evals OR evals OR guardrails") == "evals OR guardrails")
check("unbalanced quotes are left for FTS5 to report", strict('"prompt OR x') == '"prompt OR x')

print("\n-- bare queries --")
p = Q.parse_query("context engineering")
check("a bare query is ANDed", p.strict == '"context" AND "engineering"', p.strict)
check("and carries an OR to relax to", p.relaxed == '"context" OR "engineering"', p.relaxed)
check("a single word has nothing to relax to", Q.parse_query("agents").relaxed is None)
check("repeated words are de-duplicated",
      Q.parse_query("evals evals evals").strict == '"evals"', Q.parse_query("evals evals evals").strict)

print("\n-- ids in a markdown file name --")
check("a YouTube id with a hyphen", E.ids_in_filename("O72p-rBb2bA-evals-driven.md")[0] == "O72p-rBb2bA",
      E.ids_in_filename("O72p-rBb2bA-evals-driven.md"))
check("a YouTube id that starts with a hyphen",
      E.ids_in_filename("-3U1ekNsCA0-wtf-are-we-doing.md")[0] == "-3U1ekNsCA0",
      E.ids_in_filename("-3U1ekNsCA0-wtf-are-we-doing.md"))
cands = E.ids_in_filename("iq-5-principles-llm-behavior-rules-for-understanding.md")
check("an InfoQ id is tried longest prefix first",
      cands[0] == "iq-5-principles-llm-behavior-rules-for-understanding"
      and "iq-5-principles-llm-behavior" in cands and cands.index("iq-5-principles-llm-behavior")
      < cands.index("iq-5"), cands[:3])
check("a plain id needs no file name", E.ids_in_filename("dQw4w9WgXcQ") == ["dQw4w9WgXcQ"],
      E.ids_in_filename("dQw4w9WgXcQ"))

print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else "all checks passed"))
sys.exit(1 if FAILS else 0)
