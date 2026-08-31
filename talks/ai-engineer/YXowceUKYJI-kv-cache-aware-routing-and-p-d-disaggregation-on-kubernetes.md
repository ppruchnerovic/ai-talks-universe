---
id: YXowceUKYJI
title: "KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat"
slug: kv-cache-aware-routing-and-p-d-disaggregation-on-kubernetes
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 22
published_at: 2026-08-27T14:00:06Z
video_id: YXowceUKYJI
youtube_url: https://www.youtube.com/watch?v=YXowceUKYJI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YXowceUKYJI) · [Conference site](https://www.ai.engineer/)

## Description

Agentic sessions in Red Hat's traces run from a few turns to 3,000, cache hit rates routinely clear 90%, and input to output token ratios often pass 100 to 1. A public inference benchmark shows none of that, because it reports steady state numbers from one sanitized run. Yuchen Fama and Ashish Kamra spend the talk on the two levers that matter once the client rather than the server controls the cache lifecycle, and a live demo makes the first one concrete. An opening request takes about 3 seconds, the next turn reuses the cache on the same pod and takes about 1, and a fresh system prompt lands on a different pod and pays the full 3 again. With a 10x gap between cached and uncached token costs, routing is the cheaper lever to reach for before adding GPUs.

The second lever splits compute bound prefill from memory bound decode, so a long incoming prompt cannot stall token generation midstream. Across 16 H100s serving gpt-oss, P99 inter token latency falls from roughly 900 milliseconds to about 100, and the curve gets visibly smoother. The useful part is where they draw the boundary. Disaggregation wins in the middle concurrency band, roughly ties at both ends, and needs an RDMA or RoCE fabric to move cache between workers at all. Without one, stay aggregated. The closing case study runs GLM 5.2 on the H200s customers actually have instead of B200s, at three prefill workers to one decode, for 4x faster time to first token and 60% more requests.

Speaker info:
- https://www.linkedin.com/in/yuchen-fama
- https://www.linkedin.com/in/ashishkamra/
- https://github.com/llm-d/llm-d

Timestamps:
0:00 - What public inference benchmarks leave out
1:28 - Red Hat's inference stack, and the agenda
3:29 - Agentic traces: 3,000 turns, 90% cache hits, 100 to 1 ratios
5:12 - Volatile cache, and the 10x cached token gap
6:28 - How llm-d routes: endpoint picker, offload tiers, eviction
7:46 - Demo: cache hits, pod affinity, 3 seconds versus 1
9:28 - What llm-d is, and why prefill and decode interfere
12:03 - How disaggregation works in practice
13:08 - P99 inter token latency: 900ms versus 100ms
14:14 - Where PD shines across the concurrency curve
15:45 - When to use PD, and when to stay aggregated
18:10 - GLM 5.2 on H200s: 4x faster TTFT
