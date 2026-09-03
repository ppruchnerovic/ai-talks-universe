---
id: m6MF1OR_9kM
title: "Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai"
slug: z-ai-glm-4-6-what-we-learned-from-100-million-open-source
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2025
speakers: ["Yuxuan Zhang"]
channel: null
duration_min: 20
published_at: 2025-11-22T15:00:06Z
video_id: m6MF1OR_9kM
url: https://www.youtube.com/watch?v=m6MF1OR_9kM
youtube_url: https://www.youtube.com/watch?v=m6MF1OR_9kM
tags: []
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Multimodal, vision, speech & robotics", "Training, fine-tuning & model building"]
transcript: false
---

# Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai

**Yuxuan Zhang**

`AI Engineer` · `AI Engineer` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=m6MF1OR_9kM) · [Conference site](https://www.ai.engineer/)

## Description

GLM 4.6 is the only open-source model currently tied for #1 on the LMSYS Chatbot Arena, standing shoulder-to-shoulder with GPT-4o and Claude 3.5 Sonnet. In this talk, Zhang Yuxuan from zAI breaks down the technical roadmap that led to over 100 million downloads across the GLM family.

Zhang deep dives into the specific training recipes behind GLM 4.6, including their move to single-stage Reinforcement Learning (RL), the "SLIME" RL framework for handling complex agent trajectories, and how they structured 15 trillion tokens of pre-training data. If you are building AI Agents or training LLMs, this breakdown offers a rare look inside the architecture of a frontier-class open-source model.

In this video, we cover:

The Data Recipe: How zAI filters 15T tokens, moves to repo-level code contexts, and integrates agentic reasoning data.

SLIME Framework: A look at the hybrid synchronous/asynchronous architecture used to train agents without bottlenecking GPU clusters.

RL Lessons: Why zAI abandoned multi-stage RL in favor of single-stage training to preserve long-context capabilities.

GLM 4.5V: How native resolution processing improves UI navigation and video understanding.

Timestamps:
0:00 - Introduction & The GLM Ecosystem
0:55 - 100 Million Downloads & Open Source Roadmap
03:22 - Tying GPT-4o on LMSYS Arena
05:04 - The Training Pipeline: From Pre-training to Long Context
07:54 - Introducing SLIME: Efficient RL for Agents
11:08 - The "Two-Stage" Curriculum Strategy
11:57 - Why Single-Stage RL beats Multi-Stage RL
12:55 - Token-Weighted Loss for Coding
14:13 - GLM 4.5V: Multimodal & Video Understanding
16:07 - Deployment: vLLM, SGLang, and Hugging Face
18:06 - Coding Assistants & Future Plans

Zhang Yuxuan has recently started a PhD at the University of Liverpool and is currently working at Z.ai. zR (Zhang) is passionate about open-source initiatives and strives for deeper exploration in this realm. Their primary activities include the following: Engaged in research on models such as GLM-4.5 (https://arxiv.org/abs/2508.06471), GLM-4.5V (https://arxiv.org/abs/2507.01006), CogVideoX (https://arxiv.org/abs/2408.06072), CogAgent (https://arxiv.org/abs/2312.08914); researching the capabilities of model Agents and the integration with Agent frameworks such as langchain-chatchat (https://github.com/chatchat-space/Langchain-Chatchat), chatpdf (https://github.com/CosmosShadow/gptpdf); participated in several national competitions, such as RoboMaster and National Students' SmartCar Competition, and achieved some results, including national awards. These competitions have been truly fascinating. Enjoys hackathon competitions and welcomes teaming up for these events.

---
Socials:
- LinkedIn: https://www.linkedin.com/in/yuxuan-zhang-86a124282/
- X (Twitter): https://x.com/zRdianjiao
- GitHub: https://github.com/zRzRzRzRzRzRzR
- Website: https://huggingface.co/ZHANGYUXUAN-zR
- Company: Z.ai (https://z.ai)
