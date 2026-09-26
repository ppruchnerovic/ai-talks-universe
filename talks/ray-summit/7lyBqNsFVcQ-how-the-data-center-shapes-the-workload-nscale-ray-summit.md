---
id: 7lyBqNsFVcQ
title: "How the Data Center Shapes the Workload | Nscale | Ray Summit 2026"
slug: how-the-data-center-shapes-the-workload-nscale-ray-summit
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 12
published_at: 2026-09-17T16:07:44Z
video_id: 7lyBqNsFVcQ
url: https://www.youtube.com/watch?v=7lyBqNsFVcQ
youtube_url: https://www.youtube.com/watch?v=7lyBqNsFVcQ
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# How the Data Center Shapes the Workload | Nscale | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=7lyBqNsFVcQ) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Everyone talks about the software layer or the chips. Equally important is the control plane deciding which GPU a workload lands on, and when it's trustworthy enough to accept traffic.

At Ray Summit 2026, Oscar Savolainen, Senior Staff AI Engineer at Nscale, walks through Nscale's fleet manager as a state machine, from power-on and burn-in to Kubernetes admission: how silent stragglers are filtered out before a customer ever sees the node, and how InfiniBand and NVLink topology shape the units of scale Ray workloads actually run on.

You'll leave understanding how the data center itself shapes the workloads you run on it.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,170 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=6s)** Howdy all. Um, sorry for the delay. Yeah, today I'm going to be talking about how the data center shapes the workload. Uh, particularly about topology fabric, how we manage our large scale of our fleet of GPUs. My name is Oscar Savainan. I'm a senior staff AI engineer here at NScale. So, I'm not going to talk too much about this. This was covered in the keynote but obviously it's super exciting that nscale and any scale are going to coming coming together. Uh I will make the obligatory joke that yes nscale and any scale sound similar now they are similar. Uh so we're very excited about that. Um I like to think about multiode optimization kind of like GPU optimization because fundamentally it's the same thing. It's all about how data moves. Where does compute happen? Uh so

**[0:54](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=54s)** if you're optimizing your GPU, you need to think about memory hierarchy, about your compute cores. Uh similarly in multi-node jobs, you need to think about your topology, your fabric, your GPU, basically how does data move, where does the compute happen. I'm going to talk very quickly about CPU and GPU collocation. So and this refers to do you need your CPU nodes and your GPU nodes in the same DC. Um it's worth saying that in a GPU node there are some CPUs they they'll be responsible for things like scheduling the work on the GPU. Um and also if you're like running inferencing instances then uh they'll be like running the web server and they'll be scheduling the work and they'll offload all of the work the heavy computational work onto the GPUs like your matrix multiplications etc. However, there are

**[1:44](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=104s)** certain use cases where you want uh CPUs with a little bit more oomph, a little bit more power to them. uh for example like aentic RL loops if you have uh a CPU running and like a VM sandbox on top of it um typically you will want standalone CPU nodes for this and the question is should they be colllocated or not uh the question really comes down to one latency is latency a massive concern for you uh if your CPU nodes are in the hot path in terms of your AI workload then that can make sense and you want to minimize latency uh the other use case is if you have a strong like networking story. Um, for example, uh, you you want to minimize what's called north south traffic, like data your training data going over the internet flowing out of your your DC. Uh, you want to keep all of your traffic

**[2:33](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=153s)** as much as possible east west so that your training data kind of like stays inside the same data center. It's more of a security thing. Um, in which case collocation obviously makes a ton of sense. uh but there are certain use cases where it's less important if you don't have a networking story if you're not concerned about latency uh you can do like ahead of time pre-tokenization of your data set for example and your CPUs don't need to be colloccated in terms of networks um there's a couple probably the the best thing to know is that there's actually multiple physically distinct networks in your DC uh some of them you don't really need to think about there'll be like management networks there'll be sensor networks networks. Um, but the ones that on your hot path in terms of your workloads are the front end network and the back end

**[3:21](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=201s)** network. And so the front-end network is for things like sshing into your nodes, uploading code, dependencies, um, and as well it will do things like if you're running a multi-node job, uh, typically the handshake between the nodes before you get to the RDMA portion, uh, it does a handshake of a TCP that typically goes over the front end network as well as storage. So in your GPU nodes, you typically have some built-in storage like your NVMe, your RAM, and the way that that but you typically in a DC, you also have like standalone storage racks. These will be things like your model weights, um your training data. If you're doing KV cache offloading and in inferencing at like a sufficient hierarchy, then you can store your KV cache and the external storage

**[4:10](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=250s)** as well. That all goes over the front end. The front end is typically Ethernet. And just be aware that if your workloads are very front-end heavy that can cause congestion on your front end. So it's something to be aware of. Then we have the backend network. And the back end is optimized for a different use case. It's very much peer-to-peer uh RDMA between your GPUs and essentially takes a bunch of individual GPUs and turns them into like one giant supercomputer. This can also be Ethernet. Uh so stand rocky or RDMA over converged Ethernet. Uh that's really interesting because you can get to huge scale with Rocky. You can have something called multiplaner topology which is very interesting. It's essentially a bunch of distinct networks and they don't share a spine. It just lets you get to giant scale. Uh and then there's Infiniband and Envy link. And

