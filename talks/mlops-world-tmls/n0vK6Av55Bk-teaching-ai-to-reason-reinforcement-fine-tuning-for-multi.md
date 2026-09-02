---
id: n0vK6Av55Bk
title: "Teaching AI to Reason: Reinforcement Fine-Tuning for Multi-Turn Agentic Workflows"
slug: teaching-ai-to-reason-reinforcement-fine-tuning-for-multi
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2025
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 30
published_at: 2025-04-25T15:39:15Z
video_id: n0vK6Av55Bk
url: https://www.youtube.com/watch?v=n0vK6Av55Bk
youtube_url: https://www.youtube.com/watch?v=n0vK6Av55Bk
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Teaching AI to Reason: Reinforcement Fine-Tuning for Multi-Turn Agentic Workflows

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2025` · `30 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=n0vK6Av55Bk) · [Conference site](https://mlopsworld.com/)

## Description

Sameer Reddy, Research Engineer, Predibase

About the Speaker:
Sameer Reddy is a Research Engineer at Predibase, where he works on fine-tuning and serving efficient language models for real-world agentic applications. His background spans reinforcement learning, LLM infrastructure, and ML efficiency, with prior research at Cisco and Georgia Tech focused on scalable model training and inference systems.

Abstract:
Multi-turn agent workflows—where models must reason across multiple steps, gather context iteratively, and make decisions over time—pose a unique challenge for LLMs fine-tuned only on static, one-shot data. In this talk, I’ll demonstrate how reinforcement fine-tuning (RFT) unlocks more reliable, controllable performance in complex agentic tasks by letting developers define reward functions that shape model behavior across multiple turns.

In this talk, we’ll share how reinforcement fine-tuning (RFT) can be used to train small, specialized models (1B–3B parameters) that act as lightweight decision engines within larger agentic workflows. We’ll demonstrate how to fine-tune a model to select tools accurately using just a reward function—no hand-labeling required—and how this architecture can reduce both latency and cost while improving precision.

While the live demo will focus on a single-turn decision task, we’ll explore how this approach can generalize to multi-turn agent behavior, such as:

- Deferring tool selection to a compact RFT model before invoking a larger orchestrator LLM
- Teaching models to reason (via chain-of-thought) before making decision
- Building modular, low-latency components that plug into existing agent stacks

This talk is ideal for ML engineers and infra teams building production-grade agents who want to reduce costs, increase reliability, and take greater control over how their models reason and act.
