---
id: GG1qi82J8Hg
title: "How IBM Research Achieved vLLM Platform Portability with Triton Autotuning | Ray Summit 2024"
slug: how-ibm-research-achieved-vllm-platform-portability-with
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2024
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2024-10-18T21:11:10Z
video_id: GG1qi82J8Hg
url: https://www.youtube.com/watch?v=GG1qi82J8Hg
youtube_url: https://www.youtube.com/watch?v=GG1qi82J8Hg
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# How IBM Research Achieved vLLM Platform Portability with Triton Autotuning | Ray Summit 2024

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2024` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=GG1qi82J8Hg) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2024, Burkhard Ringlein from IBM Research addresses the challenges of achieving platform portability for vLLM, the current industry standard for serving Large Language Models. The talk focuses on overcoming vLLM's dependence on hand-written CUDA kernels, which can hinder performance across different hardware platforms.

Ringlein explains how IBM Research introduces a "dejavu" mechanism for the Triton autotuner, designed to eliminate the overhead typically associated with autotuning in production environments. This innovation allows the autotuner to "remember" earlier kernel executions, reducing its overhead to zero. The presentation covers early results showing speed-ups of over 100% for some kernels, improved cross-platform performance using the same code, and reduced external dependencies for vLLM. Ringlein also demonstrates Triton-only vLLM deployments, offering insights into more portable and future-proof LLM serving solutions.

--

Interested in more?
- Watch the full Day 1 Keynote: https://youtu.be/jwZHJthQvXo
- Watch the full Day 2 Keynote https://youtu.be/Lury2ad6KG8

--

🔗 Connect with us:
- Subscribe to our YouTube channel: https://www.youtube.com/@anyscale
- Twitter: https://x.com/anyscalecompute
- LinkedIn: https://linkedin.com/company/joinanyscale/
- Website: https://www.anyscale.com
