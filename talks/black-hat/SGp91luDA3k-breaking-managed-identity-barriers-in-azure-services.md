---
id: SGp91luDA3k
title: "Breaking Managed Identity Barriers In Azure Services"
slug: breaking-managed-identity-barriers-in-azure-services
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2024
speakers: []
channel: null
duration_min: 44
published_at: 2024-08-22T16:49:21Z
video_id: SGp91luDA3k
url: https://www.youtube.com/watch?v=SGp91luDA3k
youtube_url: https://www.youtube.com/watch?v=SGp91luDA3k
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# Breaking Managed Identity Barriers In Azure Services

**Speaker not identified**

`Black Hat` · `Black Hat` · `2024` · `44 min`

[Watch the recording](https://www.youtube.com/watch?v=SGp91luDA3k) · [Conference site](https://www.blackhat.com/)

## Description

Identity management and authentication mechanisms together with authorization policies play a crucial role in systems security, especially when it comes to complex interdependent systems such as cloud services. One such service in Azure is Managed Identities. Managed Identities provide a universal interface for helping users to avoid storing credentials in code. Additionally, Managed Identities is used with various other Azure services. Hence, such services require special attention when it comes to service hardening while maintaining the same level of security. This also creates a need for stronger identity management to ensure secure access.

In this session, we present our findings from two Azure services, highlighting how we successfully bypassed the security mechanisms of Managed Identities. Attendees will gain insights into two novel approaches for maintaining persistence in Azure Functions and Azure Machine Learning service. Our investigation uncovered security gaps and design oversights within these services. These flaws allow attackers to impersonate assigned managed identities and allows for stealthy persistence in scenarios following a compromise. We managed to extract Managed Identity Entra ID token off the Azure resources to which these identities were allocated, undermining the fundamental principle of managed identities. Furthermore, the generated logs couldn't be used to differentiate between malicious and legitimate requests, rendering the stealthy persistence in Azure Machine Learning service undetectable.

By:
Nitesh Surana  |  Senior Threat Researcher, Trend Micro
David Fiser  |  Senior Threat Researcher, Trend Micro

Full Abstract & Presentation Materials:
