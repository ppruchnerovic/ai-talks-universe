---
id: -tviRdpmHvs
title: "Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai"
slug: training-krea-2-what-matters-in-generative-model-training
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sangwu Lee"]
channel: null
duration_min: 22
published_at: 2026-08-18T14:00:06Z
video_id: -tviRdpmHvs
youtube_url: https://www.youtube.com/watch?v=-tviRdpmHvs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai

**Sangwu Lee**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-tviRdpmHvs) · [Conference site](https://www.ai.engineer/)

## Description

The most reliable way to render a person is to render the most boring average person and put them in the center of the frame. Sangwu Lee offers that as the price the big image models pay for consistency: ask a production model for a burning skull and every output comes back clean, competent, and nearly identical. Krea 2, whose medium variant is now open source, trades the other way, optimizing for fast generation and stylistic range so that a studio that does not yet know what it wants can actually explore.

Most of the talk is about data, which he says twice over is basically everything once the architecture is locked. The examples are specific. A painting photographed on a wall is perfectly good training data except that captioners consistently omit the frame and the white wall behind it, so the model learns to hang every painting it generates. They refuse to train on AI generated images at all, because the aesthetic is sticky and you inherit somebody else's model. Deduplication runs on hashes first across two to ten billion images, then on embeddings for near duplicates. A large vision language model's judgment gets distilled down into a classifier cheap enough to sweep a billion images. Sparse autoencoders double as an unsupervised tagging system for catching watermarks and border artifacts. World knowledge coverage is checked against Wikipedia concepts ranked by PageRank. Thirty to forty in house filters in total.

Speaker info:
- https://github.com/RE-N-Y
- https://re-n-y.github.io/devlog/
- https://github.com/krea-ai/krea-2

Timestamps:
0:00 - Open sourcing Krea 2 medium
1:40 - Consistency versus diversity in production models
3:23 - How diffusion models train, and why latent space
5:59 - Data is basically everything
6:53 - Bad data, and why they refuse AI images
8:34 - The captioning pipeline, and the painting on a white wall
10:15 - Deduplication and cheap classifiers at billion image scale
11:56 - Sparse autoencoders as an unsupervised tagging system
13:39 - Wikipedia PageRank for world knowledge coverage
14:35 - The training pipeline, borrowed wholesale from LLMs
18:54 - What actually mattered for iterating fast
19:46 - The stack is inverting back toward DALL-E 2
