---
id: LU43Q_JktMs
title: "Secure & Scalable AI on Ray + Kubernetes: Google’s Decoupled Agent Pattern | Ray Summit 2025"
slug: secure-scalable-ai-on-ray-kubernetes-googles-decoupled
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2025-11-20T21:37:01Z
video_id: LU43Q_JktMs
url: https://www.youtube.com/watch?v=LU43Q_JktMs
youtube_url: https://www.youtube.com/watch?v=LU43Q_JktMs
tags: []
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# Secure & Scalable AI on Ray + Kubernetes: Google’s Decoupled Agent Pattern | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=LU43Q_JktMs) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Alex Bulankou and Brandon Royal from Google share how to bring agentic AI systems out of the lab and into production through the Decoupled Agent Pattern—a scalable, resilient, and secure architecture built on Ray and Kubernetes.

They begin by outlining the core production challenge of agentic systems: integrating LLMs, tools, and long-lived stateful agents while ensuring security, elasticity, and high-throughput execution. Traditional architectures struggle to balance these constraints. The Decoupled Agent Pattern solves this by cleanly separating the stateful agent logic from the stateless, scalable tools it invokes.

At the heart of this pattern:

The agent’s core logic runs as a durable Ray Actor, with lifecycle and placement managed by Ray’s Global Control Store (GCS) for high availability.

Tools are executed as thousands of stateless Ray Tasks, enabling massive parallelism and elasticity.

Untrusted or dynamically generated code runs in gVisor sandboxes, providing kernel-level isolation without compromising throughput—made possible through Kubernetes’ secure runtime capabilities.

Alex and Brandon demonstrate the architecture with a series of live scenarios, including a financial analysis agent running on a Ray cluster on Google Kubernetes Engine (GKE).

They then show how the architecture leverages deep Kubernetes-native integrations:

KubeRay’s topology-aware placement allows Ray to understand node-level characteristics, enabling optimal scheduling.

This unlocks intelligent capacity management with tools like Kueue for cost-efficient batch scheduling.

And it provides a clear pathway to mission-critical resilience, supporting zero-downtime upgrades and fault-tolerant agent execution.

Attendees will leave with a practical blueprint for deploying agentic AI systems in production—combining Ray’s distributed computing strengths with Kubernetes’ security and orchestration capabilities to build scalable, resilient, and secure agentic runtimes.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
