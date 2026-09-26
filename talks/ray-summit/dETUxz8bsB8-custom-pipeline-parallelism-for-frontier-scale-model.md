---
id: dETUxz8bsB8
title: "Custom Pipeline Parallelism for Frontier-Scale Model Serving | Apple | Ray Summit 2026"
slug: custom-pipeline-parallelism-for-frontier-scale-model
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 22
published_at: 2026-09-17T16:06:58Z
video_id: dETUxz8bsB8
url: https://www.youtube.com/watch?v=dETUxz8bsB8
youtube_url: https://www.youtube.com/watch?v=dETUxz8bsB8
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Custom Pipeline Parallelism for Frontier-Scale Model Serving | Apple | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=dETUxz8bsB8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Serving frontier-scale mixture-of-experts models at low latency requires cross-node pipeline parallelism, but vLLM's compiled-DAG approach deadlocks beyond two stages, and the safe workaround leaves half the GPUs idle.

At Ray Summit 2026, Abin Shahab and Michael Lee from Apple show how they turned Ray's single-threaded FIFO actor mailboxes into the pipeline scheduler itself, bypassing compiled DAGs, then cut two hidden CPU bottlenecks to reach up to 1.5x throughput.

You'll leave able to diagnose these failures and rebuild fast pipeline parallelism on Ray and vLLM.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*3,088 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=dETUxz8bsB8&t=5s)** Please give a warm welcome to Michael Lee and Aven Shahab from Apple. Hello everyone. Uh my name is Michael and this is my colleague Abin. We are from the machine learning teams at Apple. Today we want to share how we implemented custom pipeline parallelism in VLRM for Frontier model. Uh let's dive in. So let me start with uh what the parallel track transformer or PTT actually is. So because it's one of the the key technologies powering our foundation model, the idea is that you

