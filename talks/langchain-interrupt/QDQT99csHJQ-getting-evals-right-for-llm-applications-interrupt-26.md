---
id: QDQT99csHJQ
title: "Getting Evals Right for LLM Applications | Interrupt 26"
slug: getting-evals-right-for-llm-applications-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 18
published_at: 2026-06-12T12:47:16Z
video_id: QDQT99csHJQ
youtube_url: https://www.youtube.com/watch?v=QDQT99csHJQ
tags: ["LangChain", "LangSmith", "AI evals", "LLM evaluation", "data science", "AI engineering", "Shreya Shankar", "Hamel Husain", "Parlance Labs", "agent evals", "LLM judges", "eval design", "Interrupt conference", "AI observability", "synthetic data", "metric design"]
transcript: false
---

# Getting Evals Right for LLM Applications | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `18 min`

`#LangChain` `#LangSmith` `#AI evals` `#LLM evaluation` `#data science` `#AI engineering` `#Shreya Shankar` `#Hamel Husain` `#Parlance Labs` `#agent evals` `#LLM judges` `#eval design` `#Interrupt conference` `#AI observability` `#synthetic data` `#metric design`

[Watch the recording](https://www.youtube.com/watch?v=QDQT99csHJQ) · [Conference site](https://interrupt.langchain.com/)

## Description

Shreya Shankar and Hamel Husain have taught evals to over 4,500 people across dozens of companies, and they keep seeing the same mistakes. This talk walks through five of the most common pitfalls and how thinking like a data scientist fixes them.

At Interrupt, the agent conference by LangChain, they covered:
• Why generic metrics like "helpfulness" and "hallucination" are too ambiguous to use off the shelf
• How to treat LLM judges as imperfect classifiers with train/dev/test splits
• Why synthetic data generation goes wrong and how to fix it
• Who should actually be labeling your data
• What criteria drift is and why it happens
• Why fully automating evals misses the product failures that matter most

The Return of the Data Scientist | Interrupt 26
0:00 Introduction
0:38 What is the harness? Logs, metrics, and traces
1:17 The harness is data science
1:27 How we got here: ML engineering 4 years ago
2:05 AI engineering today: vibes-based evaluation
2:37 What this talk covers: evals and common mistakes
3:28 Mistake 1: using generic or off-the-shelf metrics
4:47 How to fix it: explore data, build custom interfaces
6:04 Mistake 2: blindly trusting LLM judges
7:03 Treating LLM judges like ML classifiers
8:09 LLM judges as imbalanced classification problems
8:26 Mistake 3: bad experimental design
9:04 How to fix it: systematic synthetic data generation
10:13 Bad metric design: 1-to-100 scales
10:33 How to fix it: binary classification problems
11:23 Mistake 4: wrong people labeling data
12:00 Criteria drift
13:03 Mistake 5: automating too much
13:45 Other pitfalls: ROUGE/BLEU, unhelpful judge prompts, raw JSON, uncalibrated scores
15:34 The data science corollary: EDA, metric design, model validation
16:47 Summary: always look at your data
17:00 Where to get the slides

Extra resources:
• Evals skills: https://github.com/hamelsmu/evals-skills
• Everything mentioned during the session: https://maven.com/parlance-labs/o/0cb2fa
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interr...
• Meet LangSmith Engine: https://www.langchain.com/blog/introd...
• About LangChain: https://www.langchain.com/
