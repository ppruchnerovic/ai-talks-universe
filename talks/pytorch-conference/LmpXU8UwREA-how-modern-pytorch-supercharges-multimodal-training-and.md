---
id: LmpXU8UwREA
title: "How Modern PyTorch Supercharges Multimodal Training and Inference at Luma AI - Thomas Neff, Luma AI"
slug: how-modern-pytorch-supercharges-multimodal-training-and
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Thomas Neff"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:43:38Z
video_id: LmpXU8UwREA
url: https://www.youtube.com/watch?v=LmpXU8UwREA
youtube_url: https://www.youtube.com/watch?v=LmpXU8UwREA
tags: []
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics", "Training, fine-tuning & model building"]
transcript: false
---

# How Modern PyTorch Supercharges Multimodal Training and Inference at Luma AI - Thomas Neff, Luma AI

**Thomas Neff**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=LmpXU8UwREA) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

How Modern PyTorch Supercharges Multimodal Training and Inference at Luma AI - Thomas Neff, Luma AI

Luma AI was the first company to release a "new generation" video generative model powered by large diffusion transformers freely accessible to the public. With the release of Dream Machine in 2024, which was built by a tiny team in only 5 months, millions of users were able to see the potential of multimodal generative AI for the first time.

This session focuses on how we designed our training & inference code to scale and how we solely rely on modern PyTorch to combine extreme flexibility for researchers with efficient code paths to scale multimodal training and inference towards thousands of GPUs.
We will discuss how we are continuously keeping up with the bleeding edge of PyTorch and why this has allowed us to move extremely fast.

We will cover things such as how we efficiently use torch.compile, how to best make use of torch.distributed, how custom ops can lead to massive speedups in multimodal training, and will showcase some pitfalls, issues and share our experience from scaling up our architecture and training resources.

We will also discuss how this allows us to be flexible and push out updates to inference fast, reusing the same pieces that we use for training.
