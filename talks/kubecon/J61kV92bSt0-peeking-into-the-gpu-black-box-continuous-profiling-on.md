---
id: J61kV92bSt0
title: "Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev"
slug: peeking-into-the-gpu-black-box-continuous-profiling-on
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Zahari Dichev"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 29
published_at: 2026-04-09T05:24:09Z
video_id: J61kV92bSt0
youtube_url: https://www.youtube.com/watch?v=J61kV92bSt0
tags: []
transcript: false
---

# Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev

**Zahari Dichev**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=J61kV92bSt0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev, Buoyant

Gaining insight into how GPUs are used inside a Kubernetes cluster is a daunting challenge. Most existing tools weren’t built with containerized workloads in mind, leaving GPU activity opaque and hard to monitor. As AI and ML workloads increasingly run on Kubernetes, we need ways to introspect GPU usage at scale and understand how our services interact with these critical devices.

In this session, we’ll show an end-to-end approach to GPU observability with eBPF. You’ll learn how to continuously profile workloads and their interactions with GPU devices—tracing kernel launches, catching CUDA memory leaks, identifying faulty hardware, and visualizing workload activity across pods and nodes.

By bridging Kubernetes, GPUs, and eBPF, this solution transforms the GPU from a mysterious black box into a transparent, observable part of your cloud-native stack. If you’re ready to move beyond guesswork and gain actionable visibility into GPU workloads on Kubernetes, this talk is for you.
