---
id: pOvWgX7IJsc
title: "Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI"
slug: can-llms-write-fast-multi-gpu-kernels-simran-arora-together
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Simran Arora"]
channel: null
duration_min: 30
published_at: 2026-08-27T00:00:00Z
video_id: pOvWgX7IJsc
youtube_url: https://www.youtube.com/watch?v=pOvWgX7IJsc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI

**Simran Arora**

`AI Engineer` · `AI Engineer` · `2026` · `30 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=pOvWgX7IJsc) · [Conference site](https://www.ai.engineer/)

## Description

Between NVIDIA's A100 in 2020 and the B200 in 2024, BF16 tensor core throughput improved 7.2x. Intra node communication improved 3x, and inter node communication only 2x. That widening gap has pushed the bottleneck in large AI workloads off the individual GPU and onto the links between them, far enough that a standard PyTorch and NCCL baseline lands below 50% of its communication aware roofline on most problems. Simran Arora leads the frontier performance research team at Together AI, and her group's answer is ParallelKittens, a small set of primitives that adds roughly a dozen lines to a single GPU kernel and now runs in production at Together AI and Cursor.

The harder question was whether models can apply the same principles. ParallelKernelBench hands a model an unoptimized PyTorch reference and a topology spec across 87 problems drawn from real repositories, then asks for a CUDA kernel that moves data directly over NVLink. The best frontier model solved 28 of them zero shot, with 22 beating the baseline. Drawing more samples lifts correctness to 36, but the share that is both correct and faster stalls near 31%. Wrapping a model in a multi turn agent harness with a bash environment reached 35. The failures are not syntax. Models compile after a retry and then stall on collective ordering, data partitioning, and the choice between the copy engine, tensor memory acceleration and register level transfers, while their wins cluster in the patterns most represented on the internet.

Speaker info:
- https://arorasimran.com
- https://github.com/simran-arora
- https://github.com/togethercomputer/ParallelKernelBench

Timestamps:
0:00 - From single GPU kernels to the network between them
1:29 - Inside an H100, and why memory distance matters
4:44 - The interconnect hierarchy: PCIe, NVLink, NVSwitch
5:46 - Why GPU networking, and why now
8:27 - Disaggregated workloads and 576 GPU systems
10:24 - Compute improved 7.2x, the network 3x
11:14 - Where NCCL breaks down, and the roofline gap
13:04 - Compilers, DSLs, and hand tuned operators
14:10 - The research question, and ParallelKittens
16:06 - Transfer mechanisms: copy engine, TMA, register level
18:28 - Overlapping compute and communication across SMs
20:52 - In production at Together AI and Cursor
22:10 - Inside ParallelKernelBench: 87 problems
24:32 - Zero shot results, and where scaling stalls
26:28 - The failures are not CUDA syntax
27:07 - An agent harness, and what is still missing
