---
id: K8TXLXfJo6M
title: "INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce"
slug: inspire-intent-aware-neural-sponsored-product-retrieval-for
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 30
published_at: 2026-08-11T13:10:08Z
video_id: K8TXLXfJo6M
youtube_url: https://www.youtube.com/watch?v=K8TXLXfJo6M
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `30 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=K8TXLXfJo6M) · [Conference site](https://mlopsworld.com/)

## Description

Shasvat Desai, Staff Machine Learning Scientist, Walmart Global Tech

About the Speaker:
I am currently a Machine Learning Scientist in the Sponsored Products Search team at Walmart that is responsible for powering the advertising technology for Walmart's e-commerce platform. My work spans the domain of semantic query and item understanding, retrieval (traditional IR and neural networks), ranking, and ad auction and monetization. Apart from product dev, I work on applied research. Recently, I got a paper accepted at SIGIR 2026, Industry track: https://arxiv.org/pdf/2604.07930

Abstract:
Walmart holds the largest share of the U.S. e-commerce grocery market, where food and beverage categories generate some of the highest search traffic and, consequently, drive a substantial portion of sponsored search revenue. At this scale, even small mismatches between user intent and retrieved products can lead to significant losses in both user engagement and monetization. Yet, understanding user intent in grocery search is inherently challenging. Queries are typically short, ambiguous, and highly diverse, often underspecifying critical preferences.
For example, a query like schar white bread implicitly encodes a gluten-free preference through brand association, while queries such as chickpea pasta or oatmilk reflect underlying dietary preferences like gluten-free, plant based, or lactose-free alternatives. Failing to capture these signals results in retrieving products that might be semantically similar but misaligned with the user’s true needs.
From the advertiser’s perspective, many products are explicitly designed to target specific intents—such as dietary preferences or size variants—and must be surfaced at the right moment to be effective. For example, a brand like Quest Nutrition, which sells high-protein, low-sugar snacks, wants its products to appear for queries like protein bars, low carb snacks, or keto snacks, even when these attributes might not be explicitly stated in the product title text. When retrieval systems fail to capture these intent signals, relevant products are not shown to the right users at the right time. From an advertiser’s perspective, this means their products are missing high-intent opportunities where conversion is most likely. Over time, this leads to lower returns on ad spend, reduced trust in the platform, and potential advertiser attrition. Losing advertisers directly translates to a loss in advertising revenue and weakens the overall sponsored search ecosystem. This challenge is further amplified in sponsored search, where only a limited number of ad slots are available, making precise relevance essential. Thus, we propose INSPIRE (Intent-aware Neural Sponsored Product Retrieval for E-commerce), an intent aware retrieval framework for sponsored search that leverages structured intent signals to better align user queries with relevant food and beverage products. INSPIRE represents intent as a set of structured, multi-dimensional attributes derived from both user queries and product content, capturing explicit signals (e.g., brand, flavor) as well as implicit preferences (e.g., dietary constraints, cuisine types) that are often not directly expressed in queries.
We develop a weakly supervised intent learning pipeline, where a large language model serves as a teacher to generate structured intent annotations from product titles and descriptions. We then distill these annotations by using them to finetune a lightweight student LLM model through LoRA based supervised finetuning (LoRA-SFT) that predicts intent attributes—such as brand, flavor, dietary preference, ingredient, product subtype, and cuisine type—at Walmart catalog scale. We then introduce an intent-augmented dense retrieval framework, where predicted intents are incorporated into query and product representations within a bi-encoder, enabling more precise matching between queries and sponsored products. To support real-world usage, we deploy the system as a scalable inference service. The distilled student model is served via a high-throughput API powered by vLLM, enabling efficient intent prediction over large product catalogs with low latency. This design ensures that intent-aware retrieval can be applied in production settings while maintaining efficiency and scalability.
