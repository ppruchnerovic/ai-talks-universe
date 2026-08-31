---
id: nTEnQnW0zZQ
title: "Vamba Understanding Hour Long Videos with Hybrid"
slug: vamba-understanding-hour-long-videos-with-hybrid
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2025
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 29
published_at: 2025-07-23T15:35:39Z
video_id: nTEnQnW0zZQ
youtube_url: https://www.youtube.com/watch?v=nTEnQnW0zZQ
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Vamba Understanding Hour Long Videos with Hybrid

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2025` · `29 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=nTEnQnW0zZQ) · [Conference site](https://mlopsworld.com/)

## Description

Weiming Ren, Ph.D. Student, University of Waterloo

About the Speaker:
Weiming Ren is a second year Ph.D. student at the Cheriton School of Computer Science, University of Waterloo, supervised by Prof. Wenhu Chen. His research interests include designing efficient model architectures and data curation pipelines to enhance large multimodal models (LMMs) for image and video understanding, as well as developing novel algorithms for controllable video generation, image and video editing, and image restoration.

Abstract:
State-of-the-art transformer-based large multimodal models (LMMs) struggle to handle hour-long video inputs due to the quadratic complexity of the causal self-attention operations, leading to high computational costs during training and inference. Existing token compression-based methods reduce the number of video tokens but often incur information loss and remain inefficient for extremely long sequences. In this work, we explore an orthogonal direction to build a hybrid Mamba-Transformer model (VAMBA) that employs Mamba-2 blocks to encode video tokens with linear complexity. Without any token reduction, VAMBA can encode more than 1024 frames (640×360) on a single GPU, while transformer-based models can only encode 256 frames. On long video input, VAMBA achieves at least 50% reduction in GPU memory usage during training and inference, and nearly doubles the speed per training step compared to transformer-based LMMs. Our experimental results demonstrate that VAMBA improves accuracy by 4.6% on the challenging hour-long video understanding benchmark LVBench over prior efficient video LMMs, and maintains strong performance on a broad spectrum of long and short video understanding tasks.
