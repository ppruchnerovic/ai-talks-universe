---
id: Zd4oPBMSFhE
title: "Efficient and Cross-Platform LLM Inference in the Heterogenous Cloud - Michael Yuan, Second State"
slug: efficient-and-cross-platform-llm-inference-in-the
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI_dev Europe 2024"
year: 2024
speakers: ["Michael Yuan"]
channel: "The Linux Foundation"
duration_min: 33
published_at: 2024-06-27T14:39:45Z
video_id: Zd4oPBMSFhE
url: https://www.youtube.com/watch?v=Zd4oPBMSFhE
youtube_url: https://www.youtube.com/watch?v=Zd4oPBMSFhE
tags: []
transcript: false
---

# Efficient and Cross-Platform LLM Inference in the Heterogenous Cloud - Michael Yuan, Second State

**Michael Yuan**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI_dev Europe 2024` · `2024` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=Zd4oPBMSFhE) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Efficient and Cross-Platform LLM Inference in the Heterogenous Cloud - Michael Yuan, Second State

As AI/LLM applications gain popularity, there are increasing demands to run and scale them in the cloud. However, compared with traditional cloud workloads, AI workloads are heavily reliant on the GPU. Linux containers are not portable across different hardware devices, and traditional container management tools are not setup to re-compile applications on new devices at deployment time. Cloud native Wasm provides a new portable bytecode format that abstracts away GPUs and hardware accelerators for these applications. With emerging W3C standards like WASI-NN, you can write and test LLM applications in Rust on your Macbook, and then deploy on a Nvidia cloud server or an ARM NPU device without re-compilation or any change to the Wasm bytecode file. The Wasm apps can also be managed by existing container tools such as Docker, Podman, and K8s, making them a great alternative to Linux containers for this new workload. This talk will discuss how WasmEdge (CNCF sandbox) implements WASI-NN and supports a large array AI/LLM applications. You will learn practical skills on how to build and run LLM applications on ALL your local, edge, and cloud devices using a single binary application.
