---
id: x4PcmQKS0Ao
title: "BG - From keyless to careless: Abusing misconfigured OIDC authentication in cloud environments"
slug: bg-from-keyless-to-careless-abusing-misconfigured-oidc
conference: bsides-lv
conference_name: "BSides Las Vegas"
category: "Security conferences"
edition: "BSides Las Vegas"
year: 2024
speakers: []
channel: null
duration_min: 17
published_at: 2024-09-04T22:15:21Z
video_id: x4PcmQKS0Ao
url: https://www.youtube.com/watch?v=x4PcmQKS0Ao
youtube_url: https://www.youtube.com/watch?v=x4PcmQKS0Ao
tags: ["YEZFQC"]
topics: []
transcript: false
---

# BG - From keyless to careless: Abusing misconfigured OIDC authentication in cloud environments

**Speaker not identified**

`BSides Las Vegas` · `BSides Las Vegas` · `2024` · `17 min`

`#YEZFQC`

[Watch the recording](https://www.youtube.com/watch?v=x4PcmQKS0Ao) · [Conference site](https://bsideslv.org/)

## Description

Breaking Ground, Wed, Aug 7, 20:00 - Wed, Aug 7, 20:20 CDT

In cloud environments, static and long-lived credentials are highly discouraged as they often get leaked and are the cause for most publicly known cloud data breaches. To solve this problem, cloud providers such as AWS, Azure and Google Cloud support "keyless authentication" through OpenID Connect (OIDC), allowing you to exchange JSON Web Tokens (JWTs) signed by trusted identity providers for cloud credentials. Keyless authentication is especially popular for CI/CD, and enables pipelines to seamlessly authenticate to a cloud environment.

Keyless authentication is easy to configure—and unfortunately, to misconfigure. In this talk, we demonstrate that AWS IAM roles using keyless authentication are, in many cases, insecurely configured and allow unauthenticated attackers to retrieve cloud credentials and further compromise the environment. We share our research where we have identified dozens of vulnerable roles in the wild; in particular, we were able to compromise AWS credentials of an account belonging to the UK government, and pivot from there to an internal code repository. Finally, we showcase not only how to identify vulnerable roles in your environment, but also how to use higher-level guardrails to ensure that a human mistake doesn't turn into a data breach.

People
Christophe Tafani-Dereeper
