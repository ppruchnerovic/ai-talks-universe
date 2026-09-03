---
id: DhjbD-Bhn9E
title: "Java Agent vs. eBPF: A Deep Dive into OpenTelemetry Instrumentation Technologies - Fabian Stäber"
slug: java-agent-vs-ebpf-a-deep-dive-into-opentelemetry
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2025
speakers: ["Fabian Stäber"]
channel: null
duration_min: 38
published_at: 2025-10-02T12:31:30Z
video_id: DhjbD-Bhn9E
url: https://www.youtube.com/watch?v=DhjbD-Bhn9E
youtube_url: https://www.youtube.com/watch?v=DhjbD-Bhn9E
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: false
---

# Java Agent vs. eBPF: A Deep Dive into OpenTelemetry Instrumentation Technologies - Fabian Stäber

**Fabian Stäber**

`Devoxx` · `Devoxx` · `2025` · `38 min`

[Watch the recording](https://www.youtube.com/watch?v=DhjbD-Bhn9E) · [Conference site](https://devoxx.com/)

## Description

OpenTelemetry's new eBPF instrumentation [1] offers zero-code automatic instrumentation for a wide range of programming languages, including Java. However, there's also the well-established OpenTelemetry Java instrumentation [2], which is based on the Java agent technology and can be attached to any Java 8+ application. In this talk we'll present a comparative analysis of Java agent vs. eBPF in OpenTelemetry. You will learn to decide which instrumentation technology is right for you.

We'll cover operational aspects (deployment strategies, compatibility with third-party instrumentation), security considerations, deep dive into unexpected behaviors (why latencies reported by the Java agent may differ from the latencies reported by eBPF instrumentation), show how the underlying K8S platform and service meshes affect instrumentation, present recent advances in eBPF instrumentation (like trace ID propagation), and evaluate the performance impact of both Java Agent and eBPF.

We will close out with an outlook on future plans, including ideas on how to combine the two technologies to get the best of both worlds.

[1] https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/
[2] https://github.com/open-telemetry/opentelemetry-java-instrumentation/
