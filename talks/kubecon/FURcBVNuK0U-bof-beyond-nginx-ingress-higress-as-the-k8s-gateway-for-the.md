---
id: FURcBVNuK0U
title: "BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era"
slug: bof-beyond-nginx-ingress-higress-as-the-k8s-gateway-for-the
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:23:08Z
video_id: FURcBVNuK0U
youtube_url: https://www.youtube.com/watch?v=FURcBVNuK0U
tags: []
transcript: false
---

# BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=FURcBVNuK0U) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era

With the Nginx Ingress Controller officially retiring this March, the Kubernetes community faces a critical security vacuum where emerging vulnerabilities may no longer receive timely patches. Coupled with long-standing architectural bottlenecks, this end-of-life status creates an urgent need for a modern, supported successor. This session introduces Higress, a high-performance gateway built on the Envoy proxy, designed not just to replace Nginx, but to redefine the gateway's role in the AI stack. We will demonstrate a "zero-friction" migration path, leveraging Higress’s 90% compatibility with Nginx Ingress annotations, allowing platform engineers to upgrade their infrastructure without rewriting thousands of lines of YAML. We will dive into the "Wasm-first" extensibility architecture that eliminates the stability risks of Lua scripts, backed by a case study from Sealos Cloud showing how Higress reduced configuration latency from minutes to seconds for over 20,000 domains. Beyond that, we will explore why Higress is the "AI-Native" gateway of choice. Attendees will discover how to implement Token-based Rate Limiting to ensure fair usage of expensive GPU resources, and how to unify traffic management for diverse LLM providers (OpenAI, DeepSeek, Qwen) with automatic failover. We will also unveil the new Model Context Protocol (MCP) support, enabling the gateway to act as a bridge connecting legacy APIs directly to the burgeoning AI Agent ecosystem. Higress is extensive used by companies like Alibaba, Ant Group, Ctrip, DJI, Kuaishou, Paypal and many more. It is on the way joining CNCF sandbox. Join us to learn how to future-proof your Kubernetes networking for the next decade.
