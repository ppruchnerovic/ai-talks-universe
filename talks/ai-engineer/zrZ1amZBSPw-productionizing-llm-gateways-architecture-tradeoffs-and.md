---
id: zrZ1amZBSPw
title: "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio"
slug: productionizing-llm-gateways-architecture-tradeoffs-and
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kanish Manuja"]
channel: null
duration_min: 16
published_at: 2026-08-28T15:30:03Z
video_id: zrZ1amZBSPw
youtube_url: https://www.youtube.com/watch?v=zrZ1amZBSPw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio

**Kanish Manuja**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zrZ1amZBSPw) · [Conference site](https://www.ai.engineer/)

## Description

Something went wrong, please try again. Kanish Manuja opens on that message and then explains why it exists, which is more interesting than laziness. Once a response starts streaming you have committed to that provider. Tokens already sent cannot be recalled, so the fallback you carefully built is unavailable exactly when you need it. Streaming buys perceived speed by trading away your levers, and that error string is what the trade costs. His frame for an LLM gateway is a permanent fight between availability, latency, guardrails and cost, where degradation forces you to give one of them up.

The advice is refreshingly specific about where normal engineering instincts mislead. Retrying a slow expensive call eats the latency budget and multiplies spend, and tripping a circuit breaker is silly when a healthy second provider is sitting right there, so prefer per request fallback. Do not measure gateway wide latency, because a reasoning model's normal is a chat model's outage; track P99 per model per route and set timeouts the same way, since a missing timeout is his top cause of silent outages. Treat guardrails as services that fail too, and decide in advance whether you fail open or closed. He also argues most teams asking for a central gateway actually want centralized governance, which does not require centralizing the traffic.

Speaker info:
- https://www.linkedin.com/in/kanish-manuja-a99bb923/

Timestamps:
0:00 - The message behind the message
1:21 - Four things you cannot all maximize
2:33 - Why retries and breakers mislead here
3:39 - Per request fallback, and where failure counts live
4:49 - Fallbacks are not transparent
5:55 - Give the backup provider more headroom, not less
7:08 - Mixed workloads and the aggregate latency lie
8:17 - Reasoning and router models, 2 seconds to 60
9:28 - Hedging the tail
10:40 - Guardrails that fail open or closed
11:53 - Time budgets, fallbacks and placement
13:02 - The gateway as a new dependency
14:11 - Load shedding under a retry storm
15:18 - Centralized governance without a central gateway
