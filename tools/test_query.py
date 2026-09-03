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

import os
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
      Q.parse_query("agents agents agents").strict == '"agents"', Q.parse_query("agents agents agents").strict)

print("\n-- column filters reach FTS5 as filters --")
p = Q.parse_query("title:agents")
check("title:agents is not split on the colon", p.strict == "title:agents", p.strict)
check("and is a metadata-layer expression", p.meta == "title:agents" and p.seg is None, (p.meta, p.seg))
check("and a gate", p.gate == ("title:agents",), p.gate)
p = Q.parse_query('speakers:"harrison chase"')
check("a quoted phrase keeps its prefix unquoted", p.strict == 'speakers:"harrison chase"', p.strict)
check("a column set passes through", Q.parse_query("{title tags}:rag").strict == "{title tags}:rag",
      Q.parse_query("{title tags}:rag").strict)
check("an alias is normalised", Q.parse_query("speaker:chase").strict == "speakers:chase",
      Q.parse_query("speaker:chase").strict)
check("a punctuated term after the prefix is quoted", Q.parse_query("title:gpt-4").strict == 'title:"gpt-4"',
      Q.parse_query("title:gpt-4").strict)
p = Q.parse_query("transcript:kubernetes")
check("transcript: is for the passage layer only", p.meta is None and p.seg == "kubernetes", (p.meta, p.seg))
p = Q.parse_query('speakers:"harrison chase" agents')
check("a filter beside a word: each layer takes what it can match",
      p.meta == 'speakers:"harrison chase" agents' and p.seg == "agents", (p.meta, p.seg))
check("and every item gates", p.gate == ('speakers:"harrison chase"', "agents"), p.gate)
check("a colon with a space after it is not a filter",
      Q.parse_query("agents: what works").strict == '"agents" AND "works"',
      Q.parse_query("agents: what works").strict)
check("a prefix that is not a column is a bare term", Q.parse_query("12:30 talk").terms == ("12", "30"),
      Q.parse_query("12:30 talk").terms)
check("a bare URL stays a bare query", Q.parse_query("https://x.com").terms == ("https", "x.com"),
      Q.parse_query("https://x.com").terms)

print("\n-- -word exclusion --")
p = Q.parse_query("agents -rag")
check("-word leaves the query", p.terms == ("agents",) and p.strict == '"agents"', p)
check("and is recorded", p.excluded == ("rag",), p.excluded)
p = Q.parse_query("-rag")
check("only exclusions is a listing", p.strict == "" and p.excluded == ("rag",), p)
check("a lone dash excludes nothing", Q.parse_query("agents -").excluded == (), Q.parse_query("agents -").excluded)
check("explicit NOT is left to FTS5", Q.parse_query("agents NOT rag").excluded == ()
      and Q.parse_query("agents NOT rag").strict == "agents NOT rag")

print("\n-- synonyms --")
p = Q.parse_query("mcp")
check("a word in a group carries the group", p.groups == (("mcp", "model context protocol"),), p.groups)
check("a multi-word member is a quoted phrase", p.strict == '("mcp" OR "model context protocol")', p.strict)
check("membership is by stem", Q.parse_query("databases").groups == (("databases", "db"),),
      Q.parse_query("databases").groups)
check("a word outside every group is alone", Q.parse_query("agents").groups == (("agents",),))
p = Q.parse_query("vector db")
check("relaxed is the OR of every member",
      p.relaxed == '"vector" OR "db" OR "database" OR "databases"', p.relaxed)
check("explicit syntax is never expanded", Q.parse_query("mcp OR agents").strict == "mcp OR agents",
      Q.parse_query("mcp OR agents").strict)
check("a group is one gate term", Q.group_expr(("a", "b c")) == '("a" OR "b c")', Q.group_expr(("a", "b c")))
check("a single member is just quoted", Q.group_expr(("a",)) == '"a"')

print("\n-- helpers --")
p = Q.parse_query("agent reliability zzzqqq")
k = Q.kept_query(p, ("zzzqqq",))
check("kept_query drops the relaxed word", k.terms == ("agent", "reliability")
      and k.strict == '"agent" AND "reliability"', k)
check("and is the query itself when nothing was dropped", Q.kept_query(p, ()) is p)
check("excerpt_query: a bare query as searched",
      Q.excerpt_query(p, ("zzzqqq",)).terms == ("agent", "reliability"))
check("excerpt_query: a metadata-only filter has nothing to excerpt on",
      Q.excerpt_query(Q.parse_query('speakers:"harrison chase"'), ()) is None)
check("excerpt_query: transcript: is its passage-layer part",
      Q.excerpt_query(Q.parse_query("transcript:kubernetes"), ()).strict == "kubernetes")
check("excerpt_query: plain explicit syntax passes whole",
      Q.excerpt_query(Q.parse_query("agents OR rag"), ()).strict == "agents OR rag")
check("semantic_text drops the exclusions and keeps the question",
      Q.semantic_text("how do agents fail -rag") == "how do agents fail",
      Q.semantic_text("how do agents fail -rag"))
hits = [{"n": 1, "id": "a", "title": "Agent Evals"}, {"n": 2, "id": "b", "title": "agent  evals!"},
        {"n": 3, "id": "c", "title": "Other"}, {"n": 4, "id": "d", "title": "AGENT EVALS"}]
out = Q.collapse_dupes(None, hits)
check("collapse_dupes keeps the first of a title and lists the rest",
      [h["id"] for h in out] == ["a", "c"] and out[0]["also"] == ["b", "d"] and out[1]["also"] == [],
      [(h["id"], h["also"]) for h in out])
check("--fields accepts the new keys", Q.parse_fields("id,also,via,excerpt", False) == ["id", "also", "via", "excerpt"])
try:
    Q.parse_fields("id,nope", False)
    check("--fields rejects an unknown key", False)
except SystemExit as e:
    check("--fields rejects an unknown key", "nope" in str(e))
check("--color wins", Q.want_color(True) is True and Q.want_color(False) is False)
os.environ["NO_COLOR"] = "1"
check("NO_COLOR wins over a terminal", Q.want_color(None) is False)
del os.environ["NO_COLOR"]
check("a pipe gets no colour", Q.want_color(None) is False)

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
