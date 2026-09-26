---
id: h5hVWBPAP8A
title: "KV Cache and Long-Context Inference: Solutions for Inference at Scale | VAST Data | Ray Summit 2026"
slug: kv-cache-and-long-context-inference-solutions-for-inference
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 12
published_at: 2026-09-17T16:06:18Z
video_id: h5hVWBPAP8A
url: https://www.youtube.com/watch?v=h5hVWBPAP8A
youtube_url: https://www.youtube.com/watch?v=h5hVWBPAP8A
tags: []
topics: ["Inference, serving & GPU infra", "Prompting & context engineering"]
transcript: true
---

# KV Cache and Long-Context Inference: Solutions for Inference at Scale | VAST Data | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=h5hVWBPAP8A) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

As agentic AI drives ever-longer context windows, KV cache has become the new memory wall, dwarfing GPU HBM capacity and forcing costly recomputation on every session resume.

At Ray Summit 2026, Vaughn Stewart, VP of Systems Engineering at VAST Data, covers how offloading KV cache to VAST's flash-based storage with NVIDIA Dynamo and BlueField-4/CMX architecture eliminates that tax: 20x faster time to first token, 90 percent GPU time savings, and up to 64 percent lower three-year TCO.

You'll leave with sizing guidance, benchmark data, and a blueprint for scaling inference context without scaling GPU spend.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,842 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=6s)** All right, hopefully everybody can hear me. Um, thanks for joining our lightning session. Uh, my name is Von Stewart. I'm with Vast Data. We have a booth, just a couple of booths right behind you there if you want to follow up on any of the points that I'm going to share with you here. Um, we've got a lot of folks that can speak in greater detail today. Hey, I want to talk to you about uh the work we're doing uh both internally with our RD team but also across our partnerships with Nvidia, AMD and others around uh KV cache and the impact it has on long context inference. We are entering the next frontier of AI where models are no longer responding to single prompts. Agentic AI introduces multi-turned reason-based workflows that spawn multiple steps, tools, calling, and decision-making. As a result,

**[0:54](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=54s)** inference is no longer stateless. Agents must retain and reuse context across interactions sessions histories and even services. The context grows quickly as the sequences get longer and reasoning becomes more complex. In effect, KV cache is becoming a long lived memory and performance now depends on how efficiently we manage the KV cache and reuse this context. This shifts fundamentally how we build our infrastructure and what the new infrastructure should look like. The key problem with KV cache is it grows with the context length and the batch sizes that you work with. Assuming that we have the same model for inference in this example that I'm showing you here, this is for llama 405 billion parameter model. The cost of

**[1:44](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=104s)** computing the KV cache grows almost quadratically as the context length increases. As you can see, this increases the amount of burden that you have uh in terms of uh the longer context windows that your GPU has to work with, what they have to compute. And this is truly a case uh that we see with Agentic Workflows. What I'm going to show you in the next couple of slides is predominantly work that we're we're partnering with uh with Nvidia. But before I do, I just want to reiterate the point that we work across the entire stack with all of our partners whether we're talking about at the orchestration level, the core engine level, KV cache, or the actual the data transfer level. Currently, vast data is integrated at

**[2:34](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=154s)** the what you see on the slide here is the um uh is the context memory hierarchy here uh within within uh Nvidia um uh Nvidia's uh uh I'm having a brain fart here. Sorry. Nvidia stack. Uh we're currently integrated here at the the G3 tier. So your your G1 tier if you can't read the slide is is your GPU high bandwidth memory uh first tier of of cache. The second tier the G2 tier is actually the systems memory within the GPU server. We are integrated at the G3 tier here which is really for warm cache and reuse. Um uh and by the way this is the Dynamo stack. Sorry I had a little bit of a brain fart there. Um but as as the Dynamo stack evolves uh VAS uh VAS

**[3:24](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=204s)** R&D team will be uh VAS R&D team is currently working with Nvidia and we will be integrated into the the G4 tier. Um this will enable a full opaque life cycle management allowing the key value block manager to handle the G4 tier without exposing the underlying complexity of the rest of the system. In our current testing, we are showing performance of a 20x increase of time to first token. And when we looked at KV cache workloads and profiled it, the profile was clear. It's heavily readbased with very large blocks often measured in u meg megabytes range. Uh this gave us an opportunity. Uh by optimizing the key value block manager, we fundamentally changed the the the mass. We turn from slow IO inheavy processes of your GPU into high

**[4:16](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=256s)** throughput networkorbound data transfers. Essentially this means that the storage can scale with the network for this workload. The true value of VAS goes far beyond just raw speed or scale. It's about enterprise data services which allow us to manage the KV cache in the with the same rigor as any other sensitive enterprise data. Through our hypers scale file and object architecture, we're able to achieve worldclass data reduction. This is a massive win for AI scalability because the efficiency translates directly into more cycles for compute, which means you can support more users, hit higher cache rates, and maintain longer sessions. On the performance side, we've built an architecture for high-speed, low latency connections between your compute node and the data

