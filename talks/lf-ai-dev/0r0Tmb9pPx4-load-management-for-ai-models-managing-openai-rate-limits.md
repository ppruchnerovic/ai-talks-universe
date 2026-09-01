---
id: 0r0Tmb9pPx4
title: "Load Management for AI Models - Managing OpenAI Rate Limits with Request Prioritization- Harjot Gill"
slug: load-management-for-ai-models-managing-openai-rate-limits
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI.dev 2023"
year: 2023
speakers: []
channel: "The Linux Foundation"
duration_min: 31
published_at: 2023-12-18T18:32:24Z
video_id: 0r0Tmb9pPx4
youtube_url: https://www.youtube.com/watch?v=0r0Tmb9pPx4
tags: []
transcript: false
---

# Load Management for AI Models - Managing OpenAI Rate Limits with Request Prioritization- Harjot Gill

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI.dev 2023` · `2023` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=0r0Tmb9pPx4) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Load Management for AI Models - Managing OpenAI Rate Limits with Request Prioritization - Harjot Gill, FluxNinja

As AI-driven applications rapidly emerge, organizations face API rate limits, specially when interfacing with external services such as OpenAI. These AI APIs, are often slower than traditional APIs, and can have a typical 30s response time for complex tasks using models like gpt-4.

OpenAI imposes fine-grained rate limits to manage infrastructure load and ensure fair user access, which often leads to 429 errors when request limit is exceeded. While traditional retry and back-off strategies exist, they fall short. For example, OpenAI provides rate limiting headers, but aren't helpful in determining the optimal back-off times, due to headers that are outdated by tens of seconds and don’t consider in-flight requests.

In this talk, we’ll introduce Aperture, an open source load management platform that offers advanced rate-limiting, request prioritization, and quota management capabilities for AI models. We'll share insights from CodeRabbit, which specializes in PR reviews using OpenAI models, and how Aperture helped them ensure a reliable experience by facilitating client-side rate limits with business-attribute-based request prioritization as they continue to grow their user base.
