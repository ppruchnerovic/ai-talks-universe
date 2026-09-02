---
id: _FpCefZeObw
title: "USENIX Security '25- ORTHRUS: Achieving High Quality of Attribution in Provenance-based Intrusion..."
slug: usenix-security-25-orthrus-achieving-high-quality-of
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 9
published_at: 2025-10-30T20:03:07Z
video_id: _FpCefZeObw
url: https://www.youtube.com/watch?v=_FpCefZeObw
youtube_url: https://www.youtube.com/watch?v=_FpCefZeObw
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Classic ML & data science", "Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25- ORTHRUS: Achieving High Quality of Attribution in Provenance-based Intrusion...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `9 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=_FpCefZeObw) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

ORTHRUS: Achieving High Quality of Attribution in Provenance-based Intrusion Detection Systems

Baoxiang Jiang, Xi'an Jiaotong University; Tristan Bilot, Université Paris-Saclay, LISITE– Isep, and Iriguard; Nour El Madhoun, LISITE – Isep; Khaldoun Al Agha, Université Paris-Saclay; Anis Zouaoui, Iriguard; Shahrear Iqbal, National Research Council Canada; Xueyuan Han, Wake Forest University; Thomas Pasquier, University of British Columbia

Past success in applying machine learning to data provenance graphs – a structured representation of the history of operating system activities – to detect host system intrusions has fueled continued interest in the security community. Recent solutions, particularly anomaly-based approaches using graph neural networks to detect previously unknown attacks, have reported near-perfect accuracy. Surprisingly, despite this high performance, the industry remains reluctant to adopt these intrusion detection systems (IDSs).

We identify Quality of Attribution (QoA) as the key factor contributing to this disconnect. QoA refers to the amount of effort required from a human analyst to investigate an IDS's detection output, uncover the root causes of an attack, understand its ramifications, and dismiss potential false alarms. Unfortunately, prior work often generates large volumes of low-QoA output, much of which is irrelevant to attack activities, leading to alert fatigue and analyst burnout.We introduce ORTHRUS, the first IDS to achieve high-QoA detection on data provenance graphs at the node level. ORTHRUS detects malicious hosts using a graph neural network (GNN) encoder designed to capture the fine-grained spatio-temporal dynamics of system events. It then reconstructs the attack path through dependency analysis to ensure high-QoA detection.

We compare ORTHRUS against five state-of-the-art IDSs. ORTHRUS reduces the number of nodes requiring manual inspection for attack attribution by several orders of magnitude, significantly easing the burden on security analysts while achieving strong detection performance.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
