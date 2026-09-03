---
id: Ou14GsR2gkA
title: "Unlocking Scalable Distributed Training With Arrow Data Cache on Kubernetes - Ricardo Aravena, CNCF"
slug: unlocking-scalable-distributed-training-with-arrow-data
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "AI_dev Europe 2025"
year: 2025
speakers: ["Ricardo Aravena"]
channel: "The Linux Foundation"
duration_min: 26
published_at: 2025-09-09T18:28:22Z
video_id: Ou14GsR2gkA
url: https://www.youtube.com/watch?v=Ou14GsR2gkA
youtube_url: https://www.youtube.com/watch?v=Ou14GsR2gkA
tags: []
topics: ["Data engineering & MLOps", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Unlocking Scalable Distributed Training With Arrow Data Cache on Kubernetes - Ricardo Aravena, CNCF

**Ricardo Aravena**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI_dev Europe 2025` · `2025` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=Ou14GsR2gkA) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Unlocking Scalable Distributed Training With Arrow Data Cache on Kubernetes - Ricardo Aravena, CNCF

As the scale of AI models and training datasets grows, so does the complexity of efficiently feeding data into GPU-accelerated training workloads. Traditional I/O stacks are becoming a bottleneck—especially in cloud native environments—where elasticity and performance must go hand in hand. This talk introduces an open-source, Arrow-based data cache for distributed training workloads on Kubernetes and tabular datasets stored as Apache Iceberg tables.

We'll explore how this cache decouples data preprocessing from training jobs and enables sharing preprocessed datasets across distributed training nodes. We reduce data loading overhead by leveraging Apache Arrow's columnar format and zero-copy semantics and improve GPU utilization. We'll also discuss our integration with Kubernetes-native orchestration tools like Kubeflow TrainJob, JobSet, LeaderWorkerSet, Volcano, and Kueue and how this design pattern enables reproducibility, cache reuse, and performance across multi-tenant environments.

Whether you're running PyTorch, TensorFlow, or JAX, this session will provide practical insights into building scalable, cloud-native training workloads—without getting bottlenecked by your data.
