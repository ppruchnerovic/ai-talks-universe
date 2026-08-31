---
id: maTp79FD9gI
title: "Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens"
slug: agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Bala Ramdoss"]
channel: null
duration_min: 14
published_at: 2026-07-20T00:00:00Z
video_id: maTp79FD9gI
youtube_url: https://www.youtube.com/watch?v=maTp79FD9gI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens

**Bala Ramdoss**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=maTp79FD9gI) · [Conference site](https://www.ai.engineer/)

## Description

Getting a model to produce the right output is the part everyone works on. Turning that output into something people will actually use is the part that decides whether an AI feature ships. This talk is about that layer, the one between model output and the product experience, grounded in lessons from building agentic CX on mobile at the scale of hundreds of millions of devices.

Most teams building agentic CX hit the same wall: the feature works, the demo is impressive, and then production UX becomes less than ideal. Latency feels broken. The interface has no idea what to do when the model returns a content type it has never seen before. These are not model problems. They are delivery problems, and they live in an engineering layer the industry is only now naming: generative UI.

The rendering contract: a typed, versioned agreement between model output and your UI components, with a deliberate fallback for unknown types, so a new content type degrades gracefully instead of breaking production across a client base you cannot hot-fix.

Streaming into structured UI: progressively rendering streamed model output into typed components like product cards, comparison modules, and follow-up prompts, so the interface assembles as the response arrives instead of waiting for a complete one.

BFF patterns for AI features: a Backend-for-Frontend layer that absorbs model unpredictability away from the client while preserving conversational context across turns.

Speakers:
- Bala Ramdoss (Amazon): Bala Ramdoss is a Tech lead at Amazon, where he builds camera-based AI features like Amazon Lens to enhance the visual shopping experience.
