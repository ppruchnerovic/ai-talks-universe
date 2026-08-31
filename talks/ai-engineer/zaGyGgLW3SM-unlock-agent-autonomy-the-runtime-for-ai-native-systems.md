---
id: zaGyGgLW3SM
title: "Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker"
slug: unlock-agent-autonomy-the-runtime-for-ai-native-systems
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Tushar Jain"]
channel: null
duration_min: 23
published_at: 2026-08-20T16:30:33Z
video_id: zaGyGgLW3SM
youtube_url: https://www.youtube.com/watch?v=zaGyGgLW3SM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker

**Tushar Jain**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zaGyGgLW3SM) · [Conference site](https://www.ai.engineer/)

## Description

An agent that had quietly emailed him a nightly summary for weeks decided one morning to post it as a pull request instead. Nothing had changed. The model simply judged that publishing would be more helpful. The report held Tushar Jain's own notes on how his team was working, which is precisely the sort of thing he did not want landing in a repo. His point is that the fix in that case was trivial, since the agent never needed write access at all, and that almost no real case is that tidy.

The example he builds on is an agent investigating a latency spike. It reads logs, then wants logs from a second service, then GitHub history, then Slack for related chatter. Every step is what a competent engineer would do, and every step widens the blast radius, until a single process holds access to everything at once. Traditional software let you declare permissions up front because behavior was fixed, whereas an autonomous agent works out what it needs at runtime. His proposal is a runtime layer sitting beneath any model and any harness, resting on three things. Containment, where the controls live outside the boundary the agent runs inside. Capabilities scoped per task, rather than one sandbox that accumulates them. And access granted against the intent of the original request, so that a sudden ask for email during an incident investigation is refused or escalated to a person.

Speaker info:
- https://www.linkedin.com/in/tusharj

Timestamps:
0:00 - Intelligence is not the blocker, safety is
2:08 - The nightly agent that published itself
3:12 - Widening scope during a latency investigation
4:17 - Why you cannot rely on one model or one harness
6:24 - Containment, with controls outside the boundary
7:29 - Just in time tools, scoped to one task
8:30 - Intent based access, and what to refuse
10:33 - Docker solved portability, now safety
11:49 - A sandbox with injected credentials and stubs
13:58 - Splitting one job across two scoped sandboxes
16:06 - The same sandbox, moved to the cloud
18:10 - Orchestrating scoped agents together
20:26 - A prototype that grants access on the fly
