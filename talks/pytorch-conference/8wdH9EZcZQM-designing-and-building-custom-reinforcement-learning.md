---
id: 8wdH9EZcZQM
title: "Designing and Building Custom Reinforcement Learning Environments for Fine-tuning LLMs - N. Bantilan"
slug: designing-and-building-custom-reinforcement-learning
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["N. Bantilan"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:43:36Z
video_id: 8wdH9EZcZQM
url: https://www.youtube.com/watch?v=8wdH9EZcZQM
youtube_url: https://www.youtube.com/watch?v=8wdH9EZcZQM
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Designing and Building Custom Reinforcement Learning Environments for Fine-tuning LLMs - N. Bantilan

**N. Bantilan**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=8wdH9EZcZQM) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Designing and Building Custom Reinforcement Learning Environments for Fine-tuning LLMs - Niels Bantilan, Union.ai

Techniques like GRPO, combined with reinforcement learning with verifiable rewards (RLVR), have shown success in fine-tuning LLMs for reasoning tasks with a strong inherent reward, such as math and coding. However, can these techniques be more generally applied to other real-world tasks without a clear reward signal? This session will dive into the design considerations and practical challenges associated with building RL environments for fine-tuning reasoning models for such cases.

Using a “Wikipedia Maze” environment as a case study, I’ll demonstrate how to cast reasoning tasks into multi-turn episodic RL environments that have deterministic terminal conditions and clear rewards. I’ll generalize this particular case study into a graph traversal problem that can apply to many tasks, including multi-step agentic tasks. Finally, I’ll present some optimizations that can reduce bottlenecks during the training process, such as using inference frameworks like vLLM to generate trajectories efficiently and exploring off-policy reinforcement learning techniques to generate trajectories from a higher capacity model in order to update the weights of a lower capacity model.
