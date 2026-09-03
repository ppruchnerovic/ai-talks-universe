---
id: 4d6WZEF1iIc
title: "USENIX Security '25 - Private Investigator: Extracting Personally Identifiable Information..."
slug: usenix-security-25-private-investigator-extracting
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 12
published_at: 2025-10-30T20:03:02Z
video_id: 4d6WZEF1iIc
url: https://www.youtube.com/watch?v=4d6WZEF1iIc
youtube_url: https://www.youtube.com/watch?v=4d6WZEF1iIc
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Security, safety & red teaming", "Training, fine-tuning & model building"]
transcript: false
---

# USENIX Security '25 - Private Investigator: Extracting Personally Identifiable Information...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `12 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=4d6WZEF1iIc) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Private Investigator: Extracting Personally Identifiable Information from Large Language Models Using Optimized Prompts

Seongho Keum and Dongwon Shin, KAIST; Leo Marchyok and Sanghyun Hong, Oregon State University; Sooel Son, KAIST

Recent studies on training data extraction attacks have demonstrated significant threats to the language model ecosystem. In a typical machine learning deployment scenario where a pre-trained language model is fine-tuned on users' private data, an adversary may attempt to leak personally identifiable information (PII) memorized by the fine-tuned model. Prior work has demonstrated this privacy risk by inducing a model to output PII in response to handcrafted or outsourced prompts. However, little attention has been given to how a smart adversary will design optimal prompts for successful PII extraction.

In this work, we address this knowledge gap. We propose Private Investigator, an attack framework designed to optimize prompts for querying a target language model to extract PII used for its fine-tuning process. We propose a new prompt generation method that aims to craft promising prompts, which induce the target language model to emit as many PII items as possible by exploring diverse contexts. Private Investigator then exploits these generated prompts to conduct extraction attacks. To this end, we develop a prompt selection strategy that prioritizes the most promising prompts for successful PII extraction, taking full advantage of each extraction attack opportunity. In evaluation, we demonstrate that Private Investigator extracts up to 1,254 more email addresses, 634 more phone numbers, and 5,087 more personal names, outperforming existing attacks in extracting PII items.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
