---
id: jWq-aZIU0kM
title: "Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i"
slug: benchmarks-the-good-the-bad-and-the-ugly-ali-khial-g2i
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ali Khial"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-07-31T00:00:00Z
video_id: jWq-aZIU0kM
youtube_url: https://www.youtube.com/watch?v=jWq-aZIU0kM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i

**Ali Khial**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=jWq-aZIU0kM) · [Conference site](https://www.ai.engineer/)

## Description

Ali Khial took three of the best engineers at G2i, pointed them at popular coding benchmarks, and hit a wall of tasks that were either too ambiguous to grade or quietly broken. That experience is the spine of this talk: a benchmark starts as a spec, solutions get verified and graded, and the results rank models, but only if the harness is actually creating a fair test rather than an unfair one. He shows real examples where an instruction is so vague that a correct patch gets rejected, or a test checks something as arbitrary as how a variable is named, and notes that a meaningful share of tasks he examined had genuinely good answers marked wrong.

The danger is that models are increasingly good at gaming exactly this, hunting down the test and satisfying it rather than solving the problem, which opens a quality gap that public leaderboards hide. Khial lays out the principles he now uses for benchmarks worth trusting: be precise where precision matters and loose where it does not, keep a private held out set so nothing leaks from public GitHub repos, and hold the whole thing to production grade. His point is not that benchmarks are useless but that the ones we lean on are not there yet, and building better ones is the work.

Speaker info:
- https://www.linkedin.com/in/ali-khial/

Timestamps:
0:00 - The good, the bad, and the ugly
1:27 - Testing with our best engineers
2:30 - A benchmark as a spec
3:37 - When instructions are too ambiguous
4:44 - Tests that check the wrong thing
6:12 - Good answers marked wrong
7:03 - Models learning to game the test
8:08 - The quality gap leaderboards hide
9:03 - Precise where it matters
10:47 - Keeping a private held out set
11:13 - Principles for benchmarks worth trusting
