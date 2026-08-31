---
id: qrHEBElig3c
title: "One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms"
slug: one-hack-to-rule-them-all-pervasive-account-takeovers-in
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 37
published_at: 2025-02-24T18:12:11Z
video_id: qrHEBElig3c
youtube_url: https://www.youtube.com/watch?v=qrHEBElig3c
tags: []
transcript: false
---

# One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=qrHEBElig3c) · [Conference site](https://www.blackhat.com/)

## Description

One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, & LLM Services

Integration Platforms for Workflow Automation (e.g., Microsoft Power Automate), Virtual Voice Assistants (e.g., Amazon Alexa), Smart Homes (e.g., Google Home), and Large Language Model (LLM) platforms supporting Plugins (e.g. OpenAI ChatGPT), are becoming essential in our personal and professional lives. However, we find many of these platforms vulnerable to a new class of authorization attacks.

As one of their core functions, integration platforms support "Account Linking" to connect end-users' accounts at third-party services/apps (e.g., Gmail, Dropbox) to their platform account. This enables the platform to utilize and orchestrate a wide range of external services on behalf of the end-user. For example, users can configure Microsoft Power Automate to automatically send an email whenever a new GitHub issue is filed. Multi-party authorizations are known to be error-prone and should have gone through strict security scrutiny. Yet, with our newly discovered attacks, we successfully exploit the account linking mechanisms of 24 out of 25 mainstream integration platforms, resulting in account takeovers or privacy leakage of integrated apps/services.

In this talk, we unveil how top-tier vendors improperly realize OAuth-based account linking under the new context of Integration Platforms. The failure to verify bindings with both the intended platform user and active third-party service/app compromises the session integrity of account linking. We detail the technical aspects of 3 attacks on integration platforms' authorization frameworks: two enable account takeovers, and one leads to forced account linking of arbitrary services/apps. Notably, most attacks have easy-to-satisfy preconditions and can often be reduced to 1-click attacks. For instance, an attacker can compromise victims' Microsoft 365 suite or Azure services with their single click on an unassuming link (a CVE with CVSS 9.6).

We also offer our comprehensive insights into best security practices and mitigations and highlight some vendors' invalid remedial attempts for each identified threat, benefiting the wider community.

By:
Kaixuan Luo  |  PhD Candidate, The Chinese University of Hong Kong
Xianbo Wang  |  PhD Candidate, The Chinese University of Hong Kong
Adonis Fung  |  Director of Security, Samsung Research America
Julien Lecomte  |  Senior Director of Engineering, Samsung Research America
Wing Cheong Lau  |  Professor, The Chinese University of Hong Kong

Full Abstract and Presentation Materials:
