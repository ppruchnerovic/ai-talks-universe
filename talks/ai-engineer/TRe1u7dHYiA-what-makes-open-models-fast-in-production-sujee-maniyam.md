---
id: TRe1u7dHYiA
title: "What Makes Open Models Fast in Production — Sujee Maniyam, Nebius"
slug: what-makes-open-models-fast-in-production-sujee-maniyam
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Sujee Maniyam"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-03T22:30:28Z
video_id: TRe1u7dHYiA
url: https://www.youtube.com/watch?v=TRe1u7dHYiA
youtube_url: https://www.youtube.com/watch?v=TRe1u7dHYiA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "LLM inference", "open source LLM", "open models", "inference optimization", "speculative decoding", "KV cache", "prefill decode disaggregation", "quantization", "NVFP4", "model serving", "vLLM", "Nebius", "Nebius Token Factory", "Sujee Maniyam", "AI Engineer"]
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# What Makes Open Models Fast in Production — Sujee Maniyam, Nebius

**Sujee Maniyam**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#LLM inference` `#open source LLM` `#open models` `#inference optimization` `#speculative decoding` `#KV cache` `#prefill decode disaggregation` `#quantization` `#NVFP4` `#model serving` `#vLLM` `#Nebius` `#Nebius Token Factory` `#Sujee Maniyam` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=TRe1u7dHYiA) · [Conference site](https://www.ai.engineer/)

## Description

Open models have nearly caught up with proprietary ones. Serving them fast and cheaply is the hard part.

Dylan Bristot, who leads product marketing for Nebius Token Factory, and developer advocate Sujee Maniyam explain what it takes to run open LLMs in production. Dylan covers the trade-off between closed APIs and self-hosting, and the inference → data → post-training → deployment loop. Sujee then goes layer by layer through the optimizations behind fast inference: NVFP4 on the latest NVIDIA hardware, engine selection, cache-aware routing, speculative decoding with custom draft models, KV cache offloading, disaggregated prefill and decode, and finding the quantization sweet spot.

In this talk:
• Why open models are now competitive, and what that means for cost and lock-in
• Cache-aware routing versus naive load balancing for LLMs
• Speculative decoding and training draft models on your own traffic
• KV cache offloading, prefill/decode disaggregation and quantization trade-offs

SPEAKERS
Sujee Maniyam, AI Developer Advocate, Nebius
X: https://x.com/sujee_dev

Dylan Bristot, Senior AI Product Marketing Manager, Nebius

LINKS
Nebius Token Factory: https://tokenfactory.nebius.com/
Token Factory docs: https://docs.tokenfactory.nebius.com/quickstart
Nebius: https://nebius.com/

CHAPTERS
0:00 Intro
0:12 Engineering open LLMs for production
0:52 Who is Nebius
2:27 Nebius Token Factory
2:42 Closed APIs vs self-hosting
4:06 The full loop: inference, data, post-training, deploy
6:21 What we handle so you don't have to
8:06 From running models to improving them
10:01 Scaling open models to production
10:26 How good are open models?
11:26 Teacher and student models
11:46 Hardware layer: NVFP4
12:26 Choosing the serving engine
12:55 Cache-aware routing
14:24 Speculative decoding
15:29 Training custom draft models
15:59 KV cache and offloading
17:33 Disaggregated prefill and decode
18:13 Finding the quantization sweet spot
18:43 Recap
19:22 Try Token Factory

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*4,023 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1s)** [music] Thank you for joining us today. Um I'm Dylan. I'm here today with my colleague Suji. So I lead the product marketing for Nibbius token factory and I'm here with Suji as a developer advocate and we're going to talk a bit about engineering um open NLMs for production. So before we jump right in, um I want to give a few words about what we're going to cover today. We only have 20 minutes, so we'll try to keep this brief. Uh but we're going to give you a quick intro on who we are, what we do. Uh then talk about what it takes to build the infra for inference. Um a few words on model shaping optimizations, which are extremely important in what we do. And then we'll talk about model serving

