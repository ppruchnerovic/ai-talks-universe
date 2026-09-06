---
id: SeBoia7jcnI
title: "“Many-model” Time Series Forecasting: Scaling PyTorch Training Across 1000s...- V. Sridhar & S. Chen"
slug: many-model-time-series-forecasting-scaling-pytorch-training
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 26
published_at: 2025-11-04T03:43:38Z
video_id: SeBoia7jcnI
url: https://www.youtube.com/watch?v=SeBoia7jcnI
youtube_url: https://www.youtube.com/watch?v=SeBoia7jcnI
tags: []
topics: ["Classic ML & data science", "Training, fine-tuning & model building"]
transcript: false
---

# “Many-model” Time Series Forecasting: Scaling PyTorch Training Across 1000s...- V. Sridhar & S. Chen

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=SeBoia7jcnI) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

“Many-model” Time Series Forecasting: Scaling PyTorch Training Across 1000s of Models - Vinay Sridhar & Shulin Chen, Snowflake

Modern time series forecasting increasingly relies on transformer models, often deployed in scenarios where datasets are partitioned such as across product segments in retail, leading to the need to create a time-series model per segment, often 100s to 1000s at the same time. Training these sophisticated models involves large datasets and complex transforms, while dealing with resource limitations. This leads to training such 1000s of PyTorch models sequentially resulting in long training times and thereby much fewer iterations. This talk presents a solution that demonstrates how to train thousands of such PyTorch models in parallel leveraging Ray’s advanced scheduling and distributed processing while utilizing resources efficiently. By seamlessly integrating highly parallel data loading with distributed processing, we establish a pipeline that optimizes for cost-efficiency, resource utilization, and execution time. This approach empowers users to train larger, more complex transformer models on significantly bigger datasets and more often leading to a higher velocity of developing and deploying advanced, ML-powered forecasting applications with superior predictive quality.
