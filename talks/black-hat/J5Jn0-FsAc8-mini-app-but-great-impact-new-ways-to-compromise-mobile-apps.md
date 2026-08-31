---
id: J5Jn0-FsAc8
title: "Mini-App But Great Impact: New Ways to Compromise Mobile Apps"
slug: mini-app-but-great-impact-new-ways-to-compromise-mobile-apps
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 23
published_at: 2025-09-08T16:51:26Z
video_id: J5Jn0-FsAc8
youtube_url: https://www.youtube.com/watch?v=J5Jn0-FsAc8
tags: []
transcript: false
---

# Mini-App But Great Impact: New Ways to Compromise Mobile Apps

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=J5Jn0-FsAc8) · [Conference site](https://www.blackhat.com/)

## Description

In the mobile app ecosystem, super-apps serve as platforms hosting mini-apps, facilitating cross-platform operation across Android and iOS. Traditionally, attacks on mobile apps have targeted native applications, web pages, and networks. Our research pioneers a novel exploitation vector targeting mobile apps via mini-apps.

For security considerations, capabilities open to Mini-Apps need to be strictly restricted and implemented in the sandbox. After comprehensive research on 11 popular super-apps involving hundreds of APIs, we found the sandbox environment can not provide isolation as expected. Attackers can exploit different methods for sandbox escaping and privilege escalation such as attacks against storage and network capabilities, which lead to remote code execution (RCE) and account hijacking.

Additionally, we have adapted JavaScript prototype pollution for the mini-apps framework. This adaptation allows attackers to tamper with the mini-app environment logic, enabling malicious apps to invoke privileged APIs, inject parameters, and access sensitive data. This is the first instance of deploying this attack in mobile apps, with implications more severe than those in web security.

The significant risks we identified impacted 9 different super-apps with over 10 billion downloads. (All of the risks have already been reported and repaired.) Through our presentation, we want to expose a new remote attack surface for mobile apps, and improve the security of super-apps to better protect billions of user privacy.

By:
Wei Wen  |  Security Engineer, IES Red Team of ByteDance
Xiangyu Cao  |  Security Researcher, IES Red Team of ByteDance
Jiangchunxi Hou  |  Security Researcher, IES Red Team of ByteDance
Zixi Liao  |  Security Researcher, IES Red Team of ByteDance
Yingyan Song  |  Security Engineer, IES Red Team of ByteDance
Zhongcheng Li  |  Security Researcher, IES Red Team of ByteDance
Yijie Zhao  |  Security Researcher, IES Red Team of ByteDance
Bin Ma  |  Security Researcher, IES Red Team of ByteDance

Full Abstract and Presentation Materials:
