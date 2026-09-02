---
id: XtDEoN1DpvI
title: "Enable Generative AI Everywhere with Ubiquitous Hardware and Open Software - Guobing Chen, Intel"
slug: enable-generative-ai-everywhere-with-ubiquitous-hardware
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI.dev 2023"
year: 2023
speakers: ["Guobing Chen"]
channel: "The Linux Foundation"
duration_min: 17
published_at: 2023-12-18T18:31:36Z
video_id: XtDEoN1DpvI
url: https://www.youtube.com/watch?v=XtDEoN1DpvI
youtube_url: https://www.youtube.com/watch?v=XtDEoN1DpvI
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Enable Generative AI Everywhere with Ubiquitous Hardware and Open Software - Guobing Chen, Intel

**Guobing Chen**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI.dev 2023` · `2023` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=XtDEoN1DpvI) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Enable Generative AI Everywhere with Ubiquitous Hardware and Open Software - Guobing Chen, Intel

Generative AI like Large Language Models (LLM) usually require both massive memory and computation resource due to their incremental larger model size. However, by our comprehensive analysis, there are a set of optimization opportunities for most of the LLM models which can greatly reduce their inference latency, typically including low precision inference via bfloat16/INT8/INT4, Flash Attention and Efficient Attention in scaled dot product attention (SDPA), optimized KV cache access, Kernel Fusion such as RoPE, scale up/out model inference on multiple devices with Tensor Parallel, etc.

We implemented these optimizations within PyTorch and Intel Extension for PyTorch, and our experiment on a typical CPU server with two 4th generation of Intel Xeon Scalable Processors shows that we can achieve
