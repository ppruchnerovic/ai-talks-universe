---
id: 3jGAU2sbAyY
title: "Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral"
slug: why-tts-models-now-look-like-llms-samuel-humeau-mistral
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Samuel Humeau"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-05-09T17:00:07Z
video_id: 3jGAU2sbAyY
youtube_url: https://www.youtube.com/watch?v=3jGAU2sbAyY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral

**Samuel Humeau**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=3jGAU2sbAyY) · [Conference site](https://www.ai.engineer/)

## Description

The dominant architecture pattern for text-to-speech in 2026 looks a lot like an LLM — an autoregressive transformer generating sequences of tokens, one frame of audio at a time. Samuel Humeau from Mistral walks through why the field converged there, how neural audio codecs solve the information-density problem (audio carries ~200kbps of signal; you can't feed that raw to a transformer), and what the streaming trick actually is that makes voice agents feel responsive before the full audio has even finished generating.

The talk uses Mistral's just-released open-weight TTS model as a running example — live demos of voice cloning from a few seconds of reference audio, a voice agent answering real conference schedule questions, and a breakdown of the codec-to-backbone-to-decoder pipeline that produces it all. There's also a frank section on what's still unsettled: how to handle streaming text input (tokens arriving from an LLM in real time rather than a fixed block of text) and why getting that right is the next meaningful latency win in agent pipelines.

It's the kind of talk that makes the system feel less like a black box — not by oversimplifying, but by showing exactly which engineering choices are load-bearing and which are still open problems.

Speaker info:
- https://x.com/DrSamuelBHume
- https://www.linkedin.com/in/samuelhumeau/

Timestamps:
0:00 Introduction and Mistral's new open-source TTS model
2:06 Text-to-speech in AI agents and latency
3:33 Live demo: Voice cloning with 'Paul'
6:00 Voice cloning capabilities and multilingual examples
8:01 Historical context of audio generation
8:55 Transformer-based architecture for TTS
10:00 Challenges of information density in audio
10:55 Comparison of bit rates: text vs. audio
11:39 Using neural audio codecs
13:10 Backbone transformer and frame-based generation
14:56 Text conditioning and model architecture
16:08 Latency performance metrics
16:22 Future outlook: Streaming text input
17:35 Q&A: Generating text and audio simultaneously
18:24 Q&A: Availability of voice cloning features
19:35 Q&A: Philosophical take on speech interfaces
20:44 Q&A: Next steps for streaming audio and text input
