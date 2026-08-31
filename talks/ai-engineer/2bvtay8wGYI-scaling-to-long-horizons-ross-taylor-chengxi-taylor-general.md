---
id: 2bvtay8wGYI
title: "Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning"
slug: scaling-to-long-horizons-ross-taylor-chengxi-taylor-general
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-07-31T21:30:06Z
video_id: 2bvtay8wGYI
youtube_url: https://www.youtube.com/watch?v=2bvtay8wGYI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=2bvtay8wGYI) · [Conference site](https://www.ai.engineer/)

## Description

Ross Taylor opens with some history: back in 2022 he worked on Galactica, an early large model for science that briefly crossed the Rubicon on curated high quality data and intermediate reasoning tokens before the reaction overshadowed the work. That obsession, optimizing what happens between the question and the answer, is where this talk on long horizon reinforcement learning picks up. He and Chengxi Taylor of General Reasoning treat long horizon less as a benchmark and more as a mindset: if you want agents that stay coherent over hours, you have to be patient about signal and deliberate about how you spend tokens.

The mechanics they walk through are the ones that make long rollouts trainable. Value models reduce variance and help with credit assignment, bootstrapping pulls signal out of sparse rewards, and the real constraint becomes the tradeoff between off policy staleness and GPU utilization as sequences get longer. They make it concrete with a task where frontier models were handed real money to trade football matches and did poorly, exposing how little the environment was actually simulated. The takeaway is that scaling to long horizons demands better environments and simulation, not just bigger context windows, and they point listeners to openreward.ai to go deeper.

Speaker info:
- Ross Taylor (General Reasoning):
- https://x.com/rosstaylor90
- https://www.linkedin.com/in/rosstaylor90/
- https://rossjtaylor.com
- Chengxi Taylor (General Reasoning):
- https://x.com/chengxitaylor
- https://www.linkedin.com/in/chengxi-taylor/
- https://www.chengxitaylor.com/

Timestamps:
0:00 - Introduction and a look back
1:57 - The Galactica story
5:15 - Curated data and thinking tokens
8:09 - What got RL cooking
9:12 - Long horizon as a mindset
10:16 - Why value models help
11:08 - Credit assignment and bootstrapping
12:38 - Trading football matches for real money
13:44 - Why models struggled
14:36 - Off policy staleness versus GPU use
16:18 - openreward.ai and what's next
