---
id: sAOBXCDiDOs
title: "MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc"
slug: mcp-apps-primitives-discovery-and-the-future-of-software
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Pietro Zullo"]
channel: null
duration_min: 29
published_at: 2026-07-05T03:12:17Z
video_id: sAOBXCDiDOs
youtube_url: https://www.youtube.com/watch?v=sAOBXCDiDOs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc

**Pietro Zullo**

`AI Engineer` · `AI Engineer` · `2026` · `29 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=sAOBXCDiDOs) · [Conference site](https://www.ai.engineer/)

## Description

Everyone in this room knows what MCP is, but I am sure not many people know what MCP Apps are, how they work, how to build them and distribute them. By the end of this talk you'll know everything you need to join the race!

MCP Apps are not just MCP servers with a UI bolted on. They're a full interaction layer: bidirectional, stateful, rendered by the host, with the model and the UI sharing live context.

This talk is structured around

**What MCP Apps actually are.** The architecture: how an App is declared via `ui://` resources, how the host renders it in a sandboxed iframe, how the JSON-RPC-over-postMessage transport works, and how state flows between the model and the UI.

**The primitives that make them real.** `ui/update-model-context`, the App pushing live state into the model's context window without a user message. `ui/message`, the App talking back into the conversation unprompted. App Tools, the model calling into the App's registered tool surface.

**A showcase of MCP Apps shipping today.** Concrete demos, not slides about what's possible. What early builders have figured out, what's hard, and what the interaction patterns look like in practice.

**Distribution and discovery.** How the stores work, how to submit, what the surface looks like across hosts, and what the install/discovery UX actually means for builders.

**Why companies will need to move** Any product that is used by humans through a UI will need an MCP App version, or it gets bypassed by all the people that are getting more and more used to do everything through agents.

As long as there are people using these systems, MCP Apps is the answer. For the rest, there is MCP.

Speakers:
- Pietro Zullo (Manufact, Inc): Pietro is the co-founder of Manufact (YC S25). Manufact created and maintains mcp-use, an MCP framework with more than 8M downloads across PyPI and npm, one of the leading MCP development frameworks today. Manufact is the cloud for MCP. You can think of Manufact / mcp-use as Vercel / Next.js, but vertical on MCP Apps and servers.
X/Twitter: https://x.com/pietrozullo
