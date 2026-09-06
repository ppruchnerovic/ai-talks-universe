---
id: ZrNUppuQDhM
title: "Abhishek Murthy-Applying Foundational Models for Time Series Anomaly Detection-PyData Boston 2025"
slug: abhishek-murthy-applying-foundational-models-for-time
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: []
channel: "PyData"
duration_min: 41
published_at: 2025-12-15T19:18:25Z
video_id: ZrNUppuQDhM
url: https://www.youtube.com/watch?v=ZrNUppuQDhM
youtube_url: https://www.youtube.com/watch?v=ZrNUppuQDhM
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science"]
transcript: false
---

# Abhishek Murthy-Applying Foundational Models for Time Series Anomaly Detection-PyData Boston 2025

**Speaker not identified**

`PyData` · `PyData` · `2025` · `41 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=ZrNUppuQDhM) · [Conference site](https://pydata.org/)

## Description

The time series machine learning community has begun adopting foundational models for forecasting and anomaly detection. These models, such as TimeGPT, MOMENT, Morai, and Chronos, offer zero-shot learning and promise to accelerate the development of AI use cases.

In this talk, we'll explore two popular foundational models, TimeGPT and MOMENT, for Time Series Anomaly Detection (TSAD). We'll specifically focus on the Novelty Detection flavor of TSAD, where we only have access to nominal (normal) data and the goal is to detect deviations from this norm.

TimeGPT and MOMENT take fundamentally different approaches to novelty detection.

• TimeGPT uses a forecasting-based method, tracking observed data against its forecasted confidence intervals. An anomaly is flagged when an observation falls sufficiently outside these intervals.

• MOMENT, an open-source model, uses a reconstruction-based approach. The model first encodes nominal data, then characterizes the reconstruction errors. During inference, it compares the test data's reconstruction error to these characterized values to identify anomalies.

We'll detail these approaches using the UCR anomaly detection dataset. The talk will highlight potential pitfalls when using these models and compare them with traditional TSAD algorithms.

This talk is geared toward data scientists interested in the nuances of applying foundational models for TSAD. No prior knowledge of time series anomaly detection or foundational models is required.
