---
id: 5vfcTjosGLg
title: "PyTorch Symmetric Memory: A New Programming Paradigm for Distributed AI - Ke Wen & Chien-Chin Huang"
slug: pytorch-symmetric-memory-a-new-programming-paradigm-for
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 27
published_at: 2025-11-04T03:45:03Z
video_id: 5vfcTjosGLg
url: https://www.youtube.com/watch?v=5vfcTjosGLg
youtube_url: https://www.youtube.com/watch?v=5vfcTjosGLg
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# PyTorch Symmetric Memory: A New Programming Paradigm for Distributed AI - Ke Wen & Chien-Chin Huang

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=5vfcTjosGLg) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

PyTorch Symmetric Memory: A New Programming Paradigm for Distributed AI - Ke Wen & Chien-Chin Huang, Meta

Recent advancements in models led by DeepSeek have highlighted the need for customized communication. In response, PyTorch introduces Symmetric Memory, a new distributed programming model that creates a global address space for data spanning multiple GPUs' memory. This makes fine-grained GPU-initiated remote access possible.

In this talk, we will demonstrate how developers can author their own communication kernels at the device level. Additionally, we will show how to interleave communication and computation within the same kernel using popular languages like Triton, achieving the finest-grained fusion. Furthermore, we will discuss how these capabilities can integrate with the torch.compile ecosystem.

We will provide concrete examples based on the all-to-all-v used in MoE models, fused communication + layer norm, and masked-aware communication driven by FlexAttention.
