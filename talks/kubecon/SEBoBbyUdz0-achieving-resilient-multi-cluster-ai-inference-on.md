---
id: SEBoBbyUdz0
title: "Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Kar... Wei-Cheng Lai & Han-Ju Chen"
slug: achieving-resilient-multi-cluster-ai-inference-on
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 29
published_at: 2026-04-09T05:10:50Z
video_id: SEBoBbyUdz0
youtube_url: https://www.youtube.com/watch?v=SEBoBbyUdz0
tags: []
transcript: false
---

# Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Kar... Wei-Cheng Lai & Han-Ju Chen

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=SEBoBbyUdz0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Achieving Resilient Multi-Cluster AI Inference on Kubernetes With Karmada and KubeRay - Wei-Cheng Lai, Bloomberg & Han-Ju Chen, Anyscale

AI inference at scale faces bursty traffic, uneven GPU supply, regional latency, varied SLO requirements, and occasional cluster or availability zone outages. A single cluster cannot reliably meet all of these demands.

This session shares a practical blueprint: use Karmada to orchestrate Kubernetes fleets—policy-based placement, replica spreading, and automated failover—and run Ray Serve-based inference with KubeRay’s RayService. Ray Serve provides a distributed, scalable Python API for inference across heterogeneous compute, built on Ray, while KubeRay manages it in Kubernetes. Together they deliver a resilient multi-cluster inference architecture that fits smoothly into existing environments.

Attendees will learn when multi-cluster is warranted, how to encode Karmada placement/override/failover policies to meet SLOs, and how to operate Ray Serve via RayService with safe scaling and upgrades—and will leave with a reference architecture, as well as ready-to-use manifests and templates.
