---
id: lyL5QhgIOxc
title: "Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face"
slug: serving-2-million-models-without-melting-scaling-the
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Arek Borucki"]
channel: null
duration_min: 22
published_at: 2026-07-28T13:41:11Z
video_id: lyL5QhgIOxc
youtube_url: https://www.youtube.com/watch?v=lyL5QhgIOxc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face

**Arek Borucki**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lyL5QhgIOxc) · [Conference site](https://www.ai.engineer/)

## Description

Type llama into a catalog of 3 million public models and the result still has to feel instant. At 20,000 models any query is fast; at Hugging Face's scale, 14 million users and a million datasets on top, search becomes the hard part. Arek Borucki shows how the Hub keeps it quick: full text search on Apache Lucene, served through MongoDB Atlas, which stores only the metadata while the model artifacts sit in S3 so compute scales on its own. Regex ranking did not hold, so relevance now runs through one unified query with the $search operator, sorted by downloads, likes, and trending.

Underneath is a seven node MongoDB cluster where only the primary takes writes, with a hidden analytics node soaking up the heavy queries so production traffic never feels them. Keep queries light, push everything else elsewhere, and once the catalog outgrows a single primary, shard the data across nodes by key. The front end scales the same way: Kubernetes goes from 10 to 500 pods and CastAI adds machines underneath, and because HPA only watches CPU and memory, they scale on event loop utilization through KEDA, which sees the request queue HPA cannot.

Speaker info:
- https://x.com/_Aras_B
- https://www.linkedin.com/in/arekborucki/
- https://arekborucki.cloud/

Timestamps:
0:00 - Introduction: scaling the Hugging Face Hub
1:44 - The numbers: 14 million users, millions of models
3:57 - Why search at scale is the hard part
5:09 - Full text search on Apache Lucene
5:46 - Request flow: autoscaling, MongoDB Atlas, and S3
7:55 - How a search for "llama" works
10:11 - Ranking and Atlas Search with the $search operator
13:00 - The seven node cluster and a hidden analytics node
16:42 - Sharding the database
18:14 - Kubernetes autoscaling: 10 to 500 pods and CastAI
20:07 - Scaling on event loop utilization with KEDA
