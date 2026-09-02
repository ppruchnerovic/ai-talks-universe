---
id: RGrwb-W5FDk
title: "UnionML: A Microframework for Building Machine Learning Applications"
slug: unionml-a-microframework-for-building-machine-learning
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Niels Bantilan"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 27
published_at: 2023-05-29T05:19:19Z
video_id: RGrwb-W5FDk
url: https://www.youtube.com/watch?v=RGrwb-W5FDk
youtube_url: https://www.youtube.com/watch?v=RGrwb-W5FDk
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Governance, ethics & regulation", "Science, healthcare & applied ML", "Training, fine-tuning & model building"]
transcript: false
---

# UnionML: A Microframework for Building Machine Learning Applications

**Niels Bantilan**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `27 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=RGrwb-W5FDk) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Niels Bantilan, Machine Learning Engineer, Union.AI

Niels is a machine learning engineer and core maintainer of Flyte, an open source ML orchestration tool and author and maintainer of Pandera, a data testing tool for dataframes.

He has a Masters in Public Health with a specialization in sociomedical science and public health informatics, and prior to that a background in developmental biology and immunology.

His research interests include reinforcement learning, AutoML, creative machine learning, and fairness, accountability, and transparency in automated systems. He enjoys developing open source tools to make data science and machine learning practitioners more productive.

Abstract:
A common problem in the machine learning development life cycle is the challenge of going from research to production. An ML team might need to modularize and refactor their code to work more efficiently or effectively in production. Sometimes this might even require re-implementing and maintaining feature engineering or model prediction logic in multiple places depending on whether the application requires offline, online, and/or streaming predictions.

Thinking about a solution to this problem, we can take inspiration from the web. The HTTP protocol, for example, standardizes the way we transfer data across the internet, providing a backbone of methods with clearly defined but flexible interfaces. As machine learning systems become more prevalent across industries, we wanted to ask the question: what if we had such a protocol for building and deploying machine learning applications at scale?

In this talk, we introduce µlearn (pronounced “micro-learn”), an open source microframework for building machine learning applications. Created by the team behind Flyte, µlearn provides a simple, user-friendly interface for defining the building blocks of your machine learning application, from dataset curation and sampling to model training and prediction. Using these building blocks, µlearn automatically creates the workflows that you need to tune your models and deploy them to production in different prediction use cases, such as offline, online, or streaming contexts.
