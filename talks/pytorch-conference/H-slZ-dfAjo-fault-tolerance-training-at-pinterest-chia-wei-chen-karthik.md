---
id: H-slZ-dfAjo
title: "Fault Tolerance Training at Pinterest - Chia-Wei Chen & Karthik Anantha Padmanabhan, Pinterest"
slug: fault-tolerance-training-at-pinterest-chia-wei-chen-karthik
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 28
published_at: 2025-11-04T03:43:38Z
video_id: H-slZ-dfAjo
url: https://www.youtube.com/watch?v=H-slZ-dfAjo
youtube_url: https://www.youtube.com/watch?v=H-slZ-dfAjo
tags: []
topics: []
transcript: false
---

# Fault Tolerance Training at Pinterest - Chia-Wei Chen & Karthik Anantha Padmanabhan, Pinterest

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=H-slZ-dfAjo) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Fault Tolerance Training at Pinterest - Chia-Wei Chen & Karthik Anantha Padmanabhan, Pinterest

At Pinterest, our machine learning training datasets often far exceed available memory, requiring us to stream data from object stores such as Amazon S3. This scale makes traditional epoch-level checkpointing unfeasible, as a single epoch may last hours or days, making it difficult to accurately resume training if interrupted. To solve this, we leverage StatefulDataloader to enable fine-grained, iteration-level checkpointing, capturing not only the model, optimizer, and lr scheduler states, but also the precise dataloader position. This approach ensures robust fault tolerance for large-scale distributed training, allowing training jobs to resume seamlessly without skipping or duplicating data samples. We have integrated this capability into a managed platform, abstracting complexity for end users and providing seamless access through our CLI, UI, and workflow systems. With thousands of training jobs adversely affected each month by platform or upstream failures, our solution dramatically improves reliability and productivity for ML practitioners at Pinterest. We share technical insights, challenges, and real-world impact resulting from this framework.
