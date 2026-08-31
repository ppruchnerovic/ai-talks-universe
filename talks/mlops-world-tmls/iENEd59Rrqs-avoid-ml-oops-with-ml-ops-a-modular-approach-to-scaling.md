---
id: iENEd59Rrqs
title: "Avoid ML OOps with ML Ops: A modular approach to scaling Forethought’s E2E ML Platform"
slug: avoid-ml-oops-with-ml-ops-a-modular-approach-to-scaling
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2024
speakers: ["Salina Wu"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 51
published_at: 2024-05-15T18:17:49Z
video_id: iENEd59Rrqs
youtube_url: https://www.youtube.com/watch?v=iENEd59Rrqs
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Avoid ML OOps with ML Ops: A modular approach to scaling Forethought’s E2E ML Platform

**Salina Wu**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2024` · `51 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=iENEd59Rrqs) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Salina Wu
Senior Machine Learning Infrastructure Engineer, Forethought

Abstract:
As Machine Learning becomes more ubiquitous in business and product applications, the need for a cost-efficient, scalable, and automated infrastructure to support the end-to-end ML lifecyle becomes mission critical. However, a scalable and reusable ML Ops platform is often an afterthought in productionizing ML models, due to urgency of business needs and lack of resources or experience. A very common scenario is for ML Ops to be ad-hoc and de-centralized, with no good way to reproduce or automate ML processes. It can be challenging, especially for smaller teams, to identify and foresee specific ML Ops needs and understand how to address them.

Forethought is an enterprise company building AI-powered customer experience (CX) solutions. Our products require training customer-specific language models and deploying them on low-latency, high-uptime endpoints. With ML at the heart of our business, our infrastructure supporting it is pivotal to our growth and success. At Forethought, we took a close look at our initial ML infrastructure, aiming to identify key areas of improvement and anticipate future requirements. Through a step-by-step approach, we gradually replaced our existing infrastructure with improved, modular components to arrive at a much more mature system. This case study will dive into which areas we identified as critical to replace as well as the steps we took to enhance them. In particular, we will look at the following:

- Streamlining ML training and migrating to the Sagemaker training platform
- Achieving efficient model serving with Sagemaker Serverless and Multi-Model Endpoints
- Orchestrating our ML processes with automated pipelines on Dagster
- Centralizing ML feature engineering across our datalake using Spark
- Building intuitive model management tooling with Retool

Through this talk, we’ll show a real-world scenario of bringing a rudimentary v0 ML architecture to an enhanced v1 architecture. We will also share our plans and progress building towards our v2 vision, including automated re-training and LLM support. Key takeaways will include:
- Understanding the different components of a solid ML infrastructure
- Identifying and proactively addressing bottlenecks and opportunities for growth in your ML lifecycle
- Learning how to improve and migrate your ML infrastructure in stages
- Understanding the goals and best practices of a stable end-to-end ML infrastructure
