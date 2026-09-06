---
id: mket48-xpSk
title: "Mojo + PyTorch: A Simpler, Faster Path To Custom Kernels - Spenser Bauman, Modular"
slug: mojo-pytorch-a-simpler-faster-path-to-custom-kernels
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Spenser Bauman"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:46:56Z
video_id: mket48-xpSk
url: https://www.youtube.com/watch?v=mket48-xpSk
youtube_url: https://www.youtube.com/watch?v=mket48-xpSk
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Mojo + PyTorch: A Simpler, Faster Path To Custom Kernels - Spenser Bauman, Modular

**Spenser Bauman**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=mket48-xpSk) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Mojo + PyTorch: A Simpler, Faster Path To Custom Kernels - Spenser Bauman, Modular

PyTorch offers multiple ways to integrate custom kernel implementations, especially when working with CUDA. While this flexibility is powerful, it leads to fragmentation across tools, build systems, and APIs. Developers often run into long compile times, complex toolchain requirements, and ABI challenges that make custom op development harder to maintain and distribute.

This talk explores a new workflow for writing custom ops in PyTorch using Mojo, a high-performance systems language for AI. It shows how Mojo can be used to define custom kernels that integrate with PyTorch through Python, avoiding the need for C++, CUDA, or complex build tools. The approach offers a straightforward and portable way to develop high-performance custom ops.

We'll walk through:
- A look at the current landscape of PyTorch custom kernel integration
- How Mojo improves ergonomics and speeds up development
- Using Mojo-based ops in eager mode and with torch.compile
- Examples of accelerating inference with Mojo
- Extending to training by implementing the backwards pass in Mojo

This talk is for PyTorch developers who want more control over performance without the overhead of traditional CUDA development.
