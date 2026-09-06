---
id: HzUUuRKFbws
title: "Dima Baranetskyi - Kafka Internals I Wish I Knew Sooner | PyData Amsterdam 2025"
slug: dima-baranetskyi-kafka-internals-i-wish-i-knew-sooner
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: ["Dima Baranetskyi"]
channel: "PyData"
duration_min: 35
published_at: 2025-10-30T04:00:32Z
video_id: HzUUuRKFbws
url: https://www.youtube.com/watch?v=HzUUuRKFbws
youtube_url: https://www.youtube.com/watch?v=HzUUuRKFbws
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Data engineering & MLOps"]
transcript: false
---

# Dima Baranetskyi - Kafka Internals I Wish I Knew Sooner | PyData Amsterdam 2025

**Dima Baranetskyi**

`PyData` · `PyData` · `2025` · `35 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=HzUUuRKFbws) · [Conference site](https://pydata.org/)

## Description

www.pydata.org

Most of us start with Kafka by building a simple producer/consumer demo. It just works — until it doesn’t. Suddenly, disk space isn’t freed up after data “expires,” rebalances loop endlessly during deploys, and strange errors about missing leaders clog your logs.
In the panic, we dive into Kafka’s ocean of config options — hoping something will stick. Sound familiar?

This talk is a collection of hard-won lessons — not flashy tricks, but the kind of insights you only gain after operating Kafka in production for years. You’ll walk away with mental models that make Kafka’s internal behavior more predictable and less surprising.

We’ll cover:

- Storage internals: Why expired data doesn’t always free space — and how Kafka actually reclaims disk
- Transactions & delivery semantics: What “exactly-once” really means, and when it silently downgrades
- Consumer group rebalancing: Why rebalances loop, and how the controller’s hidden behavior affects them

If you’ve used Kafka — or plan to — these insights will save you hours of frustration and debugging.
A basic understanding of partitions, replication, and Kafka’s general architecture will help get the most out of this session.

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