**[0:49](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=49s)** optimizations. But before we jump right in, I just want to give a few words uh about who we are and what we do. So we work for Nibbius. Uh so specifically Nibbius token factory but Nibbius is a like a full stack AI cloud infrastructure. Um so this means we actually not only exposing model APIs we run the actual physical uh AI layer and infrastructure underneath it. Um we have our own data centers and video systems uh bare metal capacity manage cloud and optimizing the serving and the inference through Nibius token factory. Um top top row here is really about scale and trust. So we're a publicly traded company on the NASDAQ um headquartered in Amsterdam. Uh we're very close with Nvidia who made a 2 billion uh investment in Nebus a couple months ago and we're targeting a 5 gawit

**[1:38](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=98s)** of Nvidia systems by the end of 2030. Uh bottom row is really more about the control of the stack. This is a quite a a good edge we have. We operate own data centers across the EU and the US uh bare metal rather than shared cloud. We're a very early adopter of Nvidia Rubin um CP like uh and bluefield storage and we were amongst the first European clouds to run both Blackwell Ultra AGXP300 and GB300 in production. Uh we also have um like strong contracts from Microsoft and Meta agreements that kind of show that the largest AR builders are already building this kind of capacity from us. Um and the last time is quite important. It's the uh like really the important bridge to this talk is the vertical integration from silicon to serve that we um rely on.

**[2:28](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=148s)** So today we're talking about NEA token factory. So the idea here is to like really uh engineer AI for product. So we're managed inference company uh meaning we deploy these models and optimize them for our customers. So we noticed a few things today in the market of serving open source LLNs. Um, usually most AI teams are stuck between choosing two bad options. Um, closed APIs are really easy to start with, but you often hit a ceiling really fast and you can't really tune the model to your specific use case. Uh, you share the infra with everyone else. So, it kind of operates as a black box black box and the costs grow in a straight line with no way to really optimize things. The other option here is self-hosting. Obviously, it's quite fun. Uh, gives you full control on the model, but it's a massive engineering project. Um so you really need a dedicated team to actually

**[3:16](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=196s)** keep it running. Um and you're usually month away from production before you even start your actual product. So token factory is kind of the shift uh this third path we identified uh before you even start like on your um actual product. You get the control and the performance of self-hosting with the simplicity of a manage inference service. So we do the heavy lifting, the hard infrastructure work and then customers stay focused on their product. This really unlocks uh three main things performance, cost and behavior of the models. Um as we've seen the gap between proprietary and open source models has been closing a lot and so this is where we kind of operate and we feel comfortable um operating is really not only relying on the fact that this bridge and this gap is closing down but also figuring out how you actually make it work in your own production uh use cases.

**[4:04](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=244s)** So this is really the core of token factory. uh we've built a full stack JI platform. Um most platform we've seen on the market either give you inference training uh data tooling but here we decided to connect everything under one loop. So we have a bunch of tools to that kind of unlock this on the inference side um we allow you to run models in production. So we have 60 plus models on the platform JLM Kimmy DC you name them. Um we have dedicated endpoints we have different flavors on the models depending if you want to run them fast. uh we have different tooling like structured outputs, function calling and batch API. Second layer here is the data lab. So this allows you to really capture and structure the production logs. So we see a lot of customers actually running these models in production importing the completions and wanted a way to kind of slice and dice through these completions and this is really what we allow with the data

**[4:52](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=292s)** lab. So uh inference log imports SQL data like uh data set filtering, data set versioning, um exporting and then batching. These uh third layer is post training. So we allow you to kind of fine-tune distill optimize these models. So this is a natural follow-up with the data lab is once you have your logs and your inference and you can generate synthetic data sets you can bring them all to post training and use that to kind of either through Laura or full fine tuning make the models much more adapted to the behavior you're expecting from. Uh we also allow model distillation. We do custom spec decoding for customers who need really advanced um custo custom spec decoding tooling. uh we do like on demand and like specific quantization and calibration of the model depending on your preferences and we do our our GPO and the fourth layer here is the

