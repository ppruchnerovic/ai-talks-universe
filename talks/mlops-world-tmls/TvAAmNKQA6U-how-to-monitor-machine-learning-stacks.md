---
id: TvAAmNKQA6U
title: "How To Monitor Machine Learning Stacks"
slug: how-to-monitor-machine-learning-stacks
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2021
speakers: []
channel: null
duration_min: 33
published_at: 2021-06-30T16:00:14Z
video_id: TvAAmNKQA6U
youtube_url: https://www.youtube.com/watch?v=TvAAmNKQA6U
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education", "How To Monitor Machine Learning Stacks", "Lina Weichbrodt", "machine learning tutorial", "azure machine learning", "azure", "deep learning", "stack", "data structures", "ai"]
transcript: false
---

# How To Monitor Machine Learning Stacks

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2021` · `33 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education` `#How To Monitor Machine Learning Stacks` `#Lina Weichbrodt` `#machine learning tutorial` `#azure machine learning` `#azure` `#deep learning` `#stack` `#data structures` `#ai`

[Watch the recording](https://www.youtube.com/watch?v=TvAAmNKQA6U) · [Conference site](https://mlopsworld.com/)

## Description

💻 Abstract:
Monitoring usually focuses on the “four golden signals”: latency, errors, traffic, and saturation. Machine learning services can suffer from special types of problems that are hard to detect with these signals. The talk will introduce these problems with practical examples and suggests additional metrics that can be used to detect them. A case study demonstrates how these new metrics work for the recommendation stacks at Zalando, one of Europe’s largest fashion retailers.

🔊 Speaker bio:
Machine Learning Lead Engineer, DKB Bank
Lina Weichbrodt has 8+ years of industry experience in developing scalable machine learning models and bringing them into production. She currently works as the Machine Learning Lead Engineer in the data science group of the German online bank DKB. She previously worked at Zalando, one of Europe’s biggest online fashion retailers, where she developed real-time, deep learning personalization models for more than 32M users.

If you enjoyed this talk, visit us at https://mlopsworld.com/ and come participate in our next gathering! 💼

Would you like to receive email summaries of these talks? Join our newsletter FREE here: http://bit.ly/MLOps_Summaries 📧

Timestamps:

0:00 Intro
0:11 Introduction of Lina Weichbrodt
0:52 How do you detect that your service quality dropped?
2:40 ML stacks are often monitored like any other service
3:04 Example service with typical components
4:38 Risk area: Requests
6:19 Risk area: Code
7:03 Risk area: Model
8:20 Risk area: External Services
8:57 Risk area: Configuration
10:45 Solution
12:23 Alternative: Why not monitor user actions?
14:20 Alternative: Why not monitor model?
15:22 How to select a quality metric
16:50 Case study (Large scale use case: Recommender system at Zalando)
17:39 One metric for all use cases was enough
19:50 Implementation was done with simple metrics
20:49 Longer time rangers are useful for analysis
21:28 Quality alerts can be used during deployment
22:03 Deployment without bug
23:41 Take away: You should monitor quality metrics

❓ Q&A ❓

24:09 How can you evaluate "how a change in a service using a model is affecting another service that is using the output of the former as the inputs to its own model"?
25:30 What's the engineering response to seeing drop metrics?
26:15 What monitoring tools do you use/recommend?
26:34 Is your recommendations as something beyond just watching for model drift?
28:25 How can you detect model drift? monitor the data distribution?
29:47 How to raise a flag, you suggest computing distances between distributions?
10:11 Is it possible to monitor the joint distribution of the input data? or just the univariate distribution?
31:20 Are the quality metrics defined as part of the model training/serving process done by the data scientist?"

32:54 Closing remarks
