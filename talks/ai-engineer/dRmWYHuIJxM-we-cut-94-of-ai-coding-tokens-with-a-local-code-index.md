---
id: dRmWYHuIJxM
title: "We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco"
slug: we-cut-94-of-ai-coding-tokens-with-a-local-code-index
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rajkumar Sakthivel"]
channel: null
duration_min: 11
published_at: 2026-06-28T22:30:29Z
video_id: dRmWYHuIJxM
youtube_url: https://www.youtube.com/watch?v=dRmWYHuIJxM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

**Rajkumar Sakthivel**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=dRmWYHuIJxM) · [Conference site](https://www.ai.engineer/)

## Description

Every AI coding tool we tried had the same assumption: send as much context as possible.

In our production codebase, that meant sending 45,000 tokens per query — even when only ~5,000 were actually useful. We didn’t notice how inefficient this was until we saw the cost and latency impact.

We tried improving prompts and tweaking model settings, but nothing addressed the core problem:
we were optimising the model, not the context.

So we built a local retrieval layer between the codebase and the agent.

Instead of sending full files, we:

Structured code using AST-aware chunks (tree-sitter)
Combined vector search with keyword matching for better retrieval
Used a lightweight relationship layer to follow execution across files
The result: 👉 94% reduction in tokens
👉 faster responses
👉 more accurate outputs

The hardest problem wasn’t retrieval — it was knowing when retrieval was wrong.
We experimented with LLM-based scoring and threshold tuning, but a simple heuristic ended up working best.

Everything runs locally, with no data leaving the machine, and one index supports multiple AI tools.

In this talk, I’ll walk through:

What we got wrong initially
Why context matters more than model tuning
The architecture behind the system
Real benchmarks and trade-offs
The key takeaway: 👉 The biggest optimisation in AI coding isn’t the model — it’s the context.

Speakers:
- Rajkumar Sakthivel (Tesco): Rajkumar Sakthivel builds LLM infrastructure at scale and co-created Code Context Engine after his team's AI coding bill jumped from £15 to £200 in a single month.
X/Twitter: https://x.com/rajkumarsakthi
