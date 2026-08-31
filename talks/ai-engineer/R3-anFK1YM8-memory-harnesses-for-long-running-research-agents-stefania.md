---
id: R3-anFK1YM8
title: "Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai"
slug: memory-harnesses-for-long-running-research-agents-stefania
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Stefania Druga"]
channel: null
duration_min: 13
published_at: 2026-08-12T15:00:06Z
video_id: R3-anFK1YM8
youtube_url: https://www.youtube.com/watch?v=R3-anFK1YM8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai

**Stefania Druga**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=R3-anFK1YM8) · [Conference site](https://www.ai.engineer/)

## Description

On a literature review task where every paper already fit inside the context window, adding a memory harness changed nothing: the same accuracy, at higher cost. That negative result is the most useful thing in Stefania Druga's experiment, because it marks the boundary. Move to a long horizon task where the answer sits at step 124 and the question arrives at step 500, far outside the window, and the harness becomes the entire game.

Her framing is that memory is a write, manage, read control loop wrapped around the model, not a database you attach to it. She held the model fixed and varied only the recall policy across a ladder: no recall at all, vector RAG, a decisions ledger that tracks and prioritizes what was decided each turn, and an oracle handed the correct memory outright. Across 68 xbench questions the ranked ledger won, beating even the approach of gating the harness on whether memory seemed necessary. The oracle pointedly does not reach the ceiling, because giving a model the right memory does not make it use the right memory. Ranked recall was also cheaper, which is the line worth keeping: bad memory is expensive, since it burns tokens and sends the agent the wrong way. The whole thing runs on a local M3 Ultra in Tokyo that she is driving from her phone, with fans stacked around it because the evals have not stopped.

Speaker info:
- https://x.com/Stefania_druga
- https://www.linkedin.com/in/drugastefania/
- https://stefania11.github.io/

Timestamps:
0:00 - Context rot on long horizon tasks
1:04 - Longer tasks, fewer model releases
1:56 - Cutting spend by moving work local
2:24 - Local models crossing the usefulness line
2:50 - The machine in Tokyo, and the fans
3:44 - Memory as a write, manage, read loop
4:11 - The harness: core, recall, archival
4:36 - The recall ladder, from nothing to an oracle
5:27 - Task one: a retracted claim in a literature review
6:19 - When everything fits, memory only adds cost
6:47 - Task two: an answer 376 steps out of reach
8:08 - Results across 68 questions
8:35 - Why the oracle does not reach the ceiling
8:59 - Ablations, and generalizing across models
9:49 - Bad memory is expensive
10:16 - Treat recall policy as a first class metric
11:07 - The wider memory landscape
11:33 - What running locally bought her
12:29 - Sovereign AI at Sakana
