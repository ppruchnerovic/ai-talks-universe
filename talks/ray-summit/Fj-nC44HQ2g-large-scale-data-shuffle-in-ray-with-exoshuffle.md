---
id: Fj-nC44HQ2g
title: "Large-scale data shuffle in Ray with Exoshuffle"
slug: large-scale-data-shuffle-in-ray-with-exoshuffle
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: "Anyscale"
duration_min: 26
published_at: 2023-02-09T02:21:18Z
video_id: Fj-nC44HQ2g
url: https://www.youtube.com/watch?v=Fj-nC44HQ2g
youtube_url: https://www.youtube.com/watch?v=Fj-nC44HQ2g
tags: []
transcript: false
---

# Large-scale data shuffle in Ray with Exoshuffle

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=Fj-nC44HQ2g) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Large-scale data shuffle in Ray with Exoshuffle

Shuffle is a key primitive in large-scale data processing applications. The difficulty of large-scale shuffle has inspired a myriad of implementations. While these have greatly improved shuffle performance and reliability over time, it comes at a cost: flexibility. We show that contrary to the popular wisdom, shuffle can be implemented with high performance and reliability on a general-purpose system for distributed computing: Ray. In this talk we present Exoshuffle, an application-level shuffle system that outperforms Spark and achieves 82% of theoretical performance on a 100TB sort on 100 nodes. In Ray 2.0, we have integrated Exoshuffle with the Datasets library to provide high-performance large-scale shuffle for ML users.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
