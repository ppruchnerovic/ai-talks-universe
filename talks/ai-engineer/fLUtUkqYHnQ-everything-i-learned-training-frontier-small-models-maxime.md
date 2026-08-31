---
id: fLUtUkqYHnQ
title: "Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI"
slug: everything-i-learned-training-frontier-small-models-maxime
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Maxime Labonne"]
channel: null
duration_min: 20
published_at: 2026-04-29T00:00:00Z
video_id: fLUtUkqYHnQ
youtube_url: https://www.youtube.com/watch?v=fLUtUkqYHnQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI

**Maxime Labonne**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=fLUtUkqYHnQ) · [Conference site](https://www.ai.engineer/)

## Description

A new class of small models is emerging with the ability to reliably follow instructions and call tools while running on-device under 1 GB of memory. In this talk, we'll break down how to post-train frontier small models using the LFM2.5 recipe: on-policy preference alignment, agentic reinforcement learning, and curriculum training with iterative model merging. We'll cover training challenges unique to the 1B scale, like doom loops, capability interference, and how to fix them. The goal is to give you a concrete playbook to fine-tune and deploy small models for your own use cases, from structured data extraction to multi-turn tool use.

Speaker info:
- https://x.com/maximelabonne
- https://www.linkedin.com/in/maxime-labonne/
- https://github.com/mlabonne

Timestamps:
0:00:00 - Start
0:00:14 - Introduction to frontier small models at Liquid AI
0:01:02 - Characteristics: memory-bound, task-specific, latency-sensitive
0:02:20 - Architecture: why large embedding layers are inefficient
0:04:01 - LFM2 architecture: using gated short convolutions for speed
0:06:09 - LFM 2.5 recipe: 28T tokens and post-training stages
0:08:34 - Post-training: SFT, preference alignment, and RL best practices
0:10:43 - Identifying "doom loops" in reasoning models
0:11:34 - Solutions: mitigating loops via preference alignment and RL
0:15:29 - Future focus: using agentic tools to overcome memory limits
0:17:58 - Q&A: real-world applications for small vs. large models
