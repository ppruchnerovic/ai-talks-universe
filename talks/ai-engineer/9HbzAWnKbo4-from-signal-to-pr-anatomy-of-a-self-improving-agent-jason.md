---
id: 9HbzAWnKbo4
title: "From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize"
slug: from-signal-to-pr-anatomy-of-a-self-improving-agent-jason
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jason Lopatecki"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-07-24T00:00:00Z
video_id: 9HbzAWnKbo4
youtube_url: https://www.youtube.com/watch?v=9HbzAWnKbo4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize

**Jason Lopatecki**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9HbzAWnKbo4) · [Conference site](https://www.ai.engineer/)

## Description

Instead of getting paged at midnight and starting to dig, you wake up to an issue that has already been investigated: the traces pulled, the root cause found, and a pull request with the fix waiting for review. That is what Arize built with Signal, and Jason Lopatecki walks through the anatomy of it. The unlock is boring and specific: traces on a filesystem. A skill pulls the relevant production traces and logs down as files into the repo, right next to the code, sometimes ten megabytes of them, because coding harnesses like Claude Code are magical with files and hopeless with a dashboard.

From there the agent has the exact code path the software took, not a guess among a million branches, and can produce a real fix. You pick the harness, the sandbox, and the skills, and Arize can run it inside your VPC, because companies like Uber and Booking will not point production systems at an external model. The deeper shift is that observability stops being a dashboard you click and becomes the smoke a system throws off for agents to read, which is why you now log and trace ten times more, not less. He is honest about the limits: a one line fix is the easy case, bigger fixes still need a human to drive, and the job moves from responder to reviewer.

Speaker info:
- https://www.linkedin.com/in/jason-lopatecki-9509941/
- https://arize.com/author/jason-lopatecki/

Timestamps:
0:00 - Arize, its agent Alyx, and why v1 sucked
1:36 - Observability is changing: from dashboards to telemetry for agents
2:55 - The goal: systems that fix themselves
4:14 - Inverting the loop: the agent investigates first
6:08 - Traces on a filesystem, the key unlock
7:23 - From your laptop to sandboxes
8:13 - A real fix: the Alyx stream canceled bug
9:39 - Why you should trace ten times more
11:10 - Product demo: Signal, AX, and Phoenix
13:09 - Sandboxes, VPC, and why customers won't call out
16:20 - Q&A: why not just point Claude Code at your data?
18:04 - Q&A: where do the evals come in?
