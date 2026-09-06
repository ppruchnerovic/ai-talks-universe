---
id: FwGEM3ZdZLI
title: "How Daft Boosts Batch Inference Throughput with Dynamic Partitioning | Ray Summit 2025"
slug: how-daft-boosts-batch-inference-throughput-with-dynamic
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 34
published_at: 2025-11-18T23:37:35Z
video_id: FwGEM3ZdZLI
url: https://www.youtube.com/watch?v=FwGEM3ZdZLI
youtube_url: https://www.youtube.com/watch?v=FwGEM3ZdZLI
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# How Daft Boosts Batch Inference Throughput with Dynamic Partitioning | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=FwGEM3ZdZLI) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Kevin Wang from Eventual shares how Daft enables petabyte-scale multimodal query processing on Ray—unlocking high-performance batch inference as part of complex, end-to-end pipelines.

He begins by outlining a fundamental challenge in large-scale LLM inference: maximizing prefix caching without stalling GPUs. Traditional methods rely on a full upfront sort and partition of prompts to boost cache locality—but this preprocessing step leaves GPUs idle and limits overall throughput.

Daft solves this with a breakthrough technique called dynamic prefix partitioning. Instead of static pre-sorting, Daft continuously and automatically adjusts partitions in-flight as data streams into vLLM. This approach ensures:

High prefix cache hit rates without manual preprocessing

Full GPU saturation throughout the entire query

End-to-end performance gains across multimodal batch workloads

Kevin walks through how Daft integrates vLLM’s high-performance inference engine into its distributed execution model, powered by Ray. The session explores the inner workings of the Daft query optimizer and execution engine, along with performance benchmarks on real multimodal pipelines.

Attendees will learn how Daft’s architecture can transform large-scale batch inference—making multimodal data processing faster, more efficient, and dramatically easier to operate.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
