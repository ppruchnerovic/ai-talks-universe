---
id: 9FwufB6sHDQ
title: "How the VAST AI Operating System Powers a Dynamic Data Plane for Ray | Ray Summit 2025"
slug: how-the-vast-ai-operating-system-powers-a-dynamic-data
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2025
speakers: []
channel: "Anyscale"
duration_min: 13
published_at: 2025-12-01T20:10:41Z
video_id: 9FwufB6sHDQ
url: https://www.youtube.com/watch?v=9FwufB6sHDQ
youtube_url: https://www.youtube.com/watch?v=9FwufB6sHDQ
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# How the VAST AI Operating System Powers a Dynamic Data Plane for Ray | Ray Summit 2025

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=9FwufB6sHDQ) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

At Ray Summit 2025, Glenn Lockwood from VAST Data shares how Ray’s new Label Selector API dramatically simplifies scheduling on heterogeneous GPU and accelerator clusters—eliminating workarounds and giving users fine-grained control over resource placement in distributed Ray applications.

He begins by outlining the challenge: acquiring the right accelerator resources (GPU tier, topology, interconnect, memory profile, CPU-to-GPU ratio, etc.) in a heterogeneous cluster is often difficult. Historically, users had to rely on fragile hacks such as custom resource tags or accelerator_type annotations to target specific hardware—solutions that don’t scale, break across environments, or cause scheduling failures.

Glenn introduces Ray’s Label Selector API as a robust, intuitive solution. This new API allows developers to schedule tasks, actors, and placement groups based on Ray node labels—labels that can be defined at RayCluster creation time or discovered automatically by Ray.

Key capabilities highlighted in the session include:

Support for both static and auto-scaling RayClusters

Per-bundle label selectors for precise placement inside multi-node workloads

Fallback strategies to maintain reliability under resource scarcity

Full integration with the Anyscale platform, Ray Dashboard, and KubeRay

Identical behavior across all deployment environments—from local clusters to production-grade autoscaling fleets

Glenn walks through common real-world use cases—such as selecting GPU types, restricting workloads to nodes with local NVMe, matching topology-specific requirements, or isolating latency-sensitive inference—and shows how the Label Selector API makes these constraints trivial to express.

The talk concludes with a live demo demonstrating how this new API enhances flexibility, reliability, and developer experience when scheduling Ray workloads on heterogeneous infrastructure.

Liked this video? Check out other Ray Summit breakout session recordings https://www.youtube.com/playlist?list=PLzTswPQNepXllnU0C36WtkC0dqkAoDulh

Subscribe to our YouTube channel to stay up-to-date on the future of AI! https://www.youtube.com/c/anyscale

🔗 Connect with us:
