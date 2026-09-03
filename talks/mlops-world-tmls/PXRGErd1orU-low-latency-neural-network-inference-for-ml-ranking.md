---
id: PXRGErd1orU
title: "Low latency Neural Network Inference for ML Ranking Applications Yelp Case Study"
slug: low-latency-neural-network-inference-for-ml-ranking
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Ryan Irwin"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 39
published_at: 2023-08-18T01:34:36Z
video_id: PXRGErd1orU
url: https://www.youtube.com/watch?v=PXRGErd1orU
youtube_url: https://www.youtube.com/watch?v=PXRGErd1orU
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "Inference, serving & GPU infra"]
transcript: false
---

# Low latency Neural Network Inference for ML Ranking Applications Yelp Case Study

**Ryan Irwin**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `39 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=PXRGErd1orU) · [Conference site](https://mlopsworld.com/)

## Description

Speakers:
Ryan Irwin, Engineering Manager, Yelp Inc.
Ryan Irwin is a senior engineering manager at Yelp. He leads the teams responsible for the ML Platform, which covers ML computing, feature engineering, model training, and model inference. Ryan has a Ph.D. in Computer Engineering from Virginia Tech.

Rajvinder Singh, Sr Product Manager, Yelp Inc.
Rajvinder is currently leading product for the CoreML Group, and was previously an Engineering Manager at Etsy where he lead the ML Platform team.

Abstract:
At Yelp, we train and deploy models for a variety of business applications requiring low-latency model inference.  At first we focused on streamlining support for XGboost and LR models built in Spark to support business recommendations, search, ads, restaurants, and trust & safety use-cases.  However, we didn’t have a way of supporting low-latency neural network models with Tensorflow.  Such models usually relied on batched model inference in support of models used for photo classification [1] and popular dishes [2].

In this talk, we give an architectural overview of our ML Platform and how we overhauled it to support neural network models in low-latency ranking applications.  We cover how we built in the capabilities to train and deploy Tensorflow-based models using MLEAP and cataloged them in MLFlow.  We also discuss the deployment plugin that was using Elasticsearch and how this transitioned to using Yelp’s own near-real time search (Nrtsearch) [3] open-source framework.  Lastly, we cover the issues faced along the way in terms of latency and model performance, including how we incorporate embedded features in the model.
[1] https://engineeringblog.yelp.com/2015/10/how-we-use-deep-learning-to-classify-business-photos-at-yelp.html
[2] https://engineeringblog.yelp.com/2019/10/discovering-popular-dishes-with-deep-learning.html
[3] https://engineeringblog.yelp.com/2021/09/nrtsearch-yelps-fast-scalable-and-cost-effective-search-engine.html
