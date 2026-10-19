---
id: _cRgl3maiT8
title: "How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs"
slug: how-inference-keeps-up-with-our-insatiable-need-for-tokens
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 23
published_at: 2026-10-12T05:36:56Z
video_id: _cRgl3maiT8
url: https://www.youtube.com/watch?v=_cRgl3maiT8
youtube_url: https://www.youtube.com/watch?v=_cRgl3maiT8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# How Inference Keeps Up with Our Insatiable Need for Tokens — Cerebras & Gimlet Labs

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=_cRgl3maiT8) · [Conference site](https://www.ai.engineer/)

## Description

Google went from 480 trillion to 3.2 quadrillion tokens a month. Here's everything the industry does to keep up.

NEXT UP: AI ENGINEER CODE SUMMIT
Join us in SF for the second annual AIE CODE Summit, Nov 10–12, our last flagship summit of 2026. Applications live now: https://aie.codes

Daniel Kim of Cerebras and Michelle, co-founder of Gimlet Labs, explain how inference keeps getting faster and cheaper. Daniel covers the runtime: why decoding is memory-bound, splitting models across GPUs, continuous batching, KV cache, paged attention, prompt caching and chunked prefill. Michelle covers the system level: prefill/decode disaggregation, speculative decoding, attention/FFN disaggregation, Gimlet's multi-silicon cloud and an agent that writes optimized kernels.

In this video:
• Why decode is memory-bound and how big the KV cache gets
• Paged KV cache, prompt caching and chunked prefill explained
• Prefill/decode, speculative and attention/FFN disaggregation
• Using agents to generate optimized kernels

SPEAKERS
Daniel Kim, Head of Growth, Cerebras
X: https://x.com/learnwdaniel

Michelle, Co-founder, Gimlet Labs

LINKS
Cerebras: https://www.cerebras.ai
Gimlet Labs: https://gimletlabs.ai

CHAPTERS
0:00 Intro
0:33 Exploding demand for tokens
2:02 Autoregressive decoding and the memory bottleneck
2:37 Splitting models across GPUs
3:27 Speed vs throughput Pareto frontier
4:27 Batching and continuous batching
5:22 KV cache memory growth
6:11 Paged KV cache
7:06 Prompt caching
7:41 Prefill vs decode
8:36 Chunked prefill for long contexts
9:38 System level: workloads differ
11:06 Prefill-decode disaggregation
12:21 Memory bandwidth: Cerebras vs H100
13:05 Cerebras and AWS Trainium
13:39 Gimlet's multi-silicon inference cloud
14:28 Speculative decoding
17:01 Attention-FFN disaggregation
18:25 Agents writing optimized kernels
20:16 Agents for silicon, compilers and ops

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*4,253 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1s)** [music] Hello everyone. My name is Daniel. Uh I work on AI and AI agents here at Cerebras. Um what's your name? >> I'm Michelle. I'm a co-founder at Gimit Labs where we're building a multisilicon NeoCloud to optimize inference at every layer of the stack. and we are really excited to bring you our talk, all the things we have to do to satisfy your insatiable need for tokens. As you know, AI spend is going kind of bananas right now with this year, we're slated to spend $765 billion on compute and in 2031 up to $1.6 trillion. The frontier labs are having a mad dash to

