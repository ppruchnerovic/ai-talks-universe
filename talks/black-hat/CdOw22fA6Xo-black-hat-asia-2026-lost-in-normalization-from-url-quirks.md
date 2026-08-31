---
id: CdOw22fA6Xo
title: "Black Hat Asia 2026 | Lost in Normalization: From URL Quirks to Poisoning the Azure Supply Chain"
slug: black-hat-asia-2026-lost-in-normalization-from-url-quirks
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: null
duration_min: 28
published_at: 2026-08-16T19:00:15Z
video_id: CdOw22fA6Xo
youtube_url: https://www.youtube.com/watch?v=CdOw22fA6Xo
tags: []
transcript: false
---

# Black Hat Asia 2026 | Lost in Normalization: From URL Quirks to Poisoning the Azure Supply Chain

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=CdOw22fA6Xo) · [Conference site](https://www.blackhat.com/)

## Description

We transformed a single, isolated container in Azure Container Instances (ACI) for GPU into a full tenant-isolation breach and a critical supply chain attack. This talk details the multi-stage exploit chain that broke a seemingly secure, multi-layered design.

It all started with a misconfiguration that exposed a container image for a highly sensitive internal Kubernetes component, effectively handing us its source code. We will demonstrate how we chained two novel vulnerabilities, discovered in this internal code, with advanced Kubernetes techniques to achieve critical service compromise.

First, we achieved full cross-tenant credential theft, allowing us to steal secrets from other tenants' private container registries. More critically, we escalated this access to gain write permissions to a shared, production container registry used by ACI itself. This would have potentially allowed an attacker to poison trusted, official ACI images, creating a platform-wide supply chain attack.

Shortly after, following the disclosure of these critical vulnerabilities, the service was retired. This Briefing serves as a case study in how a single flaw can undermine a robust security design. Attendees will get a rare look into the internal security architecture of a major cloud service and learn to identify and defend against similar platform-wide vulnerabilities.

Nir Ohfeld  |  Head of Vulnerability Research, Wiz
Ronen Shustin  |  Security Researcher, Wiz
