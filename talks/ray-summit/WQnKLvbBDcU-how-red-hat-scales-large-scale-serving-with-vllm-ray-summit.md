---
id: WQnKLvbBDcU
title: "How Red Hat Scales Large-Scale Serving with vLLM | Ray Summit 2025"
slug: how-red-hat-scales-large-scale-serving-with-vllm-ray-summit
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 37
published_at: 2025-11-19T21:00:10Z
video_id: WQnKLvbBDcU
url: https://www.youtube.com/watch?v=WQnKLvbBDcU
youtube_url: https://www.youtube.com/watch?v=WQnKLvbBDcU
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# How Red Hat Scales Large-Scale Serving with vLLM | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=WQnKLvbBDcU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Robert Shaw from Red Hat shares how vLLM is evolving to support p/d disaggregation and wide expert parallelism, two critical techniques for serving frontier-scale models like DeepSeek-R1 across large GPU clusters.

He begins by breaking down how prefill/decode (p/d) disaggregation enables more efficient resource utilization by separating the heavy, bursty prefill phase from the latency-sensitive decode phase—allowing clusters to scale each stage independently for maximum throughput and cost efficiency.

Robert then dives into the implementation of wide expert parallelism (EP) in vLLM, explaining how it allows MoE-based models to leverage large numbers of experts across multi-node environments. He details the orchestration, scheduling, and memory-management challenges of EP at cluster scale, and the design decisions that make these deployments practical.

Finally, he explores the tradeoffs and system-level considerations that arise when serving massive models such as DeepSeek-R1—including GPU topology, communication overhead, batching behavior, and cluster elasticity.

Attendees will gain a deep understanding of how vLLM implements next-generation parallelism strategies and what it takes to run cluster-scale MoE and non-MoE LLMs efficiently in real production environments.

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
