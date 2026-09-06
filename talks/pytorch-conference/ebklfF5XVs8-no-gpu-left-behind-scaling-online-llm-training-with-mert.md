---
id: ebklfF5XVs8
title: "No GPU Left Behind: Scaling Online LLM Training With... - Mert Toslali & Yu Chin Fabian Lim"
slug: no-gpu-left-behind-scaling-online-llm-training-with-mert
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Mert Toslali", "Yu Chin Fabian Lim"]
channel: "PyTorch"
duration_min: 19
published_at: 2025-11-04T03:47:26Z
video_id: ebklfF5XVs8
url: https://www.youtube.com/watch?v=ebklfF5XVs8
youtube_url: https://www.youtube.com/watch?v=ebklfF5XVs8
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# No GPU Left Behind: Scaling Online LLM Training With... - Mert Toslali & Yu Chin Fabian Lim

**Mert Toslali, Yu Chin Fabian Lim**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=ebklfF5XVs8) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

No GPU Left Behind: Scaling Online LLM Training With Co-located VLLM in TRL - Mert Toslali & Yu Chin Fabian Lim, IBM Research

Training LLMs with online RL methods like GRPO presents a unique challenge: inference is required at every training step. In the standard Hugging Face TRL setup, inference is handled by vLLM running as a separate server on dedicated GPUs, communicating via HTTP. This creates a “ping-pong” inefficiency—training GPUs wait during generation, and inference GPUs wait during training—leading to poor GPU utilization and high cost.

Our talk introduces co-located vLLM, a key optimization that enables training and inference to run on the same GPUs. Built on vLLM’s external_launcher, it allows in-process, torch-compatible execution. We contributed a now-merged PR to TRL that eliminates the need for HTTP calls or separate servers. Our setup supports torchrun, TP/DP, and scales to training large models (like 72B). This setup improves training throughput by up to 1.7×, reduces # of GPUs needed, and is now part of the official TRL repo.
