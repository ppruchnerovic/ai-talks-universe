---
id: CvRngaQZQ3Y
title: "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain"
slug: improving-agents-is-a-data-mining-problem-vivek-trivedy
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Vivek Trivedy"]
channel: null
duration_min: 20
published_at: 2026-08-12T19:00:01Z
video_id: CvRngaQZQ3Y
youtube_url: https://www.youtube.com/watch?v=CvRngaQZQ3Y
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

**Vivek Trivedy**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=CvRngaQZQ3Y) · [Conference site](https://www.ai.engineer/)

## Description

Does your agent get dumber after the first compaction? After the second? You cannot read that off the code, only off the traces, and there are far too many to read yourself. So LangChain points agents at the traces of other agents and asks exactly that, alongside questions like where users got upset and what a different model would have done at the same step. Vivek Trivedy's argument is that observability and continual learning are the same problem in different clothing, because an agent acting in an environment produces the only real record of what happened, and that record is the substrate everything else is built on.

The economics fall out of reading it. Working with Harvey on a legal benchmark, they found an open model could match their frontier model's trace judging at one to two orders of magnitude lower cost, arrived at through harness engineering that the traces themselves pointed to. His rule for when to stop tuning prompts and start finetuning is speed of feedback: harness engineering answers in about two minutes, so you exhaust that ceiling first, finetune to break through it, then return to harness engineering. He also argues that dense feedback is what agents lack most, since a benchmark returning only pass or fail gives an agent nothing to act on, while traces already hold the fine grained signal. The claim worth arguing with is that you can describe an agent's behavior just by showing the evals it was measured against, because those are what it hill climbs.

Speaker info:
- https://x.com/Vtrivedy10
- https://www.linkedin.com/in/vivek-trivedy-433509134/
- https://www.vtrivedy.com/

Timestamps:
0:00 - My agent made mistakes, now what
1:28 - Ship it, collect traces, mine them
2:44 - Observability and continual learning are the same problem
4:00 - Why agents are harder to reason about than code
4:36 - Trading determinism for autonomy
5:15 - Sending agents to read other agents' traces
6:29 - Today's data is the least we will ever have
7:09 - When a trace no longer fits in context
7:48 - Not reaching for a frontier model every time
8:24 - Matching frontier trace judging with an open model
9:02 - Where harness engineering stops paying
9:40 - Finetuning on a narrow vertical
10:17 - Trading token costs for hardware costs
11:34 - Distillation from your own good traces
12:10 - Evals as a description of behavior
12:48 - What scikit learn has to do with any of this
13:28 - Model, harness, task fit
14:07 - Finding fit functions and finding data
15:24 - Why dense feedback matters
16:01 - Harness engineer, finetune, harness engineer again
17:22 - Updating agent state across three axes
18:39 - Sleep time compute and memory that is not append only
19:17 - Takeaways
