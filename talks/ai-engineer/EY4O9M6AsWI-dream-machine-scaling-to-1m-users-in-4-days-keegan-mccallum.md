---
id: EY4O9M6AsWI
title: "Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI"
slug: dream-machine-scaling-to-1m-users-in-4-days-keegan-mccallum
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2025-07-19T00:00:00Z
video_id: EY4O9M6AsWI
url: https://www.youtube.com/watch?v=EY4O9M6AsWI
youtube_url: https://www.youtube.com/watch?v=EY4O9M6AsWI
tags: []
transcript: false
---

# Dream Machine: Scaling to 1m users in 4 days — Keegan McCallum, Luma AI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2025` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=EY4O9M6AsWI) · [Conference site](https://www.ai.engineer/)

## Description

Talking about Luma AI, our mission, and how our ML infrastructure enables SOTA multimodal model development

About Keegan McCallum
I'm Keegan McCallum, the Head of ML infrastructure at Luma AI. I began my career in research focusing on portfolio optimization. Since then I've founded two startups, lead engineering at two others and have landed at Luma AI working on an unconventional multimodal path to AGI among a cracked team of researchers and engineers. When I'm not working, I'm usually out in the woods hiking with my family, or exploring the culinary delights in whatever city I happen to be in. I'm excited to share the insights and war stories I've gathered launching one of the most successful AI products to date in a (hopefully) fun and engaging way

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps
The initial launch challenges [00:00]: Luma AI was unprepared for the high traffic, quickly exhausting their initial GPU allocation and facing a large queue of requests.

Rapid scaling efforts [00:57]: They rapidly scaled their GPU capacity from 500 to 5,000 H100 GPUs within six hours, and later added another 4,000 H100 GPUs from their training cluster to keep up with demand.

Luma AI's mission [03:10]: Beyond just video models, Luma AI aims to build general multimodal intelligence that can generate, understand, and operate in the physical world.

Their product capabilities [03:22]: They demonstrate a "modify video" feature where users can upload iPhone videos and transform them with text prompts. They also highlight their public API for integrating this functionality into applications [03:52].

Infrastructure re-architecture [06:02]: They moved from a brittle, tightly coupled container setup using Triton inference server to a custom-built serving stack on vanilla PyTorch, which offers better support for multiple GPUs, nodes, and different chipsets.

Challenges and solutions in scaling [07:39]:

Back pressure [07:51]: They implemented a dispatch limitation system to prevent too many CPU workers from queuing jobs in one cluster.

Fair scheduling and work starvation [08:36]: To address issues with different user tiers (API, enterprise, unlimited, light, free) and prevent lower-priority jobs from being starved, they developed an SLO (Service Level Objective) based system that prioritizes jobs based on the percentage of their worst-case waiting time [11:14].

Handling different models and bursts [08:43]: They built a system to automatically scale up compute on their training cluster to handle demand bursts [09:16].

Model management [13:24]: They use a model repository system where each model has immutable versions stored in object storage, including the full Python environment and checkpoints. This allows for reproducible rollbacks and seamless, on-the-fly version switching for workers [14:46].

Hiring [15:13]: Luma AI is actively hiring engineers, researchers, and AI enthusiasts
