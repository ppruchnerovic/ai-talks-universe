---
id: vy7o1g2iHY8
title: "How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS"
slug: how-i-deleted-95-of-my-agent-skills-and-got-better-results
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Nick Nisi"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-05-30T18:00:06Z
video_id: vy7o1g2iHY8
youtube_url: https://www.youtube.com/watch?v=vy7o1g2iHY8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS

**Nick Nisi**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vy7o1g2iHY8) · [Conference site](https://www.ai.engineer/)

## Description

WorkOS will be back for the World's Fair next week! see https://ai.engineer/wf and use YOUTUBEPROMO for new tickets only. Join 6000 AI engineers at the "Superbowl of AI"!

---

Claude would fake running tests by touching the expected output file. Nick Nisi, DX engineer at WorkOS, fixed it by SHA-256 hashing the actual test output and verifying it cryptographically. His principle: make it easier to do the real work than to lie about it, and enforce that through code and state machines, not prompts.

The same discipline reversed an opposite problem. He generated 10,000 lines of skills from WorkOS documentation, measured with evals, and found one skill was dropping a task from 97% correct to 77% correct. He deleted 95% of it, rewrote 553 lines of handwritten gotchas, and eval time dropped from 68 minutes to 6. The model already knew how to code. It just needed to know where the landmines were.

Speaker info:
- https://x.com/nicknisi
- https://linkedin.com/in/nicknisi
- https://github.com/nicknisi

Timestamps
0:00 Introduction
1:22 The challenge of context switching with agents
2:33 Introducing Case: A harness for agentic workflows
3:33 Rebuilding with a TypeScript state machine
4:45 The critical importance of evidence-based verification
5:59 Applying agentic principles to the WorkOS CLI
7:44 Lessons in documentation: Generating skills from docs
8:52 Why more data (10,000 lines) led to worse performance
9:36 The impact of using evals to measure accuracy
10:40 Key takeaway: Enforce with code, not just prompts
12:41 Treating failures as bugs in the harness system
14:39 Advice for building agentic-ready products
16:01 Final summary: Replacing trust with evidence
