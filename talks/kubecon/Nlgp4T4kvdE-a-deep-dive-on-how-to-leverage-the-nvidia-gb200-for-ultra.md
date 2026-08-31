---
id: Nlgp4T4kvdE
title: "A Deep Dive on How To Leverage the NVIDIA GB200 for Ultra-Fast... Kevin Klues & Jan-Philip Gehrcke"
slug: a-deep-dive-on-how-to-leverage-the-nvidia-gb200-for-ultra
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 28
published_at: 2026-04-13T23:36:03Z
video_id: Nlgp4T4kvdE
youtube_url: https://www.youtube.com/watch?v=Nlgp4T4kvdE
tags: []
transcript: false
---

# A Deep Dive on How To Leverage the NVIDIA GB200 for Ultra-Fast... Kevin Klues & Jan-Philip Gehrcke

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=Nlgp4T4kvdE) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

A Deep Dive on How To Leverage the NVIDIA GB200 for Ultra-Fast Training and Inference on Kubernetes - Kevin Klues & Jan-Philip Gehrcke, NVIDIA

Multi-node AI training and inference jobs split workloads across nodes to scale performance and handle large datasets. With the introduction of specialized hardware such as NVIDIA’s GB200 NVL72, these jobs are no longer limited by traditional networking fabrics such as InfiniBand or RoCE. Instead, NVLink connects all 72 GPUs across 18 nodes in a full mesh network, accelerating multi-node workloads with low-latency, high-bandwidth communication.

In this talk, we introduce a new abstraction called a “ComputeDomain,” which users create via NVIDIA’s DRA driver for GPUs to run multi-node workloads on NVLink-connected GB200 systems. We discuss the intricacies of what’s needed to run these workloads securely, as well as how the ComputeDomain abstraction leverages DRA to hide these details from the end-user. Additionally, we discuss how this support has been pushed to all major cloud providers and integrated with their managed Kubernetes offerings. We conclude with a demo.
