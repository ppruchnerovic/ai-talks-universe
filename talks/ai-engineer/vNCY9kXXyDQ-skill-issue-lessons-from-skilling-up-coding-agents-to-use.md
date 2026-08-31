---
id: vNCY9kXXyDQ
title: "Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse"
slug: skill-issue-lessons-from-skilling-up-coding-agents-to-use
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Marc Klingen"]
channel: "AI Engineer"
duration_min: 24
published_at: 2026-05-20T15:00:06Z
video_id: vNCY9kXXyDQ
youtube_url: https://www.youtube.com/watch?v=vNCY9kXXyDQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse

**Marc Klingen**

`AI Engineer` · `AI Engineer` · `2026` · `24 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vNCY9kXXyDQ) · [Conference site](https://www.ai.engineer/)

## Description

Without a skill, Claude Code adds Langfuse using stale pre-training context, ships broken instrumentation, then catches the failure and fetches current docs to fix it. The resulting trace captures two LLM calls with no visibility into what the agent actually did.

Marc Klingen covers the six learnings from building a skill to close that gap: surfacing a natural language search endpoint so agents stop crawling 478 documentation pages, why pointing to references beats duplicating content, and what happened when they ran an auto-research loop on the skill itself. Three of six suggested improvements shipped, but their target function nearly backfired by optimizing out the documentation-fetching steps that make the skill reliable over time.

Speaker info:
- https://x.com/marcklingen
- https://www.linkedin.com/in/marcklingen/

Timestamps:
00:00 - Introduction to Marc Klingen and Langfuse
01:22 - Conceptual mental model for agent skills
04:04 - The problem: scaling documentation and onboarding for coding agents
09:03 - Six key learnings from building a Langfuse skill
09:12 - Learning 1: Looking at traces for debugging
10:47 - Learning 2: Helping agents navigate information (sitemaps/formats)
11:40 - Learning 3: Surfacing a search endpoint for docs
12:36 - Learning 4: Implementing basic evaluation (eval) setups
13:53 - Learning 5: Referencing rather than duplicating content
14:24 - Learning 6: Using auto-research loops with target functions
17:24 - Discussion on challenges: distribution, versioning, and target functions
19:21 - Roadmap and future outlook for agent automation
20:09 - Q&A session
