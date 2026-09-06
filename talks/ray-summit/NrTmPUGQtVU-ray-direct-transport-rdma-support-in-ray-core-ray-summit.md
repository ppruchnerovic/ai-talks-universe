---
id: NrTmPUGQtVU
title: "Ray Direct Transport: RDMA Support in Ray Core | Ray Summit 2025"
slug: ray-direct-transport-rdma-support-in-ray-core-ray-summit
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 32
published_at: 2025-11-20T21:16:58Z
video_id: NrTmPUGQtVU
url: https://www.youtube.com/watch?v=NrTmPUGQtVU
youtube_url: https://www.youtube.com/watch?v=NrTmPUGQtVU
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Ray Direct Transport: RDMA Support in Ray Core | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=NrTmPUGQtVU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Slides: https://drive.google.com/file/d/1i8OG2LVWZatru9VMmZ4RJb06APTAy_5O/view?usp=sharing

At Ray Summit 2025, Stephanie Wang and Qiaolin Yu from Anyscale share how Ray Direct Transport (RDT) removes one of the most significant hidden bottlenecks in distributed GPU workloads on Ray—dramatically accelerating next-generation AI and RL systems.

They begin by explaining the core issue: in traditional Ray pipelines, every tensor passed between tasks or actors must be serialized and routed through CPU memory and the Ray object store. This creates major overhead for GPU-intensive workloads, slowing down reinforcement learning for LLMs, multimodal training pipelines, and other high-throughput compute patterns.

RDT eliminates this bottleneck entirely by keeping GPU data on the device and transferring it directly between actors using high-performance backends such as NCCL, Gloo, and RDMA. The result is zero-copy, serialization-free GPU communication—unlocking speedups that were previously impossible in Ray’s object store model.

Stephanie and Qiaolin walk through:

How RDT integrates cleanly with the familiar Ray ObjectRef API, making adoption straightforward

The architecture that enables direct, device-to-device data movement across distributed clusters

How RDT powers cutting-edge workloads such as disaggregated multimodal training and reinforcement learning for large language models

Live demonstrations showing how RDT enables fast, flexible, distributed GPU programming

Attendees will gain an understanding of how RDT transforms Ray into a high-performance GPU coordination layer—and how to leverage it for the next wave of large-scale AI workloads.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
