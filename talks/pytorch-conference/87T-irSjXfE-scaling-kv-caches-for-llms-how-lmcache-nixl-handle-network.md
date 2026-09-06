---
id: 87T-irSjXfE
title: "Scaling KV Caches for LLMs: How LMCache + NIXL Handle Network and Storage...- J. Jiang & M. Khazraee"
slug: scaling-kv-caches-for-llms-how-lmcache-nixl-handle-network
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 33
published_at: 2025-11-04T03:43:36Z
video_id: 87T-irSjXfE
url: https://www.youtube.com/watch?v=87T-irSjXfE
youtube_url: https://www.youtube.com/watch?v=87T-irSjXfE
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Scaling KV Caches for LLMs: How LMCache + NIXL Handle Network and Storage...- J. Jiang & M. Khazraee

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=87T-irSjXfE) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Scaling KV Caches for LLMs: How LMCache + NIXL Handle Network and Storage Heterogeneity - Junchen Jiang, University of Chicago & Moein Khazraee, NVIDIA

Efficient KV cache management is critical for scalable, low-latency LLM inference. LMCache, a widely adopted open-source KV caching layer used in vLLM deployments, addresses two fundamental challenges: (1) transferring KV caches across LLM instances, and (2) storing KV caches into diverse backend systems. However, in real-world deployments, both operations must navigate hardware heterogeneity—from network fabrics like NVLink, RDMA, and TCP/IP, to storage layers like Infinistore, Redis, and Mooncake. That’s where NVIDIA’s NIXL library comes in. NIXL abstracts and optimizes data movement across heterogeneous infrastructures, making it easier for systems like LMCache to deliver high throughput and low latency.

In this talk, we’ll dive into how LMCache integrates with NIXL to accelerate KV cache transfers and storage. Expect real deployment demos, performance benchmarks, and practical guidance for running next-gen LLM inference on Kubernetes with minimal GPU waste.
