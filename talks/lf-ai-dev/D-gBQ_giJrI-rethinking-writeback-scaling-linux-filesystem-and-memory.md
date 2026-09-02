---
id: D-gBQ_giJrI
title: "Rethinking Writeback: Scaling Linux Filesystem and Memory Performance for the Next D... Kundan Kumar"
slug: rethinking-writeback-scaling-linux-filesystem-and-memory
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: []
channel: "The Linux Foundation"
duration_min: 38
published_at: 2025-09-05T19:44:14Z
video_id: D-gBQ_giJrI
url: https://www.youtube.com/watch?v=D-gBQ_giJrI
youtube_url: https://www.youtube.com/watch?v=D-gBQ_giJrI
tags: []
transcript: false
---

# Rethinking Writeback: Scaling Linux Filesystem and Memory Performance for the Next D... Kundan Kumar

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `38 min`

[Watch the recording](https://www.youtube.com/watch?v=D-gBQ_giJrI) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Rethinking Writeback: Scaling Linux Filesystem and Memory Performance for the Next Decade - Kundan Kumar, Samsung R&D Institute India

Linux’s current writeback infrastructure, while robust, was designed before large folios, CXL-tiered memory, and AI workloads demanding low-latency, high-throughput I/O. Today, workloads like RAG pipelines using vector databases with buffered I/O, and memory tiering on CXL, are exposing scalability limits in how the kernel handles writeback.

This talk presents a forward-looking view on evolving Linux’s writeback model. We’ll explore how the single-threaded design stalls page migration and reduces memory compaction effectiveness—affecting hugepage allocations and folio movement across memory tiers, contributing to fragmentation. On the storage side, parallelizing writeback improves throughput and responsiveness under dirty-page pressure, especially for sustained-write workloads with large memory footprints on High capacity SSDs.

We’ll also touch on early experiments within the kernel community, including efforts to make writeback more filesystem-geometry aware and parallelize it based on overwrites/new allocations.

This session invites open source community to reimagine writeback as a scalable, performance-critical component in Linux.
