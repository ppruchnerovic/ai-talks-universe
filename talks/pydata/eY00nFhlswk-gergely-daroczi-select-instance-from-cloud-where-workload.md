---
id: eY00nFhlswk
title: "Gergely Daroczi - SELECT instance FROM cloud WHERE workload = ? ORDER BY cost | Pydata London 26"
slug: gergely-daroczi-select-instance-from-cloud-where-workload
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Gergely Daroczi"]
channel: "PyData"
duration_min: 34
published_at: 2026-06-15T15:54:11Z
video_id: eY00nFhlswk
youtube_url: https://www.youtube.com/watch?v=eY00nFhlswk
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Gergely Daroczi - SELECT instance FROM cloud WHERE workload = ? ORDER BY cost | Pydata London 26

**Gergely Daroczi**

`PyData` · `PyData` · `2026` · `34 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=eY00nFhlswk) · [Conference site](https://pydata.org/)

## Description

Gergely Daroczi - SELECT instance FROM cloud WHERE workload = ? ORDER BY cost_efficiency

Choosing a cloud instance type for a DS/ML/AI workload is still largely a heuristic exercise. While public pricing and hardware specifications are available, they are fragmented, inconsistently structured, and challenging to compare across cloud providers -- especially once real workload performance is taken into account.

In this talk, we present Spare Cores Navigator, a Python-queryable benchmark dataset that covers thousands of cloud server types from multiple vendors, with standardized performance and cost-efficiency metrics. We demonstrate how instance selection can be expressed as a simple data query, e.g. filtering by workload characteristics, hardware or compliance constraints, and budget, then ranking candidates by price-performance.

Selecting a cloud instance for DS/ML/AI workloads is typically done using heuristics, vendor guidance, or trial-and-error. While cloud providers publish pricing tables and hardware specifications, this information is fragmented, inconsistently structured, and challenging to compare across vendors – especially once real workload performance is considered.

This talk introduces Spare Cores Navigator, a vendor-independent, open-source, Python-based ecosystem that treats cloud instance selection as a data problem. The project maintains a continuously updated benchmark dataset covering thousands of server types across multiple cloud providers, with standardized hardware metadata, performance measurements, and cost-efficiency metrics across over 500 workloads.

We describe how the dataset is built by automatically discovering and provisioning cloud instances at scale using public GitHub Actions to run hardware inspection tools and a diverse benchmark suite. This includes general CPU performance, memory bandwidth, compression algorithms, cryptographic workloads, web serving, and data store performance, as well as DS/ML-specific benchmarks such as gradient-boosted model training and LLM inference on CPUs and GPUs.

The main focus of the talk is demonstrating practical use cases for server type selection by querying the dataset under different workload characteristics, compliance and budget constraints, and optimization goals – such as minimizing cost-efficiency trade-offs or reducing environmental impact.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
