---
id: j0OLbJEL_yE
title: "NVIDIA’s Framework for Scalable Data Curation | Ray Summit 2025"
slug: nvidias-framework-for-scalable-data-curation-ray-summit-2025
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 30
published_at: 2025-11-18T23:19:57Z
video_id: j0OLbJEL_yE
url: https://www.youtube.com/watch?v=j0OLbJEL_yE
youtube_url: https://www.youtube.com/watch?v=j0OLbJEL_yE
tags: []
topics: ["Data engineering & MLOps", "Evals, observability & reliability", "Inference, serving & GPU infra", "Multimodal, vision, speech & robotics", "Training, fine-tuning & model building"]
transcript: false
---

# NVIDIA’s Framework for Scalable Data Curation | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=j0OLbJEL_yE) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Jacob Huffman and Hao Wang from NVIDIA share how Roblox built a modern ML platform on Ray and leveraged it to train their large-scale 3D foundation model.

They begin by walking through the platform’s architecture, including how Roblox integrated KubeRay with Istio and Kubeflow to support authentication, multi-tenancy, and secure orchestration. They also highlight efforts to open-source the new KubeRay dashboard, designed to improve iterative development, along with infrastructure innovations such as p2p Docker image distribution, lazy pulling, and the ability to scale Ray jobs across multiple clusters.

Jacob and Hao then dive into the challenges Roblox faced when applying Ray to foundation-model training workloads. This includes orchestrating massive LLM batch labeling jobs, leveraging Ray Data at scale, and supporting large distributed pipelines across heterogeneous compute. Historically, Roblox relied on MPI to launch distributed training, which handled multi-GPU execution but lacked critical capabilities like observability and fault tolerance.

Over the past year, the Roblox platform team evaluated and adopted Ray Train as their default distributed training framework—successfully migrating the majority of their training workloads from MPI to Ray, improving reliability and simplifying operations.

Attendees will take away practical insights into building production-grade Ray platforms, modernizing distributed training workflows, and supporting multimodal foundation model development at scale.

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
