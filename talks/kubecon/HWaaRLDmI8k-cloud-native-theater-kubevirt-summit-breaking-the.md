---
id: HWaaRLDmI8k
title: "Cloud Native Theater | KubeVirt Summit: Breaking the Performance Barrier... Jian Li & Yves Weisser"
slug: cloud-native-theater-kubevirt-summit-breaking-the
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 26
published_at: 2026-04-09T05:20:36Z
video_id: HWaaRLDmI8k
youtube_url: https://www.youtube.com/watch?v=HWaaRLDmI8k
tags: []
transcript: false
---

# Cloud Native Theater | KubeVirt Summit: Breaking the Performance Barrier... Jian Li & Yves Weisser

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `26 min`

[Watch the recording](https://www.youtube.com/watch?v=HWaaRLDmI8k) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Cloud Native Theater | KubeVirt Summit: Breaking the Performance Barrier: High-Performance AI Storage Virtualization with KubeVirt - Jian Li, SK Telecom and Yves Weisser, NetApp

The rapid expansion of generative AI requires infrastructure that combines the agility of virtualization with the raw power of bare-metal systems. SK Telecom's Petasus AI Cloud has demonstrated this at scale through the successful commercialization of the Haein Cluster, one of the Korea's largest virtualized GPU environments featuring over 1,000 NVIDIA Blackwell GPUs. Building on this proven production experience, SK Telecom has partnered with AI Storage vendor to further enhance the Petasus platform by integrating the fast filesystem. This collaboration focuses on pushing the boundaries of KubeVirt to support the most I/O-intensive AI workloads by virtualizing Ethernet Fabrics to enable Native NFS over RDMA and GPUDirect Storage (GDS) directly within virtual machines.

In this session, we will detail the specific optimization techniques—from fabric virtualization to memory mapping—that allow the Petasus solution to achieve I/O performance nearly indistinguishable from bare-metal environments. We will move beyond theory to share empirical data from fio and gdsio benchmarks, comparing the performance of standard KubeVirt setups against our optimized stack. By showcasing how we successfully mitigated the ""virtualization tax"" in a GPU cluster, this talk provides a comprehensive technical blueprint for cloud-native architects and engineers aiming to deploy high-performance, production-ready AI infrastructure on KubeVirt.
