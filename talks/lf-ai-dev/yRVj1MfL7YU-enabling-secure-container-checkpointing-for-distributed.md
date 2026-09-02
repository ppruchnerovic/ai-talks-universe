---
id: yRVj1MfL7YU
title: "Enabling Secure Container Checkpointing for Distributed Model Training - Radostin Stoyanov"
slug: enabling-secure-container-checkpointing-for-distributed
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: ["Radostin Stoyanov"]
channel: "The Linux Foundation"
duration_min: 13
published_at: 2025-09-08T11:36:34Z
video_id: yRVj1MfL7YU
url: https://www.youtube.com/watch?v=yRVj1MfL7YU
youtube_url: https://www.youtube.com/watch?v=yRVj1MfL7YU
tags: []
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming", "Training, fine-tuning & model building"]
transcript: false
---

# Enabling Secure Container Checkpointing for Distributed Model Training - Radostin Stoyanov

**Radostin Stoyanov**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=yRVj1MfL7YU) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Enabling Secure Container Checkpointing for Distributed Model Training - Radostin Stoyanov, University of Oxford

In the field of AI and machine learning, model training has become an increasingly complex and resource-intensive task. Training jobs often run for days or weeks, distributed across multiple nodes with expensive GPU accelerators. Container checkpointing is a crucial technique for implementing fault tolerance, mitigating the impact of hardware and software failures by periodically saving the state of computations and resuming from the last checkpoint in the event of failures. While support for checkpointing has been recently integrated into Kubernetes, enabling checkpoint/restore coordination across multiple containers and nodes remains a challenge. In this talk, we are going to discuss how we have extended container runtimes and CRIU to synchronize checkpointing operations among multiple container instances in Kubernetes clusters. The talk will cover how we enable efficient end-to-end encryption for sensitive data in checkpoints and the integration with existing container platforms.
