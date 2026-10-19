---
id: riEnw0MDbKQ
title: "How Do We Compress Giant AI Models to Run at the Edge? - Léo Arsenin - Cloudflare - dotAI 2026"
slug: how-do-we-compress-giant-ai-models-to-run-at-the-edge-leo
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Léo Arsenin"]
channel: "dotconferences"
duration_min: 11
published_at: 2026-09-28T14:00:24Z
video_id: riEnw0MDbKQ
url: https://www.youtube.com/watch?v=riEnw0MDbKQ
youtube_url: https://www.youtube.com/watch?v=riEnw0MDbKQ
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# How Do We Compress Giant AI Models to Run at the Edge? - Léo Arsenin - Cloudflare - dotAI 2026

**Léo Arsenin**

`dotAI` · `dot conferences` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=riEnw0MDbKQ) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Léo Arsenin, Solutions Engineer at Cloudflare: https://www.dotai.io/

Leo helps startups and scale-ups build on the platform that powers 20% of the web. As a Solutions Engineer at Cloudflare, he partners with customers to bridge the gap between infrastructure and AI. His work focuses on architecting agentic workloads and deploying AI inference services.

Lightning talk: "How Do We Compress Giant AI Models to Run at the Edge?"

Quantization is the go-to method for making LLMs smaller, but it's lossy, quality degrades in ways that are hard to predict and impossible to reverse. We found a different path by looking at how model weights are actually stored. In BF16 format, every weight has an 8-bit exponent, but only 16 values out of 256 cover 99% of all weights in a typical layer. Information theory says you need just 2.6 bits to represent that distribution, which means 5.4 bits per weight are pure waste. Unweight applies Huffman coding to the exponent stream, decompresses directly in fast on-chip shared memory, and feeds the reconstructed weights straight to the tensor cores, they never round-trip through slow main memory. The result is a 22% model size reduction that is 100% lossless with bit-exact outputs, saving roughly 3 GB of VRAM on Llama 3.1 8B alone. For Cloudflare, this means fitting more models on fewer GPUs across our 330+ city network, making inference cheaper and faster for everyone. We open-sourced the GPU kernels and published the full research paper, so you can use this technique on your own models today. If you care about running AI sustainably and affordably, this talk shows you a compression approach that doesn't ask you to sacrifice quality.
