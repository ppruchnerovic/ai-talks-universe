---
id: VmFcwjpt8vE
title: "Lightning Talk: In-Cluster Distributed Checkpointing: Optimizing Training... - G. Kroiz & S. Mishra"
slug: lightning-talk-in-cluster-distributed-checkpointing
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["G. Kroiz", "S. Mishra"]
channel: "PyTorch"
duration_min: 10
published_at: 2025-11-04T03:43:40Z
video_id: VmFcwjpt8vE
url: https://www.youtube.com/watch?v=VmFcwjpt8vE
youtube_url: https://www.youtube.com/watch?v=VmFcwjpt8vE
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Lightning Talk: In-Cluster Distributed Checkpointing: Optimizing Training... - G. Kroiz & S. Mishra

**G. Kroiz, S. Mishra**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=VmFcwjpt8vE) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: In-Cluster Distributed Checkpointing: Optimizing Training Goodput Through GPU Node Locality - Gerson Kroiz, Google & Saurabh Mishra, Meta

As AI model training scales to thousands of GPUs, resiliency becomes essential. Failures—due to preemption, crashes, or infrastructure issues—can cause major training inefficiency and delay time-to-market. Checkpointing enables recovery, but traditional methods relying on remote storage often introduce latency and scalability challenges.

This talk presents In-Cluster Checkpointing, a new feature built on PyTorch’s Distributed Checkpointing (DCP) APIs that leverages node-local storage for faster, more scalable checkpointing. Each GPU node saves and restores its local training state, enabling frequent, low-overhead checkpoints that reduce training progress lost and restart latency. To support node replacement (e.g., due to failure or preemption), local checkpoints are automatically replicated and transferred to new nodes during recovery.

Co-developed by Google Cloud’s GPU Resiliency team and Meta’s Distributed Checkpointing team, this solution has improved training goodput by up to 5% in large-scale deployments—saving many thousands of GPU hours over multi-week run. Attendees will gain practical insights on integrating this technique to improve goodput in their own training jobs.
