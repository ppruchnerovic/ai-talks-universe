---
id: 8P2y_gyHQA8
title: "From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data P... Rainie Li & Ang Zhang"
slug: from-idle-to-savings-building-a-global-scheduler-for
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 23
published_at: 2026-04-09T05:19:44Z
video_id: 8P2y_gyHQA8
youtube_url: https://www.youtube.com/watch?v=8P2y_gyHQA8
tags: []
transcript: false
---

# From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data P... Rainie Li & Ang Zhang

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=8P2y_gyHQA8) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

From Idle to Savings: Building a Global Scheduler for Cost‑Efficient Data Processing on K8s - Rainie Li & Ang Zhang, Pinterest

At Pinterest, we built a batch scheduling service on top of Kubernetes that saves tens of millions of CPU/GPU compute costs by running big data + AI/ML (Spark and Ray/Pytorch) jobs on a mix of temporary capacity (borrowed from online service during off-peak hours) and fixed pools. The service chooses the cheapest viable placement across clusters and AZs using live capacity, capacity forecast, and an ML model–based algorithm that scores jobs (runtime/urgency/cost) and decides which jobs to run, when to start them, and to which cluster—maximizing utilization while guaranteeing SLOs. We keep in-cluster schedulers thin (Volcano/YuniKorn for pod placement + Gang scheduling) and apply pure K8s primitives: PriorityClass, nodeAffinity/topologySpreadConstraints, and PodGroup/TaskGroup. We’ll share the service design, including cost-aware routing, quota mapping (budgets→weights/caps), and dashboards showing 99% starts ≤5m and high utilization.
