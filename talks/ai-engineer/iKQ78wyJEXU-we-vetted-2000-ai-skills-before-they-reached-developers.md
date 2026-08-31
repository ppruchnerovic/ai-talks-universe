---
id: iKQ78wyJEXU
title: "We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank"
slug: we-vetted-2000-ai-skills-before-they-reached-developers
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Lucas Palma"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-07-29T22:00:06Z
video_id: iKQ78wyJEXU
youtube_url: https://www.youtube.com/watch?v=iKQ78wyJEXU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank

**Lucas Palma**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=iKQ78wyJEXU) · [Conference site](https://www.ai.engineer/)

## Description

An AI skill is a piece of code you hand a model to extend what it can do, and once engineers start sharing skills with each other, each one becomes a supply chain risk, more so inside a regulated bank. Lucas Palma's security team at Nubank built Skill Vector to sit between a skill and the internal marketplace, so nothing reaches developers unvetted. Every skill is scanned first with deterministic checks, for destructive shell commands and the like, then with an LLM for the context those checks miss, and only then does it get a decision and permissions scoped to who will use it.

Running that gate over more than 2,000 skills surfaced real problems, since a single skill can carry many, and fed them into the bank's vulnerability management program with approval gates and human confirmation. What worked was pairing deterministic scans with LLM review; what needed work was the guidance the system gave and the habit of running skills locally before vetting. The lesson he leaves is simple: treat skills like any other dependency, and only what clears the gate belongs in the marketplace.

Speaker info:
- https://www.linkedin.com/in/lucaspalma/

Timestamps:
0:00 - Introduction: making code safe at a bank
1:32 - AI skills as a supply chain risk
2:50 - What counts as an AI skill
3:57 - The extra weight of a regulated environment
6:07 - From plugins to a vetted marketplace
6:58 - What Skill Vector does
7:37 - Deterministic checks, then the LLM
10:00 - Scanning over two thousand skills
11:22 - What worked and what needed improvement
13:30 - Approval gates and human confirmation
14:23 - Next steps and policies
