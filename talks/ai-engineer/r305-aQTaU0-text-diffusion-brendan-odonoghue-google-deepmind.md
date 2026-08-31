---
id: r305-aQTaU0
title: "Text Diffusion — Brendan O’Donoghue, Google DeepMind"
slug: text-diffusion-brendan-odonoghue-google-deepmind
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Text Diffusion"]
channel: null
duration_min: 28
published_at: 2026-06-04T18:00:06Z
video_id: r305-aQTaU0
youtube_url: https://www.youtube.com/watch?v=r305-aQTaU0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Text Diffusion — Brendan O’Donoghue, Google DeepMind

**Text Diffusion**

`AI Engineer` · `AI Engineer` · `2026` · `28 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=r305-aQTaU0) · [Conference site](https://www.ai.engineer/)

## Description

GPT-4o answered 40. Gemini 2.5 Flash answered 42 and stuck to it even after working through the reasoning incorrectly. The Gemini Diffusion model, considerably smaller than both, answered 60 on the first forward pass, then 49, then corrected itself to 39 once it finished reasoning. Bidirectional attention means it can see future tokens and go back to fix mistakes. Autoregressive models cannot do that.

Brendon O'Donoghue covers why text diffusion is fast (24 denoising steps to generate 256 tokens means roughly 10x fewer memory transfers than autoregressive generation), what the tradeoff is (lower throughput at large batch sizes makes it expensive to serve at scale today), and what gets unlocked when latency drops to 2,000 tokens per second. The demos include a fake Wikipedia generated on the fly, a Reddit clone with AI generated comments and images, an operating system where every click generates the next screen, and a todo app built in 15 seconds by voice.

Speaker info:
- https://x.com/bodonoghue85
- https://bodono.github.io/
- https://www.linkedin.com/in/bodono/

Timestamps:
0:00 Introduction to Text Diffusion
1:02 How Text Diffusion Works (Training and Inference)
2:06 Gemini Diffusion Research Preview
3:04 Difference Between Autoregressive and Diffusion Models
4:02 Pros and Cons of Text Diffusion
6:13 Hardware Efficiency: Why Text Diffusion is Faster
8:47 Bidirectional Reasoning and Self-Correction
12:00 Dynamic and Adaptive Computation
14:26 In-place Text Editing
16:09 Low Latency Applications and Demos
20:05 Q&A Session
