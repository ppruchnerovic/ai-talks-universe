---
id: PEU4uDzurvc
title: "How To Break Multi-Tenancy Again and Again ...and What We Can Learn F... Lorin Lehawany & Sven Nobis"
slug: how-to-break-multi-tenancy-again-and-again-and-what-we-can
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 29
published_at: 2026-04-09T05:21:42Z
video_id: PEU4uDzurvc
youtube_url: https://www.youtube.com/watch?v=PEU4uDzurvc
tags: []
transcript: false
---

# How To Break Multi-Tenancy Again and Again ...and What We Can Learn F... Lorin Lehawany & Sven Nobis

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=PEU4uDzurvc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

How To Break Multi-Tenancy Again and Again ...and What We Can Learn From It - Lorin Lehawany & Sven Nobis, ERNW

Namespace-based multi-tenancy is challenging to implement and less effective than control-plane isolation. Thus, the latter is the standard today. But is this really true? Workloads such as machine learning, pipelines, or scripting capabilities can introduce unobvious multi-tenancy in clusters and become increasingly popular.

So the question is: How to isolate those workloads from each other securely? Pod Security Standards, Network Policies, and Admission Controller are well-adopted, but is it enough?

The answer is no: This talk presents real-world exploits in Kubeflow, Istio, and Traefik to bypass threat boundaries between namespaces and workloads.

Based on these examples, this talk presents a methodology for assessing complex environments with isolation problems and guides how to address them.
