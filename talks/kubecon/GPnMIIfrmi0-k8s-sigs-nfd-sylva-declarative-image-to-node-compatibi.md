---
id: GPnMIIfrmi0
title: "K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibi... Eduardo Arango Gutierrez & Chaoyi Huang"
slug: k8s-sigs-nfd-sylva-declarative-image-to-node-compatibi
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 35
published_at: 2026-04-09T05:19:44Z
video_id: GPnMIIfrmi0
youtube_url: https://www.youtube.com/watch?v=GPnMIIfrmi0
tags: []
transcript: false
---

# K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibi... Eduardo Arango Gutierrez & Chaoyi Huang

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `35 min`

[Watch the recording](https://www.youtube.com/watch?v=GPnMIIfrmi0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibility for Telco Clouds. - Eduardo Arango Gutierrez, NVIDIA & Chaoyi Huang, Huawei Technology Co., Ltd

Portable images still fail or present performance degradation at runtime when host kernels, drivers, or hardware deviate—especially in telco/edge stacks. This session reports a field deployment co-developed by k8s-sigs Node Feature Discovery (NFD) maintainers and the SYLVA telco-cloud community (Linux Foundation Europe). We encode host requirements as a versioned OCI artifact stored with the image, validate target nodes pre-scheduling with the nfd client, and feed results into admission, scheduling, and CI/CD gates across heterogeneous SYLVA platforms. We cover the artifact schema, ORAS attach, NFD rule mapping/NodeFeatureGroups, and production lessons (registry behavior, kernel/driver drift, multi-vendor silicon). Live demo: GPU/RDMA/kernel-module scenarios that fail fast via policy instead of at runtime—making compatibility declarative across Kubernetes and telco clouds.
