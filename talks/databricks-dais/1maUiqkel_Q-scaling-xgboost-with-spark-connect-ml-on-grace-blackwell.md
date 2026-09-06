---
id: 1maUiqkel_Q
title: "Scaling XGBoost With Spark Connect ML on Grace Blackwell"
slug: scaling-xgboost-with-spark-connect-ml-on-grace-blackwell
conference: databricks-dais
conference_name: "Databricks Data + AI Summit"
category: "Vendor events"
edition: "DAIS 2025 AI track"
year: 2025
speakers: []
channel: "Databricks"
duration_min: 36
published_at: 2025-07-07T18:54:35Z
video_id: 1maUiqkel_Q
url: https://www.youtube.com/watch?v=1maUiqkel_Q
youtube_url: https://www.youtube.com/watch?v=1maUiqkel_Q
tags: ["Databricks"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "Inference, serving & GPU infra"]
transcript: false
---

# Scaling XGBoost With Spark Connect ML on Grace Blackwell

**Speaker not identified**

`Databricks Data + AI Summit` · `DAIS 2025 AI track` · `2025` · `36 min`

`#Databricks`

[Watch the recording](https://www.youtube.com/watch?v=1maUiqkel_Q) · [Conference site](https://www.databricks.com/dataaisummit)

## Description

XGBoost is one of the off-the-shelf gradient boosting algorithms for analyzing tabular datasets. Unlike deep learning, gradient-boosting decision trees require the entire dataset to be in memory for efficient model training. To overcome the limitation, XGBoost features a distributed out-of-core implementation that fetches data in batch, which benefits significantly from the latest NVIDIA GPUs and the NVLink-C2C’s ultra bandwidth. In this talk, we will share our work on optimizing XGBoost using the Grace Blackwell super chip. The fast chip-to-chip link between the CPU and the GPU enables XGBoost to scale up without compromising performance. Our work has effectively increased XGBoost’s training capacity to over 1.2TB on a single node. The approach is scalable to GPU clusters using Spark, enabling XGBoost to handle terabytes of data efficiently. We will demonstrate combining XGBoost out-of-core algorithms with the latest connect ML from Spark 4.0 for large model training workflows.

Talk By: Bobby Wang, Engineer, NVIDIA  ; Jiaming Yuan, Engineer, ​NVIDIA Semiconductor Co., Ltd

Databricks Named a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms: https://www.databricks.com/blog/databricks-named-leader-2025-gartner-magic-quadrant-data-science-and-machine-learning
Build and deploy quality AI agent systems: https://www.databricks.com/product/artificial-intelligence
See all the product announcements from Data + AI Summit: https://www.databricks.com/events/dataaisummit-2025-announcements
