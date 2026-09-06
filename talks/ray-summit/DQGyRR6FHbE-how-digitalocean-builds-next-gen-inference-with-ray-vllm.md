---
id: DQGyRR6FHbE
title: "How DigitalOcean Builds Next-Gen Inference with Ray, vLLM & More | Ray Summit 2025"
slug: how-digitalocean-builds-next-gen-inference-with-ray-vllm
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 17
published_at: 2025-12-01T19:56:49Z
video_id: DQGyRR6FHbE
url: https://www.youtube.com/watch?v=DQGyRR6FHbE
youtube_url: https://www.youtube.com/watch?v=DQGyRR6FHbE
tags: []
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra", "Prompting & context engineering"]
transcript: false
---

# How DigitalOcean Builds Next-Gen Inference with Ray, vLLM & More | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=DQGyRR6FHbE) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Yogesh Sharma, Boopathy Kannappan, and Debarshi Raha from DigitalOcean share how they built a robust, scalable inference platform for next-generation generative models—powered by Ray and vLLM, running on Kubernetes, and optimized for both serverless and dedicated GPU workloads.

They begin by outlining the rising complexity of inference as models grow in size, context length, and modality. Meeting real-world performance and reliability requirements demands a platform that can scale elastically, manage GPU resources intelligently, and handle dynamic workloads efficiently.

The speakers introduce DigitalOcean’s inference architecture, showing how:

Ray’s scheduling primitives ensure reliable execution across distributed clusters
Placement groups guarantee GPU affinity and predictable performance
Ray observability tools enable deep insight into system health and workload behavior
vLLM provides fast token streaming, optimized batching, and advanced memory/KV-cache management
Serverless and Dedicated Inference Modes

They explore two key operational modes:

Serverless inference for automatic scaling, burst handling, and cost efficiency
Dedicated inference for fine-grained GPU partitioning, custom quantization pipelines, and performance isolation

This dual-mode architecture allows DigitalOcean to serve diverse customer workloads while maintaining reliability and performance under varying traffic patterns.

Advanced Optimization for Long-Context Models

The team then discusses their ongoing initiatives to improve inference for models with contexts exceeding 8k tokens, including:

Dynamic batching by token length
KV cache reuse strategies
Speculative decoding to improve latency and throughput without sacrificing accuracy
Roadmap: Multimodal, Multi-Tenant, and Unified Orchestration
Finally, they present their roadmap for a fully multimodal, multi-tenant inference platform, featuring:

Concurrent model orchestration

Tenant isolation and security-aware billing

A vision for a centralized orchestration layer with Ray as the control plane

A unified model registry for intelligent model placement, prioritization, and lifecycle management

This talk is designed for AI infrastructure engineers building scalable inference systems—whether you're optimizing cutting-edge production stacks or just beginning to architect your own.

Attendees will leave with a clear understanding of how to build future-ready inference platforms capable of serving large, dynamic, multimodal generative models at scale.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
