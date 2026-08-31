---
id: Ib5t2RLtxvM
title: "From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI"
slug: from-agent-traces-to-agent-simulations-rustem-feyzkhanov
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rustem Feyzkhanov"]
channel: null
duration_min: 20
published_at: 2026-07-25T00:00:00Z
video_id: Ib5t2RLtxvM
youtube_url: https://www.youtube.com/watch?v=Ib5t2RLtxvM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI

**Rustem Feyzkhanov**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Ib5t2RLtxvM) · [Conference site](https://www.ai.engineer/)

## Description

Take a real production trace, rebuild the database state, tools, and files the agent touched, and you have a task any model can replay under identical conditions. That reconstruction is the move at the center of this talk. Public benchmarks like WebArena hand you a single success rate on someone else's tasks, but what you actually care about is cost per solved task, latency, and whether the agent followed your policies. So you build a private benchmark from your own traces, wire in the same skills, tools, and evaluators the agent sees in production, and compare models apples to apples on the environment that matters to you.

The environments are multistep and long horizon, so a verifier reads the final state while an LLM judge checks whether the agent followed policy, and a run can stop early once it clearly goes off track. The hard parts are the edge cases: agents that reward hack the simulation, missing fixtures, tasks that turn out to be unsolvable. Rustem Feyzkhanov's case is that this belongs in a CI pipeline for agents, the same way tests gate code, connecting observability traces to experiments to a benchmark that keeps up as the agent changes. Every company ends up needing its own, as part of the agent ops loop.

Speaker info:
- https://x.com/ryfeus
- https://www.linkedin.com/in/ryfeus
- https://ryfeus.io

Slides:
- https://www.dropbox.com/scl/fi/lyp1my0oc9whpusps29t7/Agent-Simulations-Talk.pdf?rlkey=rhrrpgun5c35kwculce0wmt2x&e=1&dl=0

Timestamps:
0:00 - Introduction: why Snorkel builds agent benchmarks
1:17 - Benchmark construction and testing agents in production
3:08 - The limits of public benchmarks
4:01 - Why you need a private benchmark
4:52 - Environments, tools, and evaluators
6:34 - Anatomy of a simulation task
7:37 - Task formats: instruction files and Oracle data
9:20 - Multistep, long horizon simulations
10:54 - Verifiers, LLM as a judge, and reward hacking
13:02 - A CI pipeline for agents
15:19 - Connecting traces, experiments, and benchmarks
16:51 - Q&A
