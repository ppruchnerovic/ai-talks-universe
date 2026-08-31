---
id: s4r6nk5WsZw
title: "MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal"
slug: mcp-tasks-async-why-aren-t-any-agents-supporting-them
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Cornelia Davis"]
channel: "AI Engineer"
duration_min: 24
published_at: 2026-08-02T20:00:06Z
video_id: s4r6nk5WsZw
youtube_url: https://www.youtube.com/watch?v=s4r6nk5WsZw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal

**Cornelia Davis**

`AI Engineer` · `AI Engineer` · `2026` · `24 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=s4r6nk5WsZw) · [Conference site](https://www.ai.engineer/)

## Description

You invoke a tool and expect an answer, but real work takes time, and over that time connections drop, networks blip, and processes crash. Cornelia Davis, a distributed systems veteran who wrote the book on cloud native patterns, argues that this is exactly the gap the MCP tasks specification exists to close, and walks through why almost no agents support it yet. A task lets a tool run long, report progress, and pause for human input without losing its place, which means the interaction has to be durable: it survives the client disconnecting and picks up right where it left off.

She demonstrates it with an invoice processing flow, a dashboard tracking task state, and a step that waits for a human to submit input before the backend continues, then traces how the spec evolved from V1 to V2. The design she keeps returning to is a stateless core with the harder long running behavior layered on as an extension, RPC requests replaced by the server pushing updates, and life cycle state carefully mapped so clients know what to resume. Her honest takeaway is that just because you can open a long lived stateful connection does not mean you should, and that getting durable long running tasks right is what will finally let agents handle work that does not finish in a single call.

Speaker info:
- https://x.com/cdavisafc
- https://www.linkedin.com/in/corneliadavis/

Timestamps:
0:00 - What MCP tasks are, and why they're hard
1:29 - A distributed systems point of view
2:34 - A first look at a task running
4:03 - What a task actually allows
4:43 - Why long running work breaks
6:02 - Durability across disconnections
7:04 - Demo: invoice processing dashboard
9:10 - Waiting for human input
11:18 - What changed in tasks V1
12:35 - The stateless core
16:37 - Extensions and server pushed updates
20:09 - V2 and what you need to implement
