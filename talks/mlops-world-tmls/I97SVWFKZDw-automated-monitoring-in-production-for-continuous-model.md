---
id: I97SVWFKZDw
title: "Automated Monitoring in Production for Continuous Model Improvements"
slug: automated-monitoring-in-production-for-continuous-model
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2023
speakers: []
channel: null
duration_min: 29
published_at: 2023-08-18T01:36:05Z
video_id: I97SVWFKZDw
url: https://www.youtube.com/watch?v=I97SVWFKZDw
youtube_url: https://www.youtube.com/watch?v=I97SVWFKZDw
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "Evals, observability & reliability"]
transcript: false
---

# Automated Monitoring in Production for Continuous Model Improvements

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `29 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=I97SVWFKZDw) · [Conference site](https://mlopsworld.com/)

## Description

Speakers' Bio:
Deepak Pai
Senior Manager, Machine Learning
Adobe

Deepak is a Machine Learning Engineer with 16 years of experience. He has published papers in top peer reviewed conferences and holds multiple US patents. Currently he manages a team of Machine Learning Engineers developing multiple products and services at Adobe, that are part of the Digital Experience business. Deepak holds Masters and Bachelor degree in Computer Science from a leading universities in India.

Vijay Srivastava
Manager, ML Core Services
Adobe

Vijay has 15 years of industry experience across ML & E-Learning products and has extensive experience in developing scalable Machine Learning & e-Learning cloud services from inception. During his technical journey at Adobe, he worked on multiple key positions as Senior Computer Scientist and Staff Data Scientist. As a part of his current job, he manages a team of machine learning engineers developing core ML services which feeds ML insights to Experience Cloud Intelligent Services. He had his bachelor’s degree from Indian Institute of Information Technology - Allahabad, India.

Abstract:
You spend lots of time cleansing data, visualizing it to gain insights, feature engineering, modeling while ensuring that you picked the best algorithm and architecture, best hyper parameters and so on. Finally you deploy the model and claim victory and move on. Well, that is not the end of task for an ML engineer. Model monitoring is much more critical than model building and often neglected area of MLOps. Despite their critical roles, ML models in production are not actively monitored. Ideally one should monitor the production systems proactively, but unfortunately being reactive is the norm. When a problem first arises, it may go unnoticed for some time. Once it is noticed, investigating its underlying cause is a time-consuming, manual process, not to mention the damage that is already done in production. Even if you are manually monitoring the models in production, the approach does not scale when you get to tens of models if not hundreds.
Like the saying goes, “A stitch in time saves nine”, wouldn’t it be great if the model’s output were automatically monitored? If they could be visualized, sliced by different dimensions? If the system could automatically detect performance degradation and trigger alerts? If problems in the model output could be attributed to the characteristics of input data? In this presentation, we describe our experience from building such a core machine-learning services: Model Evaluation and Data Quality.
Our service provides automated, continuous evaluation of the performance of a deployed model over commonly-used metrics like the area-under-the-curve (AUC), root-mean-square-error (RMSE) among others. In addition, summary statistics about the model’s output, their distributions are also computed. The service also provides a dashboard to visualize the performance metrics, summary statistics and distributions of a model over time along with REST APIs to retrieve these metrics programmatically. The service can correlate model performance issues to likely causes in input data/data quality, which can be leveraged by data scientists and engineers to debug the problems. This significantly reduces the turn around time for identifying and fixing  issues in production.
Further, these metrics can be sliced by input features to provide insights into model performance over different segments, and potentially improve the model. The talk will describe various components that are required in building such a service and metrics of interest. Our system has a backend component built with spark on Azure Databricks. The backend can scale to analyze TBs of data to generate model evaluation metrics. The REST endpoints are powered by a python-Flask middleware application hosted on Azure webapp and the UI is built with React.
