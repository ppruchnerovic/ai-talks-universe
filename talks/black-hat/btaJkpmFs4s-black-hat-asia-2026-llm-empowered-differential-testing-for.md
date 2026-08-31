---
id: btaJkpmFs4s
title: "Black Hat Asia 2026 | LLM-Empowered Differential Testing for the Ethereum Infrastructure"
slug: black-hat-asia-2026-llm-empowered-differential-testing-for
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: null
duration_min: 39
published_at: 2026-08-28T23:00:32Z
video_id: btaJkpmFs4s
youtube_url: https://www.youtube.com/watch?v=btaJkpmFs4s
tags: []
transcript: false
---

# Black Hat Asia 2026 | LLM-Empowered Differential Testing for the Ethereum Infrastructure

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `39 min`

[Watch the recording](https://www.youtube.com/watch?v=btaJkpmFs4s) · [Conference site](https://www.blackhat.com/)

## Description

Securing over $380 billion in digital assets, the Ethereum ecosystem relies entirely on clients to bridge users and the blockchain network. However, this infrastructure remains perilously fragile: the infamous CVE-2020-26241, a single memory corruption bug in the dominant Geth client, triggered an unintended Ethereum mainnet chain fork, causing a catastrophic 7-hour outage for major infrastructures like Infura and MetaMask. While the community now champions "client diversity" to mitigate such single points of failure, this heterogeneity introduces a new, insidious threat: subtle implementation inconsistencies across different languages and architectures that traditional testing methods fail to detect.

To fortify this multi-billion dollar foundation, we propose a novel, specification-driven differential testing framework that synergizes classical software engineering with modern AI. Unlike traditional fuzzers, our approach leverages Large Language Models (LLMs) to bridge the gap between abstract specifications and complex reality. We utilize LLMs not only to generate diverse, semantically valid test inputs (covering both EVM opcodes and Client APIs) but also to act as intelligent filters that distinguish genuine bugs from harmless semantic variations. This "dual-engine" approach allows us to identify deep logic flaws with high precision while minimizing false positives.

Our comprehensive evaluation across 11 distinct clients uncovered 98 previously unknown bugs, even including critical errors within the official Ethereum specifications themselves. The impact of our work is immediate and far-reaching: developers confirmed our findings with a greater than 90% acceptance rate, 4 vulnerabilities were assigned CNVD IDs, and our methodology has received official endorsement from the Ethereum Foundation, with specific findings escalated to core protocol management meetings. We provide not just a bug-finding approach, but a crucial safeguard for the stability of the decentralized economy.

Jie Ma  |  Eng.D Candidate, Beihang University; Zhongguancun Laboratory
Ningyu He  |  Research Assistant Professor, The Hong Kong Polytechnic University; Amber Group
Chiachih Wu  |  Partner & Head of Web3 Security, Amber Group
Haoyu Wang  |  Professor, Huazhong University of Science and Technology
Ying Gao  |  Associate Professor, Beihang University; Zhongguancun Laboratory
Yinliang Yue  |  Professor, Zhongguancun Laboratory
