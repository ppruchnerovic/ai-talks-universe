---
id: VGN22pPpb-8
title: "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j"
slug: thinner-agents-on-a-smarter-substrate-the-ontology-based
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Emil Eifrem"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-07-22T17:00:38Z
video_id: VGN22pPpb-8
youtube_url: https://www.youtube.com/watch?v=VGN22pPpb-8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j

**Emil Eifrem**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VGN22pPpb-8) · [Conference site](https://www.ai.engineer/)

## Description

To automate opening a bank account, your agent needs to verify identity, so a team wires it to the DMV and a passport service and ships it. Then the next team builds the next agent and rediscovers, from scratch, where its data lives, across a hundred databases plus Snowflake, Databricks, and S3, whether it can trust the version, and whether it is even allowed to touch it. Every agent repeats that wiring, nothing updates when a source moves without a manual rewire, and no agent is smarter tomorrow than today. Emil Eifrem's fix is to make the agents thin and put the intelligence in a shared substrate underneath.

That substrate is an ontology based semantic layer with three parts. A business ontology names the real concepts, customers, accounts, checks, in the words people actually use, not f_name. A technical ontology catalogs every data source and its schema, with a mapping between the two. And execution traces record what each agent tried and whether it worked, so the layer learns bottom up: an agent that succeeded with the DMV lookup last time is more likely to reach for it next time. Discovery, trust, deduplication, and learning stop being every team's problem and become the substrate's.

Speaker info:
- https://x.com/emileifrem
- https://www.linkedin.com/in/emileifrem/

Timestamps:
0:00 - The account opening agent and its data sources
1:53 - The problem: every team rewires data from scratch
4:00 - Thin agents on a smarter shared substrate
4:37 - Pillar 1: a business facing ontology
5:26 - Pillar 2: a technical ontology and the mapping
6:19 - Pillar 3: execution traces that make it learn
8:01 - Solving discovery, trust, DRY, and learning
