---
id: -PdQtTn6mf8
title: "Attention Is All You Need for Semantics Detection: A Novel Transformer on Neural-Symbolic Approach"
slug: attention-is-all-you-need-for-semantics-detection-a-novel
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 37
published_at: 2025-01-22T18:21:42Z
video_id: -PdQtTn6mf8
url: https://www.youtube.com/watch?v=-PdQtTn6mf8
youtube_url: https://www.youtube.com/watch?v=-PdQtTn6mf8
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# Attention Is All You Need for Semantics Detection: A Novel Transformer on Neural-Symbolic Approach

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=-PdQtTn6mf8) · [Conference site](https://www.blackhat.com/)

## Description

To identify a few unique binaries even worth the effort for human experts to analyze from large-scale samples, filter techniques for excluding those highly duplicated program files are essential to reduce the human cost within a restricted period of incident response, such as auto-sandbox emulation or AI detection engine. As VirusTotal reported in 2021 ~90% of 1.5 billion samples are duplicated but still require malware experts to verify due to obfuscation.

In this work, we proposed a novel neural-network-based symbolic execution LLM, CuIDA, to simulate the analysis strategies of human experts, such as taint analysis of the Use-define chain among unknown API calls. Our method can automatically capture the contextual comprehension of API and successfully uncover those obfuscated behaviors in the most challenging detection dilemma including (a.) dynamic API solver, (b.) shellcode behavior inference, and (c.) commercial packers detection
WITHOUT unpacking.

We demonstrate the practicality of this approach on large-scale sanitized binaries which are flagged as obfuscated but few positives on VirusTotal. We surprisingly uncovered up to 67% of binaries that were missed by most vendors in our experiment, by the factor of those threats successfully abuse the flaw of VC.Net detection to evade the scan. Also, this approach shows the inference intelligence on behavior prediction for shellcode without simulation, instead, only by using the data-relationships on
the stack to infer the relative unique behaviors involved in the payload.

Moreover, to explore the limitation of our transformer's contextual comprehension on the obfuscation problem, we evaluate the transformer with state-of-the-art commercial packers, VMProtect and Themida. Our approach successfully forensics-based investigates the original behaviors of the running protected program without unpacking. Furthermore, this approach reveals a few unexpected findings of the protection strategies of the commercial packers themselves. In conclusion, our method explores the possibility of using LLM to sample the reversing experience, analysis strategies of human experts, and success in building robust AI agents on practical obfuscated code understanding.

By:
Sheng-Hao Ma  |  Team Lead, PSIRT and Threat Research, TXOne Networks Inc.
Yi-An Lin  |  Threat Researcher, PSIRT and Threat Research, TXOne Networks Inc.
Mars Cheng  |  Threat Research Manager, PSIRT and Threat Research, TXOne Networks Inc.

Full Abstract and Presentation Materials:
