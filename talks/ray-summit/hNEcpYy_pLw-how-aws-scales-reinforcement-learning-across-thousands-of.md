---
id: hNEcpYy_pLw
title: "How AWS Scales Reinforcement Learning Across Thousands of GPUs | Ray Summit 2025"
slug: how-aws-scales-reinforcement-learning-across-thousands-of
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 32
published_at: 2025-11-20T21:27:08Z
video_id: hNEcpYy_pLw
url: https://www.youtube.com/watch?v=hNEcpYy_pLw
youtube_url: https://www.youtube.com/watch?v=hNEcpYy_pLw
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# How AWS Scales Reinforcement Learning Across Thousands of GPUs | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=hNEcpYy_pLw) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Kunal Jha and Anoop Saha from AWS share how to build a fault-tolerant, scalable RL factory for large-scale LLM alignment by combining the elasticity of Ray with the resiliency of Amazon SageMaker HyperPod.

They begin by outlining the new reality of reinforcement learning: as RL expands beyond gaming and robotics into LLM alignment, agentic workloads, and real-world control with trillion-parameter base models, success depends not just on raw speed but on robustness, scalability, and elasticity. Many RL pipelines fail at cluster scale—not because GPUs are insufficient, but because GPU failures, preemptions, and tail latencies degrade goodput, the true measure of useful learning per GPU-hour.

Ray’s unified programming model enables RL pipelines to scale seamlessly from a single machine to massive distributed clusters, and is already powering popular frameworks like Verl, which rely on Ray to spin up workers, orchestrate rollouts, and move data efficiently across nodes.

The speakers then introduce Amazon SageMaker HyperPod, a persistent, highly resilient GPU cluster designed for distributed AI at extreme scale. By pairing Ray’s efficiency with HyperPod’s robustness, teams can build scalable post-training pipelines capable of running reliably across hundreds or thousands of GPUs.

Kunal and Anoop dive into the architectural details of:

Running Ray Jobs on HyperPod at massive scale

Leveraging vLLM for high-throughput inference workers

Coordinating PPO, GRPO, and DAPO pipelines using Verl + Ray

Recovering gracefully from GPU failures and preemptions to maximize goodput

Designing an RL factory architecture suitable for trillion-parameter model alignment

They also share reference implementations for post-training large open-weight models, along with practical strategies for optimizing performance, cost, and reliability.

Attendees will learn how Ray and Amazon SageMaker HyperPod together enable a new class of fault-tolerant, massively scalable RL systems for next-generation LLM alignment.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
