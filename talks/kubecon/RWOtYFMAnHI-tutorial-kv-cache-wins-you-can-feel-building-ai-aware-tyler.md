---
id: RWOtYFMAnHI
title: "Tutorial: KV-Cache Wins You Can Feel: Building AI-Aware... Tyler S, Kay Y, Vita B, Nili G & Maroon A"
slug: tutorial-kv-cache-wins-you-can-feel-building-ai-aware-tyler
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 81
published_at: 2026-04-09T05:17:23Z
video_id: RWOtYFMAnHI
youtube_url: https://www.youtube.com/watch?v=RWOtYFMAnHI
tags: []
transcript: false
---

# Tutorial: KV-Cache Wins You Can Feel: Building AI-Aware... Tyler S, Kay Y, Vita B, Nili G & Maroon A

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `81 min`

[Watch the recording](https://www.youtube.com/watch?v=RWOtYFMAnHI) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Tutorial: KV-Cache Wins You Can Feel: Building AI-Aware LLM Routing on Kubernetes - Tyler Michael Smith, Red Hat; Kay Yan, DaoCloud; Vita Bortnikov, Nili Guy & Maroon Ayoub, IBM

Every LLM request carries invisible state: the KV-cache. Hit it, and your response is 10x cheaper and 50x faster. Miss it, and you're recomputing work you just did. Yet Kubernetes' default load balancing is cache-blind, scattering related requests across pods and destroying locality. The result? Your AI workloads are slower and vastly more expensive than they should be.

In this hands-on tutorial, we’ll fix that.

Attendees will deploy a distributed vLLM cluster, benchmark its performance, and visualize how cache-blind routing wastes GPU cycles. Then, we’ll replace the default Service with the Kubernetes Gateway API (Inference Extension) and deploy llm-d, a Kubernetes-native framework for distributed LLM inference with an AI-aware scheduler. By re-running the same benchmarks, you’ll see latency and throughput transform as prefix-reuse becomes first-class. You’ll leave with a working lab, dashboards, and a mental model for building cache-aware routing into any production AI stack.
