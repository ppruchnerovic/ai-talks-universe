---
id: 2WZsT-znFTQ
title: "Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI"
slug: guardians-of-the-state-an-air-gapped-ai-fortress-for
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rachna Srivastava"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-08-29T00:00:00Z
video_id: 2WZsT-znFTQ
youtube_url: https://www.youtube.com/watch?v=2WZsT-znFTQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI

**Rachna Srivastava**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=2WZsT-znFTQ) · [Conference site](https://www.ai.engineer/)

## Description

The fiber optic cable carrying data into California's financial fraud system has been cut in half. One end sits on the internet with a laser transmitter. The other end, inside the building, has only a receiver. There is no transmitter pointing outward, so data physically cannot leave. Rachna Srivastava's team chose that over a software firewall for a blunt reason: any configuration can be misconfigured, and a misconfigured secure system is an exploited one. Everything her group builds has to survive a defense attorney whose entire job is attacking it, which means every step must be explainable, reproducible and auditable years later.

They did not get there gracefully. The first build was the obvious one, an open model in an isolated environment with guardrails, and it collapsed within two hours. The diagnosis was not a weak model. They had treated it as a magic box rather than a data pipeline, so Kafka took ingestion and replay, Spark took cleaning, and the model was left to reason over data that had already been made sane. Her framing is that most AI data problems are data engineering problems wearing an AI mask. Running one frontier model for every task was making a neurosurgeon take everyone's blood pressure, so a router now sends over 80% of work to the smallest model that can do it, tripling throughput on the same GPUs.

Speaker info:
- https://www.linkedin.com/in/rachana-srivastava-ms-mba-78bab86
- https://dfpi.ca.gov/

Timestamps:
0:00 - When seeing and hearing stopped being proof
2:32 - Building for the courtroom, not the demo
3:44 - Why encryption and private endpoints were not enough
6:08 - Certifications as paper
7:22 - The first build, and two hours to collapse
8:29 - Kafka for spikes, ordering and replay
10:56 - Data engineering problems wearing an AI mask
12:01 - A key bolted to the server rack
13:13 - One frontier model doing every job
14:23 - Routing 80% of work to smaller models
15:38 - Learning without opening a hole
16:53 - A cable cut in half
18:05 - Time travelling to the moment of a decision
20:27 - Trust as a physical property
