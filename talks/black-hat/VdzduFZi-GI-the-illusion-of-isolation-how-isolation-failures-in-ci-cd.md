---
id: VdzduFZi-GI
title: "The Illusion of Isolation: How Isolation Failures in CI/CD Servers Lead to RCE and Privacy Risks"
slug: the-illusion-of-isolation-how-isolation-failures-in-ci-cd
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 36
published_at: 2025-09-03T16:12:56Z
video_id: VdzduFZi-GI
url: https://www.youtube.com/watch?v=VdzduFZi-GI
youtube_url: https://www.youtube.com/watch?v=VdzduFZi-GI
tags: []
topics: ["AI in the SDLC & engineering orgs", "Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: false
---

# The Illusion of Isolation: How Isolation Failures in CI/CD Servers Lead to RCE and Privacy Risks

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `36 min`

[Watch the recording](https://www.youtube.com/watch?v=VdzduFZi-GI) · [Conference site](https://www.blackhat.com/)

## Description

For many years, security research on CI/CD platforms has been a popular topic, but researchers often tend to look for flaws that are visibly present across various functionalities within the workflow rather than auditing CI/CD platform implementations to analyze application mechanisms and identify potential vulnerabilities.

In the complete CI/CD workflow, isolation mechanisms play a crucial role. For example, CI tasks typically need to be executed on the agent side, and the isolation between the agent and server ensures that users cannot execute code on the platform itself. Additionally, many functions within the CI/CD workflow also require isolation mechanisms, encompassing not only file system isolation but also isolation of user data. However, during our research on several CI/CD products, we were surprised to find that many CI/CD platforms did not prioritize implementing isolation in their functionality designs. When CI/CD servers fail to ensure proper isolation, it can lead to significant application security risks, including sensitive information leaks and even RCE vulnerabilities.

In this talk, we will share real world vulnerabilities discovered in well-known applications and outline several exploitation methodologies applicable to multiple applications. We conducted research on the implementation of isolation mechanisms, identifying four different attack techniques and discovering multiple RCE vulnerabilities in popular applications like Atlassian Bamboo, GoCD, etc. Additionally, we will analyze the workflows in these applications, discuss data isolation issues, and explore how these impact user and enterprise privacy.

By:
Tian Zhou  |  Security Researcher
Yiwen Wang  |  Security Researcher
Xiu Zhang  |  Security Engineer, Institute of Information Engineering, Chinese Academy of Sciences

Full Abstract and Presentation Materials:
