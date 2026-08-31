---
id: zMiSRliEzv4
title: "Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog"
slug: self-driving-products-product-signals-to-pull-requests
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Joshua Snyder"]
channel: null
duration_min: 16
published_at: 2026-06-10T13:00:17Z
video_id: zMiSRliEzv4
youtube_url: https://www.youtube.com/watch?v=zMiSRliEzv4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

**Joshua Snyder**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zMiSRliEzv4) · [Conference site](https://www.ai.engineer/)

## Description

A rage click, a 2am error spike, a customer Slack message — today each sits until a developer notices, triages, tickets, and writes a fix. PostHog is building a pipeline that collapses that chain: signal arrives, a background agent groups it with related errors and session replays, researches the codebase, and opens a PR. You wake up to green PRs instead of dashboards.

Three lessons from building it: off the shelf embedding models cluster signals by structural similarity rather than meaning, so errors land next to errors and Slack messages land next to Slack messages — the fix is to embed LLM generated queries rather than the signals themselves. Specificity determines whether the agent produces a useful PR or just fixes something at random; error tracking is immediately actionable, Slack and session replay usually are not. And start with agents even when it looks expensive — run the same problem through an agent 100 times, find the patterns, then collapse the expensive step into a one shot call.

Speaker info:
- https://x.com/joshsny
-https://www.linkedin.com/in/joshsny/
