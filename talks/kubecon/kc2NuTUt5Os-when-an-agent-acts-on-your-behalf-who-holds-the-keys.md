---
id: kc2NuTUt5Os
title: "When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research"
slug: when-an-agent-acts-on-your-behalf-who-holds-the-keys
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 37
published_at: 2026-04-09T05:25:44Z
video_id: kc2NuTUt5Os
youtube_url: https://www.youtube.com/watch?v=kc2NuTUt5Os
tags: []
transcript: false
---

# When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=kc2NuTUt5Os) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research

When you prompt an agent to commit code or trigger a workload, who is truly acting? In enterprise environments, ambiguity creates a critical security vulnerability that makes fine-grained authorization and audit impossible. Traditional static API keys simply can’t capture the full context behind an action.

In this session, we will present an architecture that cryptographically binds agent identity with delegated user identity. We will demonstrate how SPIRE’s workload attestation can be extended to create a verifiable agent identity, and how Keycloak, acting as an OAuth 2.0 server, manages delegated user identity while preserving context across long, nested transactions. Finally, we’ll introduce an open-source MCP Gateway that enforces policy and audit controls at a single, trusted point between agents and tools.
Attendees will leave with a clear understanding of how to build agentic systems where every action is traceable to both the code that execute it and the user who approved it.
