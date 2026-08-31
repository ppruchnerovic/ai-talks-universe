---
id: E7HIwOHbeN8
title: "No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie Bandel, NVIDIA"
slug: no-pain-no-drain-lessons-from-node-drains-at-scale-ryan
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 34
published_at: 2026-04-09T05:27:19Z
video_id: E7HIwOHbeN8
youtube_url: https://www.youtube.com/watch?v=E7HIwOHbeN8
tags: []
transcript: false
---

# No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie Bandel, NVIDIA

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=E7HIwOHbeN8) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie Bandel, NVIDIA

Draining nodes at scale is painful: workloads often can’t tolerate interruption and doing a naive $ kubectl drain can waste compute or cause downtime. In this session, we share lessons from large-scale operations at NVIDIA and our workload-aware approach to automated, safe node drain across Kubernetes clusters.

We’ll show how our drain algorithm selects the right nodes based on workload distribution, GPU utilization, and cluster capacity, while coordinating planned and unplanned maintenance to avoid overlap. Attendees will learn how to detect and recover from stuck or incomplete drains, ensuring safety, visibility, and repeatable day-2 operations.
Whether you run cloud or on-prem GPU workloads, you’ll leave with practical patterns and tooling insights that reduce risk, maximize utilization, and help Platform engineers manage GPU node maintenance reliably at scale.
