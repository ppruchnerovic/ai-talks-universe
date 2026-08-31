---
id: zL1kLftVTlo
title: "Scaling up Continual Learning — Ronak Malde, Trajectory"
slug: scaling-up-continual-learning-ronak-malde-trajectory
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ronak Malde"]
channel: null
duration_min: 23
published_at: 2026-08-12T14:30:11Z
video_id: zL1kLftVTlo
youtube_url: https://www.youtube.com/watch?v=zL1kLftVTlo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Scaling up Continual Learning — Ronak Malde, Trajectory

**Ronak Malde**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zL1kLftVTlo) · [Conference site](https://www.ai.engineer/)

## Description

Scale on policy self distillation to trajectories with a hundred tool calls and the model collapses into hedging. The tokens it learns to favor fill up with wait, but, and maybe, until, as Ronak Malde puts it, everything just turns into maybe. He calls it the but wait problem, and it happens because the student drifts far enough on a long task that the teacher course corrects at every opportunity, leaving the model parked between two divergent distributions.

The algorithm underneath is a good trick. At the frontier there is no smarter model to distill from, so you make the model its own teacher: put privileged information, a hint, in the teacher's prompt, and match the log probs of the student that never saw it. Malde scores post training methods against four properties, an online task distribution, on policy sampling, no parallel rollouts, and a per token reward, and shows SFT, RLHF, and GRPO each buying some at the cost of others. GRPO gets on policy sampling but explodes parallelism and collapses feedback into one sequence level score, which he compares to being handed 87 out of 100 on an essay and told to work out why. Self distillation gets all four, and it optimizes across the entire vocabulary at every token instead of sharpening the one that was sampled, which is why it keeps climbing past where GRPO plateaus while tokens to solve go down rather than up. The failure modes are the useful part: step level KL weighting to handle divergence, and residual guidance for hint leakage, the self distillation analogue of reward hacking, where a hint containing the answer teaches the model to state it and back fill the reasoning afterward.

Speaker info:
- https://x.com/rronak_
- https://www.linkedin.com/in/ronak-malde

Timestamps:
0:00 - From Windsurf to Trajectory
1:05 - Benchmarks are saturating and getting expensive
1:58 - The signal we throw away every day
2:51 - Four things a training algorithm should have
3:42 - SFT, and what it got right
4:31 - DPO and RLHF
5:22 - GRPO and the Faustian bargain
6:15 - How GRPO actually works
7:04 - Scored 87 out of 100 and told to figure it out
7:52 - Distillation, then on policy distillation
8:43 - Self distillation: make the model its own teacher
10:21 - Optimizing the whole vocabulary, not the top token
11:11 - Results on short horizon tasks
12:52 - What breaks at 120B and a hundred tool calls
13:41 - The but wait problem
14:31 - Step level divergence weighting
16:11 - Hint leakage, the new reward hacking
17:51 - Residual guidance
19:35 - All four properties, finally
20:25 - What Trajectory is building
21:16 - Q&A: how continual is continual learning
22:08 - Q&A: model and harness improving together
