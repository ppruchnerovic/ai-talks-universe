---
id: X3wl3lstsAY
title: "Lightning Talk: Containers Live Migration: What’s There, What’s Missing, What’s... Daniel Simionato"
slug: lightning-talk-containers-live-migration-whats-there-whats
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: []
channel: "The Linux Foundation"
duration_min: 13
published_at: 2025-09-05T19:37:55Z
video_id: X3wl3lstsAY
url: https://www.youtube.com/watch?v=X3wl3lstsAY
youtube_url: https://www.youtube.com/watch?v=X3wl3lstsAY
tags: []
topics: ["Classic ML & data science"]
transcript: false
---

# Lightning Talk: Containers Live Migration: What’s There, What’s Missing, What’s... Daniel Simionato

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=X3wl3lstsAY) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Lightning Talk: Containers Live Migration: What’s There, What’s Missing, What’s Next? - Daniel Simionato, ControlPlane

Moving a running workload from one host to another transparently without disrupting its execution flow (“live migration”) is a solved problem for virtual machines, but still poses challenges for containers.

Current checkpoint and restore functionalities in both Kubernetes and LXD are somewhat limited or not completely fleshed out, and moving containers from one host to another involves either spinning up new replicas or stopping and restarting the containers, which is undesirable for stateful workloads like databases, machine learning or deep learning jobs.

Projects like CRIU (https://criu.org/Main_Page) and DMTCP (https://github.com/dmtcp/dmtcp) propose different approaches to offer checkpointing and restore functionalities in containers, but there is still no streamlined solution in LXD and Kubernetes.

In this lightning talk, we’ll go over the current state of the art, with a quick demo of what’s currently available, describing what’s missing and what will be the future developments to achieve seamless container live migration.
