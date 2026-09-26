---
id: FCtTk4H8ynM
title: "Serving Frontier MoE Models at the Lowest Token Cost | NVIDIA | Ray Summit 2026"
slug: serving-frontier-moe-models-at-the-lowest-token-cost-nvidia
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 14
published_at: 2026-09-17T16:06:15Z
video_id: FCtTk4H8ynM
url: https://www.youtube.com/watch?v=FCtTk4H8ynM
youtube_url: https://www.youtube.com/watch?v=FCtTk4H8ynM
tags: []
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# Serving Frontier MoE Models at the Lowest Token Cost | NVIDIA | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=FCtTk4H8ynM) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Many of today's most capable open-source models use mixture-of-experts architectures, but serving MoE models at production scale is notoriously challenging. Agentic applications raise the stakes: a single prompt can trigger multiple planning, tool-calling, and reasoning requests, multiplying both latency and token costs.

At Ray Summit 2026, Amr Elmeleegy from NVIDIA goes under the hood of MoE serving to show how NVIDIA Blackwell rack-scale systems and open-source inference software enable low-cost, high-throughput inference, and how Ray Serve operationalizes these deployments.

You'll leave knowing how to serve frontier MoE models at the lowest token cost.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,984 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=6s)** Good afternoon everybody. Super excited to be here with all of you at the Ray Summit. My name is Amil Migi. I'm a member of the accelerated compute data center product marketing team at NVIDIA and I feel incredibly lucky to have the opportunity to have a front row seat as Nvidia introduces new accelerated computing platforms every year into the market from Hopper to Blackwell, Blackwell Ultra, Vera Rubin. With every new generation, we unlock new capabilities, bring in a new generation of software, and open up new opportunities for the ecosystem. We were here last year talking to you about NVIDIA Dynamo, which is a core

**[0:55](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=55s)** pillar of our inference software stack. Today and this year, we want to talk to you a little bit more broadly about inference and how NVIDIA sees some of the emerging challenges as inference is being deployed into production, how we're co-designing across the entire stack from computing to networking to software, and how we're collaborating with the open-source ecosystem to help accelerate inference, make it cheaper and more scalable. But in order for us to understand where inference is headed, we have to start by looking at where models are headed. And if we look at the last few years, we're going to notice that models have grown in size by a factor of over 25,000 times. If you look at the early model

**[1:48](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=108s)** back in 2021, the BERT model, that model was 110 million parameters. Now we fast forward to just a few days back. Some of the latest frontier models like Quen 3.8 and Kim K3 are now close to three trillion parameter models. That's almost 25,000 times larger than BERT. And if you look at the trend line, that's about a 7x annual growth rate in model sizes. But models are not only growing in size, they're also growing at an even faster pace in terms of capabilities. Over the last couple of years, model capabilities have grown by a factor of 15x, almost doubling than the prior years. But what does this mean for inference deployment? That means that we went from facing a

**[2:37](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=157s)** challenge of how do we take a lot of small models and deploy them on a GPU to now how do we take a very massive model spread that model across a very large number of GPUs and ensure that these GPUs work collect collectively together as one massive GPU. If we look a little bit even closer at some of the top large most intelligent frontier models, we'll notice that all of these models have one thing in common. And that thing is that they all rely on the mixture of experts ore architecture. That architecture is unique because it allows models to scale to very large parameter counts while still remaining efficient. However,

**[3:26](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=206s)** architectures come with a cost and that cost is the communication payload. This is a simple example of the Deepseek V3 model, arguably the model that made MOE models popular. That model consists of about 256 experts. And when a token arrives to the model, a router dispatches that token to only nine experts that are most relevant to that token. The experts compute, send the results back to the router and then the the results are combined and the output token comes out to the user. The builders of the Deepseek V3 model estimated that the communication payload of that process that is known as the dispatch and combine process can be up

**[4:15](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=255s)** to 20 megabytes per single token which is a lot. But when you deploy these models with agentic harnesses and in agentic workloads, you're actually iterating between reasoning calls, tool calls followed by reasoning calls followed by tool calls up to a 100 turns sometimes per request. With each turn, you're compounding the context of the prior turn, adding it onto the current turn, reaching context lengths of about a 100,000 tokens, and generating up to 15 times more tokens than traditional chat uh uh AI use cases. So you add that all up and when you're deploying these models, most CSPs and infant service providers, they spread

**[5:05](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=305s)** these models across a large number of GPUs to increase concurrencies. So now each request can have up to thousands of requests in the single batch. requests have hundreds of turns, 100,000 tokens of context and very quickly interGPU connections between the GPU becomes the main and primary bottleneck for deploying these models in production. And this is exactly the reason why we co-designed the GB300 NVL72. You see the image of the rack. It consists of 18 compute trays. Each tray has four GPUs. totaling 72 GPUs, all connected with a copper cable spine via nine NVLink switch trays, allowing each GPU in the

**[5:56](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=356s)** rack to talk to any other GPU at 1,800 gigabytes per second, totaling 130 terabytes per second of total all-to-all bandwidth across the the rack, eliminating the bottlenecks that the dispatch and combined process of ME models generate. Now, if we compare that to the prior architecture of Hopper, which only connected eight GPUs together in a single node, if you wanted to scale out to 72 GPUs, you would have to connect these nodes together via Ethernet at 100 gigabyte per second. That's almost 5% of the bandwidth of the GB300 NBL72 rack. And that's the benefit of co-designing

