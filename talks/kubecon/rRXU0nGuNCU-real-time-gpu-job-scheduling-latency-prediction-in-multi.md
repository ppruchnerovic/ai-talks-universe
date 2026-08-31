---
id: rRXU0nGuNCU
title: "Real-Time GPU Job Scheduling Latency Prediction in Multi-Cluster Kubernetes - Sujoy Dutta, Bloomberg"
slug: real-time-gpu-job-scheduling-latency-prediction-in-multi
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: ["Sujoy Dutta"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 22
published_at: 2026-04-13T23:36:05Z
video_id: rRXU0nGuNCU
youtube_url: https://www.youtube.com/watch?v=rRXU0nGuNCU
tags: []
transcript: false
---

# Real-Time GPU Job Scheduling Latency Prediction in Multi-Cluster Kubernetes - Sujoy Dutta, Bloomberg

**Sujoy Dutta**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=rRXU0nGuNCU) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Real-Time GPU Job Scheduling Latency Prediction in Multi-Cluster Kubernetes - Sujoy Dutta, Bloomberg

Managing thousands of GPU-enabled jobs across a multi-cluster Kubernetes environment can create unpredictable scheduling delays, impacting productivity and resource utilization. Bloomberg uses Karmada to manage ML and training workloads across data centers. This talk describes a production-ready Karmada controller that improves GPU scheduling with real-time queueing predictions, transforming a laggy process into an efficient experience.

Our system delivers precise queuing estimates through immediate processing of resource events and intelligent Karmada integration. Internal users can better understand job wait times with improved accuracy, enabling better planning and reduced GPU idle times. Our solution combines real-time statistics with Kubernetes events, seamlessly integrating with monitoring tools like Grafana and Prometheus. Attendees will learn how these innovations provide real-time insights with O(1) complexity, enhancing prediction accuracy from daily averages to live metrics.
