---
id: YYH0DMQr30A
title: "Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel"
slug: task-fidelity-scaling-laws-kobie-crawdord-snorkel
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kobie Crawdord"]
channel: null
duration_min: 21
published_at: 2026-06-02T17:00:39Z
video_id: YYH0DMQr30A
youtube_url: https://www.youtube.com/watch?v=YYH0DMQr30A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel

**Kobie Crawdord**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YYH0DMQr30A) · [Conference site](https://www.ai.engineer/)

## Description

Same model. Same compute. Same number of tasks. Fine-tuning on low quality tasks improved the base model by 1%. Fine-tuning on high quality tasks improved it by 6%. Kobe Crawford from Snorkel ran that experiment on TerminalBench style agentic tasks and got a 5x difference in training uplift from task quality alone.

The talk breaks down what separates the two buckets. Accepted tasks averaged twice as many tool calls, lower pass rates, and more output tokens. Genuinely harder problems. More importantly, their failure modes were cleaner: when a model failed on a well specified task, it failed for a real reason. Rejected tasks tended to fail because of mismatches between what was requested and what the tests actually checked, or because the task never gave the model the context needed to satisfy implicit dependencies. Ambiguous specs do not produce harder tasks. They produce noise.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/
