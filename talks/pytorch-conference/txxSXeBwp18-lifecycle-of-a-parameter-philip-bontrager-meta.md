---
id: txxSXeBwp18
title: "Lifecycle of a Parameter - Philip Bontrager, Meta"
slug: lifecycle-of-a-parameter-philip-bontrager-meta
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Philip Bontrager"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:43:40Z
video_id: txxSXeBwp18
url: https://www.youtube.com/watch?v=txxSXeBwp18
youtube_url: https://www.youtube.com/watch?v=txxSXeBwp18
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: false
---

# Lifecycle of a Parameter - Philip Bontrager, Meta

**Philip Bontrager**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=txxSXeBwp18) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lifecycle of a Parameter - Philip Bontrager, Meta

Long gone are the days where the entire lifecycle of a parameter consists of being initialized on a GPU, updated on the same GPU, and then finally saved to your local SSD. As models and training pipelines scale in size and complexity, a single parameter will get sharded, resharded, streamed across multiple machines, downloaded, possibly quantized, and renamed multiple times. In this talk we’ll follow a parameter through a large-scale LLM RL post-training job to understand everything that needs to happen behind the scenes in Pytorch for this to work. From reading in a checkpoint that’s 100s of GBs, to distributing the parameter across multiple dimensions, quantizing the weights, syncing the weights with an inference server that that is laid out and optimized completely differently, updating all of the shards together, and then saving the parameter split across multiple devices, each part has to work together and happen in almost no time at all. This talk will outline the challenges and some of the current solutions to training parameters at scale.
