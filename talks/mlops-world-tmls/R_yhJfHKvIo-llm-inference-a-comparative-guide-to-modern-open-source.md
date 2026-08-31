---
id: R_yhJfHKvIo
title: "LLM Inference: A Comparative Guide to Modern Open-Source Runtimes | Aleksandr Shirokov, Wildberries"
slug: llm-inference-a-comparative-guide-to-modern-open-source
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2025
speakers: ["Aleksandr Shirokov"]
channel: null
duration_min: 52
published_at: 2025-10-20T23:50:19Z
video_id: R_yhJfHKvIo
youtube_url: https://www.youtube.com/watch?v=R_yhJfHKvIo
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# LLM Inference: A Comparative Guide to Modern Open-Source Runtimes | Aleksandr Shirokov, Wildberries

**Aleksandr Shirokov**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2025` · `52 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=R_yhJfHKvIo) · [Conference site](https://mlopsworld.com/)

## Description

🎥 From the MLOps World | GenAI Summit 2025 — Virtual Session (October 6, 2025)

Session Title: LLM Inference: A Comparative Guide to Modern Open-Source Runtimes
Speaker: Aleksandr Shirokov, Team Lead MLOps Engineer, Wildberries
Talk Track: LLMs on Kubernetes

Abstract:
Deploying large language models at scale isn’t one-size-fits-all. In this technical deep dive, Aleksandr Shirokov shares how the Wildberries AI team built and battle-tested a production-grade LLM serving platform using vLLM, Triton TensorRT-LLM, Text Generation Inference (TGI), and SGLang.

You’ll get a detailed look at their custom benchmarking setup, the trade-offs across runtimes, and when each framework makes sense—depending on model size, latency targets, and workload patterns.

The talk also covers:

• Implementing HPA for vLLM and reducing cold start times with Tensorize
• Co-locating multiple vLLM models per pod to save GPU memory
• Using SAQ-based queue wrappers for fair and efficient request handling
• Wrapping endpoints with Kong for per-user rate limits, token quotas, and observability

Finally, Aleksandr shares insights from running DeepSeek R1-0528 in production, maintaining flexibility while keeping cost and complexity under control.

What you’ll learn:

• Why there’s no single best LLM serving stack
• How to benchmark, deploy, and optimize multiple runtimes effectively
• Trade-offs between frameworks like vLLM, TGI, Triton, and SGLang
• How to design an LLM inference setup that fits your use case

📍 Recorded: October 6, 2025 — Virtual Day, MLOps World | GenAI Summit 2025, Austin, TX
🔗 Learn more: https://mlopsworld.com
