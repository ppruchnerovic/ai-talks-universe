---
id: aHhB3sjGjkI
title: "Agents Building Agents - Alfonso Graziano, Nearform"
slug: agents-building-agents-alfonso-graziano-nearform
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Alfonso Graziano"]
channel: "AI Engineer"
duration_min: 30
published_at: 2026-06-28T00:00:00Z
video_id: aHhB3sjGjkI
youtube_url: https://www.youtube.com/watch?v=aHhB3sjGjkI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agents Building Agents - Alfonso Graziano, Nearform

**Alfonso Graziano**

`AI Engineer` · `AI Engineer` · `2026` · `30 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=aHhB3sjGjkI) · [Conference site](https://www.ai.engineer/)

## Description

Building an AI agent for a real team is not a prompt problem, it is a systems problem. In this session we walk through a practical, production-minded workflow for building an agent using a coding agent, and designing the codebase so that this loop stays reliable as complexity grows.

The core pattern is two agents with different jobs. The coding agent is the builder: it writes and changes the agent’s codebase. The agent you are building is the product agent. It is the custom agent you ship for a client or for internal use.

A key example is self-healing evals. We maintain an eval suite that exercises the product agent across representative tasks. When an eval fails, the builder agent runs the eval, inspects the failure artifacts, proposes a targeted fix to the correct layer (context, tool contract, or code), and opens a PR with a short report explaining what changed and what is still missing. If the agent cannot safely resolve the failure, it escalates by requesting specific human input and explaining exactly why it is blocked.

Speakers:
- Alfonso Graziano (Nearform): Alfonso is a Software Engineer led by curiosity and passionate about new technologies
