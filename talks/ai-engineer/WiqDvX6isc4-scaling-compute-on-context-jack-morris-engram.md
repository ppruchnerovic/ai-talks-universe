---
id: WiqDvX6isc4
title: "Scaling Compute on Context — Jack Morris, Engram"
slug: scaling-compute-on-context-jack-morris-engram
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jack Morris"]
channel: null
duration_min: 20
published_at: 2026-08-12T15:30:14Z
video_id: WiqDvX6isc4
youtube_url: https://www.youtube.com/watch?v=WiqDvX6isc4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Scaling Compute on Context — Jack Morris, Engram

**Jack Morris**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=WiqDvX6isc4) · [Conference site](https://www.ai.engineer/)

## Description

Train a model directly on ten thousand financial reports and you can drive the loss to 0.00001. It knows the documents perfectly. Then you generate from it and it collapses. Jack Morris uses that failure to set up the real problem. The three axes that powered the entire deep learning revolution, more data, more compute, bigger models, all run on public data. Models are superb on Wikipedia, arXiv, and GitHub, and know nothing about your emails, your meetings, or your company. Against your own corpus the data axis is fixed and training from scratch is off the table, which leaves compute as the only axis you can still push, and that is what he means by scaling compute on context.

The rest is a tour of what people try and exactly where each one stops. KV compaction only reaches what already fits in context and skips the gradients entirely. On policy distillation works, but raises the question of what you distill, since raw documents will not do, which is the gap self study in the cartridges paper is aimed at. Continued pretraining on synthetic data conditioned on your corpus is promising, but it overwrites some of the pretraining and assumes you have a base model rather than the post trained one most people actually start from. Every approach shares a ceiling: you define a dataset, you train, and unless the model is underparameterized it eventually absorbs everything you made. A synthetic data wall, with none of pretraining's scaling behavior. The property he wants is the one that made AlphaGo work, where getting better makes the training questions harder, so that adding compute keeps buying depth instead of flattening out.

Speaker info:
- https://x.com/jxmnop
- https://jxmo.io
- https://substack.com/@jxmnop

Timestamps:
0:00 - Scaling compute on context, and Engram
1:28 - Terence Tao on breadth against depth
2:43 - What models cannot know after training
3:22 - Long tail skills and AMD kernels
3:59 - Why a model knows nothing about you
4:37 - The many names for this problem
5:14 - Three axes of scaling
5:52 - Even post training data is public by definition
6:30 - Applying scale to your data
7:45 - Why compute is the only axis left
8:21 - The data budget is less fixed than it looks
9:40 - Stating the problem properly
10:55 - Just train on it, and why that fails
11:34 - Perfect loss, collapsed generation
12:13 - Making the model think the data is in context
12:52 - KV compaction
13:31 - On policy distillation and what to distill
14:46 - Simulating pretraining with synthetic data
16:00 - Unsupervised RL environments
16:38 - The synthetic data wall
17:54 - Self improvement, and what AlphaGo had
18:33 - The curve they are chasing
