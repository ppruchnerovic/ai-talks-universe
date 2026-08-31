---
id: hocPv10Uoro
title: "Calculating Drift, Fast with Goko"
slug: calculating-drift-fast-with-goko
conference: defcon-ai-village
conference_name: "DEF CON AI Village"
category: "AI security"
edition: "AI Village"
year: 2020
speakers: []
channel: null
duration_min: 33
published_at: 2020-08-08T04:21:03Z
video_id: hocPv10Uoro
youtube_url: https://www.youtube.com/watch?v=hocPv10Uoro
tags: []
transcript: false
---

# Calculating Drift, Fast with Goko

**Speaker not identified**

`DEF CON AI Village` · `AI Village` · `2020` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=hocPv10Uoro) · [Conference site](https://aivillage.org/)

## Description

Author: Sven Cattell

Normally concept or dataset drift is unquantifiable in practice. The only ways to calculate it are with optimal transport techniques that take O(n^4). The proxies some ML practitioners use are unreliable when applied to security. This talk presents a way to calculate a concept drift number that takes O(log n). It is faster than most inference, so can be put inline in an ML pipeline. Also, as the structure used to calculate the drift is so cheap we can apply it per-user as an extremely effective defense against attacks.

Repo: https://github.com/elastic/goko
