---
id: WQuFQ3eJ_c8
title: "Build AI across client and cloud with AMD ROCm and Microsoft | BRKSP93"
slug: build-ai-across-client-and-cloud-with-amd-rocm-and
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Anush Elangovan"]
channel: "Microsoft Developer"
duration_min: 18
published_at: 2026-06-09T05:09:26Z
video_id: WQuFQ3eJ_c8
url: https://www.youtube.com/watch?v=WQuFQ3eJ_c8
youtube_url: https://www.youtube.com/watch?v=WQuFQ3eJ_c8
tags: ["AI", "API", "Anush Elangovan", "BRKSP93", "BRKSP93_v1", "Build AI across client and cloud with AMD ROCm and Microsoft | BRKSP93", "Developer", "Developer Frameworks", "Developer Technologies", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Build AI across client and cloud with AMD ROCm and Microsoft | BRKSP93

**Anush Elangovan**

`Microsoft Build` · `Build 2026` · `2026` · `18 min`

`#AI` `#API` `#Anush Elangovan` `#BRKSP93` `#BRKSP93_v1` `#Build AI across client and cloud with AMD ROCm and Microsoft | BRKSP93` `#Developer` `#Developer Frameworks` `#Developer Technologies` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=WQuFQ3eJ_c8) · [Conference site](https://build.microsoft.com/)

## Description

As AI moves from experimentation to production, developers need practical ways to build, test, and optimize workloads across client, cloud, and on-prem environments. Learn how AMD ROCm™ provides a common AI software foundation across Radeon™, Ryzen™ AI, and AMD Instinct™ platforms. See how integrations with PyTorch and ONNX/MIGraphX enable portability with fewer code changes while optimizing performance for each target.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Anush Elangovan

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

BRKSP93 | English (US) | Developer tools & frameworks

Breakout | (300) Advanced

#MSBuild

Chapters:
0:00 - Focus on execution velocity as the key advantage in modern technology
00:02:30 - Shifting value from syntax implementation to intent-driven execution
00:03:21 - Parallel Development and Accelerated Feedback Loop
00:04:09 - Building a Unified and Pervasive Software Layer
00:10:07 - Enhanced Model Support and Memory Capabilities on AMD Platforms
00:12:04 - Explanation of client application architecture and proxy workflow
00:13:49 - Description of loaded models for domain classification, jailbreak, and PII detection
00:15:00 - Handling private data routed to local model for security
00:15:46 - Configuration flexibility for routing queries between models

## Transcript

*2,010 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=0s)** Good afternoon everyone. Can you hear me OK? Perfect. Awesome. Thanks for joining us this afternoon. So we are going to speak about AMD, AMD software stack, Rakim and more importantly A pervasive software platform that goes from client to cloud. So we are going to talk about, you know, speed, speed of execution in the in, in the era of AI and why execution speed matters most. Then we will talk about the Rockham stack itself, unified AI software layer, which is fully open source and, and is available for everyone to like hack on move at the speed at which you can execute.

**[0:51](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=51s)** And then talk about some, you know, tidbits about AI in production, right? So why is speed the mote? So I think one of the things that we got to, you know, recognize as previous platform shifts took years to play out mobile Internet, all of this were like it played out over years and you could actually adapt to it over, you know, multiple months of processing such a change, right? If you looked at, you know, the mobile transition cloud, all of them were were, you know, multiple years in motion, but this time it is it is happening in mere months or even weeks. Something that was like really important last week is no longer important today, right?

**[1:40](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=100s)** Models that that everyone was talking about is is you know, I do not know if people still remember like even six months ago rag was like the thing right Like and now it is like if you ask someone rag, they are like what rag right and it is moved on South fast. So the the advantage is not the technology itself. The advantage is how fast you can adopt to the technology. And when software becomes tokens, the advantage shifts to execution velocity right? And So what we want to focus on is execution velocity. And at AMD we are like super dialed into this to make sure that one, you have all the tools, all the software all and the ability to act at that speed.

**[2:30](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=150s)** And increasingly what happens is, you know, what you what you used to do for regular syntax implementation, all of that kind of disappears and value moves upstream to intent. So you start with what you want to do and you define what that is and then let agents operate for you, right. And then that is also why you can massively parallelize the wingspan of what you know strong individual contributors are able to do is immense. It is, you know, it is like it is like multi threading in AMD CPU core. You get like so many threads to operate on and each one is operating for you continuously and all of this like compounds right.

**[3:19](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=199s)** And so when you execute in parallel, what you are doing is you are actually evaluating in parallel, you are building in parallel, you are testing in parallel. And all of this moves fast. And then that starts to compound with the feedback, you know, brought into the into the entire pipeline. So let us take a look at what AMD's software stack and hardware stack looks like. So AMD's hardware is pervasive. AMD is uniquely positioned in laptops, desktops, workstations, edge AI, physical AI, cloud and data center across the entire spectrum of compute. You have AMD's presence with this pervasive AI hardware layer. Now what we are doing is building a pervasive software

**[4:12](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=252s)** layer. And So what this provides us is the ability to operate not just in a in your personal space on your laptop, on your desktop, but increasingly, you know to burst into other areas of, of compute like the cloud footprint or AMD instinct GPU's in your data center. So Rokom itself has a deep philosophy that we we all rally around, right, which is it is open. We strongly believe that open source allows us to not just move fast, it lifts the boat for everyone, right? It is a, it is a common, it is a common good.

