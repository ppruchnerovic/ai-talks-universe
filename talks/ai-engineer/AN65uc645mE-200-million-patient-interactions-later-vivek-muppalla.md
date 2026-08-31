---
id: AN65uc645mE
title: "200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI"
slug: 200-million-patient-interactions-later-vivek-muppalla
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Vivek Muppalla"]
channel: null
duration_min: 21
published_at: 2026-08-19T00:00:00Z
video_id: AN65uc645mE
youtube_url: https://www.youtube.com/watch?v=AN65uc645mE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# 200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI

**Vivek Muppalla**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=AN65uc645mE) · [Conference site](https://www.ai.engineer/)

## Description

Asked how many in the room had ever received a proactive call from their healthcare provider, almost no hands went up. Vivek Muppalla treats that as the signature of scarcity: too few clinicians and too few hours, so the system triages and only the sickest get called. Hippocratic AI is past 200 million clinical conversations across more than 60 health systems, which is what changes the arithmetic. The tradeoff they refused is the familiar one: models accurate enough for this work can take tens of seconds to answer, and models fast enough for a phone call are not safe enough to make one.

So the stack was built end to end. Polaris runs 31 models on every conversation, one holding the thread and 30 specialists covering labs, medications and scheduling, executed in parallel with each specialist first making a fast check on whether it has anything to say at all. A single model would be a single point of failure. Their speech recognition is a decoder only audio system fed the conversation so far and the domain context alongside the audio, so a drug name resolves against a finite list rather than an unbounded one, and prosody survives the projection so it hears the how as well as the what. Single word answers get a second scoring pass, because a heard as no is catastrophic. On evaluation he does the arithmetic that makes 99% unacceptable: at 10,000 calls a day that is 100 people sent to the wrong appointment, and catching a 1% failure rate takes roughly 450 tests.

Speaker info:
- https://x.com/vim1up
- https://www.linkedin.com/in/vivekmuppalla/
- https://hippocraticai.com/

Timestamps:
0:00 - Who has ever been called by their provider
1:05 - Triage as a math problem, and what flips it
1:54 - The oath every employee takes
2:44 - A call with a patient, start to escalation
5:12 - Why a generic voice stack does not work
6:04 - Building vertically to get speed and intelligence
7:44 - Latency and intelligence as a compounding flywheel
8:36 - Polaris, and running 31 models at once
9:29 - What speech recognition gets wrong in the real world
10:27 - Feeding context and domain knowledge into the audio model
11:19 - A finite list of medications instead of an infinite one
12:10 - Rescoring single word answers
13:51 - How a specialist decides to speak up
14:43 - Verifiers for tool calls
15:34 - Quantization, speculative decoding, cache
16:25 - Why 99% is a bad number here
17:14 - The tests needed to catch a 1% failure
18:03 - Grading on the scale used for humans
18:55 - Building a benchmark for empathy
