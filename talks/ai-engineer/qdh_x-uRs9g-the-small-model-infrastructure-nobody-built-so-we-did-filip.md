---
id: qdh_x-uRs9g
title: "The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked"
slug: the-small-model-infrastructure-nobody-built-so-we-did-filip
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Filip Makraduli"]
channel: null
duration_min: 18
published_at: 2026-05-05T17:00:06Z
video_id: qdh_x-uRs9g
youtube_url: https://www.youtube.com/watch?v=qdh_x-uRs9g
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked

**Filip Makraduli**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=qdh_x-uRs9g) · [Conference site](https://www.ai.engineer/)

## Description

Most embedding infrastructure assumes you know exactly which model you want ahead of time. This talk starts where that assumption breaks. Filip Makraduli walks through the real profiling mistakes, infrastructure gaps, and production constraints that led to building an embedding inference engine designed for dynamic model loading, hot-swapping, and memory-aware eviction instead of brittle one-model-per-container deployments.

If you're working on small-model inference, embeddings, or GPU infrastructure, this is a practical look at what breaks in the real world and how to design around it.

Speaker info:
- https://www.linkedin.com/in/filipmakraduli/

Timestamps:
0:00 Introduction and the gap in small model inference
0:53 Moving from research to building inference infrastructure
2:54 Introduction of the Superlinked inference engine
4:34 The importance of context management for agents
7:03 Misconceptions: Why more GPUs isn't the only answer
9:33 The "Yin and Yang" of inference: Model support and infrastructure
10:43 The challenge of supporting diverse model architectures
14:33 Deep dive into infrastructure and scalability
16:10 Conclusion and the open-source launch of SAI
