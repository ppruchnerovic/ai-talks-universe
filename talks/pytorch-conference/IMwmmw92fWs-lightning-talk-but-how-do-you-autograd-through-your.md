---
id: IMwmmw92fWs
title: "Lightning Talk: But How Do You Autograd Through Your Simulator? Making a... - R. Dagli & S. Lamba"
slug: lightning-talk-but-how-do-you-autograd-through-your
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["R. Dagli", "S. Lamba"]
channel: "PyTorch"
duration_min: 11
published_at: 2025-11-04T03:43:38Z
video_id: IMwmmw92fWs
url: https://www.youtube.com/watch?v=IMwmmw92fWs
youtube_url: https://www.youtube.com/watch?v=IMwmmw92fWs
tags: []
topics: []
transcript: false
---

# Lightning Talk: But How Do You Autograd Through Your Simulator? Making a... - R. Dagli & S. Lamba

**R. Dagli, S. Lamba**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=IMwmmw92fWs) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: But How Do You Autograd Through Your Simulator? Making a Differentiable Simulator in PyTorch - Rishit Dagli, University of Toronto & Shivay Lamba, Qualcomm

This talk is a playbook for making any PyTorch physics engine: rigid bodies, deformables or fluids into a differentiable simulator. This is a very relevant problem for many learning problems like, policy search in robotics, video/SDS-based parameter estimation for simulators, and soft‑material co‑design. Simply wrapping time‑stepping code with torch.autograd breaks down at the first contact, constraint or implicit solve. This causes many people to use other frameworks for differentiable physics.

There are a few challenges (1) non‑smooth events like collisions that violate the smooth chain rule assumed by autograd (2) implicit updates (backward Euler, FEM) that hide the true computational graph, and (3) long roll‑outs that explode memory.

One of our main focuses would be differentiating through inner solvers (CG/Newton) iters by implicit differentiation. We show a grab‑bag of engineering tricks: smooth contact proxies, Jacobian‑free back‑propagation to avoids linear solves during backward passes and memory‑frugal checkpointing to keep large rollouts on GPU. By the end, attendees will leave with compact recipes to make their own simulators differentiable while being stable enough.
