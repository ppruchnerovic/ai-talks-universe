---
id: 08jXkUBgWmY
title: "Extending BCC as a Data Source for System Monitoring - Eunseon Lee, LG Electronics"
slug: extending-bcc-as-a-data-source-for-system-monitoring
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: ["Eunseon Lee"]
channel: "The Linux Foundation"
duration_min: 29
published_at: 2025-09-05T19:44:13Z
video_id: 08jXkUBgWmY
url: https://www.youtube.com/watch?v=08jXkUBgWmY
youtube_url: https://www.youtube.com/watch?v=08jXkUBgWmY
tags: []
transcript: false
---

# Extending BCC as a Data Source for System Monitoring - Eunseon Lee, LG Electronics

**Eunseon Lee**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=08jXkUBgWmY) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Extending BCC as a Data Source for System Monitoring - Eunseon Lee, LG Electronics

eBPF enables efficient tracing and monitoring of modern Linux systems. However, tools in the BCC (BPF Compiler Collection) are primarily designed for standalone use, making it challenging to adopt them directly in real-time, streaming-based observability systems.

This talk introduces a practical approach to extending BCC tools for use as data sources in system monitoring pipelines. I demonstrate an architecture that transforms BCC output into time-series data by integrating with InfluxDB, and visualizes the data using Grafana. This enables real-time tracking of kernel and user-space events such as memory allocation over time.

I also explore enhancements to existing BCC tools, such as adding options to output data in time-series–friendly formats (e.g., InfluxDB’s line protocol), enabling easier ingestion by monitoring agents. These modifications help bridge the gap between raw eBPF observability and modern telemetry systems, without compromising BCC’s standalone usability. GitHub PR (https://github.com/iovisor/bcc/pull/5281) demonstrate these improvements.

Attendees will learn to leverage BCC tools for real-time insights and contribute enhancements for broader monitoring use cases.
