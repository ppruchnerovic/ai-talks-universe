---
id: kZsf_Sfm7RU
title: "The Missing Layer After Launch - Raphael Kalandadze, Wandero AI"
slug: the-missing-layer-after-launch-raphael-kalandadze-wandero-ai
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Raphael Kalandadze"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-07-05T03:15:05Z
video_id: kZsf_Sfm7RU
youtube_url: https://www.youtube.com/watch?v=kZsf_Sfm7RU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Missing Layer After Launch - Raphael Kalandadze, Wandero AI

**Raphael Kalandadze**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=kZsf_Sfm7RU) · [Conference site](https://www.ai.engineer/)

## Description

We run a production system of agents for real customers. The team that keeps it healthy is also made of agents.

Operating an agent product isn't like operating software. When our agent fails a customer — a dropped constraint, a stale price, a confident wrong answer — nothing crashes and no log lights up. The failure is in the conversation, not the stack trace. So we put agents on the operations:

- One monitors production conversations and judges where the agent actually let a customer down — across thousands of live sessions, not a sampled few.
- One watches logs and system health and traces real problems back into the code.
- One writes and runs tests, because "green CI" means nothing for a non-deterministic agent.
- One reviews every PR — human or agent-authored — against a single question: root cause, or just the symptom?

Humans stay at the merge and approval boundaries. The agents do the watching, judging, testing, and drafting that no human team could keep up with at this volume.

This talk is the honest version: what each operating agent actually checks, where we trust it and where we don't, what breaks, and why operating an agent system is becoming its own engineering discipline — done, increasingly, by agents.

Speakers:
- Raphael Kalandadze (Wandero AI): Co-founder and CTO of Wandero AI, an agent-native operating system for travel and hospitality, and co-founder of Tbilisi AI Lab, where we build the first Georgian large language model.
X/Twitter: @RaphaelKalan