**[4:58](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=298s)** probably the most important thing to know about this is that you typically have a Rocky back end or an Infiniband back end and then you also have Envy link. So you can have Rocky and Envy link, you can have Infiniband and Envy link. In terms of Infiniband, uh, one cool thing to know is that this was developed by a company called Melanox originally and I think about eight years ago, Melanox was inquired by Nvidia. Uh and so there's been a ton of optimizations for like AI workloads and probably the main takeaway is that it's a hierarchical topology and that means that within a scale unit and this is according to the Nvidia reference architecture uh within a scale unit you will get slightly faster communication bandwidth than across scale units. This is just because otherwise you have to do an extra hop over the spine. Uh versus

**[5:47](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=347s)** within a scale unit it's just one it's just one jump over the over the nearest switch. Basically what that means is that if you're renting compute capacity from somewhere you should ask if it's infiniband you should ask like hey is this within the same scale unit or not ideally it would be within the same scale unit you get slightly faster communication bandwidth. Envy link is probably the single most interesting thing or the most impactful thing that's happened in the latest generation. So, NVL link is special because it's the fastest peer-to-peer communication bandwidth that you can get between GPUs, uh, at least Nvidia. Um, and that's been really massive for shaping AI workloads because you would typically do your tensor parallelism, your expert parallelism, anything where there's a lot of data moving around, uh,

**[6:34](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=394s)** you would keep that on a single node and then anything that's less data like pipeline parallelism, data parallelism, that would be across your relatively slower fabric, your Infiniband, your Rocky. Um however that that constraint is kind of going away now. So with the GB200s, the GB300s, you have NVL72 as the the previous talker mentioned 18 compute trays. A giant NV switch goes on the back of the rack and that with four nodes per uh four GPUs per node that gets you to 72. Um and there's more in the Nvidia road map. We're expecting 576. So eight racks worth of NVLink domain which is actually larger than a scale unit. So I'll be curious to see how the um how the reference architecture evolves from that. In terms of what impact this is going to

**[7:24](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=444s)** have on AI workloads like I think the models are just going to keep getting bigger. Uh things like expert parallelism tensor parallelism you're no longer limited to that um that constraint of single node being a single node envy link domain. Uh and that's been true since of amper hopper blackwell but no longer. So that's pretty nice foundational model training. uh that's just generally going to accelerate because to the degree that communication is your bottleneck within a single rack. Um now it's that much faster. RL weight transfer reinforcement learning is really interesting. The the guy from two talks ago I think at Laya um labs he he mentioned this and it's it's super relevant. Um so as you mentioned like one of the things that you have when you do RL is at especially at scale is that you have your training

**[8:12](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=492s)** instances and you have your inference instances and transferring the weight across those two can create a bottleneck and the way the industry has gotten over that bottleneck is by doing what's called off policy training and as was mentioned uh the more off policy you go it can cause training instabilities and so having faster communication bandwidth at least within a single NVLink domain whether that's rack multiack um that gives this interesting opportunity to potentially grow your models because you can transfer the weights that much quicker or um stay more on policy for the same model size and so stabilize your training. So it's quite interesting. Uh switches are now computers. I don't know if you got the memo, but yeah, that's that's happening now. Um, and this is because traditionally speaking,

**[9:00](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=540s)** if you were doing like an all reduce or like you were syncing your gradients, for example, the way this would work is that you'd have a node, it would speak to the switch, it would broadcast it down to other nodes, uh, they do some kind of aggregation back up to the switch, back down to the nodes. And what they realized, and this is now true of Infiniband, uh, but also NV switch, um, you can now do some computation inside the switches. It's called sharp and what's cool about that is that basically the nodes they talk to the switch the aggregation happens there it comes back down. So if you are like renting compute and you're doing multiode workloads it's worth asking um hey do you guys have sharp enabled on your switches if so like it's it's worth asking about this. I'm going to switch gears a little bit

**[9:47](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=587s)** and I'm going to talk about nscale control center. So this is something I've been working on at nscale for like the last year. It's basically how we manage our giant fleet of GPUs. Uh everything from inventory to proactive health checks and automatic remediations. And kind of a big part of this is that as you're bringing up like a DC, you need to validate everything like everything needs to be fully validated. And you know, it's it's kind of like perhaps obvious what we do is that we stress the GPUs heavily for multi-day workloads, making sure that any stragglers are weeded out, if they're going to surface XID errors, if they're going to surface like remapping issues. Uh so we stress the GPUs, CPU nodes, uh fabric as well, backend, front end, uh management, uh make sure that no ports

**[10:36](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=636s)** are flapping, making sure that all the cables are plugged in correctly because apparently that's one of the hardest uh problems to solve. um as well as storage uh so just testing everything all of the individual components but also end to end uh workloads because at the end of the day you can do individual checks but you actually do have to run real production workloads on these and this serves two purposes which are quite nice. The first one is uh just general endto-end validation. It kind of like proves that everything works and we're we're proud to say that we have something called exemplar status. This is what Nvidia grants when they show that like you can train like half a dozen different kinds of LLMs and you get really the top performance that's expected from you know the compute. Um so that's something we've worked hard on and we're we're quite proud of that. The

**[11:23](https://www.youtube.com/watch?v=7lyBqNsFVcQ&t=683s)** other thing that this does is that typically when you're dealing with really state-of-the-art compute let's say GB300s and soon Vera Rubins uh the the defaults aren't always optimal. Uh it could be nickel environmental variables. It could be PCIe configurations. Uh it could be some topology aware Linux service that's in your in your Abuntu images. Um and so we we discover all of this as we're doing endto-end validation and we get to bake that all into like our kind of like cloud. So whether that's a private customer, whether that's like the public cloud, it all gets baked in. So that's really cool. And uh thank you. Got three minutes left. Whoa. >> [applause]
