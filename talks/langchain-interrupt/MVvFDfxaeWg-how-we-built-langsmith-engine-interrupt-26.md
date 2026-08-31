---
id: MVvFDfxaeWg
title: "How We Built LangSmith Engine | Interrupt 26"
slug: how-we-built-langsmith-engine-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 21
published_at: 2026-05-27T14:07:52Z
video_id: MVvFDfxaeWg
youtube_url: https://www.youtube.com/watch?v=MVvFDfxaeWg
tags: ["LangChain", "LangSmith", "agent observability", "LLM evaluation", "evals for LLMs", "agent debugging", "agent improvement loop", "LLM tracing", "online evalu…LangSmith Engine", "online evaluators", "offline evals", "ground truth dataset", "agent regressions", "deep agents", "production AI agents", "prompt engineering", "AI engineering", "autonomous agents", "self-improving agents", "Interrupt conference", "LangSmith sandbox", "building AI agents", "LangSmith Engine"]
transcript: false
---

# How We Built LangSmith Engine | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `21 min`

`#LangChain` `#LangSmith` `#agent observability` `#LLM evaluation` `#evals for LLMs` `#agent debugging` `#agent improvement loop` `#LLM tracing` `#online evalu…LangSmith Engine` `#online evaluators` `#offline evals` `#ground truth dataset` `#agent regressions` `#deep agents` `#production AI agents` `#prompt engineering` `#AI engineering` `#autonomous agents` `#self-improving agents` `#Interrupt conference` `#LangSmith sandbox` `#building AI agents` `#LangSmith Engine`

[Watch the recording](https://www.youtube.com/watch?v=MVvFDfxaeWg) · [Conference site](https://interrupt.langchain.com/)

## Description

Until now, improving your agent has been a manual process of reading traces, looking for patterns, writing evals, and creating fixes. Now LangSmith Engine can run that cycle for you. It watches your production traces, clusters failures into named issues, diagnoses root causes against your code, and proposes fixes and eval coverage to keep regressions from coming back. You just review and merge improvements.

At LangChain's agent conference Interrupt, Ben Tannyhill and Vivek Trivedy introduced LangSmith Engine and what it unlocks for teams running agents at scale.

How We Built LangSmith Engine | Interrupt 26
00:00 Introduction and context
00:33 LangChain as the Agent Engineering Platform
00:50 Our go-to-market agent and the problems we hit
01:47 Why the current process is broken (customer pain)
02:48 What we set out to build
02:45 LangSmith Engine demo: the prioritized issue inbox
03:14 Engine proposes fixes and opens PRs
03:32 Custom online evaluators
03:46 Dataset examples for offline evals
04:28 Architecture overview: how Engine works end-to-end
05:18 Early customers: Clay, Vanta, Campfire
05:23 The first version: a wind-up toy
06:54 The false positive problem ("Show me the man")
07:53 Architecture deep dive: orchestration and sandboxes
09:49 Why traces are the most valuable input
10:47 Connecting source code for PR generation
11:10 Types of fixes Engine generates
12:02 Learning from customers: the preference problem
12:56 The agent overview: Engine's memory file
13:40 Passing to Viv: evaluating Engine itself
14:04 Why evals are the only answer
14:31 How we bootstrapped evals (dogfooding + synthetic data)
15:24 Building a diverse and rounded eval suite
16:14 How evals inform model selection and prompt decisions
17:41 Beyond evals: trusting user feedback
18:24 The self-improving loop: Engine improving Engine
19:04 Key learnings and closing summary
20:36 Thank you

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/
