---
id: 1cnEPhzVv_c
title: "Benchmarking GPU Scheduling for Massive-Scale Ray Workloads at Minimal Cost - MSFT | Ray Summit 2025"
slug: benchmarking-gpu-scheduling-for-massive-scale-ray-workloads
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 10
published_at: 2025-12-01T20:29:47Z
video_id: 1cnEPhzVv_c
url: https://www.youtube.com/watch?v=1cnEPhzVv_c
youtube_url: https://www.youtube.com/watch?v=1cnEPhzVv_c
tags: []
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: false
---

# Benchmarking GPU Scheduling for Massive-Scale Ray Workloads at Minimal Cost - MSFT | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=1cnEPhzVv_c) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Anson Qian from Microsoft shares a novel, cost-effective approach for benchmarking GPU scheduling and large-scale Ray workloads on Kubernetes—using Kwok (Kubernetes Without Kubelet) to simulate massive Ray clusters without requiring massive hardware.

He begins by outlining a key challenge in ML infrastructure development: validating the scalability and stability of Ray, KubeRay, and Kubernetes GPU scheduling typically requires extremely large and expensive clusters. Traditional testing at this scale is often cost-prohibitive, making it difficult for teams to evaluate performance under realistic production loads.

Anson introduces a breakthrough solution: using Kwok to simulate 10,000 RayCluster and RayJob workloads across 10,000 GPU nodes—all running on a modest, cloud-managed Kubernetes cluster, such as a 3-node Azure Kubernetes Service (AKS) setup. The entire benchmark environment runs for roughly $10 per hour, making large-scale infrastructure testing accessible to any team.

This session covers:

How Kwok simulates massive Kubernetes clusters without real GPU nodes

How to stress-test KubeRay, the Kubernetes control plane, and Ray’s scheduling logic at extreme scale

Techniques for validating stability, analyzing performance, and uncovering bottlenecks before real-world deployment

Why this simulated approach accelerates the development of robust, production-grade ML systems

Anson demonstrates how this simulation framework provides a practical, low-cost path to evaluating large-scale ML infrastructure—unlocking a level of testing depth previously accessible only to teams with enormous compute budgets.

Attendees will leave with an actionable blueprint for scaling Ray, testing GPU scheduling logic, and validating ML infrastructure in a highly efficient, affordable way.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