**[4:59](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=299s)** And so the philosophy of open is very important for us at Rockham. And then increasingly what we had been investing in is abstractions right? Whether it is kernel programming, inferences, inference engines serving. And what this provides us is the ability to kind of give you the right layering for developers to rely on our SDKS and our platform without having to worry about the details. And when you get to things like kernel programming, you know, using languages like Triton allows you to get away from very, very deep nuances of of the GPU or. For you to build on top of Onyx Runtime Gen.

**[9:37](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=577s)** AI with there are some banner numbers with this. With the new ROKM EP, we see about like 3X faster prefill and about 40% faster decode using the ROKM EP and I think that will have an immediate impact in anyone using a MDGPUS. It also supports unified memory on Ryzen AI for Apus and up to models even larger than 100 million parameters. And the impact of all of this is that you can enable a variety of dense and Moe models on AMD platforms just seamlessly. So with that said, let's talk about a little bit more on use case driven routing solutions. This is a very interesting and exciting topic because you

**[10:29](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=629s)** know, until now you had to build, you had to choose, you had to either use a frontier model and I'm sure you know, you dread seeing the user limit when you hit it or, or the API throttling on the other side. It's not your problem. It's still the the service is throttled. So what we have built is like a, a solution that can start with seamlessly like processing your intent and then routing to either local LLMS or to cloud providers. Not just for cost reasons, but also for, you know, privacy reasons and being able to like give you a scalable burst capacity of thinking burst capacity of, you know, just cost event, right?

**[11:21](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=681s)** Like it's like when you when you need to do your quote UN quote ultra think it's OK to go to the frontier model. But for most of your set and search and and grep, it can all run locally and you can save a lot of API calls just going up to to the cloud. So what we are going to do in in a couple of slides, we are going to show you a demo of this. But yeah, so this gets you the ability to go from, you know, different prompts and go through your semantic router, your Lemonade SDK, and then to, you know, the corresponding back end. So just walking that forward a little bit, you know, this is a little overview of how we would be

**[12:10](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=730s)** doing hybrid workflows. And so your client applications which are your web, e-mail, internal tools, etcetera, use your normal open air endpoint and it is terminated on your, you know, on by proxy with the VLLM semantic router. And then that allows you to, you know, select which model you want to hit in the back end and that pairs up with the Lemonade router. And that gives you the ability to choose, you know, based on the complexity, the task, what which of these models you want to pick up, right? And that could be your Quen 3.5 or, or any cloud frontier models that you want to leverage. So now that we have this, let us see if we can see this in a live demo. I am going to get Satya on stage. Satya, come on.

**[13:05](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=785s)** Thank you Anush. So this is a live demo of what Anush has just shared. So for this we are using VLM Semantic Router. It is an open source framework from VLLM. So what it essentially does is it takes an LLM text and then routes it to a right model at the right time. So it does this using predefined configuration file where we define our routing logics. So as you can see here we have a bunch of layers where we define domains, keywords and complexity, context length, and then like Anush was saying, we also define our jailbreak and PII prompts. And based on these routing layers, the router decides where a specific prompt has to go to. So we have three models loaded here. 1 is for classifying a given prompt into 14 different

**[13:57](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=837s)** domains like computer science, sociology or biology. These are some of the examples. And then we also have a jailbreak detection and also PII detection. So this is the brain of the VLM semantic router. So if we take a look at one of the So if we take a look at one of the layer where we have a jailbreak and PII, so this gets routed to a local model running on the Ryzen AI laptop. And for any other complex prompts, it gets routed to a cloud model where we have Azure plugged in. So if we go to the playground and then I'll start with a simple prompt like my phone number, no.

**[14:57](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=897s)** So the idea is since I'm sharing a private data, it is supposed to go to a local model. So as you can see it flagged it as a sensitive PII and then it went to a laminate server. So this is an open source server that we built at AMD. It runs efficiently on our AMD hardware and as you can see it loaded a quaint 3.59 B model and all the entire prompt got processed locally. Now, if I send a complex question which might, which might not need a local model. So the idea is this should go to a cloud model. So in this case, it's going to a GPT 4.1 mini. So this is hosted on Azure and we can efficiently tune our configuration file, this brain to route our questions between any any set of models.

**[15:48](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=948s)** As long as you know, the model is exposing an endpoint. Let's go back and it's still running. Yeah. That's it. Thank you. Thanks Satya. Thank you. So I hope that was not your real phone number, but as you can see in the demo that Satya showed us, right, we have, oh, I think is that good? That's still the demo. Oh, that's OK. So as as you can see in the demo that

**[16:40](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=1000s)** Satya showed us the the the ability to like semantically choose which model you hit and where you hit is an important part of our overall client to cloud story. This allows you the flexibility and the security to use the morals that are most relevant for your task with the safety that safety guards that we want to have in place, like your phone number or Social Security number that you do not want to expose in a public setting. With that said, I think our, our, you know, our key take away message now is like software is now tokens and time. And what that literally means is, you know, if there is any, any gaps in anything that you see, which is attributed to software, it is a matter of time

**[17:31](https://www.youtube.com/watch?v=WQuFQ3eJ_c8&t=1051s)** and just applying the right tokens. With that said, we definitely at AMD are like super focused on applying those tokens to cover the entire breadth of software from our Rackam EP to our client to cloud story and just base enablement of the entire software stack to agents. Increasingly we think it is going to be a very agentic world and that is fast accelerating and we are here to like support that. So with that, I think, you know, I'll wrap it up if there are any questions, happy to answer any questions, you know, just we'll see if there's cool. Thank you.
