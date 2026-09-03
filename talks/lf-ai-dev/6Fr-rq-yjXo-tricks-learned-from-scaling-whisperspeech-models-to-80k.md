---
id: 6Fr-rq-yjXo
title: "Tricks Learned from Scaling WhisperSpeech Models to 80k+ Hours of Speech - Jakub Cłapa, Collabora"
slug: tricks-learned-from-scaling-whisperspeech-models-to-80k
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "AI.dev 2023"
year: 2023
speakers: []
channel: "The Linux Foundation"
duration_min: 35
published_at: 2023-12-18T18:32:25Z
video_id: 6Fr-rq-yjXo
url: https://www.youtube.com/watch?v=6Fr-rq-yjXo
youtube_url: https://www.youtube.com/watch?v=6Fr-rq-yjXo
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Tricks Learned from Scaling WhisperSpeech Models to 80k+ Hours of Speech - Jakub Cłapa, Collabora

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI.dev 2023` · `2023` · `35 min`

[Watch the recording](https://www.youtube.com/watch?v=6Fr-rq-yjXo) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Tricks Learned from Scaling WhisperSpeech Models to 80k+ Hours of Speech - Jakub Cłapa, Collabora

WhisperSpeech is a new OpenSource text to speech model created by Collabora and based on recent research from
the biggest AI research labs (Google, Meta, Microsoft, OpenAI). It delivers high quality speech that it learned from tens of thousands of hours of human speech recordings.

To deliver state of the art quality we scaled our models and training pipelines from hundreds to tens of thousands of hours of speech and we share the lessons learned along the way. Nearly every component of your initial training process had to be replaced or tweaked heavily.

Challenges we'll briefly cover:
- Gone in 16 minutes: the importance of small scale experiments.
- Full throttle: is 100% GPU utilization enough?
- Do you need a fancy framework? From single- to multi-GPU training.
- Are SSDs fast enough? WebDataset brings a 10x improvement.
- Does bigger always mean better? How to effortlesly scale AI models.
- Clouds, enthusiasts or clusters? How to hunt down GPUs.
- Defending moats. How is a gaming 4090 different from an H100?
