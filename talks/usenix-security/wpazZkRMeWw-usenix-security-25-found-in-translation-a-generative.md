---
id: wpazZkRMeWw
title: "USENIX Security '25 - Found in Translation: A Generative Language Modeling Approach to Memory..."
slug: usenix-security-25-found-in-translation-a-generative
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 19
published_at: 2025-10-30T20:03:07Z
video_id: wpazZkRMeWw
url: https://www.youtube.com/watch?v=wpazZkRMeWw
youtube_url: https://www.youtube.com/watch?v=wpazZkRMeWw
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - Found in Translation: A Generative Language Modeling Approach to Memory...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `19 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=wpazZkRMeWw) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - Found in Translation: A Generative Language Modeling Approach to Memory Access Pattern Attacks

Grace Jia, Alex Wong, and Anurag Khandelwal, Yale University

Confidential computing environments (CCEs) provide a secure way for privacy-sensitive applications to ensure the confidentiality and integrity of data and computations offloaded to the cloud, relying on a hardware root of trust. However, the cloud provider-controlled Operating System (OS) stack still manages key memory management system services such as paging. Several recent works have demonstrated that these services can leverage side channels, specifically page access patterns, to reconstruct private application data. However, related attacks have primarily targeted applications with simple one-to-one mappings between application-level objects and OS-level pages, which is seldom true for most real-world cloud applications. Moreover, these attacks tend to overlook correlations in access patterns—a common occurrence in most real-world applications—leaving untapped critical side-channel information for improving attack accuracy.
We propose a novel attack approach that leverages access correlations across pages in cloud applications using generative language models. Our key insight is that there are strong parallels between application page access patterns and grammatical structures in natural languages, making language modeling an excellent fit for reconstructing sensitive application data with high accuracy. Our attack, named FIT, utilizes a recurrent encoder-decoder architecture to predict application-level object accesses from a sequence of page-level accesses. Our evaluations on popular AI/ML model inference services and semantic search applications show that FIT can predict object-level access sequences with an average accuracy ranging from 71.7% to 99.9%, significantly outperforming prior state-of-the-art approaches.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
