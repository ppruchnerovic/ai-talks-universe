---
id: 0i8UhpUgw_0
title: "Black Hat USA | LLMs-Driven Automated YARA Rules Generation with Explainable File Features & DNAHash"
slug: black-hat-usa-llms-driven-automated-yara-rules-generation
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 25
published_at: 2026-03-07T14:00:04Z
video_id: 0i8UhpUgw_0
youtube_url: https://www.youtube.com/watch?v=0i8UhpUgw_0
tags: []
transcript: false
---

# Black Hat USA | LLMs-Driven Automated YARA Rules Generation with Explainable File Features & DNAHash

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=0i8UhpUgw_0) · [Conference site](https://www.blackhat.com/)

## Description

Malware on the cloud is growing massively every day, and an automated rule generation solution is needed to improve operational efficiency. YARA is a widely used tool for creating malware signatures and detection rules, however, existing YARA-based automated rules generation solutions suffer from limitations in three key areas: rule quality, false positive rates, and the interpretability of features. These shortcomings restrict their effectiveness in real-world malicious threat detection scenarios.

In this presentation, we will introduce LLMDYara, which is an automated rule generation solution that integrates expert knowledge with large language models. We first utilize expert knowledge to pre-extract string, function, and file DNAHash features. Subsequently, we design a function signature algorithm and an efficient querying similarity search mechanism to filter these features against a billion-scale white database, thereby enhancing feature quality. We then leverage large models for string feature evaluation and functional identification of function fragments, where the latter enhanced the interpretability of opcode features. Finally, we generated YARA rules through an ensemble decision based on selected features. Our newly introduced file DNAHash feature ensures rule usability even when other features have lower quality, further reducing false positives.

Our automated rule generation solution has made efforts to address challenges such as reducing false positives, enhancing feature interpretability, and improving rule quality. Additionally, we will share our experiences in feature engineering and large language model fine-tuning, with the hope that these insights will help advance the application of large language models in the program analysis domain.

By:
Xiaochen Wang  |  Security Engineer, Alibaba Cloud
Yiping Liu  |  Security Engineer, Alibaba Cloud
Xiaoman Wang  |  Security Engineer, Alibaba Cloud
Cong Cheng  |  Senior Security Engineer, Alibaba Cloud

Presentation Materials Available at:
