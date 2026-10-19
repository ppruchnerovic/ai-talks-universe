---
id: 7AebpJri-T8
title: "The Moving Target: Benchmarking Dynamic AI Systems End-to-End - Gaëtan Brison - Doctolib - dotAI 26"
slug: the-moving-target-benchmarking-dynamic-ai-systems-end-to
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Gaëtan Brison"]
channel: "dotconferences"
duration_min: 18
published_at: 2026-09-28T14:00:25Z
video_id: 7AebpJri-T8
url: https://www.youtube.com/watch?v=7AebpJri-T8
youtube_url: https://www.youtube.com/watch?v=7AebpJri-T8
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "Multimodal, vision, speech & robotics", "Science, healthcare & applied ML", "Training, fine-tuning & model building"]
transcript: false
---

# The Moving Target: Benchmarking Dynamic AI Systems End-to-End - Gaëtan Brison - Doctolib - dotAI 26

**Gaëtan Brison**

`dotAI` · `dot conferences` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=7AebpJri-T8) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Gaëtan Brison, AI Manager at Doctolib: https://www.dotai.io/

Gaëtan is an AI Manager at Doctolib. Together with his team, he works closely with the AI Lab to enhance models through various retrieval and post-training approaches. He has contributed to several open-source initiatives in NLP, computer vision, and optimization.

Previously, he served as an AI Research Engineering Manager at Institut Polytechnique de Paris and also worked at NYU and Amazon. His main areas of interest include foundation models and multimodal systems.

Talk: "The Moving Target: Benchmarking Dynamic AI Systems End-to-End"

AI systems don't stand still — so why should our evaluation frameworks?

At Doctolib, we are building a complex ecosystem of AI agents spanning triage, clinical interview, retrieval, memory, booking, and image understanding. Evaluating each component in isolation is no longer enough. In a medical context, what matters is whether the system as a whole performs reliably — across multiple turns, multiple sessions, and across successive versions as the product evolves.

In this talk, we explore how to build an end-to-end evaluation framework for dynamic, multi-agent AI systems in high-stakes healthcare settings. We tackle the core challenge head-on: how do you test a moving target?

We introduce the concept of synthetic users — AI-powered personas that simulate realistic patient journeys, enabling systematic and reproducible evaluation at scale without compromising real patient data. We show how synthetic users allow us to stress-test agent pipelines across diverse scenarios, edge cases, and failure modes — including interactions with external systems.

But evaluation goes beyond task completion. In a medical setting, what the AI says matters as much as what it does. We dive into the challenge of managing context integrity across long multi-turn conversations — ensuring the system neither loses track of critical information nor hallucinates facts that were never grounded in the conversation. We present our approach to measuring groundedness: how well agent responses stay anchored to verified sources, retrieved documents, and the actual patient context — rather than drifting into confabulation.
