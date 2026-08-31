---
id: cjQIvLHUEws
title: "Using Deep Learning Attribution Methods for Fault Injection Attacks"
slug: using-deep-learning-attribution-methods-for-fault-injection
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-09-26T16:29:34Z
video_id: cjQIvLHUEws
youtube_url: https://www.youtube.com/watch?v=cjQIvLHUEws
tags: []
transcript: false
---

# Using Deep Learning Attribution Methods for Fault Injection Attacks

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=cjQIvLHUEws) · [Conference site](https://www.blackhat.com/)

## Description

I Have Got to Warn You, It Is a Learning Robot: Using Deep Learning Attribution Methods for Fault Injection Attacks

Deep Learning (DL) has recently received significant attention in breaking cryptographic implementations on embedded systems. However, research on the subject mostly focused on side-channel attacks (SCAs).

In this talk, we present for the first time the use of DL attribution methods used for image processing as a reverse engineering tool for fault injection (FI). We present a practical example in the case of attacking a secure EEPROM (Analog Devices DeepCover DS28C36) in black box approach.

We collect power consumption traces from the chip while the read memory command is executed. This acquisition is performed when the EEPROM is protected and unprotected. Then, we deliver the power consumption traces to a DL model to learn the difference between them. After that, we use deep learning attribution methods such as gradient or layer-wise relevance propagation (LRP) to reverse the deep learning model decision. This step guides the attacker about the manipulation timings of the security fuses of the EEPROM. By using this knowledge, we conclude that the chip performs a double checking as a countermeasure against single fault injection attacks. Finally, we perform a double laser fault injection which bypasses the two security checks, and therefore we can extract the protected EEPROM user secrets.

By:
Karim Abdellatif  |  Hardware Security Expert, Ledger-Donjon

Full Abstract and Presentation Materials Available:
