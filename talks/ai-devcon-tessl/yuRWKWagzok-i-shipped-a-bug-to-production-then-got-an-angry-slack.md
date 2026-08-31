---
id: yuRWKWagzok
title: "I Shipped a Bug to Production — Then Got an Angry Slack Message (and That's Why This Formula Exists)"
slug: i-shipped-a-bug-to-production-then-got-an-angry-slack
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: null
duration_min: 28
published_at: 2026-05-01T16:01:47Z
video_id: yuRWKWagzok
youtube_url: https://www.youtube.com/watch?v=yuRWKWagzok
tags: []
transcript: false
---

# I Shipped a Bug to Production — Then Got an Angry Slack Message (and That's Why This Formula Exists)

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=yuRWKWagzok) · [Conference site](https://tessl.io/devcon/)

## Description

What happens when 96% of your AI's most expensive computation is completely wasted?

In this talk, Dominic Brown (developer tech at NVIDIA) breaks down skip softmax — a kernel-level optimization that lets you skip redundant attention tiles at inference time, delivering meaningful speedups for long-context workloads without any model retraining.

He covers the full story: from the quadratic cost of attention at 1M+ token context lengths, to online softmax, to the moment a colleague sent him an angry Slack message that changed how the threshold formula actually works.

What you'll learn:

Why attention is both expensive and sparse — and why that matters
How online softmax enables single-pass computation (and why the running max is the secret ingredient)

The skip softmax optimization: what gets skipped, what you save, and the accuracy tradeoffs

Why picking the right threshold is harder than it looks
Where to find this today: TensorRT-LLM, FlashInfer, SGLang, and soon vLLM
