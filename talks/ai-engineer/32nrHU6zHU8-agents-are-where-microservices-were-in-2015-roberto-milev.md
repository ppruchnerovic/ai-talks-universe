---
id: 32nrHU6zHU8
title: "Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan"
slug: agents-are-where-microservices-were-in-2015-roberto-milev
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-29T00:00:00Z
video_id: 32nrHU6zHU8
youtube_url: https://www.youtube.com/watch?v=32nrHU6zHU8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=32nrHU6zHU8) · [Conference site](https://www.ai.engineer/)

## Description

Tell a travel agent to book a flight whenever the fare drops below 200 dollars and something awkward follows. When it fires two weeks later, who made that purchase? Roberto Milev and Uday Kanagala keep returning to that blurring, because Navan sells travel and expense management and the answer decides what authorization even means. An agent may act on behalf of a user or under its own service account, and the old model of a user or a service principal does not survive contact with either. Their guardrails run before and after every tool call rather than at the edge.

The framing is that agents are where microservices sat in 2015, when the sensible advice was that if you can build a well structured monolith you probably should not reach for microservices. The same holds here for reaching past a single agentic loop. Navan runs one master agent that progressively loads skills, treating a skill as the unit of context, pluggable and testable on its own. Logs stop working when an agent emits this much thinking, so hooks intercept each tool call and emit the goal, the reasoning and a confidence score, which lets an inferred answer be routed to a human. Testing a nondeterministic system means scoring trajectories rather than asserting outputs. Cost remains genuinely unsolved.

Speaker info:
Roberto Milev:
- https://www.linkedin.com/in/robertomilev/
Uday Kanagala:
- https://www.linkedin.com/in/udaybhanuprasad

Timestamps:
0:00 - The microservices bandwagon, and what it taught
1:25 - A reference architecture starting to crystallize
2:34 - Runtime, and agents being stateful by nature
3:42 - Memory, from RAG to episodic
6:04 - Skills as the unit of context
7:16 - Why logs stop working for agents
8:24 - Hooks, traces, and confidence scores
9:32 - Testing something nondeterministic
10:44 - Scoring trajectories instead of outputs
13:04 - Who actually bought the flight
14:15 - One master agent, or many
15:29 - What is solved, and what is not
17:48 - Cost, replay, and emerging standards
