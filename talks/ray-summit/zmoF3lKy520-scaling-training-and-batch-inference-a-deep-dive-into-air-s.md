---
id: zmoF3lKy520
title: "Scaling Training and Batch Inference- A Deep Dive into AIR's Data Processing Engine"
slug: scaling-training-and-batch-inference-a-deep-dive-into-air-s
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2023
speakers: []
channel: null
duration_min: 44
published_at: 2023-02-09T03:07:32Z
video_id: zmoF3lKy520
url: https://www.youtube.com/watch?v=zmoF3lKy520
youtube_url: https://www.youtube.com/watch?v=zmoF3lKy520
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Scaling Training and Batch Inference- A Deep Dive into AIR's Data Processing Engine

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `44 min`

[Watch the recording](https://www.youtube.com/watch?v=zmoF3lKy520) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Scaling Training and Batch Inference- A Deep Dive into AIR's Data Processing Engine

Are you looking to scale your ML pipeline to multiple machines? Are you encountering an ingest bottleneck, preventing you from saturating your GPUs? This talk will cover how Ray AIR uses Ray Datasets for efficient data loading and preprocessing for both training and batch inference, diving into how AIR uses Datasets to achieve high performance and scalability.

We start by giving an overview of creating training and batch inference pipelines using Ray AIR. Next, we dive into the Ray Datasets internals, detailing features such as distributed data sharding, parallel + distributed I/O and transformations, pipelining of CPU and GPU compute, autoscaling pools of inference workers, and efficient per-epoch shuffling. Finally, we present case studies of users that have deployed such AIR workloads to production and have seen the performance + scalability benefits.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
