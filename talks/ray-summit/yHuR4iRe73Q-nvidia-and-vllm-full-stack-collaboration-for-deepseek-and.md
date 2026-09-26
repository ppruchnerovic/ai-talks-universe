---
id: yHuR4iRe73Q
title: "NVIDIA and vLLM Full-Stack Collaboration for DeepSeek and MiniMax Performance | Ray Summit 2026"
slug: nvidia-and-vllm-full-stack-collaboration-for-deepseek-and
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 23
published_at: 2026-09-17T16:06:59Z
video_id: yHuR4iRe73Q
url: https://www.youtube.com/watch?v=yHuR4iRe73Q
youtube_url: https://www.youtube.com/watch?v=yHuR4iRe73Q
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# NVIDIA and vLLM Full-Stack Collaboration for DeepSeek and MiniMax Performance | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=yHuR4iRe73Q) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

NVIDIA and the vLLM community collaborated to deliver record-setting DeepSeek and MiniMax performance in the SemiAnalysis InferenceX benchmark.

At Ray Summit 2026, Siyuan Fu, Software Engineer at NVIDIA, covers the full-stack optimization path, from kernel-level improvements powered by FlashInfer to distributed serving capabilities enabled by NVIDIA Dynamo, and shows how these contributions help vLLM users reach higher throughput, lower latency, and more efficient inference on NVIDIA GPUs.

You'll leave with a map of the optimizations and where they land in your stack.

This session was part of the first vLLM Conference at Ray Summit, hosted by Inferact.

Liked this video? Check out other Ray Summit vLLM session recordings: https://www.youtube.com/playlist?list=PLXMguE8Nc9o4

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,910 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=6s)** [clears throat] Okay, I guess I guess it's time to get started. So, hello everybody. Good afternoon. Um, my name is Suen. I'm a senior AI derive technology engineer at Nvidia. So I mainly working on the inference optimizations for model LLM and I contribute a lot to open source projects like flash infer and VM of course. So in this session I will talk about some optimizations Nvidia has made to VM to optimize the open source models performance. So first of all I want to highlight the close collaboration between v uh between

**[0:55](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=55s)** Nvidia and opensource communities. So so far we have um participated in a lot of uh open source models day zero bring up and we also have a lot of employees uh actively contributing to VRM project. So this is today's agenda. So in the first part I want to uh talk about some optimizations we made to Kim K3 minimax and deepse R1. So this part will be very technical and also kind of low level. Uh and in the second part I will do a brief introduction into the Dynamo project. So let's get started.

**[1:44](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=104s)** Yeah. First Kim K3. So Nvidia has participated in Kim K3's day zero optimization. Yeah. And we achieved significant speed up from 72 tokens per second to 111 tokens per second. And in this effort I want to specifically talk about a um the optimization we made to Kim K3's latente. So we know that Kimik3 has uh adopted this latoe design. So it introduced a linear layer to uh project the hidden size down from 7K to 3k uh for router expert only. Uh for share experts the size is still 7K

**[2:33](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=153s)** and since for serving Kim K3 we use tensor parallel we use TP8 on GB300 system. Uh so we will introduce a or all reduce kernel after thee. However, this cause a problem because now your shared expert results size is inconsistent uh with your route experts results. Uh so we cannot use one single kernel to reduce them uh at least when we started this effort. So the original design is to use two or reduce kernels. First we use one or reduce for sorry do I have a do I have question so we use one kernel to reduce the share expert result and we use this or reduce plus

**[3:23](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=203s)** arms norm fuse kernel uh provided by flash infer for routy experts result and after that we u use up project kernel to project it up to 7k and we reduce them together. So this design is not optimal because we definitely do do not want two reduced kernels here. So in order to optimize this uh we have some prior knowledges. Uh first uh we know that all reduce has two stage. Uh we first do one reduce scatter and then we do the all gather. Yeah. And second nowadays we can effectively fuse the all together uh with a gen and hide it latency as well. So the proposed optimization looks like

**[4:14](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=254s)** this. We first break the all reduce kernel for shared expert uh into two stage the reduce scatter and all gather and then we can effectively uh fuse the all gather kernel with our project kernel. And furthermore, we can also fuse the reduce scatter kernel with the all reduce kernel after the router experts. Uh so the proposed optimization looks like this. So we only have two kernels right now. Yeah. And this is the achieved result. So first of all, we also try to optimize uh the or reduce kernel for shared expert. uh we try to overlap it with the app project. Uh however with our new new

**[5:03](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=303s)** kernels we achieve better performance uh we achieve approximately 19.5% improvement. So this is the latest optimization for kimit k3. Uh next I will talk about the all reduce optimization for minax. So again we also participated in miniax day zero optimization and we achieved significant improvement. Uh oh sorry this is kim oh minia max m2.5 it's a bit small here. So uh in this part I want to talk about the reduce optimization for the postq project. So normally even with tens of parallel

