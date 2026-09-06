---
id: RA5GRNJOW2w
title: "Inside Adobe Firefly: JIT-Embedding with Ray Serve for Faster GenAI Training | Ray Summit 2025"
slug: inside-adobe-firefly-jit-embedding-with-ray-serve-for
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2025-11-20T21:29:10Z
video_id: RA5GRNJOW2w
url: https://www.youtube.com/watch?v=RA5GRNJOW2w
youtube_url: https://www.youtube.com/watch?v=RA5GRNJOW2w
tags: []
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: false
---

# Inside Adobe Firefly: JIT-Embedding with Ray Serve for Faster GenAI Training | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=RA5GRNJOW2w) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Haoran Cai and Baqiao Liu from Adobe share how they accelerated large-scale Generative AI training for Adobe Firefly through JIT-Embedding (Just-in-Time Embedding)—a novel Ray Serve–powered architecture that decouples embedding computation from model training to dramatically improve scalability, performance, and cost efficiency.

They begin by outlining the core bottlenecks in foundation diffusion model training for image and video generation, including slow on-the-fly embedding computation (VAE, CLIP, T5), the high cost and long turnaround time of offline embedding precomputation, and severe GPU memory constraints when training high-resolution or large-scale models.

To overcome these challenges, Adobe developed JIT-Embedding, a Ray Serve–based system that enables embedding computation and model training to scale independently. The speakers walk through its major components and innovations:

JIT Service via Ray Serve – Embedding computation is wrapped as an on-demand, autoscaled service deployed on underutilized lower-tier GPUs (e.g., A100), freeing H100s for training while reducing GPU memory pressure on both sides.

JIT Client integrated with the Dataloader – Multiprocessing and prefetching overlap embedding requests with training, hiding latency and maximizing end-to-end GPU utilization.

High-throughput Serialization/Deserialization – A custom Rust + Python library compresses multimodal data (images, videos, long text) to speed up client–server communication and increase system flexibility.

Advanced performance optimizations – Ray Serve’s dashboards plus Adobe’s custom profiling and load-testing tools enable dynamic batching, autoscaling, in-place updates, client-side load balancing, overlapping CPU/GPU execution, optimized codecs, and shared GPU usage across models.

JIT Cache – Automatically stores computed embeddings for reuse in future training jobs, further reducing compute time and cost.

The presenters share end-to-end experimental results demonstrating how JIT-Embedding significantly improved scalability, enabled higher-resolution Firefly model training, and delivered substantial performance gains and cost reductions—contributing to the public release of the Firefly Video Model.

Haoran and Baqiao conclude with future directions, lessons learned from building on Ray Serve, and Adobe’s plan to open source the entire JIT-Embedding stack, including services, clients, and the serialization library.

Attendees will leave with a deep understanding of how to decouple multimodal embedding workloads from training, optimize GPU allocation at scale, and use Ray Serve to accelerate next-generation GenAI pipelines.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute
