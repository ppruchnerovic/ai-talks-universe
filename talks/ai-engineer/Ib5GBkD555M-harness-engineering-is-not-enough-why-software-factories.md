---
id: Ib5GBkD555M
title: "Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer"
slug: harness-engineering-is-not-enough-why-software-factories
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dex Horthy"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-07-23T16:30:06Z
video_id: Ib5GBkD555M
youtube_url: https://www.youtube.com/watch?v=Ib5GBkD555M
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer

**Dex Horthy**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Ib5GBkD555M) · [Conference site](https://www.ai.engineer/)

## Description

In July 2025 Dex Horthy turned the lights off: an agent software factory where nobody read the code. It fell apart. An issue appeared that no amount of prompting could fix, the site was down, users were furious, and he was digging through a codebase he had stopped reading three months earlier. His claim is that this is not a skill or scale issue, and no harness or extra tokens fixes it, because it is a model training problem. Coding models are reinforced on one thing, did the test pass without breaking another, and nothing in that reward penalizes bad architecture, whose cost shows up months later. So they get better at passing tests and no better at keeping a codebase maintainable.

That is why Claude Code went from nothing to billions while tools with the same read, write, and edit commands did not: it was the first model trained against the harness it ships in. But maintainability is far harder to verify than a green test, and as Horthy puts it, if a model knew what good code looked like it would already write it. So for now you are stuck reading the code, which is fine, because you can still move fast. His fix is to turn the lights back on and plan up front: product review, system architecture, the underrated step of program design down to types and call graphs, then vertical slices. Thirty minutes of alignment saves hours of review, and a good PR becomes a joy to read instead of slop to untangle.

Speaker info:
- https://x.com/dexhorthy
- https://linkedin.com/in/dexterihorthy
- https://github.com/humanlayer/12-factor-agents

Timestamps:
0:00 - The narrative: you are the bottleneck, just ship more
1:28 - The cracks: outages and falling PR review quality
2:20 - The thesis: the harness is not enough
3:36 - A brief history of the software factory
5:52 - The agentic factory and turning the lights off
7:30 - Why it fails: the July 2025 lights-off experiment
8:56 - Models cannot maintain codebase quality
10:12 - Why Claude Code won and how coding models are trained
13:18 - Verifying maintainability and better benchmarks
14:58 - Turning the lights back on: plan up front
17:16 - Too many bad PRs, and closing advice
