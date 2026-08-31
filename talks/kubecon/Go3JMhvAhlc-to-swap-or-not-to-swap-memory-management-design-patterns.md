---
id: Go3JMhvAhlc
title: "To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kuber... Nic Vermande"
slug: to-swap-or-not-to-swap-memory-management-design-patterns
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 35
published_at: 2026-04-09T05:25:42Z
video_id: Go3JMhvAhlc
youtube_url: https://www.youtube.com/watch?v=Go3JMhvAhlc
tags: []
transcript: false
---

# To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kuber... Nic Vermande

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `35 min`

[Watch the recording](https://www.youtube.com/watch?v=Go3JMhvAhlc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kubernetes 1.34+ - Nic Vermande, ScaleOps

Kubernetes swap support is now stable, reopening a debate the industry thought was settled: is swap still evil? For AI/ML workloads with 100GB+ memory footprints, the answer is nuanced.

This talk explores when swap helps vs. hurts GPU inference and training workloads. We'll cover 3 real production scenarios:

- Overcommitting Memory: Running multiple small models on shared nodes where occasional swap prevents OOMKills.
- Burst Traffic Handling: Using swap as a safety valve during traffic spikes when KV cache grows beyond predictions. Live demo with vLLM showing graceful degradation vs. pod eviction.
- When Swap Kills You: Training workloads and real-time inference where swap latency destroys performance.
By the end of this talk, you will know exactly when to enable swap and when to keep it disabled. Production-tested configs included!
