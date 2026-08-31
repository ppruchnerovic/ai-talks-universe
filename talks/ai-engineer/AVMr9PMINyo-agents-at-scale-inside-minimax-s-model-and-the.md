---
id: AVMr9PMINyo
title: "Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song"
slug: agents-at-scale-inside-minimax-s-model-and-the
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 20
published_at: 2026-07-31T00:00:00Z
video_id: AVMr9PMINyo
youtube_url: https://www.youtube.com/watch?v=AVMr9PMINyo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=AVMr9PMINyo) · [Conference site](https://www.ai.engineer/)

## Description

In this conversation, Olive Song, who leads reinforcement learning at MiniMax, opens up the stack behind the company's open weight models and the infrastructure that serves them. Her starting point is a belief in open source: put the weights out, let builders optimize on them, and share the capability widely. From there she walks through what it takes for a model to land well, from agentic coding that also understands and builds games, to computer use problems trained with RL against environments like OS World.

Much of the discussion is the unglamorous engineering that makes a launch real. When a model ships, the team wants the inference stack ready on day zero, which means writing and tuning GPU kernels, working through benchmarks like a parallel kernel bench, and threading optimization into everything from KV cache handling to routing. Song also talks through multimodality and the training pitfalls that come with it, such as text and vision collapsing after training unless you train both modalities together, and reflects on longer horizon tasks like replicating a twelve hour run. She closes optimistic that open models are closing the gap faster than a year ago would have suggested.

Speaker info:
- https://x.com/olive_jy_song

Timestamps:
0:00 - Introducing the RL lead at MiniMax
1:17 - Why open source and open weights
3:45 - What builders are doing with the model
4:11 - A model that builds games
5:12 - Computer use and OS World
5:49 - Writing GPU kernels
6:25 - Parallel kernel bench
7:28 - A day zero inference stack
9:34 - Optimization across the stack
10:47 - Multimodality and training collapse
14:10 - Replicating a twelve hour run
17:22 - Where open models go next
