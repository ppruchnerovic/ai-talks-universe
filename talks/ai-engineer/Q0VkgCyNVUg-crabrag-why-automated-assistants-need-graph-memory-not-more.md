---
id: Q0VkgCyNVUg
title: "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j"
slug: crabrag-why-automated-assistants-need-graph-memory-not-more
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Stephen Chin"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-07-22T00:00:00Z
video_id: Q0VkgCyNVUg
youtube_url: https://www.youtube.com/watch?v=Q0VkgCyNVUg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j

**Stephen Chin**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Q0VkgCyNVUg) · [Conference site](https://www.ai.engineer/)

## Description

Stephen Chin gave two copies of the same agent the same facts about his home network, one storing them as a vector database, the other as a graph. He asked both what was running end of life software exposed to the internet. The vector agent said it could not find specific details. The graph agent traced the connections and flagged his daughter's Minecraft server running an out of date OS, then found real open management ports he quietly patched after the demo. Same data, and only one of them could actually answer.

That gap is the whole talk. Most assistants, OpenClaw included, keep their memory as markdown files, which is why Chin's agents burn over 100,000 tokens a round loading everything in case some of it matters. It holds at small scale and breaks at large scale, because similarity in vector space is not a real relationship, so multi hop questions hallucinate. A graph stores entities and the edges between them, seeds the search with vectors, then traverses, so answers come back precise, explainable, and auditable. And if you do not know graphs, Claude writes Cypher better than he does.

Speaker info:
- https://x.com/steveonjava
- https://www.linkedin.com/in/steveonjava/
- https://www.oreilly.com/library/view/graphrag-the-definitive/9798341630147/

Timestamps:
0:00 - Meet Crab D and the agent memory problem
2:34 - Why markdown memory wastes tokens
4:43 - Skills are just markdown too
5:49 - Goose: memory as an MCP server
7:44 - Vector databases and why similarity is not a relationship
9:54 - Enter graphs: precise, explainable, auditable
11:38 - You do not need to be a graph expert, Claude writes Cypher
12:04 - The demo: a home lab digital twin, vector versus graph
13:23 - Live: finding end of life software on the network
15:30 - Live: finding exposed management ports
16:49 - Why large scale needs graph memory
18:05 - Resources: the GraphRAG book and GraphAcademy
