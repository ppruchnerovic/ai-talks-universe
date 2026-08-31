---
id: nZWpDeY9p6g
title: "The GCP Jenga Tower: Hacking Millions of Google's Servers With a Single Package (and more)"
slug: the-gcp-jenga-tower-hacking-millions-of-google-s-servers
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 33
published_at: 2025-03-10T17:17:16Z
video_id: nZWpDeY9p6g
youtube_url: https://www.youtube.com/watch?v=nZWpDeY9p6g
tags: []
transcript: false
---

# The GCP Jenga Tower: Hacking Millions of Google's Servers With a Single Package (and more)

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=nZWpDeY9p6g) · [Conference site](https://www.blackhat.com/)

## Description

Cloud security is so complex that even cloud providers get it wrong sometimes - one simple faulty command argument by Google Cloud Platform (GCP) was enough to enable us to find a critical RCE vulnerability (dubbed 'CloudImposer') in GCP customers' workloads and Google's internal production servers, affecting millions of cloud servers. To further emphasize the point of complexity, I will also reveal a privilege escalation vulnerability we discovered in GCP that stemmed from the deployment of services with dangerous defaults by GCP themselves.

I will start the talk by sharing the thrilling process of discovering the CloudImposer vulnerability, including getting hundreds of DNS requests from internal Google servers, until a PyPI guardrail stopped us.

However, this talk is about more than just a vulnerability. This investigation led to some unique research insights about cloud services:
1. Supply chain vulnerabilities in the cloud are on steroids. Instead of one malicious package affecting one server, one malicious package affects a service that is deployed to millions.
2. Cloud providers build their services like Jenga towers. They use their core services as the foundation of more popular customer-facing offerings. For example, one click to create a Cloud Function service creates resources in six different services. This exposes customers to a larger attack surface and risks.

The next part of the talk will dive deep into the vulnerable GCP Cloud Functions deployment flow. I will showcase the vulnerability I found in this flow and present a simple tool we built, newly available to the community, to find the hidden APIs that are called by the cloud provider when performing an action.

By the end of this talk, the audience will learn the dangers of treating cloud services like a black box - and get the right tools and ideas for looking inside it.

By:
Liv Matan  |  Senior Security Researcher, Tenable

Full Abstract Available:
