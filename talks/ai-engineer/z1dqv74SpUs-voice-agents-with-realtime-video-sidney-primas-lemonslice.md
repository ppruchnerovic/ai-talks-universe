---
id: z1dqv74SpUs
title: "Voice agents with Realtime Video — Sidney Primas, LemonSlice"
slug: voice-agents-with-realtime-video-sidney-primas-lemonslice
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sidney Primas"]
channel: "AI Engineer"
duration_min: 27
published_at: 2026-08-18T16:00:06Z
video_id: z1dqv74SpUs
youtube_url: https://www.youtube.com/watch?v=z1dqv74SpUs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Voice agents with Realtime Video — Sidney Primas, LemonSlice

**Sidney Primas**

`AI Engineer` · `AI Engineer` · `2026` · `27 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=z1dqv74SpUs) · [Conference site](https://www.ai.engineer/)

## Description

An avatar of Teddy Roosevelt holds court in a replica Oval Office, generating video continuously for eight hours with no reset, and a second deployment is being built to run for sixteen. That duration is the hard part. Sidney Primas explains that a real time avatar can only look backward, because the future frames do not exist yet, so every block it generates inherits the errors of the blocks before it and compounds them. LemonSlice trains with an attention mask that enforces this during training rather than discovering it at inference, and collapses roughly 30 denoising steps down to a single step to hit real time.

The less obvious bottleneck is audio. Emotion and facial expression turn out to depend on the audio embedding, and most audio encoders are trained on audiobooks, which are monotone by construction, so an expressive model needs its own. The wider bet is to take a world model and point it at humans, paying a harder training and deployment cost up front in exchange for full body movement, object interaction, and physics arriving closer to free. Two things surprised him. Serving this costs about what serving a voice model costs, despite the difference in pixels. And the model harness, meaning the orchestration of threads and queues across GPU and CPU so that video never stutters through an interrupt, is where he now thinks much of the durable value will sit.

Speaker info:
- https://www.linkedin.com/in/sidneyprimas/

Timestamps:
0:00 - Breaking the avatar Turing test
2:26 - Teddy Roosevelt in a replica Oval Office
4:40 - Why the visual layer matters
5:46 - Pointing a world model at humans
6:58 - One image in, any style out, and being the API layer
9:12 - Audio is what makes it expressive
10:15 - Making a video model interactive, then real time
12:22 - Error accumulation over hours of generation
14:34 - Cost parity with a voice model
15:36 - The model harness nobody talks about
16:38 - An emotion engine for the next model
19:55 - A single end to end EQ layer
22:09 - Questions: internal state, and a real Turing test
