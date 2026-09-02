---
id: Boz5u4-61XI
title: "How Xoople Scales Python for AI using Anyscale on Azure | LIVE148"
slug: how-xoople-scales-python-for-ai-using-anyscale-on-azure
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Milos Colic", "Nate Waters"]
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-05T15:32:11Z
video_id: Boz5u4-61XI
url: https://www.youtube.com/watch?v=Boz5u4-61XI
youtube_url: https://www.youtube.com/watch?v=Boz5u4-61XI
tags: ["How Xoople Scales Python for AI using Anyscale on Azure | LIVE148", "LIVE148", "LIVE148_v1", "Milos Colic", "Nate Waters", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# How Xoople Scales Python for AI using Anyscale on Azure | LIVE148

**Milos Colic, Nate Waters**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#How Xoople Scales Python for AI using Anyscale on Azure | LIVE148` `#LIVE148` `#LIVE148_v1` `#Milos Colic` `#Nate Waters` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=Boz5u4-61XI) · [Conference site](https://build.microsoft.com/)

## Description

Python is the backbone of modern AI workflows, but scaling Python across data processing, training, and inference introduces real distributed systems challenges. In this customer conversation, Xoople’s VP of Engineering shares how their team moved from early distributed Python approaches to running production AI workloads with Ray on Azure.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Milos Colic
* Nate Waters

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE148 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Overview of Any Scale integration as managed Ray platform on Azure
00:03:14 - Discussion on Zoople’s AI stack, data ingestion, training, and inference using Any Scale on Azure
00:03:48 - Summary of hybrid and heterogeneous computing benefits in Zoople’s AI operations
00:05:15 - Scaling image processing across trillions of pixels
00:06:19 - Focus on delivering business value instead of managing clusters
00:07:48 - Discussion on scaling Python-based AI systems
00:09:31 - Excitement about generative AI augmenting engineers
00:10:56 - Collaboration between product, application, and platform teams
00:11:16 - Adoption of AI tools like Copilot on Azure across teams

## Transcript

*2,447 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Boz5u4-61XI&t=0s)** NATE WATERS: Hi, I'm Nate Waters. I work in Product for Azure, and I'm here with my good friend, my new friend, Milos Colic joining us from Xoople, and we are here to talk about scaling Python AI workloads on Azure. So Milos, would you please tell us about Xoople? Who are you guys? What's your company about? MILOS COLIC: Sure, Nate, and thank you for having me, this wonderful issue of Build this year. It's really nice to be here at San Francisco. Sure, Xoople, we are a Spanish-based startup, but we are a global company, and we are bringing to the existence Earth system of record. What we mean by that is Earth data infrastructure layer built specifically for the era of AI. The focus of this data layer is to enable AI, and agentic AI,

