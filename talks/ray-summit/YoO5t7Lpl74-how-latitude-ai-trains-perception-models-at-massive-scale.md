---
id: YoO5t7Lpl74
title: "How Latitude AI Trains Perception Models at Massive Scale | Ray Summit 2025"
slug: how-latitude-ai-trains-perception-models-at-massive-scale
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 32
published_at: 2025-11-18T17:29:36Z
video_id: YoO5t7Lpl74
url: https://www.youtube.com/watch?v=YoO5t7Lpl74
youtube_url: https://www.youtube.com/watch?v=YoO5t7Lpl74
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# How Latitude AI Trains Perception Models at Massive Scale | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=YoO5t7Lpl74) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Richard Kwant, Marius Seritan, and Krishna Toshniwa from Latitude AI share how Ray powers their dataset generation, inference workloads, and complex training pipelines for multimodal perception models.

They begin by walking through how Ray’s distributed computing model supports the entire ML lifecycle at Latitude, with a deep focus on their most demanding component: the training pipeline. Their models rely on images, point clouds, rich metadata, and multi-task targets—requiring extremely fast, parallel data loading to keep GPUs fully saturated.

Starting from a traditional PyTorch DataLoader, the team encountered concurrency limits and throughput constraints. Migrating to Ray Data unlocked new levels of parallelism, but also surfaced fresh challenges around data loading, memory management, serialization, and prefetching. The speakers detail the optimizations and distributed patterns that enabled them to overcome these bottlenecks and achieve over a 3× increase in training throughput.

They also discuss hurdles such as implementing scalable sampling techniques and improving observability across the Ray Data pipeline.

Attendees will gain practical insights into designing high-performance multimodal training pipelines, debugging distributed data systems, and leveraging Ray to accelerate complex perception workloads end-to-end.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
