---
id: EoePOh9bTKs
title: "Enabling Lightweight, High-Performance FSDP With NVIDIA GPU - J. Chang CN, C. Ye, X. Chen & S. Lym"
slug: enabling-lightweight-high-performance-fsdp-with-nvidia-gpu
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Enabling Lightweight"]
channel: "PyTorch"
duration_min: 29
published_at: 2025-11-04T03:45:03Z
video_id: EoePOh9bTKs
url: https://www.youtube.com/watch?v=EoePOh9bTKs
youtube_url: https://www.youtube.com/watch?v=EoePOh9bTKs
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Enabling Lightweight, High-Performance FSDP With NVIDIA GPU - J. Chang CN, C. Ye, X. Chen & S. Lym

**Enabling Lightweight**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=EoePOh9bTKs) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Enabling Lightweight, High-Performance FSDP With NVIDIA GPU - Jianbin Chang CN, Cory Ye, Xuwen Chen & Sangkug Lym, NVIDIA

Fully sharded data parallel (FSDP) is quickly becoming the dominant distributed training technique for large models due to its impressive performance and ease of adoption. However, existing FSDP implementations often face communication and memory inefficiencies at scale. Here, we introduce Megatron-FSDP, which further enhances the performance of FSDP with native PyTorch compatibility. The key contributions of Megatron-FSDP include:

Add support for persistent communication buffers to enable user-buffer registration in low-resource collectives and mitigate memory fragmentation.
Leverage NVLink/InfiniBand-SHARP to offload collective operations from GPU SMs.
Provide native TransformerEngine FP8 support.
Enable scalable MoE support through tight Megatron-Core integration with expert parallelism.
Adheres to zero-copy principles, avoiding parameter/gradient copy overhead when sharding.

Our implementation is fully compatible with PyTorch APIs and deeply supports Megatron-Core and TransformerEngine. We share deployment tips—NVLink/IB SHARP offloading, operator fusions, FP8 workflows—demonstrating how Megatron-FSDP streamlines large-scale training.
