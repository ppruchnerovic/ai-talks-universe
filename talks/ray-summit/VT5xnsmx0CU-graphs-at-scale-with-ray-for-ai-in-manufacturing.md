---
id: VT5xnsmx0CU
title: "Graphs at scale with Ray, for AI in Manufacturing"
slug: graphs-at-scale-with-ray-for-ai-in-manufacturing
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: null
duration_min: 33
published_at: 2023-02-09T03:11:27Z
video_id: VT5xnsmx0CU
youtube_url: https://www.youtube.com/watch?v=VT5xnsmx0CU
tags: []
transcript: false
---

# Graphs at scale with Ray, for AI in Manufacturing

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=VT5xnsmx0CU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Graphs at scale with Ray, for AI in Manufacturing

Graph models provide the best representation for data in many use cases in manufacturing, continuous and discrete, plus closely related business verticals such as pharma. This drives a growing demand for graph technologies applied in this domain. The core concept of bill of materials (BOM) linked to product data, linked to supplier networks, production planning, inventory data, linked with customer and sales data almost naturally translates into graphs. Meanwhile much the relevant input for AI in manufacturing is stored in documents, spreadsheets, or legacy data silos. NLP and deep learning applications help prepare such data for integration into graph models.

The graph space has transformed over the past few years: graph neural networks provide exciting new capabilities, graph visualizations augmented by GPU break through previous barriers, algorithms of mathematical graph theory can be applied at scales hardly doable before. There are popular graph query languages and the W3C standards for ontologies and axiomatic inference and validation, and probabilistic graphs. Unfortunately, these camps within graph space remain largely disjoint. An open source project 'kglab' provides integration paths for different kinds of graph work, while aligning with PyData tools. Manufacturing firms including Siemens, Bosch, and BASF began using this library. A follow up project leverages Ray to provide graphs at billion-node scale, for horizontal scale-out of graph compute in large industrial use cases.

This talk explores use cases for AI in Manufacturing, discussing where Ray can address critical bottlenecks at scale, and also helps augment work with NLP and deep learning. We'll consider the roles that Ray could play for more optimal graph technologies. Some points are counter-intuitive: for example, GNNs are quite useful, however the hard problems requiring graph algorithms at scale are often in data preparation (resolving ambiguity, detecting unwanted cycles, handling gaps and errors), which must occur long before training any GNN models. While there are numerous graph database vendors, few can handle scale, and their enterprise licensing costs often exceed the cloud computing costs for large clusters. Ray on K8s can be used to break through crucial limitations, allowing for open source integrations for managing large graphs within secure enterprise environments.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
