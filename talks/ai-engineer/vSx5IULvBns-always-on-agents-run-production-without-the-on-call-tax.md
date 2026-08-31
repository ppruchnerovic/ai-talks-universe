---
id: vSx5IULvBns
title: "Always-on agents run production without the on-call tax — Justin Smith, Resolve AI"
slug: always-on-agents-run-production-without-the-on-call-tax
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Justin Smith"]
channel: "AI Engineer"
duration_min: 25
published_at: 2026-08-09T00:00:00Z
video_id: vSx5IULvBns
youtube_url: https://www.youtube.com/watch?v=vSx5IULvBns
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Always-on agents run production without the on-call tax — Justin Smith, Resolve AI

**Justin Smith**

`AI Engineer` · `AI Engineer` · `2026` · `25 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vSx5IULvBns) · [Conference site](https://www.ai.engineer/)

## Description

Someone drops a GitHub release tag into Slack and the agent decides on its own that this is a deploy worth watching. It reads what actually changed, works out which telemetry would expose trouble for that particular change, and writes a check plan for this release alone: checkout is replacing the currency service, so watch checkout latency and error rates, then follow the causal chain into the Kafka pipeline. None of the timing is hardcoded. It can decide to look again in an hour because this class of failure only surfaces intermittently, or come back in three days to ask whether the deploy is still healthy. Justin Smith is careful to say CI/CD already handles the baseline well. The gap is everything routed around it, the feature flags and infrastructure changes that ship with no monitoring at all and get caught only when an alert wakes somebody up.

The premise underneath is that around 70% of an engineer's time goes to running code rather than writing it, and coding agents made that worse by raising the volume of change flowing into production. Resolve's background agents are defined by three questions: when they run, on a schedule or an event stream or just a message; how they run, in the cloud inside a sandbox with its own file system, so closing your laptop changes nothing; and how they know what to do. The one Smith clearly enjoys most watches Slack channels and answers engineering questions without being addressed, staying quiet when it lacks confidence, and DMing him to confirm an answer before it replies in public. His sharpest point is that execution is the easy half. Loading a dashboard is execution. Deciding a metric smells wrong is production context, and building the knowledge system that keeps up with an environment changing faster every month is where the real work sits.

Speaker info:
- https://www.linkedin.com/in/justin-smith-7b1534a8/
- https://resolve.ai/events/behind-the-build/agents-for-engineering-workflows
