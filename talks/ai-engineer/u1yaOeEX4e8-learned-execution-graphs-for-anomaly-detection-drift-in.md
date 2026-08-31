---
id: u1yaOeEX4e8
title: "Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase"
slug: learned-execution-graphs-for-anomaly-detection-drift-in
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ritvik Pandya"]
channel: null
duration_min: 20
published_at: 2026-07-23T00:00:04Z
video_id: u1yaOeEX4e8
youtube_url: https://www.youtube.com/watch?v=u1yaOeEX4e8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Learned Execution Graphs for Anomaly Detection & Drift in APIs — Ritvik Pandya, JP Morgan Chase

**Ritvik Pandya**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=u1yaOeEX4e8) · [Conference site](https://www.ai.engineer/)

## Description

Traditional monitoring reported the system healthy: latency down, errors at zero. A mandatory processing step had been silently skipped, and nothing caught it except the graph. Ritvik Pandya's team at JP Morgan models each API request as a short lived execution graph, a DAG of the middleware steps it passes through, learned from telemetry at over 1,600 requests per second. Compare what actually ran against that learned graph and a skipped, reordered, or injected step stops hiding behind healthy averages.

The same graph localizes performance problems to the exact node instead of the whole endpoint. In production it flagged a 41x deviation at a single node that service level monitoring never saw, cutting root cause from hours to under 30 seconds. The talk separates a one off anomaly from real drift, a slow shift that needs a new baseline, and sorts drift into structural, volume, and behavioral, using per node baselines and KL divergence rather than one threshold for every request. The payoff is a cheap tier one check that only escalates when the graph says something actually changed.

Speaker info:
- https://www.linkedin.com/in/ritvik-pandya/

Timestamps:
0:00 - Execution graphs for anomaly and drift detection
1:07 - What a short lived execution graph is
3:28 - Tiered checks and per client baselines
5:23 - The method: baseline, deviation, localize, act
6:16 - Localizing a slow node, and how the system is trained
7:33 - Anomaly versus drift
8:55 - The three kinds of drift: structural, volume, covariate
12:46 - The pipeline: from telemetry to gradual rollout
13:54 - Hot path versus recon, and worked examples
15:21 - Tuning it: delayed events, sampling, cold starts
17:09 - Results and lessons
