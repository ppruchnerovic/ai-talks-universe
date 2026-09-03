---
id: uCl0MvchI08
title: "USENIX Security '25 - IDFuzz: Intelligent Directed Grey-box Fuzzing"
slug: usenix-security-25-idfuzz-intelligent-directed-grey-box
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 11
published_at: 2025-10-30T20:02:11Z
video_id: uCl0MvchI08
url: https://www.youtube.com/watch?v=uCl0MvchI08
youtube_url: https://www.youtube.com/watch?v=uCl0MvchI08
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - IDFuzz: Intelligent Directed Grey-box Fuzzing

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `11 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=uCl0MvchI08) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

IDFuzz: Intelligent Directed Grey-box Fuzzing

Yiyang Chen, Tsinghua University; Chao Zhang, Tsinghua University and JCSS, Tsinghua University (INSC) - Science City (Guangzhou) Digital Technology Group Co., Ltd.; Long Wang, Tsinghua University; Wenyu Zhu, Tsinghua University and AscendGrace Tech; Changhua Luo, Wuhan University; Nuoqi Gui, Zheyu Ma, and Xingjian Zhang, Tsinghua University; Bingkai Su, Hunan University

Directed grey-box fuzzing aims to test target code in programs and is widely utilized in various scenarios, including patch testing, candidate vulnerability confirmation, and known vulnerability reproduction. However, we find that existing directed fuzzers generally lack effective input mutation strategies and resort to the randomness and empiricism inherent in AFL-based strategies, which prove to be inefficient in directed fuzzing contexts.
This paper presents IDFuzz, an intelligent input mutation solution for directed fuzzing. Our key insight is to leverage a neural network model to learn from historically mutated inputs and extract useful experience that can guide input mutation towards the target code. We introduce several novel techniques in model construction and model training, which help build a model that well captures experience on how to cover both explored and unexplored code relevant to the target. We further devise a refined model gradient-guided scheme that leverages the experience to locate critical input fields and develop a directed input mutation strategy. We implement IDFuzz as an input mutation module that complements most open-source state-of-the-art directed fuzzers. In our evaluation, IDFuzz significantly accelerates existing directed fuzzers by over 2.48x in reproducing target vulnerabilities on the Google Fuzzer Test Suite. Moreover, we demonstrate that IDFuzz helps existing directed fuzzers reduce ineffective mutations by 91.86%. Lastly, we detected 6 previously unknown vulnerabilities with 4 CVE IDs assigned so far and 1 incomplete fix of a high-severity vulnerability in well-tested real-world software using IDFuzz.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
