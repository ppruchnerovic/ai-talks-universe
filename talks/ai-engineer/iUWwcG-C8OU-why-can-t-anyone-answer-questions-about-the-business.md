---
id: iUWwcG-C8OU
title: "Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS"
slug: why-can-t-anyone-answer-questions-about-the-business
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Garrett Galow"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-06-11T18:00:06Z
video_id: iUWwcG-C8OU
youtube_url: https://www.youtube.com/watch?v=iUWwcG-C8OU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

**Garrett Galow**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=iUWwcG-C8OU) · [Conference site](https://www.ai.engineer/)

## Description

Every business question that needs SQL follows the same loop: explain the question, wait for an engineer, get an answer, realize it needs one more join, share a one-off in Slack, repeat. Garrett Galow from WorkOS built Studio to break that loop — an internal workspace where anyone can ask questions against Snowflake, Linear, and Notion in natural language and get answers or reusable widgets without filing a request.

The widgets are the interesting part: the LLM writes them once as declarative JavaScript that calls the underlying data sources directly, so every subsequent run is deterministic and cheap. Three things made it reliable enough to hand to a support team. Preflight sequencing that injects schema context only at the moment a tool is invoked, not upfront, keeping the context window clean. A layering rule that explicitly tells the model to distrust its own knowledge about WorkOS and go to primary sources. And query validation that runs every generated Snowflake query before hardcoding it into a widget, catching the valid SQL that returns zero rows failure mode.

Speaker info:
- https://www.linkedin.com/in/garrett-galow/
