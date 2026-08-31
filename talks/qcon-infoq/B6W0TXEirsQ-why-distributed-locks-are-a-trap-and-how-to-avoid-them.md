---
id: B6W0TXEirsQ
title: "Why Distributed Locks are a Trap (and How to Avoid Them)"
slug: why-distributed-locks-are-a-trap-and-how-to-avoid-them
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: "InfoQ"
duration_min: 42
published_at: 2026-01-26T12:56:01Z
video_id: B6W0TXEirsQ
youtube_url: https://www.youtube.com/watch?v=B6W0TXEirsQ
tags: ["Artificial Intelligence", "Data Engineering", "QCon London", "Case Study", "Database", "Serverless", "Serverless Database", "ArcticDB", "InfoQ", "Transcript", "Database Design", "Cloud Computing", "S3", "Dystributed Systems", "Python"]
transcript: false
---

# Why Distributed Locks are a Trap (and How to Avoid Them)

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `42 min`

`#Artificial Intelligence` `#Data Engineering` `#QCon London` `#Case Study` `#Database` `#Serverless` `#Serverless Database` `#ArcticDB` `#InfoQ` `#Transcript` `#Database Design` `#Cloud Computing` `#S3` `#Dystributed Systems` `#Python`

[Watch the recording](https://www.youtube.com/watch?v=B6W0TXEirsQ) · [Conference site](https://qconferences.com/)

## Description

Build a high-performance time-series database directly on object storage without the overhead of traditional servers.

Alex Seaton from ArcticDB (Man Group) shares how one of the world's largest hedge funds replaced a massive MongoDB cluster with a "thick client" architecture that streams data at 40GB/s.

⏱️ Video Timestamps (For Navigation)
0:00 - The problem: Managing hedge fund data at scale
2:15 - Why MongoDB failed us (The "Arms Race" with users)
5:10 - What is a truly "Serverless" Database?
7:45 - Building atomicity and versioning on Object Storage
11:20 - Performance bottlenecks: CPU vs. I/O vs. Python overhead
14:50 - The Global State Problem: Managing millions of keys
18:30 - Deep Dive: Set CRDTs (Grow-only vs. Observed-Remove)
23:15 - Why Distributed Locks are a trap
27:00 - The Future: Atomic operations and conditional writes in S3
30:20 - Q&A: Retrofitting metadata and compaction strategies

🔗 Transcript available on InfoQ:  https://bit.ly/4pUUVbb
