---
id: -TiET_K-E_g
title: "From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google"
slug: from-46-to-90-fine-tuning-tiny-llms-for-on-device-agents
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Cormac Brick"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-05-20T00:00:00Z
video_id: -TiET_K-E_g
youtube_url: https://www.youtube.com/watch?v=-TiET_K-E_g
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

**Cormac Brick**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-TiET_K-E_g) · [Conference site](https://www.ai.engineer/)

## Description

Function Gemma ships at 270 million parameters and processes nearly 2,000 tokens per second prefill on a Pixel 7. Out of the box, on a fixed set of app intents, it hits 46% accuracy. Fine-tuned on a synthetically generated dataset, it clears 90% on eight of ten functions.

Cormac Brick covers the two options developers have for on-device AI: Gemini Nano via AI core for common tasks, and LiteRT-LM for custom models that ship inside your app. The session walks through a live skill harness built on Gemma 4 with a restaurant roulette demo running fully on-device, and Eloquent, a production transcription app built by chaining two models under a few hundred million parameters.

Speaker info:
- https://www.linkedin.com/in/cbrick/

Timestamps:
0:00 Introduction to on-device agents and tiny LLMs
0:48 Overview of AI Edge, SLMs, and TLMs
0:57 Taking a look at agent skills
1:06 Taking a look at tiny models
1:24 Motivations for on-device AI (latency, privacy, offline use)
3:01 System-level GenAI (Gemini Nano via AI Core)
4:03 App-level GenAI (LiteRT-LM for custom/boutique models)
5:06 Google AI Edge Gallery app demo
6:22 Deep dive into agent skills and the skill harness
7:41 How the skill harness works (system prompts, tool calls, and JavaScript UI)
9:00 Creating and publishing your own skills
10:28 Using LiteRT-LM runtime for model deployment
12:31 Export and inference workflow (from PyTorch to deployment)
13:19 Function Gemma: Robust, small-scale function calling
14:35 Fine-tuning workflow for tiny models using synthetic data
16:01 Eloquent: A production transcription app example using tiny models
17:28 Q&A: Agent skill robustness and multi-skill calling
19:26 Q&A: LiteRT-LM file format vs. Task files
20:00 Q&A: Performance on CPU/TPU and resources
