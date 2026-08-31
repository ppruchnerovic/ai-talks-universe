---
id: lQgjBvrWh84
title: "ToolShell, Patch Bypass, and the AI That Might Have Seen It Coming - Pedram Hayati & Soroush Dalili"
slug: toolshell-patch-bypass-and-the-ai-that-might-have-seen-it
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: []
channel: "NDC Conferences"
duration_min: 47
published_at: 2026-01-29T14:03:29Z
video_id: lQgjBvrWh84
youtube_url: https://www.youtube.com/watch?v=lQgjBvrWh84
tags: ["AI/ML", "Application Security", "Bug Bounties", "Design", "Fun", "Security", "Tooling", "Testing", "AI", "ML", "Machinelearning", "NDC", "Conferences", "2025", "Live", "Manchester", "England", "UK", "United Kingdom", "Pedram Hayati", "Soroush Dalili"]
transcript: false
---

# ToolShell, Patch Bypass, and the AI That Might Have Seen It Coming - Pedram Hayati & Soroush Dalili

**Speaker not identified**

`NDC Conferences` · `NDC` · `2026` · `47 min`

`#AI/ML` `#Application Security` `#Bug Bounties` `#Design` `#Fun` `#Security` `#Tooling` `#Testing` `#AI` `#ML` `#Machinelearning` `#NDC` `#Conferences` `#2025` `#Live` `#Manchester` `#England` `#UK` `#United Kingdom` `#Pedram Hayati` `#Soroush Dalili`

[Watch the recording](https://www.youtube.com/watch?v=lQgjBvrWh84) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Manchester in Manchester, England.

Attend the next NDC conference near you:

/          @NDC

Follow our Social Media!

In mid-May 2025, during the ZDI’s Pwn2Own contest in Berlin, a researcher chained together two SharePoint vulnerabilities, later called “ToolShell” (CVE-2025-49704 and CVE-2025-49706), to achieve remote code execution on a SharePoint server. Following Microsoft’s patch on 8 July 2025, threat actors began reverse engineering the fix to target unpatched systems. Shortly after this, Microsoft also acknowledged the initial patch was incomplete, and the media announced the exploitation of the bypasses without having any evidence. A follow-up emergency patch was issued over a weekend to resolve the issue. Meanwhile, there was a lot of debate about whether the exploit had been leaked and used before anyone knew about it.

This technical session walks through the full incident, what was exploited, what failed, and how. We will examine the vulnerable code paths and explain how the authentication mechanism was bypassed. We will also look at why the first patch was ineffective.

Taking a historical lens, we will trace the issue back through earlier SharePoint versions including 2010 to understand how it may have originated. A live demo will then explore how AI tools could have assisted in patch diffing and dynamic analysis to identify the exploit code after the initial patch, and whether AI could have flagged the bypass when given the new code changes along with public research and exploit data.

Finally, we will discuss the official workarounds that were recommended, how they could be circumvented particularly in the context of ASP.NET and IIS, and offer practical suggestions for building more resilient mitigations against similar attacks in the future.

The audience will take a way with the followings:
• Understand how the ToolShell (CVE-2025-49704/49706) SharePoint vulnerability chain and its bypass worked.
• See how the attack unfolded and how to craft detection signatures based on its behaviour.
• Discover how AI tools can assist in patch diffing and exploit detection.
• Gain practical strategies for defending against similar future threats in ASP.NET and IIS environments.
