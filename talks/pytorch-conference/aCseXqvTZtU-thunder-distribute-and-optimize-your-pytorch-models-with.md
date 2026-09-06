---
id: aCseXqvTZtU
title: "Thunder: Distribute and Optimize Your PyTorch Models With Zero... - Luca Antiga & Thomas Viehmann"
slug: thunder-distribute-and-optimize-your-pytorch-models-with
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Luca Antiga", "Thomas Viehmann"]
channel: "PyTorch"
duration_min: 26
published_at: 2025-11-04T03:46:57Z
video_id: aCseXqvTZtU
url: https://www.youtube.com/watch?v=aCseXqvTZtU
youtube_url: https://www.youtube.com/watch?v=aCseXqvTZtU
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Thunder: Distribute and Optimize Your PyTorch Models With Zero... - Luca Antiga & Thomas Viehmann

**Luca Antiga, Thomas Viehmann**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=aCseXqvTZtU) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Thunder: Distribute and Optimize Your PyTorch Models With Zero Code Changes - Luca Antiga & Thomas Viehmann, Lightning AI

Since its early days, PyTorch has empowered researchers and practitioners with its expressive design. However, as hardware advances and model scales grow, users are increasingly required to embed optimizations and distributed logic directly into model code.

Thunder is a PyTorch compiler designed to easily enhance models programmatically using composable, full-graph transforms. Emphasizing usability, understandability, and extensibility, Thunder generates Python code at each transformation stage, making it simple to develop and debug new transforms.

In this talk, you’ll learn how to achieve 2x speedups on LLMs like Qwen and Llama running on Hopper and Blackwell architectures, starting from model definitions from HuggingFace Transformers and LitGPT. We’ll demonstrate how to apply composable transforms to augment models with Megatron-style parallelism, kernel fusion (NVFuser and torch.compile), and specialized libraries (cuDNN, TransformerEngine, Apex) with zero code changes.

We’ll walk through writing a transform from scratch for parameter sharding and distributed communication. Finally, we’ll show how Thunder integrates with popular training and inference frameworks.
