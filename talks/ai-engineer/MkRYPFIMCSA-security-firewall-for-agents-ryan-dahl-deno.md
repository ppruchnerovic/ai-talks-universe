---
id: MkRYPFIMCSA
title: "Security Firewall for Agents — Ryan Dahl, Deno"
slug: security-firewall-for-agents-ryan-dahl-deno
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ryan Dahl"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-17T18:30:06Z
video_id: MkRYPFIMCSA
youtube_url: https://www.youtube.com/watch?v=MkRYPFIMCSA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Security Firewall for Agents — Ryan Dahl, Deno

**Ryan Dahl**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=MkRYPFIMCSA) · [Conference site](https://www.ai.engineer/)

## Description

Deno gives its incident response agents read and write access to production Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack, and it works. Agents now close incidents that used to wake a human up. Ryan Dahl's problem is what happens when one of those agents gets prompt injected through the support system it is wired into. He grants that Opus refuses to drop the users table no matter how hard you push it, then says the part that matters out loud: security cannot be wishful thinking that a model stays obedient. The agent is untrusted software, so the guard cannot live inside it.

Claw Patrol is their answer, an MIT licensed proxy that sits in front of the agent and parses every byte leaving it, below the HTTP layer, because the dangerous path frequently is not HTTP. An agent can spawn psql as a subprocess and tunnel to a production database through an EKS endpoint, and no MCP tool definition or HTTP rule will see it. Rules live in HCL, the Terraform configuration language, checked into git and unit tested against fixture requests, with Deno's own file running about a thousand lines. The proxy holds credentials so the agent never sees them, covering cookies, OAuth, and AWS SigV4, and can route an action to an LLM judge, a human in Slack, or both before it is allowed. The demo is Codex in yolo mode cheerfully obeying an order to delete the users table, and the proxy killing it at the Postgres wire protocol.

Speaker info:
- https://x.com/rough__sea
- https://github.com/ry
- https://tinyclouds.org/
- https://deno.com

Timestamps:
0:00 - Deno Deploy, incidents, and the pager
1:28 - Giving agents write access to production
2:47 - Opus refuses, and why that is not enough
3:28 - Prompt injection through the support system
4:05 - Every action is bytes on the wire
5:24 - The hard case: psql through an EKS endpoint
6:47 - Why credentials and ACLs are not sufficient
7:26 - Where MCP tool permissions break down
8:48 - The existing landscape of proxies and sandboxes
10:09 - Claw Patrol
10:50 - Writing rules in HCL
12:07 - Protocol plugins
12:52 - Demo: blocking a dropped users table
13:34 - The dashboard
14:14 - Approvals by LLM judge or by human
14:58 - Credential injection
15:38 - Running it over Tailscale or WireGuard
16:58 - Agents cannot police themselves
17:42 - Q&A: testing the rule file
18:22 - Q&A: does this get easier as models improve
