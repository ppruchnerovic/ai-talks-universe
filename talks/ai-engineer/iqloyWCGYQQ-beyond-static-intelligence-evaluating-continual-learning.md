---
id: iqloyWCGYQQ
title: "Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley"
slug: beyond-static-intelligence-evaluating-continual-learning
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Parth Asawa"]
channel: null
duration_min: 20
published_at: 2026-08-12T00:00:00Z
video_id: iqloyWCGYQQ
youtube_url: https://www.youtube.com/watch?v=iqloyWCGYQQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley

**Parth Asawa**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=iqloyWCGYQQ) · [Conference site](https://www.ai.engineer/)

## Description

Every leaderboard you have seen was built by asking a model to do one task, wiping its memory, and asking it another. Parth Asawa's objection is that this quietly assumes learning across instances does not count. His benchmark measures what that assumption hides, using a metric called gain: run a system with state, then run the identical system reset between every single instance, and take the difference. Cumulative reward cannot show you this, because a stronger base model can post a higher total while learning less than a weaker one that genuinely improves.

Building tasks that can measure learning turns out to be the hard part, and he sets three requirements. Headroom, so the task is not already solved by pretraining. Shared latent structure across instances, since standard benchmarks are deliberately independent and therefore offer nothing to improve on, which is why chaining existing benchmarks together does not work. And a learning signal in the environment, whether reward, error messages, or plain text. Continual Learning Bench 1.0 spans six domains including database exploration, where a system should need fewer SQL queries by the tenth question, after which a schema migration tests whether it can throw away stale knowledge without throwing away the useful kind. The headline result is uncomfortable: plain in context learning tops the leaderboard, beating the more elaborate context management systems on reward, on gain, and on cost. Failure modes land on either side of stability and plasticity, including a forecasting model that overpredicts, is corrected, underpredicts, is corrected again, and then jumps straight back to its original overprediction instead of splitting the difference.

Speaker info:
- https://x.com/pgasawa
- https://www.linkedin.com/in/pgasawa/
- https://pgasawa.github.io/

Timestamps:
0:00 - How we evaluate models today
1:28 - Imagine forgetting everything after every task
2:05 - What continual learning actually means
2:42 - In context, external memory, or parametric
3:18 - The case that we are not measuring it at all
3:58 - What the existing literature does
4:37 - Why those evaluations are not enough
5:13 - Why you cannot chain existing benchmarks
5:51 - Design criterion one: headroom
7:06 - Shared structure and a learning mechanism
7:42 - Reward, and why cumulative reward misleads
8:58 - Gain: the same system with memory wiped
10:15 - Isolating learning from base capability
10:54 - The database exploration task
12:06 - Adding concept drift with a migration
13:20 - Six domains in the benchmark
13:57 - Results, and the in context learning surprise
15:12 - Failure modes on stability and plasticity
15:51 - A forecast that forgets its own correction
16:28 - A notepad that refuses to update
17:07 - Why the training stack was never built for this
17:47 - The sunk cost fallacy in continual learning
19:02 - Rethinking third party AI research
19:38 - Roadmap
