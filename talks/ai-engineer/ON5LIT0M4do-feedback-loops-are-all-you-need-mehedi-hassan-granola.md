---
id: ON5LIT0M4do
title: "Feedback Loops are All You Need — Mehedi Hassan, Granola"
slug: feedback-loops-are-all-you-need-mehedi-hassan-granola
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Mehedi Hassan"]
channel: "AI Engineer"
duration_min: 10
published_at: 2026-05-10T00:00:00Z
video_id: ON5LIT0M4do
youtube_url: https://www.youtube.com/watch?v=ON5LIT0M4do
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Feedback Loops are All You Need — Mehedi Hassan, Granola

**Mehedi Hassan**

`AI Engineer` · `AI Engineer` · `2026` · `10 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ON5LIT0M4do) · [Conference site](https://www.ai.engineer/)

## Description

One-shotting is seductive. One line of code for web search. One prompt to serve every user. One deploy and you're done. Granola shipped a chat feature into their meeting notes app and found out what comes after that.

This talk is a product engineer's honest account of why the gap between "it works in the playground" and "it works in production" is so hard to close. Web search looks like a single tool call — until it blows up your context, bills you 10p per chat, and your provider ships an overnight update that silently degrades your results. Prompt personalization looks straightforward — until you realize that one prompt genuinely cannot serve the salesperson expecting a deal summary, the engineer expecting blockers and linear tickets, and the HR manager expecting something else entirely.

The response at Granola wasn't to prompt better. It was to build the machinery for iteration: custom internal tracing that exposes tool calls, search trails, reasoning traces, and cost in a UI built for everyone — not just engineers with CloudWatch access. And a move to run their Electron frontend as a web app, so every PR gets a preview link and Cursor can go test changes automatically. The point isn't any single technique. It's the feedback loop — and what happens to an AI feature when it actually has one.

Speaker info:
- https://x.com/mehedih_
- https://github.com/MehediH

timestamps:
0:15 Introduction to Granola and product engineering
1:08 Demonstration of meeting transcription and note-taking features
1:52 The challenges of shipping generic AI features
2:48 The difficulties of integrating web search tools
4:02 Why a single prompt cannot serve diverse user roles
4:40 Building custom internal tracing and observability tools
6:22 Enhancing developer experience for desktop applications
7:16 Refactoring Electron for web-based testing and CI/CD preview links
8:33 Automating feature verification with Cursor
8:46 Concluding thoughts on building iterative feedback loops for AI products
