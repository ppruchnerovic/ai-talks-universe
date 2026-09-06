---
id: h6LjH6Jkaf0
title: "PyTorch APIs for High Performance MoE Training and Inference - D. Vega-Myhre; Ke Wen & N. Gimelshein"
slug: pytorch-apis-for-high-performance-moe-training-and
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:45:07Z
video_id: h6LjH6Jkaf0
url: https://www.youtube.com/watch?v=h6LjH6Jkaf0
youtube_url: https://www.youtube.com/watch?v=h6LjH6Jkaf0
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# PyTorch APIs for High Performance MoE Training and Inference - D. Vega-Myhre; Ke Wen & N. Gimelshein

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=h6LjH6Jkaf0) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

PyTorch APIs for High Performance MoE Training and Inference - Daniel Vega-Myhre; Ke Wen & Natalia Gimelshein, Meta

With models like DeepSeekV3 and Llama4 rising in popularity, there has been an increasing demand for PyTorch-native APIs and tailored performance optimizations for MoE architectures.

This will be a joint talk between PyTorch Core, Distributed and Performance teams, focusing on features we’ve developed to better support and accelerate both MoE training and inference:

The talk will be broadly divided into 3 categories:
1. Computation (grouped GEMMs in PyTorch Core)
2. Communication (all-to-all-v dispatch/combine APIs in PyTorch Distributed)
3. Low precision training and inference optimizations (torchao API for MoE float8 training, low precision comms kernels, differentiable scaled grouped GEMM with dynamic quantization)
