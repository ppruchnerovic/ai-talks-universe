---
id: KtnD-wILqb0
title: "LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu"
slug: llm-inference-at-scale-orchestrating-prefill-decode
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Zhonghu Xu"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 32
published_at: 2026-04-09T05:25:42Z
video_id: KtnD-wILqb0
url: https://www.youtube.com/watch?v=KtnD-wILqb0
youtube_url: https://www.youtube.com/watch?v=KtnD-wILqb0
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu

**Zhonghu Xu**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=KtnD-wILqb0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu, Huawei Technologies Co., Ltd

Prefill-Decode (PD) disaggregation has emerged as the reference architecture for large language model (LLM) inference deployments. By separating the prefill and decode stages, PD disaggregation eliminates cross-stage interference, significantly improving Time-To-First-Token (TTFT) and Time-Per-Output-Token (TPOT) metrics.

This session introduces Kthena's approach to orchestrating PD-disaggregated LLM workloads in Kubernetes through a simple, lightweight API. Our hierarchical role-based design natively supports multi-group xPyD inference deployments with the following capabilities:

- Dynamically adjust instance ratios between prefill and decode stages accordingly
- Either collaborate with LeaderWorkerSet (LWS) for role-based deployments or direct Pod management
- Enhanced network topology aware shceduling: combined with Volcano or Kueue supernode-aware scheduling to achieve better inference performance.

## Transcript

*3,247 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=KtnD-wILqb0&t=0s)** Today, I'm going to talk about LM inference at scale. Especially how to orchestrate uh PD disaggregation LM. I'm Junhu Shi from Huawei Cloud. Uh actually, my name is a little bit hard to pronounce. Uh in Chinese, Shi Who means tiger actually. Yeah. Uh first, let's talk about my myself. My name is Junhu. Currently, I work serve as the since F tech infra tech leader. Uh and also represent the Istio steering committee. Uh as a member as a maintainer of Volcano and also Istio Kmesh. And I have spent many years contributing to the

