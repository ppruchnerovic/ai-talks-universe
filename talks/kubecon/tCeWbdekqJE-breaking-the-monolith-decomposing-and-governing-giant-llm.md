---
id: tCeWbdekqJE
title: "Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei"
slug: breaking-the-monolith-decomposing-and-governing-giant-llm
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Kevin Wang"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 24
published_at: 2026-04-09T05:29:40Z
video_id: tCeWbdekqJE
youtube_url: https://www.youtube.com/watch?v=tCeWbdekqJE
tags: []
transcript: false
---

# Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei

**Kevin Wang**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=tCeWbdekqJE) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei

Multi-cluster architecture is now a common choice for enterprise AI infrastructure, enabling unified resource management, flexible integration of multi-cloud and data center GPUs, and abstraction of hardware differences for simplified scheduling.

Traditionally, AI jobs were scheduled as a whole to a member cluster to ensure performance consistency, but this limited flexibility and resource utilization. In practice, splitting jobs across clusters becomes necessary for large-scale LLM training exceeding single-cluster capacity or aggregating idle resources from multiple clusters.

This session introduces how Volcano Global and Karmada enable adaptive cross-cluster scheduling for LLM jobs:
1. a universal global scheduling control plane
2. a higher-level job abstraction for intelligent decomposition of large AI jobs across clusters
3. a centralized global queue and priority mechanism to ensure fair and orderly resource allocation, preventing large tasks from overwhelming the shared pool
