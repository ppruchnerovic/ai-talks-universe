---
id: mJqwmmOx4WA
title: "How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe"
slug: how-to-avoid-disaster-when-vibe-coding-a-billing-engine
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Andrew Garvin"]
channel: null
duration_min: 18
published_at: 2026-08-28T16:00:06Z
video_id: mJqwmmOx4WA
youtube_url: https://www.youtube.com/watch?v=mJqwmmOx4WA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe

**Andrew Garvin**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=mJqwmmOx4WA) · [Conference site](https://www.ai.engineer/)

## Description

Andrew Garvin types one sentence asking for a billing engine that copies Lovable's pricing, and gets back a working sandbox: a customer, metered usage flowing in, and a draft invoice broken into separately scoped credit pools for builds, plan mode, cloud and gateway calls. Reproducing that by hand means understanding auto recharge, credit expiry and overage, which is exactly where people hurt themselves. He cofounded Metronome, the usage billing platform Stripe acquired this year in its largest deal, so he has watched a lot of companies get this wrong.

What makes the talk useful is that a billing vendor stands on stage and argues against full autonomy. Billing carries deep business logic and real money, so his recommendation is to let an agent accelerate you into a test environment and stop there, rather than ship to production unattended. The guardrails are unglamorous: portable skills files that carry the API's hard won context, and deliberately verbose error messages written so an agent can correct itself. He also separates three things people blur together, an agent as your product, as your buyer, and as your user. The third is the disruptive one, and he points at a large software company cutting seat prices and moving to credits, because seats stop meaning much once one agent does the work of many logins.

Speaker info:
- https://www.linkedin.com/in/agarvin/

Timestamps:
0:00 - Metronome, Stripe, and what they are demoing
2:29 - Where billing goes sideways with agents
3:40 - Provisioning an environment from the CLI
6:02 - Skills files that carry the hard parts
7:13 - Why a human stays in the loop
9:30 - Agent as product, buyer and user
10:38 - Moving off seats and onto credits
13:01 - Opening what the agent actually built
14:12 - Scoped credit pools and a draft invoice
16:27 - What this suggests beyond billing
