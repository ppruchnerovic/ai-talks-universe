---
id: hacEQHHhu2Q
title: "Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google"
slug: why-large-tiny-lms-agents-on-edge-robotics-cormac-brick
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Cormac Brick"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-07-25T17:00:06Z
video_id: hacEQHHhu2Q
youtube_url: https://www.youtube.com/watch?v=hacEQHHhu2Q
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google

**Cormac Brick**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=hacEQHHhu2Q) · [Conference site](https://www.ai.engineer/)

## Description

The constraint on edge AI is not compute, it is RAM, and it is getting worse: phone makers are shipping less of it this year, and a 6GB Raspberry Pi costs 2.5 times what it did at launch. So Cormac Brick's team at Google AI Edge spends its effort making models small enough to fit. A 2 billion parameter Gemma, quantized to 2.9 bits per weight, runs on a Raspberry Pi at about 8 tokens per second and on a Qualcomm NPU fast enough for a few frames of vision a second.

Below that sit tiny models, from 500 million parameters down to 50, that reach the older laptops and cheap devices where even a small model will not fit. They usually need fine tuning rather than prompting, but the payoff is real: a fine tuned Gemma turns free text into the right function call across ten actions at over 86% reliability, and putting a speech model in front gives you voice to function calling. One shipped example is an offline voice dictation app with no subscription, built on two sub billion Gemma models that also strip your ums and ahs.

Speaker info:
- https://x.com/cormacb
- https://www.linkedin.com/in/cbrick/
- https://github.com/google-ai-edge/gallery

Timestamps:
0:00 - Why intelligence at scale needs tiny models
1:17 - The Google AI Edge team and its open source stack
2:35 - Why run on the edge at all
3:25 - The real constraint: DRAM cost
4:40 - Small models: 1 to 4 billion parameters
6:08 - Shrinking Gemma to 2.9 bits per weight
7:36 - Decode speeds across Raspberry Pi, Jetson, and NPUs
9:30 - Try it yourself: AI Edge Gallery and a hobby robot
12:07 - When small is still too big: tiny models
13:24 - Off the shelf tiny models: ASR, vision, embeddings
14:28 - Fine tuning for voice to function calling
17:50 - In production: offline voice dictation
19:30 - Takeaways and Q&A
