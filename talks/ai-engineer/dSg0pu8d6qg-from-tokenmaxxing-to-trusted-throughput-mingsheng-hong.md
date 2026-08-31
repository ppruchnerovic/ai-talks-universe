---
id: dSg0pu8d6qg
title: "From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad"
slug: from-tokenmaxxing-to-trusted-throughput-mingsheng-hong
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Mingsheng Hong"]
channel: "AI Engineer"
duration_min: 23
published_at: 2026-08-29T00:00:00Z
video_id: dSg0pu8d6qg
youtube_url: https://www.youtube.com/watch?v=dSg0pu8d6qg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad

**Mingsheng Hong**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=dSg0pu8d6qg) · [Conference site](https://www.ai.engineer/)

## Description

An engineer at a large tech company built a voluntary dashboard showing everyone's AI token usage, and colleagues promptly started competing to top it. Mingsheng Hong uses that as the thing not to do. His team runs the same dashboards, but treats them as a smoke detector rather than a leaderboard: a team using surprisingly few tokens is worth a conversation, and nobody should ever be rewarded for burning more. He draws the parallel to lines of code, a number worth tracking and a terrible thing to optimize, given that deleting code is often the better outcome.

The pitfall he flags is going straight from measuring cost to cutting it, because that is only one side of a ratio. So Ironclad measures value too, and the metric evolved in public: lines of code, then open pull requests, then merged ones, and now merged pull requests weighted by a complexity score, since a ten line concurrency fix is not a thousand lines of boilerplate. He calls the target trusted throughput, work that clears objective checks, human review, and finally contact with customers. The bottleneck has moved downstream to review and CI, where slow pipelines quietly push engineers toward giant batched pull requests that are harder to review well. His fix is unglamorous: kill flaky tests, cap agent retry loops, and measure the wait from ready to merged.

Speaker info:
- https://www.linkedin.com/in/mingshenghong/

Timestamps:
0:00 - Token leaderboards, and why they backfire
1:34 - Dashboards as smoke detectors
2:56 - Getting past adoption before managing cost
4:19 - The engineers who lost the craft
5:44 - Trust as the product constraint at Ironclad
7:09 - Measuring cost across several vendors
8:33 - Why cutting cost first is premature
9:58 - Lines of code, and metrics you should not optimize
11:20 - From open pull requests to weighted merges
12:43 - What trusted throughput actually means
14:06 - The bottleneck moves to review and CI
15:30 - AI as the first pass, humans for judgment
16:56 - Flaky tests, babysitting, and morale
18:19 - Guardrails, budgets and anomaly alerts
19:44 - Prompt caching and context pruning
21:09 - What to build and what to buy
