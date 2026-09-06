---
id: Drnt6rkeA9c
title: "Lightning Talk: Model Checkpoint Compression With OpenZL - Nick Terrell & Teja Rao, Meta"
slug: lightning-talk-model-checkpoint-compression-with-openzl
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Nick Terrell", "Teja Rao"]
channel: "PyTorch"
duration_min: 9
published_at: 2025-11-04T03:43:38Z
video_id: Drnt6rkeA9c
url: https://www.youtube.com/watch?v=Drnt6rkeA9c
youtube_url: https://www.youtube.com/watch?v=Drnt6rkeA9c
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Lightning Talk: Model Checkpoint Compression With OpenZL - Nick Terrell & Teja Rao, Meta

**Nick Terrell, Teja Rao**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=Drnt6rkeA9c) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: Model Checkpoint Compression With OpenZL - Nick Terrell & Teja Rao, Meta

Introducing OpenZL, an innovative open-source lossless compression framework optimized for structured data types. Traditional lossless compression methods are ineffective at compressing tensors because they operate at the byte level rather than at the tensor level. OpenZL leverages type information to achieve remarkable size reductions—33% for bfloat16, 21% for float32, and 15% for float16—with best-in-class performance. Deployed at scale within Meta Platforms Inc., we observed a 15% reduction in checkpoint overhead, saving thousands of GPUs, and a 17% reduction in storage, saving more than a hundred petabytes.

Unlike lossy compression methods like quantization, which can affect model quality, OpenZL maintains model quality and is easy to deploy at scale. We are exploring new AI use cases with OpenZL, leveraging its powerful compression capabilities in areas such as logits and image and video embeddings.
