---
id: TiYIPmzb0z8
title: "Personalized Recommendations and Search with Retrieval and Ranking at scale on Hopsworks"
slug: personalized-recommendations-and-search-with-retrieval-and
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Jim Dowling"]
channel: null
duration_min: 121
published_at: 2023-08-18T01:34:36Z
video_id: TiYIPmzb0z8
url: https://www.youtube.com/watch?v=TiYIPmzb0z8
youtube_url: https://www.youtube.com/watch?v=TiYIPmzb0z8
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "RAG, retrieval & knowledge"]
transcript: false
---

# Personalized Recommendations and Search with Retrieval and Ranking at scale on Hopsworks

**Jim Dowling**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `121 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=TiYIPmzb0z8) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Jim Dowling, CEO, Hopsworks
Jim Dowling is CEO of Logical Clocks and an Associate Professor at KTH Royal Institute of Technology. He is lead architect of the open-source Hopsworks platform, a horizontally scalable data platform for machine learning that includes the industry’s first Feature Store.

Abstract:
Personalized recommendations and personalized search systems at scale are increasingly being built on retrieval and ranking architectures based on the two-tower embedding model. This architecture requires a lot of infrastructure. A single user query will cause a large fanout of traffic to the backend, with hundreds of database lookups in a feature store, similarity search in an embedding store, and model outputs from both a query embedding model and a ranking model. You will also need to index your items in the embedding store using an item embedding model, and instrument your existing systems to store observations of user queries and the items they select.

In this workshop, we will introduce the retrieval and ranking architecture based on the two-tower recommendation model, and we will walk through the implementation of a personalized recommendations service on the open-source Hopsworks platform. We will introduce  first the offline infrastructure needed to train your models, index your items in an embedding store,  and update your feature store. We will then walk through the online infrastructure needed to retrieve candidates with similarity search using an embedding store and ranking candidates with both a ranking model and features from the feature store. We will show you how you can keep end-to-end latencies below 100ms and ensure all components of the system are highly available.
