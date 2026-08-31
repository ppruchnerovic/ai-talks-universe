---
id: 24E4LDWThAE
title: "Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM"
slug: three-shades-of-isolation-a-multi-tenancy-fortress-braulio
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 34
published_at: 2026-04-09T05:23:08Z
video_id: 24E4LDWThAE
youtube_url: https://www.youtube.com/watch?v=24E4LDWThAE
tags: []
transcript: false
---

# Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=24E4LDWThAE) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM

Multi-tenancy is a popular architectural concept in cloud native environments. For Kubernetes, it’s concerned with sharing a single cluster resource among multiple users referred to as tenants, while maintaining isolation, security, and performance between them. In this talk, we present a new approach for multi-tenancy isolation that hardening tenant’s boundaries by providing three shades of isolation (i.e., data-plane, control-plane and network) for each tenant in a cost-effective manner using open-source technologies: K3s, KubeFlex/KubeStellar, KubeVirt and UDN/OVN-k8s. Our approach helps to simplify the multi-tenancy management and enforcement strategies for clusters admins. We’ll also dive into the main requirements for multi-tenancy in Kubernetes, survey the most popular models and discuss their challenges, as well as how our approach addresses them. Finally, we’ll demonstrate how to use our framework to isolate workloads, using llm-d and vLLM production stack as case studies.
