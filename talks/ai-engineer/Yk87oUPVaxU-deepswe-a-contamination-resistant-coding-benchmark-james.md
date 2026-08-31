---
id: Yk87oUPVaxU
title: "DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve"
slug: deepswe-a-contamination-resistant-coding-benchmark-james
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["James Shi"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-07-26T00:00:00Z
video_id: Yk87oUPVaxU
youtube_url: https://www.youtube.com/watch?v=Yk87oUPVaxU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve

**James Shi**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Yk87oUPVaxU) · [Conference site](https://www.ai.engineer/)

## Description

DeepSWE is 113 software engineering tasks written from scratch, not scraped from pull requests, so a model cannot have seen them in training. Each one is a long horizon problem drawn from a real open source repository, authored by engineers who actually maintain that code, with isolated environments and program based verifiers that check observable behavior rather than trusting the model's own account. James Shi's point is that once you remove the contamination the leaderboard stops clustering: strong models pull far ahead and others, Gemini 3.1 Pro among them, fall toward the bottom.

The more revealing signal is in how models fail. Some quietly expand a task beyond what was asked, a failure mode DeepSWE scores in its own right, and Claude models did this a good fraction of the time while GPT models did it less often. Stronger models also tend not to verify their own work, and there is a real gap between the ones that test what they wrote and the ones that assume it is correct. Since reward hacking is a constant temptation, the verifiers are built to be gamed as little as possible, keeping the score anchored to the objective rather than to a convincing looking rollout.

Speaker info:
- https://x.com/shiqyy
- https://www.linkedin.com/in/jamesshi117/
- https://deepswe.datacurve.ai

Timestamps:
0:00 - Introduction: the DeepSWE benchmark
1:03 - 113 original, contamination-resistant tasks
2:08 - What makes a good benchmark
3:51 - The leaderboard and model spread
5:18 - Failure mode: over-scoping the task
7:16 - Do models verify their own work?
8:45 - Tasks authored by core contributors
10:15 - Writing realistic, high level prompts
11:45 - Program based verifiers and observable behavior
13:43 - Limitations and future work
15:25 - Reward hacking and keeping it cheating proof
