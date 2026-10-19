---
id: IuOIVUiE6f8
title: "Honpeng Guo, ByteDance: verl: A Flexible and Efficient RL Framework for LLM Reasoning & Tool-calling"
slug: honpeng-guo-bytedance-verl-a-flexible-and-efficient-rl
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 25
published_at: 2026-09-29T21:10:59Z
video_id: IuOIVUiE6f8
url: https://www.youtube.com/watch?v=IuOIVUiE6f8
youtube_url: https://www.youtube.com/watch?v=IuOIVUiE6f8
tags: []
topics: ["Agents & orchestration", "Enterprise adoption & strategy", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Honpeng Guo, ByteDance: verl: A Flexible and Efficient RL Framework for LLM Reasoning & Tool-calling

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=IuOIVUiE6f8) · [Conference site](https://aiconference.com/)

## Description

Hongpeng Guo, Research Scientist, ByteDance

verl: A Flexible and Efficient RL Framework for LLM Reasoning and Tool-calling

Large language models (LLMs) have enabled advances in language understanding and multimodal tasks, yet scaling reinforcement learning (RL) with these models remains challenging: most existing frameworks either lack the abstractions needed to define and manage complex dataflows or cannot handle models with billions of parameters.
verl (https://github.com/volcengine/verl) is an open-source framework for building end-to-end RL pipelines with LLMs. It provides high-level abstractions and optimizations for dataflow orchestration and resource management via a Ray-based hybrid-controller model. It offers high-level abstractions for dataflow orchestration and resource management: the entire RL dataflow runs as a single controller process on the Ray driver, issuing primitive API calls to WorkerGroup modules. The WorkerGroup and ResourcePool components distribute computation and resources across GPU clusters, delivering high throughput and strong extensibility.
Since its release, verl has seen adoption in both academic research and industry production. It integrates with major training backends (FSDP, FSDP2, Megatron-LM) and inference engines (vLLM, SGLang), and supports various RL algorithms (PPO, GRPO, DAPO, etc) with effortless scaling. Recent trends in reasoning models bring new challenges to RL infrastructure, such as efficient tool calling, multi-turn interactions, and capability to scale up to giant MoE models like DeepSeek 671B. To lower the barrier to RL for advanced reasoning and tool calling, we recently improved verl with (1) efficient request level async multi-turn rollout and tool calling, (2) integration with expert parallelism for large scale MoE models, and (3) async system architecture for off-policy / async RL algorithms and flexible device placement.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved
