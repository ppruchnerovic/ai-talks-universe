---
id: FvxY8oPoI8o
title: "Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean"
slug: preferences-over-benchmarks-model-routing-archana-kamath
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 16
published_at: 2026-08-22T15:30:18Z
video_id: FvxY8oPoI8o
youtube_url: https://www.youtube.com/watch?v=FvxY8oPoI8o
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FvxY8oPoI8o) · [Conference site](https://www.ai.engineer/)

## Description

Two terminals run the same prompt, build me a spinning wheel app. On the left every request goes to a single premium model. On the right they go through a router that picks a model per task. Both finish at about the same time with comparable output, and by then the router's session has cost 8 cents against 25. The gap widens with every prompt after that. Archana Kamath and Tyler Gillam use it to argue that picking a model by climbing a leaderboard is the wrong instinct, because there is no single best model, only the right one for a given request.

What makes a model right is a mix no public leaderboard encodes: the task itself, the system prompt and tools around it, the cost you are willing to spend, the latency the use case needs, and what the end user actually wants. Their router takes those as preferences you declare, in natural language or as decision tree rules, then honors them per request. It runs on a purpose built mixture of experts model that decides in under 200 milliseconds, costs nothing extra, and is open sourced along with the proxy in front of it. Gillam then shows the part that separates it from a vibe check, an evaluation scoring the router at 90% correctness against 95% for the single premium model while using far fewer tokens and returning faster. Routing is the foundation layer, with evaluation, caching and personalization built on top.

Speaker info:
- https://www.linkedin.com/in/tdgillam

Timestamps:
0:00 - Why the one model habit is breaking
2:42 - There is no single best model
4:21 - A router you can customize and evaluate
6:57 - Configuring tasks, model pools and failover
7:48 - Side by side in the playground
9:29 - Proving it with an evaluation
10:18 - Two coding agents, and the session cost gap
13:49 - Under 200ms, open sourced, no code changes
14:43 - Evaluation, caching, personalization
