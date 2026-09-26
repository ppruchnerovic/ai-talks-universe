---
id: Zln7cKS75WY
title: "Closing the Train-Inference Divide for Asynchronous RL at Scale | Lila Sciences | Ray Summit 2026"
slug: closing-the-train-inference-divide-for-asynchronous-rl-at
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["Lila Sciences"]
channel: "Anyscale"
duration_min: 14
published_at: 2026-09-17T16:06:18Z
video_id: Zln7cKS75WY
url: https://www.youtube.com/watch?v=Zln7cKS75WY
youtube_url: https://www.youtube.com/watch?v=Zln7cKS75WY
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# Closing the Train-Inference Divide for Asynchronous RL at Scale | Lila Sciences | Ray Summit 2026

**Lila Sciences**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=Zln7cKS75WY) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

In asynchronous RL with disaggregated training and inference, even slight differences in model behavior between the training and inference stack can cause significant training instabilities that are painful to debug.

At Ray Summit 2026, Dominic Yurk, AI Researcher at Lila Sciences, walks through two contributions upstreamed to SkyRL that close that gap: faithful replay of expert-router decisions and of per-token sample support, both captured at rollout and reconstructed exactly on the training side. He digs into the engineering: a consistent abstraction for attaching token-level metadata, efficient encoding and transport of large-scale router replay data, and a sparse representation that makes sample-support computation fast at scale.

You'll leave with empirical results showing the effect on training stability and throughput.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,253 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Zln7cKS75WY&t=0s)** Cool. All right, I think I am on now. All right, cool. Can folks hear me? All right, sweet. So, hi, my name is Dominic Jük. I'm going to be talking to you today about closing the train inference divide for asynchronous RL at scale. And we're going to break down a lot of what that means as I go through the talk. So, to start off on a little bit of background, I work at Laya Sciences. Hopefully you heard about us from our CTO's keynote today and we are working to build scientific super intelligence and in practice that means that we need to do a lot of largecale RL on large LLMs across a lot of different environments and we've chosen to really build our postraining stack on top of

