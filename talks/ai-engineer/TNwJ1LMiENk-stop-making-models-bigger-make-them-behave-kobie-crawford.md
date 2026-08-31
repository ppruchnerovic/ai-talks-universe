---
id: TNwJ1LMiENk
title: "Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel"
slug: stop-making-models-bigger-make-them-behave-kobie-crawford
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kobie Crawford"]
channel: null
duration_min: 21
published_at: 2026-06-10T17:00:25Z
video_id: TNwJ1LMiENk
youtube_url: https://www.youtube.com/watch?v=TNwJ1LMiENk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

**Kobie Crawford**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=TNwJ1LMiENk) · [Conference site](https://www.ai.engineer/)

## Description

Qwen 3 235B was asked for YouTube's year over year ad revenue growth from 2023 to 2024. It queried a table that didn't exist, tried again, got nothing back both times, and hallucinated an answer. The 4B model Snorkel finetuned with RL called `get_table_name` first, inspected the schema, ran a query, hit a column error, self-corrected, and got the right answer. The training run cost under $500.

Kobe Crawford covers why tool discipline matters more than reasoning depth for this class of tasks, how single table training transferred cleanly to harder multi table problems (13.9% to 26.6% on the FinQA reasoning benchmark), and why breaking evals into rubrics helps identify which specific behavior to fix before writing any training data.

Speaker info:
- https://www.linkedin.com/in/kobie-crawford
- https://snorkel.ai/author/kobie-crawford/