**[5:40](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=340s)** deployment. So once you like run these models once you like train these models you need a way to deploy them. So these this is what allows us to push the models into production on our own um owned infra. So for most teams this is kind of usually a choice of different tools that you stitch together. But that's creates kind of a lot of friction and need for iteration. It slows the need for like the the ability to iterate here. And so what we allow is really to make the data flow from u the inference to the training and the training flows directly into production. So that allows you to keep like a virtuous loop of your product. And that's really what I think is the main difference between uh running a model and running an actual production uh AI system. Um so here is a little slide about what we handle so you don't have to. Um so running models in production is actually

**[6:28](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=388s)** quite complicated. It takes a lot of work and so I think uh the way we approach it the value here is in three main layers. The first one is the optimization. So we actively tune how models run so the customers get much better speed and lower co and lower costs without having to figure out um all of that themselves. Like we really do the heavy lifting around the model deployment and optimization and really allow you to kind of uh come in and just play with them. This is like all around optimizing latency, throughput and cost at the actual engine level because you could be running the same open source model on different providers and have completely different um results in terms of costs. So there's a lot of technical stuff that goes on under the hood uh to make this work and Suji will cover that in a few minutes. Uh second layer is the infrastructure. So the fact that we actually own the hardware uh we keep it running. We own this like kind of

**[7:15](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=435s)** vertical stack um gives us an edge that uh most providers don't have. So it's it's it's the control like we really control what the model does. Uh we handle like everything underneath and so we just give the the customers um the full control of the behavior and we take care of the infrastructure. Third layer is the enterprise readiness. I think this is really important here because like running open source seems kind of obvious but you need a bunch of ways to like secure like make it make sure it works in a secure environment. So there's a bunch of things here. Um security compliance reliability they all requirements that all these large companies usually have. Um and they kind of need those before they can ship anything into production. And so a lot of AI providers make you figure out all of these yourself. And uh our mission here is to really handle all of these so

**[8:03](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=483s)** you don't have to. Um something that comes up a lot with AI teams is that they start with inference. um they just get a model up and running and then they realize that pretty quickly quickly that running it is not just as easy as it seems and it's only the beginning of your path through running open source models at scale. So they really need to understand how it's actually performing in the real world and this is kind of where we come in. They want to improve it over time. Um they need to redeploy updates without breaking things. Um, and and that full cycle from running to observing to capturing and to redeploying the model is really what separates team from that ship like great AI products from team that ship demos. And I think that's really important to hear especially when talking about open source. Um, and so token factory covers that full loop uh

**[8:52](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=532s)** inference to run the models. So as I said, Kimmy, Deepseek, all the all the main ones uh through real-time inference or batch inference through structured outputs and function calling um and on dedicated end points when it's necessary. Um and then moving on to the datab to collect and analyze the real world signal uh the completions, moving over to post training to improve and customize the model and finally moving to the last step and probably the most important one which is the deployment to push uh updates with full control over the model. And you actually really it's it's really important for most our customers to know where how it's running and what chips it's running on uh the level of quantization and all that stuff and that's really where we kind of operate uh and are comfortable. Most teams today we figured have to stitch different tools together to get this and we actually built uh one platform that tries and covers it end to

**[9:40](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=580s)** end. So we really see this as a continuous improvement loop. Every cycle makes your AR more specific uh way faster and much cheaper. And now we'll dive into scaling open models to production. And I'll invite Suji on stage to take it over. All right. Thank you, Dylan. All right, everyone. So, um I'll zip through a few of these, but um I'm happy to um have a discussion afterwards. So, come and find us if you have any questions. So, we believe great inference starts with great models, but that's not enough. you need great infrastructure behind the scene to get the best performance and I believe that's what uh Nebio token fighter provides. Uh I get a lot of times I get

