---
id: IQkVMvXQKLY
title: "Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis"
slug: your-llm-deception-monitor-is-broken-the-fix-is-in-the
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sachin Kumar"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-07-08T08:05:21Z
video_id: IQkVMvXQKLY
youtube_url: https://www.youtube.com/watch?v=IQkVMvXQKLY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

**Sachin Kumar**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=IQkVMvXQKLY) · [Conference site](https://www.ai.engineer/)

## Description

You fine-tune LLMs and ship them. Your evals are green, your behavioral monitors are green — and a sleeper-agent backdoor can still flip the model to harmful output on a trigger you never tested. Behavioral testing can't reach it, and the interpretability tool people reach for — joint cross-model features (crosscoders) — dilutes the signal until it sits at the noise floor.

The fix is in what the training data changed. A backdoor is a directional shift that fine-tuning writes into the model's activations, so you isolate it by watching the difference between the base and fine-tuned model. In a controlled SQL-injection backdoor, a sparse autoencoder trained on that difference flags it with 40× the signal of joint features, perfect precision, and zero false positives — from a single cheap layer. You'll leave knowing how to wire a "delta monitor" into your fine-tuning pipeline as a quiet CI gate. Based on my peer-reviewed paper accepted at IJCNN.

Speakers:
- Sachin Kumar (LexisNexis): Sachin Kumar is a Senior Data Scientist III and Tech Lead at LexisNexis, building agentic AI for the legal domain. His independent AI-safety and interpretability research has been accepted at top-tier venues including ACL, AAAI, and IJCNN.
