---
id: 9gvxEhugnVM
title: "Gotta Cache Em All: Bending the Rules of Web Cache Exploitation"
slug: gotta-cache-em-all-bending-the-rules-of-web-cache
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 36
published_at: 2025-02-07T18:38:20Z
video_id: 9gvxEhugnVM
url: https://www.youtube.com/watch?v=9gvxEhugnVM
youtube_url: https://www.youtube.com/watch?v=9gvxEhugnVM
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# Gotta Cache Em All: Bending the Rules of Web Cache Exploitation

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `36 min`

[Watch the recording](https://www.youtube.com/watch?v=9gvxEhugnVM) · [Conference site](https://www.blackhat.com/)

## Description

In recent years, web cache attacks have become a popular way to steal sensitive data, deface websites, and deliver exploits. We've also seen parser inconsistencies causing critical vulnerabilities like SSRF and HTTP Request Smuggling. This raises the question: what happens if we target web caches' URL-parsers?

In this session, I'll introduce two powerful new techniques that exploit RFC ambiguities to bypass the limitations of web cache deception and poisoning attacks and inflict some serious damage.

First, I'll introduce Static Path Deception, a novel technique to completely compromise the confidentiality of an application. I'll illustrate this with a case study showing how such a breach can be replicated in environments like Nginx behind Cloudflare and Apache behind CloudFront, using just their default configurations.

Next, I'll present Cache Key Confusion, and show how to exploit URL parsing inconsistencies in major platforms, including Microsoft Azure Cloud. I'll then show how to achieve arbitrary cache poisoning and full denial of service in OpenAI and countless platforms.

Finally, I'll reveal how to supercharge these vulnerabilities with a live demo that blends Cache Key Confusion with a "non-exploitable" open redirect. By modifying the response of a static javascript file, I'll show how to execute arbitrary JS code cross-domain.

Attendees will depart armed with a set of innovative techniques for uncovering concealed bugs, along with a definitive methodology to find and exploit these and other URL or HTTP discrepancies. To facilitate this, I'll provide an open-source tool to detect all discussed vulnerabilities, plus a lab to level-up your cache exploitation skills!

By:
Martin Doyhenard  |  Security Researcher, PortSwigger

Full Abstract and Presentation Materials Available:
