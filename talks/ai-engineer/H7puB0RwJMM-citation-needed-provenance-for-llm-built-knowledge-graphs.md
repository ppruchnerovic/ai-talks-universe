---
id: H7puB0RwJMM
title: "Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI"
slug: citation-needed-provenance-for-llm-built-knowledge-graphs
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Daniel Chalef"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-07-23T00:00:00Z
video_id: H7puB0RwJMM
youtube_url: https://www.youtube.com/watch?v=H7puB0RwJMM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI

**Daniel Chalef**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=H7puB0RwJMM) · [Conference site](https://www.ai.engineer/)

## Description

An agent hands a doctor a clean, confident fact: the patient has a penicillin allergy. But that fact was synthesized from three sources, an EHR record, a lab report, and something the patient typed into an intake chatbot, and by the time it reaches the doctor, which one it came from is gone. You cannot just stamp a source ID on it, because the LLM merged entities and later data invalidated earlier facts, so the store keeps shifting under your pointer. Daniel Chalef's argument is that provenance for a knowledge graph an LLM builds has to be a graph itself.

In Graphiti, the open source framework behind Zep, sources become episodes and every derived fact links back to them, so tracing a fact to its origin is just a graph walk. Tag a source once and the tag follows every node and edge derived from it, which lets an agent keep only facts from verified clinical sources. Deletion is the same walk in reverse: a GDPR erasure removes a source, and a fact survives only if another source still supports it. Compliance gets an audit trail, and engineers get agents they can debug instead of black boxes.

Speaker info:
- https://x.com/danielchalef
- https://www.linkedin.com/in/danielchalef/
- https://github.com/getzep/graphiti

Timestamps:
0:00 - Why LLM synthesis destroys the paper trail
1:10 - Graphiti, Zep, and the provenance problem
1:47 - The failure mode: a penicillin allergy from three sources
2:53 - Why a source ID does not survive an LLM pipeline
4:20 - Provenance as a graph: tracing a fact is a walk
5:09 - Keeping lineage correct through merges and invalidation
6:06 - Metadata projection: tag a source once
7:25 - Mixed trust parents: allergy flags versus consent
8:57 - Deletion: GDPR erasure through the same edges
10:26 - Benefits: compliance, veracity, and debuggability
11:31 - Q&A: cost, dedup, and why not just markdown
