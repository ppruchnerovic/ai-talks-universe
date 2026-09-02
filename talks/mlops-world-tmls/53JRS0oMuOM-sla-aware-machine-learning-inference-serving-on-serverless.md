---
id: 53JRS0oMuOM
title: "SLA Aware Machine Learning Inference Serving on Serverless Computing Platforms"
slug: sla-aware-machine-learning-inference-serving-on-serverless
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Nima Mahmoudi"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 36
published_at: 2023-08-18T01:34:36Z
video_id: 53JRS0oMuOM
url: https://www.youtube.com/watch?v=53JRS0oMuOM
youtube_url: https://www.youtube.com/watch?v=53JRS0oMuOM
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra"]
transcript: false
---

# SLA Aware Machine Learning Inference Serving on Serverless Computing Platforms

**Nima Mahmoudi**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `36 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=53JRS0oMuOM) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Nima Mahmoudi
Machine Learning Engineer, Telus Communications Inc.

Nima Mahmoudi is a Data Scientist at TELUS Communications Inc. He received the BSc degrees in Electronics and Telecommunications and the MSc degree in Digital Electronics from Amirkabir University of Technology, Tehran, Iran in 2014, 2016, and 2017 respectively. He received the PhD degree in Software Engineering and Intelligent Systems from the University of Alberta, Edmonton, AB, Canada in 2022. He used to be a visiting research assistant in the Performant and Available Computing Systems (PACS) lab at York University, Toronto, ON, Canada

Abstract:
Serving machine learning inference workloads on the cloud is still a challenging task on the production level. Optimal configuration of the inference workload to meet SLA requirements while optimizing the infrastructure costs is highly complicated due to the complex interaction between batch configuration, resource configurations, and variable arrival process. Serverless computing has emerged in recent years to automate most infrastructure management tasks. Workload batching has revealed the potential to improve the response time and cost-effectiveness of machine learning serving workloads. However, it has not yet been supported out of the box by serverless computing platforms. Our experiments have shown that for various machine learning workloads, batching can hugely improve the system's efficiency by reducing the processing overhead per request. In this work, we present MLProxy, an adaptive reverse proxy to support efficient machine learning serving workloads on serverless computing systems. MLProxy supports adaptive batching to ensure SLA compliance while optimizing serverless costs. We performed rigorous experiments on Knative to demonstrate the effectiveness of MLProxy. We showed that MLProxy could reduce the cost of serverless deployment by up to 92% while reducing SLA violations by up to 99% that can be generalized across state-of-the-art model serving frameworks.
