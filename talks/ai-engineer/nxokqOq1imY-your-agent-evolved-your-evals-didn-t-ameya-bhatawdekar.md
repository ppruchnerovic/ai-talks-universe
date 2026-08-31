---
id: nxokqOq1imY
title: "Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust"
slug: your-agent-evolved-your-evals-didn-t-ameya-bhatawdekar
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ameya Bhatawdekar"]
channel: null
duration_min: 24
published_at: 2026-08-20T13:00:06Z
video_id: nxokqOq1imY
youtube_url: https://www.youtube.com/watch?v=nxokqOq1imY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust

**Ameya Bhatawdekar**

`AI Engineer` · `AI Engineer` · `2026` · `24 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=nxokqOq1imY) · [Conference site](https://www.ai.engineer/)

## Description

Teams built orchestration graphs because the models of 2024 could not be trusted to orchestrate, and then the models learned to orchestrate and the graphs became the thing holding them back. Ameya Bhatawdekar traces that loop across five generations of architecture, each one forced by a step change in model capability, and argues that evals have to move with it. A single prompt needed only answer quality. A retrieval chain added a parser that grabs the wrong field and a retriever that returns the wrong context. Graphs added branch logic, contracts between nodes, and classifier nodes that misfire quietly, which is a great deal of new surface to check.

What changed most recently is not another layer but the unit of measurement. Once a loop is reliable enough to run free, the same input produces visibly different trajectories on every run, so a single eval result stops meaning very much. He separates the two questions it hides. Pass at k asks whether the system succeeds at least once across k attempts, which measures capability. The stricter variant asks how many of those k attempts succeed, which measures reliability. A system can look strong on the first and weak on the second, and you only learn that by running the distribution rather than the sample. Underneath it all is the claim that evals are the durable asset across replatformings, and that the ones which go stale are the ones nobody feeds from production.

Speaker info:
- https://www.linkedin.com/in/ameyab

Timestamps:
0:00 - Replatforming, not iterating
2:24 - Step function model changes, not incremental ones
3:30 - Why you cannot just drop in a new model
5:34 - Grounding it in a site reliability agent
6:40 - One prompt, one call, one answer to grade
7:44 - The chain, and where retrieval goes wrong
8:48 - The first ReAct loop, and why it fell short
9:49 - Taking control back with workflow graphs
11:58 - The eval surface a graph creates
13:07 - Models get good enough to loop again
15:19 - Pass at k for capability, the stricter one for reliability
16:21 - Memory, sandboxes, and skills around the loop
19:34 - The flywheel most teams accept but never run
