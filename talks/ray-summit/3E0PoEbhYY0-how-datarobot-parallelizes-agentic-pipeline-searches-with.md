---
id: 3E0PoEbhYY0
title: "How DataRobot Parallelizes Agentic Pipeline Searches with Ray + syftr | Ray Summit 2025"
slug: how-datarobot-parallelizes-agentic-pipeline-searches-with
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 16
published_at: 2025-12-01T19:44:58Z
video_id: 3E0PoEbhYY0
url: https://www.youtube.com/watch?v=3E0PoEbhYY0
youtube_url: https://www.youtube.com/watch?v=3E0PoEbhYY0
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: false
---

# How DataRobot Parallelizes Agentic Pipeline Searches with Ray + syftr | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=3E0PoEbhYY0) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Mark Steadman from DataRobot shares how syftr—a new framework for optimizing agentic and non-agentic LLM pipelines—uses Ray to perform massive multi-objective search across extraordinarily large configuration spaces, enabling the design of fast, accurate, and cost-efficient generative AI workflows.

He begins by outlining the complexity of building high-quality agentic pipelines. These workflows require careful selection and tuning of components such as vector databases, embedding models, chunkers, retrievers, synthesizing LLMs, verifiers, rewriters, and rerankers—each with interconnected hyperparameters and tradeoffs among latency, accuracy, and cost. As real-world constraints tighten, manual optimization becomes infeasible.

Mark introduces syftr, which performs efficient, distributed, multi-objective search across a vast configuration space (~10²³ possible flows). Using advanced Bayesian Optimization, syftr discovers Pareto-optimal pipelines that jointly optimize cost and accuracy. A novel early-stopping mechanism prunes suboptimal candidates, dramatically reducing compute overhead.
Across benchmarks, syftr finds workflows that are ≈9× cheaper than highly accurate baselines, while retaining most of their accuracy—and its modular design allows seamless integration of new components.

Ray’s Role: Powering Large-Scale AutoML for Agentic Pipelines
Mark details the significant infrastructure challenges behind syftr and how
Ray enables the system to operate efficiently:

Ray distributed execution scales VDB construction across heterogeneous clusters, managing CPU-heavy small-model pipelines and GPU-dependent large-model pipelines (T4, A100, H100, etc.).

Ray Serve automatically scales OSS LLMs and embedding models during search, elastically allocating compute to models that the optimizer favors—while scaling others to zero to save cost.

Ray’s unified distributed computing model provides the reliability, elasticity, and developer ergonomics needed for large-scale AI/infra research.

Why it matters
syftr demonstrates how Ray accelerates cutting-edge research at the intersection of AI infrastructure, AutoML, and agentic pipeline optimization, enabling the automated discovery of high-performing generative AI workflows that were previously impractical to build by hand.
Attendees will gain deep insights into how Ray powers syftr’s large-scale distributed search and how these techniques can be applied to design high-performance, cost-efficient, and production-ready agentic pipelines.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
