---
id: YNJvm7t3yq8
title: "Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably"
slug: why-your-ai-ux-is-broken-and-it-s-not-the-model-s-fault
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Mike Christensen"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-05-17T15:30:06Z
video_id: YNJvm7t3yq8
youtube_url: https://www.youtube.com/watch?v=YNJvm7t3yq8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably

**Mike Christensen**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YNJvm7t3yq8) · [Conference site](https://www.ai.engineer/)

## Description

SSE ties a response stream to a single connection. The user refreshes the page, walks out of WiFi range, or opens a second tab and the in-progress response is gone. Abort and resume are mutually exclusive for the same reason: the only signal a client can send over a one-way pipe is closing it, so the agent cannot tell the difference between a cancel and a disconnect. Vercel's AI SDK documents this explicitly.

Mike Christensen from Ably makes the case for treating the session itself as a durable shared resource, decoupled from any individual connection, device, or agent instance. Clients subscribe to the session rather than to a request, so reconnects resume automatically, any tab or device has full visibility of live activity, and concurrent agents write independently without routing everything through an orchestrator. The demo shows all of this: multi-tab sync, a forced network disconnect that self-recovers, two agents running in parallel, and a handoff to a human support agent who joins the session mid-conversation with the full interaction history already visible.

Speaker info:
- https://x.com/christensencode
- https://www.linkedin.com/in/mikescottchristensen/

Timestamps:
0:00 Introduction to AI chat applications
0:51 Current implementation: Direct HTTP streaming and SSE
3:03 Three foundational capabilities for great AI products
4:34 Limitations of direct HTTP streaming
5:21 Introducing durable sessions
6:06 Resumability in streams
7:43 The conflict between SSE, resumability, and live control
9:13 Multi-device and multi-tab synchronization issues
11:12 Handling concurrent multi-agent architectures
12:54 Using Pub/Sub and Ably channels for durable sessions
14:12 Introducing Ably AI Transport SDK
15:34 Live demo of durable session capabilities
17:38 Handoff to human support agent
