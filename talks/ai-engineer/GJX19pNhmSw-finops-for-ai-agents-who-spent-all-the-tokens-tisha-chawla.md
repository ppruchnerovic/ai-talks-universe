---
id: GJX19pNhmSw
title: "FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft"
slug: finops-for-ai-agents-who-spent-all-the-tokens-tisha-chawla
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 21
published_at: 2026-08-22T00:00:00Z
video_id: GJX19pNhmSw
youtube_url: https://www.youtube.com/watch?v=GJX19pNhmSw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=GJX19pNhmSw) · [Conference site](https://www.ai.engineer/)

## Description

Turning the full policy suite on cut average agent spend by about 78% across benchmark runs on two open source repos, and lifted the share of runs that actually completed from 67% to roughly 96%. That second number is the point. Simple throttling holds the bill down by killing runs, so Tisha Chawla and Susheem Koul built their control plane to steer instead. Their framing is that every software era grew a control surface, usage caps in SaaS, autoscaling policies in cloud, and the agentic era still has none at the layer where code calls a model. Gateways can hard cap and downgrade, but nothing sits between your code and the spend it triggers.

The design splits in two. In your code an annotation marks a boundary around methods you already have, floating attribution up without a rewrite, while a governor holds the list of actions you authorized so the control plane cannot do whatever it likes to your agent. The control plane groups runs into segments by any dimension you emit, sets budgets against a time window, and attaches policies. Actions come in two flavors. Halt is a circuit breaker. Steer is the interesting one: a cost guard watches both how much of the budget is gone and how fast it is going, and when it predicts an overrun it injects an instruction to keep outputs succinct rather than killing the run. They demo it in preview mode first, policies evaluating with enforcement off, which is how you would actually introduce this to a production agent.

Speaker info:
- https://www.linkedin.com/in/tisha-chawla
- https://dev.to/tisha
- https://www.linkedin.com/in/susheemkoul
- https://susheemk.substack.com

Timestamps:
0:00 - From token maxxing to value maxxing
1:58 - Every era got a control surface, this one has not
4:30 - First principles at the model call boundary
6:19 - Why gateways are not enough
8:57 - The SDK side: boundary, ledger, governor
13:13 - Segments, budgets, actions, policies
14:53 - Halt versus steer
16:36 - Demo: preview mode, then enforcement
18:17 - Cost guard, and steering on velocity
19:06 - Benchmark results and the policy catalog
20:47 - A self learning control plane
