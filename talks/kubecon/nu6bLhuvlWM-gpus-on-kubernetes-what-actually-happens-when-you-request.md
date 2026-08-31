---
id: nu6bLhuvlWM
title: "GPUs on Kubernetes: What Actually Happens When You Request Nvidia... Gulcan Topcu & Daniele Polencic"
slug: gpus-on-kubernetes-what-actually-happens-when-you-request
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:20:37Z
video_id: nu6bLhuvlWM
youtube_url: https://www.youtube.com/watch?v=nu6bLhuvlWM
tags: []
transcript: false
---

# GPUs on Kubernetes: What Actually Happens When You Request Nvidia... Gulcan Topcu & Daniele Polencic

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=nu6bLhuvlWM) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

GPUs on Kubernetes: What Actually Happens When You Request Nvidia.com/gpu: 1 - Gulcan Topcu & Daniele Polencic, LearnKube

You write `nvidia.com/gpu: 1` in your pod spec and somehow your container can use a GPU. But what actually happened?

This session pulls back the curtain on GPU scheduling in Kubernetes.

We'll trace a GPU workload end-to-end. You'll see how device plugins advertise GPUs to the scheduler, how the container runtime mounts device files into your container, and why the NVIDIA driver does all the real work while the Linux kernel stays blind.

Along the way, you'll learn why GPUs break every assumption Kubernetes makes about resource isolation.Then we tackle the expensive problem: your team wants to share a single GPU between multiple pods, but Kubernetes only understands whole numbers.

We'll compare practical approaches like time-slicing, MIG hardware partitioning, and software enforcement. You'll learn when each makes sense and why "GPU utilization" metrics often lie.

No GPU background needed. Just bring curiosity about how things work under the hood.
