---
id: __NtTfL0oPw
title: "Back to the Future: Hacking and Securing Connection-based OAuth Architectures"
slug: back-to-the-future-hacking-and-securing-connection-based
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-12-19T19:03:42Z
video_id: __NtTfL0oPw
url: https://www.youtube.com/watch?v=__NtTfL0oPw
youtube_url: https://www.youtube.com/watch?v=__NtTfL0oPw
tags: []
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: false
---

# Back to the Future: Hacking and Securing Connection-based OAuth Architectures

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=__NtTfL0oPw) · [Conference site](https://www.blackhat.com/)

## Description

Back to the Future: Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms

Access delegation is indispensable for Agentic AI and Integration Platforms, where orchestration engines (e.g., Microsoft Power Automate, Copilot Studio) obtain access tokens from 3rd-party providers to act on behalf of end-users or authenticate end-users across chat channels. To better support these new use cases, there is a growing trend to offload token retrieval and lifecycle management to a separate cloud-based service (a.k.a. Credential Manager, Token Store), which enables developers to streamline "access re-delegation" when building AI agents and low-code solutions. Different home-grown variants of OAuth have emerged to support such access re-delegation architecture.

Unlike the traditional OAuth setup, re-delegation centralizes token handling via a dedicated OAuth Token Service (a.k.a. OAuth-as-a-Service), which introduces an abstract "OAuth connection". This connection provides an application a pre-configured handle for a managed OAuth token, outsourcing token negotiations with the OAuth Authorization Server to the Token Service. Unlike "Broker" architectures that chain together two OAuth flows (authorization server-broker and broker-application), under the new connection-based OAuth architecture, applications acquire and utilize tokens through proprietary "OAuth connections" instead.

We have found that such a proprietary approach often reintroduces critical new vulnerabilities previously mitigated by OAuth standards. In this talk, we explain how classic web vulnerabilities like Session Fixation, Open Redirect, Confused Deputy, XSS, and Cross-window Communication attacks have re-manifested themselves or been amplified within these proprietary, yet increasingly-common, connection-based OAuth architectures. Through practical exploits of these vulnerabilities, attackers can take over well-authenticated AI agents or gain unauthorized access to arbitrary integrations, all without explicit user consent.

Using Microsoft as a case study, we illustrate how connection-based OAuth architectures are adopted in Azure, Power Platform, and Copilot Studio. We systematize the attack surface and highlight how Microsoft's case reflects the good, the bad and the ugly across the industry, revealing systemic issues shared by other vendors such as Composio and ByteDance Coze.

Attendees will walk away with an attacker's mindset and actionable best practices in building a hardened auth layer for AI agents and integrations.

By:
Kaixuan Luo  |  PhD Candidate, The Chinese University of Hong Kong
Xianbo Wang  |  PhD Candidate, The Chinese University of Hong Kong
Adonis Fung  |  Director of Engineering, Security, Samsung Research America
Yanxiang Bi  |  PhD Candidate, The Chinese University of Hong Kong
Wing Cheong Lau  |  Professor, The Chinese University of Hong Kong

Presentation Materials Available at:
