---
id: FW6AAXs4PqU
title: "Shekhar Prasad Rajak + bhrathjatoth - Streaming AI Workflows in Python - PyData Global 2025"
slug: shekhar-prasad-rajak-bhrathjatoth-streaming-ai-workflows-in
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 26
published_at: 2026-01-09T17:56:11Z
video_id: FW6AAXs4PqU
url: https://www.youtube.com/watch?v=FW6AAXs4PqU
youtube_url: https://www.youtube.com/watch?v=FW6AAXs4PqU
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Data engineering & MLOps"]
transcript: true
---

# Shekhar Prasad Rajak + bhrathjatoth - Streaming AI Workflows in Python - PyData Global 2025

**Speaker not identified**

`PyData` · `PyData` · `2026` · `26 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=FW6AAXs4PqU) · [Conference site](https://pydata.org/)

## Description

Python users working on real-time analytics—from payment processing and fraud detection to AI-driven support—rely on message queues to keep data moving reliably and efficiently. Traditional message queues, however, can struggle with large-scale, concurrent workloads, especially when you need durability and replayability.

In this session, we’ll show how Kafka 4.0 introduces robust queue semantics to distributed streaming, empowering Python applications to handle fair, concurrent, and isolated message processing at scale—using familiar Kafka Python clients and frameworks.

But the power lies in what you can build next. We’ll demonstrate how Apache Flink can connect Kafka event streams to real-time Large Language Model (LLM) inference for tasks like sentiment analysis and summarization, all orchestrated via Python APIs and remote model endpoints for powerful, flexible AI inference.

To complete the picture, we’ll cover how enriched results can be stored in popular data lake solutions—such as Apache Iceberg—enabling long-term analytics, time travel, and integration with downstream data science workflows. Support for Iceberg and other lakehouse formats is optional, giving you flexibility to choose the right data backend for your needs.

## Transcript

*2,956 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=6s)** Okay. Hello everybody. Uh welcome to the session streaming AI workflows in Python. Uh Kafka Kafka Q's and Flink powered LLM interference. Uh our speakers uh today um have pre-recorded their talk. So um if you just allow me two seconds to play that on the stage. >> Hello everyone. >> Thank you for joining me in this talk. We will learn more about streaming AI workflows in Python. My name is Shakhar Raj. I'm keen interested in opensource and mainly contributing different organizations around data AI and platform engineering domain. Uh we have Bhat. Yeah.

**[0:56](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=56s)** >> Yeah. Uh, hi all. I'm Bat Arkumar Jat. Um, open source contributor and, uh, currently working as senior AG architect at with Lords Banking Group. So, let's get started. So the agenda is to know and uh recap how the real time processing and real time ML inferencing will work in future. As you know the batch analytics is very common where we used to run some some spark job or doing some kind of analytics on top of past data to predict something for uh different use cases and and now we have real time

**[1:46](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=106s)** ML inferencing AI functionalities like that that Flink provides and tomorrow or maybe uh very near future we will be having realtime ML geni systems that can understand the events and act accordingly. So the first question that comes in our mind is why it is needed. So let me give you one example. Let's say we have we are building live streaming application just like Instagram live or Facebook live where user are able to comment anything and as per our policy we need to make sure that none of the comments are

**[2:36](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=156s)** violating any our policies rules or any compliance. So what that mean is we need a system which can process millions of users comment in real time and make sure that none of them are hate speech or violating any policies. So that in those use cases real-time ML inferencing solve these kind of problems where all the comments will be processed in milliseconds and decide whether we should render those new comments or not. So in in in concise way

**[3:24](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=204s)** any domain where the cost of being late is higher than the cost of being slightly wrong needs realtime ML call. So business we can think of like fast decision making and deriving some kind of dynamic payment or dynamic pricing of the items and so on. So this is how the typical realtime uh fling job looks like where we get some kind of events from Kafka message bus. we do some kind of operations, data processing or any kind of enrichment of the data and then we would like to call an ML API, the ML endpoint which will do

**[4:15](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=255s)** some kind of prediction or inferencing and give some opinion about the event and later on we would like to rather um whether we we can use iceberg as a data lake or maybe publishing another event that have those inferencing. So let's let's go not go very far uh far back like uh the flank AI functions are already available where we can create a model and then it provides flank SQL uh function ML predict using which we can easily do these kind of inferencing. So in this example uh this is all about uh the fraud detection the in the

**[5:05](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=305s)** transaction event and identify if it is um any kind of bad event or something like that. So here we can see we already have the APIs like create model and ML predict but these are all think SQL not uh Java API or Python API. Second is this is mainly uh not actually doing any kind of processing or doing ML calls. What I mean is here we do not have tool accessibility. We cannot add tools. We cannot make sure uh any kind of agentic workflow here. This is very simple

**[5:53](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=353s)** inferencing where every record will be goes to model as a request and model will respondse back with a with a prediction and maybe some kind of scoring. So let's see um what's new um so yeah those are the advantages and some disadvantages comes with the API itself this provides only the flink SQL not the um not the correct way of doing the agentic workflow. So the only SQL integration is there. There is retry logic in internally available in the flank AI functions. There are error handlings and those are

**[6:43](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=403s)** asynchronous calls to uh model. So those are good points about using ML predict and AI functions that Flink provides out of the box. The cons we can think that those are not multi-step reasoning. There are not react agent, no chain of thoughts. We cannot add tools. These are all stateless. Basically, if pling job uh dies, then there will be nothing will be stored in a state and we need to retry calling the model back for the inferencing call and there are limited providers right now. This is mainly open AI or u the local models we can use. There is no dynamic orchestration that means fixed

**[7:31](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=451s)** inferencing flow. No branching logic as such. And one more thing ML predict treat AI like a UDF a simple stateless and SQL integrated where contextual retrieval is not required. So in those cases the ML predict and flank AI functional functions are useful. So let's see what is getting built in open source. So to solve these >> yeah flink agent [clears throat] >> thanks Jer. So let me start uh with a question like why we get why we are building the flink agents

**[8:22](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=502s)** because uh the modern enterprise systems are like drawing in realtime events but uh today's as said LLMs are stateless and request driven and completely disconnected from the moment the prompt ends. So this is where the flink agents fix uh this by making AI a native stateful operator inside Apache Flink stream processing runtime. So these Flink agents run always on AI agents on your streaming platform react to the live events that were happening and it guarantees you to expect from fitting jobs and this scale and have millisecond latency and exactly once actions

**[9:10](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=550s)** and they live in a topology see every event instantly and uh maintain the long running context reason use tools and act all exactly and uh they scale horizontally. So just to give you an example as shaker uh uh demonstrated earlier like take an example of fraud detection which is as a perfect example. So there are like millions of transactions which stream in per minute. Uh so Flink instantly computes per user baselines sliding windows and anomaly scores. So it the moment a score spikes the embedded agent wakes up inspects the full session state and output and

**[10:00](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=600s)** outputs whether uh outputs in a less than of 200 milliseconds like it and again it is fully replayable and auditable. So the same pattern works for supply chain rear routing and live personation and many other use cases. So the flink agents turn continuous streams into continuous intelligence. So that's the reason they are the these are the missing primitive for production grade realtime AI. So coming to the the next slide. Yeah. So we have this uh no the previous slide. Okay. Yeah. So this is uh once we get the system generated events, it goes to the flink and it has the embedded

**[10:50](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=650s)** LLMs and uh we also have the tool calling like with the latest MCP servers and other output events as well. So most like the enterprise AI today is still request and response like you ask it answers it forgets which is said earlier though we have the context but that that works only for a chart but whenever it is having in the real time it is not so feasible or it is not like an event driven. So that's where these realtime flink agents help like these are not any wrappers around the language models or any language models they are a native citizens of Apache Flink's

**[11:38](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=698s)** runtime. So what they do is they live inside the stream topology see every event the moment it happens in real time and keep the state forever and all with exactly once guarantees and subsecond latency. So they don't have no fragile glue of microservices and cues and now a single fling job can now run hundreds of autonomous agents that detect any of the fraud uh any personalized experiences and coordinate with each other as synchronously like any human nervous systems. So these are like the eventdriven flink agents which are the new primitive that

**[12:25](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=745s)** makes the realtime enterprise AI finally possible. Yeah. Next slide. Okay. So now we have the intros done. Let's go to the more exciting part of the talk. The Kafka Q semantics. As we know the Kafka is already a messaging bus but Kafka 4.x come come up with Q semantics. So how the traditional Kafka looks like. So we have Kafka topic. We have let's say four partitions of this topic and we want to read these messages from Kafka uh to the flank for the processing. We

**[13:17](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=797s)** can only parallelize the number of partitions. Basically the maximum parallelism is not unlimited. Those are bound to partitions count. So one worker is kind of having one consumer and those will be reading for from one partition. So this is like one partition one consumer mapping. And if we have more consumers than the partitions then those consumers will be sitting idle. That is kind of one tradeoff in current Kafka world. So why this make uh why why do we have this uh kind of design in Kafka? Those

**[14:06](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=846s)** are all previous to uh keep 848 and um keep 932. So those are having mainly the consumer assignment very static like per partition. The load balancing is a time slice client side. So whenever there is new consumers are added or older consumers are re removed we are doing some kind of rebalancing of the client side itself. So let's see in Q semantics how this will look like. So when we have Kafka share groups came into picture in um Kafka 4 we can extend number of uh consumers unlimited. So the

**[14:58](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=898s)** max paralism will be can be go beyond the number of partitions and the offset management is taken care by the broker manager itself. Even the load balancing will be handled by the broker side automatically. So the client side the operational cost is reduced. The throughput will be higher and since we are able to process the events as quickly as possible. The overall system latency will be low. Okay. So till now we went through the flink AI functions and then Kafka Q semantics the flink agent and let's let's brainstorm a little bit how the

**[15:48](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=948s)** unified real-time EI platform should look like we are envisioning a system which is having nonblocking ML inferencing the model life cycle management will be loosely coupled we will be having state management management and all agentic AI building blocks like tools, resources and memories. The Flink comes up with fall tolerance. So basically if something went wrong, something crashed then it can recover itself. So this is what we want in our AI realtime uh streaming AI workflow. So let's combine these two idea about

**[16:41](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1001s)** Kafka Q semantics and the flink agent. So what's going on in the open source? There are a few some of the works that is still uh work in progress where in the flink connector Kafka we would like to have Q semantics so that we can increase the throughput and low latency systems we can build through that. So these are the works that is still going on. This also come up with the Python API. So we can easily connect to Kafka share group using fling connector Kafka Python API. So some of the comments shows how um the overall consumption will look like

**[17:31](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1051s)** through the FlinkSQL. But I will show you how we will be able to do the Kafka share group uh consumption through the Python API also. As you can see it's look it just mainly need these uh config configurations about share group ID topic and the parallelism we want and then um we should be able to read records with higher throughput. Okay. Um so I just wanted to quickly touch upon the components that the Flink agent have and the overall um demo that we will be seeing. So we have Kafka source topic which have three partitions

**[18:20](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1100s)** and at the end we have Kafka source operator the flink where basically move to the action action executor which will be the react agent. So basically in flink agent we have two types of agent. One is workflow agent where we will orchestrate what we want to do in a sequence. And the second is react agent which will nothing but reasoning and actions. Basically it will reason it will it will understand the event and accordingly act and observe. So the flink agent is the building block for event driven streaming agents. This inherits distributed at scale fall tolerance structure data processing and

**[19:09](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1149s)** mature state management. So yeah, this comes up with another interesting feature which is exactly once action consistency. That means if an agent calls a tool that sends an email or alert event, right? If the job fails, we do not want those events to send again after the recovery. So this makes sure that there is exactly one action. Second, the stateful memory. So if you want to build a rack system, we would like to have all the context in vector store. So the context retrieval request will be sent to vector DB and get the response based on the context. There is multi-step reasoning as well.

**[19:58](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1198s)** So basically react loops builtin and this helps in complex task without much custom code. So this is the flow that we would like to demonstrate exactly once guarantee there is a recovery and there is back pressure handling as well. So this makes sure that we are able to have heavy workload and as soon as uh process as soon as possible the inferencing as soon as possible. So this is a small code snippet that I have where we will initialize the agent environment and add the resources here using Olama chat chat model connection

**[20:49](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1249s)** and the Kafka share group API will look like this where we will share we will set the share group ID bootstrap server and how we would like to decentralize it. There will be react agent as I mentioned previously which have the resource descriptor the chat model details and about the prompt in this example this is sentiment prompt and output schema where how we would like to output in the console or if you want to send back to Kafka there will be Kafka sync. So when we have the sentiment agent available, we will tight it up with the environment and apply or for all the messages that we have.

**[21:45](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1305s)** So I have one recording so that we can quickly see the demo within timeline. So the here there is one fling job running as we can see there are number of tasks and we can see the content and the sent sentiment that is derived by the agent. This is a simple example but does a lot. So here we can see we can have the source kafka and the action executor. We had basically a topic which have three partitions and we have share group my share group

**[22:34](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1354s)** with the share group ID. You can see some of the events are getting generated. As we can see there was three partitions for the topic but the number of workers are more than partitions that helps in the high throughput and make sure the records are processed as soon as possible. In the log we can see how it is calling the Kafka share consumer and getting response from the ML API call. number of tasks which are consuming. So all the workers are getting records mostly even evenly distributed.

**[23:37](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1417s)** So yeah, this is what we wanted to quickly show you guys. Okay, I think we will be over time if we'll talk about the iceberg part. But there are some of the features which have branching, time travel and snapshotting mechanism that can help in different context uh and which context helps in better accurate response from the LLM. So this is what we wanted to cover in this section. So thank you so much. Just for the

**[24:27](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1467s)** conclusion, we went from run predictions on yesterday's data to autonomous agent responding to events in real time with reasoning capabilities. So there are three things we should just recall. Streaming is the new default for AI. Batch is for training. Streaming is for serving. Second agent needs in infrastructure not just prompt. That means we need all the AI building blocks state tools state management tools resources recovery and how we we scale for the overall system integration. Third, link agent bridges the gap. All the stream processing

**[25:15](https://www.youtube.com/watch?v=FW6AAXs4PqU&t=1515s)** guarantees plus the first class aentic AI support. So if you are building AI platforms, start thinking event first. Your user won't wait for bad jobs. Your agent shouldn't either. So thank you so much guys. These are our LinkedIn QR code and let's connect. That's correct. >> Yeah. Thanks a lot uh audience for showing up.
