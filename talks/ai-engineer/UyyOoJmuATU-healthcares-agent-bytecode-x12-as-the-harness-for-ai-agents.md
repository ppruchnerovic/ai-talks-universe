---
id: UyyOoJmuATU
title: "Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay"
slug: healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Vasant Kearney"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-08-19T16:30:32Z
video_id: UyyOoJmuATU
youtube_url: https://www.youtube.com/watch?v=UyyOoJmuATU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay

**Vasant Kearney**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=UyyOoJmuATU) · [Conference site](https://www.ai.engineer/)

## Description

Call the payer, open their web portal, and read their X12 feed, and all three can tell you the patient is covered. You treat the patient anyway, and the claim comes back denied because they were not covered at the time. Vasant Kearney's point is that none of those surfaces is ground truth. A payer's phone system, portal and X12 layer are often built by different teams, sometimes by different contractors entirely, so they can contradict each other and they can just as easily agree on the wrong answer together.

His response is to treat X12 as a harness rather than a file format. Models do their best work confined, the way a strict language confines, and X12 already encodes the contract between a provider and a payer. Every stage of the claim lifecycle has an X12 correspondence, from an eligibility check as a 270 through the 999 that acknowledges syntax to the 835 that records payment, so an agent placing a phone call or driving a portal is emitting the same transaction by another route. Everything normalizes into an internal representation held as correct only until downstream evidence says otherwise. Two constraints travel with it. Memory has to live in a database rather than on local disk the way coding agents do it, for logical separation. And a stronger model cannot simply be dropped in, because better on a benchmark is not the same as better inside a system built around the model it replaces. He describes the posture as being AI pilled and AI skeptical at once.

Speaker info:
- https://x.com/vasantkearney
- https://www.linkedin.com/in/vasant-kearney-7b7a48b3
- https://onlay.ai/

Timestamps:
0:00 - Reading the room
1:06 - The goal is cost and patient experience
1:58 - How we arrived at an execution layer
3:06 - Solving handwritten digits does not cash the check
4:42 - What gets lost when you flatten a multimodal record
6:16 - What the agentic execution layer actually touches
7:23 - Why enterprise memory cannot live on local disk
7:49 - A better model is not automatically better for you
8:31 - Harness, and why X12 belongs in it
9:44 - Fifty steps, error propagation, and the cost of pure reasoning
11:16 - Memory that helps without steering the user
12:36 - The claim lifecycle, transaction by transaction
13:29 - A phone call is an X12 transaction underneath
14:47 - The schema is public, so agents can look it up
15:30 - X12 is a system of rules, not ground truth
16:47 - Normalizing to an internal representation
19:02 - Be AI pilled and AI skeptical
