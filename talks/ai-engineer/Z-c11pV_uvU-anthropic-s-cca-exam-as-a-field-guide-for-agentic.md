---
id: Z-c11pV_uvU
title: "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley"
slug: anthropic-s-cca-exam-as-a-field-guide-for-agentic
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Frank Coyle"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-08-08T00:00:00Z
video_id: Z-c11pV_uvU
youtube_url: https://www.youtube.com/watch?v=Z-c11pV_uvU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley

**Frank Coyle**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Z-c11pV_uvU) · [Conference site](https://www.ai.engineer/)

## Description

The Claude Certified Architect exam hands you six production scenarios and picks four at random, and Frank Coyle walks through them backwards, leading with the anti pattern in each one. Knowing what not to do is what points you toward what to do, the same way the design patterns movement of the early 1990s came with a catalog of the moves that quietly ruin you. Scenario one is a customer support loop, and the anti pattern is calling the model, taking the response, and using it. What you want instead is to branch on the stop reason, because the model cannot execute a tool at all. It only hands back the parameters your own code runs, and the stop reason is also how you learn you ran out of tokens and the answer in your hands is partial.

The rest is context discipline. Loading one agent with every tool is the carpenter who turns up with plumbing and electrical gear too, so specialized subagents with one or two tools each win, and every agent should see only its own slice. Coyle gives a critic agent the claim and the evidence but withholds the reasoning that produced them, because agents that watch each other think converge on a single idea the way a group talks itself into pizza. Subtask output gets forked into its own context so only the summary returns to the main thread, with a token count check that triggers compaction past a threshold. He closes on a cheap win most people skip: batch mode runs the same work for half the token cost if you can wait a day for it.

Speaker info:
- https://x.com/coyle_frankp
- https://www.linkedin.com/in/frank-coyle/
- https://www.frank-coyle.ai/
