---
id: 5vmbRVXBvVM
title: "Lightning Talk: Vllm-triton-backend: How To Get State-of-the-art Performance on... - B. Ringlein"
slug: lightning-talk-vllm-triton-backend-how-to-get-state-of-the
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["B. Ringlein"]
channel: "PyTorch"
duration_min: 9
published_at: 2025-11-04T03:45:03Z
video_id: 5vmbRVXBvVM
url: https://www.youtube.com/watch?v=5vmbRVXBvVM
youtube_url: https://www.youtube.com/watch?v=5vmbRVXBvVM
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Lightning Talk: Vllm-triton-backend: How To Get State-of-the-art Performance on... - B. Ringlein

**B. Ringlein**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=5vmbRVXBvVM) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: Vllm-triton-backend: How To Get State-of-the-art Performance on NVIDIA and AMD With Just Triton - Burkhard Ringlein, IBM

Today, vLLM (part of pytorch) is the de-facto industry standard for serving Large Language Models. vLLM is increasingly being adopted in production and can be executed on NVIDIA GPUS, AMD GPUs, as well as custom accelerators like AWS Inferentia.

However, for most of the past, vLLM’s state-of-the-art performance war largely depending on a number of hand-written CUDA or HIP kernels. These kernels have typically been carefully optimized for a specific GPU platform and may pose a serious obstacle to the portability of vLLM across different hardware.

Leveraging Open AI Triton, we were able to introduce a “triton backend” to vllm that produces state-of-the-art performance across GPU platforms with a single code base, without involving hand written CUDA or HIP kernels.

In this talk, we will present our recent advances that lead to state-of-the-art performance on both NVIDIA and AMD GPUs with a single Triton-only code-base. We will present the engineering and science behind this triton-only backend, including autotuning for different platforms, system aspects like the launch overhead of Tritons Just-in-time compiler, and different kernel optimizations.
