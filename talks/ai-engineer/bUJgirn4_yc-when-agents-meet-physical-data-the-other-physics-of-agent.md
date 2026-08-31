---
id: bUJgirn4_yc
title: "When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain"
slug: when-agents-meet-physical-data-the-other-physics-of-agent
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dmitry Petrov"]
channel: null
duration_min: 28
published_at: 2026-07-20T06:25:07Z
video_id: bUJgirn4_yc
youtube_url: https://www.youtube.com/watch?v=bUJgirn4_yc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain

**Dmitry Petrov**

`AI Engineer` · `AI Engineer` · `2026` · `28 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=bUJgirn4_yc) · [Conference site](https://www.ai.engineer/)

## Description

Ask an agent to find every night-time pedestrian frame across terabytes of dashcam video in S3. The first pass can cost thousands of dollars and run for hours or days. Once you’ve paid that cost, the agent’s favorite move - loop, inspect, re-derive - becomes the worst thing it can do.

Most agent intuition comes from a different physics: coding and business automation, where recompute is cheap, verification means re-running code, and state fits in context. That physics is real, useful, and everywhere. But like mechanics at cosmic or particle scale, those intuitions stop working when scale changes.

Large-scale data work is where the cracks start showing. OpenAI’s in-house data agent needed layers of context engineering to operate over 600 petabytes in a structured warehouse - and warehouses are still the forgiving version, with schemas, indexes, query engines, and cheaper ways to check the work.

Now move to the data behind physical AI: video, logs, and sensor data from robots, vehicles, labs, and factories. Petabytes will never fit in a context window. "Just verify it" may mean another expensive inference job. A follow-up question should recall what the system already paid to discover, not trigger another perception pass.

This talk is a tour of that other physics: what breaks, what inverts, and what replaces today’s harness assumptions when recompute is the enemy. Materialization becomes the default, recall becomes first-class, and the dataset - not the context window - becomes the unit of state. I’ll demonstrate the pattern live with Claude Code over raw data in S3, where follow-ups return in seconds and cents instead of reprocessing everything, with measured gaps on the order of millions between recompute and recall.

Same word: harness. Different physics.

Speakers:
- Dmitry Petrov (DataChain): Dmitry Petrov is the co-founder and CEO of DataChain, where he builds open-source infrastructure for AI agents to work with unstructured and physical-world data, and previously created DVC (Data Version Control).
X/Twitter: https://x.com/FullStackML
