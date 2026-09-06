---
id: pjJBkaKcfuU
title: "Distributed Embeddings at Scale: Processing 10M+ Rows/ Day with Ray, GPUs & Qdrant | Ray Summit 2025"
slug: distributed-embeddings-at-scale-processing-10m-rows-day
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 13
published_at: 2025-12-01T20:45:45Z
video_id: pjJBkaKcfuU
url: https://www.youtube.com/watch?v=pjJBkaKcfuU
youtube_url: https://www.youtube.com/watch?v=pjJBkaKcfuU
tags: []
topics: ["Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: false
---

# Distributed Embeddings at Scale: Processing 10M+ Rows/ Day with Ray, GPUs & Qdrant | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=pjJBkaKcfuU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Justin Miller from ZEFR shares how his team built a production-grade, multi-platform NLP pipeline using Ray and GPU acceleration to process millions of social media posts across TikTok, YouTube, and Instagram.

He begins by describing the challenges of handling massive, fast-changing content streams across multiple platforms—each with unique data formats, ingestion patterns, and quality constraints. To meet these demands, ZEFR engineered a robust distributed pipeline that uses Ray to orchestrate scalable embedding generation, GPU-heavy processing, and high-throughput vector search ingestion.

Justin walks through the architecture step-by-step:

Snowflake → Ray ingestion: Retrieve rows for each platform with consistent batch scheduling

Cleaning, chunking, and preprocessing: Normalize and prepare multimodal content at scale

Distributed embedding generation: Use Ray Actors to shard GPU inference tasks across the cluster

High-throughput writes: Send results to Google Cloud Storage (GCS), Qdrant for vector search, and back to Snowflake for analytics and pipeline tracking

Shard lifecycle management: Delete stale shards, manage multi-platform ingestion, and maintain healthy storage footprints

He also shares practical, real-world guidance for operating Ray in production—covering deployment patterns, debugging tips, failure recovery, throughput tuning, and cost management.

Whether you’re processing large multi-source datasets, running GPU-heavy inference pipelines, or building modern vector-search–backed systems, this talk provides both code-level insights and actionable advice for running Ray at scale.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
