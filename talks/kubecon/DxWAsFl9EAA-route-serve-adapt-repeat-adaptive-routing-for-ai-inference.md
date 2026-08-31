---
id: DxWAsFl9EAA
title: "Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workl... Nir Rozenbaum & Kellen Swain"
slug: route-serve-adapt-repeat-adaptive-routing-for-ai-inference
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 20
published_at: 2026-04-09T05:10:51Z
video_id: DxWAsFl9EAA
youtube_url: https://www.youtube.com/watch?v=DxWAsFl9EAA
tags: []
transcript: false
---

# Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workl... Nir Rozenbaum & Kellen Swain

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=DxWAsFl9EAA) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workloads in Kubernetes - Nir Rozenbaum, Red Hat & Kellen Swain, Google

Running inference on K8s can be costly and extremely slow.
Today’s inference routing strategies like traffic splitting, node affinity or session stickiness — are all static. Once defined, they ignore changing load, queue build-ups, and cache locality.

Inference workloads, however, are dynamic: requests vary, cache states shift, and cluster conditions evolve. Static routing strategies simply can’t keep up, leading to latency spikes and wasted GPU cycles.

With K8s Gateway API Inference Extension, we introduce adaptive routing strategies for inference, driven by real-time signals such as queue length and cache utilization. By continuously adapting, the system balances cache efficiency with load distribution, reduces latency, improves GPU utilization, and lowers costs at scale.

Attendees will learn why static routing strategies limit inference performance and see benchmarks demonstrating latency, efficiency, and cost gains with adaptive routing in K8s Gateway API Inference Extension.
