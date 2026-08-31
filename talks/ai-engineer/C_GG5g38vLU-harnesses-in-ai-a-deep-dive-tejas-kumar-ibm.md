---
id: C_GG5g38vLU
title: "Harnesses in AI: A Deep Dive — Tejas Kumar, IBM"
slug: harnesses-in-ai-a-deep-dive-tejas-kumar-ibm
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Tejas Kumar"]
channel: null
duration_min: 20
published_at: 2026-05-17T17:30:06Z
video_id: C_GG5g38vLU
youtube_url: https://www.youtube.com/watch?v=C_GG5g38vLU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

**Tejas Kumar**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=C_GG5g38vLU) · [Conference site](https://www.ai.engineer/)

## Description

Tejas will be back on stage at the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

The agent hit a login page, panicked, reported success anyway, and the upvote never happened. Tejas Kumar's diagnosis: not a prompt problem. A harness problem.

The demo builds a browser agent on GPT-3.5 Turbo (consciously choosing a VERY old model to show how good harness eng can improve it a lot) against Hacker News and layers in a harness without touching the prompt once. Guardrails cap iterations and compact context. A verify step reads the tool call history to catch the agent lying about what it did. A login handler watches the browser URL each loop and injects credentials programmatically when it hits the login page. By the end the cheap old model reliably logs in and upvotes the post.

Speaker info:
- https://x.com/TejasKumar_
- https://www.linkedin.com/in/tejasq/
- https://github.com/TejasQ

Timestamps:
0:00 Introduction to Tejas Kumar and AI Harnesses
1:45 Why we use harnesses: Reliability and control
3:00 Defining an agent harness from first principles
4:32 Key components of an agent harness (Tooling, Context, Guardrails)
5:59 Starting the demo: Building a browser agent
7:00 Inspecting the initial agent loop
8:12 The problem: Agent failure and hallucination
10:20 Adding guardrails and context management
11:54 Refactoring into a formal harness
13:02 Implementing a verify step to catch lies
15:36 Implementing a login handler for programmatic access
17:42 Final demonstration: Successful autonomous upvoting
18:34 Summary and the future of dynamic harnesses
