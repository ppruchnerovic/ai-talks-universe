---
id: khVX_BUnEwU
title: "Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital"
slug: active-graph-agent-runtime-babyagi-4-yohei-nakajima
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Yohei Nakajima"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-07-22T00:00:00Z
video_id: khVX_BUnEwU
youtube_url: https://www.youtube.com/watch?v=khVX_BUnEwU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital

**Yohei Nakajima**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=khVX_BUnEwU) · [Conference site](https://www.ai.engineer/)

## Description

Yohei Nakajima was running a 500 question eval when his API key died at question 350. Normally that means restarting the whole long agent from scratch. Instead it rolled back one step and resumed at 353, because in ActiveGraph the log is the agent. Most people build agents around the LLM and bolt on memory and logging; Nakajima, the creator of BabyAGI, flips it and builds around an immutable event log. Every action and every change to the agent flattens into one typed log, which projects a graph that is the agent's state, so you get replays, rollbacks, and forks for free.

On top of the log sit behaviors that react to graph changes and emit events, policies that decide what the agent may change on its own versus what needs a human or a contradiction check, and swappable packs for memory, tools, and chat. The LLMs never talk to each other; they only touch shared state, an idea he borrows from 1970s blackboard systems and Kafka, and his hunch is that AI writes this style better than modern agent code because it has decades of training data on it. The payoff is self improvement: a loop that forks the agent, proposes a patch, gates it behind sandbox tests, and keeps it only if accuracy actually rises, and a lab that reads his blog posts, runs its own experiments, and once found a bug in its own code and opened the PR.

Speaker info:
- https://github.com/yoheinakajima/activegraph
- https://x.com/yoheinakajima
- https://www.linkedin.com/in/yoheinakajima

Timestamps:
0:00 - ActiveGraph and three years of BabyAGI
1:55 - Build around the log, not the LLM
3:24 - Behaviors, policies, and views
6:43 - Packs and the blackboard architecture lineage
8:12 - The log as memory, and the API key that resumed itself
9:53 - Reference agents built natively on the log
11:11 - Self improvement: regimes and controlled self modification
12:25 - ActiveGraph Lab writes its own experiments
13:02 - A Pokemon card competition as a testbed
14:33 - Surprises: why AI architects this better
15:49 - Why an agent needs an experiential world model
