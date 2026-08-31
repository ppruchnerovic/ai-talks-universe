---
id: jtnRFgu4tdI
title: "Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Vi... Fan Zhang, Kevin Klues & Alay Patel"
slug: cloud-native-theater-kubevirt-summit-kubevirt-on-gb200-vi
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 33
published_at: 2026-04-09T05:20:35Z
video_id: jtnRFgu4tdI
youtube_url: https://www.youtube.com/watch?v=jtnRFgu4tdI
tags: []
transcript: false
---

# Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Vi... Fan Zhang, Kevin Klues & Alay Patel

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=jtnRFgu4tdI) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Virtualizing a Rack-Scale Supercomputer - Fan Zhang, Kevin Klues, and Alay Patel, NVIDIA

GB200 (Grace Blackwell) changes the implementation for virtualization versus classic PCIe-based servers. Instead of discrete CPU and GPU devices connected through PCIe, GB200 couples CPU and GPU through a cache-coherent interconnect and unified memory, and the rack behaves like a single logical system. That shift breaks long-standing assumptions in the VFIO/QEMU/Kubernetes stack and requires changes in KubeVirt.

In this talk, we’ll share the practical enablement path for running KubeVirt successfully on GB200. We’ll cover:
- VFIO and kernel requirements.
- QEMU/libvirt requirements
- Topology Manager requirements for Device Plugins or using DRA
- Rack-scale orchestration: introducing Compute Domains as the unit of allocation for multi-node GPU fabrics, and how IMEX domain bring-up/teardown is orchestrated via an IMEX daemon integrated with KubeVirt lifecycle.
- Guest topology pass-through: Pass host CPU/memory/GPU topology into the guest, and how we mirror host topology so the guest driver can online and use memory correctly.

Attendees will leave with an end-to-end mental model, practical integration patterns, and a validation checklist for bringing KubeVirt to GB200-class racks.
