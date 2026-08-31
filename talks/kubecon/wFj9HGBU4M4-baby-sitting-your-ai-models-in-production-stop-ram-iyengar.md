---
id: wFj9HGBU4M4
title: "Baby Sitting Your AI Models in Production? STOP! - Ram Iyengar, Linux Foundation"
slug: baby-sitting-your-ai-models-in-production-stop-ram-iyengar
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: ["Ram Iyengar"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 18
published_at: 2026-04-13T23:36:47Z
video_id: wFj9HGBU4M4
youtube_url: https://www.youtube.com/watch?v=wFj9HGBU4M4
tags: []
transcript: false
---

# Baby Sitting Your AI Models in Production? STOP! - Ram Iyengar, Linux Foundation

**Ram Iyengar**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=wFj9HGBU4M4) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Baby Sitting Your AI Models in Production? STOP! - Ram Iyengar, Linux Foundation

AI in production is broken. They're as fussy, as can be. The number of personas involved in making an AI model ready for production is high, which makes MLOps an order of magnitude more complicated compared to DevOps.

This talk introduces a streamlined, standardized workflow to take the manual effort out of MLOps packaging & deployment.

The first step is ModelPack, a sandbox project under the Cloud Native Computing Foundation (CNCF). It provides a standard, open-source way to organize all the files that make up a machine learning model.

We will introduce ModelKit, which is a directory structure that logically groups all the previously dispersed artifacts into a single, cohesive package. The final deployment artifact will automate the process of building a runnable, OCI-compliant container image.

The final step of deployment becomes rudimentary, as the image is available on any container registry.
