---
id: poJ1bdZJjLk
title: "When Prompting Runs Out: Post-Training an Open Model - Ziv Ilan - NVIDIA - dotAI 2026"
slug: when-prompting-runs-out-post-training-an-open-model-ziv
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Ziv Ilan"]
channel: "dotconferences"
duration_min: 21
published_at: 2026-09-28T14:00:21Z
video_id: poJ1bdZJjLk
url: https://www.youtube.com/watch?v=poJ1bdZJjLk
youtube_url: https://www.youtube.com/watch?v=poJ1bdZJjLk
tags: []
topics: ["Inference, serving & GPU infra", "Prompting & context engineering", "RAG, retrieval & knowledge", "Training, fine-tuning & model building"]
transcript: false
---

# When Prompting Runs Out: Post-Training an Open Model - Ziv Ilan - NVIDIA - dotAI 2026

**Ziv Ilan**

`dotAI` · `dot conferences` · `2026` · `21 min`

[Watch the recording](https://www.youtube.com/watch?v=poJ1bdZJjLk) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Ziv Ilan, AI Labs at NVIDIA: https://www.dotai.io/

Ziv Ilan works with AI labs at NVIDIA, where he previously served as a Senior Solutions Architect. With a background spanning software engineering, electrical engineering, and computer science, he helps research teams architect and scale the systems behind their AI models, bridging cutting-edge research with the infrastructure that brings it to production.

Talk "When Prompting Runs Out: Post-Training an Open Model"
There is a specific moment when prompt engineering, retrieval, and better tooling stop paying and post-training starts. Most teams miss it in both directions.

This talk maps the cheaper levers first - a newer base checkpoint, context engineering, RAG, tools, constrained decoding, routing - and the exit condition for each. Then what comes after: choosing between SFT, DPO, RL with verifiable rewards, and distillation by the learning signal you actually have, with real data and compute needs per method.

We'll use Nemotron as the worked example, having the weights, the datasets, and the training recipes all public - you can read every step, then run it on your own domain.
