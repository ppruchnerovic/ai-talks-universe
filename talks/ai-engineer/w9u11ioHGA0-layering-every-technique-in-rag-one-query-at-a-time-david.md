---
id: w9u11ioHGA0
title: "Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)"
slug: layering-every-technique-in-rag-one-query-at-a-time-david
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["David Karam"]
channel: "AI Engineer"
duration_min: 20
published_at: 2025-07-29T14:30:06Z
video_id: w9u11ioHGA0
url: https://www.youtube.com/watch?v=w9u11ioHGA0
youtube_url: https://www.youtube.com/watch?v=w9u11ioHGA0
tags: []
topics: ["RAG, retrieval & knowledge"]
transcript: false
---

# Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)

**David Karam**

`AI Engineer` · `AI Engineer` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=w9u11ioHGA0) · [Conference site](https://www.ai.engineer/)

## Description

Start with the simplest Search - in-memory embeddings with relevance ranking. End with the most complex planet-scale Search - 70+ corpus mix of token, embeddings, and knowledge graphs, all jointly retrieved, custom ranked, joint re-ranked, and then LLM-processed, at 160,000 queries per second in under 200msec.

This talk will be a fun “one query at a time” survey of all techniques in RAG in incremental complexity, showing the limits of each technique and what the next layered one opens up in terms of capabilities to handle ever-more complex queries in RAG. You’ll learn why queries like [falafel] are notoriously hard to Search over, why chunking your documents can be disastrous, how you can sometimes can get away with a simple bm25, and how some Search problems are so hard to solve that you’re better off punting the problem to the LLM or the UX. Brought to you by the team that worked on 50+ Search products, in the context of Google.com and custom Enterprise Search.

About David Karam
I'm David K. I love straddling the line between deep tech research and application development. I’ve spent a decade at Google as Product Director working on Search’s core AI and NLU systems, helping Search’s own version of “AI Engineers” develop magical applications. Around a year ago I left with my cofounder to start Pi Labs where we’re trying to bring that same spirit to the rest of the industry. Outside work I love to read, cook, and spend time in nature.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter

Timestamps:
00:00 Introduction and Context
01:41 Quality Engineering Loop and Mindset
04:09 In-Memory Retrieval
04:50 Term-Based Retrieval (BM25)
05:18 Relevance Embeddings (Vector Search)
06:15 Re-Rankers (Cross Encoders)
07:59 Custom Embeddings
09:40 Domain-Specific Ranking Signals
11:09 User Preference Signals
12:17 Query Orchestration (Fan Out)
14:26 Supplementary Retrieval
16:09 Distillation
17:14 Punting the Problem and Graceful Degradation
