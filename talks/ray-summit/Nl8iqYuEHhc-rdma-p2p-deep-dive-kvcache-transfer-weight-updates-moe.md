---
id: Nl8iqYuEHhc
title: "RDMA P2P Deep Dive: KvCache Transfer, Weight Updates & MoE Routing at Perplexity | Ray Summit 2025"
slug: rdma-p2p-deep-dive-kvcache-transfer-weight-updates-moe
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2025-11-18T17:32:47Z
video_id: Nl8iqYuEHhc
url: https://www.youtube.com/watch?v=Nl8iqYuEHhc
youtube_url: https://www.youtube.com/watch?v=Nl8iqYuEHhc
tags: []
topics: ["Enterprise adoption & strategy", "Training, fine-tuning & model building"]
transcript: false
---

# RDMA P2P Deep Dive: KvCache Transfer, Weight Updates & MoE Routing at Perplexity | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=Nl8iqYuEHhc) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Lequn Chen from Perplexity shares a fresh perspective on communication patterns for Large Language Models (LLMs) as they scale and as Mixture-of-Experts (MoE) architectures become more widely adopted.

He explains how today’s LLM systems rely heavily on collective communication via torch.distributed, NCCL, and other SPMD-based APIs—an approach that introduces unnecessary constraints on peer-to-peer data movement. As models grow and workloads diversify, especially across training and inference boundaries, inter-node communication becomes a critical bottleneck.

This talk revisits RDMA-based peer-to-peer communication for modern LLM workloads—an established but underutilized technique in contemporary large-scale model systems. Lequn walks through essential RDMA primitives and presents the design of Perplexity’s new communication library API, illustrated through three high-impact use cases:

KvCache transfer for disaggregated inference

Weight transfer between training and inference nodes during RL rollouts

MoE dispatch–combine all-to-all kernels

Attendees will gain a deeper understanding of alternative communication strategies that can unlock new efficiencies in next-generation LLM and MoE systems.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