**[5:04](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=304s)** stored using NFS over RDMA or TCP. As we move into the G4 tier, we will support S3 over RDMA to facilitate rapid offloading uh and retrieval. Ultimately, this will ensure your storage layer is fast enough to scale in lock step with your network. We've performed experimentations to see what performance we can get with the vast architecture. The results uh were done on two 100 Gbit Ethernet uh link network and we're certainly and we can certainly get to uh even a higher performance level with uh higher bandwidth network speeds. This is just a a test lab environment. Um but in our experiment we used the llama 3 40 45 billion parameter model with 128k context length on h8

**[5:53](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=353s)** h100 GPUs. The experiment checked how time how much time it takes to compute a prefill of 128k context compared to reading it from the vast kv cache solution. The results showed a 20x improvement in time to first token when fetching the KV cache from the VAS system compared to forcing the GPU to recalculate it. This speed up along with a 90% savings in GPU time demonstrate a massive gain in efficiency. I've provided some additional data here besides the simple charts that I showed on the prior slide so that you can see that u as the context length changes right you can kind of see the range of the impact of the KV cache uh around uh both reducing uh computational time but

**[6:43](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=403s)** also the GPU cost. I also have a second set of slide here looking at this data in a comparison of uh cost to recomputee u the same set of contexts versus pulling them and retrieving them from cache. Uh as you can see in this 100,000 GPU cluster scenario the savings over three years is roughly $66 million. In addition to performance and speed, we've also conducted an experiment to determine the data reduction ratio. Uh sometimes you may see it on a slide as an acronym DRR. Uh the data reduction ratio that we receive on the KV cache offload to vast data. We created a data set of 1.2 terabytes of KV cache which was a collection of several types of data including documents, code, chat

**[7:32](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=452s)** bots. We consistently found that the data reduction ratio of 1.4 to1 across each of these workloads. This 1.4 to1 efficiency has significant implications that span the entire life cycle and inference requests. It directly allows for extended user sessions, an increased number of users due to more capacity and leads to a higher cache hit rate, which in turn reduces latency and frees up more space for additional compute. Essentially, our storage efficiency is a key to maximizing the value of your AI infrastructure. Once the KV cache leaves the GPU, it continues. It contains sensitive user data and is vulnerable to manipulation or reverse engineering by attackers. It must be treated as enterprise storage or data requiring security and compliance.

**[8:21](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=501s)** Mandatory encryption is essential to meet regulatory frameworks like the EU AI act and mitigate prompt leakage for shared infrastructures. Multi-tenency security and clear isolation policies are paramount. We must also establish and enforce SLA driven retention periods for the context life cycle. So what we're bringing is is a complete what we believe at this time the most complete and comprehensive set of KBA caching capabilities both in terms of scale performance economics security and compliance. We're continuing to do additional work here uh with Nvidia on integrating on CMX which when you go back to the architecture now we'll introduce a new tier uh a tier 3.5 one that's comprised

**[9:12](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=552s)** of local storage on each GPU server. We will be deploying vast data cnode software onto bluefield for DPUs. This framework will allow each uh DGX server or HDX server to basically have their own storage controller on that server and we'll take the local storage of each and actually make it sharable to all nodes within a pod thus extending from a nodebased cache into a global cache uh at the local SSD level. So um uh K shared KV content if you context if you will. Um this will uh further increase cache hit ratios further driving down um the the uh capacity required to run your workloads or

**[10:01](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=601s)** probably more importantly providing more capacity so that you can further scale more uh more context and and more uh work. Wow, I am blowing through my time here. [laughter] Uh so this is my my last slide. Um so in short uh you know I'm trying to hit on these six key points here uh with regards to uh what vast data is providing in terms of KV caching. Uh so a lower time to first token uh as demonstrated in the one example I showed you there with the 20x acceleration. If you go to blogs.vastata.com vastata.com. You can read a number of articles that we have within this space that show you additional testing that we've done both within uh Nvidia and other partners like AMD. Um we want to enable an infinite uh context so that your sessions and your

**[10:52](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=652s)** users session states remain persistent longer allowing and enabling agentic AI uh and longunning um prompts. Uh we provide increased resilience so we can protect those prompts along with data encryption and observ observability obs observability um and and notifications and monitoring so we can meet your compliance and regulatory requirements. Um we also have a lot of flexibility. We are a software company. We're not a hardware company. So we provide you um heterogeneous hardware strategy whether you want to purchase from Nvidia, one of their HDX partners, Super Micro, Dell, whoever it may be. Uh and the bottom line is that every GPU second uh that we span uh that spans recmp computing that that every GPU second spent ah I had a finishing

**[11:44](https://www.youtube.com/watch?v=h5hVWBPAP8A&t=704s)** statement there. uh spent recmp computing the the KV cache uh that is already exists on the flash as a GPU second not generally [clears throat] uh not generating revenue for you as a GPU provider. So uh that's our summary. Um stop by our booth and let's uh let's extend this conversation.
