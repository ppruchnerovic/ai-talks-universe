---
id: pvonHzx-z0o
title: "Optimizing Error Recovery for Cost-Ef... Radostin Stoyanov, Andrey Velichkevich & Viktória Spišáková"
slug: optimizing-error-recovery-for-cost-ef-radostin-stoyanov
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 21
published_at: 2026-04-09T05:17:25Z
video_id: pvonHzx-z0o
youtube_url: https://www.youtube.com/watch?v=pvonHzx-z0o
tags: []
transcript: false
---

# Optimizing Error Recovery for Cost-Ef... Radostin Stoyanov, Andrey Velichkevich & Viktória Spišáková

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `21 min`

[Watch the recording](https://www.youtube.com/watch?v=pvonHzx-z0o) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Optimizing Error Recovery for Cost-Efficient Distributed AI Model Training with Kubernetes - Radostin Stoyanov, University of Oxford & Andrey Velichkevich, Apple; Viktória Spišáková, Masaryk University

Achieving scalable and fault-tolerant distributed AI model training that runs efficiently across multiple nodes remains a key challenge for platform administrators and ML engineers. This problem is further exacerbated by interactive GPU workloads, such as Jupyter notebooks, that generate intermittent computations followed by idle periods while users refine their code and explore the results.

This talk will present how transparent GPU checkpointing can be integrated with Kubernetes to improve both cost efficiency and cluster utilization for distributed AI workloads. By automatically capturing and restoring the state of training jobs, this approach enables seamless recovery from preemptions or failures. This session will also explore how checkpoint policies integrate with the Kueue, JobSet, and TrainJob APIs for Kubernetes-native, infrastructure-level checkpointing of GPU workloads - empowering users to leverage preemptible spot instances for reliable, cost-effective AI model training.
