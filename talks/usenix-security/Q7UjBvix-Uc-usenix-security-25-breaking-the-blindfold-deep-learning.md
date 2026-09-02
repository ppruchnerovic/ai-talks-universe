---
id: Q7UjBvix-Uc
title: "USENIX Security '25 - Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis"
slug: usenix-security-25-breaking-the-blindfold-deep-learning
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 20
published_at: 2025-10-30T20:02:02Z
video_id: Q7UjBvix-Uc
url: https://www.youtube.com/watch?v=Q7UjBvix-Uc
youtube_url: https://www.youtube.com/watch?v=Q7UjBvix-Uc
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `20 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=Q7UjBvix-Uc) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Breaking the Blindfold: Deep Learning-based Blind Side-channel Analysis

Azade Rezaeezade, Delft University of Technology and Digital Security Group, Radboud University; Trevor Yap, Dirmanto Jap, and Shivam Bhasin, Temasek Laboratories and National integrated Centre For Evaluation, Nanyang Technological University; Stjepan Picek, Digital Security Group, Radboud University and University of Zagreb Faculty of Electrical Engineering and Computing

Physical side-channel analysis (SCA) operates on the foundational assumption of access to known plaintext or ciphertext. However, this assumption can be easily invalidated in various scenarios, ranging from common encryption modes like Offset CodeBook (OCB) to complex hardware implementations, where such data may be inaccessible. Blind SCA addresses this challenge by operating without the knowledge of plaintext or ciphertext. Unfortunately, prior such approaches have shown limited success in practical settings.
This paper introduces the Deep Learning-based Blind Side-channel Analysis (DL-BSCA) framework, leveraging deep neural networks to recover secret keys in blind SCA settings. In addition, we propose a novel labeling method, Multi-point Cluster-based (MC) labeling, accounting for dependencies between leakage variables by exploiting multiple sample points for each variable, improving the accuracy of trace labeling. We validate our approach across four datasets, including symmetric key algorithms (AES and Ascon) and a post-quantum cryptography algorithm, Kyber, with platforms ranging from high-leakage 8-bit AVR XMEGA to noisy 32-bit ARM STM32F4. Notably, previous methods failed to recover the key on the same datasets. We demonstrate the first successful blind SCA on a desynchronization countermeasure enabled by DL-BSCA and MC labeling. All experiments are validated with real-world SCA measurements, highlighting the practicality and effectiveness of our approach.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
