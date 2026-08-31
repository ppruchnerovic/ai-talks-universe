---
id: xbPriQWXtWM
title: "The Base Model Is Dead — Varun Singh, Arcee AI"
slug: the-base-model-is-dead-varun-singh-arcee-ai
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Varun Singh"]
channel: null
duration_min: 18
published_at: 2026-07-31T20:30:21Z
video_id: xbPriQWXtWM
youtube_url: https://www.youtube.com/watch?v=xbPriQWXtWM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Base Model Is Dead — Varun Singh, Arcee AI

**Varun Singh**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=xbPriQWXtWM) · [Conference site](https://www.ai.engineer/)

## Description

The old story is that a base model is a mirror of the internet, a good model of human web text that everything else gets bolted onto. Varun Singh, who leads pre-training at Arcee AI, argues that story is dead: no modern base model reflects the web the way GPT-3 once did. Instruction data and synthetic reasoning traces have moved earlier and earlier into training, and a distinct mid-training stage has emerged for longer datapoints that look much more like the downstream capabilities you actually want. Reading recent open recipes, from Nemotron to Kimi K2, the pattern is clear: raw web text is taking a backseat.

The rest of the talk is what that shift does to how you build. Once reinforcement learning became the thing that got models to reason, the base model stopped being a cherry on top and started needing to carry the prior that RL builds on, which changes the data mix and pulls post-training-flavored data forward. Singh walks through the practical pitfalls his team hit training the Trinity series, like getting the balancing coefficients right and establishing stable representations early so the model is prepared for what it must compose during RL. The message is that as capabilities advance, the base model's job keeps redefining itself, and pretending it still just mirrors the internet will cost you.

Speaker info:
- https://x.com/stochasticchasm
- https://www.linkedin.com/in/varun-singh-cs

Timestamps:
0:00 - The base model as a mirror of the web
1:26 - How knowledge accumulates in training
2:49 - When instruction data moves earlier
4:11 - After o1: RL and reasoning
5:41 - What prior the base model must carry
6:18 - Filtering web text, adding synthetic
8:01 - Reading the open data recipes
9:41 - Lessons from training Trinity
12:02 - Balancing coefficients and early stability
13:30 - Why RL keeps raising the stakes
15:55 - The base model's shifting job
