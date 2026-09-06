---
id: DvFmVYA8nmA
title: "Unlocking Performance: Harnessing LLMs To Streamline GPU Kernel Development in... - Jiannan Wang"
slug: unlocking-performance-harnessing-llms-to-streamline-gpu
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Jiannan Wang"]
channel: "PyTorch"
duration_min: 20
published_at: 2025-11-04T03:46:55Z
video_id: DvFmVYA8nmA
url: https://www.youtube.com/watch?v=DvFmVYA8nmA
youtube_url: https://www.youtube.com/watch?v=DvFmVYA8nmA
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Unlocking Performance: Harnessing LLMs To Streamline GPU Kernel Development in... - Jiannan Wang

**Jiannan Wang**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=DvFmVYA8nmA) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Unlocking Performance: Harnessing LLMs To Streamline GPU Kernel Development in PyTorch - Jiannan Wang, Meta

Custom CUDA kernels offer significant performance advantages for PyTorch developers aiming to optimize deep learning models. While PyTorch currently provides multiple pathways to integrate these kernels, ongoing efforts are focused on enhancing abstractions and tooling, analyzing kernel usage patterns through extensive datasets, and creating LLM-based tooling to assist kernel authors in maximizing GPU efficiency.

One key initiative is KernelBook, a comprehensive dataset containing over 25,000 pairs of PyTorch operations and their corresponding Triton implementations. This dataset serves as a foundation for training models capable of generating optimized Triton code directly from PyTorch inputs.

Complementing this effort, the KernelLLM project leverages large language models to automate GPU kernel generation. Notably, an 8B-parameter model trained on KernelBook has achieved performance comparable to DeepSeek-R1, a 671B-parameter model, based on pass@10 benchmarks. Further development includes training an 80B-parameter model specifically for kernel translation tasks and another model focused on generating performant Triton kernels beyond direct translations.
