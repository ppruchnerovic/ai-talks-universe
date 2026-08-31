---
id: KA5kPbdkK2E
title: "How Lovable self-improves every hour — Benjamin Verbeek, Lovable"
slug: how-lovable-self-improves-every-hour-benjamin-verbeek
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Benjamin Verbeek"]
channel: null
duration_min: 19
published_at: 2026-06-02T16:00:33Z
video_id: KA5kPbdkK2E
youtube_url: https://www.youtube.com/watch?v=KA5kPbdkK2E
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How Lovable self-improves every hour — Benjamin Verbeek, Lovable

**Benjamin Verbeek**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=KA5kPbdkK2E) · [Conference site](https://www.ai.engineer/)

## Description

Within the first hour of launching the vent tool, the agent filed 20 complaints about a silent file copy failure. The team checked: the tool worked fine. What the agent had caught was that filenames with a space in them silently failed to copy, a bug that never surfaced in logs. Benjamin Verbeek from Lovable built it a channel to complain directly to Slack when platform limitations block it, and the first thing it did was find a real production bug.

At 200,000 projects per day, Lovable runs two continuous improvement loops. The first detects sessions where a nontechnical user got stuck and then unblocked, clusters similar cases, and injects that context upstream; a holdout group measures actual project completion rates to prune stale entries when models or features change. The vent loop runs in parallel: the agent flags missing tools, broken platform behavior, and confusing docs as it works. Vent volume spikes turned out to be a reliable incident detector. A second agent now monitors the channel, deduplicates reports, and opens PRs automatically.

Speaker info:
- https://se.linkedin.com/in/benjamin-verbeek
- https://x.com/benjaminvrbk/
