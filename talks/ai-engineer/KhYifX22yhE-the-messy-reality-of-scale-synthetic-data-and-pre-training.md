---
id: KhYifX22yhE
title: "The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside"
slug: the-messy-reality-of-scale-synthetic-data-and-pre-training
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-07-26T01:00:06Z
video_id: KhYifX22yhE
youtube_url: https://www.youtube.com/watch?v=KhYifX22yhE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=KhYifX22yhE) · [Conference site](https://www.ai.engineer/)

## Description

Good code data runs out, so poolside manufactures more of it, and the hard part is making it teach. Their synthetic pipeline pairs templates with supplementary context and spreads generations across an axis of phrasing, with difficulty tuned so a task is neither trivial nor so hard the model learns nothing from it. Multistage pipelines port existing data into new shapes, swapping character styles or plots and turning single prompts into multi turn chats, while an orchestrator polices every generation and drops the ones that miss.

On the training side the team trusts nothing: run two replicas of the same model on the same data and they must return the same number, or the run gets killed. That is how the messy failures surface. Broken GPUs show up as a spiky loss curve, a numerical precision bug in tensor parallel accumulation quietly flattened another until they patched it, and silently corrupted gradients from a race condition were a blind spot nothing caught. The payoff is a 118 billion parameter model built for agentic coding whose early results already edge out GLM 4.5 Air, on a recipe that held as it scaled.

Speaker info:
Marah Abdin, poolside:
- https://x.com/marah_i_abdin
- https://www.linkedin.com/in/marah-abdin
- https://marahabdin.com

Robert McHardy, poolside:
- https://x.com/robert_mchardy
- https://www.linkedin.com/in/robert-mchardy
- https://www.robertmchardy.de

Timestamps:
0:00 - Introduction: synthetic data and pre-training at poolside
1:52 - Why synthetic data
3:11 - Limitations and the training budget
4:44 - Inside the synthetic data pipeline
6:37 - Multistage pipelines and porting data
7:43 - Multi turn chats and policing generations
9:03 - Pre-training: trust nothing, crash on mismatch
10:41 - Failures at scale: broken GPUs
11:56 - Numerical precision and corrupted gradients
13:15 - A 118B model for agentic coding
15:07 - Early results vs GLM 4.5 Air
