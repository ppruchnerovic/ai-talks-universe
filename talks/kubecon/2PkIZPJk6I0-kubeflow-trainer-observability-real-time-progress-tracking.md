---
id: 2PkIZPJk6I0
title: "Kubeflow Trainer Observability: Real-Time Progress Tracking for Reliab... Abhijeet Dhumal & Rob Bell"
slug: kubeflow-trainer-observability-real-time-progress-tracking
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 29
published_at: 2026-04-13T23:36:02Z
video_id: 2PkIZPJk6I0
youtube_url: https://www.youtube.com/watch?v=2PkIZPJk6I0
tags: []
transcript: false
---

# Kubeflow Trainer Observability: Real-Time Progress Tracking for Reliab... Abhijeet Dhumal & Rob Bell

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=2PkIZPJk6I0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Kubeflow Trainer Observability: Real-Time Progress Tracking for Reliable ML Training on Kubernetes - Abhijeet Dhumal & Rob Bell, Red Hat

Without observability, training is just expensive guesswork.

Imagine a hyperparameter search across 50 configurations—16 GPUs for 8 hours each—consumes 6,400 GPU-hours at $25,600. Without real-time metrics, underperforming configs burn resources. Platform teams can't distinguish converging TrainJobs from diverging ones. Algorithms like Hyperband reduce costs through early stopping, but can't function without real-time training metrics from distributed jobs.

In this session, we'll show how Kubeflow Trainer v2's native observability unlocks Katib's full potential. We'll demonstrate how training metrics flow into TrainJob status through the Kubernetes API—no code instrumentation, no MLflow servers, no TensorBoard infrastructure. We'll show how to query progress with kubectl. We'll demonstrate Katib's Hyperband watching TrainJob eval metrics and terminating underperforming trials immediately, delivering 5-10x cost reduction.

With native observability, make every GPU-hour count!