**[0:49](https://www.youtube.com/watch?v=Zln7cKS75WY&t=49s)** skyl and we've been working a lot with the scale team to develop this out both for integrating it to our own workloads and actually working with them to develop features that we contribute back. So all the work I'm going to be talking about today has been upstreamed and you can go use it in skyl. So to set the stage for the problem as most of you are probably familiar with async disagregated RL has become the dominant paradigm for pretty much any kind of largecale agentic training loop. And this is really great. People prefer it because it gets you really high throughput. It lets you deal with long rollouts and stragglers and things like that. But it does create this challenge which is that you now have two copies of your model. The inference copy and the

**[1:36](https://www.youtube.com/watch?v=Zln7cKS75WY&t=96s)** training copy. And over time as you do a lot of rounds of training, these will drift out of sync. The inference policy gets stale relative to the trainer. And if you let these differences accumulate too much, eventually it can throw off your training dynamics and you can really screw up your run. So for this talk I'm going to focus on two particular sources of mismatch that can pop up in these async RL loops. The first one has to do with routing specifically. So when you're dealing with a big mixture of experts model, the router has to make a lot of decisions about which tokens go to which experts. And if the training and inference make different decisions at the router level, that completely changes all of the weights that the token goes through. And

**[2:24](https://www.youtube.com/watch?v=Zln7cKS75WY&t=144s)** that can create really big divergences. And then the other part is that if you're doing things like top K and top piece sampling on the inference side that are pretty common, that can also cause a drift on the training side if your trainer picks a different top K set or a different top P set and it also throws out your training dynamics. So both of these can result in just worse performance or even collapse on your training runs. So for the first problem, a really common approach that's been out there in the literature is called R3 rollout routing replay. And this means that instead of having your inference and trainer independently recalculate all of these routing decisions, you just capture whatever routing decision the inference side made and replay that exactly on the training side. And so

**[3:13](https://www.youtube.com/watch?v=Zln7cKS75WY&t=193s)** you're guaranteed that every token goes through all the same sets of routers. And this cuts down on drift substantially. And for the other part around the sampling, you can do much the same thing on the inference side. You cap you capture exactly what set of token IDs were included in the top K or the top P set. And then you just replay that on the training side so that you know you get a consistent renormalization and all of your training and gradient updates go more smoothly. So both of these features were things that were not yet either had partial or no support yet in SkyRL and we wanted to experiment with them in our training stack. So first we built a very simple version of these features and applied them at small scale and it worked great. We took a 30 billion parameter model and

**[4:03](https://www.youtube.com/watch?v=Zln7cKS75WY&t=243s)** we saw what we wanted to on the routing replay side the drift and log props got a lot lower. On the entropy side, we were able to maintain significantly higher entropy over a long training run, which happens with top P. And the throughput was basically unaffected. Everything was going very well until we took it to scale. So we took these exact same implementations but applied them to a bigger model on longer horizon actual science tasks at LILA and the training dynamics benefit was still there, but it really got unusably slow. we were paying a huge tax for these features and this was just not going to be viable at all for real production level runs. So the reason we were hitting this huge

**[4:51](https://www.youtube.com/watch?v=Zln7cKS75WY&t=291s)** bottleneck is because when you look at this async RL loop normally the data going from generator to trainer of just the token by token rollouts is not that big. But when you want to do these replay types of corrections, you have to ship really big amounts of token metadata alongside the tokens themselves. And if you don't handle this carefully, it can really throttle you at the CPU level and at the network level so that no matter how good your GPU kernels are, they're just sitting there idle. So to quantify like what kind of big are we talking about at scale, the biggest culprit is the routing replay because for every single token, you're capturing every one of the top K expert indices across every single layer in the model.

**[5:41](https://www.youtube.com/watch?v=Zln7cKS75WY&t=341s)** So for smaller scale models, this isn't a ton of data, but once you get to any sort of like large scale by modern standards, you're dealing with 100 gigabyte arrays potentially just sitting in RAM. And you know, if you're trying to do a bunch of manipulations on these, send them back and forth all over your network, handling that volume of data can slow you down dramatically if you're not careful about it. And so in order to address this, there wasn't any one silver bullet of like one line we changed and magically everything got faster. It really took a lot of layered improvements to make this better step by step. So part of it are things like using lower precision integers to represent the expert indices, using sequence packing on the metadata so

**[6:30](https://www.youtube.com/watch?v=Zln7cKS75WY&t=390s)** you're not wasting space on padding tokens with ragged links. um using smart binary encoding protocols so that when you're sending the data over network via JSON, you're not wasting tons of data on just standard ABC character encodings. Um, and then part of it is actually getting down to the Ray level underneath Sky RL and thinking carefully about how much data you're putting into Ray's shared object store at one time because if you overload that, it will start paging onto disk, which is great for not crashing your run, but really terrible for running quickly. Um, and then finally, you just need to think a lot more about all the operations you're doing because Python list slicing and list comprehension and for loops are all

**[7:19](https://www.youtube.com/watch?v=Zln7cKS75WY&t=439s)** very easy. But again, when you're operating on tens of gigabytes size data, Python gets really, really slow. So, you need to be very careful about every copy and slice and scan and whatnot that you do. And when you stack all of these improvements on top of each other, you can drastically improve how quickly your training system is able to handle this R3 data. Now, another class of tricks that um that really helps is that on the top P sampling side, a really nice empirical property when you're post-training models is that if you apply top P sampling, even at like 0.95 of the probability mass, you end up with really sparse numbers of tokens that can

**[8:07](https://www.youtube.com/watch?v=Zln7cKS75WY&t=487s)** possibly contribute. In our internal workloads, over half of tokens have the top token is over 95% of the probability mass. So you're reduced to just greedy sampling. And for most of the rest of the tokens, only you know somewhere between two to six possible candidates emerge. And so if you would set your top K to something like 64, rather than collecting all of those and sending all of it around, you can use sparse data representations to only capture the top key subset that actually mattered. And that can also drastically cut the amount of data you're sending around. And then furthermore, you can use PyTorch's sparse tensor operations to do math on these more efficiently when you're actually doing your loss computation at

**[8:56](https://www.youtube.com/watch?v=Zln7cKS75WY&t=536s)** the end. And so it can save you a lot of runtime at the loss computation layer as well as well as some memory headroom on your GPUs. Now, the last class of like engineering challenge I want to talk about is the types of bugs that you only really hit at scale because there's various things that in a perfect mathematical world where everything is continuous could never happen. But when you're dealing with realworld numerical engines that are trying to run as fast as possible and making tradeoffs, you can hit really weird edge cases. So, a couple examples we saw within VLLM is that every once in a while it will give you a token and say that its log prop was negative infinity

**[9:45](https://www.youtube.com/watch?v=Zln7cKS75WY&t=585s)** because there was just something weird going on in its numerical random exponential sampler. And in a related thing, every once in a while, if you tell VLM to sample with a top K of 20, it may give you token number 21 or 22 that was outside of that 20 you requested because it's whole Triton fast kernel does an approximate sort. And the reason these bugs haven't been fixed by VLM, you know, many months ago is that they are really rare edge cases. In our workloads, we were seeing this on the order of once every 100 million tokens, you might see something like this. And so if you're running like smallcale tests, running CI loops, this sort of thing is not going to pop up. But when you're running at scale, if you're

**[10:33](https://www.youtube.com/watch?v=Zln7cKS75WY&t=633s)** crashing your whole run once every 100 million tokens because VLM threw a nan, you know, that's not going to that's not going to suffice. So you have to, you know, build in mitigations to account for these kinds of weird edge cases. And now after all that engineering, I can talk about what this actually enables us to do. So this is a pair of real LIA training runs we did on some of our science environments at a larger scale. And the gray curve was an initial attempt we made a few months ago um without any of this uh R3 or sample support. And you can see that it was hill climbing really nicely for about a hundred steps, but then training destabilized. The gap between the inference and trainer shot up and the

**[11:21](https://www.youtube.com/watch?v=Zln7cKS75WY&t=681s)** reward just cratered and went basically to zero. So this run became relatively unusable. But then when we did the exact same run with these features enabled, you can see that training stays stable. We get continued very nice hill climbing behavior to higher rewards. the gap between the training and inference stays much lower and healthier. And in contrast to that earlier graph I showed you with all of these um engineering choices put in place to handle this big token metadata more efficiently, the throughput got to a very competitive level with where this run was at with both of these features turned off. So this is now like a really viable feature that we can use for our RL runs at scale to hopefully let them run you know on bigger models longer rollouts more steps

**[12:11](https://www.youtube.com/watch?v=Zln7cKS75WY&t=731s)** and climb higher in the reward space. So just to summarize the big takeaways from this talk at a high level async disagregated RL is really great for largecale reinforcement learning but you pay this price of training inference mismatch and you really need strategies to be able to mitigate this mismatch if you want your RL runs to stay stable and climb to really high rewards over the long run. However, the methods for mitigating this involve shipping a lot more data around and you need to put some thought and some careful engineering into handling these data volumes appropriately so that the CPU and network get out of the way and the GPUs can keep doing their jobs. And yeah, it's just it takes a real stack

**[13:02](https://www.youtube.com/watch?v=Zln7cKS75WY&t=782s)** of, you know, incremental improvements on top of each other to get there. And it's great to be working with a framework like SkyRL where it's fully open. It's a great developer community and we can really build with them to layer in these improvements. Um, and then, you know, I can throw up a whole bunch of PRs that Eric needs to deal with later. Um, so yeah, thanks for coming by here. I don't know if they're doing questions for these lightning talks, but I will be over at the Laya booth right over there if anyone wants to chat more about this.
