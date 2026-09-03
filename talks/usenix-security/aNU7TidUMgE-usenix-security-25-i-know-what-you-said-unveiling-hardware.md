---
id: aNU7TidUMgE
title: "USENIX Security '25 - I Know What You Said: Unveiling Hardware Cache Side-Channels in Local Large"
slug: usenix-security-25-i-know-what-you-said-unveiling-hardware
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 15
published_at: 2025-10-30T19:58:13Z
video_id: aNU7TidUMgE
url: https://www.youtube.com/watch?v=aNU7TidUMgE
youtube_url: https://www.youtube.com/watch?v=aNU7TidUMgE
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - I Know What You Said: Unveiling Hardware Cache Side-Channels in Local Large

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `15 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=aNU7TidUMgE) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

I Know What You Said: Unveiling Hardware Cache Side-Channels in Local Large Language Model Inference

Zibo Gao, Junjie Hu, Feng Guo, Yixin Zhang, Yinglong Han, Siyuan Liu, Haiyang Li, and Zhiqiang Lv, Institute of Information Engineering, Chinese Academy of Sciences and School of Cyber Security, University of Chinese Academy of Sciences

Large Language Models (LLMs) that can be deployed locally have recently gained popularity for privacy-sensitive tasks, with companies such as Meta, Google, and Intel playing significant roles in their development. However, the security of local LLMs through the lens of hardware cache side-channels remains unexplored. In this paper, we unveil novel side-channel vulnerabilities in local LLM inference: token value and token position leakage, which can expose both the victim's input and output text, thereby compromising user privacy. Specifically, we found that adversaries can infer the token values from the cache access patterns of the token embedding operation, and deduce the token positions from the timing of autoregressive decoding phases. To demonstrate the potential of these leaks, we design a novel eavesdropping attack framework targeting both open-source and proprietary LLM inference systems. The attack framework does not directly interact with the victim's LLM and can be executed without privilege.

We evaluate the attack on a range of practical local LLM deployments (e.g., Llama, Falcon, and Gemma), and the results show that our attack achieves promising accuracy. The restored output and input text have an average edit distance of 5.2% and 17.3% to the ground truth, respectively. Furthermore, the reconstructed texts achieve average cosine similarity scores of 98.7% (input) and 98.0% (output).

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
