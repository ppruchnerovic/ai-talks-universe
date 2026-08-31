---
id: xIt_mTQp6mY
title: "Loop Engineering from First Principles — Kyle Mistele, HumanLayer"
slug: loop-engineering-from-first-principles-kyle-mistele
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kyle Mistele"]
channel: null
duration_min: 18
published_at: 2026-07-25T20:41:40Z
video_id: xIt_mTQp6mY
youtube_url: https://www.youtube.com/watch?v=xIt_mTQp6mY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Loop Engineering from First Principles — Kyle Mistele, HumanLayer

**Kyle Mistele**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=xIt_mTQp6mY) · [Conference site](https://www.ai.engineer/)

## Description

A coding agent will happily hand you a 40,000 line pull request that nobody can review and that quietly does the wrong thing. Kyle Mistele's argument is that the fix is not a better prompt but a better loop, borrowed from control theory: a thermostat senses the error between where a system is and where you want it, emits a control signal, and measures again, over and over. Infrastructure as code already approximates this. The point is to design agent loops the same way, so each iteration makes a small, readable change you can actually verify, instead of one giant diff you have to trust.

The working example is migrating a codebase one procedure at a time. A sensor, often just Grep or a structural search, finds the smallest unmigrated piece, a controller picks what to work on next, and an actuator agent makes the change against golden patterns defined by hand, gated by deterministic CI like a single loop iteration in CircleCI. The loop tracks its own PRs in version control, refuses to stack a new change while an earlier one is still open, and keeps improving the code incrementally, even while the team is away.

Speaker info:
- https://x.com/0xBlacklight
- https://www.linkedin.com/in/kyle-mistele
- https://blacklight.sh

Timestamps:
0:00 - Introduction: the 40,000 line PR problem
1:55 - Why more code is not the goal
3:37 - Is the generated code any good?
4:43 - Control loops from control theory
5:49 - Infrastructure as code and Ralph loops
7:06 - Applying control loops to coding
8:35 - Migrating a codebase one procedure at a time
10:40 - Tracking the loop in version control
12:35 - The actuator agent and golden patterns
13:51 - Wiring the loop into CI
15:44 - Avoiding stacked PRs and scaling the controller
