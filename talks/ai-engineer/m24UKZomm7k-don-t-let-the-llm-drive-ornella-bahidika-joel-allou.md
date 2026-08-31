---
id: m24UKZomm7k
title: "Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft"
slug: don-t-let-the-llm-drive-ornella-bahidika-joel-allou
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 6
published_at: 2026-07-20T00:00:00Z
video_id: m24UKZomm7k
youtube_url: https://www.youtube.com/watch?v=m24UKZomm7k
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=m24UKZomm7k) · [Conference site](https://www.ai.engineer/)

## Description

The LLM in my voice tutor doesn't decide when the lesson is over. It doesn't decide whether the user got the answer right. It doesn't decide which step comes next. A harness does all of that. The LLM just shows up and talks.

Every engineer who's tried to ship a multi-step flow agent has felt this: the model declares itself done before it should, skips a check, loops on a step, or quietly drops half the procedure. Prompting gets you most of the way. Tool-use discipline gets you closer. The last stretch, the difference between a demo and a system real users sign into every day, is owning the flow outside the model.

Ace is a voice tutor in production. The lesson is a small state machine: intro, teach, check, grade, advance, wrap. Each node hands the LLM a narrow contract: do this, return that. The harness validates the return, advances the state, decides what comes next. When the LLM tries to skip ahead the harness ignores it. When the LLM tries to declare the lesson finished the harness checks the actual completion signal. Same pattern for the shared canvas the agent draws on, for grading, for interruption handling.

Seven minutes. The state machine, the contract shape, a few places where I tried to give the LLM more authority and rolled it back, and a short list of decisions the LLM should never own in any flow agent.

Speakers:
- Ornella Bahidika (Microsoft): Ornella Bahidika is a Product Manager at Microsoft, where she develops solutions that help organizations optimize collaboration, workplace technology, and AI-driven experiences.
- Joel Allou: Joel builds voice-first AI tutors. Solo founder focused on agentic systems for personalized learning, with a particular interest in infrastructure that makes flow agents reliable.