**[10:28](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=628s)** asked like so this is great you guys host open models but how good are the open models really and I like to show you this benchmark here. Uh this is from artificial analysis. The black ones are proprietary models and the blue ones are open models. And the cool thing you can see here is how um the open models are actually very competitive sometimes even better than a lot of the proprietary models. So the gap between uh proprietary and open models is very narrow. Uh so we don't really have to chase proprietary models all the time for the intelligence. You can just just as well choose an open model that's just as smart and also ends up being much cheaper in most cases which is pretty cool. So what does it mean for customers? You get choice, right? You

**[11:15](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=675s)** can run these open models in any provider, hopefully token factory, but so there's no vendor lock in and also you end up saving a lot of money on tokconomics. And here's a a few examples of models we host. Uh the top the top table is like the large models. We call them sort of the teacher models, right? They are very capable uh very smart but also kind of large. You can also use a large teacher models to train the smaller student models. So you sort of see the both large models and small models posted. So I want to sort of structure the talk a little bit um sort of the from the hardware layer, the serving layer and the optimizing layer. Uh so Dylan talked a little bit about hardware, we have we work very closely with Nvidia, we get the latest chipsets and uh not not just um the latest we also optimize uh

**[12:04](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=724s)** kernels and runtimes. So the models run really uh really well. For example, something like the Nvidia floating point. standard we embraced it. It gives us a really good model performance on latest Nvidia chips. And if you think about model serving that kind of takes us to the middle layer and there are few optimization I'll talk about uh starting with the engines because you need an engine to serve the model. Uh we utilize a lot of the open source engines. Uh we have our own internal folk uh that we continuously tweak and optimize and we will deploy the model on the best engine possible. uh you know not all the models run equally well on all the engines. So we figure out which engines run well and we'll deploy the models accordingly. So as a customer you can just use an API not having to worry about you know which

**[12:52](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=772s)** kind of GPU which engine because we take care of all that work behind the scene and uh when you have like hundreds of thousands of GPUs uh running models load balancing and routing becomes an issue. So a lot of the time people say oh that's easy right we just you know put a put a load balancer in front um send traffic randomly to different GPUs uh that's not how it works in LLMs because the workloads are slightly different for example just to kind of give you an idea uh in the early days of LLM the inputs were small I could just say write like a oneliner and the output is also small but now we are seeing your input could be pretty large like we are sending like large code bases uh as using coding agents to do like refactor or summarize or analyze right so the output as you can see can vary from like you know

**[13:39](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=819s)** large to small large to large and routing them accordingly will give you um you know it's not it's not trivial so what we employ is we employ um routers that actually are cache aware what I mean by that is like if you look at the left side here you will see that my cache like different colors it's kind of fragmented all over so our cache rate is isn't all that great because my request landing randomly at different GPU use that may or may not have the cache. But if you look at the the one on the right, you can see that now the cache is much more coherent. See the colors are kind of together and the router knows where the caches are stored and it'll route them accordingly. So when we actually do the inference, you get pretty good cache and very good speed. Um another thing and this is something we are really excited about. Um it's

**[14:27](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=867s)** called spec decoding. So the challenge is uh LLMs they generate tokens one by one one two three four right and then large models take a long time to generate these tokens. So the idea for spec decoding is how about we employ a smaller model which is a lot of the time faster and cheaper to generate the tokens but then have the large model verify at the end. So it's kind of like if you're like a senior engineer, you're kind of farming out the work to a junior engineer. So they're kind of doing the heavy lifting and then you are verifying the work. And this actually surprisingly scales really well. So the smaller models can generate tokens very quickly and the large model can verify and the and if it's good, we are done. If the large model doesn't like the the answer, it will actually regenerate the tokens

