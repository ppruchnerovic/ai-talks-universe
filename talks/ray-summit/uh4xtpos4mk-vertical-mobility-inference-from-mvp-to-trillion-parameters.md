---
id: uh4xtpos4mk
title: "Vertical Mobility: Inference from MVP to Trillion Parameters | CoreWeave | Ray Summit 2026"
slug: vertical-mobility-inference-from-mvp-to-trillion-parameters
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 12
published_at: 2026-09-17T16:01:53Z
video_id: uh4xtpos4mk
url: https://www.youtube.com/watch?v=uh4xtpos4mk
youtube_url: https://www.youtube.com/watch?v=uh4xtpos4mk
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Vertical Mobility: Inference from MVP to Trillion Parameters | CoreWeave | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=uh4xtpos4mk) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

The future of AI inference is not one-size-fits-all.

At Ray Summit 2026, Sitanshu Gupta, Director of Engineering for Inference Services at CoreWeave, explores a multi-tiered architecture that supports the full AI lifecycle, from rapid pay-per-token experimentation to dedicated, SLO-bound production and extreme-scale self-managed deployments, with lessons from CoreWeave's inference stack as performance, cost, and control requirements evolve.

You'll leave with a model for scaling an inference platform from MVP to trillion-parameter workloads.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,973 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=uh4xtpos4mk&t=6s)** Hi folks. I hope you all had a good lunch. I'm going to be talking about vertical mobility. It's a funny name that we gave. But mostly it's about how we are setting up the platform over here for inference in Corvi. A little bit about me. I have a little little bit more than 17 years of experience largely spanning in the infra space for machine learning inference and training. And before Corvi, I was at Anapurna Labs in AWS and before that at SambaNova and Oracle. Most of our work right now on the infant stack revolves around the engines and performance optimizations, utilization on that, and making sure that the reliability and uptimes are super high for the customers. At a high level, few things that I'll be

