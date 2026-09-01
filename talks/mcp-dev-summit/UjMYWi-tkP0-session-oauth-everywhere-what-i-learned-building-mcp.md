---
id: UjMYWi-tkP0
title: "[Session] OAuth Everywhere: What I Learned Building MCP Clients, Servers, & the Gateway Between Them"
slug: session-oauth-everywhere-what-i-learned-building-mcp
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit Europe 2025"
year: 2025
speakers: []
channel: "Agentic AI Foundation"
duration_min: 24
published_at: 2025-10-13T04:00:40Z
video_id: UjMYWi-tkP0
youtube_url: https://www.youtube.com/watch?v=UjMYWi-tkP0
tags: ["mcp", "model context protocol", "mcp dev summit", "mcp summit", "mcp ai"]
transcript: false
---

# [Session] OAuth Everywhere: What I Learned Building MCP Clients, Servers, & the Gateway Between Them

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit Europe 2025` · `2025` · `24 min`

`#mcp` `#model context protocol` `#mcp dev summit` `#mcp summit` `#mcp ai`

[Watch the recording](https://www.youtube.com/watch?v=UjMYWi-tkP0) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

[Session] OAuth Everywhere: What I Learned Building MCP Clients, Servers, & the Gateway Between Them
🎤 Donnie Adams, Software Architect - Obot AI

The MCP specification references seven RFC standards in its authorization section. These seven standards, combined with the MCP spec, provide comprehensive details for authenticating and authorizing with remote MCP servers. But how well do they work together in practice? Where are the pitfalls?When I set out to build OAuth integration for MCP, I thought I understood the complexity. I quickly discovered there was much more to learn. Over the past several months at Acorn Labs, I've implemented OAuth across the entire MCP stack: clients that authenticate users, servers that validate tokens, and a gateway that orchestrates authentication between multiple MCP servers. Each component revealed valuable insights into the intersection of these standards and where the gotchas, sharp edges, and fuzzy boundaries lie.The challenges were illuminating: ensuring clients request the correct scopes across different OAuth implementations; handling scenarios where metadata URLs are omitted or not found; working with authorization servers that don't support dynamic client registration; and managing third-party token expiration in gateway architectures where downstream failures can disrupt user workflows.In this talk, I'll share the specific implementation challenges I encountered building all three OAuth components, the architectural decisions that streamlined our development, and the flexible patterns that kept everything working when clients and servers behaved differently than expected. You'll leave with practical guidance for implementing OAuth in your MCP projects and a realistic understanding of where specification meets real-world implementation.

✨ MCP Developers Summit EU 2025
📅 2 Oct 2025
📍 London, UK
