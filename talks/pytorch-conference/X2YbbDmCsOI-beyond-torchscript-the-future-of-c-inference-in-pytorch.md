---
id: X2YbbDmCsOI
title: "Beyond TorchScript: The Future of C++ Inference in PyTorch - Sherlock Huang, Meta"
slug: beyond-torchscript-the-future-of-c-inference-in-pytorch
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Sherlock Huang"]
channel: "PyTorch"
duration_min: 27
published_at: 2025-11-04T03:43:40Z
video_id: X2YbbDmCsOI
url: https://www.youtube.com/watch?v=X2YbbDmCsOI
youtube_url: https://www.youtube.com/watch?v=X2YbbDmCsOI
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Beyond TorchScript: The Future of C++ Inference in PyTorch - Sherlock Huang, Meta

**Sherlock Huang**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=X2YbbDmCsOI) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Beyond TorchScript: The Future of C++ Inference in PyTorch - Sherlock Huang, Meta

TorchScript is the load bearing component for serving PyTorch models in a non-Python environment. It powers a wide range of ML applications, including mobile applications and hyper-scale recommendation systems. However, early design decisions in TorchScript made it difficult to incorporate innovations.

Since the introduction of PyTorch 2.0, we have developed a new C++ inference workflow leveraging the new power components that improve the performance and deployability of ML models.

In this talk, you'll discover the best practices and latest advancements in C++ inference. We'll cover:
- Recommended workflows for C++ inference in different scenarios.
- ExecuTorch Mobile: Stable for mobile and embedded env.
- ExecuTorch Full: Coming soon for PC and server deployments.

Migrating from TorchScript?
If you're currently using TorchScript, we'll provide guidance on how to transition smoothly:
- Replacing TorchScript Frontend: Discover torch.export, a modernized graph capturing system.
- Upgrading from TorchScript Backend: Introducing the ExecuTorch Full Runtime, a high-performance C++ runtime that simplifies and accelerates PyTorch model deployment on PCs and servers.
