---
id: SLXM1Z0ZjAw
title: "Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai"
slug: lightning-talk-k8s-issue-52757-sharing-gpus-among-multiple
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: ["Xiao Zhang"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 10
published_at: 2026-04-13T23:36:44Z
video_id: SLXM1Z0ZjAw
youtube_url: https://www.youtube.com/watch?v=SLXM1Z0ZjAw
tags: []
transcript: false
---

# Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai

**Xiao Zhang**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=SLXM1Z0ZjAw) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai

This issue has plagued Kubernetes for nearly 8 years: K8s issue #52757. The challenge of flexibly sharing GPUs across multiple containers is particularly prominent in AI scenarios, where inference tasks are typically short-lived. As a result, resource utilization becomes a critical concern.

In this talk, we will share solutions and practices for implementing GPU sharing in Kubernetes, focusing on two key projects gaining traction recently: Dynamic Resource Allocation (DRA) and the CNCF sandbox project HAMi. The presentation will cover the following topics:
1. Challenges in GPU sharing.
2. Approaches for sharing AI chips beyond NVIDIA GPUs.
3. How sharing technologies integrate with projects like Volcano, Koordinator, and Kueue.
