---
id: J3zJ1MZtLN8
title: "Ray + vLLM Efficient Multi Node Orchestration for Sparse MoE Model Serving | Ray Summit 2025"
slug: ray-vllm-efficient-multi-node-orchestration-for-sparse-moe
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2025-11-18T23:31:17Z
video_id: J3zJ1MZtLN8
url: https://www.youtube.com/watch?v=J3zJ1MZtLN8
youtube_url: https://www.youtube.com/watch?v=J3zJ1MZtLN8
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Ray + vLLM Efficient Multi Node Orchestration for Sparse MoE Model Serving | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=J3zJ1MZtLN8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Slides: https://drive.google.com/file/d/11OSdPJLZ1v4QH2KHlEYGYCts5qEdR5gN/view?usp=sharing

At Ray Summit 2025, Kourosh Hakhamaneshi and Seiji Eicher from Anyscale share how Ray Serve and vLLM are enabling efficient, scalable serving of Mixture-of-Experts (MoE) models—despite the complex orchestration challenges these architectures introduce.

They begin by outlining why MoE models are so appealing: selective expert activation offers cost-effective scaling for large language models. But to realize these efficiency gains in production, serving systems must handle very large batch sizes, where KV-cache memory quickly becomes the bottleneck.

The speakers dive into how Multi-head Latent Attention (MLA) helps reduce KV-cache footprint through low-rank compression—yet creates new challenges when combined with high degrees of expert parallelism (EP). When tensor parallelism is introduced, KV-cache duplication becomes unavoidable, often making data-parallel attention the better choice for MoE inference.

Kourosh and Seiji also highlight how combining data parallelism with expert parallelism unlocks unique optimizations for the prefill vs. decode phases of inference, making prefill/decode disaggregation a powerful strategy for maximizing utilization across heterogeneous resources.

These interconnected tradeoffs require sophisticated multi-node orchestration, and this is where Ray Serve + vLLM shine. The speakers show how the two systems work together to balance flexibility, high throughput, and operational simplicity—enabling practical, production-grade MoE serving at scale.

Attendees will learn how to design and operate distributed MoE inference pipelines, optimize KV-cache usage, and leverage Ray Serve to coordinate complex parallelism strategies across large GPU clusters.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
