---
id: KtnD-wILqb0
title: "LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu"
slug: llm-inference-at-scale-orchestrating-prefill-decode
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Zhonghu Xu"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 32
published_at: 2026-04-09T05:25:42Z
video_id: KtnD-wILqb0
youtube_url: https://www.youtube.com/watch?v=KtnD-wILqb0
tags: []
transcript: false
---

# LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu

**Zhonghu Xu**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=KtnD-wILqb0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu, Huawei Technologies Co., Ltd

Prefill-Decode (PD) disaggregation has emerged as the reference architecture for large language model (LLM) inference deployments. By separating the prefill and decode stages, PD disaggregation eliminates cross-stage interference, significantly improving Time-To-First-Token (TTFT) and Time-Per-Output-Token (TPOT) metrics.

This session introduces Kthena's approach to orchestrating PD-disaggregated LLM workloads in Kubernetes through a simple, lightweight API. Our hierarchical role-based design natively supports multi-group xPyD inference deployments with the following capabilities:

- Dynamically adjust instance ratios between prefill and decode stages accordingly
- Either collaborate with LeaderWorkerSet (LWS) for role-based deployments or direct Pod management
- Enhanced network topology aware shceduling: combined with Volcano or Kueue supernode-aware scheduling to achieve better inference performance.
