---
id: vh2VGuQ3zhY
title: "The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica"
slug: the-100-tool-agent-is-a-trap-sohail-shaikh-ankush-rastogi
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 28
published_at: 2026-06-28T15:15:15Z
video_id: vh2VGuQ3zhY
youtube_url: https://www.youtube.com/watch?v=vh2VGuQ3zhY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `28 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vh2VGuQ3zhY) · [Conference site](https://www.ai.engineer/)

## Description

The common “Fat Agent” architecture loads a large catalog of tools directly into the system prompt. This often creates latency, cost, and reliability problems in production agent systems. As tool schemas take up more of the context window, agents can become slower and more likely to choose the wrong tool.

This session takes a practical look at the Semantic Tool Router pattern, a deterministic layer that reduces the amount of context shown to the model in real time. The talk will share benchmarks across frontier models, including GPT-4o and Gemini 2.0, showing how the number of available tools affects Time-to-First-Token latency and tool-selection accuracy.

Attendees will learn how to move from static tool loading to Just-in-Time Context Injection, where only the most relevant tools are added to the prompt for each request. In high-tool-density benchmark scenarios, this approach can reduce response latency by up to 90%, reduce cross-tool confusion, and improve agent reliability. The session will end with a practical framework for building tool routers that can scale to hundreds of capabilities without sacrificing speed or predictability.

Speakers:
- Sohail Shaikh (Prosodica): Sohail Shaikh is a data scientist with nearly a decade of experience across AI, data science, analytics, marketing, and software-oriented work, focused on building practical, reliable, and scalable AI systems using NLP, RAG, conversational intelligence, and LLM workflows.
- Ankush Rastogi (Prosodica): Ankush Rastogi is a Senior Data Solutions Engineer with over a decade of experience building scalable data, analytics, and machine learning platforms, with a focus on turning AI models into reliable, production-ready enterprise systems through strong evaluation, inference performance, cost optimization, and operational design.
