---
id: BM4L74qL8zE
title: "Redefining SLIs for LLM Inference: Managing Hybrid Cloud wit... Christopher Nuland & Hilliary Lipsig"
slug: redefining-slis-for-llm-inference-managing-hybrid-cloud-wit
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 29
published_at: 2026-04-09T05:19:43Z
video_id: BM4L74qL8zE
youtube_url: https://www.youtube.com/watch?v=BM4L74qL8zE
tags: []
transcript: false
---

# Redefining SLIs for LLM Inference: Managing Hybrid Cloud wit... Christopher Nuland & Hilliary Lipsig

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=BM4L74qL8zE) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Redefining SLIs for LLM Inference: Managing Hybrid Cloud with vLLM & LLM-D - Christopher Nuland & Hilliary Lipsig, Red Hat

Large Language Models (LLM) are reshaping application delivery, introducing new operational challenges for SREs. Traditional metrics like CPU or request latency are no longer sufficient. Latency is now measured in tokens per second, and reliability depends on routing efficiency and cache hit rates. In hybrid cloud environments, inference pipelines span gateways, schedulers, caches, and sharded backends, complicating observability and SLO management. This session explores evolving SLOs/SLIs for production LLMs, covering metrics like Time-to-First-Token (TTFT), cache hit ratio, routing latency, and GPU utilization. We’ll show how vLLM and llm-d provide the primitives for scalable, observable inference: vLLM for high-performance batching and caching, and llm-d for intelligent scheduling and KV-cache-aware routing. Attendees will learn to define new SLOs, instrument distributed inference with Prometheus, OpenTelemetry, and Grafana, and integrate LLM telemetry into Kubernetes SRE workflows.
