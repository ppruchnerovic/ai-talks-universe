---
id: nPn42_EXB5U
title: "Lessons learned from scaling large language models in production"
slug: lessons-learned-from-scaling-large-language-models-in
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2024
speakers: ["Matt Squire"]
channel: null
duration_min: 40
published_at: 2024-05-16T15:09:13Z
video_id: nPn42_EXB5U
url: https://www.youtube.com/watch?v=nPn42_EXB5U
youtube_url: https://www.youtube.com/watch?v=nPn42_EXB5U
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: false
---

# Lessons learned from scaling large language models in production

**Matt Squire**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2024` · `40 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=nPn42_EXB5U) · [Conference site](https://mlopsworld.com/)

## Description

Speaker: Matt Squire, CTO, Fuzzy Labs

Open source models have made running your own LLM accessible many people. It's pretty straightforward to set up a model like Mistral, with a vector database, and build your own RAG application.

But making it scale to high traffic demands is another story. LLM inference itself is slow, and GPUs are expensive, so we can't simply throw hardware at the problem. Once you add things like guardrails to your application, latencies compound.

In this talk, I'll share the lessons we've learned from our experience building and running LLMs for our customers at scale. Using real code examples, I'll cover performance profiling, getting the most out of GPUs, and interactions with guardrails.
