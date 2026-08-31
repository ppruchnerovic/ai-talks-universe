---
id: YBYUvGOuotE
title: "MCP = Mega Context Problem - Matt Carey"
slug: mcp-mega-context-problem-matt-carey
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Matt Carey"]
channel: "AI Engineer"
duration_min: 23
published_at: 2026-04-25T17:00:06Z
video_id: YBYUvGOuotE
youtube_url: https://www.youtube.com/watch?v=YBYUvGOuotE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# MCP = Mega Context Problem - Matt Carey

**Matt Carey**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YBYUvGOuotE) · [Conference site](https://www.ai.engineer/)

## Description

The best MCP server is the one you didn't have to build.

At Cloudflare we have a lot of products. Our REST OpenAPI spec is over 2.3 million tokens. When teams started building MCP servers, they did what everyone does: cherry-picked important endpoints for their product, wrote some tool definitions and shipped a separate service that covered a small fraction of their API.

This was driven by a fundamental context limit of the end users' agent. And tools use a bunch of context just to describe themselves. MCP felt like a Mega Context Problem (and a separate service to maintain).

I think we got it all wrong.

The context limit is not an MCP problem. It's an agent problem. Tools should probably be discovered on demand and clients are coming around to this. But maybe we can also do it on the server?

CLIs get this for free, self-discoverable and documented by design. APIs just need a little help.

This talk will cover some of the techniques we've been exploring at Cloudflare, such as codemode and tool search, to make complete APIs accessible to agents through MCP.

I'll also cover some of the work we are doing with the MCP Typescript SDK to make stateless servers the default.

Speaker info:
- https://github.com/mattzcarey
- https://www.linkedin.com/in/mattzcarey/
- https://x.com/mattzcarey
