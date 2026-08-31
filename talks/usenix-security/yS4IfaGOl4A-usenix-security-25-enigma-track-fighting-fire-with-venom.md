---
id: yS4IfaGOl4A
title: "USENIX Security '25 (Enigma Track) - Fighting Fire with Venom: Adversarial Defense Against..."
slug: usenix-security-25-enigma-track-fighting-fire-with-venom
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 23
published_at: 2025-10-16T21:25:02Z
video_id: yS4IfaGOl4A
youtube_url: https://www.youtube.com/watch?v=yS4IfaGOl4A
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 (Enigma Track) - Fighting Fire with Venom: Adversarial Defense Against...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `23 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=yS4IfaGOl4A) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Fighting Fire with Venom: Adversarial Defense Against Unauthorized Web Crawling

Nick Sullivan

As companies developing large language models (LLMs) race to gather fresh data from the open web, their crawling operations grow increasingly aggressive. While the Robots Exclusion Standard (robots.txt) was meant to provide guidelines for responsible crawling, many entities either ignore it or interpret it loosely in pursuit of large-scale data. This talk explores a novel way to push back by actively serving different or misleading content to identified crawlers.
We will introduce Venom, an experimental toolkit that combines advanced fingerprinting and inline proxy techniques to dynamically alter served content based on the specific crawler detected. Venom evaluates multiple signals—request headers, behavior patterns, and known crawler infrastructure—before deciding how to respond. The talk will cover the practical challenges of implementing this defense, the legal and ethical dilemmas involved, and how well it works against both text-based and image-based crawling strategies.
Drawing on case studies covering text and image scraping, this presentation includes a validation study demonstrating how LLMs trained on intentionally "poisoned" content experience degraded performance, ultimately making large-scale crawling a net negative for data harvesters. Rather than relying on traditional blocking (which remains neutral to a crawler's value proposition) or CAPTCHA/puzzle approaches, this adversarial strategy focuses on reshaping the cost-benefit equation so that unscrupulous collection efforts yield poor results.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