**[6:45](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=405s)** compute and networking together to serve some of the challenges of models. But hardware is just part of Nvidia's codeesign strategy. Software is also a very critical part of that strategy. And at Nvidia, we tend to think of the infant software stack as comprising three layers. At the top layer, we have the production operation. That layer is responsible for deploying models reliably and scalably in production. Underneath that layer comes the application layer. The application layer is responsible for ensuring that the GPU itself is operating at its maximum capability in terms of performance and communication capability. At the very bottom we have the infrastructure access

**[7:35](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=455s)** layer. This is our infamous CUDA library that many of you are familiar with. Our infrastructure access layer is designed to help developers interact with our hardware, interact at a very low level without necessarily needing to learn and understand all of the device instruction set of that hardware. And the interesting thing about the NVIDIA software stack is that we integrate all of these three layers of the stack allowing you to activate optimizations from any layer of the stack and compound them together. So you can take for example optimizations in the top layer in Dynamo like disagregated serving and KV cache aware routing layer that on top of optimizations in the middle layer in tensor RTLM kernel optimization kernel

**[8:24](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=504s)** fusion speculative decode and combine that with communication optimizations at the nixel layer for a mixture of experts and you can get optimizations more than the sum of the parts of the each individual optimization if you had activated it alone. Another important pillar of Nvidia's infant software stack is that we work with third-party open-source projects as if they were first class citizens of the NVIDIA software stack. So we collaborate very very closely with projects like VLM, SG Lang and make sure that we are co-inovating with them. We have joint road maps. We open PRs. We give them access to our latest generation of hardware to make sure that they're

**[9:12](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=552s)** building software that runs optimally on Nvidia. So what's the benefit of all of this? If you are a developer or an engineer deploying these frontier open-source models today in production in Agentic workloads, by moving from NVIDIA's prior generation Hopper to our GB300 NVL72, you can unlock more than 20 times more performance on Agentic workloads. This is on silicon performance. This is not simulated data. This is not static data. This is real agentic workloads. This is actually a very new benchmark that was just published yesterday by semi analysis agent X. You might have heard

**[10:00](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=600s)** of it in the keynote today. And the benefit of this is it includes all the different terms that we talked about. It includes large context. It simulates the endtoend agentic workload loop. uh so you can get a better understanding across the entire interactivity rate the types of benefits that you can see by moving from an 8-way GPU node to a 72 GPU full rack scale design like GB300 NVL72 and if you go to the semi analysis agentex website you can see multiple more models GLM and many more where you can benchmark that performance now I know what some of you are saying some of you are saying well But Omar, Blackwell costs more to rent than Hopper.

**[10:48](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=648s)** That's true. But even accounting for that incremental cost, Blackwell can deliver tokens at tenth of the cost of Hopper because of the co code co-design and because of the higher performance that you get. So even if you're paying a little bit more for rental cost of Blackwell, you can still generate tokens at a tenth of the cost, which means you can return some of that value to your end users or return it to your investors or, you know, use it to deploy larger, more intelligent models uh on your infrastructure. As I mentioned, we were here last year talking to you about NVIDIA Dynamo. It's the operating system of AI factories. It includes capabilities like disagregated serving and KV cache aware routing topology aware scaling. We don't have time to go into all of these but in our

**[11:38](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=698s)** benchmarks we've seen that deploying Dynamo even on the same hardware on the same Blackwell GPUs can unlock up to 7x more performance from your deployment. And today we're excited to share that Rayerve now integrates with Nvidia Dynamo. So you can leverage components from NVIDIA Dynamo like the KV uh indexer and integrate that directly into your Ray environment. So you can continue to use your your investments in Ray across the request plane, the control plane, the data plane and then bring in the benefits of KB aware routing to avoid KB cache recmp computation which is very common in aentic workloads. We're also uh excited to share that Ry now adds NVLink group awareness in its

**[12:28](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=748s)** placement uh group policies so it can recognize that you're trying to set up or spin up GPUs in an NVLink uh domain and place these nodes in the same rack such that you get the benefit of the 130 terabytes per second instead of spreading your GPUs across multiple racks that then have to communicate with scale out networking um or lower bandwidth scaleout networking. So, we're excited about this announcement. There's a couple of blogs as well that that were just published. Uh we invite you to have a look at them on the Rayerve uh website. As I said at the beginning, I feel very lucky to have the opportunity to have a front row seat as Nvidia brings new accelerated computing platforms to the market. Vera Rubin is in full production

**[13:17](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=797s)** being deployed across CSPs and Nvidia partners. Vera Rubin is not a GPU. It is not a rack. It is a full pod that consists of seven different chips across CPUs, GPUs, scaleout networking, scale up networking, data processing units, and low latency inference with our latest Grock LPX chips. In the semi analysis agent X benchmarks, Vera Rubin demonstrated on silicon that it can deliver up to 30x more performance on top of what Blackwell brings. We're very excited about Vera Rubin and I look forward to coming back here next year and sharing with you a little bit more about that platform and what it unlocks. With that, thank you very much for your time and feel free to

**[14:05](https://www.youtube.com/watch?v=FCtTk4H8ynM&t=845s)** bring your questions uh offline.
