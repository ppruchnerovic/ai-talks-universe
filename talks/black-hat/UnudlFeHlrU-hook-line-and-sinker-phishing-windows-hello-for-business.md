---
id: UnudlFeHlrU
title: "Hook, Line and Sinker: Phishing Windows Hello for Business"
slug: hook-line-and-sinker-phishing-windows-hello-for-business
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 25
published_at: 2025-02-10T18:30:16Z
video_id: UnudlFeHlrU
url: https://www.youtube.com/watch?v=UnudlFeHlrU
youtube_url: https://www.youtube.com/watch?v=UnudlFeHlrU
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# Hook, Line and Sinker: Phishing Windows Hello for Business

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=UnudlFeHlrU) · [Conference site](https://www.blackhat.com/)

## Description

In my presentation, I will share a method to phish the phishing-resistant authentication mechanism, Windows Hello for Business (WHfB). Despite WHfB's design to provide secure authentication through cryptographic keys, my research uncovers a method that allows attackers to downgrade this secure method to a more vulnerable, phishable one.

My research reveals how attackers can intercept and modify POST requests to Microsoft's authentication services and manipulate the system into defaulting to a less secure authentication method. This is achieved by altering parameters such as User-Agent or isFidoSupported in the authentication request.

I will detail the exploitation process, showing how I have modified the EvilGinx framework to automate the attack, making it scalable. Furthermore, I will discuss mitigation strategies, specifically focusing on the implementation of conditional access policies that leverage authentication strength — a feature introduced after reporting the issue to Microsoft, designed to enforce the use of phishing-resistant methods.

This presentation aims to shed light on this flaw, to provide a deeper understanding of Windows Hello for Business and to encourage the adoption of enhanced security measures.

By:
Yehuda Smirnov  |  Red Team & Security Researcher, Accenture

Full Abstract and Presentation Materials Available:
