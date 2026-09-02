---
id: Y2qc0UhDSnc
title: "Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA"
slug: hacking-the-inference-pareto-frontier-kyle-kranen-nvidia
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Kyle Kranen"]
channel: "AI Engineer"
duration_min: 20
published_at: 2025-08-01T13:45:06Z
video_id: Y2qc0UhDSnc
url: https://www.youtube.com/watch?v=Y2qc0UhDSnc
youtube_url: https://www.youtube.com/watch?v=Y2qc0UhDSnc
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA

**Kyle Kranen**

`AI Engineer` · `AI Engineer` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=Y2qc0UhDSnc) · [Conference site](https://www.ai.engineer/)

## Description

Your model works! It aces the evals! It even passes the vibe check! All that’s required is inference, right? Oops, you’ve just stepped into a minefield:

-Not low-latency enough? Choppy experience. Users churn from your app.
-Not cheap enough? You’re losing money on every query.
-Not high enough output quality? Your system can’t be used for that application.

A model and the inference system around it form a “token factory” associated with a Pareto frontier— a curve representing the best possible trade-offs between cost, throughput, latency and quality, outside of which your LLM system cannot be applied successfully.

Outside of the Pareto frontier? You’re back to square one.
That is, unless you’re able to change the shape of the Pareto frontier.

In this session, we’ll introduce NVIDIA Dynamo, a datacenter-scale distributed inference framework as well as the bleeding-edge techniques it enables to hack the Pareto frontier of your inference systems, including:

-Disaggregation - separating phases of LLM generation to make them more efficient
-Speculation - predicting multiple tokens per cycle
-KV routing, storage, and manipulation - ensuring that we don’t redo work that has already been done
-Pipelining improvements for agents - accelerating our workflows using information about the agent

By the end of the talk, we’ll understand how the Pareto frontier limits where models can be applied, the intuition behind how inference techniques can be used to modify it, as well as the mechanics of how these techniques work.

---related links---

Timestamps:

00:00 Introduction to Breaking the Inference Pareto Frontier
00:33 Introduction of Kyle Cranon and NVIDIA Dynamo
01:31 The Three Pillars of Deployment (Quality, Latency, Cost)
02:11 Understanding the Pareto Frontier
03:06 Application-Specific Prioritization of Quality, Latency, and Cost
04:32 Common Techniques to Manipulate the Pareto Frontier (Quantization, RAG, Reasoning)
05:19 Compounding Techniques
06:04 Three Drivers for Modifying the Pareto Frontier (Scale, Structure, Dynamism)
06:20 Scale: Disaggregation
11:02 Scale: Routing
13:00 Structure: Inference Time Scaling
16:14 Structure: KV Manipulation
17:43 Dynamism: Worker Specialization
18:42 Dynamism: Dynamic Load Balancing
19:55 Conclusion and NVIDIA Dynamo Resources