**[15:15](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=915s)** for you. So that's kind of the worst case scenario. But most of the time you will get pretty good performance out of this by mixing small models and large models. And this actually a feature we actually baked into token factory. Uh that gives you pretty pretty good optimization um speed. So one of the things we experimented we sort of trained graph models. Uh you can train them using synthetic data. Even if you train them using like you know generic data you get like you know we seeing like up to 30% improvement. But it it gets even better if you can train the smaller model using your own data. Right? So we do a lot of experiments here and u we are launching a feature feature. You can actually train these draft models almost like with one click and you know we will capture your production data and train the draft models for you which is pretty cool. Uh another optimization uh behind the scene

**[16:02](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=962s)** is KV cache. Um this is probably one of the biggest ROI in doing inference because uh creating tokens expensive especially when you're doing one at a time and the common sense is once you generate a token it it doesn't change. So there's no need to keep keep regenerating the same token over and over again. So the idea is we cache the tokens. So just to kind of give you an example here, let's say this is my prompt the cat sat on, right? Let's say the those are my prompts and I'm creating the next word and as soon as we create the next token, we cash it and the next time we need to look up, we don't have to regenerate regenerative, we just look up the cache very easy and this actually speeds up quite a bit. So just to kind of give you some ideas, we have seen uh speed ups anywhere from 5 to 10x, not just 5 to 10 percentage,

**[16:50](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1010s)** actually 10x, right? because caching really works well. Um the thing about caching is it takes a lot of memory right because you know especially with our large inputs large token windows and one thing we we we've been implementing in token factory is when we do caching we can actually uh because GPU memory is very precious. So we can offload caching out of GPU memory automatically save it in a regular memory and then bring it back. So we don't like throw away the cache we spend a lot of time building. we actually offload it and bring it back and all of this is done automatically. So you don't have to worry about managing cache. This is done for you behind the scenes. So and this is one of the um um one of the important optimization we have done to speed up inference. Uh another one is called decoding. Um so the way you think about

**[17:38](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1058s)** this is like there are two stages to LLM. So one of them is like sort of fill in the context that is very CPU intensive and then other one is actually decoding that is very memory intensive. And a lot of the time if you do them in the same GPU they're kind of computing for resources. So what we have done we sort of separate this two phases out. So one GPU set does prefill they are very you know uh compute efficient and the other one does uh boding that's very memory efficient and then they sort of transfer the KV cache in between and we have seen this is actually working working out pretty well. And another thing we do and and this is already you know already baked into our platform we also quantize the models uh and when we do quantizing you know we are reducing the precision. So if but we don't want to go too far right because

**[18:25](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1105s)** then your model starts you know quality starts getting degrading. So what we do is we do a lot of experiments to figure out like what's the kind of the sweet spot of a quantization. So you can run the models efficiently but not not degrade the performance too much. So, so all of these things are already built in and and there's a there's a few more and interest of time I'll sort of wrap this up here and these are some of the things we kind of covered uh spec decoding KV cache and when you do caching doing um routing that is actually cache aware and also pre-fill uh you know uh separating prefill and decoding cases and if you're using an API you may not realize all these works going behind the scene but they are right and this is what make up you know make a a inference platform really great to serve especially the large large models we are seeing like the one

**[19:13](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1153s)** trillion models we are seeing and finally I want to quickly um give this out so we um probably this is the most important slide of the presentation so we can take the take a quick picture or scan the code uh this will give you some credit on token factory platform so we allow you for allow for you guys to try it out and we have all the uh latest open source models uh GLM52 kit K27s. Uh try them out. I've been using them them a lot a lot for coding lately and they work really really well. So if you're using a cursor or open code um you can very easily incorporate our models to um for coding work. Try them out. Let us know. And there's a discord channel um at the bottom. If you have any questions you can post them there or you can um you know um message me or Dylan. We will happy to um answer your questions. Uh so

**[20:03](https://www.youtube.com/watch?v=TRe1u7dHYiA&t=1203s)** I'll stop here. We have like 10 seconds. >> [laughter] >> right on time, but uh we'll be around. Please come and talk to us if you have any questions. We'll happy to um chat more and then take any take your questions. Thank you all.
