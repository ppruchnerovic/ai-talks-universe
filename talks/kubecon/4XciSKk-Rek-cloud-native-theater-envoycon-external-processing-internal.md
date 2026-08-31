---
id: 4XciSKk-Rek
title: "Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls... Jens Kat"
slug: cloud-native-theater-envoycon-external-processing-internal
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 20
published_at: 2026-04-09T05:15:13Z
video_id: 4XciSKk-Rek
youtube_url: https://www.youtube.com/watch?v=4XciSKk-Rek
tags: []
transcript: false
---

# Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls... Jens Kat

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=4XciSKk-Rek) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls to REST with Envoy - Jens Kat, ING

AI agents are quickly becoming first-class consumers of APIs. However most enterprises already have mature API ecosystems they can't (and shouldn't) rebuild for "agentic" workflows.

At ING we operate a large service mesh with thousands of services owned by hundreds of teams and serving millions of customers.
These services all implement OpenAPI specifications. To bridge agent tool calls to existing REST endpoints at scale, we implement an MCP server as an Envoy external processing (ext_proc) integration, keeping the innovation outside the proxy while using Envoy as the production-grade data plane.
This talk focuses on why ext_proc is the right extension point. Envoy's external processing filter connects a gRPC "external processor" over a bidirectional stream, allowing the processor to examine and mutate headers, bodies, and trailers, or even return an immediate response, while Envoy remains in control of traffic handling and policy.

We'll show how we use this model to keep MCP "thin": no business logic in tool definitions just 1:1 mapping from tool calls to API endpoints, and why that decision matters for maintainability and governance. Finally, we'll highlight what we get out of the box by building on Envoy: built-in filter statistics (including ext_proc stats), standard access logging, and OpenTelemetry-based distributed tracing patterns plus an operational model we already trust at scale.

We'll close with our plan to open-source the implementation so others can adopt MCP-on-Envoy in their own meshes.
