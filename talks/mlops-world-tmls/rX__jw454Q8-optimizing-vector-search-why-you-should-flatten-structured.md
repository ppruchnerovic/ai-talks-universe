---
id: rX__jw454Q8
title: "Optimizing Vector Search: Why You Should Flatten Structured Data"
slug: optimizing-vector-search-why-you-should-flatten-structured
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 20
published_at: 2026-08-11T13:10:08Z
video_id: rX__jw454Q8
youtube_url: https://www.youtube.com/watch?v=rX__jw454Q8
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Optimizing Vector Search: Why You Should Flatten Structured Data

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `20 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=rX__jw454Q8) · [Conference site](https://mlopsworld.com/)

## Description

Oleg Tereshin, Senior Software Engineer, Independent Software Engineer

About the Speaker:
I am a Senior Software Engineer with 12 years of experience, specializing in AI Infrastructure and Semantic Search. I am currently building a semantic search platform, managing high-throughput embedding pipelines, and orchestrating vector databases on Kubernetes. As an author on Towards Data Science, I share practical, empirical strategies for vector search optimization.

Abstract:
When integrating structured data into a RAG system, engineers often default to embedding raw JSON into a vector database. The reality, however, is that this intuitive approach leads to dramatically poor retrieval performance. Modern embeddings leverage BERT architectures optimized for natural language, which struggle with the high frequency of non-alphanumeric characters found in JSON syntax.
In this session, I will break down the exact failures of embedding structured data—from tokenization and attention mechanism disruption to the mathematical liability of Mean Pooling on syntax tokens. I will then demonstrate a practical, production-ready solution: implementing a simple preprocessing step to convert structured JSON into natural language templates. Backed by empirical testing on the Amazon ESCI dataset, I will show how this straightforward architectural shift natively boosts Recall@10 by over 19% and MRR by 27%.
Note: This article was recently featured as a top weekly article on Towards Data Science, reaching over 9,000 views.
