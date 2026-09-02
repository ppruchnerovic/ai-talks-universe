#!/usr/bin/env python3
"""Offline checks for the topic facet in atu.py and sync_catalog.py — no corpus.

topics_of() is a pure function of a title, its tags and its description, and
its mistakes are the quiet kind: a talk shelved under a topic it is not about,
found by nobody until someone filters on that topic and reads the list. Each
case here is a shape the corpus actually has, a boundary the design fixed as
a rule (a bare "enterprise" is a product tier, a bare tool name is not the
SDLC), or a false positive the first run over the corpus actually produced
(PyData's boilerplate, AI Engineer's channel-wide tags).

    cd tools && python3 test_topics.py
"""

import re
import sys

sys.path.insert(0, ".")
import atu
import sync_catalog as S

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


T = atu.topics_of
AGENTS, CODING, SDLC, RAG, EVALS, PROMPT, SEC, GOV, INFRA, TRAIN, DATA, MM, ENT, SCI, ML = atu.TOPIC_NAMES


print("-- every topic fires on a title that names it --")
for topic, title in [
    (AGENTS, "Building Multi-Agent Systems with MCP"),
    (CODING, "Vibe Coding a SaaS with Claude Code in an Afternoon"),
    (SDLC, "Spec-Driven Development: Agentic Coding at FAANG Scale"),
    (RAG, "GraphRAG: Knowledge Graphs Meet Retrieval"),
    (EVALS, "Evals Are All You Need — Observability for LLM Apps"),
    (PROMPT, "Context Engineering Beyond the System Prompt"),
    (SEC, "Prompt Injection and Jailbreaks: Red Teaming Agents"),
    (GOV, "The EU AI Act and Responsible AI in Practice"),
    (INFRA, "Serving Llama at Scale with vLLM on Kubernetes"),
    (TRAIN, "Fine-Tuning with LoRA and RLHF From Scratch"),
    (DATA, "MLOps on Databricks: Feature Stores and Lakehouses"),
    (MM, "Voice Agents and Vision-Language Models for Robotics"),
    (ENT, "Enterprise AI Adoption: From Pilot to Production"),
    (SCI, "Drug Discovery and Clinical Trials with Foundation Models"),
    (ML, "Time Series Forecasting with XGBoost and scikit-learn"),
]:
    got = T(title, [], "")
    check(f"{topic[:32]:<32} <- {title[:50]!r}", topic in got, repr(got))

print("\n-- and stays out of a title that does not --")
for topic, title in [
    (AGENTS, "Container Orchestration at Scale with Kubernetes"),
    (CODING, "Microsoft 365 Copilot for Sales Teams"),
    (SDLC, "Cursor Tips and Tricks for Beginners"),
    (RAG, "Dragging Your Feet on Storage Vectors? (Not This Talk)"),
    (EVALS, "Monitoring Kubernetes Clusters with Prometheus"),
    (PROMPT, "Prompt Injection: The Attack Nobody Fixed"),
    (SEC, "Rust Ownership and the Borrow Checker Explained"),
    (GOV, "Kubernetes Network Policy Deep Dive"),
    (INFRA, "Making Inferences About Your Users From Their Clicks"),
    (TRAIN, "Training Your Team to Use ChatGPT"),
    (DATA, "Streaming Tokens to the Browser with SSE"),
    (MM, "Our Vision for the Next Decade of Java"),
    (ENT, "Enterprise-Grade Kubernetes for Regulated Workloads"),
    (SCI, "Computer Science Fundamentals Every Engineer Forgets"),
    (ML, "Deploying LLM Apps to Kubernetes"),
]:
    got = T(title, [], "")
    check(f"{topic[:32]:<32} -/-> {title[:50]!r}", topic not in got, repr(got))

print("\n-- the boundaries that are rules --")
check("'enterprise' alone is a product tier, not adoption",
      ENT not in T("Enterprise features in our new release", [], "Enterprise customers get SSO and audit logs."))
check("'enterprise AI' is adoption", ENT in T("Enterprise AI in 2026", [], ""))
check("a bare tool name is coding, not the SDLC",
      T("A Cursor Demo", [], "") == [CODING], repr(T("A Cursor Demo", [], "")))
check("the tool plus the process is both",
      {CODING, SDLC} <= set(T("Cursor in Our Code Review Pipeline", [], "")))
check("'Copilot' alone is not a coding assistant (half of Microsoft's are M365)",
      CODING not in T("What's new in Copilot", [], "Copilot in Excel and Copilot in Teams."))
check("'GitHub Copilot' is", CODING in T("What's new in GitHub Copilot", [], ""))
check("'prompt injection' is security, not prompting",
      T("Prompt Injection 101", [], "") == [SEC], repr(T("Prompt Injection 101", [], "")))

print("\n-- the scoring rule --")
check("a title mention is enough by itself", AGENTS in T("Agents", [], ""))
check("one phrase in the description is below the bar",
      RAG not in T("Untitled", [], "We use embeddings."))
check("two distinct phrases in the description reach it",
      RAG in T("Untitled", [], "We use embeddings and a vector database."))
check("the same phrase twice is one phrase",
      RAG not in T("Untitled", [], "Embeddings, embeddings, embeddings."))
