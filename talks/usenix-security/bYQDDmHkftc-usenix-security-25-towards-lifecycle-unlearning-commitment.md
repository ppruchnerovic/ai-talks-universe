---
id: bYQDDmHkftc
title: "USENIX Security '25 - Towards Lifecycle Unlearning Commitment Management: Measuring Sample-level..."
slug: usenix-security-25-towards-lifecycle-unlearning-commitment
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 13
published_at: 2025-10-30T20:02:02Z
video_id: bYQDDmHkftc
url: https://www.youtube.com/watch?v=bYQDDmHkftc
youtube_url: https://www.youtube.com/watch?v=bYQDDmHkftc
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - Towards Lifecycle Unlearning Commitment Management: Measuring Sample-level...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `13 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=bYQDDmHkftc) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Towards Lifecycle Unlearning Commitment Management: Measuring Sample-level Unlearning Completeness

Cheng-Long Wang, King Abdullah University of Science and Technology; Qi Li, King Abdullah University of Science and Technology and National University of Singapore; Zihang Xiang, King Abdullah University of Science and Technology; Yinzhi Cao, Johns Hopkins University; Di Wang, King Abdullah University of Science and Technology

Growing concerns over data privacy and security highlight the importance of machine unlearning--removing specific data influences from trained models without full retraining. Techniques like Membership Inference Attacks (MIAs) are widely used to externally assess successful unlearning. However, existing methods face two key limitations: (1) maximizing MIA effectiveness (e.g., via online attacks) requires prohibitive computational resources, often exceeding retraining costs; (2) MIAs, designed for binary inclusion tests, struggle to capture granular changes in approximate unlearning. To address these challenges, we propose the Interpolated Approximate Measurement (IAM), a framework natively designed for unlearning inference. IAM quantifies sample-level unlearning completeness by interpolating the model's generalization-fitting behavior gap on queried samples. IAM achieves strong performance in binary inclusion tests for exact unlearning and high correlation for approximate unlearning--scalable to LLMs using just one pre-trained shadow model. We theoretically analyze how IAM's scoring mechanism maintains performance efficiently. We then apply IAM to recent approximate unlearning algorithms, revealing general risks of both over-unlearning and under-unlearning, underscoring the need for stronger safeguards in approximate unlearning systems. The code is available at https://github.com/Happy2Git/Unlearning_Inference_IAM.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
