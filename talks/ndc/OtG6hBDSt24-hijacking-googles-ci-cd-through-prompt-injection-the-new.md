---
id: OtG6hBDSt24
title: "Hijacking Google’s CI/CD Through Prompt Injection:The New Era of AI-Based Exploits-Mackenzie Jackson"
slug: hijacking-googles-ci-cd-through-prompt-injection-the-new
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: []
channel: null
duration_min: 34
published_at: 2026-03-23T13:54:45Z
video_id: OtG6hBDSt24
youtube_url: https://www.youtube.com/watch?v=OtG6hBDSt24
tags: ["Application Security", "Architecture", "DevOps", "Supply Chain", "Testing", "CI/CD", "CI/CD Pipeline", "AI", "GitHub", "NDC", "Conferences", "2026", "Live", "Fun", "Oslo", "Norway", "Mackenzie Jackson"]
transcript: false
---

# Hijacking Google’s CI/CD Through Prompt Injection:The New Era of AI-Based Exploits-Mackenzie Jackson

**Speaker not identified**

`NDC Conferences` · `NDC` · `2026` · `34 min`

`#Application Security` `#Architecture` `#DevOps` `#Supply Chain` `#Testing` `#CI/CD` `#CI/CD Pipeline` `#AI` `#GitHub` `#NDC` `#Conferences` `#2026` `#Live` `#Fun` `#Oslo` `#Norway` `#Mackenzie Jackson`

[Watch the recording](https://www.youtube.com/watch?v=OtG6hBDSt24) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Security in Oslo, Norway. #ndcsecurity  #ndcconferences  #security  #developer   #softwaredeveloper

Attend the next NDC conference near you:

Follow our Social Media!

Prompt injection has long been treated as an amusing quirk of large language models, a curiosity demonstrated through simplistic examples like “ignore previous instructions.” Those surface-level attacks have been largely addressed, and with that, much of the security community moved on.

But the real risk was never about tricking chatbots.

As AI systems become embedded into CI/CD pipelines, build tooling, automation frameworks, and production infrastructure, prompt injection evolves from a toy problem into a true security vulnerability. When AI agents are granted access to privileged tools, shell commands, GitHub/GitLab tokens, issue editing, code generation, untrusted text becomes an execution vector.
Aikido Security recently uncovered a critical, widespread vulnerability pattern inside GitHub Actions workflows used by multiple Fortune 500 companies, including Google, where prompt injection enabled unauthorized command execution and credential exfiltration directly from their pipelines. These were not hypothetical weaknesses: the attacks were reproduced in controlled environments and confirmed by affected companies.

This talk examines why prompt injection becomes fundamentally dangerous when AI agents act inside trusted automation systems, and why solving it is far harder than filtering keywords or blocking certain phrases. We will draw parallels to SQL injection, another vulnerability once thought “solved”, and explore how we can protect ourselves against this new classification threat.