**[0:49](https://www.youtube.com/watch?v=KtnD-wILqb0&t=49s)** uh modern orchestration. I'm very delighted dedicated to the open source. Yeah. You can find me with this GitHub. Yeah. Uh today, we are going to explore the evolving landscape of AI infrastructure. Our discussion will center on how to move beyond traditional deployment patterns to build more efficient and cloud native system for large language models, especially for distributed inference. Yeah. Let's get to the first part. Uh what's the current status of LM inference in Kubernetes? To understand why Cassena exist, we

**[1:39](https://www.youtube.com/watch?v=KtnD-wILqb0&t=99s)** first have to look at the last mile of AI production inference. For many years, Kubernetes have has excelled at orchestrating stateless microservices, but LMs are completely different beast. They require gigabit They require gigabytes of weights to be loaded. They generate They generate massive data in the form of cubic hash, and they require stricter gun scheduling for GPU resources. If you try to So, if you try to manage LM using uh standard community deployment or like project little offset,

**[2:28](https://www.youtube.com/watch?v=KtnD-wILqb0&t=148s)** you may actually uh fall into a dead loop. Uh you would need to manage um specific um resources one by one. Oh, next. Uh to understand the orchestration problems, we have to look inside the model. Um inference happens in two distinct stages. I mean the language model, yeah. The first is the prefill stage, where the model injects your entire prompt. This is very highly parallel and extremely compute bound. Second, it is the decode stage. Uh this is a very memory bandwidth

**[3:19](https://www.youtube.com/watch?v=KtnD-wILqb0&t=199s)** bound. It is the procedure of generate tokens one by one. So, it it is sick a very different stages. Uh so, if we deploy the prefill and the decode in the same instance, they may interference each other. Yeah, many times people run them in the same uh GPU instance. This causes interfere interference problem Image request A is a

**[4:06](https://www.youtube.com/watch?v=KtnD-wILqb0&t=246s)** uh very long prompt and it requires very high compute resources. And suddenly request B arrives with a message prompt. It also needs to use uh uh compute resources. And then sorry. Uh sorry. I think from the picture left is a profile, right is a decode. Yeah, sorry. Very sorry. The GPU shifts is computer power to handle request B's profile. Request A's those. They are fighting for the same silicon causing

**[4:54](https://www.youtube.com/watch?v=KtnD-wILqb0&t=294s)** uh major latency spikes and leaving expensive high high hardware uh underutilized. Okay, in the AI world user user experience is defined by the two metrics. Uh TTFT actually is the time to first token. And also the TPOT time per output token. Because of the interference we just discussed, a coupled architecture forces a painful trade-off. If you optimize your batch size for faster profile, your token uh streaming which means TPOT gets slow and

**[5:44](https://www.youtube.com/watch?v=KtnD-wILqb0&t=344s)** and slow. If you optimize for smooth, for smooth streaming new users wait forever for their first token. It will will degrade degraded the user experience. We realized that the only way to break this trade-off is to write these two stages apart, which leads to uh prefill decode disaggregation. Yeah, next part we'll talk about the paradigm shift of prefill decode disaggregation. The The industry's answer to the interference problem is prefill decode

**[6:35](https://www.youtube.com/watch?v=KtnD-wILqb0&t=395s)** uh disaggregation. Instead of forcing GPU to do everything, prefill decode in one GPU will split the class into two distinguished parts. Port A handles the prefill procedure, and Port B handles the decode procedure. Yeah, so they have no actually no interference. Once the parameter is uh processed, it handles the state over to Port B to do decode. By physically isolating these workloads, we completely eliminate uh implement eliminate the cross-stage interference. Okay, this brings us to the XT XPYD

**[7:29](https://www.youtube.com/watch?v=KtnD-wILqb0&t=449s)** model. X represents the number of prefill instances, and the Y represent represents the decode instances. The beauty of disaggregation is a symmetric scaling. If you are running a rate uh IG rag pipeline you you process you process massive documents, but generate uh short answers. So, you scale up X. Uh you scale up prefill. If you are running uh coding like coding assistant that generates high hundreds of lines of code from a short prompt, you scale up Y. Scale up uh decode. You only pay for the exact hardware profile your workload needs.

**[8:19](https://www.youtube.com/watch?v=KtnD-wILqb0&t=499s)** Also, it's very flexible. Okay, but the disaggregation isn't magic. This is a There's a catch when you uh when the prefill node finishes prefe- uh processing the prefill, it has to transfer the state uh which means the KV cache over the network to the decoder node. For large context, the KV cache can be a very large maybe uh gigabytes of data. If your prefill pod and decode pod are sitting on off sides of your data center, the network transfer time will completely erase any TTFT speed up you gain from the disaggregation.

**[9:10](https://www.youtube.com/watch?v=KtnD-wILqb0&t=550s)** This network becomes the network become the new bottleneck. Yeah that's what I mean uh vanilla Kubernetes struggles with the X P Y D disaggregation. Yeah. Imagine you are trying to build and manage the X P Y D architecture using vanilla Kubernetes. It is a nightmare. You have to separate deployments for pre-prefill and the code. Uh if you are using AWS, you need to define one uh AWS for prefill and then you need to dis- find another for decode instance. You have to build

**[9:58](https://www.youtube.com/watch?v=KtnD-wILqb0&t=598s)** customer routing to switch across them. You uh your standard HPA has no idea how to scale Yeah, how to scale based on the KV cache pressure pressure and the most importantly, the default Kubernetes scheduler is topology blind. It might It might uh schedule your prefill pod on rack one and then uh your decode pod on rack 10, killing your uh KV cache transfer speed. Uh this massive operational gap is exactly why we built Cassini. Yeah, this part I will introduce Cassini. It is a sub-project under Volcano.

**[10:52](https://www.youtube.com/watch?v=KtnD-wILqb0&t=652s)** Yeah, to solve this routing scaling and uh scheduling nightmares, the Volcano community community built uh Cassini. Cassini is a open source project under since I've Volcano. It is a designed to from the ground up to orchestrate LM inference. It acts as a intelligent control plan that understands the unique life cycle of AI workloads. Instead of hacking together uh hacking together generative generic Kubernetes deployments to mi- uh mimic disaggregation, Cassini gives you a native purpose-built engine to manage it. Yeah, from the architecture of CosenA, we can see it actually has two

**[11:42](https://www.youtube.com/watch?v=KtnD-wILqb0&t=702s)** decoupled decoupled components. One is the a CosenA router. Actually, it is a data plane and manage the traffic routing. And this the second component is the CosenA control manager. It is a operator that can help you manage distributed PD disaggregated workload. It It has a very simple API called model serving. Uh we will take a look at it later. Yeah. Uh so, let's take a about the take a look at the model serving.

**[12:31](https://www.youtube.com/watch?v=KtnD-wILqb0&t=751s)** In CosenA, we actually introduce three lightweight custom resource definition. Uh model server actually defines your inference engine and uh uh serving instances. Model router defines the traffic routing. And the for the workload orchestration, it is the model serving. From the picture, we can see model serving can help us define uh managers issue. Uh actually, it is a You can use it to represent profile or decode or even if you want to uh deployment deployment the uh EPD, you can use a rule to represent encoder

**[13:19](https://www.youtube.com/watch?v=KtnD-wILqb0&t=799s)** for uh for the visual models. Yeah, I will show you about more details about the uh model router. It is a data plan API help you define the model the model routing rules. We can see here uh if you want to access the deep six simple model, you can define the this rule. If you access with the body model name deep six the traffic will be routed to the model server. Let's take a look at the what is model model server. Model server is actually

**[14:08](https://www.youtube.com/watch?v=KtnD-wILqb0&t=848s)** uh like inference pool. It is used to select the uh workloads. Uh but the difference is here. We can see we defined the PD group attribute in the model serving. It is used to help us help the casena router to understand uh the workload whether it is the prefill or decode. Uh it is quite different from the inference pool here. Uh so it is basically natively can support prefill and a decode routing. We don't need any other side cars or something else. Yeah. Uh next to take a look at the

**[14:56](https://www.youtube.com/watch?v=KtnD-wILqb0&t=896s)** hierarchical rule based design of model serving. This is a workload. Uh we can use model serving to define multiple serving group. One serving group here is XPYD. Under the serving group, we have mm defined the rules. I issue you can represent a prefill a decode or uh some other rules if you like. Yeah, to a developer or user to basically view and you just join model. They shouldn't to have to care about it whether it's running across 10 different machines or in two different stages. Uh so, Kaseina here is to

**[15:45](https://www.youtube.com/watch?v=KtnD-wILqb0&t=945s)** uh design the to help uh resolve this as a top level of our modeling. It's very flexible for you to to define the deployment paradigm. So next This is a hierarchy API. Uh actually, in each row, we uh are equivalent to the F 1 2 S. So, I mean, uh you don't need to define multi CRs if you want to deploy distributed uh inference extensions inference instances.

**[16:34](https://www.youtube.com/watch?v=KtnD-wILqb0&t=994s)** Yeah, the detail here is you you are you can use serving group as a atomic scheduling unit for uh XBYD likely 1P1D. Uh here, we have we collaborate with the Volcano scheduler to support multi-level gun scheduling. Um Here, the serving group level at the serving group level, we require at least we may require one profile and one decoder to serve. And at the row level, all the pods within a row must be scheduled together. Uh To be accurate, the in the row, we may have many parts um to represent a row, especially for very large models like deep say V 3

**[17:26](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1046s)** You may deploy with large EP or DP. Actually, that can't be running one machine. So, we need to go scheduling the row level two. So, here it is a two level go scheduling. Yeah. And also we need multi-level network topology aware scheduling. Serving group level co- located uh collocate the entire PD group in the same maybe hyper node. Yeah, row level we collect collocated the entry and worker within each per field decoder row. And also we need a pluggable KV connectors like M cache or Nicsol.

**[18:17](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1097s)** Memcache for KV cache transfer between PD. So, I mean here you can uh use a row to represent the KV cache. Next, I will deep dive the advanced orchestration capabilities. Okay, once you deploy PD disaggregation, you'll realize that traffic is never static. Static, if you hardcode your cluster to uh uh two per field and four decoder ratio, you will eventually stranded GPU capacity with workload perfect profile shift. Cosin enables dynamic instance ratio adjustment because per field and decoder are defined as

**[19:06](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1146s)** separate rows. Cosin enables can monitor stage specific metrics like KV cache usage, uh memory fragments. and also the Q depths and the independently scale them. We can elastically shift from a heavy prefill ratio to a heavy decode ratio on the fly ensuring max maximum GPU utilization depends on our business. Okay, we also support elastic auto scaling with very very high level. Uh it is supposed both homogeneous and heterogeneous scaling

**[19:55](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1195s)** with a integral opera- optimizer uh built in the model serving controller. For the homogeneous auto scaling similar to KPA, it supports both stable and panic models. Yeah, for the heterogeneous scaling, hetero- genius scaling can plan the optimal hard- hardware resource configuration through an integral programming solver based on the cost of the accelerator and the service presence processing capability. Okay, so next part is the topology aware scaling. Now we arrive at hot hottest problem problem. We mentioned earlier that that a prefill

**[20:43](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1243s)** nodes must transfer the cubic actual to the decode node if the Kubernetes scheduler place your prefill pod on rack one and your decode pod on maybe rack 10, then the cubic actual had to traverse multi spin switches. The network latency will have completely destroyed the TDFT improvements you gained by aggregating in the first place. So then the community scheduling is topology blind. It just looks for available GPU resources. It doesn't look at the network. Yeah, the model aware inference routing we talked about the orchestration and scale

**[21:32](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1292s)** scaling of pods, but how does the actual promoter get to the right pod? Standard Kubernetes load balancer is completely blind to air context. If you are using generic proxy, it might send a massive tokens promoter to a pod whose KV cache is already maybe full. To solve this, we build the Kasina router. It acts as an intelligent data plan entry point natively and understanding the XPUID topology and directing the traffic specially for the disaggregated setups. It is understanding the the inference engine metrics like the pending queues

**[22:20](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1340s)** and the KV cache usage and GPU usage. And also it supports lower lower aware. Yeah, we have built in many advanced scheduling algorithms includes profile cache KV cache awareness and and also supports fairness scheduling for multi-tenancy. For the PD disag decode profile decode disaggregation, we natively support the PD group aware. Yeah, the magic of the Kasina router lies in its scope plugin architecture because it's a stand-stand alone binary with minimal dependencies. It continuously monitors your back-end inference engines

**[23:10](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1390s)** like VM or SG line. It knows exactly the metrics of the engine. So, it can do the traffic scheduling more efficiently and helps uh improves the performance in terms of latency. And it also helps uh ensuring higher throughput and protecting your TPO T. So, by leveraging Kina Router's flexible scheduling plug-in architecture, we can intelligently route requests based on what is already cached by combi- combining cube cache or any sending the request to the pod that

**[23:58](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1438s)** already have the perimeter in memory. With the least requested strategy, we achieve massive gains compared to just randomly assigning requests to the route, almost tripling. And the time it takes to get the first token drops by nearly three quarters. Okay, we also want to ensure Kina fits seamlessly into the modern Kubernetes system as the indus- industry moved away from the traditional ingress API. Kina Router natively supports the new Kubernetes Gateway API and specializes to Gateway API inference extension. This means you can

**[24:46](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1486s)** also expose your disaggregated AM workloads using the standard interoper- interoperable traffic management APIs, avoiding vendor lock-in and allowing your API infrastructure teams to use the exact same patterns they use for microservices. Oh next I will show a demo here. How we use Okay. Okay. In this demo, we will It is a little bit small. In this demo, we will deploy

**[25:33](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1533s)** a profile decode disaggregated deep learning model. You can see here we use the rules profile decode. And the issue and the issue rule actually it has a entry pod. Because the model is very small, we only need a entry entry pod and no worker pod is needed. So, just two pods. One is profile pod and the other is decode pod. Yeah, we also define the model route for how how we access the uh models. And this is the model server which is

**[26:21](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1581s)** used to uh define how to uh find out the profile pod and the decode pod for the Casina router. It is used by the router. I think the next two we will test its accessible. Okay.

**[27:10](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1630s)** Sorry. Sorry. It's comes forward. Uh so I may not have enough time to show this. Actually, the the other step is just to test this can be accessed from the Cosina router to the exact profile and decode. Okay. If you want to see the demo, you

**[28:00](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1680s)** can come to our Volcano booth. We will be at the booth today and also tomorrow, I think. Okay. Uh next part is the last part we're looking forward. We recently released the V 0.3 which made Cosina product ready and with full a little work set integration and end-to-end router over the ability. But we are just getting started on our road map. We are building more advanced scale plugins for 7000 routing, expanding our support for header heterogeneous accelerators. So you can mix and match the GPUs and MPUs across profile and decode.

**[28:50](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1730s)** And refining the zero downtime upgrades, specially for disaggregated topology. Yeah, if you are interested in our project, please join us with uh uh GitHub or Slack. You can talk talk to us directly. So, thank you. I think we have 2 minutes for questions. Uh one thing I'm curious about, often

**[29:41](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1781s)** times in high-performance and efficient inference setups, you split all the experts onto their own nodes and GPUs. How would this roughly be accomplished with Volcano? Sorry? If you have, say, Deep Seek, um which has 370 experts or something, because it's a mixture of experts model. Um often times you to improve the cache utilization stuff, you put each of those experts onto their own GPU. And then just uh split the requests over multiple nodes and then combine the results again. Can this be somewhat easily implemented on Kubernetes as well, or how would you do this? Uh I think this sound maybe a little

**[30:32](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1832s)** hard to uh Can you repeat again? Sure. I think the You can see directly without it. Okay. Um, if you have a mixture of experts models, Yeah. then it is often times more efficient to have each of those experts live on its own GPU and then just route the request to whichever experts get activated, which are live on different machines and combine the requests back together again for the activations. Is that reasonably easily implemented on a cluster setup like this or not? For the EP load balance, actually it is responsibility of the inference engine

**[31:21](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1881s)** like the RM. I heard many users maybe enhance their own EP LB policy in the engine. This actually, to be honest, is not the a scope of Cassini. We are focusing on the high level oxy-shading the high level routing. Not not the internal inner routing to for the different EP. Okay. Yeah, actually you can uh, deploy many EP expert in one GPU. This is uh, according to your resources and the scenarios maybe. I've heard many users deploy many

**[32:10](https://www.youtube.com/watch?v=KtnD-wILqb0&t=1930s)** many experts on one CPU and one GPU. Yeah. Yeah. Good. Thank you. So, thank you.