**[0:52](https://www.youtube.com/watch?v=Boz5u4-61XI&t=52s)** to reason about things that happen in physical world and empower businesses to make better high-stakes critical decisions about the physical assets they may have displaced in the world around us. NATE WATERS: That's great. You're joining us all the way from Madrid. Thank you for making the trip out to San Francisco. Tell us about Xoople's customers. You're taking satellite imagery and doing lots of training and inference, but who are the customers you're surveying or what is the Xoople product? Can you tell us about that? MILOS COLIC: Yeah, well, I kind of touched a little bit about it when I said the physical world, that should be your anchor to our customers as well. It's pretty much covering multiple verticals because many businesses across agriculture, across insurance, across critical infrastructure and similar businesses

**[1:46](https://www.youtube.com/watch?v=Boz5u4-61XI&t=106s)** that have physical assets that are at risk will be very much interested in this data layer that allows AI to reason about those assets in the real world. Maybe an example of a use case that could be quite interesting, if you have a large infrastructure project, maybe a larger railway network being built, you're working across multiple states or multiple counties, it's hundreds of miles of corridor, and things happen around you. The world evolves as you build. Other companies might be building other infrastructure. There might be legal buildings. There might be vegetation that went out of control. All of those things can have a negative impact on your ability to deliver the value that you have to your stakeholders.

**[2:38](https://www.youtube.com/watch?v=Boz5u4-61XI&t=158s)** So how do we enable these businesses to make timely decisions against their roadmap, both physical and logical, it's where we shine. NATE WATERS: That's great. And one of the new announcements we're here to talk about, Xoople has been a great customer of ours, for a new announcement called Anyscale on Azure. Now, Anyscale on Azure is all running on Azure Kubernetes service. It's bringing the open source distributed compute framework Ray into Azure. And so Anyscale is, of course, the managed platform for Ray, and we have a great partnership with the Anyscale team. Could you talk with us about Xoople and your AI stack and how you're maybe using Anyscale on Azure, from data ingestion to training to inference? MILOS COLIC: Yeah.

**[3:25](https://www.youtube.com/watch?v=Boz5u4-61XI&t=205s)** So I think from that perspective, both the Azure as a platform and Anyscale have been very good tools and assets for us to execute against our vision and our product strategy. Where I believe this tool and this platform has empowered us to deliver the most value, I think it's in the combination of hybrid -- sorry, compute, meaning combining CPUs with GPUs, and CPUs are very valuable when you're preparing the data, but then GPUs are needed for executing your large models or your foundational models. Where that, for instance, fits very well with an exemplary use case is you pick up off-shelf models within this domain.

**[4:16](https://www.youtube.com/watch?v=Boz5u4-61XI&t=256s)** A famous one would be TerraMind. It's been built by IBM together with NASA, and this is a big model. This is a foundation model territory. You need GPUs to run it, and you will get some embeddings. Once you get those embeddings, you can actually classify the patches against those embeddings and cluster them in groups, and you can do a few-shot labeling and then get your own classification of how is the land mass being used within the areas of interest. Obviously, that sounds very easy when you say it this way, but you need to move large images. You need to move images that don't have only red, green, blue. They have multiple spectral bands. In many cases, 10, 15 or more, and so it's multimodal. It's different.

**[5:06](https://www.youtube.com/watch?v=Boz5u4-61XI&t=306s)** It's big. It's heavy. Images can be hundreds of megabytes. You need to chunk it up differently. You need to spread it out, and you need to, yeah, scale it. NATE WATERS: Across trillions of pixels. MILOS COLIC: Across trillions of pixels. Actually, that's a very nice number. That, for example, is just Spain for less than a year worth of data, and it's just the beginning. NATE WATERS: Yeah. Well, so tell us about getting started with Anyscale on Azure. Of course, there's a lot of open source frameworks you can go through, but it kind of creates this trade-off of build versus buy, and with you as really one of the leaders of the engineering team, how did you approach that? MILOS COLIC: I think that's an interesting question, and I know there will be multiple schools of thought here, and I'm not going to preach that the one is right or the other one is wrong. I think there is a time and place and maturity

**[5:55](https://www.youtube.com/watch?v=Boz5u4-61XI&t=355s)** of the organization and the size of the team. We are a young company. We have a young and growing team, and I think in our case, buy was a better option than build, and I would say also it matters on how close you want to be to the value you're delivering. You want to spend that valuable engineering hours as close as possible to the value. We are not there to compete about being the best generic distributed system platform out there. We're there to deliver the value that they described in the -- NATE WATERS: You don't spend time managing clusters, where you're not matching, and updates. You just get direct access to the GPUs and CPUs that you require. MILOS COLIC: Exactly. NATE WATERS: Yeah, and so why don't you share some of the outcomes that you've had from this? You've been running with Anyscale on Azure for a while.

**[6:44](https://www.youtube.com/watch?v=Boz5u4-61XI&t=404s)** Can you talk about GPU utilization or some of those? MILOS COLIC: Yeah. So I think that's a good situation, and it also kind of allows me to talk about two value threads in this partnership with Anyscale. One was that we actually got some Forward Deployed Engineers from Anyscale working together with us. I believe that is a very, very positive experience when working with a vendor within Azure ecosystem, and I know Microsoft is a big proponent of that mechanism as well. I think that allows you to be very tightly coupled with your partner and learn from them, and who's better to learn from than the ones building the platform itself, the tool itself, and what that actually allowed us was to really squeeze the juice out of the GPUs that we were using in the pipeline.

**[7:33](https://www.youtube.com/watch?v=Boz5u4-61XI&t=453s)** So we were getting into high 80s or 90s percentage of the utilization, and the handshake between the CPUs and loading the data into the GPUs, that was something where that partnership has really landed well for us. NATE WATERS: That's great. And so you have a lot of scale, or a lot of experience scaling up all of these Python AI systems. For the other developers out there and maybe startups who are just getting started, what is the recommendations that you would have? You've been doing this for many years across a lot of different technology stacks. What advice do you have out there? MILOS COLIC: The way I would think about it is you need to think in the smallest solvable units of your problem. Because when you're scaling, it's about parallelism. It's about things that can happen independently one from another.

**[8:21](https://www.youtube.com/watch?v=Boz5u4-61XI&t=501s)** If you ever spent any time thinking about languages like Scala or Lisp or similar type of languages, and I'm going now a little bit on a deep end, but they had this notion of Amona, the thing that is like, there's a field theory, there's a mathematical thing, but basically things you can operate on in parallel and that allows you to get that very, very high scale. So when you're approaching your problem, you need to really think about something it can solve that is the smallest unit, that then you can issue millions of those units and scale it that way. If you can decompose your problems in such a way, that also can lend itself into very easy roadmap planning because you're thinking in a divide and conquer type of perspective. NATE WATERS: Right. I think that's what I've been so excited about at Build. There's so many of our announcements, and this Anyscale

**[9:08](https://www.youtube.com/watch?v=Boz5u4-61XI&t=548s)** in Azure announcement, it allows you to find that smallest solvable unit and get so much closer to the application layer. You don't have to worry about the infrastructure or the scaling problem, but it just brings you all there. So that brings me to my next question is, what are some of the tools and innovations that you've seen maybe today or that you're just looking forward to in the future to help you and your development team? MILOS COLIC: I'm very, very much excited, and obviously in an event like this, this is not going to come as a surprise, but I'm really excited about agentic as extension and augmentation of an engineer, and I'm specifically saying engineer and not the coder. I think that as we go into the future, we're going to start expanding quite a bit beyond code into this true -- and we already are, but like, I think into system design and to organizational design

**[9:59](https://www.youtube.com/watch?v=Boz5u4-61XI&t=599s)** as well, which every developer will start being like a manager of these agents as well in a way. And the ratio between product managers and engineers and these augmented engineers is going to probably get more closer to one to one, and I think that's going to get us into this mode of hyper-velocity, and I've been talking lately about velocity. Think faster. Think agents talking to each other, agents forming teams, think cross-evaluating one being a judge, one being the pentester, one being the actual coder, and then all of them working together with a human in the loop that can make sure that this is hardened together with their product counterpart. I think that's the axis that I'm excited about. I don't think we're going to be here today, tomorrow, but I don't think it's that far into the future either.

**[10:49](https://www.youtube.com/watch?v=Boz5u4-61XI&t=649s)** NATE WATERS: But you're starting to see, as a small, almost engineering team, very -- a lot of this being implemented today, though, as in you have your PMs, your application, your platform teams all working much more closer. Is that right? MILOS COLIC: Yeah, I think, as I said, we're a young, small company, but very modern in that sense. We really think in the product-led perspective, and we are AI-native company as well. We embrace that. So tools like Copilot and Azure, it's rolled out pretty much to everybody. So we do use and leverage AI both in the pipelines, as picking up FMs and scaling them up, but also the way we code is augmented by AI in its purest form. NATE WATERS: Yeah, well, let's see.

**[11:37](https://www.youtube.com/watch?v=Boz5u4-61XI&t=697s)** So what are some of the recommendations you might have for people starting with large unprocessed volumes of data? Maybe you want to start your first training workflow or you have an app that you're looking forward to getting into inference. Where are you seeing some of the best places to start that? MILOS COLIC: So I think I would go back probably to my smallest solvable problem. I think where things get a little bit out of hand for some people is when they start going -- the first thing they go is, "Let me compare the metrics and the KPIs, and this model is faster, and this model is bigger, and this model is more number of parameters, and it has a longer embedding vector." I usually would say start from the value of what are you trying to solve?

**[12:27](https://www.youtube.com/watch?v=Boz5u4-61XI&t=747s)** If you are in this space, I would also probably point you towards Uri Levine, the founder of Waze. He has this amazing book called "Fall in Love with a Problem, Not a Solution." Models are fundamentally a part of the solution, not a part of the problem. Find your problem, understand the value, and then start understanding if this tool that you have answers that problem and to which degree. Get to your smallest solvable problem, get your minimum viable product, and iterate. And don't try to boil the ocean. I know it sounds like a cliche, but it happens way too often still. NATE WATERS: Yeah. How have you found leading with Anyscale in Azure, a lot of the integration that the two companies have really brought together, you mentioned the partnership

**[13:15](https://www.youtube.com/watch?v=Boz5u4-61XI&t=795s)** with the Forward Deployed Engineers. Can you talk about what it's been like to work with Microsoft in the partnership and also with Anyscale as these two teams have really come together to offer this new kind of joint offering? MILOS COLIC: Well, I mean, one thing that we say pretty much both internally and externally is that we are a partner-first company. We really truly believe in the power of partnership. So seeing some of our partners coming themselves close to each other makes things better for us and easier and smoother. So we're very excited about where the two of you are going and where we can benefit from the things you do in your partnership and the things that we can benefit from. NATE WATERS: Well, we can't thank you enough. Thank you so much for traveling all this way to be at Microsoft Build.

**[14:02](https://www.youtube.com/watch?v=Boz5u4-61XI&t=842s)** We are so excited for all the announcements, and please go give a tryout to Anyscale on Azure. It's now available today in public preview, and we'll send it back to the rest of the team. MILOS COLIC: Thank you for having me. It was lovely to be here at Build. NATE WATERS: Thanks, Milos. MILOS COLIC: Thanks, Nate.
