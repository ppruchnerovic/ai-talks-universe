---
id: tWj843v6B3o
title: "USENIX Security '25 - From Purity to Peril: Backdooring Merged Models From \"Harmless\" Benign..."
slug: usenix-security-25-from-purity-to-peril-backdooring-merged
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 15
published_at: 2025-10-30T20:02:11Z
video_id: tWj843v6B3o
url: https://www.youtube.com/watch?v=tWj843v6B3o
youtube_url: https://www.youtube.com/watch?v=tWj843v6B3o
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - From Purity to Peril: Backdooring Merged Models From "Harmless" Benign...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `15 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=tWj843v6B3o) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

From Purity to Peril: Backdooring Merged Models From "Harmless" Benign Components

Lijin Wang, The Hong Kong University of Science and Technology (Guangzhou); Jingjing Wang, Zhejiang University; Tianshuo Cong, Tsinghua University; Xinlei He, The Hong Kong University of Science and Technology (Guangzhou); Zhan Qin, Zhejiang University; Xinyi Huang, Jinan University

The expansion of capabilities in large-scale models often incurs prohibitively high training costs. Fortunately, recent advancements in model merging techniques have made it possible to efficiently combine multiple large models, each designed for a specific task, into a single multi-functional model with negligible cost. Despite these advantages, there is a notable research gap regarding the security implications of model merging, particularly concerning backdoor vulnerabilities. In this study, we introduce a novel supply chain threat under the model merging scenario: multiple ostensibly benign models can be merged into a backdoored model. To rigorously explore this threat, we propose MergeBackdoor, a versatile training framework designed to suppress backdoor behaviors in upstream models before merging, while simultaneously ensuring the emergence of the backdoor when these models are merged. Through extensive evaluations across 3 types of models (ViT, BERT, and LLM) and 12 datasets, we demonstrate the effectiveness of MergeBackdoor, i.e., the attack success rates (ASRs) of the upstream models before merging are all at a random-guessing level, and the ASRs can reach nearly 1.0 for the final merged model. Besides conducting an in-depth analysis of MergeBackdoor's underlying mechanism, we further demonstrate that even the most knowledgeable detectors fail to identify the anomalies in these models before merging. We highlight that our findings underscore the critical need for security audit throughout the entire merging pipeline.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
