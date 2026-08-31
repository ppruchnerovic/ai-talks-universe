---
id: Jj8DNLA5hYc
title: "Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simula... Weizhou Lan"
slug: making-topology-aware-scheduling-practical-for-ai-workloads
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 24
published_at: 2026-04-09T05:19:53Z
video_id: Jj8DNLA5hYc
youtube_url: https://www.youtube.com/watch?v=Jj8DNLA5hYc
tags: []
transcript: false
---

# Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simula... Weizhou Lan

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=Jj8DNLA5hYc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simulation at Scale - Weizhou Lan, Daocloud

In large-scale AI inference clusters, multi-tenant workloads require both efficient GPU utilization and dynamic RDMA networking. However, heterogeneous GPU interconnect technologies inevitably lead to multi-level network topologies, such as scale-up networks and RDMA spine–leaf structures.
These diverse topologies introduce several challenges: Dynamic topology discovery and health detection across multiple layers, including scale-up, RDMA spine, and RDMA leaf. Second, Topology-aware scheduling that supports priority-based placement and ensures GPUs leverage optimal communication paths.Third, Validation at scale, requiring cost-effective simulation of large, multi-level topologies instead of relying on expensive hardware.
In this talk, it will share practical approach of topology discovery to help Kueue to achieve topology-aware scheduling, and showcase how Kwok simulates thousands of virtual nodes with multi-level topologies, enabling large-scale validation at zero hardware cost.
