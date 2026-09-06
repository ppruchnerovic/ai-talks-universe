---
id: mzHed-fKHx8
title: "Lightning Talk: Accelerating PyTorch FSDP Via Overlapping Collectives With In... - Nariaki Tateiwa"
slug: lightning-talk-accelerating-pytorch-fsdp-via-overlapping
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Nariaki Tateiwa"]
channel: "PyTorch"
duration_min: 14
published_at: 2025-11-04T03:45:07Z
video_id: mzHed-fKHx8
url: https://www.youtube.com/watch?v=mzHed-fKHx8
youtube_url: https://www.youtube.com/watch?v=mzHed-fKHx8
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Lightning Talk: Accelerating PyTorch FSDP Via Overlapping Collectives With In... - Nariaki Tateiwa

**Nariaki Tateiwa**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=mzHed-fKHx8) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: Accelerating PyTorch FSDP Via Overlapping Collectives With In-Network Computing and Multicast - Nariaki Tateiwa, Nippon Telegraph and Telephone

The rapid growth of LLM scale has exceeded accelerator memory limits; as a result, memory-efficient distributed training has become essential. In PyTorch, Fully Sharded Data Parallel (FSDP) has become a critical solution to address this challenge. However, FSDP suffers from significant inter-accelerator communication overhead, particularly with the ReduceScatter and Allgather collectives in the backward pass. Recent research by Khalilov et al. (SC’ 24) proposes a scheme for overlapping these collectives using in-network computing and multicast technologies, potentially halving communication volume in the backward pass. However, there are no practical collective communication libraries that enable both technologies, and thus the current PyTorch FSDP (v1/v2) implementations do not support overlapping these collectives.

In this talk, we present (1) an extension to the UCC library that leverages in-network computing and InfiniBand multicast; (2) an implementation that enables overlapping ReduceScatter and Allgather in PyTorch FSDP; and (3) numerical results demonstrating up to 2x faster communication and significant improvements in training throughput for LLM workloads.
