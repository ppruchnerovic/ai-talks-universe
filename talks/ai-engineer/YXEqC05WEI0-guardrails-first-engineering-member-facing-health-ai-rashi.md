---
id: YXEqC05WEI0
title: "Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health"
slug: guardrails-first-engineering-member-facing-health-ai-rashi
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rashi Agrawal"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-08-19T00:00:00Z
video_id: YXEqC05WEI0
youtube_url: https://www.youtube.com/watch?v=YXEqC05WEI0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health

**Rashi Agrawal**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YXEqC05WEI0) · [Conference site](https://www.ai.engineer/)

## Description

A healthy 60 year old man asked a popular AI assistant how to cut salt from his diet. It pointed him at sodium bromide. Three months later he arrived in an emergency room with paranoia and hallucinations, bromide at 200 times the safe level, and stayed three weeks. Rashi Agrawal stacks that against the first independent safety test of a consumer health AI, out of Mount Sinai, which under triaged life threatening emergencies half the time, and against ECRI naming chatbot misuse the top health technology hazard of 2026. Roughly 40 million people already triage themselves this way. None of it is a frontier problem. It is the production baseline.

Her argument is that most healthcare AI safety failures are architectural decisions made before a single token is generated. PHI is stripped at the pipeline boundary on ingestion, so a developer who opens a dashboard finds nothing to redact because it was never stored. Anything that can never be wrong lives in a code layer above the model rather than in its prompt: routing to 911 or 988, deciding which capability owns a turn, verifying who is on the other end. The frontier labs publish an authority hierarchy in which every layer above the user sits one prompt injection from being overridden, and her reading is blunt: if they will not treat a prompt as a security boundary, neither should you. Safety then runs as a continuous layer of judges scoring live traffic, with one discipline attached. When a score drops, first ask whether the judge is right.

Speaker info:
- https://www.linkedin.com/in/rashi283/
- https://sessionize.com/rashiagrawal/

Timestamps:
0:00 - The state of healthcare AI, and 40 million self triagers
1:04 - Poisoned by a chatbot
1:30 - Under triaging emergencies half the time
2:35 - Three non negotiable foundations
3:41 - Where PHI actually lives
5:53 - Deterministic rules belong above the model
7:27 - If the labs will not trust the prompt, neither should you
7:54 - Escalation, intent routing, identity
9:39 - Safety as a continuous evaluation layer
12:47 - Five stakeholders, five risks, five days to launch
14:02 - The five rules for deciding
18:10 - Verify the scorer before you trust the score
20:24 - The whole talk in one slide
