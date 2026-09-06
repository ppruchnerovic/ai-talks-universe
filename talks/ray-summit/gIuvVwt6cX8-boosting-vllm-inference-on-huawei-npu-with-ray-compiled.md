---
id: gIuvVwt6cX8
title: "Boosting vLLM Inference on Huawei NPU with Ray Compiled Graphs — Huawei | Ray Summit 2025"
slug: boosting-vllm-inference-on-huawei-npu-with-ray-compiled
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 11
published_at: 2025-12-01T20:38:13Z
video_id: gIuvVwt6cX8
url: https://www.youtube.com/watch?v=gIuvVwt6cX8
youtube_url: https://www.youtube.com/watch?v=gIuvVwt6cX8
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Boosting vLLM Inference on Huawei NPU with Ray Compiled Graphs — Huawei | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=gIuvVwt6cX8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Boyuan Chen, Zhilong Chen, and FengChun Hua from Huawei Canada share a major advancement in Ray Compiled Graph (CG): a new extension that accelerates vLLM inference on Huawei Ascend NPUs, achieving over 50% performance gains compared to existing NPU-based solutions.

They begin by explaining how this work serves as both a production-grade optimization and a proof-of-concept for SPMD-mode support in the upcoming vLLM V1 integration with Ray. Central to the design is a new NPU Store, inspired by Ray’s GPU Store, created to streamline tensor movement and improve cross-device efficiency in heterogeneous pipelines.

The speakers highlight several key contributions:

1. Multi-Accelerator Support Layer for Ray CG

A new, generic abstraction layer—compatible with GPU Store—enables NCCL-style, peer-to-peer tensor transfers across accelerators. This design dramatically simplifies the future integration of other hardware backends, including TPUs, NPUs, and emerging accelerators.

2. SPMD-Mode NPU Backend for vLLM in Ray CG

The team built a high-performance backend for Huawei Ascend NPUs that leverages:

Advanced operator fusion

Optimized memory scheduling

NPU-native execution paths

Together, these unlock substantial speedups for large-scale LLM inference.

3. Optimized Cross-Device Tensor Transfer

A prototype NPU Store maximizes throughput and minimizes latency when moving tensors across CPU ↔ NPU boundaries—crucial for hybrid inference and post-training pipelines.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
