---
id: U4w8X8ycoY8
title: "Verl: A Flexible and Efficient RL Framework for LLMs - Hongpeng Guo & Ziheng Jiang, ByteDance Seed"
slug: verl-a-flexible-and-efficient-rl-framework-for-llms
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Hongpeng Guo", "Ziheng Jiang"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:43:40Z
video_id: U4w8X8ycoY8
url: https://www.youtube.com/watch?v=U4w8X8ycoY8
youtube_url: https://www.youtube.com/watch?v=U4w8X8ycoY8
tags: []
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Verl: A Flexible and Efficient RL Framework for LLMs - Hongpeng Guo & Ziheng Jiang, ByteDance Seed

**Hongpeng Guo, Ziheng Jiang**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=U4w8X8ycoY8) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Verl: A Flexible and Efficient RL Framework for LLMs - Hongpeng Guo & Ziheng Jiang, ByteDance Seed

Large language models (LLMs) have unlocked capabilities in language understanding and multimodal tasks. Integrating reinforcement learning (RL) at scale remains a major challenge. Existing frameworks lack either the abstractions for complex dataflow or the scalability for billion-parameter models.

verl (https://github.com/volcengine/verl) is an open-source framework for building end-to-end RL pipelines with LLMs. It provides high-level abstractions and optimizations for dataflow orchestration and resource management via a hybrid-controller model. WorkerGroup modules and ResourcePool components distribute computation and resources across GPU clusters, delivering high throughput and strong extensibility.

Since its release, verl has been adopted in both academic research and industry production. It integrates with major training backends (FSDP, FSDP2, Megatron-LM) and inference engines (vLLM, SGLang), supports RL algorithms (PPO, GRPO, DAPO, etc) and agentic features (multi-turn dialogue, tool calling). Recent DeepSeek-671B post-training integration further demonstrates verl's scalability to ultra-large models, making it a robust foundation for RL-enhanced LLM systems.
