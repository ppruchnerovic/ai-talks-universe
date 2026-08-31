---
id: bMjlRrWjdT0
title: "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash"
slug: ai-evals-for-cross-functional-teams-nachiket-paranjape
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 16
published_at: 2026-08-28T00:00:00Z
video_id: bMjlRrWjdT0
youtube_url: https://www.youtube.com/watch?v=bMjlRrWjdT0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=bMjlRrWjdT0) · [Conference site](https://www.ai.engineer/)

## Description

The people annotating DoorDash's eval data are not engineers, and they build their own annotation tools. Because the GenAI platform team went API first, strategy and operations staff can point a coding agent at those endpoints and vibe code whatever interface their use case needs, whether that is grading restaurant menus or reviewing images. The platform team stopped trying to anticipate every UI, and shipped stable APIs instead. Nachiket Paranjape and Swaroop Chitlur Haridas make the broader case that evals stopped being an engineering harness for them and became a cross functional job.

That reframing has an org chart attached. Strategy and operations set the quality bar, product managers turn it into rubrics, operations run the annotations, and engineering supplies telemetry, datasets and judges. Which group actually owns a judge prompt varies by team, and they treat that variation as a sign the org is still learning rather than a problem to standardize away. The loop underneath is deliberately plain: trace, sample down to something a human will really look at, annotate, promote a golden set, calibrate the judge against it, then monitor and go again. Judge calibration runs self serve through a UI, showing the original and optimized prompts side by side so a product manager can see what changed and decide whether to trust it. Per annotation cost fell sharply.

Speaker info:
Nachiket Paranjape:
- https://x.com/nmparanjape
- https://www.linkedin.com/in/nachiketparanjape/

Timestamps:
0:00 - The GenAI platform team, and its three forces
2:05 - Why eval became the fourth pillar
3:05 - UI first, then API first, then workflow first
4:01 - Evals as a team sport, not an engineering harness
4:57 - Who owns which part of quality
5:53 - The continuous loop: trace, sample, annotate, calibrate
7:42 - Telemetry and workflow as two surfaces
9:32 - Operators vibe coding their own annotation UIs
11:21 - Calibrating judge prompts, self serve
13:10 - Different teams, different prompt owners
14:04 - What it did to annotation cost
