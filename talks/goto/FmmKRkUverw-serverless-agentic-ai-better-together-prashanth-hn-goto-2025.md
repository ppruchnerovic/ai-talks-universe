---
id: FmmKRkUverw
title: "Serverless & Agentic AI: Better Together • Prashanth HN • GOTO 2025"
slug: serverless-agentic-ai-better-together-prashanth-hn-goto-2025
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: []
channel: "GOTO Conferences"
duration_min: 15
published_at: 2026-01-19T13:00:25Z
video_id: FmmKRkUverw
url: https://www.youtube.com/watch?v=FmmKRkUverw
youtube_url: https://www.youtube.com/watch?v=FmmKRkUverw
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTO Serverless", "GOTO Serverless Day", "Serverless", "AWS Serverless", "Event-Driven Architecture", "EDA", "Agentic AI", "Prashanth HN"]
topics: ["Agents & orchestration"]
transcript: true
---

# Serverless & Agentic AI: Better Together • Prashanth HN • GOTO 2025

**Speaker not identified**

`GOTO Conferences` · `GOTO` · `2026` · `15 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTO Serverless` `#GOTO Serverless Day` `#Serverless` `#AWS Serverless` `#Event-Driven Architecture` `#EDA` `#Agentic AI` `#Prashanth HN`

[Watch the recording](https://www.youtube.com/watch?v=FmmKRkUverw) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Prashanth HN - CTO and Co-Founder at AntStack & AWS Serverless Hero

RESOURCES

ABSTRACT
Agents are changing the way GenAI applications are built and has become a fundamental building block between data & LLMs. With a widely accepted standard like MCP, it is set to take off exponentially in the coming months/years. Agents by design are event-driven and are naturally fit into Serverless architecture.

In this session we explore how Serverless can be a huge part of empowering the upcoming Agentic revolution & why this combination is such a killer! [...]

TIMECODES
00:00 Intro
00:40 What is an agent?
04:26 Events
05:48 LLM inference
06:29 Agents/Tools/MCP
07:33 Data
08:46 Agentic RAG
10:06 Swarm
11:11 Agent orchestration
14:10 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ashley Peacock • Serverless Apps on Cloudflare • https://amzn.to/3EU7P85
Jeroen Mulder • Multi-Cloud Strategy for Cloud Architects • https://amzn.to/3FdNDOA

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*2,205 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=FmmKRkUverw&t=0s)** [Music] Today I'm going to talk about serless and agent AI and how they are better together. Uh I didn't know Nick is going to do so much in his keynote about agents and uh you know uh serless. So this almost looks like an extension to uh Nick's keynote to be honest. Uh hopefully I'll be able to add some value to you all and cover some some things which was probably not part of his keynote. Um like Nick mentioned it's all events right end of the day whether uh you look at um somebody using chatbot they are typing in some query and asking

