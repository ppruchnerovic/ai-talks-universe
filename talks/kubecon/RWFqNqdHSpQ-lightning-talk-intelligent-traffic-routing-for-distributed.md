---
id: RWFqNqdHSpQ
title: "Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Trad... Zhonghu Xu"
slug: lightning-talk-intelligent-traffic-routing-for-distributed
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 11
published_at: 2026-04-13T23:36:03Z
video_id: RWFqNqdHSpQ
youtube_url: https://www.youtube.com/watch?v=RWFqNqdHSpQ
tags: []
transcript: false
---

# Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Trad... Zhonghu Xu

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=RWFqNqdHSpQ) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Traditional Gateway Approaches - Zhonghu Xu, Huawei Technologies Co., Ltd

As LLM inference adopts Kubernetes, intelligent routing has become critical. Existing gateways like Gateway Inference Extension, LLM-d, and Aibrix struggle with emerging patterns like prefill-decode (PD) disaggregation and distributed parallelism (DP+EP).

This session introduces **Kthena Router**, a production-grade orchestration system for multi-model LLM workloads. Unlike approaches relying solely on engine metrics, it uses **closed-loop control with adaptive modeling** based on connections, token lengths, load distribution, and role-aware routing.
In this session, we also will deep dive:

1. How to do multi-model serving through routing policies, eliminating per-model gateway deployments
2. Native PD disaggregation support with prefill-decode awareness, then removes dependencies on per-group routers or LLM-d sidecars
3. Pluggable scheduling with fairness scheduling, semantic-aware routing, KV-cache aware placement, and GPU utilization-aware balancing.
