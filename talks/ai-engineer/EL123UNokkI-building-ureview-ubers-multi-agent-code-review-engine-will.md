---
id: EL123UNokkI
title: "Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber"
slug: building-ureview-ubers-multi-agent-code-review-engine-will
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 15
published_at: 2026-08-28T00:00:00Z
video_id: EL123UNokkI
youtube_url: https://www.youtube.com/watch?v=EL123UNokkI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=EL123UNokkI) · [Conference site](https://www.ai.engineer/)

## Description

In 2024 an Uber engineer waited about three hours for a first review on a pull request. In 2026 that wait is nine hours. Volume and size both grew, and code review became the bottleneck for thousands of engineers spread across hundreds of teams, twelve sites and six language specific monorepos. Will Bond and Ameya Ketkar walk through uReview, the system Uber built rather than bought, partly because most vendors do not support Phabricator and partly because they wanted agents in the inner loop reviewed against exactly the same rules as humans.

The instructive half is what they had to measure before it worked. Early observability was cost, an NPS survey and a Google form, and the quality to cost ratio landed all over the chart. Tracking reply sentiment, whether a comment actually got addressed, and the agent's own trajectory is what let them tune it, because a model never signals that it is wrong and will assert a bad review with full confidence. Teams write their own reviewers, and Ketkar is blunt that authoring a skill was the easy part while running skills at scale cheaply was not. It now posts about 25,000 comments a week, roughly 67% get addressed, and cost fell 60% against their naive first build.

Speaker info:
Will Bond:
- https://x.com/wbond
- http://linkedin.com/in/wbond
Ameya Ketkar:
- https://www.linkedin.com/in/ameya-ketkar
- https://scholar.google.com/citations?user=6JO46GMAAAAJ&hl=en

Timestamps:
0:00 - Three hours to review in 2024, nine in 2026
1:53 - Why Uber built this instead of buying it
3:42 - The architecture, and deduplicating comment volume
4:37 - Humble beginnings, and cost as the only metric
5:33 - Sentiment, addressal rate, agent trajectory
6:32 - The model never knows that it is wrong
7:26 - Letting hundreds of teams customize reviews
10:10 - Results: 25,000 comments a week
11:08 - Inner loop versus outer loop
13:57 - Expanding the outer loop rather than killing it
