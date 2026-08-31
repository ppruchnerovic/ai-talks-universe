---
id: ebidMHNmO8E
title: "BigDL 2.0- Seamlessly scaling end-to-end AI pipelines at Intel"
slug: bigdl-2-0-seamlessly-scaling-end-to-end-ai-pipelines-at
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: null
duration_min: 26
published_at: 2023-02-09T03:13:08Z
video_id: ebidMHNmO8E
youtube_url: https://www.youtube.com/watch?v=ebidMHNmO8E
tags: []
transcript: false
---

# BigDL 2.0- Seamlessly scaling end-to-end AI pipelines at Intel

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=ebidMHNmO8E) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

BigDL 2.0: Seamlessly scaling end-to-end AI pipelines at Intel

Applying AI models to end-to-end data analysis pipelines plays a critical role in today's large-scale, intelligent applications. On the other hand, AI projects usually start with a Python notebook running on a single laptop or workstation, and one needs to go through a mountain of pains to scale it to handle larger datasets with high performance (for both large-scale experimentation and production deployment). These often require data scientists to follow many manual, error-prone steps and even make intrusive code changes so as to fully take advantage of the available hardware resources. To address these challenges, we have open sourced BigDL 2.0 (https:/ /github.com/intel-analytics/BigDL/) under the Apache 2.0 license (combining the original BigDL and Analytics Zoo projects), which allows users to build end-to-end AI pipelines that are transparently accelerated on a single node (with up to 9.6x speedup in our experiments) and seamlessly scaled out to a large cluster (across several hundreds of nodes in real-world use cases). It automatically provisions Big Data and AI systems (such as Ray and Apache Spark) for the distributed execution; on top of the underlying systems, it efficiently implements the distributed, in-memory data pipelines (for Spark Dataframes, TensorFlow Dataset, PyTorch, DataLoader, as well as arbitrary Python libraries), and transparently scales out deep learning (such as TensorFlow and PyTorch) training and inference on the distributed dataset (through scikit-learn style APIs). BigDL 2.0 has already been adopted by many real-world users (such as Mastercard, Burger King, Inspur, etc.) in production. In this session, we will demonstrate how to build an end-to-end AI pipeline using BigDL2.0 on Ray, and showcase real-world BigDL use cases.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
