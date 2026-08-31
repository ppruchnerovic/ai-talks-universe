---
id: ycnDgULCHTA
title: "Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observ... Iris Dyrmishi & Rodrigo Fior Kuntzer"
slug: cutting-metrics-traffic-cutting-costs-the-az-aware-observ
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 31
published_at: 2026-04-09T05:19:55Z
video_id: ycnDgULCHTA
youtube_url: https://www.youtube.com/watch?v=ycnDgULCHTA
tags: []
transcript: false
---

# Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observ... Iris Dyrmishi & Rodrigo Fior Kuntzer

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=ycnDgULCHTA) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observability Blueprint - Iris Dyrmishi & Rodrigo Fior Kuntzer, Miro

We know observability gets expensive, yet we consistently overlook the highest-cost element: network traffic. Optimizing for storage and compute is common, but inter-AZ data transfer remains a major budget sink.
This talk presents a field-proven strategy for significantly reducing cloud traffic costs by minimizing cross-availability zone (AZ) metrics collection. We'll show how to leverage standard relabeling mechanisms in popular tools, like Prometheus, OpenTelemetry, and VictoriaMetrics, to implement an AZ-aware sharding strategy. Configuring agents to scrape only targets within their own zone drastically reduces inter-AZ transfer. We'll share a practical, vendor-agnostic blueprint, including real-world savings data, applicable to any large-scale metrics pipeline. This approach directly addresses unnecessary cloud spend and provides a clear path to a more cost-efficient and resilient observability stack.
