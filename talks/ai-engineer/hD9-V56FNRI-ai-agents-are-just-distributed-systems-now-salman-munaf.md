---
id: hD9-V56FNRI
title: "AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok"
slug: ai-agents-are-just-distributed-systems-now-salman-munaf
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Salman Munaf"]
channel: null
duration_min: 20
published_at: 2026-08-29T00:00:00Z
video_id: hD9-V56FNRI
youtube_url: https://www.youtube.com/watch?v=hD9-V56FNRI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok

**Salman Munaf**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=hD9-V56FNRI) · [Conference site](https://www.ai.engineer/)

## Description

An agent calls a refund tool and the request times out. Did the customer get their money? Salman Munaf uses that to make his central point, which is that a timeout has never meant failure, it means unknown, and an agent's first instinct on any failure is to try again. Without request identifiers, idempotency keys and a status lookup, that instinct refunds someone twice. He works in site reliability at TikTok, and his argument is that the moment a model started calling external services it stopped being a model problem and became a distributed systems problem, complete with every failure mode that field spent decades naming.

The reframing he keeps returning to is that an agent is a probabilistic coordinator. Older systems coordinated multi step workflows too, but they followed a decision tree somebody drew. This one does not, so the determinism has to live in the controls around it: circuit breakers, spend and turn ceilings, compensating actions defined per step, and credentials scoped to separate reads from writes rather than handed over wholesale. He is good on two things teams get wrong. Context that can influence an action is state, so it goes stale and needs invalidation and provenance like any cache. And human approval has to bind to an action, an actor and an expiry, or approving a 30 dollar refund quietly becomes approval for a 300 dollar one.

Speaker info:
- https://www.linkedin.com/in/salman96/

Timestamps:
0:00 - Two incidents that systems thinking would have caught
2:33 - When the architectural boundary left the model
3:46 - The agent as a probabilistic coordinator
4:57 - Every step of the loop crosses a boundary
7:19 - A timeout means unknown, not failure
8:32 - Idempotency keys and status lookups
9:42 - Retry storms, backoff and budgets
10:57 - Context that influences action is state
12:08 - Treating memory as a cache
13:19 - Compensating actions across systems
14:36 - Circuit breakers, rate limits and ceilings
15:43 - Scoped credentials over blanket permissions
16:51 - Why logs are not enough
19:20 - What the system lets it do when it is wrong
