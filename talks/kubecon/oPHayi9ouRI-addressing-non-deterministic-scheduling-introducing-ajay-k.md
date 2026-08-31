---
id: oPHayi9ouRI
title: "Addressing Non-Deterministic Scheduling: Introducing... Ajay K, Sreeram V, Karthik N & Priyanka S"
slug: addressing-non-deterministic-scheduling-introducing-ajay-k
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 32
published_at: 2026-04-09T05:17:25Z
video_id: oPHayi9ouRI
youtube_url: https://www.youtube.com/watch?v=oPHayi9ouRI
tags: []
transcript: false
---

# Addressing Non-Deterministic Scheduling: Introducing... Ajay K, Sreeram V, Karthik N & Priyanka S

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=oPHayi9ouRI) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Addressing Non-Deterministic Scheduling: Introducing the Node Readiness Controller - Ajay Sundar Karuppasamy, Google; Sreeram Venkitesh, DigitalOcean; Karthik K N, IBM; Priyanka Saggu, SUSE

Kubernetes nodes report “Ready” before critical dependencies, such as CNI plugins, storage drivers or device plugins are fully functional. This “readiness gap” causes non-deterministic scheduling, where sensitive workloads immediately fail upon placement.

Since our KubeCon NA Unconference discussion, this initiative has matured into an official SIG-Node subproject. In this session, its maintainers will present the architecture of the Node Readiness Controller, which uses ‘NodeReadinessRules’ to declaratively manage taints based on custom conditions, ensuring a protected node initialization.

This session is designed for platform builders and contributors. We will discuss:
-Architecture patterns: Leveraging existing node-problem-detector ecosystem as a unified mechanism for readiness reporting.
-Roadmap: Discuss current status, upcoming features and potential integration pathways.
-Cross-SIG alignment: how the controller interacts with existing scheduling primitives and autoscalers.
