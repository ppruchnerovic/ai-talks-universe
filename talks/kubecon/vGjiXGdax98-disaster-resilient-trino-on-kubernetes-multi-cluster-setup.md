---
id: vGjiXGdax98
title: "Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karma... Sung Yun & Antoine Marthey"
slug: disaster-resilient-trino-on-kubernetes-multi-cluster-setup
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 31
published_at: 2026-04-09T05:23:11Z
video_id: vGjiXGdax98
youtube_url: https://www.youtube.com/watch?v=vGjiXGdax98
tags: []
transcript: false
---

# Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karma... Sung Yun & Antoine Marthey

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=vGjiXGdax98) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Disaster Resilient Trino on Kubernetes: Multi-Cluster Setup With Karmada and Trino Gateway - Sung Yun & Antoine Marthey, Bloomberg LP

As firms scale their data science and AI platforms, ensuring that distributed SQL engines remain available during cluster failures or regional outages is just as crucial as governance and scalability. At KubeCon EU 2025, we shared Bloomberg’s managed Trino architecture on Kubernetes, built around centralized policy enforcement and tenant isolation.

This year, we present its evolution: a disaster-resilient Trino design. With Karmada, we duplicate Trino deployments across multiple regions for high availability. On top, Trino Gateway provides namespace-scoped unified query endpoints for each tenant, enabling transparent query routing while preserving strong governance. Together, these components deliver a multi-cluster, highly available, production-ready Trino platform that powers Bloomberg’s analytics workloads.

By sharing design principles, trade-offs, and operational lessons, we’ll offer attendees a practical blueprint for building resilient, governed data platforms on Kubernetes.
