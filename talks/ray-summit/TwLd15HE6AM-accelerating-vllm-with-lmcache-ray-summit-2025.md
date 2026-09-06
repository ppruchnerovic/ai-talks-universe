---
id: TwLd15HE6AM
title: "Accelerating vLLM with LMCache | Ray Summit 2025"
slug: accelerating-vllm-with-lmcache-ray-summit-2025
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 35
published_at: 2025-11-19T21:01:57Z
video_id: TwLd15HE6AM
url: https://www.youtube.com/watch?v=TwLd15HE6AM
youtube_url: https://www.youtube.com/watch?v=TwLd15HE6AM
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Accelerating vLLM with LMCache | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `35 min`

[Watch the recording](https://www.youtube.com/watch?v=TwLd15HE6AM) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Kuntai Du from TensorMesh shares how LMCache expands the resource palette for serving large language models—making LLM inference faster and more cost-efficient by moving beyond GPU-only execution.

He begins by highlighting a key limitation in today’s serving stacks: KV-cache memory demands often exceed what GPUs alone can provide efficiently. LMCache addresses this by enabling KV-cache offloading to a wide range of datacenter resources—including CPU memory, local disk, and remote storage—and dynamically loading caches back to GPUs on demand. This unlocks new flexibility and dramatically reduces GPU memory pressure.

But LMCache goes far beyond simple prefix caching. Kuntai introduces KV-cache–related machine learning techniques that allow the inference engine to:

Reuse KV caches for non-prefix text

Share and reuse caches across different LLMs

Improve inference efficiency even for complex, non-sequential workloads

These innovations enable faster inference, lower cost, and improved hardware utilization without modifying model architectures.

Attendees will learn how LMCache opens new frontiers in LLM serving by leveraging broader datacenter resources and smart KV-cache reuse strategies—delivering scalable performance improvements even for the largest models.

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
