---
id: 1UmZHb_E_SM
title: "How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs"
slug: how-web-data-infrastructure-powers-the-next-generation-of
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-14T17:00:37Z
video_id: 1UmZHb_E_SM
youtube_url: https://www.youtube.com/watch?v=1UmZHb_E_SM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=1UmZHb_E_SM) · [Conference site](https://www.ai.engineer/)

## Description

Minutes into a call to demo a search API rebuilt to answer in under a second, the system got blocked, badly, in front of the client. Patricija Žemaitytė treats that as the useful distinction: something that works in development, something that passes tests, and something that survives reality are three different systems. The rebuild had no trick to it. Browsers are slow, expensive, and incompatible with low latency, and they were unavoidable, so the team went hunting for time across layouts, parsers, sessions, and proxies until the seconds were gone. It averages 550 milliseconds now, against a 4 second baseline.

Two other stories run the same way. A video API request arrived with a two week deadline and a floor of 5 petabytes a month, then kept moving. The transcripts the client asked for turned out to be subtitles, then came search, then metadata, until a one off feature request had quietly become a product suite. The punchline she offers is that the client has since collected 30 petabytes and has not paid yet. Scaling the unblocker from 10,000 to 60,000 requests per second hit a wall around 20,000 in load testing, where the real difficulty was not generating synthetic traffic but knowing whether the number meant anything, since telemetry at that volume becomes part of the load it measures. Project 60 is already Project 150. Her argument throughout is that this is not a build once business, it is an adapt forever one.

Speaker info:
- https://www.linkedin.com/in/patricijazemaityte
- https://oxylabs.io/press-area/from-web-to-artificial-intelligence

Timestamps:
0:00 - Infrastructure, not models, as the starting point
2:23 - A video API with a two week deadline
4:08 - Transcripts, subtitles, search, metadata
5:51 - Thirty petabytes later, still unpaid
7:25 - A subsecond request, built and then shelved
8:42 - The rebuild, and getting blocked live on the call
10:53 - Hunting for time, second by second
12:26 - Scaling the unblocker to 60,000 per second
14:09 - Load testing, and the wall at 20,000
15:31 - Project 60 becomes Project 150
