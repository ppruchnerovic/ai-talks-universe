---
id: maRzp4kImJ4
title: "Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal"
slug: taking-reinforcement-learning-cross-datacenter-nan-jiang
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Nan Jiang"]
channel: null
duration_min: 20
published_at: 2026-08-10T17:30:30Z
video_id: maRzp4kImJ4
youtube_url: https://www.youtube.com/watch?v=maRzp4kImJ4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal

**Nan Jiang**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=maRzp4kImJ4) · [Conference site](https://www.ai.engineer/)

## Description

A frontier scale checkpoint is around 500 GB, so shipping one to a rollout fleet in another region takes minutes to hours and kills any hope of weight updates landing in seconds. Nan Jiang's claim is that you can send roughly 500 MB instead and have the rollout engine reconstruct a bitwise identical weights version. Fewer than 1% of rollout visible weights actually change between consecutive versions, and the reason is not that gradients are sparse. Gradients are dense, about 99% of parameters get a nonzero gradient and the FP32 master update is dense too. It is just small.

The mechanism is a small Adam step meeting finite precision. The rollout engine serves a BF16 view whose rounding boundary sits near theta over 256, about 0.0039 for a weight around 1, while a typical Adam step at RL post training learning rates runs around 3 millionths, more than a thousand times too small to cross it. The master weights move and the served value does not, which he calls Adam absorption. Lower precision serving makes it sharper still: an internal run serving GLM 4.7 Air in FP8 saw 0.15% of weights change on the first step and settle near 0.05%. Once a lossless patch is the unit of synchronization instead of a checkpoint, the rollout fleet stops needing to live in the trainer's cluster. Training keeps its all reduce and its fast fabric, rollout islands scatter across whatever regions and providers have GPUs right now, a sidecar makes any engine version aware, and scattered inference capacity becomes one elastic rollout fleet. Modal's implementation is called Stitch.

Speaker info:
- https://x.com/nanjiangwill
- https://www.linkedin.com/in/nanjiangwill/
- https://www.nanjiangwill.com/
- https://github.com/nanjiangwill

Timestamps:
0:00 - Where the GPUs actually are
1:29 - The standard RL post training loop
2:06 - The cathedral and the bazaar
2:43 - RL wants four things at once
3:22 - What can leave the cluster and what cannot
3:59 - The rollout serving island as the movable unit
5:16 - Why a full checkpoint is the wrong unit of sync
6:33 - The bet: under 1% of served weights change
7:10 - Ingredient one, the precision floor
8:30 - Ingredient two, the size of an Adam step
9:48 - Adam absorption, visualized
11:06 - Shipping a lossless patch, not a delta
12:21 - What the measurements show
12:58 - Why this is not gradient sparsity
13:35 - FP8, NVFP4, and group scaled formats
14:54 - An internal run on GLM 4.7 Air
15:33 - The bulletin board architecture
16:48 - The sidecar that makes engines version aware
17:26 - 500 GB down to 500 MB
18:02 - Stitch
18:43 - Open questions: Muon, fully async RL, and beyond