**[0:52](https://www.youtube.com/watch?v=dETUxz8bsB8&t=52s)** take a standard transformer and short it into tracks. Each track is basically an independent transformer living on its own on GPU. To see why that matters, think about tensor parallelism. There sharding cost you two or reduces on every layer. One for attention, one for the feed forward. So on L layer model, that's two L collectives and the traffic is large and expensive. um parallel tracks go straight at the problem and the track runs independently and they only join at single or reduce every D layers. Uh so instead of two L you get L over D and in our benchmarks that cuts collective communication a lot while barely moving model quality. So then our job was to map the architecture onto

**[1:40](https://www.youtube.com/watch?v=dETUxz8bsB8&t=100s)** what VLM already already gives us. Um tracks map onto the tensor parallel axis. Um parallel stages map on onto the pipeline parallel axis. So and that means no new communicator because the tracks just reuse VLM's existing nickel communicator. So so now um here's the problem. Um, VLM assumes your model is one sequential stack with one single hidden state flowing from top to bottom. Um, and that assumption is baked into um, everywhere. The scheduler, the executor, all of it. But the PTT model, it's a fundamentally a different shape. Um, it's many tracks run running side by side merging only every D layers. Um, so so these two things are just not equal. So the hard part here isn't the math,

**[2:29](https://www.youtube.com/watch?v=dETUxz8bsB8&t=149s)** it's the plumbing. So we want to serve this architecture at scale and get all of the VLMs serving machinery for free without forking the engine and maintaining our own diverging copy forever. So our answer is simple. We build a plug-in uh taking advantage of the VLM plug-in system. So the PTT model um registers itself uh into the serving frameworks model registry and the VM core stays completely unmodified. So the scheduler, the page page KV cache, continuous batching um and the chart completion HTTP API all of it works exactly as shipped. Um so this is great because there's no engine for there's no ongoing merchant tags. We pick upstream improvements with almost no work on our side. So now let's trace one request end to end. Ray owns the GPU cluster. Um our

**[3:21](https://www.youtube.com/watch?v=dETUxz8bsB8&t=201s)** serving layer exposes the HTTP API that hits VL and V1 runner. Uh the plug-in supplies the actual model through the registry and from there uh the request request fence out across N tracks running in parallel and those tracks synchronize every D layers. So now the division of labor is pretty clean. VLM runs inference. The plug-in supplies the model and Ray places and scales the workers. Everything writes on VL and V1's async LM which we currently are upgrading to the V2. Now know that there's nothing custom in the hot serving path. So so now um being correct isn't enough. The fast path have to stay fast. So three things get us there. Now consider one of the tracks on one GPU. Uh first we have one grouped gem. Uh all

**[4:11](https://www.youtube.com/watch?v=dETUxz8bsB8&t=251s)** the experts get computed in a single batched map not a Python loop. Second uh one attention call all the tracks fuse STPA into a single multi head attention and third sharded load. The weights are pre-sharted per track and per stage. So each GPU only loads its own slice under the hood. Uh that's VLM's fuse with experts replicated. We use cutless group jam on hopper and blockwell and runtime patches that keeps whole um fuse inside a single cuda graph replace even when the concurrency is high. So now finally scale race serve gives us one placement group that spends the whole deployment um combine with combine that with tight integration into Apple's accelerated

**[4:58](https://www.youtube.com/watch?v=dETUxz8bsB8&t=298s)** compute platform scaling out becomes a config change instead of new code. Our pipeline stages um live on separate nodes and they pass activations node to node with send and receive over ray remote calls. Then when traffic grows uh ray just autoscales more nodes into the group. So uh but getting there um took some work. Uh Ray's com compiled DAG uh kept hanging on our pipeline execution. So we ended up uh writing a custom Ray distributed executor to dispatch the pipeline workload ourselves. and Abin's going to walk you through that debugging journey. >> Thank you, Michael. All right. So, um a little bit of recap. So, the model is large enough where we

**[5:46](https://www.youtube.com/watch?v=dETUxz8bsB8&t=346s)** need to shard it into multiple hosts. In this diagram, we're sharding the model and four into four hosts. And let's say each of the four hosts have eight GPUs each. And the naive way to shard it is 32-way tensor parallelism. So again, as Michael said, um you're basically for this at every inference step, for every token that the model returns you, for every layer, you're doing two synchronizations across all 32 GPUs. So, so it it's like this like if these this was like uh 32 chefs cooking uh a recipe, you're basically telling them cut all the onions together at the same

**[6:34](https://www.youtube.com/watch?v=dETUxz8bsB8&t=394s)** time and tell each other did you cut your onions? Did you cut your onions? All 32 ways. So that's the naive way. So what we pay we basically pay the cost of throughput there. So the better way that we chose um is P pipeline parallelism. This also should be pretty well known by the audience here. So what we do here is that we keep the tensor parallelism inside the nodes. So inside the nodes it's nylink. Um it's very fast. So it is fine to do those per layer synchronizations there. And then each node basically will send its output its activations to the next node. And that part does not require a 32-way synchronization.

**[7:22](https://www.youtube.com/watch?v=dETUxz8bsB8&t=442s)** So here we call these stages. So here this diagram is showing four stages. Stage zero sends to stage one. Stage one sends to stage two. Stage one, stage two sends to stage three. Um the re the reason I mentioned stages is most of our issues and how we fix things really involves pipeline stages. So what issues did we encounter? uh first was that the so we used VLM for this particular problem and then it uses ray underneath and ray's compile tags gave us some heartache. The next issue we had was um after solving the compile tag issue, we saw that there's CPU uh trans CPU

**[8:11](https://www.youtube.com/watch?v=dETUxz8bsB8&t=491s)** transfers, data transfers that are holding up GPU data transfers and slowing things down. And then the next thing we ran into after solving this problem was that we were introducing an extra CPU GPU synchronization. So I'm going to talk about all three of these problems. First is the ray compile DAG. So the way pipeline parallelism works in VLM is that there is this engine core which is the main driver of VLM's orchestration which is basically setting up how each stage is going to talk to the next stage and then ultimately that setup path is what's used by each of the um B the input that goes in and that's what generates the output. So the engine core sets up this

**[9:02](https://www.youtube.com/watch?v=dETUxz8bsB8&t=542s)** um uh ray compile DAG uh using this dox tasks loop. So this loop is a single threaded loop uh over a ray compile DAG and what it does underneath is set up a tensor accelerator channel um over or a torch tensor accelerated channel over nickel to send those activation. So in theory is it's very very fast because it's sending the activation from one pipeline stage to the next pipeline stage over Nvidia's extremely fast nickel. However, what happens here is that this is a single threaded loop and we what we experienced was deadlocks. So um the outwork outside experience that we had

**[9:50](https://www.youtube.com/watch?v=dETUxz8bsB8&t=590s)** here was that uh we deploy the model and it comes up fine health checks run fine and then in the first inference sometimes we will basically get a deadlock it will just hang and it will not return to us. So why the first is inference? Looking inside it, we saw that there's this lazy DAG compile, the RAID DAG compilation to set up these nickel channels over multiple stages happens at that first inference. And then once that when that is happening, um the expectation is that all the messages that are going and coming are in order. And it is possible that that doesn't end up happening where you have this kind of a cyclic loop of stages. One stage is waiting a stage is ended

**[10:40](https://www.youtube.com/watch?v=dETUxz8bsB8&t=640s)** ending up waiting for its own output and therefore a deadlock. So the solution once we looked into it was simple. It's basically using Ray's own actor uh dispatch mechanism. So when you actually dispatch a message or a method to or invoke a method on an actor, Ray will actually send it to that actor's mailbox so to speak or queue and then it will get executed in a FIFO manner by that actor. So we just took advantage of that fact. So we um had the executor um um send these uh kind of ray execute so or VLM execute model invocations as

**[11:29](https://www.youtube.com/watch?v=dETUxz8bsB8&t=689s)** actor exe invocations. And so each stage which is a worker would be basically an actor that is invoking these execute models. And then it it would be used underneath it would use this torch uh send and torch receive uh the distributed torch send and torch receive to um send its activations and then the receiver side would get the activation using torch receive. So uh yeah so the next slide talks about that. So we're basically underneath banking on torches send and receive. Um so how did this actually solve it? So when um we saw that in our in our code basically we override um VLM's um exe execute ray executor and we have a

**[12:18](https://www.youtube.com/watch?v=dETUxz8bsB8&t=738s)** custom ray executor that basically will um send the the torch send and or the execute models to u to to make the reactor mailbox uh send and receive work. So this solves the the ray compile DAG um um deadlock issue but then that didn't solve all that basically enabled pipeline parallelism where we needed to so we could spread the model into hardware that we had and basically unlock a lot of use cases. Um however we ran into the next problem which is that our throughput was not very high. Um so we saw that the actual activation by profiling this we saw that the act

**[13:06](https://www.youtube.com/watch?v=dETUxz8bsB8&t=786s)** actual activation data was being sent in microsconds over nickel but the metadata the data about the shape of the activation data needed to be sent from one stage to the next stage so that the next stage knows what to do with this activation data. So that day metadata was being sent over um CPU with four glue calls. So it's basically the way it works is glue will first sends the the size of the metadata and then it will actually send the actual metadata and then on the receiver side glue will receive the size of the metadata and then it will actually um get the actual metadata and unpickle it. So these end

**[13:57](https://www.youtube.com/watch?v=dETUxz8bsB8&t=837s)** up costing us um according to our profiles between like 70 milliseconds to uh a tail latency of 2 seconds. So given that the actual nickel transfer was extremely fast, we were basically paying the cost of this very very slow CPU transfer. Um so how do we how did we actually solve that? So the way to solve this is a computer science pattern is that when something is too costly, we we cache it. So is there a way to cache this tensor metadata? So turns out there is the tensor metadata depends on the dimension of it

**[14:48](https://www.youtube.com/watch?v=dETUxz8bsB8&t=888s)** depends on the actual bat size or the input token size that is coming in and given that this is this was running in CUDA compiled mode we had these very set CUDA graph capture sizes. So the input tokens would only be one of the set CUDA graph capture sizes 32 128 or so on. So we created a table on the sender and the receiver side that had the uh tensor metadata for each CUDA capture size that we supported. And now what did we need to send from a sender to a receiver? It's the index of this table. So at each stage uh the sender needs to

**[15:39](https://www.youtube.com/watch?v=dETUxz8bsB8&t=939s)** figure out okay what is my bat size I'm sending I'm just going to send that particular size in index the index to that size table and the nickel the that size index we can send over nickel because it's it's also extremely small. Um so and now it's being transferred in microsconds from oops sorry um it got transferred in microsconds from one stage to another. So we got rid of that bottleneck. So after we fixed this bottleneck we felt pretty smart that okay we've solved all the problems here but turns out that was not true. So the throughput is still slow. So and looking at the profile we see another 20 millisecond uh blockage somewhere. So we

**[16:29](https://www.youtube.com/watch?v=dETUxz8bsB8&t=989s)** had like 70 to two uh 70 milliseconds to 2 second blockers. Now we have a 2 millisec 20 milliseconds blocker which is better but it still shows up as a as a gap between the the extremely fast GPU uh nickel GPU to GPU nickel transfers. So the root cause of this was that um when we are reading the index on the receiver side we're what we are doing is we're saying okay there's this GPU tensor that's being sent to us the index tensor and we call item on it dot item and so dot item tell gives us basically the actual value into the CPU it also call it does it actually will copy that

**[17:18](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1038s)** data data from the GPU to CPU and when it's co doing the copy it is also causing a CUDA synchronize which means that it it stops the GPU right there and says give me like um stop and give me your output. So and if that stream happens to have other things in it also drains all of that. So we basically by by doing this kind of stopping by putting a traffic cop in front of nickel we basically slow it down. So the solution for this was again how can we avoid this. So the way to avoid this was we speculate how can we guess like what is going to

**[18:07](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1087s)** be the bat size or the token size of the the input tokens that are coming in. Turns out the VLMuler already gives us this information. Um so I forget the exact it's like token uh token size um something. So so that's the that uh if we have that information from theuler we already know that what is going to be the number of tokens sent to us for this particular batch we're running in cudraph so it has to fit in one of these cudggraph capture sizes so what we do is a very simple fitting in so we look for the next cudraph size that is larger than this to find the fit and then that's our that's basically

**[18:57](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1137s)** that um nickel index size that we were looking for. Um so with that we are able to now speculate the tensor metadata and correctly find correctly guess and so we don't need to look up the tensor metadata and cause a GPU CPU synchronization. um we keep we kept the GPUCP synchronization as sort of a fallback in case we don't have the scheduleuler output then we can use that. So now for the kind of the combined effect of this. So we started off with uh TP32 here. We benchmarked in TP16 to kind of keep the hardware the same. Um and in that benchmarked um the we basically started at these kind of very

**[19:45](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1185s)** low generation token throughput. So this is the throughput of the tokens that you're getting back when you're asking your favorite LLM question. So then we ran into the pipeline parallels deadlocks and whoops. Um so that the the next stage of improvement came from the adding the pipeline parazone solution and also the the custom MOE kernel that Michael talked about which also enabled CUDA graphs. So that was our kind of the next stage of improvement. Um and then the next stage of improvement came from the other two uh the sending the nickel size index instead of the tensor metadata over to the next stage. Um and the other

**[20:34](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1234s)** improvement that came from was uh came uh was the uh the speculative receive. So we um instead of actually sending or reading the in integer on the receiving side we decided to just speculate on it and uh figure out the what in the tensor corresponding tensor metadata. So this was our journey. We hope that from this like um the um the audience anybody in the audience who's going through their own uh model deployment journey can uh kind of learn and anticipate the the what you need to go through. Um uh even for models that have been already are in the open source and published you may have to go through the

**[21:22](https://www.youtube.com/watch?v=dETUxz8bsB8&t=1282s)** same journey because things at in production as you know always differ. So while it like on the published paper it may look in one way when you actually run it on some hardware some things may be different um and therefore uh you may have to go through the same journey. That was the talk and thank you so much for participating. We'll [applause] take questions towards the on the side.
