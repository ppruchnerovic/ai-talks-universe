---
id: ODhJFe4-n6Y
title: "Keynote: New Advances for Cross-platform AI Applications in Docker - Michael Yuan & Justin Cormack"
slug: keynote-new-advances-for-cross-platform-ai-applications-in
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI_dev Europe 2024"
year: 2024
speakers: []
channel: "The Linux Foundation"
duration_min: 12
published_at: 2024-06-27T14:39:45Z
video_id: ODhJFe4-n6Y
url: https://www.youtube.com/watch?v=ODhJFe4-n6Y
youtube_url: https://www.youtube.com/watch?v=ODhJFe4-n6Y
tags: []
transcript: false
---

# Keynote: New Advances for Cross-platform AI Applications in Docker - Michael Yuan & Justin Cormack

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI_dev Europe 2024` · `2024` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=ODhJFe4-n6Y) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Keynote: New Advances for Cross-platform AI Applications in Docker - Michael Yuan, Maintainer, CNCF WasmEdge and CEO, Second State & Justin Cormack, Chief Technology Officer, Docker, Inc

We will discuss new ways to support cross-platform GPU / AI workloads in container ecosystems, specifically with Docker’s support for the WebGPU standard. WebGPU allows container applications to access the host GPUs and other AI accelerators through a portable API. There is no more need to build Docker images for GPU vendors and their proprietary drivers. We will demonstrate how the WasmEdge project builds on the WebGPU standard to create portable LLM inference applications in Rust, and have those apps seamless managed and orchestrated by Docker.

Community impact:

A major advantage of open-source LLMs is to run them on each user’s private computers. Those include personal laptops, AI PCs, private or hybrid or edge cloud servers, edge devices, or even mobile devices. However, the heterogeneous hardware and software accelerators on those private computers or devices also pose great challenges for today’s AI developers. For example, today, an LLM app requires separate Docker images for all combinations of Nvidia CUDA, CUDNN, AMD ROCm, or Intel AVX etc. Each of those platform-dependent Docker images need to be developed, tested, and deployed separately.

WebGPU and Wasm provide an opportunity to abstract away and unify these underlying AI hardware and software stacks. With Docker support, they allow developers to create truly portable AI applications, and allow ops to manage those applications using their familiar Docker and Kubernetes tools.
