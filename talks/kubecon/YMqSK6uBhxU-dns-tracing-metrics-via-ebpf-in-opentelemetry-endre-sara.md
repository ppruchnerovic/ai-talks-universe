---
id: YMqSK6uBhxU
title: "DNS Tracing & Metrics Via eBPF in OpenTelemetry- Endre Sara, Causely & Nikola Grcevski, Grafana Labs"
slug: dns-tracing-metrics-via-ebpf-in-opentelemetry-endre-sara
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 33
published_at: 2026-04-27T16:59:33Z
video_id: YMqSK6uBhxU
youtube_url: https://www.youtube.com/watch?v=YMqSK6uBhxU
tags: []
transcript: false
---

# DNS Tracing & Metrics Via eBPF in OpenTelemetry- Endre Sara, Causely & Nikola Grcevski, Grafana Labs

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=YMqSK6uBhxU) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

DNS Tracing & Metrics Via eBPF in OpenTelemetry - Endre Sara, Causely & Nikola Grcevski, Grafana Labs

Modern cloud native applications rely heavily on DNS resolution under the hood—service discovery, external API calls, internal dependencies. Yet, DNS performance issues (latency, timeouts, misconfigurations) often remain invisible in observability stacks, hidden behind “network” or “external call” noise.

This talk proposes integrating DNS observability directly into the OpenTelemetry eBPF Instrumentation (OBI) agent. We’ll cover the architectural challenges (eBPF context, semantic conventions, scalability), the proposed metrics & tracing model, and the value this adds to operators diagnosing performance or reliability issues. Attendees will walk away with lessons on how to instrument low-level system interactions (like DNS) in a cloud native world, and a blueprint for extending observability in eBPF agents beyond what exists today.