**[0:50](https://www.youtube.com/watch?v=FmmKRkUverw&t=50s)** questions uh to the to the chatbot that's a that's an event coming from uh from the user and that event can actually then split into multiple subevents uh can do lot more processing and stuff like that. So even in the world of AI everything is just events uh at the core at the core. So what is an agent? We have uh events coming in uh which are coming to agents and agent is basically it has access to LLM so that it can do thinking and then on the other side it has access to tools. It could be a bunch of statically programmed tools. It could be another agent as a tool. It could be an MCP server which is exposing all the

**[1:38](https://www.youtube.com/watch?v=FmmKRkUverw&t=98s)** different tools to the agent. Then these tools will have access to underlying data, right? So you could probably have uh like if you are running a large enterprise business or any kind of business for that matter, you may have data sitting in different different places, you could expose those data to LLM or the agent uh through the tools. Right? So this is at the core what an agent looks like. It has access to tools. It has access to LLM and then through the tools it has access to data. Sometimes it may even have access to data directly through vector stores. U but the core at the core what what we see here is it's not a static workflow. uh it is the LLM's thinking can pick what tool to use for what kind of query

**[2:26](https://www.youtube.com/watch?v=FmmKRkUverw&t=146s)** and automatically use that uh for its execution and another thing here is what we call agentic is basically when you create a loop right so you have agent producing an answer then it goes through an evaluation see to check if that answer is good if it is not it goes back in loop and until it finds the right Answer. Last slide was little more simpler. Uh here you can look at multiple agents. You can look at one main orchestrator agent. They're like sub agents and each of these agents can have access to different LLMs, different data sets, different tools and stuff like that. Why is this important? Again it is very

**[3:14](https://www.youtube.com/watch?v=FmmKRkUverw&t=194s)** similar to microservices architecture like we are drawing parallels from our foundational way we architect things. There could be some agents which are doing very minuscule things which may not need very capable models right. So why you want to use the same model everywhere? So you can actually say okay for this agent which needs little more thinking complex there is more complexity uh use a much larger model much capable model then in different places you could switch to a smaller model and save a lot of cost and also improves the speed of your agent and at the same time uh you can also limit the tool tools available for the each agent like for example if you have u let's say a salesforce agent

**[4:02](https://www.youtube.com/watch?v=FmmKRkUverw&t=242s)** it may not need access to uh you know other parts of the data other parts of the tooling and stuff like that. So this way you will be able to control what each agent is doing and how what kind of access it has uh and stuff like that. Now you might be wondering I'm I'm just giving talk about agents agents uh how is serless coming into picture here. So like Nick mentioned it's all events and in AWS in in the serverless ecosystem we have so many components uh which are capable of managing events right so you have event bridge you have SQS which is Q which which is very good for decoupling uh you you have SNS to fan out you have API gateway and step

**[4:50](https://www.youtube.com/watch?v=FmmKRkUverw&t=290s)** functions so API gateway generally is uh used as a public gateway right so it's a front door where all of your queries are coming in u like whether it is you know front end request which is saying some user typed something and sent and that generally hits API gateway that's like the front door for most of our uh events uh then we have uh we have step functions I will go little more detail uh in in about uh in the upcoming slides about step functions But again step functions can be used to build agentic AI systems to orchestrate uh different parts of your uh agentic systems. Then we have event bridge we have SNS uh SQS

**[5:40](https://www.youtube.com/watch?v=FmmKRkUverw&t=340s)** and also ALB like if you are using containers ecosystem to run some of your workloads. uh when it comes to LLM inference uh we have uh AWS bedrock as well as uh SageMaker if you want to run uh models from hugging face and stuff like that right so uh again Bedrock is uh serverless you pay for the tokens u one great announcement which happened recently I think couple of days ago if I'm not wrong uh which is uh open um open weights model is now available on bedrock so that's a great news U so that's inference for you. So you will be able to hook up LLM models to your agents very easily and in a very serverless manner.

**[6:30](https://www.youtube.com/watch?v=FmmKRkUverw&t=390s)** Uh then comes the components which is like uh how do you run agents? How do you host agents? So there are several options again we have lambda functions which is which is really good if you want to you can you can access LLMs from lambda function and do a lot of things with lambda functions. Uh if you want something lot more long earning and stuff like that. Uh you can also look at ECS and target as a compute. Now any guesses on what is this squiggly little logo doing here? It does not look like it belongs in this slide. Yeah, a lot of some people got it right. Eric got it right more importantly. So yeah, that's that's trans SDK. You

**[7:18](https://www.youtube.com/watch?v=FmmKRkUverw&t=438s)** should absolutely check that out if you're building agenti. They have several different patterns uh lot of tooling makes your agent development really accelerated. uh when it comes to data again we we need uh for lag systems for example you need capability to store vectorzed uh data now you might be wondering what dynamob is doing here it does not have vector support right so but dynamob still can be used for memory right if you if you're building chat interfaces you need to keep track of what the previous conversations are and dynamob can be a huge good uh uh backend data platform for you to use. And then we have uh Aurora

**[8:08](https://www.youtube.com/watch?v=FmmKRkUverw&t=488s)** Postgress uh which which supports u vector store. Uh we have open search and recently uh these two announcements were really exciting which happened in last couple of weeks uh which is S3 now supports vectors uh you can natively search do vector search in S3. So that is a huge uh advantage for people who love using S3. And another advant another announcement which came just last week was uh document DB now has serverless option. So that is also a good uh vector store for you in case if you want to use document DB. Uh now we talked about uh what an agentic AI system looks like and what are the AWS components which can enable that. Now I will just walk through some

**[8:56](https://www.youtube.com/watch?v=FmmKRkUverw&t=536s)** of the examples of how both of them come together. So we have uh like for example this is an agent lag. We have request coming in from API gateway uh which is hitting an agent which is in inside a lambda. Now that lambda agent can access LLM through bedrock and it can also have access to a bunch of tools through MCP server and you can also run MCP servers on lambda function. So that way everything is serverless for you and then you know those tools can internally talk to different data stores. Obviously this is simplistic for the slide. That data block can be anything right? It could be document DB, it could be Aurora, it could be an API call to third party

**[9:44](https://www.youtube.com/watch?v=FmmKRkUverw&t=584s)** systems and using all of these you can generate the answer and also you can do evaluation in other lambda function and create that agentic loop. So you evaluate the answer if it is good okay if not go back uh give the feedback to the agent and say you know do it again. Uh similarly we can also do uh swam. Uh here what we have is event bridge and we have bunch of agents connected to hooked up to event bridge. Right. So here you can do like any agent can publish events any can any agent can subscribe to different events and they all can work together. U and to instead of just directly subscribing to events uh

**[10:34](https://www.youtube.com/watch?v=FmmKRkUverw&t=634s)** through uh event bridge from a lambda function, you can also look at decoupling with SQS and SNS. And each of these agents could actually have much more complex subsystems, right? Like for example in this slide itself, we have some agents running on Lambda, some are on ECS depending on you know the kind of workload you want to run there. And each agent even like some of these agents could be onstep functions um and branch out into much more complex tasks and stuff like that. Again I am oversimplifying for the sake of the slide here. So u step functions uh I think is really really powerful uh and that's like a repeated uh turn in the entire keynote session I'm assuming uh especially in

**[11:24](https://www.youtube.com/watch?v=FmmKRkUverw&t=684s)** terms of agentic AI applications step function can really be very very powerful here there are like two examples I'm giving but you can do lot more with step functions now um in Nick's keynote he mentioned you know uh agents are nondeterministic and like a static workflow is highly deterministic. So what if we can blend the two right and that's what we can achieve using step functions. Uh in the first example we uh we have a workflow which is serial right you cannot execute the second one without completing the first one. So this next workflow depends on the output from the previous. So in step function you can achieve this very easily. You make sure the one step is

**[12:13](https://www.youtube.com/watch?v=FmmKRkUverw&t=733s)** complete and next one is executing and the next one is executing after that one after another. So in this way you don't let the AI just go do whatever it wants. Instead of that you control the path of agent path of LLM uh in a nice way at the same time giving it the autonomy in each step. Right? in the research type it still has autonomy to do however it wants to do the research but you are guiding the AI into that path similarly if you if you want to do parallel execution against a functions is great and this is a good example of it if in this example a user is asking okay give me an itinary to for Seattle right I'm there for like couple of days I don't

**[13:00](https://www.youtube.com/watch?v=FmmKRkUverw&t=780s)** know what to do u and uh you know then probably can I go to LA from Seattle I don't know so then it can figure out okay user is asking for an itery that means uh the user needs to look for flights hotels and probably look at other attractions and you know all of that so what it can do then instead of doing serially it can actually parallelize it it can give the task to subsystems and do each of these now each of these pieces can again branch out into multiple subsystem subsystem systems have different LLMs, different data stores, different API integrations and all of that. Again, we are we are kind of uh guiding the AI uh non-determinism into a deterministic

**[13:48](https://www.youtube.com/watch?v=FmmKRkUverw&t=828s)** workflow still keeping that non-deterministic outcomes in each of those blocks. Yeah, that's the time I had and if you want to explore more on this topic, these are two amazing talks. uh which are happening later today. They are back to back. So you will you'll get to learn a lot uh from that. Uh and also if you are more curious about step functions uh Eric's talk is something you you should check out. Thank you. >> Nice.
