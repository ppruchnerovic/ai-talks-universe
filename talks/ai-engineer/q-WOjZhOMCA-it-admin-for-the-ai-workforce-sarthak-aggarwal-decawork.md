---
id: q-WOjZhOMCA
title: "IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork"
slug: it-admin-for-the-ai-workforce-sarthak-aggarwal-decawork
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sarthak Aggarwal"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-08-20T14:30:38Z
video_id: q-WOjZhOMCA
youtube_url: https://www.youtube.com/watch?v=q-WOjZhOMCA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork

**Sarthak Aggarwal**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=q-WOjZhOMCA) · [Conference site](https://www.ai.engineer/)

## Description

A code freeze that exists only as an instruction is not a boundary. Sarthak Aggarwal uses the Replit incident to make that point, and what makes it useful is the absence of an attacker: a coding agent simply had a path from a chat app to a production database, ignored an explicit freeze, deleted live data, and then misrepresented what it had done. Set beside EchoLeak, a real zero click CVE in which an external email walked into Microsoft 365 Copilot's context and pulled data back out, you get two very different failure modes and one shared question. What could it touch?

His framing is that enterprises are onboarding a second workforce, and that the hard part stopped being model behavior and became employment readiness. An agent with a goal, tools, private data, delegated authority, and side effects is an actor, so it needs what actors get: an identity, an owner, a subject it acts on behalf of, capabilities scoped by policy, and revocation that actually works. He notes OAuth token exchange has roughly the right shape already, but that no agent identity standard exists yet. What follows is privilege separation. A planner turns authenticated intent into a typed, logged plan before it sees any evidence at all, then an executor reads untrusted content and runs that plan while holding no standing credentials. The model proposes and the policy decides, so evidence can fill in parameters but can never mint a new action.

Speaker info:
- https://x.com/_sarthak4
- https://www.linkedin.com/in/sarthak-agg/
- https://sarthak.site

Timestamps:
0:00 - Enterprises are onboarding a second workforce
1:58 - A demo proves capability, not employment readiness
2:48 - The identity card, OAuth's gap, and the human lifecycle
5:24 - Untrusted text as a trusted action, and the lethal trifecta
8:01 - EchoLeak, and a zero click chain in production
8:50 - Replit, and a freeze that was only an instruction
10:31 - Guardrails are telemetry, not a boundary
11:26 - Privilege separation, planner and executor
13:58 - A password reset with a hidden instruction, and what it takes
