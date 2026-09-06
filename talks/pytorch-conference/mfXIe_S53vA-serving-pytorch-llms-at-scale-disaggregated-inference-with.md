---
id: mfXIe_S53vA
title: "Serving PyTorch LLMs at Scale: Disaggregated Inference With Kubernetes and Llm-d - M. Ayoub & C. Liu"
slug: serving-pytorch-llms-at-scale-disaggregated-inference-with
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["M. Ayoub", "C. Liu"]
channel: "PyTorch"
duration_min: 27
published_at: 2025-11-04T03:43:40Z
video_id: mfXIe_S53vA
url: https://www.youtube.com/watch?v=mfXIe_S53vA
youtube_url: https://www.youtube.com/watch?v=mfXIe_S53vA
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Serving PyTorch LLMs at Scale: Disaggregated Inference With Kubernetes and Llm-d - M. Ayoub & C. Liu

**M. Ayoub, C. Liu**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=mfXIe_S53vA) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Serving PyTorch LLMs at Scale: Disaggregated Inference With Kubernetes and Llm-d - Maroon Ayoub, IBM Research & Cong Liu, Google

As PyTorch-based LLMs scale in complexity and user concurrency, their inference demands diverge across stages. Prefill is compute-heavy; decode is latency-sensitive. In this talk, we introduce a disaggregated serving pattern for PyTorch LLMs using llm-d—a Kubernetes-native, open-source framework co-developed by IBM Research, Google, and Red Hat. We'll walk through how llm-d separates prefill and decode into orchestrated sidecars, improving GPU utilization and QoS alignment. You'll learn how the Gateway API Inference Extension (GIE) enables routing based on load, cache locality, and session affinity. The talk includes real-world benchmarks and a visual demo of llm-d serving PyTorch models with vLLM across heterogeneous hardware on Kubernetes.
