---
id: 5YSJEP0HWzM
title: "Personalization in the Era of LLMs - Shivam Verma, Spotify"
slug: personalization-in-the-era-of-llms-shivam-verma-spotify
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Shivam Verma"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-05-19T13:00:06Z
video_id: 5YSJEP0HWzM
youtube_url: https://www.youtube.com/watch?v=5YSJEP0HWzM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Personalization in the Era of LLMs - Shivam Verma, Spotify

**Shivam Verma**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=5YSJEP0HWzM) · [Conference site](https://www.ai.engineer/)

## Description

Spotify represents Ariana Grande and Bruno Mars as sequences of six tokens. The first two are shared because both are pop artists. The remaining tokens diverge to capture what makes each distinct. That is a Semantic ID, and it is how Spotify teaches open-weight LLMs to reason over a catalog of 100 million tracks the same way they reason over words.

Shivam Verma from Spotify's AI foundation team walks through the three components they assembled to personalize LLMs at scale without full fine-tuning. User embeddings trained on streaming history across 750 million users form the base. Semantic IDs compress catalog vectors into tokens the model can autoregressively generate, predicting the next song or episode as the next token in a sequence. A soft tokenization layer projects a user's embedding directly into the LLM's token space, giving the frozen model a user-specific token to attend over. Podcast next-episode recommendations are already running on this stack in production.

Speaker info:
- https://x.com/kaffeinated
- https://www.linkedin.com/in/shivam13verma
