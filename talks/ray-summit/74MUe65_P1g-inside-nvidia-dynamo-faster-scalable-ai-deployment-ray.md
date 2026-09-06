---
id: 74MUe65_P1g
title: "Inside NVIDIA Dynamo: Faster, Scalable AI Deployment | Ray Summit 2025"
slug: inside-nvidia-dynamo-faster-scalable-ai-deployment-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 34
published_at: 2025-11-20T21:33:41Z
video_id: 74MUe65_P1g
url: https://www.youtube.com/watch?v=74MUe65_P1g
youtube_url: https://www.youtube.com/watch?v=74MUe65_P1g
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Inside NVIDIA Dynamo: Faster, Scalable AI Deployment | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=74MUe65_P1g) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Harry Kim from NVIDIA shares how NVIDIA Dynamo is redefining large-scale LLM inference through system-level optimizations that seamlessly integrate with high-performance engines such as vLLM, SGLang, and TensorRT-LLM (TRT-LLM).

He begins by outlining the core challenge: as LLMs grow in size, context length, and real-world usage, inference systems must deliver massive efficiency gains—not just from kernels or hardware, but across the entire distributed serving stack. NVIDIA Dynamo addresses this by introducing a new layer of intelligent orchestration and memory management designed specifically for LLM workloads.

Harry walks through Dynamo’s key innovations, including:

Smart Scheduling – Routes requests based on KV-cache hit rates and system load, intelligently autoscaling and disaggregating the prefill and decode phases for maximum throughput and efficiency.

Hierarchical Memory Management – Transparently leverages HBM, CPU memory, local NVMe, and remote storage to minimize latency and maximize effective model capacity.

Low-Latency KV-Cache Transfer – Quickly moves KV-cache across nodes and memory tiers, enabling fast context reuse and efficient distributed inference.

The session also introduces Dynamo’s production-grade LLM serving capabilities, including:

Tools to identify optimal disaggregated serving configurations offline

Automated tuning based on real-time traffic

Topology-aware gang scheduling to dynamically scale prefill and decode workers

LLM-specific fault-tolerance mechanisms for reliable serving at scale

Harry demonstrates how Dynamo enables organizations to achieve higher throughput, lower latency, and better cost efficiency across distributed LLM deployments—while still leveraging their preferred inference engine.

Attendees will leave with a clear understanding of how NVIDIA Dynamo transforms end-to-end LLM serving, making large-scale inference more efficient, robust, and operationally simple.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