check("two spellings of one phrase are one phrase",
      RAG not in T("Untitled", [], "An embedding. Several embeddings."))
check("a tag counts like a description phrase, not like a title",
      RAG not in T("Untitled", ["RAG"], "") and RAG in T("Untitled", ["RAG"], "We use embeddings."))
check("a talk that scores nothing gets []", T("Welcome and Opening Remarks", [], "") == [])
check("the list is sorted", T("Evals for Agents", [], "") == sorted(T("Evals for Agents", [], "")))
check("None and empty inputs are fine", T(None, None, None) == [])
check("bold-Unicode descriptions are read (NFKC)",
      RAG in T("Untitled", [], "𝗘𝗺𝗯𝗲𝗱𝗱𝗶𝗻𝗴𝘀 and a 𝘃𝗲𝗰𝘁𝗼𝗿 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲."))
check("topic_scores reports the partial scores topics_of does not assign",
      atu.topic_scores("Untitled", [], "We use embeddings.") == {RAG: 1},
      repr(atu.topic_scores("Untitled", [], "We use embeddings.")))

print("\n-- the boundaries AI_RE uses --")
check("'rag' does not fire inside 'storage'", RAG not in T("Object Storage at Scale", [], ""))
check("'rag' does not fire inside 'drag-and-drop'", RAG not in T("Drag-and-drop UIs", [], ""))
check("'ml' does not fire inside 'html'", ML not in T("HTML for Machines", [], ""))
check("a trailing hyphen is allowed: 'GPU-accelerated'", INFRA in T("GPU-accelerated Pandas", [], ""))
check("'agents' matches in any case", AGENTS in T("AGENTS EVERYWHERE", [], ""))

print("\n-- every pattern compiles and matches its own canonical phrase --")


def canonical(pattern: str) -> str:
    """A phrase the pattern ought to match, read off the pattern itself.

    First alternative of every group, optional pieces dropped, `\\w*` as "x".
    Not a regex engine — just enough to catch a pattern that can match
    nothing, which is the typo nobody would ever see.
    """
    s = pattern.replace("\\.", ".").replace("\\w*", "x").replace("\\w+", "x")
    s = re.sub(r"\(\?[!=][^)]*\)", "", s)                  # lookarounds
    s = re.sub(r"\.\{0,\d+\}", "", s)                       # .{0,40}
    for _ in range(4):
        s = re.sub(r"\((?:\?:)?([^()]*)\)\?", "", s)        # (group)? -> ''
        s = re.sub(r"\((?:\?:)?([^()|]*)\|[^()]*\)", r"\1", s)  # (a|b) -> a
        s = re.sub(r"\((?:\?:)?([^()]*)\)", r"\1", s)        # (a) -> a
    s = re.sub(r"\[- \]", " ", s).replace("[sz]", "s").replace("[cs]", "c")
    s = re.sub(r"(?<!\\)(.)\?", "", s)                       # x? -> ''
    return s.replace("\\", "")


for name, phrases, whole in atu.TOPIC_RES:
    for p in phrases:
        raw = p.pattern[len("(?<![\\w-])(?:"):-len(")(?!\\w)")]
        text = canonical(raw)
        check(f"{name[:18]:<18} /{raw[:44]}/ matches {text!r}", bool(p.search(text)) and bool(whole.search(text)))
check("fifteen topics, no duplicate names", len(atu.TOPIC_NAMES) == 15 == len(set(atu.TOPIC_NAMES)))
check("every phrase is attributed to exactly one index",
      all(atu._phrase_index(i, m.group().lower()) >= 0
          for i, (_, phrases, whole) in enumerate(atu.TOPIC_RES)
          for m in whole.finditer("agents rag evals gpu security mlops embeddings copilot")))

print("\n-- boilerplate: what one conference repeats is the channel's, not the talk's --")
stock = "PyData is an educational program of NumFOCUS, a non-profit for data science and machine learning."
descs = [f"Talk {i} about its own thing.\n{stock}" for i in range(12)]
lines, tags = S.boilerplate(descs, [["python", "education", "numfocus"] + (["rag"] if i == 0 else [])
                                    for i in range(12)])
check("a line in every description is boilerplate", " ".join(stock.split()).lower() in lines, repr(lines))
check("a line said once is not", not any("talk 3" in l for l in lines))
check("a tag on every video is a channel tag; one on one video is not",
      tags == {"python", "education", "numfocus"}, repr(tags))
check("fewer talks than the floor: nothing is boilerplate",
      S.boilerplate(descs[:5], [["education"]] * 5) == (set(), set()))
check("short repeated lines are headings, not boilerplate",
      "speakers:" not in S.boilerplate(["Speakers:\nA B"] * 12, [[]] * 12)[0])
stripped = S.without_lines(descs[0], lines)
check("without_lines removes exactly the stock line", stripped == "Talk 0 about its own thing.", repr(stripped))
check("…which is what keeps the channel's subject off every talk",
      ML not in T("A Talk About Rust", ["python"], stripped)
      and ML in T("A Talk About Rust", ["python"], descs[0]))
check("without_lines with nothing to strip returns the text", S.without_lines("x\ny", set()) == "x\ny")

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: " + "; ".join(FAILS))
    sys.exit(1)
print("all checks passed")
