---
id: sKH8283CFzs
title: "WorstFit: Unveiling Hidden Transformers in Windows ANSI!"
slug: worstfit-unveiling-hidden-transformers-in-windows-ansi
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-05-19T19:23:16Z
video_id: sKH8283CFzs
youtube_url: https://www.youtube.com/watch?v=sKH8283CFzs
tags: []
transcript: false
---

# WorstFit: Unveiling Hidden Transformers in Windows ANSI!

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=sKH8283CFzs) · [Conference site](https://www.blackhat.com/)

## Description

*It was the best of fit, it was the worst of fit, it was the age of wisdom, it was the age of foolishness.*

As we know, certain codepages have limitations and cannot support all Unicode Codepoints. So, why not just convert unsupported characters to the closest one? This is the essence of the "Best Fit" feature in Windows — a seemingly clever long-existing solution to character conversion issues.

However, it is a double-edged sword.

This system-wide behavior, often neglected by developers, has remained lurked in the deep-seated design flaws in Windows C/C++ Runtime and APIs for decades. It constitutes a critical risk to the Windows ecosystem, giving rise to numerous vulnerabilities across various applications.

This presentation unveils a novel attack vector that exploits the "Best Fit" behavior to bypass security mechanism, remount argument injection, and, in certain scenarios, achieve arbitrary code execution. We have identified vulnerabilities across several applications and open-source projects, including Microsoft Office, cURL, PHP, Subversion, and multiple built-in executables in the Windows operating system.

Moreover, we demonstrate how this attack vector can be exploited to achieve remote code execution (RCE) in PHP, Microsoft Office, and other applications that indirectly use vulnerable command line tools, such as pip, composer and git.

Throughout this session, we delve into shedding light on the overlooked aspect of this behavior in Windows and a new attack surface that can be exploited by attackers. Furthermore we will also discuss optimal practices in coding and design to effectively mitigate them.

By:
Orange Tsai  |  Principal Security Researcher, DEVCORE
Splitline Huang  |  Security Researcher, DEVCORE

Full Abstract and Presentation Materials:
