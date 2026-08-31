---
id: l9F_pLbdUvY
title: "MLOps for Deep Learning"
slug: mlops-for-deep-learning
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Diego Klabjan", "Yegna Jambunath"]
channel: null
duration_min: 48
published_at: 2023-08-18T01:34:36Z
video_id: l9F_pLbdUvY
youtube_url: https://www.youtube.com/watch?v=l9F_pLbdUvY
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# MLOps for Deep Learning

**Diego Klabjan, Yegna Jambunath**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `48 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=l9F_pLbdUvY) · [Conference site](https://mlopsworld.com/)

## Description

Speakers:
Diego Klabjan, Professor and Yegna Jambunath, MLOps Researcher, Northwestern University, Center for Deep Learning

MLOps Researcher at Centre for Deep Learning, Northwestern University. Holding six years of total work experience with four years of industry specific ML research experience.  Presented a ML research abstract in healthcare in ESHRE international conference. Aspiring to learn, research and contribute to the community.

Abstract:
In model serving, two important decisions are when to retrain the model and how to efficiently retrain it. Having one fixed model during the entire often life-long inference process is usually detrimental to model performance, as data distribution evolves over time, resulting in a lack of reliability of the model trained on historical data. It is important to detect drift and retrain the model in time. We present an ensemble drift detection technique utilizing three different signals to capture data and concept drifts. In a practical scenario, ground truth labels of samples are received after a lag in time, which we consider appropriate. Our framework automatically decides what data to use to retrain based on the signals. It also triggers a warning indicating a likelihood of drift.

Model training in serving is not a one-time task but an incremental learning process. We address two challenges of life-long retraining: catastrophic forgetting and efficient retraining. To solve these two issues, we design a retraining model that can select important samples and important weights utilizing multi-armed bandits. To further address forgetting, we propose a new regularization term focusing on synapse and neuron importance.

Only a significant minority of companies unlock the true potential of AI as trained models accumulate dust due to challenges in MLOps. Serving reliable AI predictions to customers involves cost, effort, and planning to set up a continuous deployment pipeline. MLOps for Deep Learning demands a carefully crafted deployment pipeline. We discuss our open-source project which is a robust continuous deployment pipeline by integrating our unique drift detection and model retrain algorithms for serving DL models. We show how to efficiently deploy, monitor, and maintain DL models in production using our solution which is a Kubernetes native POC solution.
