---
id: BG_nB5dolKs
title: "Scaling Production-Grade LLMs: Diagnosing Hidden Bottlenecks in Training and Inference Systems"
slug: scaling-production-grade-llms-diagnosing-hidden-bottlenecks
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 25
published_at: 2026-08-11T13:09:26Z
video_id: BG_nB5dolKs
youtube_url: https://www.youtube.com/watch?v=BG_nB5dolKs
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Scaling Production-Grade LLMs: Diagnosing Hidden Bottlenecks in Training and Inference Systems

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `25 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=BG_nB5dolKs) · [Conference site](https://mlopsworld.com/)

## Description

Deepkamal Gill, Senior AI/ML Scientist, The Vanguard Group
Mehul Soni, Senior AI Research Engineer, Enterprise AI Research, The Vanguard Group

About the Speaker:
Deepkamal Kaur Gill is a Senior Applied AI Scientist at Vanguard, where she builds production-grade LLM systems for high-stakes financial applications. Her work spans data generation, post-training, and evaluation, with a focus on building reliable, low-latency AI systems under real-world constraints.

Deepkamal holds a Master’s in Computer Science from the University of Toronto and is an active contributor to the AI community through research, mentorship, and initiatives supporting women in technology. At TMLS, she brings a practitioner’s perspective on what it truly takes to scale LLMs in production.

Mehul is a Senior AI Engineer at Vanguard, specializing in building enterprise-scale LLM and agentic AI systems that bridge applied research and production impact. She brings over five years of industry experience applying AI/ML techniques to solve complex business problems. Her work spans LLM post-training, multi-agent systems, evaluation frameworks, and AI systems engineering, with a strong emphasis on translating cutting-edge research into scalable, production-ready solutions. Mehul is actively engaged in AI and professional communities, contributing to initiatives that promote mentorship and inclusive growth, such as Women in Data Science.

Abstract:
While recent advances in LLMs emphasize improved model capabilities, many systems fail to scale in real-world production settings. Beyond a certain point, adding GPUs or data yields diminishing returns: training stops scaling efficiently, hardware remains underutilized, and inference latency is dominated by system constraints rather than compute. These failures are often silent, poorly documented, and difficult to diagnose in distributed environments.

In this talk, we share lessons from building enterprise-scale domain LLM systems, focusing on the system-level bottlenecks that limit scaling in practice. We examine failure modes across distributed training and inference—including communication overhead, pipeline imbalance, numerical instability during training as well as memory-bound decoding, KV cache growth, and throughput–latency tradeoffs at inference—and show how they manifest in production systems.

Rather than introducing new modeling techniques, this session presents a practical, symptom-driven approach to debugging: identifying failure patterns, tracing their root causes, and applying targeted mitigations. The key takeaway is that scaling LLMs is fundamentally a systems problem, and attendees will leave with a concrete framework to diagnose bottlenecks and make better design decisions when moving from prototype to production.