**[0:53](https://www.youtube.com/watch?v=uh4xtpos4mk&t=53s)** covering today are giving you an overview of the consumption models and the product. Giving a high level overview of how the platform looks like and how it is scaling, how it's scalable. And what are the key features and performance that mostly attest to the customers. Before I jump into the consumption models and product, let's look at how what are the different types of workload profiles. Agent tech is one of the most popular ones today. It is one of the biggest one biggest work profiles today. Which is quite a bit latency sensitive since agents really do not have any time between each other. A lot of high KV cash reuse because a lot of prompt is common for the same user and across different users in the

**[1:43](https://www.youtube.com/watch?v=uh4xtpos4mk&t=103s)** same organization. Turn off tool calling that happens over there. So there's a lot of processing on the CPUs also for that. And a lot of bursty traffic. Chat is another form which is kind of like agent tech, but there are longer later longer delays in between turns over there. So, similarly multi-turn, but longer delays. So, um it's not so heavy on the loop side, but again bursty, and there are no tool calls typically on that. Batch is another one, which is uh pretty important from the point of view of heavy utilization of the underlying hardware, because all the batch workloads come with uh super high SLAs. Hey, take 24 hours, it take 48 hours, take 72 hours to process these millions and billions of jobs that we have. Uh and even if they fail, it doesn't matter. Restart and uh resume from

**[2:32](https://www.youtube.com/watch?v=uh4xtpos4mk&t=152s)** there. And real-time voice and uh image, those are actually super low ultra-low latency workload profiles, where uh it really matters where your customer centers are, where their clients are, and where the gateways are actually being set up. So, keeping in mind these uh four different types of workload profiles, um the different offerings that we have on the product side at CoreWeave are serverless, inference dedicated inference, and inference on CKS. Let me go one by one from left to right. Serverless is where, as a customer, you do not have to make any of the deployments yourself. You get the models pre-deployed. You can imagine it's like a buffet. Uh you get what we serve, but you take as much as you want from that. Um there is a noisy neighbor problem in

**[3:19](https://www.youtube.com/watch?v=uh4xtpos4mk&t=199s)** that, just like a buffet. If everyone likes the same food, if everyone likes the likes to go after the same food item, then there will be a little less of that. Um you you pay as you go on the on serverless. Dedicated is the one where, as a customer, you are basically asking us to guarantee a specific amount of uh GPUs for you in the cluster. And then you manage your own deployments yourself. We give you the recipes, we give you our performance profiles, and if you want to tweak it further, we can help you with that. But, ultimately you own the the deployments. Uh but it uses the underlying inference serving stack that we have, which we have battle tested. And inference on CKS is where you are basically not having much of that inference stack, only the Kubernetes framework to orchestrate

**[4:07](https://www.youtube.com/watch?v=uh4xtpos4mk&t=247s)** the cluster over there. Uh inference on CKS is the one which customers rarely use, but very few customers wanted because they do not want anyone else to have access to their model specifics. Um let me take a few minutes to walk over the platform that we have and how the workflow over here is. And I'll take maybe one example from both the serverless and the dedicated side. Um so you can see like when the client start, they will start and they will hit the gateway. And the gateway will go into our control plane for authentication, to check if there are any rate limits that are set and if you're violating them, usage, and then billing, etc. also gets kicked in over here. Uh based on from that, we decide if it's going to be going through the serverless

**[4:54](https://www.youtube.com/watch?v=uh4xtpos4mk&t=294s)** or the dedicated side. Serverless, the billing will be paper token. Dedicated, the billing would be per the GPU by hour. Uh and dedicated is going to be single tenant uh irrespective of how the customer has treated it their end. Uh then comes the router, which is a super critical piece, especially for the two workload profiles that we saw in the beginning, the agentic and chat, which are super super prefill heavy. So, cache locality becomes very important and the ability to reuse cache is extremely important. Because of that, routing across different replicas for cache cache reuse becomes super important. Uh under that, you have prefill and decode. There are different setups. You can either have them happen on the same hardware or you can disaggregate them for better utilization.

**[5:43](https://www.youtube.com/watch?v=uh4xtpos4mk&t=343s)** Uh but again, that utilization kicks in only that kicks in when your prefills are super long and you don't want to delay the decodes just because the pre-fill is consuming the hardware. Uh what we use as engines underlying are vLLM, S L ang, and TensorRT LLM. And across all these different pieces of hardware. Now, let me walk you through a quick example over here. Request comes in, it hits the gateway, uh goes for billing for serverless. It picks a particular model. That model is body-based routed over here. So, based on the model name, it will figure out which particular deployment to go and pick up. Based on that deployment, if it has the cache aware routing already in, it will first try to figure out uh if the cache is available somewhere or not. Uh if yes, it'll try to route it to those particular replicas. Otherwise, it'll

**[6:30](https://www.youtube.com/watch?v=uh4xtpos4mk&t=390s)** find a new one. Um period disagg depends on how it was actually configured uh from our side as a core view for the serverless case. Uh and then goes in and hits the underlying hardware. Uh on the dedicated side, it's slightly different because the configuration is managed by you as the customer yourself. Um Uh you will hit will hit your own private gateway. If you have your own private connectivity, it'll come through that. Right? And then um most likely in most of the customer cases we see that cache reuse is like super super high, especially in agentic cases where cache reuse runs into like 95% plus, chat use cases where it runs into 70 75% plus. Um and then depending on the configuration, some customers have pre-fill disagg pre-fill and decode

**[7:18](https://www.youtube.com/watch?v=uh4xtpos4mk&t=438s)** disaggregated, and some do not. They have they have been running it on the same particular hardware. Um one important piece that I kind of skipped over, uh but uh which typically happens in the beginning, is um the the cluster set up over here. So, the control plane actually helps us out with that. Uh with the all the deployments and the canary rollouts uh over here. And for observability, we have a separate stack running all across, which is basically measuring all of this and throwing it on Grafana dashboards for for all the customers and even for serverless. Uh like I mentioned, the main main engines that we are actually focused on right right now are vLLM, S Chat Lang, and TensorRT-LLM because any of these models that new models that come in, they are very well supported on these

**[8:07](https://www.youtube.com/watch?v=uh4xtpos4mk&t=487s)** three different engines. And going forward as well, we see the same thing and a lot of open source contribution over here, and we also contribute ton of fixes back upstream. Uh coming to performance, something that is super close to my heart. Uh like we talked about cache, uh so that is one of the levers over here, and in the next slide, I will be talking about the other four levers. But cache is one of the biggest things, especially if you've seen the way models are the model economics work. Uh the token pricing for cache tokens is super super low because you do it basically don't want to be spending any compute cycles on that. Uh so it's important to first have the prefill do this expensive part at least once, and then you store it, and then you have proper routing towards it, so

**[8:54](https://www.youtube.com/watch?v=uh4xtpos4mk&t=534s)** that you have immense amount of reuse. Also, for cases like chat where the the latency between turns can be super long, you don't want that your cache keeps getting evicted. You want to store it. So, what you want to do is you actually want to offload it. And we use techniques like LM Cache or Moon Cake to offload it back to the storage devices. Um on top of caching, the other four levers that become super important are disaggregation, like we had discussed, especially in the cases where the workloads are super prefill heavy and where different prefills with little cache reuse, there you might really want to go in and disaggregate prefill and decode so that what those long pre-fills are not stalling decodes. Quantization becomes extremely important

**[9:43](https://www.youtube.com/watch?v=uh4xtpos4mk&t=583s)** because the smaller bit width that you use, the lesser memory space the model needs. You can actually deploy it on smaller number of hardware, lesser number of hardware and you do lose time to time you do lose some amount of accuracy on this, but there are there's enough work done on quantization to kind of revive this accuracy loss. Uh speculative decoding is becoming extremely common now. Most of the models come with their own speculators these days. So no specific training needed on that, but one interesting piece is that if you know that you have specific type of data then as a customer we do provide the service where you give us your data and we train the speculators specifically on your cases which drastically improves the acceptance length and ultimately the decode speed that you get is like

**[10:30](https://www.youtube.com/watch?v=uh4xtpos4mk&t=630s)** extremely extremely high. And lot of these parallelization knobs, your tensor pipeline expert etc. Those you have to continue to tune and then there are fixes that you keep making inside the engines to extract the performance from the hardware quite significantly. Uh one quick show over here. Since we started this particular team a couple of few months back there have been times when we have been number one on performance on both artificial analysis and open router. Uh we like to show both because artificial analysis is sort of a artificial workload and then open router is running a lot of real traffic. So models like Kimiko 6, Kimiko 27, MiniMax M3, GLM 52.

**[11:20](https://www.youtube.com/watch?v=uh4xtpos4mk&t=680s)** Uh we've had like extremely extremely high decode throughputs. And with that comes to the end and I I take some questions if there are. All right. Thank you so much, folks.
