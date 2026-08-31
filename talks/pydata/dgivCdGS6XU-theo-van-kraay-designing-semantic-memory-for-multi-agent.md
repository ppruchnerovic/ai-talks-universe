---
id: dgivCdGS6XU
title: "Theo van Kraay - Designing Semantic Memory for Multi-Agent Systems with Python | Pydata London 26"
slug: theo-van-kraay-designing-semantic-memory-for-multi-agent
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Theo van Kraay"]
channel: null
duration_min: 46
published_at: 2026-06-15T15:54:10Z
video_id: dgivCdGS6XU
youtube_url: https://www.youtube.com/watch?v=dgivCdGS6XU
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Theo van Kraay - Designing Semantic Memory for Multi-Agent Systems with Python | Pydata London 26

**Theo van Kraay**

`PyData` · `PyData` · `2026` · `46 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=dgivCdGS6XU) · [Conference site](https://pydata.org/)

## Description

Theo van Kraay - Designing Semantic Memory for Multi-Agent Systems with Python

Multi-agent GenAI systems don’t fail because models lack intelligence, they fail because they lack memory.

As LLM applications move from demos to production, semantic memory becomes the defining systems challenge. Agents must remember user preferences, share context across roles, preserve conversational state across sessions, and evolve over time, all without exploding token costs or losing observability.

In this talk, I’ll explore semantic memory as a data engineering problem rather than a prompt engineering trick. Drawing on real-world experience from the Azure Cosmos DB engineering team, we’ll examine how to design layered memory for multi-agent systems in Python: short-term conversational state, episodic event logs, declarative and procedural memory, and retrieval-driven personalization.

Using a practical multi-agent travel planner built with LangGraph, we’ll implement patterns such as session-level versus per-turn persistence, hybrid retrieval design (structured filters plus semantic signals), memory lifecycle management (write, retrieve, summarize, supersede, expire), and checkpointed workflows for reproducibility and debugging.

You’ll leave with practical design heuristics for building agent systems that become more reliable, more efficient, and more explainable over time.

All demonstrations will be in Python and applicable to production-scale systems.

This session focuses specifically on semantic memory architecture as the critical systems layer in production-grade multi-agent AI applications.

From my role on the Azure Cosmos DB engineering team, I’ve worked with teams building large-scale agentic systems that must support multi-tenancy, personalization, long-lived conversational state, and operational observability. A consistent lesson is that orchestration frameworks coordinate agents, but memory design determines whether the system behaves coherently over time.

The talk will cover:

A practical taxonomy of agent memory: short-term state, episodic logs, declarative knowledge, and procedural memory
Modeling conversations as append-only event streams versus mutable session documents
Designing retrieval-aware memory stores that combine structured filtering with semantic signals
Memory lifecycle management: summarization spans, supersession flags, retention windows, and TTL-based compaction
Checkpointed agent workflows for traceability and debugging
Multi-tenant memory partitioning strategies
Cost tradeoffs between growing context windows and durable storage
A live Python-based multi-agent travel planner (built with LangGraph and backed by Azure Cosmos DB) will demonstrate these patterns in practice, including MCP-based memory tools that separate reasoning from storage concerns.

The goal is to provide PyData attendees with a concrete systems framework for thinking about semantic memory, not as an afterthought to prompting, but as a first-class data architecture problem at the intersection of distributed systems and applied AI.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
