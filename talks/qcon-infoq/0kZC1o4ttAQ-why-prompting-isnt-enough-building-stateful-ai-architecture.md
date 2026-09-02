---
id: 0kZC1o4ttAQ
title: "Why Prompting Isn’t Enough: Building Stateful AI Architecture"
slug: why-prompting-isnt-enough-building-stateful-ai-architecture
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: "InfoQ"
duration_min: 53
published_at: 2026-07-06T09:44:57Z
video_id: 0kZC1o4ttAQ
url: https://www.youtube.com/watch?v=0kZC1o4ttAQ
youtube_url: https://www.youtube.com/watch?v=0kZC1o4ttAQ
tags: ["QCon AI", "InfoQ", "Transcript", "Context Engineering", "Prompt Engineering", "Software Architecture", "Stateful AI", "Apache Flink", "Apache Kafka", "Distributed Systems", "AI Agents"]
topics: ["Agents & orchestration", "Data engineering & MLOps", "Inference, serving & GPU infra", "Prompting & context engineering"]
transcript: false
---

# Why Prompting Isn’t Enough: Building Stateful AI Architecture

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `53 min`

`#QCon AI` `#InfoQ` `#Transcript` `#Context Engineering` `#Prompt Engineering` `#Software Architecture` `#Stateful AI` `#Apache Flink` `#Apache Kafka` `#Distributed Systems` `#AI Agents`

[Watch the recording](https://www.youtube.com/watch?v=0kZC1o4ttAQ) · [Conference site](https://qconferences.com/)

## Description

Most developers treat LLMs as stateless applications - sending a prompt, getting a response, and forgetting the rest. But building truly resilient, production-ready AI agents requires moving past prompt engineering and into the realm of Context Engineering and distributed state management.

In this InfoQ talk, Adi Polak breaks down how to leverage proven real-time streaming architectures like Apache Kafka and Apache Flink to build state-aware, low-latency AI agent systems.

Learn how to overcome the critical limitations of modern LLMs - such as token caps, cost spikes, and "lost in the middle" context degradation - by treating AI infrastructure as a stateful distributed system.

Discover how to implement multi-tiered memory structures (from ultra-fast SSD caching to long-term object storage) and see real-world implementations, including invoking LLMs via Model Context Protocol (MCP) using standard SQL and real-time anomaly detection workflows.

⏱️ Video Timestamps (For Navigation)
00:00 — The "Men in Black" Lesson: Why LLMs Need Real Context
01:45 — Prompt Engineering vs. Context Engineering
03:10 — The Paradigm Shift: Moving from Stateless to Stateful AI
04:55 — Core Architecture Bottlenecks: Latency, Tokens, & Cost Spikes
06:40 — Deep Dive: Scaling Streaming Agents with Apache Flink & Kafka
08:50 — Designing Memory Tiers: Short-Term SSD Caching to Long-Term Storage
10:35 — Code Walkthrough: Integrating LLMs & MCP inside SQL Queries
12:15 — Real-World Case Study: E*TRADE Volume Anomaly Detection
13:50 — Audience Q&A: Open-Source Availability & Managing Context Lengths

🔗 Transcript available on InfoQ:  https://bit.ly/4gXCEZW
