---
id: FlzpEGHNVKQ
title: "Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take"
slug: building-a-chess-coach-anant-dole-and-asbjorn-steinskog
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-05-13T00:00:00Z
video_id: FlzpEGHNVKQ
youtube_url: https://www.youtube.com/watch?v=FlzpEGHNVKQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FlzpEGHNVKQ) · [Conference site](https://www.ai.engineer/)

## Description

LLMs can explain things clearly but can't play chess reliably. Take Take Take (Magnus Carlsen's app) solved this by separating concerns: Stockfish handles position evaluation, tactical and positional detectors extract concepts like forks, pins, and structural weaknesses, and the LLM's only job is translating those structured signals into English. Keeping the model as a translator rather than a reasoner is what makes it work at sub-3-second latency for a consumer app.

Anant Dole and Asbjørn Steinskog also walk through how they closed the feedback loop. When a user flags bad commentary, it posts to Slack and injects the event into a running Claude Code session via Channels, a new MCP feature in research preview. Claude investigates the position, modifies prompts or detectors, regenerates the commentary, and asks clarifying questions back through Slack. During the live demo, Anant was reviewing the PR from his phone.

Speaker info:
- https://www.linkedin.com/in/asbj%C3%B8rn-ottesen-steinskog-a8000241/
- https://www.linkedin.com/in/anantdole/
