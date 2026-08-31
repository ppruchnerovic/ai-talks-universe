---
id: 4loPnxvWWhg
title: "Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End"
slug: your-fine-tuned-model-is-tech-debt-a-50x-roi-house-of-cards
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dan Bjornn"]
channel: null
duration_min: 17
published_at: 2026-08-20T16:00:22Z
video_id: 4loPnxvWWhg
youtube_url: https://www.youtube.com/watch?v=4loPnxvWWhg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End

**Dan Bjornn**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=4loPnxvWWhg) · [Conference site](https://www.ai.engineer/)

## Description

A customer replied good morning to an outreach text and the model called him immediately. Another confirmed a Thursday appointment, said sounds good, and was told a call was happening right now. Both reached production, from a finetuned classifier that had also generated $12 million of revenue at 50 times return inside a year. Dan Bjornn's talk is about what that model was quietly costing underneath those numbers, which he calls the calcification tax.

The repair loop is where it accrued. Gather examples of the new failure, synthesize more when there are too few, validate those by hand, sort them into intent buckets, review again, and only then train, which took about an hour and was the shortest step in a process that ran a week. Each round fixed its target and reintroduced something older, so bugs ended up ranked by how much customer pain was tolerable while they waited. The promised portability never arrived either, since training data does not transfer cleanly between model versions, let alone between providers, so they stayed put and could not adopt newer architectures while busy keeping the old one alive. The rebuild swapped the tuned model for skills, prompts, and context on a model agnostic framework. Fixes now ship in under an hour as files uploaded to a bucket, accuracy went up, cost per message went up, and total cost went down.

Speaker info:
- https://www.linkedin.com/in/dkbjornn

Timestamps:
0:00 - Classifying customer intent with retrieval
1:54 - Four reasons to finetune, all of them reasonable
3:32 - The pipeline, and $12 million at 50x return
4:24 - The confused confirmer, and the overeager puppy
6:04 - A week per retrain, with training the shortest step
8:39 - Ranking bugs by tolerable customer pain
9:31 - The calcification tax, in model and architecture
11:18 - The realization from changing skills, not models
12:14 - Rebuilding on skills, tools, and context
13:08 - Fixes in under an hour, deployed as files
14:54 - Cross your reason off the list before you finetune
