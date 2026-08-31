---
id: EcqMYoIV57A
title: "Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo"
slug: why-more-context-makes-your-agent-dumber-and-what-to-do
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Nupur Sharma"]
channel: null
duration_min: 26
published_at: 2026-06-08T15:00:17Z
video_id: EcqMYoIV57A
youtube_url: https://www.youtube.com/watch?v=EcqMYoIV57A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo

**Nupur Sharma**

`AI Engineer` · `AI Engineer` · `2026` · `26 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=EcqMYoIV57A) · [Conference site](https://www.ai.engineer/)

## Description

Give an agent your full codebase and it will attend to the start and the end, then quietly drop the middle. Nupur from Qodo calls this the U curve and builds the whole talk around it: why growing the context window did not fix the problem, and what actually does. She runs through iterative retrieval, hierarchical summarization, and self correction with honest cost tradeoffs for each.

The second half covers the orchestration paradox: capable models burn most of their tokens deciding how to solve a problem rather than solving it. Her team's fix is an 80/20 split, using high reasoning models for open ended discovery and lighter deterministic models for validation. Qodo's code review architecture runs this live: a context collector feeds specialized agents, a judge node recombines the results and weighs them against PR history, and every accepted or rejected suggestion shifts the weights for the next run.

Speaker info:
- https://www.linkedin.com/in/nupursh/
