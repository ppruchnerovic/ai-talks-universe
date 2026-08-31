---
id: o6U_2vd967Y
title: "Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft"
slug: let-s-integrate-ai-agents-in-event-sourced-systems-divakar
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Divakar Kumar"]
channel: null
duration_min: 22
published_at: 2026-07-30T00:00:06Z
video_id: o6U_2vd967Y
youtube_url: https://www.youtube.com/watch?v=o6U_2vd967Y
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft

**Divakar Kumar**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=o6U_2vd967Y) · [Conference site](https://www.ai.engineer/)

## Description

A card gets declined and no one, including the customer, can say exactly why. That gray zone is where Divakar Kumar points his agents. In a payments and fraud system, a rule based engine and an ML model already score most transactions cleanly; the hard cases are the ambiguous ones that neither can resolve. His approach adds an agentic layer on top of an existing event sourced architecture rather than replacing it, so the bounded contexts already in the system, transaction, device, and account, become the context the agents reason over.

Events flow through change feeds into projections and a semantic layer that the agents read, communicating asynchronously through a message broker in a saga style loop. A risk analyzer agent, a second agent that reaches a verdict, and a third work the case while guarding against infinite loops and keeping memory short, all runnable serverless. The takeaway is architectural: event sourcing already carries the state and history an agent needs, so the cleanest way to add judgment to a production system is to layer agents onto the events you are already emitting.

Speaker info:
- https://www.linkedin.com/in/divakar-kumar/
- https://iamdivakarkumar.com

Timestamps:
0:00 - Introduction: adding agents to an existing system
1:20 - A declined transaction you can't explain
3:04 - Where rule based and ML systems fall short
5:40 - Handling the gray zone with agents
5:53 - Bounded contexts: transaction, device, account
8:24 - Event sourcing and change feeds
10:57 - Building the semantic layer
13:16 - Avoiding infinite loops
14:07 - The risk analyzer and verdict agents
15:24 - The saga orchestration loop
19:00 - Putting the architecture together
