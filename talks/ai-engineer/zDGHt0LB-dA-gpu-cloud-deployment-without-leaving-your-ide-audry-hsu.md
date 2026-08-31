---
id: zDGHt0LB-dA
title: "GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod"
slug: gpu-cloud-deployment-without-leaving-your-ide-audry-hsu
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Audry Hsu"]
channel: null
duration_min: 20
published_at: 2026-06-09T00:00:00Z
video_id: zDGHt0LB-dA
youtube_url: https://www.youtube.com/watch?v=zDGHt0LB-dA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod

**Audry Hsu**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zDGHt0LB-dA) · [Conference site](https://www.ai.engineer/)

## Description

The iteration cycle before Flash: commit, push, build a Docker image, pull it from the registry, load it onto a server, allocate a GPU, then find out if it works. Audrey Hsu demos what replacing that with a single decorator looks like — add `@flash.endpoint` to an async Python function and it deploys to GPU cloud from your IDE, with hot reload so a model swap is one line of code rather than a container rebuild.

The second demo chains three models: Qwen 3 generates image prompts, DreamShaper renders them, Nano Banana 2 composes the results into a single photo. H100 pricing is $0.00116 per second, charged only while a worker is handling a request. RunPod's recommendation: start with pods while experimenting, switch to serverless when you need hundreds of workers autoscaling across data centers.

Speaker info:
- https://www.linkedin.com/in/audry-hsu/
