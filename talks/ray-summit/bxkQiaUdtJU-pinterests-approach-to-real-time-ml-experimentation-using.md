---
id: bxkQiaUdtJU
title: "Pinterest’s Approach to Real-Time ML Experimentation Using Ray | Ray Summit 2025"
slug: pinterests-approach-to-real-time-ml-experimentation-using
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 30
published_at: 2025-11-18T23:12:10Z
video_id: bxkQiaUdtJU
url: https://www.youtube.com/watch?v=bxkQiaUdtJU
youtube_url: https://www.youtube.com/watch?v=bxkQiaUdtJU
tags: []
topics: ["Classic ML & data science"]
transcript: false
---

# Pinterest’s Approach to Real-Time ML Experimentation Using Ray | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=bxkQiaUdtJU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Sameer Jain, Filip Ryzner, and Kritarth Anand from Pinterest share how they transformed one of the company’s most critical bottlenecks—dataset curation and label generation—into a fast, iterative, and cost-efficient workflow powered by Ray.
They begin by outlining a major challenge at Pinterest: improving recommendation models depends on continuous iteration over sampling strategies, feature selection, and long-term engagement labels—but existing data generation workflows made this nearly impossible. Teams were forced to choose between expensive, compute-intensive backfills costing thousands of dollars and requiring tedious monitoring, or waiting weeks for new data to naturally populate experimental datasets. Both paths severely limited developer velocity.
Two core use cases exemplify this problem:

Sampling strategy exploration, where the composition and quality of training data directly impacts model performance, yet iterating on sampling approaches was prohibitively slow and costly.

Downstream engagement label generation, which relies on multi-parameter definitions of long-term user engagement, creating vast hyperparameter search spaces that were infeasible to explore under the old pipeline.

To overcome these barriers, the Pinterest team shifted from static dataset generation to a real-time streaming paradigm built on Ray. By moving sampling and label-generation logic directly into the training dataloader, teams can now process data on the fly—unlocking true iterative experimentation and enabling extensive hyperparameter search without backfills or long waits.
This new Ray-powered pipeline has produced transformative results:

Sampling updates for ranking models ship 10× faster

Engagement label iteration dropped from 6 weeks to 3 days

Multiple teams have adopted the approach

Ray’s bucket join capabilities allow joining massive embedding features and multi-day datasets that were previously cost-prohibitive

Overall, Pinterest has saved hundreds of thousands of dollars in compute costs

In this talk, they share how Pinterest unified sampling, labeling, and training into a single scalable pipeline—turning dataset iteration from a fundamental bottleneck into a catalyst for rapid model improvement.

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
