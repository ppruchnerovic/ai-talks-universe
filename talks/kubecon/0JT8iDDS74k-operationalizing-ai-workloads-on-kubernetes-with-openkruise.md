---
id: 0JT8iDDS74k
title: "Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun"
slug: operationalizing-ai-workloads-on-kubernetes-with-openkruise
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 20
published_at: 2026-04-09T05:24:09Z
video_id: 0JT8iDDS74k
youtube_url: https://www.youtube.com/watch?v=0JT8iDDS74k
tags: []
transcript: false
---

# Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=0JT8iDDS74k) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen, Alibaba Cloud & Vec Sun, Xiaohongshu(RedNote)

AI workloads on Kubernetes face unique operational challenges: container images packed with large models and libraries require pre-warming for fast startup, and distributed training jobs often run as PodGroups that must be scheduled and disrupted together. However, native Kubernetes lacks group-aware disruption handling—PodDisruptionBudget treats pods individually, risking partial job failures during node maintenance or hardware issues.

In this talk, we showcase OpenKruise’s solutions: (1) cron-based image pre-warming to proactively cache AI images on target nodes; (2) an advanced disruption policy that enforces availability constraints at the PodGroup level; and (3) upcoming enhancements to ContainerRestartRequest to support planned, in-place restarts of entire PodGroups—rebuilding only necessary pods while restarting others inplace. These features enable reliable, efficient AI workload operations on Kubernetes at scale.
