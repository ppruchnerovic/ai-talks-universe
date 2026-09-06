---
id: bc7x6cmMB8Q
title: "Lightning Talk: Improved GEMM and SDPA Performance on ROCm With Composable Kernel - Andres Lugo, AMD"
slug: lightning-talk-improved-gemm-and-sdpa-performance-on-rocm
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Andres Lugo"]
channel: "PyTorch"
duration_min: 10
published_at: 2025-11-04T03:45:05Z
video_id: bc7x6cmMB8Q
url: https://www.youtube.com/watch?v=bc7x6cmMB8Q
youtube_url: https://www.youtube.com/watch?v=bc7x6cmMB8Q
tags: []
topics: []
transcript: false
---

# Lightning Talk: Improved GEMM and SDPA Performance on ROCm With Composable Kernel - Andres Lugo, AMD

**Andres Lugo**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=bc7x6cmMB8Q) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: Improved GEMM and SDPA Performance on ROCm With Composable Kernel - Andres Lugo, AMD

As the artificial intelligence space continues to grow and evolve with increasingly complex use cases, the need for customized kernels to maximize performance grows alongside it. Two of the more popular operations within machine learning, GEMMs and Scaled-Dot-Product Attention represent key areas of improvement across key compute kernels for most LLMs. GEMMs are present in almost all models as one of the most fundamental operations, and SDPA is the backbone of modern Transformer architectures which are currently spearheading the field of Generative AI. We now introduce Composable Kernel (CK) as an backend library for both GEMMs and SDPA. CK is a library that provides a programming model for writing performance critical kernels for ML workloads. It uses a tile-based programming model to adhere to the underlying hardware architecture efficiently. We have integrated CK for both GEMMs and SDPA exhibiting good performance requiring only a single line of Python code to enable per operator. In this lightning talk, we present our findings using the new CK backend for both GEMMs and SDPA, briefly discuss the integration points of the library, as well as usage basics for enablement.
