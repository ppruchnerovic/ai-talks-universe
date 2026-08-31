---
id: FLUoowDJg4I
title: "How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face"
slug: how-i-automate-my-own-job-at-hugging-face-using-agents
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Niels Rogge"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-08-20T15:30:35Z
video_id: FLUoowDJg4I
youtube_url: https://www.youtube.com/watch?v=FLUoowDJg4I
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face

**Niels Rogge**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FLUoowDJg4I) · [Conference site](https://www.ai.engineer/)

## Description

Thousands of GitHub issues, opened automatically, have produced exactly two negative replies. Niels Rogge works on what he calls the Google Drive to the hub team at Hugging Face, whose job is noticing that a paper's weights are sitting on Dropbox or Zenodo where nobody will find them, then asking the authors to publish on the hub instead. Hundreds of papers land on arXiv every day, so he automated himself.

The useful part is that he built it twice, in opposite shapes, and explains why each time. The outreach half is a deterministic workflow: a model call at each step of the path he used to walk by hand, no agent framework at all, running nightly as a cron job on free GitHub Actions minutes, with tracing so he can inspect prompts, cost, and latency. He chose that because the prevailing advice when he built it was to avoid agents unless you genuinely need one. The follow up half, built recently, is the reverse. It is a fully autonomous loop whose main tool is bash, carrying one CLI, one skill, and a sandbox, fanned out so that every issue gets its own container. He is also candid that recipients are not told an agent wrote to them, on the grounds that it sends what he used to send himself and a disclosed bot tends to get closed unread.

Speaker info:
- https://x.com/NielsRogge
- https://www.linkedin.com/in/niels-rogge-a3b7a3127/
- https://nielsrogge.github.io/

Timestamps:
0:00 - The Google Drive to the hub problem
1:59 - Paper pages, metadata, and discoverability
3:41 - Why manual outreach does not scale
4:29 - The workflow he was running by hand
5:19 - Workflow or agent, and why it is not binary
7:03 - Nightly cron jobs, and tracing cost and latency
8:46 - The flood of replies, and automating follow up
9:36 - Switching to a fully autonomous loop
10:25 - Bash, one CLI, one skill, one sandbox
12:06 - A container per issue, fanned out
13:49 - What researchers actually reply
15:32 - Migrated models, and a 400 gigabyte dataset
18:06 - Open models, agents over workflows, and evaluation
