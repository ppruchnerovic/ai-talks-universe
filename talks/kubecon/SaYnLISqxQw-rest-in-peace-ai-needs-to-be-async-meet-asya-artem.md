---
id: SaYnLISqxQw
title: "REST in Peace: AI Needs to Be Async - Meet Asya - Artem Yushkovskiy, Delivery Hero"
slug: rest-in-peace-ai-needs-to-be-async-meet-asya-artem
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Meet Asya", "Artem Yushkovskiy"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:24:11Z
video_id: SaYnLISqxQw
youtube_url: https://www.youtube.com/watch?v=SaYnLISqxQw
tags: []
transcript: false
---

# REST in Peace: AI Needs to Be Async - Meet Asya - Artem Yushkovskiy, Delivery Hero

**Meet Asya, Artem Yushkovskiy**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=SaYnLISqxQw) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

REST in Peace: AI Needs to Be Async - Meet Asya - Artem Yushkovskiy, Delivery Hero

Modern AI isn’t just POST /predict anymore. It’s messy, long-running conversations between models, tools, services — with errors, timeouts and rate limits. At Delivery Hero, we’ve rethought the AI orchestration layer with message queues, actor-model microservices, and external state store for durable execution.

Here's the idea: every step is an async actor ("asya"). Video generator? One asya. Smart router? Another. Agents, tools, backend workers — dozens of specialized actors coexist in the cluster, each scaling from zero to whatever you need (thanks, KEDA!). The result: true composability, independent scalability, and no hidden bottlenecks.

Open-sourced as Asya, the framework is battle-tested in production and powers real AI workloads today. It also now includes native support for A2A (agent-to-agent) and MCP protocols to turn your AI pipelines into a distributed agent mesh.

Come see why async isn't an optimization — it's a paradigm shift for AI orchestration.
