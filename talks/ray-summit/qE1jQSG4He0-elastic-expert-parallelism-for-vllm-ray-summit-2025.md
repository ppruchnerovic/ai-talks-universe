---
id: qE1jQSG4He0
title: "Elastic Expert Parallelism for vLLM | Ray Summit 2025"
slug: elastic-expert-parallelism-for-vllm-ray-summit-2025
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 34
published_at: 2025-11-19T17:21:22Z
video_id: qE1jQSG4He0
url: https://www.youtube.com/watch?v=qE1jQSG4He0
youtube_url: https://www.youtube.com/watch?v=qE1jQSG4He0
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Elastic Expert Parallelism for vLLM | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=qE1jQSG4He0) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Yongji Wu from UC Berkeley and Rui Qiao from Anyscale share how they are advancing large-scale Expert Parallelism (EP) to unlock efficient, scalable inference for Mixture-of-Experts (MoE) models.

They begin by outlining a core constraint in MoE serving: EP often requires massive, monolithic deployment units—for example, DeepSeek R3/V1 needs 144 GPUs just to form a single serving instance. Such large units make it extremely difficult for traditional inter-instance autoscaling systems to react to real-world workload fluctuations.

To address this, the speakers introduce intra-instance Elastic EP, a new technique that brings fine-grained, low-latency autoscaling inside a single EP instance. This enables vLLM to tightly match GPU resources to workload demand without incurring downtime, fragmentation, or inefficient overprovisioning.

They then show how Ray is used to orchestrate Elastic EP scaling across distributed clusters, providing the coordination, lifecycle management, and flexibility needed to dynamically adjust expert-parallel resources while keeping inference fast and reliable.

Attendees will learn practical strategies for serving large MoE models at scale, optimizing KV-cache and expert utilization, and using Ray to coordinate sophisticated intra-instance parallelism patterns.

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
