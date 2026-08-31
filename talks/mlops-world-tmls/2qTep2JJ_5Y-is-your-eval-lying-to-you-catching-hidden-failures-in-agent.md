---
id: 2qTep2JJ_5Y
title: "Is Your Eval Lying to You? Catching Hidden Failures in Agent Evaluation"
slug: is-your-eval-lying-to-you-catching-hidden-failures-in-agent
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 28
published_at: 2026-08-11T13:09:30Z
video_id: 2qTep2JJ_5Y
youtube_url: https://www.youtube.com/watch?v=2qTep2JJ_5Y
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Is Your Eval Lying to You? Catching Hidden Failures in Agent Evaluation

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `28 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=2qTep2JJ_5Y) · [Conference site](https://mlopsworld.com/)

## Description

Abhimanyu Anand, Sr. Data Scientist, Elastic

About the Speaker:
Abhimanyu is a Senior Data Scientist at Elastic, where he works on the development and evaluation of enterprise-grade AI agents. He holds an M.Sc. in Big Data Analytics from Trent University, specializing in natural language processing.

Throughout his career, he has designed and deployed robust AI solutions across a range of industries, including social media, e-commerce, and metals and mining.

Abstract:
Your agent eval says accuracy improved. But did latency spike? Does your LLM-based metric even agree with human judgment? And is that 5% gain real or noise? Do we ship it or not?
If you're evaluating AI agents, you've likely encountered hidden failures such as:

1. Improving accuracy with a tool change also increases tool calls and latency, and a single positive metric masks overall degradation.
2. LLM-based evaluators are nondeterministic, so a score increase may only reflect sensitivity to a prompt change, not an improved user experience.
3. Without robust testing, you might be shipping coin-flip gains that will disappear on the next run.

In this session, I'll walk through how we addressed these at Elastic. Using a real experiment as an example, I'll cover the evaluation setup we built to catch these failures. This includes multi-metric evaluation to expose tradeoffs (accuracy, tool usage, and latency) and a claim-level correctness evaluator (we developed in house) validated against human judgment to ensure LLM-based scores are meaningful. I'll also discuss key significance testing principles we used to filter out noise and verify real gains.
Along the way, I'll show the prompt structure behind our evaluator and examples of practical results.
