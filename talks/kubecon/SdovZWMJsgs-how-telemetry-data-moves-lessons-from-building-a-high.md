---
id: SdovZWMJsgs
title: "How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent - Eduardo Silva"
slug: how-telemetry-data-moves-lessons-from-building-a-high
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Eduardo Silva"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 27
published_at: 2026-04-09T05:19:53Z
video_id: SdovZWMJsgs
youtube_url: https://www.youtube.com/watch?v=SdovZWMJsgs
tags: []
transcript: false
---

# How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent - Eduardo Silva

**Eduardo Silva**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=SdovZWMJsgs) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent - Eduardo Silva, Chronosphere | A Palo Alto Networks Company

Have you ever thought about how telemetry data really moves from the kernel to user space, across threads, buffers, and disks? This session goes beyond APIs and dashboards to explore the low-level mechanics of data processing at scale.

Drawing on experience developing Fluent Bit, we’ll examine how an open source agent processes billions of events per minute through custom user-space serialization, adaptive buffering, memory-mapped files, and multithreaded I/O orchestration. We’ll connect these design choices to Linux primitives like epoll, async I/O, and zero-copy strategies that keep CPU and memory footprints predictable.

This is not a product talk, it’s a deep exploration of data movement, buffering, and concurrency in modern telemetry systems, with insights valuable to anyone building high-throughput agents, collectors, or streaming engines.
