---
id: XQmbTpXfcvo
title: "Devoxx Greece 2025 - Elasticsearch Serverless: the Transition from Stateful to Stateless"
slug: devoxx-greece-2025-elasticsearch-serverless-the-transition
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2025
speakers: ["Iraklis Psaroudakis"]
channel: "Devoxx"
duration_min: 40
published_at: 2025-04-22T15:39:17Z
video_id: XQmbTpXfcvo
url: https://www.youtube.com/watch?v=XQmbTpXfcvo
youtube_url: https://www.youtube.com/watch?v=XQmbTpXfcvo
tags: []
topics: []
transcript: false
---

# Devoxx Greece 2025 - Elasticsearch Serverless: the Transition from Stateful to Stateless

**Iraklis Psaroudakis**

`Devoxx` · `Devoxx` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=XQmbTpXfcvo) · [Conference site](https://devoxx.com/)

## Description

Speaker : Iraklis Psaroudakis

Modern-day observability & security demand fast-paced searches in ever-increasing data volumes. Elasticsearch (ES), at the core of the Elastic Stack, is a leading distributed AI search and analytics engine. ES has been stateful so far, using primarily the disk to store data. In this presentation, we show the technical design of the new ES Serverless (ES3) mode, that achieves unparalleled scalability without any administration burden. We focus on the basic premise of decoupling compute from storage, and offloading data to an affordable highly available object store (e.g., S3), while supporting the same APIs and read-after-write semantics. Specifically, we show why and how we simplify node tiers to just two: indexing and search. We describe how we use batched compound commits to wrap Lucene files onto the object store, how the translog is buffered on the object store for recovery, and how refresh and search semantics operate.
