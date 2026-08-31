---
id: 5Sui_OnSRlY
title: "The Missing Primitive for Agent Swarms — Lou Bichard, Ona"
slug: the-missing-primitive-for-agent-swarms-lou-bichard-ona
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Lou Bichard"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-05-23T16:00:06Z
video_id: 5Sui_OnSRlY
youtube_url: https://www.youtube.com/watch?v=5Sui_OnSRlY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Missing Primitive for Agent Swarms — Lou Bichard, Ona

**Lou Bichard**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=5Sui_OnSRlY) · [Conference site](https://www.ai.engineer/)

## Description

Stripe called theirs Minions. RAMP called theirs Inspect. Both are internal infrastructure for running fleets of background agents, and both teams built it from scratch. Lou Bichard's argument is that this shouldn't keep happening.

The talk breaks down what agent swarm infrastructure actually needs: a runtime (largely solved), orchestration and triggers (solved), and coordination, which is not. Coordination is the gap where agents pick up tasks from each other, pass messages, and verify they have cleared a stage of the development cycle before moving on. GitHub is a poor substitute: noisy, designed for humans, and not built for agents raising hundreds of parallel pull requests. Lou covers what a proper primitive looks like, shows how Owner ships VM level isolation for agent fleets today, and makes the case that the coordination layer probably needs to be a CLI gateway that any local coding agent can invoke to check its progress and proceed.

Speaker info:
- https://x.com/loujaybee
- https://www.linkedin.com/in/loujaybee

Timestamps:
0:00 Introduction and definition of a Software Factory
1:50 Agent swarm patterns: Swarms, Fleets, and Events
3:11 Real-world examples of internal agent infrastructure (Stripe, RAMP)
3:50 How Owner handles agent infrastructure and development environments
4:49 Understanding Harness Engineering
5:43 The three pillars of agent swarm infrastructure: Runtime, Orchestration, and Coordination
7:17 Demo: Running sub-agents and fleets in Owner
10:20 Challenges of building a software factory
11:44 The issue with Context Management and Context Rot
12:16 Why GitHub is a poor coordination layer for agents
12:59 Proposed solutions: State machines, Durable execution, and CLI gateways
