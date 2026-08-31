---
id: lLxrtmpIlMk
title: "Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kub... Peter H, Adrian R, Radostin S & Viktória S"
slug: ctrl-x-ctrl-v-your-pods-wg-checkpoint-restore-in-kub-peter
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 34
published_at: 2026-04-09T05:17:23Z
video_id: lLxrtmpIlMk
youtube_url: https://www.youtube.com/watch?v=lLxrtmpIlMk
tags: []
transcript: false
---

# Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kub... Peter H, Adrian R, Radostin S & Viktória S

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=lLxrtmpIlMk) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kubernetes - Peter Hunt & Adrian Reber, Red Hat; Radostin Stoyanov, University of Oxford; Viktória Spišaková, Masaryk University

Checkpoint/Restore is a relatively old technology in linux that allows taking a snapshot of a process, and later resuming the execution of that checkpoint. In Kubernetes 1.25, preliminary support was added for checkpointing containers in KEP 2008. However, there is a lot more that can be done with Checkpoint/Restore.

The Kubernetes community has recently pulled together a working group to accelerate the adoption of Checkpoint/Restore technologies. Some items on the roadmap are pod level checkpointing, an in-tree API, and using checkpoint/restore for advanced use cases like preemption and eviction (which will especially help batch workloads, like ones for training AI models). Join the leads of the WG Checkpoint Restore and learn about what has been done already, and what lies on the horizon of this WG.
