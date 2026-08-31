---
id: vi_VhZLWs9k
title: "Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution... Mingshan Zhao & Zhen Zhang"
slug: sandbox-operator-enabling-session-aware-efficient-mcp-tool
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 32
published_at: 2026-04-09T05:10:54Z
video_id: vi_VhZLWs9k
youtube_url: https://www.youtube.com/watch?v=vi_VhZLWs9k
tags: []
transcript: false
---

# Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution... Mingshan Zhao & Zhen Zhang

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=vi_VhZLWs9k) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution in Kubernetes - Mingshan Zhao & Zhen Zhang, Alibaba

As AI agent architectures evolve, MCP is emerging as the standard interface connecting LLMs with external tools. MCP tools must maintain contextual state within user sessions to support multi-turn interactive tasks.

However, in Kubernetes environments, launching separate Pods for each user session to run MCP Tools presents challenges: 1. Massive concurrent sessions lead to explosive Pod growth (potentially reaching hundreds of thousands); 2. Sparse tool invocations cause Pods to remain idle for extended periods, resulting in severe resource waste; 3. Traditional “use-and-destroy” patterns fail to preserve runtime state, disrupting contextual continuity.

I implemented the Sandbox Operator to natively support MCP Tools within K8s. Its core features are: 1. Managing Sandbox Pods based on session lifecycle; 2. Integrating community Checkpoint/Snapshot mechanisms to persist tool state; 3. Reconstructing tool context during recovery to maintain user continuity.
