---
id: FB-MLPhL9Ms
title: "The maturity phases of running evals — Phil Hetzel, Braintrust"
slug: the-maturity-phases-of-running-evals-phil-hetzel-braintrust
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Phil Hetzel"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-05-27T13:00:06Z
video_id: FB-MLPhL9Ms
youtube_url: https://www.youtube.com/watch?v=FB-MLPhL9Ms
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The maturity phases of running evals — Phil Hetzel, Braintrust

**Phil Hetzel**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FB-MLPhL9Ms) · [Conference site](https://www.ai.engineer/)

## Description

Most teams approach evals like unit tests and try to cover every possible failure. Phil Hetzel from Braintrust argues that is the wrong frame: enumerate your known failure modes, cover those specifically, and ship. The goal is a flywheel where production traces surface what is going wrong, feed back into offline experimentation, and guide the next improvement.

The session walks four maturity stages: vibe checking with documented human justifications not just thumbs up or down, LLM as judge built from those justifications at scale, then the hard part, tool calls that touch external systems. Context gathering tools are manageable. CRUD tools are not, because you have to represent the state of external systems at the exact moment the original trace ran. Timestamp queries against a vector database and injecting captured system state directly into the trace are two approaches for getting there.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/
