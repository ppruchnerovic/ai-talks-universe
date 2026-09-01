---
id: 7tMntN9kQbA
title: "A serverless resilient graph analysis platform built on Ray at ByteDance"
slug: a-serverless-resilient-graph-analysis-platform-built-on-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: "Anyscale"
duration_min: 34
published_at: 2023-02-09T01:49:28Z
video_id: 7tMntN9kQbA
url: https://www.youtube.com/watch?v=7tMntN9kQbA
youtube_url: https://www.youtube.com/watch?v=7tMntN9kQbA
tags: []
transcript: false
---

# A serverless resilient graph analysis platform built on Ray at ByteDance

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=7tMntN9kQbA) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

A serverless resilient graph analysis platform built on Ray at ByteDance

Graph processing aims to process super large-scale graphs and execute graph data analysis tasks, such as PageRank, TriangleCount, community detection, etc. Most graph processing systems are under in-memory architecture, which makes it hard to process real-world large graphs with a gigantic number of edges (e.g., 100 trillion edges) at a cheap cost. In addition, few graph processing systems really implement serverless fault tolerance capability, hindering wide adoption in production. Hence, at ByteDance, we proposed an enterprise-level Graph Analytics Platform (GAP) for graph computing and graph mining, named ByteGAP, to process super large graphs such as Douyin and TikTok.

ByteGAP is built on a serverless engine atop KubeRay to provide flexible cluster resource management, automatic deployment in the cloud, elasticity for scalability, and fault tolerance. It eases the maintenance and deployment effort and lowers the number of machines and memory consumption but supports much larger graphs by a hierarchical out-of-core design of DRAM/PMEM/SSDs on Ray clusters. Thanks to Ray's powerful abstraction of tasks/actors/GCS, we have built a Ray-based control plane for rank management, agent (actor) rendezvous, and stateful fault tolerance as an infrastructure component. It handles failures at node level, agent level, and worker level end-to-end with synergy that MPI can not fully cover. The Ray agents of dynamically assigned ranks manage worker processes of different languages as well as checkpoints in PMEM. It can relaunch agents and workers of specific ranks, load mutable status of vertices from vertex table in PMEM, and ensure that they are automatically recoverable from any iteration for any workers of arbitrary ranks.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
