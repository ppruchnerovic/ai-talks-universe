---
id: icizosswxsM
title: "How Stripe Moves Petabytes of Data with 5.5 Nines of Reliability"
slug: how-stripe-moves-petabytes-of-data-with-5-5-nines-of
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: null
duration_min: 44
published_at: 2026-05-28T06:19:13Z
video_id: icizosswxsM
youtube_url: https://www.youtube.com/watch?v=icizosswxsM
tags: ["QCon San Francisco", "InfoQ", "Transcript", "Case Study", "Stripe", "DocDB", "MongoDB", "open source", "software architecture", "Distributed Document Oriented Database", "NoSQL", "migration", "Database", "AI", "ML & Data Engineering", "system design", "distributed systems"]
transcript: false
---

# How Stripe Moves Petabytes of Data with 5.5 Nines of Reliability

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `44 min`

`#QCon San Francisco` `#InfoQ` `#Transcript` `#Case Study` `#Stripe` `#DocDB` `#MongoDB` `#open source` `#software architecture` `#Distributed Document Oriented Database` `#NoSQL` `#migration` `#Database` `#AI` `#ML & Data Engineering` `#system design` `#distributed systems`

[Watch the recording](https://www.youtube.com/watch?v=icizosswxsM) · [Conference site](https://qconferences.com/)

## Description

📩 Subscribe to the InfoQ Weekly newsletter!

No hype. No fluff. Just the signals senior engineers actually care about - from #AI, #DevOps, and #Java to #CloudComputing & #SoftwareArchitecture.

🗓️ Delivered every Tuesday, it's your quick round-up of innovator & early-adopter technologies.

Join 250,000+ developers who read it to stay ahead 👉 https://www.infoq.com/news/#infoq-nl
************************************************
How does Stripe process $1.4 trillion in payments annually with 5.5 nines of availability? Stripe Staff Software Engineer Jimmy Morzaria breaks down the custom zero-downtime data movement platform that powers their critical database tier.

Scaling database infrastructure for global commerce requires moving from treating shards like "pets" to an automated "herd." In this InfoQ, discover how Stripe handles 5 million database queries per second across 2,000+ MongoDB shards. Jimmy pulls back the curtain on why Stripe bypassed off-the-shelf solutions like MongoDB Atlas/mongos to build "DocDB" - their in-house Database-as-a-Service.

You’ll learn the exact blueprint for their zero-downtime horizontal data migration platform, including how they achieved a 10x write throughput boost using B-tree insertion ordering, orchestrated bidirectional replication for safe rollbacks, and implemented custom version gating for seamless traffic switching.

⏱️ Video Timestamps (For Navigation)
00:00 — The Hartsfield-Jackson Airport Engineering Analogy
01:30 — Stripe’s Scale: $1.4 Trillion & 5.5 Nines Reliability
02:45 — The Evolution of Stripe’s Database Infrastructure (2011–2020)
04:15 — Moving Beyond the Physical Limits of Vertical Scaling
05:30 — Architecture Deep Dive: Why Stripe Built DocDB In-House
07:45 — Blueprint for Zero-Downtime Data Movement (First Principles)
09:15 — Achieving 10x Write Throughput via B-Tree Optimization
10:45 — Bidirectional Replication & Ensuring Idempotency via the Oplog
12:30 — The Traffic Switch: Custom Version Gating Protocol
14:50 — Beyond Sharding: Black Friday prep & Skip-Major-Version Upgrades
17:15 — Q&A: Handling Split-Brain, Fencing Proxies, & Migration Speeds

🔗 Transcript & slides  available on InfoQ:   https://bit.ly/4dK2RId
