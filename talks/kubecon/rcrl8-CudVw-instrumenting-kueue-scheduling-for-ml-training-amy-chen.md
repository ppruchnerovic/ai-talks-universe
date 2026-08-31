---
id: rcrl8-CudVw
title: "Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google"
slug: instrumenting-kueue-scheduling-for-ml-training-amy-chen
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Amy Chen"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 32
published_at: 2026-04-09T05:27:21Z
video_id: rcrl8-CudVw
youtube_url: https://www.youtube.com/watch?v=rcrl8-CudVw
tags: []
transcript: false
---

# Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google

**Amy Chen**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=rcrl8-CudVw) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google

Kueue is a job scheduler with functionality essential for running batch/ML workloads. Operating it at scale surfaced opaque scheduling failures. We take learnings from our large-scale ML training platform, detailing how we cracked open Kueue's scheduler’s “black box,” improving observability and translating complex scheduling logic into clear, actionable signals.

In this session, we will first deep dive into the stages of Kueue's scheduling to create a foundational understanding. Then present a subtle fairsharing quota reclamation bug, showcasing the metrics and logging we added to detect it and prove its impact. And finally, present examples where Kueue metrics helped us identify critical bottlenecks in Kueue’s preemption logic.

Attendees walk away with practical knowledge to instrument the Kueue workload lifecycle, enabling them to track workloads through each stage, from reservation to admission, definitively answering the critical question: “Why is my workload still pending?”
