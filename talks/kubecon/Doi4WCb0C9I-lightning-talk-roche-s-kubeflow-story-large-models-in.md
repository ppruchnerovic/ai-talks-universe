---
id: Doi4WCb0C9I
title: "Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Securit... Oswaldo Gomez"
slug: lightning-talk-roche-s-kubeflow-story-large-models-in
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 11
published_at: 2026-04-13T23:36:03Z
video_id: Doi4WCb0C9I
youtube_url: https://www.youtube.com/watch?v=Doi4WCb0C9I
tags: []
transcript: false
---

# Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Securit... Oswaldo Gomez

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=Doi4WCb0C9I) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Security up With Bottlerocket - Oswaldo Gomez, Roche

At Roche pRED, our MLOps platform runs hundreds of ML endpoints for scientific discovery. Spikes in traffic were causing timeouts, as our large (13.4GB+) GPU models took ~10 minutes for a cold-start pull. To ensure quick responses, we were forced to set min=1 replicas, resulting in over $100K in annual waste for idle nodes. This was unsustainable, especially as we retrain and deploy new models daily.

This is our end-user story of how we solved this by adopting Karpenter for rapid node autoscaling and Bottlerocket on EKS. We will detail the specific technique of using Bottlerocket's mutable data volume to prefetch large container images before pods are scheduled.

We will show load-test data (20K API calls) that proves how we cut pull times from minutes to seconds, achieving a 58% faster cold-start. Learn how this combination enabled true scale-to-zero (even for GPUs), slashed costs, and enhanced security with an immutable OS
