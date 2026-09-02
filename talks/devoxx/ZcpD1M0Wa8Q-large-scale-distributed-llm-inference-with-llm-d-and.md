---
id: ZcpD1M0Wa8Q
title: "Large Scale Distributed LLM Inference with LLM D and Kubernetes by Abdel Sghiouar"
slug: large-scale-distributed-llm-inference-with-llm-d-and
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2025
speakers: ["Abdel Sghiouar"]
channel: "Devoxx"
duration_min: 104
published_at: 2025-10-07T05:13:52Z
video_id: ZcpD1M0Wa8Q
url: https://www.youtube.com/watch?v=ZcpD1M0Wa8Q
youtube_url: https://www.youtube.com/watch?v=ZcpD1M0Wa8Q
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Large Scale Distributed LLM Inference with LLM D and Kubernetes by Abdel Sghiouar

**Abdel Sghiouar**

`Devoxx` · `Devoxx` · `2025` · `104 min`

[Watch the recording](https://www.youtube.com/watch?v=ZcpD1M0Wa8Q) · [Conference site](https://devoxx.com/)

## Description

Running Large Language Models (LLMs) locally for experimentation is easy but running them in large scale architectures is not. It requires businesses looking to intergate LLMs into their critical paths to deal with the high costs and scarcity of GPU/TPU accelerators present a significant challenge. Striking the balance between performance, availability, scalability, and cost-efficiency is a must.While Kubernetes is a ubiquitous runtime for modern workloads, deploying LLM inference effectively demands a specialized approach. Enter LLM-D a Cloud Native Kubernetes based high-performance distributed LLM inference framework. It&#39;s architecture centers around a well-lit path for anyone looking to serve at scale, with the fastest time-to-value and competitive performance per dollar, for most models across a diverse and comprehensive set of hardware accelerators.In this deep dive we will start with a gentle introduction to the topic of Inference on Kubernetes and slowly work our way to why LLM-D and what kind of challenges it solves. LLM-D is a set of components and an opinionated architecture. Building on top of existing projects like vLLM, Prometheus, the Kubernetes Gateway API. It&#39;s optimized KV-cache aware routing and disaggregated serving are designed to operationalize GenAI deployments. The project was designed by the creators of vLLM (Redhat, Google, Bytedance) and it&#39;s licensed under the Apache 2 License.
