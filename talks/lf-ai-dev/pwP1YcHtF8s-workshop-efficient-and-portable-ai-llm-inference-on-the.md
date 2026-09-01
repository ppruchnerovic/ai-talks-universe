---
id: pwP1YcHtF8s
title: "Workshop: Efficient and Portable AI / LLM Inference on the Edge Cloud - Xiaowei Hu, Second State"
slug: workshop-efficient-and-portable-ai-llm-inference-on-the
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI_dev Europe 2024"
year: 2024
speakers: ["Xiaowei Hu"]
channel: "The Linux Foundation"
duration_min: 48
published_at: 2024-06-27T14:39:47Z
video_id: pwP1YcHtF8s
youtube_url: https://www.youtube.com/watch?v=pwP1YcHtF8s
tags: []
transcript: false
---

# Workshop: Efficient and Portable AI / LLM Inference on the Edge Cloud - Xiaowei Hu, Second State

**Xiaowei Hu**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI_dev Europe 2024` · `2024` · `48 min`

[Watch the recording](https://www.youtube.com/watch?v=pwP1YcHtF8s) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Workshop: Efficient and Portable AI / LLM Inference on the Edge Cloud - Xiaowei Hu, Second State

As AI applications gain popularity, we are increasingly seeing requirements to run AI or even LLM workloads on the edge cloud with heterogeneous hardware (eg GPU accelerators). However, the simplistic approaches are too heavyweight, too slow and not portable. For example, the PyTorch container image is 3GB and a container image for a C++ native toolchain is 300MB. Python apps also require complex dependency packages and could be very slow. Those container images are dependent on the underlying host’s CPU and GPU, making them difficult to manage. Wasm has emerged as a lightweight runtime for cloud native applications. For an AI app, the entire Wasm runtime and app can be under 20MB. The Wasm binary app runs at native speed, integrates with k8s and is portable across CPUs & GPUs. In this tutorial, we will demonstrate how to create and run Wasm-based AI applications on edge server or local host. We will showcase AI models and libraries for media processing (Mediapipe), vision (YOLO, amd Llava) and language (Llama2 series of models). You will be able to run all examples on your own laptop at the session.
