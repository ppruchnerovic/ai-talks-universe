---
id: AqU_WyOdEyo
title: "Observing And Testing CX Agents | Interrupt 26"
slug: observing-and-testing-cx-agents-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 23
published_at: 2026-06-10T12:59:00Z
video_id: AqU_WyOdEyo
youtube_url: https://www.youtube.com/watch?v=AqU_WyOdEyo
tags: []
transcript: false
---

# Observing And Testing CX Agents | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=AqU_WyOdEyo) · [Conference site](https://interrupt.langchain.com/)

## Description

At Interrupt, the agent conference by LangChain, Carlos Pereira from Cisco's Customer Experience team showed how you close the loop between production feedback and code at 16 million customer interactions per year.

The core problem with scaling agents: once adoption climbs, feedback volume outpaces your team. Every thumbs down, every confused user, every low-confidence routing decision is a signal. If you treat it as noise, or if your team becomes the bottleneck processing it, adoption drops. This talk walks through the system Cisco built to take a user's thumbs down all the way to a merged PR, with AI handling triage and diagnostics and humans in the loop only where decisions matter.

Observing And Testing CX Agents | Interrupt 26
0:00 Introduction and Day 2 context
0:49 What today covers: observability, testing, and support
1:11 Cisco support at scale: 16M interactions per year
1:34 When network outages hit: why this matters
1:54 CX methodology and team structure
2:16 Evolution: from chatbot to autonomous teammate
2:51 Today's question: closing the production feedback loop
3:23 The approach: continuous feedback loop, not a ticket queue
4:11 Every signal matters: thumbs down, errors, and confusion
4:41 Why humans become the bottleneck at scale
5:57 Signal capture via LangSmith traces
6:12 Triage agent: LangSmith MCP and Jira MCP in practice
6:55 Code agent: clustering and diagnosing issues
7:35 Human in the loop: only on writes, not reads
7:56 Proactive and reactive feedback pipeline
9:20 Treat evals like tests, not experiments
10:56 MCP as the integration layer
11:21 Human oversight only on writes
12:47 Lessons learned
13:53 Observability is your new bottleneck
14:05 Close the feedback loop with agents
14:36 Evals are infrastructure, not a side project
15:34 Support use case: Cisco technical support
15:48 Live example: enterprise network assessment
17:04 2,176 security findings: where do you start?
18:13 Semantic routing for ambiguous prompts
19:33 Parallel pipeline with guardrails
20:55 Tracing every step with LangSmith
21:36 Self-learning routing system
21:54 Observing LangSmith itself with Splunk
22:22 Closing

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/
