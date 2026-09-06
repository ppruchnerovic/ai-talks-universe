---
id: gjPQ8J38SSw
title: "Breaking Heterogeneity Barriers: Unified Cloud-to-Robot AI System SW Stack for... - Yonghua Lin"
slug: breaking-heterogeneity-barriers-unified-cloud-to-robot-ai
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Yonghua Lin"]
channel: "PyTorch"
duration_min: 30
published_at: 2025-11-04T03:47:26Z
video_id: gjPQ8J38SSw
url: https://www.youtube.com/watch?v=gjPQ8J38SSw
youtube_url: https://www.youtube.com/watch?v=gjPQ8J38SSw
tags: []
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: false
---

# Breaking Heterogeneity Barriers: Unified Cloud-to-Robot AI System SW Stack for... - Yonghua Lin

**Yonghua Lin**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=gjPQ8J38SSw) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Breaking Heterogeneity Barriers: Unified Cloud-to-Robot AI System SW Stack for Embodied Intelligence - Yonghua Lin, BAAI

Embodied AI demands unprecedented efficiency: brain-planning models (VLM) evolve in the cloud while sensing-action models (VLA) run on resource-constrained robots. This dual-stack paradigm introduces critical challenges including compute fragmentation (requiring 1,000+ GPU clusters for VLMs vs ≤10ms response for VLAs), hardware heterogeneity across cloud and edge devices, and latency cliffs in end-to-end execution pipeline. Multi-robot scenarios further exacerbate these challenges, often exceeding human-level response standards (≤100ms) and causing system instability.

In this talk, we present FlagOS - our PyTorch-native unified AI system software stack that seamlessly extends PyTorch's capabilities to embodied AI. Through its parallel framework FlagScale, unified communication library FlagCX, and underlying Triton-based operator library FlagGEM with AI compiler FlagTree, FlagOS provides a PyTorch-based solution for Embodied AI. We'll demonstrate how this stack powers innovative embodied AI solutions like RoboBrain and RoboOS across diverse robot hardware platforms, effectively mitigating the challenges posed by hardware heterogeneity.
