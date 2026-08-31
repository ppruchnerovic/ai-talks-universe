---
id: 17-YSUHo6Lk
title: "Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber"
slug: agentic-sdlc-at-uber-uday-kiran-medisetty-adam-huda-uber
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-08-21T00:00:00Z
video_id: 17-YSUHo6Lk
youtube_url: https://www.youtube.com/watch?v=17-YSUHo6Lk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=17-YSUHo6Lk) · [Conference site](https://www.ai.engineer/)

## Description

More than 70% of pull requests at Uber now come from local or cloud agents, and lines of code per engineer has doubled year over year. Uday Kiran Medisetty walks through the six pieces of infrastructure underneath that, and the constraint shaping all of them shows up in the first one: every model call in the company goes through a single gateway doing Spire identity, redaction of 20 plus PII types, and five specialized safety models, with that entire guardrail budget held under 100 milliseconds. It carries 100 million requests a day across 800 projects, each one attributable to a caller, team, and project.

Most of the rest is about not drowning agents in tokens. An MCP gateway crawls internal APIs into MCP servers, then projects them into a CLI so responses stay out of the context window, which cut fleetwide token use by more than 40%. A skills marketplace holds 2,500 entries behind lint checks and automated review, running 20,000 executions a day. A context graph of 150 node and edge types and 40 million entries replaces the 20 to 30 separate systems agents used to crawl for basic ownership and dependency facts. Adam Huda then takes one feature end to end, from a Slack thread to a draft PR that deliberately stops short of CI so that validation happens in the inner loop, comparing simulator screenshots against Figma specs before anything reaches a build queue. His closing point is that the bottleneck has moved to whether a thing should be built at all.

Speaker info:
Uday Kiran Medisetty:
- https://x.com/udaykiran
- https://www.linkedin.com/in/udaykiran/

Adam Huda:
- https://x.com/hudaman
- https://www.linkedin.com/in/thinktopdown/
- https://adamhuda.com

Timestamps:
0:00 - The numbers: 70% of PRs, twice the code per engineer
1:26 - The model gateway, and a 100 millisecond guardrail budget
3:51 - MCP gateway, and cutting the token tax
5:48 - Dev pods, agentified into pre-provisioned balloon pods
7:18 - A managed skills marketplace
8:39 - The context graph, 40 million entries
10:19 - Cortana across Slack, CLI, and web
11:34 - One feature end to end, starting from a Slack thread
13:28 - Minion, and stopping short of CI on purpose
16:01 - Maintenance as a managed loop
17:29 - The bottleneck is now whether you should build it