**[5:52](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=352s)** uh you don't do not need a or all reduce kernel after your QK project because normally we use per head arms norm and when you enable tensor parallel the QK project is shed along this dimension the height dimension so it's hidden size is still intact so you don't normally you do not need to reduce the result yeah but you do need or reduce after the attention that's unavoidable. However, Miniax introduced this full heads RMS norm. So now you need uh you need to gather all the every hat from the token to do RMS norm. So this time we cannot avoid doing the or reduce here. So bas basically we need to first

**[6:41](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=401s)** calculate the square sum and we reduce them together and we use it to normalize the tokens. Uh however we have a very important observation here. So to do RM's norm um your numerator is actually not reduced. Uh you only need to reduce this the square sum uh in the denominator. So naturally we want to first uh calculate the square sum locally in each rank and then we can just reduce the square sum result. So this this is good because you only need to reduce a scalar value per each hand. So in this way we imagine that the overhead of all reduce can be very minimal. Um but in the profile it still shows some overhead and we want to

**[7:31](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=451s)** optimize it. So uh recall that I said all reduce has two stage uh the reduce scatter plus or So why do we adopt this methodology? So the idea is to reduce your traffic size. So for example, if uh to do reduce scatter, each rank needs to pull one chunk from every other rank. So if you calculate the traffic size uh it will be your chunk size times n minus one and times n since you have n ranks so the size will be n minus one. Yeah. And all gather is exactly the

**[8:21](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=501s)** same. It's also n minus one since each rank pulls one chunk from every other rank. So the uh so the traffic size for the normal twoshot or reduce kernel is 2 m minus two. But um what about one shot? So the answer is obvious since each rank needs to pull the entire tensor from every other rank. So you ends up with n minus one * n. So you need to uh comm uh you need to move n square minus n uh number of tensers. So any questions so far? Good. So looks like you should always use two

**[9:09](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=549s)** shot or reduce since it it's since it traffic size is very small. Um but in this case like I said before each head only need to reduce one scalar value. So your uh your size is already very very small. So in fact using two shot and one shot doesn't matter anymore in terms of the traffic size. You are not saturate your reading bandwidth anyway. So in this case we uh we focus more on reduce the latency. So if you use two shots or reduce uh you you have to do two synchronizations since you have two stages obviously but with one shot or reduce uh you only need to do one synchronization at the

**[9:58](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=598s)** beginning of the kernel. So in this case one shot or reduce is actually better and in fact not just this QK project or reduce actually ine and attention if your batch size is really small uh using one shot or reduce kernel is better than use the traditional twoshot or reduce. Uh so so this this benchmark I run it on GB300 with TPT4 uh and the oneshot kernel is from the flash infer and actually you don't need to worry about this anymore if you use flash infer because it uses a huristic to select between one shot and two shot. So if I remember remember correctly uh if your batch size is less than 40 uh it

**[10:46](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=646s)** will choose one shot over two shot. Okay that wraps up the or reduce optimizations for minax. Um next I want to talk about the deepse R1 PDDD sac optimization. Uh so some background for this project. Uh we started this project uh last year in November and it's a joint effort with meta. Uh the goal is to optimize deepsea and vfp4 um with pdac on gb200 and vl72 system. And the target is to achieve more than 7k tokens per second per GPU. Uh and as you can see we achieved this goal. we

**[11:34](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=694s)** end up with more than 10,000 tokens per second per GPU in January. Um so the first optimization I want to talk about is still the reduce kernel. So we we are seeing this all gather and reduce scatter again. Um but this time it's reversed. So we this time we first do all and then we do reduce scatter. Um because when serving deep CR1 we are not using TP the tensor parallel like Kimmy or Miniax uh we we use data parallel plus expert parallel. So after attention since you enable data parallel uh the tokens are distributed on each rank um evenly but the needs to see different tokens

**[12:25](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=745s)** based on the routing result. So therefore after attention you have to gather all the tokens together and feed them to thee. So that's why we use all gather here and of course aftere you need to distribute the tokens again uh evenly. So aftere we use reduce scatter. So this all reduce or all get reduce scatter communication back end is uh simple but it's also the best uh for the decode workers. Uh we we found that so the first optimization we did is actually very simple. So your is running at NVFP4 accuracy. So you you do not need hidden states to be at BF16 accuracy. So

**[13:14](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=794s)** originally VRM would first gather hidden states in BF-16 and then it use a kernel to quantize it to VFP4. So the first optim optimization we proposed uh is to simply quantize hidden states hidden states to FP4 before. So this significantly uh reduce your traffic size. And second uh the second optimization I want to talk about is the V2 weight offloader. Uh so with GB200's MVL link uh your uh your transfer between CPU and GPU is very fast and very effective. So it actually make weight offloading available. And also VRM just introduced

