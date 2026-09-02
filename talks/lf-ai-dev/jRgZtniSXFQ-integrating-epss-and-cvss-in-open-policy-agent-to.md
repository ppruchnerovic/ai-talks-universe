---
id: jRgZtniSXFQ
title: "Integrating EPSS and CVSS in Open Policy Agent To Quarantine Real-world Vulnerabili... Nigel Douglas"
slug: integrating-epss-and-cvss-in-open-policy-agent-to
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: []
channel: "The Linux Foundation"
duration_min: 41
published_at: 2025-09-05T19:39:27Z
video_id: jRgZtniSXFQ
url: https://www.youtube.com/watch?v=jRgZtniSXFQ
youtube_url: https://www.youtube.com/watch?v=jRgZtniSXFQ
tags: []
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: false
---

# Integrating EPSS and CVSS in Open Policy Agent To Quarantine Real-world Vulnerabili... Nigel Douglas

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `41 min`

[Watch the recording](https://www.youtube.com/watch?v=jRgZtniSXFQ) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Integrating EPSS and CVSS in Open Policy Agent To Quarantine Real-world Vulnerabilities - Nigel Douglas, Cloudsmith

CVSS (Common Vulnerability Scoring System) and EPSS (Exploit Prediction Scoring System) are both valuable tools for vulnerability management, but they serve different purposes. CVSS assesses the inherent severity of a vulnerability, whereas EPSS estimates the likelihood of that vulnerability being exploited in the wild. At Cloudsmith, we integrate open source projects like EPSS and the Trivy scanner for CVSS analysis into Open Policy Agent (OPA) to strengthen supply chain enforcement.

In this session, we’ll examine four recent CVEs that highlight the contrast between these two approaches—cases where vulnerabilities score highly under CVSS but have a low EPSS probability, and others with high EPSS scores (indicating strong exploit potential) that had not yet been published in the NIST CVE database at the time of artifact scanning. These examples underscore the importance of leveraging both CVSS and EPSS in a comprehensive vulnerability management strategy.

We’ll also explore how open-source tools like OPA can be used to enforce these security controls effectively within the software supply chain.
