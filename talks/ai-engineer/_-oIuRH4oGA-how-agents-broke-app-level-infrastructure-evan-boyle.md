---
id: _-oIuRH4oGA
title: "How agents broke app-level infrastructure - Evan Boyle"
slug: how-agents-broke-app-level-infrastructure-evan-boyle
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Evan Boyle"]
channel: "AI Engineer"
duration_min: 14
published_at: 2025-06-03T22:22:28Z
video_id: _-oIuRH4oGA
url: https://www.youtube.com/watch?v=_-oIuRH4oGA
youtube_url: https://www.youtube.com/watch?v=_-oIuRH4oGA
tags: []
transcript: false
---

# How agents broke app-level infrastructure - Evan Boyle

**Evan Boyle**

`AI Engineer` · `AI Engineer` · `2025` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=_-oIuRH4oGA) · [Conference site](https://www.ai.engineer/)

## Description

LLMs have completely broken our assumptions about app-level workloads. Compared to querying a database, LLMs are extremely flakey and slow. In web 2.0, p99 latency was just a few hundred milliseconds - anything higher and the on call is getting paged.

But today any API that uses LLMs has a p1 latency of a couple of seconds. Yet, the infrastructure we build on top of hasn't caught up with these new assumptions. There isn't a single serverless provider that supports running code for more than a few minutes!

In this session we'll take about infrastructure patterns that used to be niche, but today require attention from anyone building on top of LLMs:

- Durable execution
- Long running workflows and APIs
- Durable execution
- Agent-scoped storage
