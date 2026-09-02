---
id: co3logJvghQ
title: "From One Voice to Forty: Inside Vimeo’s Dubbing Engine"
slug: from-one-voice-to-forty-inside-vimeos-dubbing-engine
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2025
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 33
published_at: 2025-07-27T09:55:33Z
video_id: co3logJvghQ
url: https://www.youtube.com/watch?v=co3logJvghQ
youtube_url: https://www.youtube.com/watch?v=co3logJvghQ
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Prompting & context engineering"]
transcript: false
---

# From One Voice to Forty: Inside Vimeo’s Dubbing Engine

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2025` · `33 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=co3logJvghQ) · [Conference site](https://mlopsworld.com/)

## Description

Tanushree Nori, Principal Data Scientist, Vimeo
Gautham Anil, Senior Data Scientist, Vimeo

About the Speaker:
Tanushree Nori is a Principal Data Scientist at Vimeo, where for the past 4½ years she’s built LLM-powered features—Video Insights, Chapters, Summaries, Highlights, and multilingual Dubbing—that help viewers unlock more value from every upload. Her earlier work on cloud-storage optimization now saves the platform about $1 million annually and was showcased at Demuxed 2024 in San Francisco. When she isn’t dissecting LLM evals for fun, Tanushree is dancing—bringing her Indian classical foundation into hip-hop and house for a trippy, vibrant fusion.

Abstract:
Imagine every video greeting viewers in their own language—no studio booth, no red-eye caption sprints. Vimeo’s new pipeline turns a single upload into time-locked captions and natural-sounding dubs, almost as fast as the video plays.
1. Gemini Flash 2.0 handles translating transcripts fast enough that you can watch progress in real-time.
2. Careful chain-of-thought prompting coaxes phoneme details of translations, so we can contract roomy German syllables or subtly expand packed Mandarin ones before the subtitles and dubs wander off-beat.
3. Our chunking strategy that pins every subtitle segment to its timestamp, keeping drift under 10 ms.
4. Spot a rare error in the subs? Segment-level re-edit lets you fix a single line; only that slice gets re-translated (and re-dubbed if so wished).
5. A creative and thorough eval framework to run translation experiments.

We’ll share the system design involved, prompting tricks, the timing math, and a few war stories when subs and dubs went rogue—plus the metrics and eval methodology that convinced us the system was ready for production.
