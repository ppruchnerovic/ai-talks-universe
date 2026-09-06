---
id: rX1ar5lcZy4
title: "Monarch: A Distributed Execution Engine for PyTorch - Colin Taylor & Zachary DeVito, Meta"
slug: monarch-a-distributed-execution-engine-for-pytorch-colin
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 24
published_at: 2025-11-04T03:43:40Z
video_id: rX1ar5lcZy4
url: https://www.youtube.com/watch?v=rX1ar5lcZy4
youtube_url: https://www.youtube.com/watch?v=rX1ar5lcZy4
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Monarch: A Distributed Execution Engine for PyTorch - Colin Taylor & Zachary DeVito, Meta

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=rX1ar5lcZy4) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Monarch: A Distributed Execution Engine for PyTorch - Colin Taylor & Zachary DeVito, Meta

In this talk we present Monarch, a distributed training stack for PyTorch. Our goal, following the PyTorch philosophy, is to provide a set of composable primitives with which users can easily build orchestration at large scale over heterogeneous compute resources and lifecycles.

Traditional distributed PyTorch uses a multi-controller approach: you launch multiple copies of the same script across different machines, and these independent processes coordinate through collective operations. Each process runs its own copy of your training loop.

Monarch is a single-controller: one script directly orchestrates all distributed resources, almost as if they were local. Instead of spawning multiple independently controlled processes, you write one program that treats the entire cluster as a single, unified system.

This architectural shift simplifies programming: no more reasoning about process ranks, synchronization barriers, or collective communication patterns. Your code looks and feels like a single-machine PyTorch, but scales across thousands of GPUs, and you can directly use ordinary programming constructs – classes, functions, loops, tasks, futures – to express distributed algorithms.
