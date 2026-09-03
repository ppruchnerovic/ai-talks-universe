---
id: U-bK-WFJk_c
title: "BG - My Terrible Roommates (see description for full title)"
slug: bg-my-terrible-roommates-see-description-for-full-title
conference: bsides-lv
conference_name: "BSides Las Vegas"
category: "Security conferences"
edition: "BSides Las Vegas"
year: 2024
speakers: ["My Terrible Roommates"]
channel: null
duration_min: 17
published_at: 2024-09-04T22:15:16Z
video_id: U-bK-WFJk_c
url: https://www.youtube.com/watch?v=U-bK-WFJk_c
youtube_url: https://www.youtube.com/watch?v=U-bK-WFJk_c
tags: ["RV7BRK"]
topics: ["Security, safety & red teaming"]
transcript: false
---

# BG - My Terrible Roommates (see description for full title)

**My Terrible Roommates**

`BSides Las Vegas` · `BSides Las Vegas` · `2024` · `17 min`

`#RV7BRK`

[Watch the recording](https://www.youtube.com/watch?v=U-bK-WFJk_c) · [Conference site](https://bsideslv.org/)

## Description

My Terrible Roommates: Discovering the FlowFixation Vulnerability & the Risks of Sharing a Cloud Domain

Breaking Ground, Tue, Aug 6, 17:00 - Tue, Aug 6, 17:20 CDT

Could providers have prevented some of the more impactful web vulnerabilities revealed to date. Will they be able to prevent those yet to come? Is there a “secret” guardrail that those who report bugs and triage vulnerabilities simply don’t know of, but should?

At this session, I will unveil a high-severity vulnerability I discovered and dubbed 'FlowFixation'.

The talk will first explore a common cloud provider default configuration that can be likened to a javascript execution primitive on a victim's subdomain in on-prem environments. The root issue: you share parent domains with every other cloud customer.

I will then introduce a lesser-known guardrail for preventing this risk: The public suffix list (PSL). Audiences will learn about my unique domain management research into the major cloud providers and better understand the services’ domains that were vulnerable to same-site attacks. I will also share case studies of significant cloud vulnerabilities that could have been prevented with this guardrail.

The next part of the talk will dive deep into the FlowFixation vulnerability, that affected AWS Managed Workflows for Apache Airflow (MWAA), enabling attackers to hijack a user session and potentially execute remote code (RCE) on underlying instances.

People
Liv Matan
