---
id: esY99nYXxR4
title: "How we solved Context Management in Agents — Sally-Ann Delucia"
slug: how-we-solved-context-management-in-agents-sally-ann-delucia
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 16
published_at: 2026-05-10T19:00:06Z
video_id: esY99nYXxR4
youtube_url: https://www.youtube.com/watch?v=esY99nYXxR4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How we solved Context Management in Agents — Sally-Ann Delucia

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=esY99nYXxR4) · [Conference site](https://www.ai.engineer/)

## Description

The naive solution is truncation. The obvious solution is summarization. Neither worked — and the Arize team found out the hard way while building an AI agent that had to analyze the very trace data it was generating.

A year of lessons from building Alyx, starting with the vicious loop that defined the problem: Alex runs on trace data, the spans grow, the context limit hits, it fails and tries again. The talk covers why truncation breaks reasoning, why summarization gives the LLM too much control, and how head/tail preservation with a retrievable memory store is what actually held. Then: long session evals, sub-agents as the answer when one context accumulates too much, and what they found when they went looking for secrets in the Claude Code source release.

Speaker info:
- https://www.linkedin.com/in/sallyann-delucia-59a381172/

Timestamps:
0:00 Introduction and speaker background
1:02 Overview of the AI agent, Alyx
1:29 The problem: Context engineering vs. prompt engineering
4:06 The vicious loop of data growth in AI agents
5:16 Why naive truncation failed
6:14 Why summarization proved unreliable
6:46 The solution: Smart truncation and memory stores
8:02 Handling long session challenges
9:23 Offloading tasks to sub-agents
11:19 Ongoing challenges and future work
12:57 Findings from the Claude Code source release
13:44 Final key takeaways on context management
14:58 Q&A session
