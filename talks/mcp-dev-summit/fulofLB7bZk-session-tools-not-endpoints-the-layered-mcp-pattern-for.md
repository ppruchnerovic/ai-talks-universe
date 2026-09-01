---
id: fulofLB7bZk
title: "[Session] Tools, Not Endpoints: The Layered MCP Pattern for Task‑Centric Agents"
slug: session-tools-not-endpoints-the-layered-mcp-pattern-for
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit Europe 2025"
year: 2025
speakers: []
channel: "Agentic AI Foundation"
duration_min: 20
published_at: 2025-10-14T16:01:18Z
video_id: fulofLB7bZk
url: https://www.youtube.com/watch?v=fulofLB7bZk
youtube_url: https://www.youtube.com/watch?v=fulofLB7bZk
tags: ["mcp", "model context protocol", "mcp dev summit", "mcp summit", "mcp ai"]
transcript: false
---

# [Session] Tools, Not Endpoints: The Layered MCP Pattern for Task‑Centric Agents

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit Europe 2025` · `2025` · `20 min`

`#mcp` `#model context protocol` `#mcp dev summit` `#mcp summit` `#mcp ai`

[Watch the recording](https://www.youtube.com/watch?v=fulofLB7bZk) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

[Session] Tools, Not Endpoints: The Layered MCP Pattern for Task‑Centric Agents
🎤 Richard Moot, Technical Lead - Block, Inc.

LLMs should not be handed a single, all-in-one tool. They need scaffolding. In this talk, I will show a practical and repeatable way to design task-centric MCP tools by layering them around what humans actually try to do with your product, rather than around the raw API surface. The pattern is straightforward:Discovery (WHAT): Expose human and LLM-readable slices of your documentation or OpenAPI so the model can see what is possible.Planning (HOW): Translate intent into concrete calls, moving from a prompt to a sample request.Execution (DO): Make the HTTP call, and nothing more.We will walk through real examples, including the Square MCP server that handles more than 30 APIs and about 200 endpoints with just three tools: discovery, type-planning, and execute. You will leave with a checklist for refactoring any API into layered, reliable MCP tools, along with patterns for mapping tools to tasks and guardrails that reduce malformed calls and brittle prompts. If you already have typed SDKs and solid documentation, you are closer than you think. Let’s build tools that match human tasks and let the model do the deciding.

✨ MCP Developers Summit EU 2025
📅 2 Oct 2025
📍 London, UK
