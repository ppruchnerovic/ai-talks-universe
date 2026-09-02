---
id: RWFqNqdHSpQ
title: "Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Trad... Zhonghu Xu"
slug: lightning-talk-intelligent-traffic-routing-for-distributed
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "General software conferences"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 11
published_at: 2026-04-13T23:36:03Z
video_id: RWFqNqdHSpQ
url: https://www.youtube.com/watch?v=RWFqNqdHSpQ
youtube_url: https://www.youtube.com/watch?v=RWFqNqdHSpQ
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Trad... Zhonghu Xu

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=RWFqNqdHSpQ) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: Intelligent Traffic Routing for Distributed LLM Inference: Beyond Traditional Gateway Approaches - Zhonghu Xu, Huawei Technologies Co., Ltd

As LLM inference adopts Kubernetes, intelligent routing has become critical. Existing gateways like Gateway Inference Extension, LLM-d, and Aibrix struggle with emerging patterns like prefill-decode (PD) disaggregation and distributed parallelism (DP+EP).

This session introduces **Kthena Router**, a production-grade orchestration system for multi-model LLM workloads. Unlike approaches relying solely on engine metrics, it uses **closed-loop control with adaptive modeling** based on connections, token lengths, load distribution, and role-aware routing.
In this session, we also will deep dive:

1. How to do multi-model serving through routing policies, eliminating per-model gateway deployments
2. Native PD disaggregation support with prefill-decode awareness, then removes dependencies on per-group routers or LLM-d sidecars
3. Pluggable scheduling with fairness scheduling, semantic-aware routing, KV-cache aware placement, and GPU utilization-aware balancing.

## Transcript

*1,114 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=0s)** Hi everyone. Today, I'm going to talk about something every platform team hates when scaling LM on Kubernetes. Traffic routing, especially how we move beyond traditional gateway approaches to intelligent workload aware routing for distributed LM inference. Yeah, first let me introduce myself. My name is Shu and I'm deeply honored to be here. And currently, I serve as a tech leader for Sense F tech infra and represent the Istio steering committee. My journey in cloud native is driven by a passion for building scalable infrastructure. As a maintainer of Volcano and Istio, and also Kmesh.

**[0:49](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=49s)** I'm also a Kubernetes member. I have spent many years contributing to the backbone of model modern orchestration. Yeah. So, as we migrate LM inference to Kubernetes, standard gateways are breaking down. Existing solutions like AMD or Airbus rely heavily on Envoy external processor. But emerging architectures like Dit Perlm mixed with expert parallel parallelism and profile decode disaggregation breaks this paradigm. So, why existing gateway uh

**[1:36](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=96s)** does not fit at all? We can see here with uh this these approaches only support single model if I read correctly. Correctly. And especially for PD disaggregation, they are not aware of the PD groups. So, that means in one PD group, XPYD uh user have to deploy one router or one Envoy gateway inference extension. Yeah, that's kind of complex. So, uh let's talk about the Cassini router. Uh we don't call gateway here because it is a

**[2:23](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=143s)** actually a very lightweight router, part of the volcano ecosystem. It is a production grade orchestration system built specially for multimodal workloads. Unlike traditional routers that just generate backend uh and backend inference engine metrics like uh read VM or SG on metrics, uh Cassini used uses a closed-loop control system and also open-loop control system. It is adaptively models routing based on active active connections, incoming token lens, and also the load distri- distribution. It knows the role of the backend

**[3:12](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=192s)** uh pulse allowing for highly intelligent state-aware routing. Let's dive into uh three specific ways this changes the game. First, under the hood, this is powered by a high-performance data plan and a highly extensive control plan that integrates natively with Kubernetes and volcano. To summarize, if you are running multimodal LLMS hitting the limits of traditional gateway or trying to implement PD disaggregation, you need a router to understand Uh sorry. You need a rush to understand the back end. Okay. Kase is not just only a dead blind component. It also has a

**[4:04](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=244s)** management component on the right side, the Kase control manager. I don't want to talk about the control manager much more. It is actually just workload orchestration, especially for the pre-filled decoded integration workload on this margin node disaggregate distributed difference. Yeah. Next. Firstly, multi-model serving typically platform teams deploy a dedicated gateway or sidecar for every single model type. So, that means if you deploy about 10 models in your cluster, you have to deploy

**[4:52](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=292s)** 10 gateways. Yeah. This leads to massive operation overhead and fragmented load balancing. Kase eliminates eliminates per model gateway deployment by using a unified routing policy at a single ingress layer. Kase uh Sorry. Okay. Kase use is uh uh the request body's model field and do the routing based on the model and then according to the routing policy user defined and then prox uh forward the the request to the related pods.

**[5:42](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=342s)** Yeah. Uh second and perhaps most importantly, prefill decode disaggregation. Uh there are many talks here today talking about the inference uh traffic scheduling, but mostly they don't talk about it. PD disaggregation. Actually, prefill is a compute bound and decoding is a memory bound memory bandwidth bound. If you couple them, your GPUs are bottlenecks. To do uh PD disaggregation, today teams usually have to deploy complex per group uh routers or inject LD LMD sidecars to manage the traffic handoff between prefill and decode pulse.

**[6:29](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=389s)** Uh Kasena has native PD uh awareness built in. It routes It is aware of the PD group. And so so that means for um multi XPYD groups, we can only deploy one set of uh Kasena router. It routes the initial initial heavy prompt to the prefill pool, tracks the uh KV cache details, and sim- seamlessly directs the subsequent token generation request to the optimal optimal decode node. No sidecar, no messy per group routing. Just a pure efficient disaggregation at the ingress layer. Oh.

**[7:17](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=437s)** Uh third, one size doesn't fit all. Kasena treats routing at the skidding skidding problem of offering pluggable policies. Um here's what we pro- provided features. Uh first is uh fairness scheduling. It ensures no single noisy tenants can starve your cluster. Yeah. Next uh is uh semantic aware routing. We want to This is our on the way. We want to integrate semantic routing to uh Kserve routing and to make the cost efficient. And the third one is the KV cache aware placement. It It is a massive we route a request to the nodes that already hold

**[8:05](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=485s)** the KV cache for specific prompt. Uh It is can make the TTFT very very uh slow. Yeah. And the next one is the GPU utilization aware balancing. It ensures we are maximizing hardware IOI across the board. Uh And the last one I think is the most important and also the very different feature we provide. It provide open loop and closed loop scheduling based on both the inference engine metrics and also the gateway own uh metrics. If we just rely on the inference execution inference

**[8:53](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=533s)** uh engine metrics, it is very The latency is about 2 seconds. Yeah. That that does not fit all. Oh. Uh we also want to be in full Kserve fit seamlessly into the modern Kubernetes ecosystem. As the industry industry moves away from the traditional ingress API, Kserve routing natively supports the Kubernetes gateway API and also the gateway inference extension. This means you can expose your disaggregated LLM workloads using the gateway API. And this avoid vendor lock-in and allowing your API inference

**[9:43](https://www.youtube.com/watch?v=RWFqNqdHSpQ&t=583s)** infrastructure team to use the exact same patterns they use for microservices. Yeah. Oh. Lastly, let's take a look at how we config Kuma to support model canary release. With the model route left, it will match the user type header. If it is a premium user, the request will be forwarded to the 7B model of deep fake. And otherwise, it will be forwarded to the 5B model. On the right side side, we have a model service ID to define which model instance we select. It's a very simple. Yeah. So, that's all. Thank you.
