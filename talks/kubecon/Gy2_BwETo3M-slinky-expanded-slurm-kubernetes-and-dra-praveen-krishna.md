---
id: Gy2_BwETo3M
title: "Slinky Expanded: Slurm, Kubernetes, and DRA - Praveen Krishna, Google & Marlow Warnicke, SchedMD LLC"
slug: slinky-expanded-slurm-kubernetes-and-dra-praveen-krishna
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Praveen Krishna"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:25:42Z
video_id: Gy2_BwETo3M
youtube_url: https://www.youtube.com/watch?v=Gy2_BwETo3M
tags: []
transcript: false
---

# Slinky Expanded: Slurm, Kubernetes, and DRA - Praveen Krishna, Google & Marlow Warnicke, SchedMD LLC

**Praveen Krishna**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=Gy2_BwETo3M) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Slinky Expanded: Slurm, Kubernetes, and DRA - Praveen Krishna, Google & Marlow Warnicke, SchedMD LLC

For training and multi-node inference jobs to be performant and efficient, you must maximize cluster use and minimize resource costs. This requires fine-grained resource scheduling plugged into an advanced scheduler; without it, your workloads will not meet these goals. The Kubernetes ecosystem has solved half of the problem by exposing hardware information via Dynamic Resource Allocation (DRA), but an advanced scheduler is needed to use that information for efficient scheduling.

The slurm-bridge scheduler, part of the SlinkyProject, brings this advanced scheduling to Kubernetes for multi-node workloads. Historically, it relied on slurmd daemons running directly on the node to get the detailed topology information. We have now adapted the slurm-bridge to consume resource information directly from the Kubernetes-native CPU DRA driver, demonstrating a new level of attainable efficiency.

Join us for a demonstration of how these technologies work together.
