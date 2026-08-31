---
id: KMR_RBoCa4M
title: "SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)"
slug: simulationmaxxing-how-we-ship-agents-20-faster-aman-gupta
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Aman Gupta"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-07-29T19:00:06Z
video_id: KMR_RBoCa4M
youtube_url: https://www.youtube.com/watch?v=KMR_RBoCa4M
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)

**Aman Gupta**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=KMR_RBoCa4M) · [Conference site](https://www.ai.engineer/)

## Description

Nubank serves 135 million customers, so an AI agent that mishandles a support conversation fails at scale. The talk opens with the result: five agents in production, higher customer satisfaction, and roughly 20 times faster shipping. Shreya Rajpal, CEO of Snowglobe, argues the thing that unlocked that pace was evals, and specifically simulated data standing in for real conversations. Good agent evals are hard because the data is multi turn and stateful, not single turn question and answer, and hand curating it and waiting on production to confirm can take forever.

Snowglobe points at the agent and generates grounded simulations, a customer like Maria trying to order a credit card, complete with account context, tone, and intent, so you can ship, observe, simulate, and feed the results back in a tight loop. Human review found the simulated conversations comparable to real ones about 80% of the time, enough to bring up new agents, derisk changes, and protect the self service rate. With aligned metrics and cheap simulation, the team now tests open models and variant agents freely, because the eval bottleneck is gone.

Speaker info:
- https://x.com/aman2304
- https://x.com/ShreyaR
- https://www.linkedin.com/in/shreya-rajpal/
- http://shreya-rajpal.com

Timestamps:
0:00 - Opening with the results
0:39 - Nubank at 135 million customers
2:34 - Why evals matter most
2:47 - Why simulated data works
3:49 - What makes agent eval data hard
4:49 - How teams get eval data today
6:44 - Simulations in minutes, not weeks
7:35 - Pointing Snowglobe at your agent
8:48 - A grounded simulation: Maria orders a card
10:31 - Ship, observe, simulate, repeat
11:34 - How close simulations are to real
13:43 - Testing models and variants
