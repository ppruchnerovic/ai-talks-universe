---
id: K0X9QDRkIdg
title: "Anthropic's Applied AI team on the Evolution of Agentic Surfaces"
slug: anthropic-s-applied-ai-team-on-the-evolution-of-agentic
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 31
published_at: 2026-08-11T00:00:00Z
video_id: K0X9QDRkIdg
youtube_url: https://www.youtube.com/watch?v=K0X9QDRkIdg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Anthropic's Applied AI team on the Evolution of Agentic Surfaces

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `31 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=K0X9QDRkIdg) · [Conference site](https://www.ai.engineer/)

## Description

Sonnet 4.5 developed what Anthropic's Applied AI team came to call context anxiety: approaching its context window limit, it would wrap work up early and stop with room to spare. They built context resets into the harness to compensate. Then Opus 4.5 shipped without the behavior, and the fix turned into pure overhead, adding latency and discarding cache it should have kept. That is the principle Gagan Bhat and Isabella Kai He build the whole session on: a harness encodes assumptions about what the model cannot do on its own, and those assumptions go stale as models improve.

The architectural consequence is decoupling the brain, meaning the agent loop, from the hands, meaning the tool execution environment. Both started in one container, so the model could not begin reasoning until setup finished and either half failing took the whole agent down. Splitting them lets reasoning start while the container builds in parallel, which they measured at 60% faster time to first token at P50 and over 90% at P95. It also changes failure into something recoverable: a dead sandbox is simply retried, and a dead brain resumes from a durable session log. That log ends up doing triple duty, providing observability, letting the harness read context slices back in after Claude discards them mid run, and feeding a periodic batch process they call dreaming that rewrites the agent's memory so the next day's sessions start smarter.

Speaker info:
Gagan Bhat (Anthropic):
- https://www.linkedin.com/in/gagan-bhat/

Isabella Kai He (Anthropic):
- https://x.com/IsabellaKHe
- https://www.linkedin.com/in/isabella-kai-he/

Timestamps:
0:00 - Who the Applied AI team is
1:52 - From simple questions to owning outcomes
2:45 - The Messages API and the hand rolled agentic loop
4:29 - Six production infrastructure problems
5:20 - The Claude Agent SDK
6:13 - What managed agents takes off your plate
7:02 - Harnesses encode assumptions that go stale
7:51 - Context anxiety, and the fix that outlived its need
9:34 - Designing for the model capabilities of tomorrow
10:25 - What long running agents demand
11:16 - Decoupling the brain from the hands
12:59 - Three primitives: agent, environment, session
13:51 - Reliability and the four session states
15:32 - Recovering discarded context from the session log
16:23 - What the developer still owns
17:14 - Demo: an SRE agent for a latency spike
18:58 - Defining the environment and its network limits
19:49 - Kicking off a session
20:38 - Root cause, and the observability trace
22:25 - Lesson one: keep credentials away from the agent
23:15 - Lesson two: where the latency went
24:58 - Lesson three: session logs as memory
25:47 - Lesson four: self hosted sandboxes and MCP tunnels
27:28 - Dreaming
29:08 - Outcomes and grader agents
30:49 - Harnesses as the limiting factor
