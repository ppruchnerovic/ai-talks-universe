---
id: JBBIPhjmuT0
title: "USENIX Security '25 - Breaking the Layer Barrier: Remodeling Private Transformer Inference with..."
slug: usenix-security-25-breaking-the-layer-barrier-remodeling
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 15
published_at: 2025-10-30T20:00:26Z
video_id: JBBIPhjmuT0
url: https://www.youtube.com/watch?v=JBBIPhjmuT0
youtube_url: https://www.youtube.com/watch?v=JBBIPhjmuT0
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - Breaking the Layer Barrier: Remodeling Private Transformer Inference with...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `15 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=JBBIPhjmuT0) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - Breaking the Layer Barrier: Remodeling Private Transformer Inference with Hybrid CKKS and MPC

Tianshi Xu, Peking University; Wen-jie Lu, TikTok; Jiangrui Yu, Yi Chen, Chenqi Lin, Runsheng Wang, and Meng Li, Peking University

This paper presents an efficient framework for private Transformer inference that combines Homomorphic Encryption (HE) and Secure Multi-party Computation (MPC) to protect data privacy. Existing methods often leverage HE for linear layers (e.g., matrix multiplications) and MPC for non-linear layers (e.g., Softmax activation functions), but the conversion between HE and MPC introduces significant communication costs. The proposed framework, dubbed BLB, overcomes this by breaking down layers into fine-grained operators and further fusing adjacent linear operators, reducing the need for HE/MPC conversions. To manage the increased ciphertext bit width from the fused linear operators, BLB proposes the first secure conversion protocol between CKKS and MPC and enables CKKS-based computation of the fused operators. Additionally, BLB proposes an efficient matrix multiplication protocol for fused computation in Transformers. Extensive evaluations on BERT-base, BERT-large, and GPT2-base show that BLB achieves a 21x reduction in communication overhead compared to BOLT (S&P '24) and a 2x reduction compared to Bumblebee (NDSS '25), along with latency reductions of 13x and 1.8x, respectively, when leveraging GPU acceleration.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
