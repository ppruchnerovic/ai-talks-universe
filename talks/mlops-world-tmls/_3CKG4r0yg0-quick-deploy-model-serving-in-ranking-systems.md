---
id: _3CKG4r0yg0
title: "Quick Deploy Model Serving in Ranking Systems"
slug: quick-deploy-model-serving-in-ranking-systems
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2023
speakers: []
channel: null
duration_min: 32
published_at: 2023-08-18T01:37:38Z
video_id: _3CKG4r0yg0
url: https://www.youtube.com/watch?v=_3CKG4r0yg0
youtube_url: https://www.youtube.com/watch?v=_3CKG4r0yg0
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education", "mlops community", "Quick Deploy Model Serving in Ranking Systems", "Quick Deploy Model Serving", "Ranking Systems", "Model Serving", "Quick Deploy"]
topics: ["Data engineering & MLOps", "Inference, serving & GPU infra"]
transcript: false
---

# Quick Deploy Model Serving in Ranking Systems

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `32 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education` `#mlops community` `#Quick Deploy Model Serving in Ranking Systems` `#Quick Deploy Model Serving` `#Ranking Systems` `#Model Serving` `#Quick Deploy`

[Watch the recording](https://www.youtube.com/watch?v=_3CKG4r0yg0) · [Conference site](https://mlopsworld.com/)

## Description

Speaker Bio:

Talal Riaz, Software Engineer
Yelp
Software Engineer with the ML Infrastructure team at Yelp.  Ph.D. with a focus on Randomized and Distributed Algorithms from the University of Iowa.

Abstract:
At Yelp, we use ElasticSearch(ES) to power most of our Search. However, the process for updating a model or replacing it was slow and error-prone; engineers needed to spend time implementing any new feature transformations when training and serving, as well as ensuring parity between the two. We improve this situation by building an ES plugin that integrates neatly into Yelp’s Model Platform. Spark Pipelines trained and stored as MLeap bundles to MLFlow using the Model Platform can now be deployed directly to ES as MLeap pipelines. These Spark/MLeap pipelines encapsulate not only the ML model itself but also it’s feature engineering pipeline. Subsequently, this allows the ES plugin to swap one modeling pipeline for another as long as the base features for their pipelines are available through the ES index!

In this talk, we will discuss this ES plugin,  as well as lessons learnt in making model pipelines performant.
