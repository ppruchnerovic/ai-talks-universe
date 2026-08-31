---
id: B9h9ovW5H9U
title: "Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j"
slug: why-your-agents-need-decision-traces-not-just-documents
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Zach Blumenfeld"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-05-29T16:00:33Z
video_id: B9h9ovW5H9U
youtube_url: https://www.youtube.com/watch?v=B9h9ovW5H9U
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

**Zach Blumenfeld**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=B9h9ovW5H9U) · [Conference site](https://www.ai.engineer/)

## Description

A knowledge base tells a financial analyst agent the risk factors. A context graph tells it whether to reject or accept, because it also carries past decision traces, the reasoning behind them, and how similar cases resolved. Zach from Neo4j walks through how context graphs extend a standard RAG setup with three layers: short term conversation history, long term extracted entities, and reasoning traces that embed into vectors so structurally similar past decisions surface alongside semantically similar ones.

The fastest path in is `uvx create-context-graph`, a one-command scaffold that gives you a backend, frontend, demo data, and an MCP server. It ships with 22 built-in domains or generates a graph ontology from a custom domain you describe. The underlying `neo4j-agent-memory` package handles entity extraction through a spaCy to GLiNER to LLM pipeline with deduplication and merging baked in, and plugs into pydantic AI, LangGraph, Crew, Google ADK, and others.

Speaker info:
- https://www.linkedin.com/in/zachblumenfeld/