**[14:02](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=842s)** this V v2 weight offloader at the beginning of this year. So it it it just work very well. It can overlap the weight loading of your next layer uh with current layers computations. And this is very important because since we reduce the memories of weight uh we can go to EP2 for deepse R1 and VFP4. Um if before this we can only goes to EP4. And the reason why EP2 is good uh is because we want to reduce the overhead of communication. So for prefield workers uh they are pretty much computer bound. So in this case your number of ex uh of expert parallelo doesn't matter

**[14:51](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=891s)** anymore in instead we want to reduce the overhead as much as possible. Uh sorry this diagram is actually not very good. the number is quite small. So basically here the with 4GPU the latency is 400 4,900 but with two GPUs the latency is 2,000. So uh it's like uh more than 100% difference. So eventually our best recipe is to use four preview workers with EP2 plus one decode workers with EP8. But by the way for decode workers it's a different scenario since decode worker is not purely computer bound. It's also some sort memory bound. So for G cold

**[15:41](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=941s)** water, you still want to increase your experts uh extra parallel size. Yeah. And and with that being said, uh I I I said that all reduce scatter is the best communication back end for decode worker. But since we started this project like uh a long time ago at that time VRM doesn't have a lot of uh back end to choose. Uh but nowadays we we see that there's a lot of uh different all to all back end you can choose from. So nowadays I uh all gather reduce scatter may not be the single best choice for decode worker. Uh for example this flash info link uh one side uh may be better. So please take my uh message with green

**[16:30](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=990s)** offsource. Yeah. Yeah. So that wraps up the first part. So to summarize it uh first we can split or reduce into reduce scatter plus all together and hide their latency separately and second we can fuse together with gen and third we can use oneot or reduce kernel when traffic is small and for lastly it's better to use smaller parallel size in prefield worker if you enable pdac and you should also consider weight offloading Okay, that wraps up the first part. So let's continuing this topic of PDD sec. So let's jump into Dynamo.

**[17:23](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1043s)** So nowadays if you look at the inference X results you you will notice that uh for NVL72 uh recipes uh it's almost certain that they use PDDD set for example this is deep V4 pro and this is Kim K3 yeah and also they have this prefix the dynamo yeah before BLM on So what is Dynamo? So Dynamo is an open-source uh project that uh Nvidia has been heavily contributed to. It focuses on system level optimizations for LM inference and the goal is to provide very strong optimizations for scheduling, memory

**[18:13](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1093s)** management, data transfer uh and so on. So Dynamo is compatible with Kubernetes but it can also run on its own without Kubernetes and it's also uh compatible with various different LLM framework. Yeah. And also Dynamo is uh not a single project. It's actually a family or or or a suite containing a lot of different useful tools. Uh for example, we now have AI perf uh which is a very easy to use benchmarking tool. Uh we have Nixo uh which is a widely used uh data transfer library right now. Uh we also have model express uh which can speed up your model loading. Yeah. And so on.

**[19:06](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1146s)** Uh so with Dynamo enabled your inference structure will be like this. First of all, Dynamo provided a API server. So it compatible with open AI API and beneath it, it will use a KV cache aware router. uh I will talk about it later and beneath the KV cache aware router is your actual uh actual workers and I want to highlight that uh your you you will have many preview worker and the decode workers and also this uh every preview worker is visible to every decode worker and vice versa. So this is important because it provides some sort of uh some level of fault tolerance and also you use model express to speed

**[19:56](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1196s)** up your model loading and you can use nixo to handle the KV cache transfer between different nodes. Yeah, etc. So what is the KV cache a viral router? So since you have many different workers so when a request new request come so how do you choose uh which worker it routes to. So Dynamo provides this very useful KV cache aware router. So whenever a new request come uh first the router has been keep uh has been tracking the status of every worker. So it will first see uh how much this new request match uh the KB cache already on the workers and also it will check uh how much this

**[20:45](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1245s)** worker has been loaded. Then it will use a cost function to decide which is the best uh worker it routes to. And furthermore, I want to highlight that Dynamo provides fault tolerance at different level. So for example at your front end and router level uh these routers they share states with each other. Therefore if a router dies the other available routers can take over that router's request. And for the workers since I said before every preview worker is visible to every decode worker and vice versa. Therefore if a worker dies its counterpart worker

**[21:34](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1294s)** can find a healthy worker to continue on the work. Uh and furthermore Dynamo also provides a uh cancellation throughput. So basically if the user cancel the request or cancel the true calling uh the workers will know and stop uh proceeding with the generation. Therefore you won't re uh won't waste your computer resources. Uh and furthermore if you know this okay but if you the GPU on the node dies uh Dynamo is capable of migrating the request and KV cache to another healthy node. uh therefore you won't lost your requests and start from the beginning and lastly

**[22:24](https://www.youtube.com/watch?v=yHuR4iRe73Q&t=1344s)** uh Dynamo 1.0 focuses on tax models uh but in the upcoming Dynamo 2.0 we will also uh highlight on multimodality diffusion agentic and reinforce learning etc. Okay. So, this is the end of my presentation. Yeah. Thank you.
