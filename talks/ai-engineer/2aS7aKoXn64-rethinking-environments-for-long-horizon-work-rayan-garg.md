---
id: 2aS7aKoXn64
title: "Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software"
slug: rethinking-environments-for-long-horizon-work-rayan-garg
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rayan Garg"]
channel: null
duration_min: 21
published_at: 2026-08-01T00:00:06Z
video_id: 2aS7aKoXn64
youtube_url: https://www.youtube.com/watch?v=2aS7aKoXn64
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software

**Rayan Garg**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=2aS7aKoXn64) · [Conference site](https://www.ai.engineer/)

## Description

Everyone wants agents that handle long horizon work, but Rayan Garg starts with the awkward question of what long horizon even means. One popular answer measures the time horizon as the task length at which an agent crosses a success threshold, like the sixteen hour mark, which is a useful endpoint but a noisy one, since human time estimates vary and the same wall clock hides very different amounts of real difficulty. How you choose to measure this has an outsized effect on what you conclude about a model.

From there Theta Software's work is about designing the environments and verifiers that make those measurements honest. A task can be artificially stretched by forcing serial dependencies, or made genuinely hard when a bad early query cascades through everything after it, and as environments grow more complex, standardized evaluation gets harder and correctness is best verified from the final state rather than a judge's guess. Garg walks through collapsing a huge state space with sample trajectories, being careful that judges do not see information they should not, and reusing agents to sift artifacts like CI logs. The recurring principle is that long horizon progress lives or dies on environment and verifier design, not on the headline benchmark number.

Speaker info:
- https://x.com/RayanGarg
- https://www.linkedin.com/in/rayan-garg/

Timestamps:
0:00 - What does long horizon mean?
1:13 - Time horizon and the threshold metric
3:17 - Why the metric is noisy
4:20 - Measuring what actually matters
6:38 - Creating tasks and environments
7:42 - When a bad early step cascades
10:01 - Why standardized evaluation is hard
11:17 - Verifying from the final state
13:46 - Judges, tools, and reused agents
17:45 - Rubrics, QA, and careful grading
