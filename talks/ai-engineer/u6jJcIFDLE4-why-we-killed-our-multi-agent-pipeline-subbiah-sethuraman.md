---
id: u6jJcIFDLE4
title: "Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates"
slug: why-we-killed-our-multi-agent-pipeline-subbiah-sethuraman
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 15
published_at: 2026-07-23T05:00:02Z
video_id: u6jJcIFDLE4
youtube_url: https://www.youtube.com/watch?v=u6jJcIFDLE4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=u6jJcIFDLE4) · [Conference site](https://www.ai.engineer/)

## Description

Their first pharma analytics system mimicked a human analyst: one agent to detect a signal, one to localize it, one to find the cause, one to synthesize, all wired to an orchestrator. It produced answers like this: prescriptions dropped 18% in a territory because a payer moved the drug to a worse tier, so send more sales reps. The cause was right and the action was wrong, because no single agent owned the whole picture. So Subbiah Sethuraman's team at ZS killed the multi agent pipeline.

Instead of redesigning the topology, they opened an empty directory, gave Claude Code bash and the database, and watched what it actually did. The rebuild came out smaller, not bigger. Signal detection moved into a deterministic pipeline that runs before the agent wakes up, so the agent investigates rather than guesses. A single agent owns the reasoning and spawns sub agents only when a focused lookup needs one. A pharma knowledge graph acts as a control plane, not a lookup table: every edge is a hypothesis the agent tests against the data, which bounds the search. The result does in 20 minutes what an analyst did in a month.

Speaker info:
- https://www.linkedin.com/in/subbiahsethuraman/
- https://subbiah-sethuraman.medium.com/

Timestamps:
0:00 - Pharma commercial analytics and the analyst's four steps
2:33 - V1: an agent for every step
3:26 - Why the output was incoherent
4:32 - Why it failed: signals, handoffs, and missing domain
5:57 - The rebuild: watching Claude Code in an empty directory
7:01 - Deterministic signal detection before the agent
8:05 - Consolidating to a single agent
9:22 - The knowledge graph as a control plane
11:04 - Every edge a hypothesis, and the result
