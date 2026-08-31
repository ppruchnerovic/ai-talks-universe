---
id: ipKgoKSkBnc
title: "Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io"
slug: enterprise-challenges-with-mcp-adoption-christian-posta
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Christian Posta"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 30
published_at: 2026-04-09T05:21:42Z
video_id: ipKgoKSkBnc
youtube_url: https://www.youtube.com/watch?v=ipKgoKSkBnc
tags: []
transcript: false
---

# Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io

**Christian Posta**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=ipKgoKSkBnc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io

The Model Context Protocol specifies how MCP servers expose tools, data, and workflows to agents. The spec was written in terms of single tenant, desktop based use cases. Enterprises need to move beyond this definition of and begin building “MCP services”: secure, remotely accessible, multi-tenant, governed services that expose sensitive business capabilities to AI agents.

In this talk, I'll highlight three challenges that arise:

Onboarding & Discovery: How do you register, approve and safely expose MCP services while defending against tool poisoning and shadow services?

Authorization & Identity: How much of the MCP Authorization spec can be adopted when most IdPs don’t support the RFCs it assumes? What’s the gap between the spec’s design for public SaaS and the reality of enterprise SSO, policy engines, and workload identity?

Upstream Access & Consent: Once an MCP service needs to call enterprise APIs on behalf of a user, how do we govern delegation and prevent credential misuse?
