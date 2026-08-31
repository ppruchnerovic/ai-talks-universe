---
id: MoDYOm2fPJ0
title: "Utilizing AI Models to Conceal and Extract Commands in C2 Images"
slug: utilizing-ai-models-to-conceal-and-extract-commands-in-c2
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 21
published_at: 2025-09-16T16:58:25Z
video_id: MoDYOm2fPJ0
youtube_url: https://www.youtube.com/watch?v=MoDYOm2fPJ0
tags: []
transcript: false
---

# Utilizing AI Models to Conceal and Extract Commands in C2 Images

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `21 min`

[Watch the recording](https://www.youtube.com/watch?v=MoDYOm2fPJ0) · [Conference site](https://www.blackhat.com/)

## Description

AI-Powered Image-Based Command and Control (C2) Framework: Utilizing AI Models to Conceal and Extract Commands in C2 Images

Generative AI concentrates on generating novel and unique content in various forms, including text, image, and video. Many researchers focus on utilizing GenAI models to improve our lives or identifying vulnerabilities in GenAI models. In this talk, we investigate the potential application of GenAI for malicious purposes. Specifically, we aim to explore the feasibility of training a model to serve Command and Control (C2) attacks.

Many C2 attacks have started to rely on the steganography techniques to hide their C2 secrets in images. Even if the firewall enables the decryption feature, it is still hard for security researchers to identify C2 secrets in images within decrypted network payloads. However, it is possible to detect existing C2 implants by identifying the decoding logic in the code. Most steganography techniques used by attackers are rule-based to embed the payload in the least significant bytes of an existing image. The decoding logic is also hard coded in the implant to retrieve C2 secrets. It could be easy to detect the decoding logic in the code using antivirus software via code analysis.

In this talk, we would like to adapt existing ML based steganography techniques for C2 attacks. More specifically, we propose an AI-enhanced C2 framework. It will employ AI models to generate visually indistinguishable encoded images with C2 secrets, and a decoder model which can recover the original C2 secrets from images. The decoding logic is no longer hard coded but a legitimate ML model. This makes the detection more challenging for traditional anti-virus techniques. The decoder model can be retrained to change its hash value to evade signature based detections. We investigate the feasibility of utilizing AI models to generate and decode C2 images, and also show the effectiveness of our framework with a live demo.

By:
Qian Feng  |  Security Researcher, Palo Alto Networks
Chris Navarrete  |  Principal Security Researcher, Palo Alto Networks

Full Abstract and Presentation Materials:
