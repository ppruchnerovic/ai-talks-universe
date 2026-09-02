---
id: uFPAtKIN-FQ
title: "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri"
slug: exposing-agents-as-mcp-servers-with-mcp-agent-sarmad-qadri
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2025
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2025-06-11T00:00:00Z
video_id: uFPAtKIN-FQ
url: https://www.youtube.com/watch?v=uFPAtKIN-FQ
youtube_url: https://www.youtube.com/watch?v=uFPAtKIN-FQ
tags: []
topics: ["Agents & orchestration"]
transcript: false
---

# Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2025` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=uFPAtKIN-FQ) · [Conference site](https://www.ai.engineer/)

## Description

In this talk, we will show that agents can be represented as MCP servers, allowing them to be run from any MCP client (such as Claude, Cursor and other applications).

This is made possible with [mcp-agent](https://github.com/lastmile-ai/mcp-agent), a simple, composable framework to build agents using [Model Context Protocol](https://modelcontextprotocol.io/introduction).

## Overview

Currently "agentic" behavior exists only on the MCP client side – clients like Claude or Cursor use MCP servers, which are often simple tool APIs, to solve tasks.

However, if Agents are MCP servers themselves, then any MCP client can invoke, coordinate and orchestrate agents the same way it does with any other MCP server.

This paradigm shift enables:
1. **Agent Composition**: Build complex multi-agent systems over the same base protocol (MCP).
2. **Platform Independence**: Use your agents from any MCP-compatible client
3. **Scalability**: Run agent workflows on dedicated infrastructure, not just within client environments
4. **Customization**: Develop your own agent workflows and reuse them across any MCP client.

## Background

mcp-agent was inspired by 2 foundational updates that Anthropic introduced for AI application developers:

1. [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) - a standardized interface to let any software be accessible to AI assistants via MCP servers.

2. [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - a seminal writeup on simple, composable patterns for building production-ready AI agents.

`mcp-agent` puts these two foundational pieces into an AI application framework:

1. It handles the pesky business of managing the lifecycle of MCP server connections.

2. It implements every pattern described in Building Effective Agents, and does so in a _composable_ way, allowing you to chain these patterns together.

Now as MCP continues to grow adoption, we are exploring advanced agent architectures that allow for sophisticated workflows in simple ways.
