---
id: yWS0udrIOc8
title: "Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town"
slug: agentic-security-permissions-provenance-and-the-agent
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Steve Yegge"]
channel: null
duration_min: 23
published_at: 2026-07-20T00:00:00Z
video_id: yWS0udrIOc8
youtube_url: https://www.youtube.com/watch?v=yWS0udrIOc8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town

**Steve Yegge**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=yWS0udrIOc8) · [Conference site](https://www.ai.engineer/)

## Description

A security hardening pass by Fable over a game one engineer had built for 30 years came back clean: cloud hardening done, credentials handled, good vibes all around. Then Snyk ran over the same code and surfaced 241 vulnerabilities the agent never thought to look for. That gap is the center of Steve Yegge's talk, whose real title, he says, is not agentic security but be scared. A chief security architect at a big bank had already handed him the math: if everyone ships code 10 times faster and the rate of security defects holds steady, the vulnerable surface grows 10 times with it, and with models writing the code that rate does not hold steady, it gets worse.

The frightening part is not the familiar bugs like XSS that models still cheerfully write, it is the new attack surface. Slop squatting is the clean example: a model hallucinates a package name like graphy 123, someone uploads a real package under that exact name that does the expected thing plus a backdoor, and the build succeeds with the tests green. Yegge's partial answer follows from how models work. They do one thing well at a time, so asking for correctness and security in a single pass gets you a half job of both. Security becomes its own pass, the first one and the last one, with the agent handed real tools like Snyk and Chainguard to check its own work. And the window is closing: Five Eyes now measures the moment open source models can autonomously hack production systems in months, not years.

Speaker info:
- https://www.linkedin.com/in/steveyegge
- https://x.com/steve_yegge
- https://github.com/steveyegge/beads

Timestamps:
0:00 - The real title of this talk: be scared
1:38 - The bank architect's question: 10x speed, 10x defect surface
3:08 - New attack surfaces and slop squatting
4:51 - How Google surfaces bugs at the developer's fingertips
6:08 - Why security bugs have no half life
6:46 - Can the model just write secure code?
7:24 - Running Snyk on his own game: 241 vulnerabilities
8:14 - The rule of five and security as its own pass
9:32 - Software Survival 3.0: lazy models reach for tools
10:09 - Give the agent Snyk and Chainguard
12:03 - Five Eyes: months, not years
13:34 - Refresh your family code words
14:36 - The arms race you can start fighting now
15:30 - Q&A: what has surprised you in AI coding
17:28 - Q&A: Gas Town, beads, and running agents all night
19:13 - Q&A: adversarial agents watching your agents
20:58 - Q&A: prompt injection
