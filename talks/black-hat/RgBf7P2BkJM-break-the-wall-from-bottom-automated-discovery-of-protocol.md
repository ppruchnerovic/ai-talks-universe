---
id: RgBf7P2BkJM
title: "Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities"
slug: break-the-wall-from-bottom-automated-discovery-of-protocol
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 27
published_at: 2025-01-24T18:18:02Z
video_id: RgBf7P2BkJM
youtube_url: https://www.youtube.com/watch?v=RgBf7P2BkJM
tags: []
transcript: false
---

# Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=RgBf7P2BkJM) · [Conference site](https://www.blackhat.com/)

## Description

Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls

Web Application Firewalls (WAFs) are a crucial line of defense against web-based attacks. However, an emerging threat comes from protocol-level evasion vulnerabilities, in which adversaries exploit parsing discrepancies between the WAF HTTP parser and those of web applications to circumvent WAFs. Currently, uncovering these vulnerabilities still depends on manual, ad hoc methods.

In this talk, we propose WAF Manis, a novel testing framework to automatically discover protocol-level evasion vulnerabilities in WAFs. We evaluated WAF Manis against 14 popular WAFs including Cloudflare and ModSecurity and 20 popular web frameworks including Laravel and Spring. In total, we discovered 311 protocol-level evasion cases affecting all tested WAFs and applications. Due to the generic nature of protocol-level evasions, these evasion vulnerabilities do not hinge on specific payload patterns and can transmit any malicious payloads - for instance, SQL injection, XSS, or Log4jShell - to the target websites.

We further analyzed these vulnerabilities and identified three primary reasons contributing to WAF evasions. We have reported those identified vulnerabilities to the affected providers and received acknowledgments and bug bounty rewards from Cloudflare WAF, Fortinet WAF, Alibaba Cloud WAF, Huawei Cloud WAF, ModSecurity, Go security Team, and the PHP security team.

By:
Qi Wang  |  P.h.D Student, Tsinghua University
Jianjun Chen  |  Assistant Professor, Tsinghua University and Zhongguancun Laboratory
Run Guo  |  Ph.D. Candidate, Tsinghua University
Chao Zhang  |  Tenured Associate Professor, Tsinghua University and Zhongguancun Laboratory
Haixin Duan  |  Professor, Tsinghua University; Zhongguancun Laboratory; QI-ANXIN Technology Research Institute

Full Abstract and Presentation Materials:
