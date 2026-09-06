---
id: 2TyulEkOMyU
title: "Scaling Inference of O(10K)-length Sequence Recommendation Models Using... - S. Joshi & K. Rajesh"
slug: scaling-inference-of-o-10k-length-sequence-recommendation
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["S. Joshi", "K. Rajesh"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:43:36Z
video_id: 2TyulEkOMyU
url: https://www.youtube.com/watch?v=2TyulEkOMyU
youtube_url: https://www.youtube.com/watch?v=2TyulEkOMyU
tags: []
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "Prompting & context engineering"]
transcript: false
---

# Scaling Inference of O(10K)-length Sequence Recommendation Models Using... - S. Joshi & K. Rajesh

**S. Joshi, K. Rajesh**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=2TyulEkOMyU) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Scaling Inference of O(10K)-length Sequence Recommendation Models Using CudaGraph and Triton Kernels - Saurabh Joshi & Kousik Rajesh, Pinterest

In this talk we discuss how we scaled Pinterest’s RecSys models from a context length of 500 to 16000 for a 10M+ QPS system while maintaining latency and throughput.

We start with how we optimized goodput, using Torchscript on a custom CudaGraph backend and OpenAI triton kernels to fuse expensive model operations in PyTorch. Then, deep dive into our Single Kernel Unified Transformer, which leverages GPU L2 Cache to store all transformer weights and a single fused kernel. This approach achieves 85% latency and 13% memory reduction over flash attention for small transformer sizes.

We’ll also cover details of our serving system optimizations for long context lengths such as request level deduping and pinned memory arena. Using a custom sparse tensor format specialized for ranking models, we minimize CPU preprocessing and memory copy overheads. This led to a payload size reduction of 16x, saving CPU and PCIe copy bandwidth and lowering latency.

Together, these optimizations reduced E2E latency by 250x and GPU serving costs by 98% over initial estimates. The project has driven substantial improvements to our recommendation quality and powers key product surfaces.
