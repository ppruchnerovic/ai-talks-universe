---
id: KJTbr72fsJ8
title: "Yuri Shelke: Scaling Enterprise RAG: Distributed Indexing and Dynamic Retrieval at Terabyte Scale"
slug: yuri-shelke-scaling-enterprise-rag-distributed-indexing-and
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 25
published_at: 2026-10-07T23:11:20Z
video_id: KJTbr72fsJ8
url: https://www.youtube.com/watch?v=KJTbr72fsJ8
youtube_url: https://www.youtube.com/watch?v=KJTbr72fsJ8
tags: []
topics: ["Data engineering & MLOps", "Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: false
---

# Yuri Shelke: Scaling Enterprise RAG: Distributed Indexing and Dynamic Retrieval at Terabyte Scale

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=KJTbr72fsJ8) · [Conference site](https://aiconference.com/)

## Description

Standard vector search architectures collapse under the weight of indexing latency, ballooning storage costs, and degraded retrieval precision when enterprise RAG systems scale to terabyte-scale production knowledge bases, hitting a Scaling Wall. This session explores the engineering patterns required to build a high-throughput enterprise search infrastructure. Using our production implementation as a case study, we graduate from basic vector stores to a distributed indexing strategy. We will analyze the critical trade-offs between Approximate Nearest Neighbor (ANN) accuracy and memory overhead, the impact of hybrid metadata-vector filtering on query latency, and the necessity of partitioned retrieval architectures to maintain sub-second response times. Attendees will gain a blueprint for a "Knowledge Lake" architecture, learning how to handle incremental indexing at scale, manage vector infrastructure costs, and implement dynamic query routing to ensure system consistency across distributed environments. Key Takeaways: * Distributed Indexing & Sharding: Partition billion-vector datasets across distributed nodes using HNSW/IVF algorithms to ensure sub-second retrieval without exhausting cluster memory. * Trade-off - ANN accuracy vs Memory: Tune ANN indexes for billions of vectors, balancing retrieval speed against infrastructure spend with tiered storage. * Partitioned Retrieval & IVF Strategies: Engineering strategies for segmenting vector space using Inverted File Indexing (IVF), centroid-based sharding, and cluster-level pruning to achieve high search completeness with minimal compute overhead. * Hybrid Filtering & Routing: Implementation patterns for combining structured metadata filters with vector similarity to optimize retrieval performance. * Operational Consistency: Monitoring ingestion lag, managing incremental indexing, and ensuring data integrity across distributed vectors. Engineering Trade-offs & Operational Insights: * Ingestion Scaling vs. Index Freshness: Dynamic task mapping in Airflow and Spark to parallelize the embedding bottleneck while managing vector database write-limits. * Vector Storage Economics: Reducing high-dimensionality embeddings cost through product quantization (PQ) and binary hashing. * System Resiliency: Handling retrieval hot spots and implementing circuit breakers for bulk data backfills that threaten to saturate vector endpoints.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved
