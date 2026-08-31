---
id: KXmPxmNN0fc
title: "Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM"
slug: agentic-networking-securing-ai-agents-on-kubernetes-haiyan
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Haiyan Meng"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:24:09Z
video_id: KXmPxmNN0fc
youtube_url: https://www.youtube.com/watch?v=KXmPxmNN0fc
tags: []
transcript: false
---

# Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM

**Haiyan Meng**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=KXmPxmNN0fc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM

AI agents function like next-generation microservices, but their autonomous behavior and unique communication patterns present challenges and new security needs for existing cloud-native infrastructure. Prompt injections can exfiltrate PII to third-party tools, and poisoned tool responses can manipulate agent decisions.

Kubernetes was not originally designed for the intricate and often unpredictable traffic patterns of A2A, agent-to-tool, and agent-to-LLM communication.

This session introduces "Agentic Networking" to adapt Kubernetes for this new reality. We will dive into the core challenges posed by AI-first protocols like MCP and A2A, which require a fundamental rethinking of traffic management, security, and governance.

We will present our work extending the Kubernetes Gateway API to provide well-governed, auditable agentic traffic, with gateway-level guardrails to further secure agents running on Kubernetes. Join us to explore the future of Kubernetes networking in the age of AI.
