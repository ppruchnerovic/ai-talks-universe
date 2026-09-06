---
id: rTi0z32i8XE
title: "Lightning Talk: Challenges and Standardization in PyTorch Ecosystem... - Zesheng Zong & Ashok Emani"
slug: lightning-talk-challenges-and-standardization-in-pytorch
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Zesheng Zong", "Ashok Emani"]
channel: "PyTorch"
duration_min: 13
published_at: 2025-11-04T03:45:45Z
video_id: rTi0z32i8XE
url: https://www.youtube.com/watch?v=rTi0z32i8XE
youtube_url: https://www.youtube.com/watch?v=rTi0z32i8XE
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Lightning Talk: Challenges and Standardization in PyTorch Ecosystem... - Zesheng Zong & Ashok Emani

**Zesheng Zong, Ashok Emani**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=rTi0z32i8XE) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: Challenges and Standardization in PyTorch Ecosystem Accelerators - Zesheng Zong, Huawei & Ashok Emani, Intel

This talk aims to provide a practical and structured overview of the current challenges and recent standardization efforts in supporting accelerators within the PyTorch ecosystem. By sharing community-driven solutions and practical implementations, we hope to help more hardware developers and contributors effectively integrate with PyTorch and improve the overall developer experience.

The TAC Out-of-Tree Working Group was formed to address these ecosystem gaps. Efforts include:

Testing Framework & Quality Standards
A public testing repository(pytorch-fdn/oota) was established to support daily CI testing for plugin stability. This initiative helps ensure that hardware plugins remain compatible with PyTorch core changes. Additionally, we standardized testing and quality standards for out-of-tree accelerators.

Simplified Plugin and Feature Integration
We optimized the integration mechanism and introduced automatic plugin loading to reduce the complexity of adding new devices. Including improving the code generalization and less coupling with CUDA, which previously made device-specific changes difficult. And make torch.compile better support integrating out-of-tree devices.
