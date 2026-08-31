---
id: F1DYkY1BlfM
title: "Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat"
slug: lobster-trap-openclaw-in-containers-from-local-to-k8s-and
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 22
published_at: 2026-05-22T17:00:06Z
video_id: F1DYkY1BlfM
youtube_url: https://www.youtube.com/watch?v=F1DYkY1BlfM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=F1DYkY1BlfM) · [Conference site](https://www.ai.engineer/)

## Description

Sharing a good agent setup usually means handing someone a pile of markdown, config files, and YAML and hoping they reproduce what you have. The answer in this demo is a container image: spin up a sub agent in two seconds from a Podman command, flip a flag for Kubernetes, and your personal setup becomes the team baseline.

The stack is Podman locally, Kubernetes for distribution, same container image throughout. Secrets get two layers: Podman secrets for API keys on the host, OpenClaw secret refs inside the container. Volumes handle backup and recovery. An Nvidia team runs the same pattern in production with ten engineers each running their own OpenClaw in Kubernetes for model evals, doing work that used to take six people.

Speaker info:
- https://www.linkedin.com/in/sally-ann-omalley/

Timestamps:
0:00 Introduction and background on Sally Ann O'Malley
1:25 Discovering and experimenting with OpenClaw
2:35 Benefits of running AI agents in containers
3:05 Introducing Forever Claw and sub-agents
5:52 Using containers for agent configuration and tools
6:21 Managing secrets with Podman and Kubernetes
8:10 Scaling agent workloads with Kubernetes
9:15 Nvidia team case study: Model evaluations
11:09 Backup, recovery, and persistence with volumes
11:47 Vision for workplace agent standardization
14:14 Local demo: Running OpenClaw with Podman
16:45 Choosing providers and configuring settings
17:50 SSH sandbox features
18:22 Running the Podman command and checking agent status
20:52 Transitioning agent workloads to Kubernetes and OpenShift
