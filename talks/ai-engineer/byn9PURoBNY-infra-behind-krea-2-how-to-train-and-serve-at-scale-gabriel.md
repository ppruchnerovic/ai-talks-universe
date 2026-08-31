---
id: byn9PURoBNY
title: "Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai"
slug: infra-behind-krea-2-how-to-train-and-serve-at-scale-gabriel
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Gabriel Jorge Menezes"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-08-18T17:00:05Z
video_id: byn9PURoBNY
youtube_url: https://www.youtube.com/watch?v=byn9PURoBNY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai

**Gabriel Jorge Menezes**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=byn9PURoBNY) · [Conference site](https://www.ai.engineer/)

## Description

GPU utilization is a lie. It read 100% straight through pretraining while the cluster was nowhere near well used, so Gabriel Jorge Menezes tracks tensor core utilization instead, and watched it climb as training resolution stepped from 128 pixels up to 1024. That is one of several numbers he argues you cannot train at this scale without. InfiniBand counters are exported by nothing off the shelf, and most of their failures turned out to be cross node communication, so they built that collection themselves. Any GPU running hotter than 78 degrees gets pulled rather than debugged, because one warm card throttles and destabilizes the entire run.

This is the infrastructure half of Krea 2, the model trained from scratch on thousands of GPUs. Crashes scaled with the cluster and often failed silently, with communication timing out while every dashboard stayed green, and the practical answer was to stop treating each one as a mystery. Let it crash, and the same nodes running the same code will frequently go 24 hours on the next attempt. What made that survivable was checkpointing aggressively against a filesystem quick enough to write a terabyte in under 30 seconds. Production and training then share one cluster, with training holding priority and inference evicted to outside providers through a fake Kubernetes node, migrated back gradually rather than all at once so the site never drops.

Speaker info:
- https://www.linkedin.com/in/gabriel-jorge-menezes/
- https://gab-menezes.github.io/

Timestamps:
0:00 - Krea 2, trained from scratch, and two open checkpoints
3:26 - Crashes at scale, and the silent ones
4:18 - Metrics are everything, starting with temperature
5:58 - GPU utilization is a lie, use tensor cores
6:48 - InfiniBand and NVLink metrics you have to build yourself
8:29 - Checkpointing hard against a fast filesystem
9:21 - Gang scheduling, and training outranking production
11:01 - Flipping inference out through a fake node
14:23 - Taints that stop you wasting GPUs
16:03 - Inference runs on almost any GPU
