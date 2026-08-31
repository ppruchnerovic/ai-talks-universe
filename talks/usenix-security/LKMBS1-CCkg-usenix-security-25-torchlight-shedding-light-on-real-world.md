---
id: LKMBS1-CCkg
title: "USENIX Security '25 - TORCHLIGHT: Shedding LIGHT on Real-World Attacks on Cloudless IoT Devices"
slug: usenix-security-25-torchlight-shedding-light-on-real-world
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 13
published_at: 2025-10-30T19:58:10Z
video_id: LKMBS1-CCkg
youtube_url: https://www.youtube.com/watch?v=LKMBS1-CCkg
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - TORCHLIGHT: Shedding LIGHT on Real-World Attacks on Cloudless IoT Devices

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `13 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=LKMBS1-CCkg) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

TORCHLIGHT: Shedding LIGHT on Real-World Attacks on Cloudless IoT Devices Concealed within the Tor Network

Yumingzhi Pan and Zhen Ling, Southeast University; Yue Zhang, Drexel University; Hongze Wang, Guangchi Liu, and Junzhou Luo, Southeast University; Xinwen Fu, University of Massachusetts Lowell

The rapidly expanding Internet of Things (IoT) landscape is shifting toward cloudless architectures, removing reliance on centralized cloud services but exposing devices directly to the internet and increasing their vulnerability to cyberattacks. Our research revealed an unexpected pattern of substantial Tor network traffic targeting cloudless IoT devices, suggesting that attackers are using Tor to anonymously exploit undisclosed vulnerabilities (possibly obtained from underground markets). To delve deeper into this phenomenon, we developed TORCHLIGHT, a tool designed to detect both known and unknown threats targeting cloudless IoT devices by analyzing Tor traffic. TORCHLIGHT filters traffic via specific IP patterns, strategically deploys virtual private server (VPS) nodes for cost-effective detection, and uses a chain-ofthought (CoT) process with large language models (LLMs) for accurate threat identification.

Our results are significant: for the first time, we have demonstrated that attackers are indeed using Tor to conceal their identities while targeting cloudless IoT devices. Over a period of 12 months, TORCHLIGHT analyzed 26 TB of traffic, revealing 45 vulnerabilities, including 29 zero-day exploits with 25 CVE-IDs assigned (5 CRITICAL, 3 HIGH, 16 MEDIUM, and 1 LOW) and an estimated value of approximately $312,000. These vulnerabilities affect around 12.71 million devices across 148 countries, exposing them to severe risks such as information disclosure, authentication bypass, and arbitrary command execution. The findings have attracted significant attention, sparking widespread discussion in cybersecurity circles, reaching the top 25 on Hacker News, and generating over 190,000 views.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
