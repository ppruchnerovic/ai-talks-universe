---
id: R2NXTHrsFwU
title: "Efficient MoE Pre-training at Scale on AMD GPUs With TorchTitan -Liz Li & Yanyuan Qin, Matthias Reso"
slug: efficient-moe-pre-training-at-scale-on-amd-gpus-with
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 26
published_at: 2025-11-04T03:45:05Z
video_id: R2NXTHrsFwU
url: https://www.youtube.com/watch?v=R2NXTHrsFwU
youtube_url: https://www.youtube.com/watch?v=R2NXTHrsFwU
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Efficient MoE Pre-training at Scale on AMD GPUs With TorchTitan -Liz Li & Yanyuan Qin, Matthias Reso

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=R2NXTHrsFwU) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Efficient MoE Pre-training at Scale on AMD GPUs With TorchTitan - Liz Li & Yanyuan Qin, AMD; Matthias Reso, Meta

Mixture-of-Experts (MoE) architectures enable efficient scaling of deep learning models but face challenges across diverse hardware. We present a scalable, optimized MoE pre-training pipeline with TorchTitan on AMD MI300X GPUs, built fully within PyTorch ecosystem. Our method uses efficient FP8 blockwise and grouped GEMM via torch._scaled_mm, combining scaling, quantization-aware compute, and reduced-precision arithmetic. Moreover, we remove CPU-GPU sync via a custom triton kernel speeding up the forward pass by ~3x.

These optimizations support various backends including the AITER library, Triton, and HIP backends, fully leveraging AMD’s CDNA architecture and matrix cores. Key contributions include register-level data movement optimizations, expert-grouped execution via grouped GEMM, and dynamic MoE routing. We achieve strong scaling to 1000+ MI300X GPUs, demonstrating linear scaling and competitive per-GPU performance on large-scale MoE training.

Final proposal will include thorough analysis of Fp8 training pipeline with TorchTitan and optimized parallel strategy on Tensorwave’s AMD GPU cloud, demonstrating state-of-the-art training performance at scale on DeepSeek-R1 and LLaMA4.
