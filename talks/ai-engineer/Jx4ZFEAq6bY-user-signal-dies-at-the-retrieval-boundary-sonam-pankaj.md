---
id: Jx4ZFEAq6bY
title: "User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch"
slug: user-signal-dies-at-the-retrieval-boundary-sonam-pankaj
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sonam Pankaj"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-06-28T17:00:20Z
video_id: Jx4ZFEAq6bY
youtube_url: https://www.youtube.com/watch?v=Jx4ZFEAq6bY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

**Sonam Pankaj**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Jx4ZFEAq6bY) · [Conference site](https://www.ai.engineer/)

## Description

Utility is all you need! Closing the Agent Learning Loop with Utility-Ranked Memory

Most production agent systems have a fatal flaw: they start every run from a blank slate. You have traces in your observability stack and pass/fail judgments in your eval suite, but the agent that runs tomorrow has no memory of why yesterday's runs succeeded or failed.

This talk exposes the gap between observation and action and shows how to close it.

We'll examine why current memory approaches stall: conversation buffers that only remember recency, semantic systems that retrieve what sounds similar rather than what helped, and reflection-based methods that capture lessons but don't learn which ones actually work. The core idea: utility-ranked memory. Treat memories like a credit score. When a memory is retrieved and the run passes, its utility rises. When the run fails, its utility falls. The ranking formula combines semantic similarity with outcome history.

There is also a demo with an example of the product SQL agent, of how it updates the context for the right outcome, everything happening at runtime.

Speakers:
- Sonam Pankaj (StarlightSearch Inc): Sonam is the CEO and Co-Founder of StarlightSearch. She is also the co-creator of embedanything, which is a Rust pipeline for RAG, which got contributions from Elastic, Milvus, and Qdrant, and has over 450k+ downloads. Prior to Starlight Search, Sonam spent years in developer tools and AI infrastructure, and has worked as a generative AI Evangelist, GTM lead at Articul8, a spin-off of Intel, and AI Researcher at Saama. She has been presenting talks for the last 10 years, and loves to interact with developers. She has been constantly speaking at Berlin Buzzwords, Europe's largest search conference, PyCon DE, and PyData. She also got an opportunity to present her work at Google, Deutsche Bank, and JetBrains.
X/Twitter: https://x.com/sonam_pankaj_
