---
id: 0jeZfjJMfmo
title: "Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face"
slug: reachy-mini-the-300-open-source-robot-you-can-actually-hack
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Andres Marafioti"]
channel: null
duration_min: 21
published_at: 2026-05-29T17:00:06Z
video_id: 0jeZfjJMfmo
youtube_url: https://www.youtube.com/watch?v=0jeZfjJMfmo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face

**Andres Marafioti**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0jeZfjJMfmo) · [Conference site](https://www.ai.engineer/)

## Description

Qwen3-TTS shipped at 0.8x real time: one second of audio took 1.2 seconds to generate. Andres Marafioti from Hugging Face spent two weeks fixing it. The culprits were no streaming, 500 autoregressive steps per audio packet with a CPU GPU round trip on each, and a dynamic KV cache that blocked compilation. Static KV cache plus CUDA graph captures brought it to 5.8x real time with time to first audio under 200 milliseconds.

The platform is Reachy Mini, a $300 open source robot Hugging Face has shipped to 7,500 people. It arrives unassembled. Talking to it is their most used app by far. The voice stack runs Parakeet transcription every 150 milliseconds with partial results feeding back to the robot mid-sentence, Qwen 3.5 27B for the LLM, and this optimized TTS. At that speed, infrastructure round trips match model latency, so the load balancer separates LLM endpoints from conversation nodes to handle the difference in how much different users actually talk.
