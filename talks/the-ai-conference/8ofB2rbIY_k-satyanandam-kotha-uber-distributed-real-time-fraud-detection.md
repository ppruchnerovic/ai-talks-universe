---
id: 8ofB2rbIY_k
title: "Satyanandam Kotha, Uber: Distributed Real-Time Fraud Detection"
slug: satyanandam-kotha-uber-distributed-real-time-fraud-detection
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 22
published_at: 2026-09-29T17:56:43Z
video_id: 8ofB2rbIY_k
url: https://www.youtube.com/watch?v=8ofB2rbIY_k
youtube_url: https://www.youtube.com/watch?v=8ofB2rbIY_k
tags: []
topics: ["Classic ML & data science", "Data engineering & MLOps"]
transcript: false
---

# Satyanandam Kotha, Uber: Distributed Real-Time Fraud Detection

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=8ofB2rbIY_k) · [Conference site](https://aiconference.com/)

## Description

Satyanandam Kotha, Staff Software Engineer, Uber

Distributed Real-Time Fraud Detection: A Scalable Architecture for Combating Fake Reviews in E-Commerce

This presentation introduces a cutting-edge distributed system for real-time fake review detection that addresses critical marketplace integrity challenges while delivering exceptional performance metrics. Our architecture leverages streaming data pipelines built on Apache Flink, Kafka, and Spark Streaming to process reviews as they arrive, enabling immediate identification of fraudulent activity with average detection latencies under 100 milliseconds—a substantial improvement over traditional batch-processing approaches.
The system employs a sophisticated hybrid detection model that combines natural language processing, graph neural networks, and behavioral analytics to identify complex fraud patterns. Our multi-model integration approach demonstrates a 0.94 precision score, significantly outperforming single-architecture alternatives that typically achieve 0.78-0.86 precision. The temporal pattern analysis component can detect coordinated campaigns involving as few as 8 accounts, with marked improvement in early detection rates compared to conventional methods.
For sophisticated collusion networks, our graph-based detection methodology achieves high detection rates for campaigns involving just 12 accounts—far exceeding non-graph approaches for similar operations. The system architecture scales near-linearly to 32 worker nodes with strong efficiency metrics, essential for processing massive review graphs containing 500 million to 3 billion edges.
Privacy and security remain paramount through our federated learning implementation, which achieves detection accuracy comparable to fully centralized approaches while dramatically reducing cross-organizational data exposure. Our differential privacy guarantees maintain F1 scores above 0.92 with privacy parameter ε = 4.6.
Production deployment across multiple e-commerce environments has demonstrated the system's effectiveness, substantially reducing fraudulent review prevalence while maintaining high availability. Resource utilization increases sub-linearly with traffic volume, and the system sustains low latency even at 5x normal traffic—critical for maintaining performance during promotional events when both legitimate and fraudulent review volumes typically spike.
This presentation will provide attendees with architectural insights and implementation strategies for building high-performance fraud detection systems that protect marketplace integrity and consumer trust.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved
