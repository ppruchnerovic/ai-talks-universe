---
id: dllQLs3lVpA
title: "From Cold Start To Warp Speed: Triton Kernel Caching With OCI Container Images - Maryam Tahhan"
slug: from-cold-start-to-warp-speed-triton-kernel-caching-with
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "AI_dev Europe 2025"
year: 2025
speakers: ["Maryam Tahhan"]
channel: "The Linux Foundation"
duration_min: 20
published_at: 2025-09-09T18:28:26Z
video_id: dllQLs3lVpA
url: https://www.youtube.com/watch?v=dllQLs3lVpA
youtube_url: https://www.youtube.com/watch?v=dllQLs3lVpA
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# From Cold Start To Warp Speed: Triton Kernel Caching With OCI Container Images - Maryam Tahhan

**Maryam Tahhan**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI_dev Europe 2025` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=dllQLs3lVpA) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

From Cold Start To Warp Speed: Triton Kernel Caching With OCI Container Images - Maryam Tahhan, Red Hat

Model startup latency is a persistent bottleneck for modern inference workloads, particularly when using custom kernels written in Triton that are Just In Time (JIT) compiled. In this talk, we’ll present a novel approach to speeding up model boot times by wrapping Triton kernel caches in OCI container images.
We’ll demo a working prototype that packages Triton-generated LLVM Kernels into reusable, portable container layers. These "hot start" containers can be deployed directly to Kubernetes, bypassing costly JIT compilation and significantly reducing model startup time.
Whether you're building ML infrastructure, working with OSS compilers, or deploying models at scale, this talk offers practical techniques to optimise cold starts for Models using Triton-lang.
