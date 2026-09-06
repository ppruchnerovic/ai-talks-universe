---
id: Ylp1Pt1nvEU
title: "Enabling VLLM V1 on AMD GPUs With Triton - Thomas Parnell, IBM Research & Aleksandr Malyshev, AMD"
slug: enabling-vllm-v1-on-amd-gpus-with-triton-thomas-parnell-ibm
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Thomas Parnell"]
channel: "PyTorch"
duration_min: 22
published_at: 2025-11-04T03:45:05Z
video_id: Ylp1Pt1nvEU
url: https://www.youtube.com/watch?v=Ylp1Pt1nvEU
youtube_url: https://www.youtube.com/watch?v=Ylp1Pt1nvEU
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Enabling VLLM V1 on AMD GPUs With Triton - Thomas Parnell, IBM Research & Aleksandr Malyshev, AMD

**Thomas Parnell**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=Ylp1Pt1nvEU) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Enabling VLLM V1 on AMD GPUs With Triton - Thomas Parnell, IBM Research & Aleksandr Malyshev, AMD

In January 2025, vLLM announced the alpha release of V1: a major upgrade to vLLM’s core architecture. One of the key goals of V1 was to enable all vLLM’s inference performance optimizations (e.g., continuous batching, paged attention, chunked prefill, prefix caching, speculative decoding) to work seamlessly together. Achieving this required architectural changes that propagated down to the kernel-level. In fact, in the alpha release of V1, only NVIDIA GPUs were supported due to lack of V1-compliant attention kernels.

In this talk, we will describe how we enabled vLLM V1 to run with state-of-the-art performance on AMD GPUs. We will begin by describing an initial attempt to enable V1 using a relatively old Triton kernel and explain why this approach was not performant. We will then describe a sequence of kernel-level optimizations made by the teams from IBM, Red Hat and AMD that, when combined, allowed us to improve the performance of V1 on AMD GPUs by up to 5x.

This talk will provide deep insights into how vLLM V1 works from community and industry experts. It will also provide Triton kernel developers with tips and tricks into how to achieve maximum performance.
