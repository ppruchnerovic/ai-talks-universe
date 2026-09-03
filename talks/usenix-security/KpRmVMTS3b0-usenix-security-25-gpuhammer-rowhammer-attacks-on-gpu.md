---
id: KpRmVMTS3b0
title: "USENIX Security '25 - GPUHammer: Rowhammer Attacks on GPU Memories are Practical"
slug: usenix-security-25-gpuhammer-rowhammer-attacks-on-gpu
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 14
published_at: 2025-11-03T18:50:28Z
video_id: KpRmVMTS3b0
url: https://www.youtube.com/watch?v=KpRmVMTS3b0
youtube_url: https://www.youtube.com/watch?v=KpRmVMTS3b0
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - GPUHammer: Rowhammer Attacks on GPU Memories are Practical

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `14 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=KpRmVMTS3b0) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

GPUHammer: Rowhammer Attacks on GPU Memories are Practical

Chris S. Lin, Joyce Qu, and Gururaj Saileshwar, University of Toronto

Rowhammer is a read disturbance vulnerability in modern DRAM that causes bit-flips, compromising security and reliability. While extensively studied on Intel and AMD CPUs with DDR and LPDDR memories, its impact on GPUs using GDDR memories, critical for emerging machine learning applications, remains unexplored. Rowhammer attacks on GPUs face unique challenges: (1) proprietary mapping of physical memory to GDDR banks and rows, (2) high memory latency and faster refresh rates that hinder effective hammering, and (3) proprietary mitigations in GDDR memories, difficult to reverse-engineer without FPGA-based test platforms.

We introduce GPUHammer, the first Rowhammer attack on NVIDIA GPUs with GDDR6 DRAM. GPUHammer proposes novel techniques to reverse-engineer GDDR DRAM row mappings, and employs GPU-specific memory access optimizations to amplify hammering intensity and bypass mitigations. Thus, we demonstrate the first successful Rowhammer attack on a discrete GPU, injecting up to 8 bit-flips across 4 DRAM banks on an NVIDIA A6000 with GDDR6 memory. We also show how an attacker can use these to tamper with ML models, causing significant accuracy drops (up to 80%).

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
