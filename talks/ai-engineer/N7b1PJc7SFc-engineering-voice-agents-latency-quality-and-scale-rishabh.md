---
id: N7b1PJc7SFc
title: "Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI"
slug: engineering-voice-agents-latency-quality-and-scale-rishabh
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rishabh Bhargava"]
channel: null
duration_min: 25
published_at: 2026-05-31T00:00:00Z
video_id: N7b1PJc7SFc
youtube_url: https://www.youtube.com/watch?v=N7b1PJc7SFc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI

**Rishabh Bhargava**

`AI Engineer` · `AI Engineer` · `2026` · `25 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=N7b1PJc7SFc) · [Conference site](https://www.ai.engineer/)

## Description

Users notice latency above 500ms and hang up above one second. In an already optimized pipeline, 75ms of network latency from models sitting in a different data center adds 30% overhead. Colocating everything in the same building drops that to around 5ms. Rishabh Bhargava from Together AI walks through the full speech to text, LLM, and text to speech pipeline at that level of specificity.

The LLM dominates the budget: 200 to 300ms time to first token target, 8 to 30B parameter range — larger models blow the latency budget, smaller ones break tool calling. Speech to text target is P90 under 100ms with around 6% word error rate. One pattern for handling complex workflows without adding latency: a small thinker LLM handles conversation flow and issues a single tool call to a larger model when the request is complex, keeping the fast path fast.

Speaker info:
- https://www.linkedin.com/in/bhargavarishabh
