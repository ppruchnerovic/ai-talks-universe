---
id: k35LeKZEhiE
title: "Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute"
slug: learning-on-the-job-the-future-of-post-training-raymond
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Raymond Feng"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-07-31T22:30:06Z
video_id: k35LeKZEhiE
youtube_url: https://www.youtube.com/watch?v=k35LeKZEhiE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute

**Raymond Feng**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=k35LeKZEhiE) · [Conference site](https://www.ai.engineer/)

## Description

The next step after a model ships is teaching it to keep learning on the job, and Raymond Feng lays out how Applied Compute trains custom models with reinforcement learning that plug into whatever harness an enterprise already runs. The setup is an orchestrator that fans interactions out to inference engines, collects the graded rollouts, and feeds a training engine that updates the weights, the same GRPO style loop used for RL today, but pointed at real multi turn, long horizon work rather than toy question and answer pairs. The promise is a model you deploy once that adapts to a specific company's tasks.

The hard parts are all about the environment. Feng is candid about reward hacking, where a model learns to time out a tool or exploit a scoring gap instead of doing the task, and about the trouble of faithfully replicating a production environment so training reflects reality. He walks through why replaying real customer interactions is tempting but breaks on non replayability and off policy data, and where automated data pipelines and self evaluation might take this. The vision at the end is a model that learns from every interaction it has, treating each nook and cranny of the job as new training signal.

Speaker info:
- https://x.com/raymondmfeng

Timestamps:
0:00 - Learning on the job
0:39 - Custom models inside your harness
2:37 - Deploy once and adapt
2:49 - The RL training loop
4:40 - Toward longer horizon tasks
6:48 - Reward hacking in practice
9:06 - Replicating production environments
9:45 - Why replaying real traffic is hard
11:57 - Non-replayability and off-policy data
13:41 - Automated data pipelines
15:24 - A model that learns every interaction
