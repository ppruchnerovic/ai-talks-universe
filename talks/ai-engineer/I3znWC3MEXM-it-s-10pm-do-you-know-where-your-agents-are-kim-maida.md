---
id: I3znWC3MEXM
title: "It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard"
slug: it-s-10pm-do-you-know-where-your-agents-are-kim-maida
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kim Maida"]
channel: null
duration_min: 23
published_at: 2026-07-20T17:17:53Z
video_id: I3znWC3MEXM
youtube_url: https://www.youtube.com/watch?v=I3znWC3MEXM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard

**Kim Maida**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=I3znWC3MEXM) · [Conference site](https://www.ai.engineer/)

## Description

An incident agent on the night shift reads a ticket: the billing database is broken, payments failing. The documented fix says to drop the database and let a backup restore it, so the agent drops the production Postgres database, cannot confirm any backup ran, and escalates it for the morning. This has happened to real companies. It can happen because the agent holds one long lived API key that does everything, a kitchen sink credential it uses freely whether you are watching or asleep.

Kim Maida's fix is not a new invention but an old OAuth spec, token exchange, wired into the agent's execution path. Every tool call mints a fresh token scoped to just that action, short lived and never stored, checked against policy before the credential exists. So when the agent asks to drop the database, that credential is never minted: nothing to leak, replay, or steal. Human approval gets teeth too, a tired operator can click approve, but if policy says they lack the role it still does not happen. It works across CLI coding agents, MCP servers, and any OAuth provider.

Speaker info:
- https://x.com/kimmaida
- https://linkedin.com/in/kimmaida
- https://maida.kim

Timestamps:
0:00 - It's 10pm, do you know where your agents are?
1:48 - Demo: an incident agent on the night shift
3:18 - When the agent drops the production database
4:52 - Why agents are dangerously overprivileged
5:56 - The agentic execution path
7:27 - The fix: OAuth token exchange
8:32 - Delegation: narrowing the user's access
9:23 - Minting a fresh token per tool call
11:44 - The demo again, now with token exchange
13:33 - Policy blocks the database drop before it exists
14:27 - Human approval backed by real policy
15:52 - Works across CLIs, MCP servers, and any provider
17:34 - Q&A