**[0:53](https://www.youtube.com/watch?v=_cRgl3maiT8&t=53s)** secure as much compute as possible to buy um across hardware vendors to do both training for their frontier models as well as to serve all of their users. And all of their compute is going to satisfy everyone's insatiable need for tokens. Um Google at their IO last year said that they were serving 480 trillion tokens per month and last month they said that it jumped up to 3.2 2 quadrillion tokens per month. So all of this is happening at the same time as models are getting cheaper and faster. Llama 3.370B when it was first released compared to now is now 25% cheaper while still being 3.6 times faster. So in today's talk we're going to talk about

**[1:40](https://www.youtube.com/watch?v=_cRgl3maiT8&t=100s)** two things. One, what have we done so far to optimize inference to make it cheaper and faster? and what does the road map look like to juice Perf and throughput even further. So to do this, let's take a little bit of a time jump to 2022 and learn about all the optimizations that led us to the point we're at now and hopefully what the future looks like. So LLMs produce tokens one at a time in something called an auto reggressive loop. So to generate one additional token, you need to read all of the weights from memory into compute. So most of the time the compute is sitting idle. It's just waiting for memory to be able to stream in all the weights necessary to do the compute itself. So up to 90% of the time the compute's just sitting there waiting

**[2:28](https://www.youtube.com/watch?v=_cRgl3maiT8&t=148s)** on memory to load. So how can we figure out how to optimize this so there's less idle time and you can make full advantage and serve tokens faster? So what you can do is throw more compute at the problem. So instead of streaming in the whole set of weights, what if you could split up the entire model into four and have each GPU take care of a fourth of the model each? Then you could reduce in theory the amount of time it takes to serve a single token by four times. However, you have to pay a tax if you want to do this. before the attention block and then the F. So sorry after the attention block and the FFM block, you have to do something called all reduce where you take each of the individual calculations from each GPU and you combine it all together. So you can actually get a calculation because each of the GPUs doesn't have the whole

**[3:16](https://www.youtube.com/watch?v=_cRgl3maiT8&t=196s)** picture. It only does 1/4 of the model. So you need to do this across every layer twice which can lead to only getting 2x speed up for getting 4x the amount of compute that you add on. If I were to graph this in a pretty graph, um you can see that throwing more GPUs at the problem does get you faster tokens, but it requires exponentially more energy to serve a single token as you put in more compute at the problem because of the communication overhead we just talked about. So if we flip the y-axis here, so it's throughput. You can see that this resembles something like a paro frontier where you can see that you have to make some kind of sacrifice between throughput and speed when you're an inference provider. A great example of this is cloud code fast mode where you can spend I think sixx the amount of

**[4:04](https://www.youtube.com/watch?v=_cRgl3maiT8&t=244s)** tokens to serve a single token compared to regular cloud for twice the speed. So for that product they're really optimizing towards the right of the par frontier where they're getting the speed but at the cost of not being able to serve as many tokens. So during today's talk we're going to talk about what are the innovations we have done in the past and in the future to be able to shift the paro frontier to the right. So you already know from our previous slides that to generate each token you have to read the whole model. So what if we could spend one pass that we already paid for to serve multiple requests. So that is where the idea of batching and continuous batching comes in. The idea of batching is when you take a weight read that you've already done and be able to serve multiple user requests.

**[4:53](https://www.youtube.com/watch?v=_cRgl3maiT8&t=293s)** However, the problem though is that some of these requests are longer than others, which means that there's all of these idle periods in the compute where nothing is happening. So how can we solve this problem and squeeze out more performance? That's where continuous batching comes in. So the idea here is that for every single idle slot, you slot in a new user request to be served during that same weight read to be able to serve as many requests as possible. However, this does come with a slight downside because every single token when you do inference requires you to save something into the KV cache because that's how the attention block works. You need to understand how every single token like what the K and V vectors are. This can add up very quickly. So if you're running a coding agent with very

**[5:41](https://www.youtube.com/watch?v=_cRgl3maiT8&t=341s)** long context, for example, 128K context, you're going to save 42 gigabytes of KV cache that is needed to serve that individual request. So the rule of thumb here for a 70 billion parameter model is that for every 3,000 tokens, you need 1 GBTE of additional KV cache. And that's for one user request. So imagine you're doing batching and you're doing like eight different requests at the same time. Then your KV cache is going to explode and you will not have enough memory to be able to serve all of your requests. So what are some of the innovations we have done to be able to optimize how we use memory? So that's where paged KV cache comes into play. So how traditionally KV cache worked was that you would have physical memory that you would reserve to make sure that you could have enough room to be able to store all of the KV information from each request into memory. However, this

**[6:31](https://www.youtube.com/watch?v=_cRgl3maiT8&t=391s)** came with a downside and a lot of inefficiency because you would just have a lot of memory blocks that would be reserved but wouldn't actually be used. So the idea with a paged KV cache is we use something that's similar to like an OS or a virtual machine where you provision a whole memory block that's all virtual and you can store wherever there's free space KV cache for each request. So this allows you to serve three times more requests than not having a page KV cache and just doing what was before. And this really reduces the amount of wasted space where you're reserving memory slots without actually using them. This was right after followed by an innovation called prompt caching. So the idea here is that if you have a coding agent or if you have a chat app that has a very long system prompt, you don't

**[7:20](https://www.youtube.com/watch?v=_cRgl3maiT8&t=440s)** actually have to recalculate the KB cache needed every single time you have a request. What you can do is you can reuse the KV cache that you calculated already for the previous request for the next request. That way you can pick up where you left off. Here you can skip the very very time consuming prefill phase. And you might be wondering what is prefill. So during inference you can split up what happens into two major phases. Prefill and decode. So the prefill phase consists of all the things that happen once the request arrives and then ends when the first tokens gets generated. And here you can see this when you type something into chatgpt and then it takes a couple seconds before it starts returning the first token and then it goes kind of like smoothly from there. So what's happening during the first

**[8:08](https://www.youtube.com/watch?v=_cRgl3maiT8&t=488s)** couple of seconds where it's not returning anything is that it's computing KMBB vectors for every single prompt token that you've inputed and produces the first output token. This is very computebound because you can optimize the hell out of this. You can parallelize this extremely. However, after the first token is generated, what happens is uh that you decode one token at a time, reusing the KV cache you just built in the prefill phase. So, this is more reliant on memory. The reason I'm talking about this is because something happened lately that's really messing up a lot of inference pipelines, which is super super token hungry coding agents. So, let's say you have a coding agent that's using 200k context or 500k context or a million context, right? What happens is that it starts to clog up the pipeline while pre-fill is running. No other

**[8:56](https://www.youtube.com/watch?v=_cRgl3maiT8&t=536s)** prefill or decode request can get through. So this is kind of catastrophic if you have a bunch of people that are sending in coding requests and a couple people that are just trying to figure out like math problems in chat mode. So to avoid this clogging problem, there is an innovation called chunked prefill that kind of goes and solves this problem. And the idea is quite simple here. The idea is taking a very long piece of prefill, chopping it up into smaller bits so you can interle in different decode and prefill requests. That way there's not one thing that's taking up a bunch of time and clogging the whole pipeline. So now Michelle tell us more about what else we can optimize. >> Yeah, so all of the optimizations that Daniel just talked about are runtime level optimizations. So that explains we

**[9:44](https://www.youtube.com/watch?v=_cRgl3maiT8&t=584s)** explore how we make inference more efficient within a single worker. But in order to to keep pushing that frontier, we really need to start looking at system level optimizations, which is how can we distribute these workloads across many different workers. And so the first thing to recognize there is that every request is different. So take for example a summarization use case. You're throwing the LLM a bunch of different documents and you just really want a single question answered. And so this workload is going to have a long prompt and short answer. And so it's dominated by that prefill phase and so therefore computebound. On the other hand, you might have a case where it's the opposite. Let's say you want to write a long story or book. You just want to pass it a few themes for it to go off of. And so this is going to

**[10:32](https://www.youtube.com/watch?v=_cRgl3maiT8&t=632s)** have a short prompt and long answer. And this is going to be dominated by decode because you have so many output tokens compared to the number of input tokens coming in. And this is going to be memory bound. And finally, you can have a case that's somewhere in the middle, right? It's both a long prompt, a long answer, and you're seeing here that both the prefill and decode phases and therefore compute and memory both matter. And by looking at these different examples, you can really see that the resource requirements that you have for your hardware, it's pretty different depending on what your workload looks like. And so how do you prevent yourself from getting, you know, bound by compute, bound by memory. And so one way to do that is called disagregation. So splitting up your workload to different worker nodes. And so the most common form is called prefill decode disag where you're

**[11:21](https://www.youtube.com/watch?v=_cRgl3maiT8&t=681s)** actually splitting and disagregating this workload by phase. And what that allows you to do is essentially have two pools. So you have your prefill pool that's going to be running the prefill part of your workload. The decode pool that's going to be running the decode part of your workload. And taking the summarization use case for example, you know, you're going to want to scale up that prefill pool so you're not blocked by the compute and scale down your decode pool because you don't want to waste resources when you just really don't have that much decode work to do. And it's nice because now you can scale all these independently and neither part is stalling the other. And we can take that one step further, right? We said before prefill that workload itself is inherently bound by compute decode that is bound by memory. And just walking through that really

**[12:09](https://www.youtube.com/watch?v=_cRgl3maiT8&t=729s)** quickly again the reason for that is as you're doing decode you're stepping through each of these tokens one by one and for every decode step you're rereading the entire KB cache, right? That's going to be memory bound. So yeah, um the the thing that Michelle just said about this being memory bound, this can be clearly seen by what the hardware can actually do. So GPUs, right, uh the the speed at which you can transfer data from memory into compute is limited by something called memory bandwidth. So for an H100, this looks like 3.35 terabytes per second. However, Cerebrris has 7,000 times the bandwidth of a H100 with 21,000 terabytes per second. This is because we have a very specialized SRAMM based memory architecture on our chip. So this really means that Cerebrus is really built for

**[12:58](https://www.youtube.com/watch?v=_cRgl3maiT8&t=778s)** decode. So we can serve tokens at 3,000 tokens per second versus an H100 serving it at 600 tokens per second for decode. So we're really excited to partner with AWS to productionize this. So we are going to partner with AWS tranium so they can serve prefill using their AWS tranium chips use their EFA service to transfer the KV cache to our Cerebra CS3 systems to finally serve the end token. So this will lead us to give us 5x highspeed token capacity in the same footprint. So this is one of the things that we're doing to try to make fast inference more accessible and cheaper for developers. So we're really excited to really p pursue this partnership >> and at Gimlet we're really generalizing that beyond just tranium and cerebras. What Gimlet is building is essentially a

**[13:46](https://www.youtube.com/watch?v=_cRgl3maiT8&t=826s)** multi-ilicon inference cloud which takes your workload, breaks it down into finer grain pieces, determines the resource characteristics of all of those different pieces and then figures out the best way to map it to the underlying hardware where that hardware can be really anything, right? Nvidia, AMD, Tranium Cerebrus Dematrix Intel Gouty, the list goes on and on. And by running those tasks on the machine that is most efficient for running it, we're actually seeing pretty crazy results. So we're seeing three to 10 times faster inference compared to homogeneous systems that have the same power budget. And this is diving into more than just the pre-fold decode disagregation than before. And some of those techniques are for example disagregating based on model instead of on phase. And so that's called speculative decoding. So just reviewing again the decode phase.

**[14:34](https://www.youtube.com/watch?v=_cRgl3maiT8&t=874s)** Typically, you do a forward pass for each of the D tok to to decode tokens that you're getting out. And that's the standard way of doing it. What speculative decode is is that you essentially have a draft model. And this is just a smaller form of the full model that um can generally approximate the results that you get out of it. And the nice thing there is because it's smaller, it runs a lot more quickly and also uses less resources. And so in speculative decode, what you can do is in order to get, you know, the nine next tokens, you will essentially run the decode on that draft model first, it's going to give you back what is called candidate tokens. So you're not 100% sure all these tokens are right, but because you know often these have been fine-tuned or trained off of the full model. It's it's approximately right. And you want to validate, okay, are these the tokens that I actually want to

**[15:22](https://www.youtube.com/watch?v=_cRgl3maiT8&t=922s)** output? And so you'll actually run the next phase on that full model. That's called the verify stage to validate okay which of these tokens are correct. And essentially you can keep doing this until you know you've validated all these tokens from the draft model. And at the end of the day you can see here on the top the standard way of running it you needed to run that forward pass on your full model nine times to get those nine tokens. On the other hand with speculative decode you actually only needed to run it three times on that full model. And if you can get that draft model to run really really quickly, then that time is minimal and you can really shorten the amount of time it takes to get your tokens. And looking at some more concrete results. So this is essentially that paro frontier that Daniel was showing earlier where x-axis is the speed at which you're getting the tokens and the

**[16:08](https://www.youtube.com/watch?v=_cRgl3maiT8&t=968s)** y-axis is the throughput. And so the baseline case we're comparing to here is prefill decode disag across homogeneous GPUs. And you can see that, you know, throughput is pretty good, but as soon as you're pushing on that speed, that throughput drops pretty drastically. So what if you then run speculative decode across those same GPUs? So now you're running that draft model and you're able to see you're able to get that curve to the right. And the reason for that is because you're running the decode on that full model less times. But we can push that even further, right? Going back to our theme of running those workloads on the hardware that can run it best on something such as you know Dematrix or Cerebrus where you're able to run small models very very quickly you see drastic performance improvements. So here this is where you're seeing those numbers for that

**[16:56](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1016s)** same throughput right you're able to get 10x the interactivity compared to if you're just running it on homogeneous machines. The final form of DSAG we wanted to talk about is called attention FFN disag. This one gets pretty exciting when you think about serving large models and I'm saying like three trillion parameter models where these models are so large that even just running one layer it can be pretty resource intensive and so the concept is essentially the same thing right like for that particular task that you need to do whether it's that attention layer or the feed forward FFN network layer then you are essentially trying to figure out okay what are the resource characteristics then what is the best hardware to map it to and so the attention layer that's going to be more memory bound. It's doing a lot of KB cache accesses. The FFN layer that's doing a lot of dense matrix

**[17:44](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1064s)** multiplications. And so then it makes sense, right? You're going to run the attention on the machine that has memory bandwidth. The FFN layer on the machines that can run those matrix multip multiplications as quickly as possible. And essentially what happens here is even within the model, you're pingponging across, you know, many different machines in order to to get the inference from that model and just really disagregating every single layer. And one thing that we really wanted to note here is that there is no best form of disag. It really depends on the trade-offs that you have for, you know, depending on what your model is, your workload, and what you need for latency and what you need for throughput guarantees. And as we look towards the future, we see that agents are only becoming more and more incorporated into our everyday

**[18:33](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1113s)** life. It's incorporated into our work. Everyone is using it. And it's continuing to push that need for more and faster tokens. >> Yeah, it's really getting yeated to the right. >> I [laughter] I told Daniel not to say that. But the good thing about this is that even though you know this seems like a crazy crazy target, we can actually use agents to help us solve these problems and keep pushing the frontier. And so one of the things that we're doing at Gimlet is actually using an agent to generate optimized kernels. Especially for a use case where we want to support such a wide range of different kinds of hardware. We need to figure out how do you make that problem a lot more tractable because right now how people generate and how people optimize kernels is that there's a lot of people sitting there handtuning and figuring out how to optimize these kernels. And the thing is that these optimizations can vary pretty

**[19:22](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1162s)** drastically based on you know the model that you're trying to run the hardware that you're running on even within generations of the hardware and you know the workload shape itself. And so what we do at Gimlet is we built KForge which is an agent for generating these kernels. It takes in a bunch of information like your hardware profiles, your workload profiles, basically anything that you can use to figure out how to optimize kernels and we solve it as a brute force problem, right? And so here's an example, right? We have a forward pass and the kernel that um KForge optimized from it and we're seeing pretty interesting results. So last week, you know, we're running the agent for probably less than the span of a week. And within that time, it was able to speed up GPTOSS 12B on AMD hardware by 33% end to end. And the interesting thing to note here is that

**[20:09](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1209s)** this is building on top of kernels that have already been optimized. and you can go and take you know agents to the next level and use them to help us build and design custom silicon that is hyper tuned for specific models or your specific workload. This can then be used to train even better and smarter and faster AI which then can also be used then to design the next generation of the custom silicon. And you know this loop keeps going on and on and it's a recursive loop like shout out to the folks at recursive >> and I want to end the talk by saying that we are just getting started in our journey to optimize throughput and speed on inference because at the very top of the stack you don't think really about inference optimization when you talk

**[20:56](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1256s)** about like incident response right but when you have agents that are making our systems much more reliable and increasing uptime we're getting more throughput and we can get more token Or you can apply agents to the problem of bringing up models as soon as a model drops on the market, getting it running on all the different kinds of hardware on day one. >> You can even go a little bit crazier with compilers. Imagine a world where you an inference stack can be customuilt for your workload and the model that you're running. This is already being demonstrated by folks at Anthropic, right, that built a compiler in two weeks. So I think there's a lot of optimizations that you can do when you're building just in time custom software to support the model you want to run on the workload you want to run on your custom hardware >> and referring back to the previous slide using agents to continue to help us to build you know more custom silicon and

**[21:46](https://www.youtube.com/watch?v=_cRgl3maiT8&t=1306s)** helping speed up the tape process. And finally, this is the non very technical part, but all of the things that surround what takes to serve inference, all the procurement, all the legal, all of the things that are in the back office, all of these things combined with agentic workflows are able to be optimized. So when we do all of this, I'm really optimistic about the future and all the things we can accomplish to serve tokens faster and cheaper. So next slide, please. Thank you so much for coming to our talk. Uh we are working both very very hard to give you faster and cheaper tokens. And yeah, let us know if you have any questions. We'll be around after the talk. >> Yeah. And go eat tokens. >> We're making more tokens for you so you can also generate gifs like this. >> Yeah. [laughter] >> [music]
