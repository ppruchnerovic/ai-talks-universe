---
id: L2r6vLlLgs8
title: "Fighting AI with AI — Lawrence Jones, Incident"
slug: fighting-ai-with-ai-lawrence-jones-incident
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Lawrence Jones"]
channel: null
duration_min: 17
published_at: 2026-05-17T00:00:00Z
video_id: L2r6vLlLgs8
youtube_url: https://www.youtube.com/watch?v=L2r6vLlLgs8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Fighting AI with AI — Lawrence Jones, Incident

**Lawrence Jones**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=L2r6vLlLgs8) · [Conference site](https://www.ai.engineer/)

## Description

Incident's AI SRE runs hundreds of prompts per investigation across logs, metrics, traces, and code. When it produces a wrong root cause analysis, there is no tractable way for a human to read through the full trace and find where the reasoning went sideways. Lawrence Jones, founding engineer at Incident.io, describes the moment the team realized they needed AI to debug their AI.

The talk covers three patterns they built. A small CLI lets coding agents read and edit eval YAML files that had grown too large for agents to work with directly, enabling a red-green runbook where the agent writes a failing eval, fixes the prompt, and checks nothing else broke. Their bigger unlock was serializing every UI debugging view as a downloadable file system: drop it into a Claude Code session, describe the bad behavior, and the agent traces through the prompt hierarchy to tell you exactly which prompt to change. For fleet-scale analysis, 25 agents run in parallel each analyzing one investigation, then a second stage clusters the results to surface systemic failure patterns across customer accounts.

Speaker info:
- https://x.com/lawrjones
- https://www.linkedin.com/in/lawrence2jones/
