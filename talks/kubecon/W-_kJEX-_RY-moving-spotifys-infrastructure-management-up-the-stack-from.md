---
id: W-_kJEX-_RY
title: "Moving Spotify’s Infrastructure Management Up the Stack from Kubebu... Alexander Buck & Tomas Aschan"
slug: moving-spotifys-infrastructure-management-up-the-stack-from
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 36
published_at: 2026-04-09T05:25:44Z
video_id: W-_kJEX-_RY
youtube_url: https://www.youtube.com/watch?v=W-_kJEX-_RY
tags: []
transcript: false
---

# Moving Spotify’s Infrastructure Management Up the Stack from Kubebu... Alexander Buck & Tomas Aschan

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `36 min`

[Watch the recording](https://www.youtube.com/watch?v=W-_kJEX-_RY) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Moving Spotify’s Infrastructure Management Up the Stack from Kubebuilder to Kro and K-poperator - Alexander Buck & Tomas Aschan, Spotify

Spotify’s Resource Management platform, built on Kubernetes, enables other platform teams in various domains such as Storage, Workloads, Data and AI Platforms to ship infrastructure products to Spotify’s developers through a consistent interface. The infrastructure products are modelled as CRDs, supported by kubernetes operators written by those platform teams/

Rather than using kubebuilder (go SDK for kubernetes operators), Spotify platform teams now use the open-source project kro to abstract and compose underlying resources, and k-poperator (an internal Spotify operator) to integrate tightly with Spotify’s service ecosystem.

In this talk, you will learn how these technologies have significantly increased the developer experience, and have moved the operational burden from the platform teams to the platform itself.

And you will see case studies of how Spotify platform teams have solved real problems with these technologies, rather than struggling to build operators from scratch.
