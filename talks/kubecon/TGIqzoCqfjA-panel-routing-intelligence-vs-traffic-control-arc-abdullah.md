---
id: TGIqzoCqfjA
title: "Panel: Routing Intelligence Vs Traffic Control: Arc... Abdullah G, Morgan F, Eitan Y, Nili G & Dan S"
slug: panel-routing-intelligence-vs-traffic-control-arc-abdullah
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 41
published_at: 2026-04-13T23:31:27Z
video_id: TGIqzoCqfjA
youtube_url: https://www.youtube.com/watch?v=TGIqzoCqfjA
tags: []
transcript: false
---

# Panel: Routing Intelligence Vs Traffic Control: Arc... Abdullah G, Morgan F, Eitan Y, Nili G & Dan S

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `41 min`

[Watch the recording](https://www.youtube.com/watch?v=TGIqzoCqfjA) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Panel: Routing Intelligence Vs Traffic Control: Architectural Tradeoffs for AI Inference in Gateway API - Abdullah Gharaibeh, Google; Morgan Foster, Red Hat; Eitan Yarmush, Solo.io; Nili Guy, IBM, Dan Sun, Bloomberg

As AI inference workloads become the norm in Kubernetes, the Gateway API Inference Extension (GAIE) faced a pivotal architectural question: should request scheduling act as a "consultant" via an external processing filter or become a full-fledged Service in the traffic path?
This panel brings together maintainers and practitioners to explore two models for routing AI inference. GAIE uses external processing to make scheduling decisions without proxying traffic - an unconventional but deliberate choice that prioritizes simplicity and performance. An alternative would place the scheduler directly in the data path as a next-hop Service, aligning with Gateway API norms.
This discussion isn’t just theoretical - the architecture shapes what GAIE can do and how it integrates with Gateway API. Attendees will leave with a clear decision framework for designing GW API extensions, and a deeper understanding of how architectural choices impact performance, complexity, and ecosystem alignment.
