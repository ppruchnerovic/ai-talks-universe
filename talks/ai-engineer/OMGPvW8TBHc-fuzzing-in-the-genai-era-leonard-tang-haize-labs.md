---
id: OMGPvW8TBHc
title: "Fuzzing in the GenAI Era — Leonard Tang, Haize Labs"
slug: fuzzing-in-the-genai-era-leonard-tang-haize-labs
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Leonard Tang"]
channel: "AI Engineer"
duration_min: 19
published_at: 2025-08-22T00:00:00Z
video_id: OMGPvW8TBHc
youtube_url: https://www.youtube.com/watch?v=OMGPvW8TBHc
tags: []
transcript: false
---

# Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

**Leonard Tang**

`AI Engineer` · `AI Engineer` · `2025` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=OMGPvW8TBHc) · [Conference site](https://www.ai.engineer/)

## Description

"Evaluation" is one of those concepts that every AI practitioner vaguely knows is important, but few practitioners truly understand. Is "eval" the dataset for measuring the quality of your AI system? Is "eval" the measure, the metric of quality? Is "eval" the process of human annotation and scoring? Or is "eval" a third-party dataset run once to benchmark a model?

To mitigate this cacophony, this talk will provide an opinionated and principled perspective for what we actually mean when we say “evaluation”, beyond the traditional for-loop-over-a-static dataset.

In particular, this perspective draws heavy inspiration from *fuzzing*, i.e. bombarding AI with simulated, unexpected user inputs to uncover corner cases at scale. This factors into sub-problems regarding:

- Quality Metric. What is the actual criteria we, as humans, are using to determine if an AI system is producing good or bad responses? How do we elicit these criteria before the human SME can articulate them? How do we, as efficiently as possible, operationalize this criteria with an automated *Judge*?

- Stimuli Generation. Given a metric, how do we know, with confidence, that an AI system is performing well with respect to the metric? What data is representative and sufficient for discovering all potential bugs of an AI system? And how do we generate this complex, diverse, faithful data at scale?

We will discuss in detail the philosophy, technology, and case studies behind both problems of Quality Metric and Stimuli Generation, and how they interact in concert.

Timestamps
00:00 Introduction to Haizing
01:16 The "Last Mile Problem" in AI
02:47 The Brittleness of GenAI Applications
03:54 Examples of Brittle Chatbots
04:29 Inadequacy of Standard Evaluation Methods
06:09 Haizing: Simulating the Last Mile
08:43 Scaling Evaluation with Agents as Judges
09:29 Verdict: Accuracy vs. Latency
11:47 Scaling Evaluation with RL-Tuned Judges
14:06 Fuzzing vs. Adversarial Testing in AI
14:37 Simulation as Prompt Optimization
16:23 Case Study: Haizing a Major European Bank's AI App
17:05 Case Study: Haizing a F500 Bank's Voice Agents
17:46 Case Study: Scaling Voice Agent Evals with Verdict

Leonard Tang
Founder & CEO

I am the co-founder and CEO of Haize Labs, where we are solving the ultimate extant problem in AI: ensuring its reliability, quality, and alignment for any application. You might also know of us for our red-teaming work.

Prior, I studied math and computer science at Harvard. My research then covered adversarial robustness, math reasoning, computational neuroscience, interpretability, and large(-ish) language models. Much of that has now been distilled into the Haize technology agenda. I also dropped out of, before starting, a Stanford PhD in computer science.

In the limit of my life, I am chiefly invested in starting Bell Labs 2.0.
