---
id: QJEFQlbShf8
title: "Fixing S3 Bottlenecks: Scalable I/O for Ray with Alluxio | Ray Summit 2025"
slug: fixing-s3-bottlenecks-scalable-i-o-for-ray-with-alluxio-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 10
published_at: 2025-12-01T20:31:58Z
video_id: QJEFQlbShf8
url: https://www.youtube.com/watch?v=QJEFQlbShf8
youtube_url: https://www.youtube.com/watch?v=QJEFQlbShf8
tags: []
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Fixing S3 Bottlenecks: Scalable I/O for Ray with Alluxio | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=QJEFQlbShf8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Bin Fan from Alluxio shares how a fast-moving AI startup transformed a fragile, high-throughput training pipeline into a production-grade data infrastructure—using Ray and Alluxio to accelerate model iteration for advanced document understanding and search systems.

He begins by highlighting the core challenge: rapid experimentation is crucial for startups, yet large-scale preprocessing and training pipelines often collapse under heavy I/O pressure. The team evaluated three architectural designs for integrating Ray with storage systems—each addressing different bottlenecks and scaling constraints.

1. Direct Ray → S3 Access (Initial Architecture)

The pipeline originally relied on Ray preprocessing workers writing directly to S3 while PyTorch handled training reads. Under real-world concurrency—1,000+ Ray workers writing simultaneously—the system suffered from:

Severe throughput degradation

High S3 egress and PUT/GET costs

Training slowdowns from inconsistent read performance

This setup proved unsustainable for fast model iteration.

2. Alluxio with Async Write-Back (Intermediate Architecture)

Adding Alluxio as an asynchronous write buffer improved read performance during training, but new bottlenecks surfaced:

Metadata saturation during peak concurrency

Instability in the write path

Frequent cluster crashes and job restarts

Throughput improved, but reliability did not.

3. Decentralized Alluxio 3.x with Cache-Through Writes (Final Architecture)

A fully decentralized Alluxio 3.x deployment with cache-through writes unlocked the performance and stability required:

Consistent ingestion under 400 Gbps internal bandwidth

Throttled 10 Gbps outbound writes to S3 for cost control

Zero restarts—even under bursty load

Significantly improved GPU utilization and end-to-end iteration speed

This architecture enabled fast, stable, scalable model development without expensive storage overhauls.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
