---
id: 504PvfXou5Y
title: "BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence"
slug: bdd-adr-prd-wtf-capturing-decisions-for-humans-and-ai-alike
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Michal Cichra"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-06-03T00:00:00Z
video_id: 504PvfXou5Y
youtube_url: https://www.youtube.com/watch?v=504PvfXou5Y
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

**Michal Cichra**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=504PvfXou5Y) · [Conference site](https://www.ai.engineer/)

## Description

"One thing harder than reading AI code is reading AI tests." Mikuel from Safe Intelligence argues spec driven development leaves a loop open: you have a markdown spec, but how do you know the product actually behaves that way? His answer is Cucumber, nearly forgotten and suddenly useful again. Executable, human readable BDD scenarios connect directly to PRDs and critical user journeys and close the gap between what the spec says and what the tests verify.

The rest of the talk is enforcement. ADRs capture not just what the rules are but why; agents rejected at commit time get linked back to the document and iterate. Module import linting makes N+1 queries structurally impossible: rendering templates cannot touch the database, E2E tests cannot import any module that could. His sessions run 20 to 50 context compacts. The agent stays on track because the rules live in git hooks and CI, not in the prompt.

Speaker info:
- https://cz.linkedin.com/in/michal-cichra-61188a84
