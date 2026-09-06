---
id: nAcyi2BGwMo
title: "Building Agentic AI Systems with AWS Serverless • Uma Ramadoss • GOTO 2025"
slug: building-agentic-ai-systems-with-aws-serverless-uma
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Uma Ramadoss"]
channel: "GOTO Conferences"
duration_min: 23
published_at: 2026-01-28T13:01:28Z
video_id: nAcyi2BGwMo
url: https://www.youtube.com/watch?v=nAcyi2BGwMo
youtube_url: https://www.youtube.com/watch?v=nAcyi2BGwMo
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Uma Ramadoss", "Agentic AI", "Prompt Chaining", "GenAI", "Generative AI", "Software Architecture", "AWS", "Amazon Bedrock", "EventBridge", "Serverless Platform", "Infrastructure", "GOTO Serverless Day", "Serverless", "Event-Driven Architecture", "Serverless Compute", "Lambda"]
topics: ["Agents & orchestration", "Prompting & context engineering"]
transcript: true
---

# Building Agentic AI Systems with AWS Serverless • Uma Ramadoss • GOTO 2025

**Uma Ramadoss**

`GOTO Conferences` · `GOTO` · `2026` · `23 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Uma Ramadoss` `#Agentic AI` `#Prompt Chaining` `#GenAI` `#Generative AI` `#Software Architecture` `#AWS` `#Amazon Bedrock` `#EventBridge` `#Serverless Platform` `#Infrastructure` `#GOTO Serverless Day` `#Serverless` `#Event-Driven Architecture` `#Serverless Compute` `#Lambda`

[Watch the recording](https://www.youtube.com/watch?v=nAcyi2BGwMo) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Uma Ramadoss - Principal Solutions Architect at AWS

RESOURCES

ABSTRACT
Agentic AI is transforming enterprise applications but building them is not just about prompt engineering and model selection. Join this session to learn about agentic systems, how they are changing the way we work, and how to build them using open-source agents framework and AWS Serverless services such as Lambda, Step Functions, and Amazon Bedrock.

You'll learn the difference between AI enabled workflows and agentic workflows, when to choose agentic workflows and things to consider when building agent-based systems. [...]

TIMECODES
00:00 Intro
01:10 Agenda & takeaways
02:07 What are AI agents?
03:29 How are AI agents different from AI workflows?
11:50 Building AI agents on AWS
21:16 Things to consider
22:16 Resources
22:57 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
James Urquhart • Flow Architectures • https://amzn.to/3Tyz8cY
Adam Bellemare • Building Event-Driven Microservices • https://amzn.to/3WfNKfM
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ford, Richards, Sadalage & Dehghani • Software Architecture: The Hard Parts • https://amzn.to/3v4pKQS
Gerardus Blokdyk • Event-Driven Architecture EDA • https://amzn.to/3FOfUHE

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*3,128 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=12s)** We are at a fascinating intersection where AI is evolving from just being a tool to something like an intelligent participant that works alongside you that can take goals and complete goals. This is not about replacing human capability. It is about enhancing it. I know you know what I'm talking about. Agentic AI systems. Who here are developers or developer background? Okay, a lot of you. I am a developer myself. So, we are all we want to build things, right? We want to see things in action. So this talk is about building

**[1:02](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=62s)** agentic systems. My name is Umar Ramadas. I'm a specialist solutions architect at AWS. So in this talk we will define first what an AI agent is and then we will learn a little bit more about AI agents. As we go through it, we will know and we will understand how they are different from AA enabled workflows and then we'll see how we can build such an agentic system in AWS and then I'll leave you with some thoughts and key resources that you can take away. There are three things I want you to take away from this talk and on the these three things I call them as fundamental guidelines. Actually

**[1:50](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=110s)** there are four. I'll show the fourth one in the end. These three uh fundamental concepts are wired in the presentation and I kind of like I encourage you to keep these three things in mind when you are building agentic systems. So what exactly are AI agents? These are not fancy things, right? These are software applications that we are all familiar with. But what makes them different and powerful is their ability to think and act iteratively and independently. They can observe results, adjust their approaches, and continue working toward a goal. They not only answer questions, but they also

**[2:38](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=158s)** solve problems through a process of exploration and refinement. But why should you care about it? Who here do not want more time to do the things that you love the most? Nobody here, right? But we only have got 24 hours. How do we make the most of it? Agents or agentic systems can automate mundane task. They can free up the time and so you can do the valuable things that you always wanted to do. That's why enterprises are doubling down on agents. And here's you can see some impressive numbers from Gartner's study. So we know what AI agents are, but we need to know a little bit about them. So

**[3:27](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=207s)** I'm going to take that I'm going to take you to, you know, in 2023 when I learned about or when I started my generative AI journey. I'm sure most of you here would have started your generative AI journey with a chatbot. And that experience was really fascinating for me. It was amazingly natural humanlike and it made mistakes and even apologize for the mistakes and I was able to create new things. I was able to ask write uh write ask it to write a poem about serverless. It was really fun to play with. But just like me, you probably have noticed there are some fundamental characteristics of the large language model that limits its ability to become

**[4:16](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=256s)** fully functional. Number one, they are trained in the past. They don't know the current situation. They don't know the stock market today. They are stateless. They don't know you. They don't know who you are, what conversation you previously had with it. and they cannot take actions. But the chat experience you might have had with a chatbot would have made you feel differently. Would have made you feel that LLM knows about you. It would have made you feel that LLM can take actions. How does it do it? It's the context. And that's why context is everything. It's the amount of information that you

**[5:04](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=304s)** send it to the LLM and that has access to it through the session and it's really really important part of your application and that's why we're going to see why this context is important and how you enrich it. If you think about a normal chatbot experience, you ask a question, a chatbot assistant will take that question and send it to a large language model and that is context. That's a user prompt. Let's say you want to assign a personality to it. Let's say we want our LLM to behave like a famous French chef. You just add a system prompt. Now what happens? You use a prompt and sister prompt goes together and that's the context. Now so all of a sudden your

**[5:52](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=352s)** model now behaves like a French chef. You kind of wonder is actually the French chef that you were talking to. Then you can take it to the next level where you add history. So you add all the previous conversations and you add it to the prompt. You enrich it. And so now that now the model gives you a feeling that it knows about you. It knows about your previous conversations. So how about something that's internal to your corporation? Something that's an internal knowledge or domain data. We all know that rag is one of the finest techniques that you can incorporate or you can make the large

**[6:40](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=400s)** language model aware of your domain specific data. And so what happens you populate this rag data and when you populate the rag data actually your knowledge corpus data generally you store it in a vector database which stores the information in just like a human memory does right and then you get that data and you augment your context again so basically you're enriching the context Now retrieve augmented generation data system prompt history everything together goes to the model and model responds back. Now think about it if the model has to respond model has to give an answer based on what you are passing

**[7:30](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=450s)** in the context how good that context has to be. So that's why it's very very important that you have right information in the context and in the right format and you can extend that context to agentic AI as well. Here is a question is this will be solved by agentic AI. What's the weather forecast for tomorrow in my location? I'm asking two things that actually touches a limitation of the model. one a weather forecast which is some something that happens tomorrow and then I'm asking the model to remember my location. So if you are going to design an application just not using generative AI which is traditional application where

**[8:18](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=498s)** this information comes in a structured format how do you do it you will leverage location API weather API right and you're going to do the same thing with agentic system as well that's why I said this is again a software application so you bundle them as tools your APIs are bundled as tools You give the tool description, input parameters and the output parameter and everything and you put it in the context. Give it to the model. Then model tells it knows the intent. That's the purpose of the model. Model knows the intent. Model has a context. It's going to tell I need the location. Then it's going to give back to the agentic assistant the location tool. Agentic assistant is going to call the tool.

**[9:06](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=546s)** That tool could be an API. It could dip into the database. It could be anything. Right? Once the assistant has that information, it will enrich the context again because it has to tell the tool results. Then the model decides what needs to be done. In this case, model would tell I I need weather data. And so this process gets repeated until the model the model is the one which is going to say I'm done with this process. I'm going to send back the response. And so as you can see that in agentic AI system the model along with the agent they can not only make the decision they also take the decision.

**[9:55](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=595s)** If I had to recap what agent is, it is a software application that leverages that uses models and tools in loop in order to achieve a goal or until the goal is reached. So how are they different from AI workflows? A A AI workflow, a AI enabled workflow is that also leverages generative AI. It might also has branches, but any point in time at any any part of the branch, you can tell exactly how many steps are in that workflow and you were the one who is going to code how that AI enabled workflow branches out, what step needs to be

**[10:44](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=644s)** taken. But in an agentic AI, the model decides what tool to use and the model tells when to stop. So you never know how many steps are involved in it. And so that makes agentic AI highly autonomous and so it's non-deterministic whereas an AI workflow is highly deterministic, highly reliable, faster and cheaper. And so here is the rule of thumb. Rub Goldberg machine is a highly complex purposeful purposefully built complex machine. Do you really want to build a complex machine to port?

**[11:34](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=694s)** So if your business use case can be built with AI enabled workflows, go for AI enabled workflows. Check if you really need an AI agent. When you're building an agentic system, keep it simple. Start simple. All right. So, we have seen what an AI agent is, how they are different from AI enabled workflows. And we're going to see how we can build such a system in AWS. In order to build an a system, we need an use case. So, I'm going to take the travel agent use case. If you ask me, it's one of the complex use case to build as an agentic system. We have seen code assistant, we have seen searchbased um agents. They are more reliable. Whereas a travel um agent

**[12:25](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=745s)** is really complex because of all of the context because of multiple variables associated with it. But this use case resonates with everybody. We have all booked travel. So, as I said before, we're going to start really simple. Let's say we're going to do what just the flight booking. What functionalities are available in flight booking? You can search for a flight, book a flight, cancel a flight, maybe check in. If your company is not new to the business, you will already have APIs for each of them. Those APIs become tools. Then you will have your travel agent use the context enrich the tool information into the context and ask the large language

**[13:13](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=793s)** model and the process gets repeated. If you have to build such a system, you need a large language model. You need tools that we already have because your company already has APIs and you need a travel agent. How many of you have used Amazon Bedrock? Quite a lot. It's really good. Amazon Bedrock offers you the broadest choice of models. It gives you a very easy way to consume those models through APIs. And so, Amazon Bedrock, let's just take it as our LLM provider. And the next thing is building the Table agent.

**[14:00](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=840s)** There are in my opinion there are two broad ways. One you can use specialized agent framework something that already gives you lot of knobs to build an agent. You don't really have to do anything. The other option is to write it yourself. I mean we're all programmers. I told you how the agent system is basically invoking the large language model and the tools in loops. So we can write it right? We can write it in Python. We can write it in any language and we can write it in a compute. We can also use AWS step functions for that purpose. How many of you here have used step functions? That's good number. One of the common use cases of step

**[14:48](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=888s)** functions is to automate business process. What does agentic AI do? It also automates business process. So, step functions is a serverless visual workflow service that allow you to build automate business processes. It can integrate with bedrock directly. If your model is outside AWS, you can leverage HTTP APIs. You can run things parallel. You can run things serially. You can run things in loop, which is very very important. Running things in loop. That's one of the agentic AI characteristics. So if you use step functions to build an agentic AI system that might look something like this. At first you will call the large language model. You give the intent. You give the

**[15:38](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=938s)** context along with the tools. Then the model tells whether it needs more information, whether it already has everything and it it has the answer or it tells you what tool to invoke. When it tells you what tool to invoke, you will invoke the tool. You will enrich the context and then you ask the model again. The same thing we saw earlier in agentic AI diagram can be written in all can can be seen like this in step functions. So this this particular workflow right not just visually building but also executing when you execute you will see all of those different iterations you will see the input and output for every

**[16:27](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=987s)** single iteration and everything and that actually improves the observability of the agentic systems. I always prefer to use step functions for AI enabled workflows and also workflows that have flow autonomy and then workflows which are task based agents. When I say task based agents, they are not interactive like a travel agent. You know, a user interacts often with a travel agent. But there are use cases where just run on schedule. agentic systems that run on schedule where you don't really have to um exchange memory across uh across executions. So I prefer in those scenarios there's also another way to build agents

**[17:17](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1037s)** that's through stance SDK. How many of you are building or familiar with open-source agent frameworks like lang chain llama index so how many of you familiar with strands SDK we've got a few so stance SDK is just like lang graph just like lang chain is a open-source SDK for building agents with just few lines of Let's see how it does. So you bundle the library, import the classes, you choose the model. This model can be in bedrock model. It can be a model outside AWS as well. Then you define the agent and you ask the agent.

**[18:06](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1086s)** That's it. It's pretty much very very simple. So agent abstracted a lot of the things that you will have to do with step functions. Once you build that agent, right, you might have to add sessions. There's a session storage that um stands natively supports. It supports S3 as a session storage. You can also use Dynamob with your own code. So it's so easy to attach a session that you know keeps all the previous history of conversations and then it offers you mechanisms or um abstractions to invoke tools whether the tools are internal tools are external through API or through MCP the model

**[18:55](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1135s)** context protocol. Once you have your agent code the next thing is you need to deploy it. You can use any of these favorite compute choices that you have to deploy your agent. Lambda, ECS or EKS. The new kit on the block is agent core uh bedrock agent core runtime. It's in preview. It's purpose-built for running agents. Let's say we choose to run it in Lambda. Then an agent might require an API. So you can attach an API gateway, you manage the session in S3 and you have a model. It's a simple application we're all

**[19:45](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1185s)** familiar with. So now you can add authorization on top of it. It's something that you have always built as OBS application and you can use all of the other services for observability like Cloudatch. You can use other services for guardrail key management services as like every serverless application that you are familiar with. Every serless services that you're familiar with can fit in into the agentic system that you're building. Now coming back to our travel agents, we started with flight booking. Let's say we are extending it to car booking, hotel booking or corporate policies. All you do is extend your tool chain,

**[20:35](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1235s)** right? Or you might also want to use MCP. You build MCP servers for it. But the thing is you're making it extensible. That actually reminds me of microser architecture. So whether you are extending your tools, whether you are building MCP servers or whether you are breaking it down and have different agents, a car agent and a flight booking agent, think in terms of microservices architecture because your agent need extensibility. It also needs scalability. All right. So we have looked at what is an AI agent. We have looked at how they are different from AI enabled workflows.

**[21:24](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1284s)** How you can build it on AWS and the last thing is all those three guidelines plus verify. It's very very important. I did not cover it much here but if you are putting your agentic system in production it is really really important you verify it. Remember the agentic systems are highly autonomous. If you're highly autonomous, noneterministic, it's going to give you unreliable answer. How do you make it production fit? That's why verification evaluation is really really important. One of the finest techniques some people use are LLM as judge and there are libraries available for you to leverage. So these are the final thoughts that I

**[22:12](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1332s)** want you to take away from the talk. And last but not the least, there are some resources. It has got some workshop not just agent take other generative AI workshops um and a few other blogs as well to help you with if you're interested to build what I said y whether with uh step functions or whether with stance SDK we're running a workshop on Monday uh in the Aquila building on Amazon development center and here is the QR code for it you can use to register for the event and then we are running throughout the year some serless uh webinars and events. You can check them out. Thank you so much. I really appreciate the time here.

**[23:03](https://www.youtube.com/watch?v=nAcyi2BGwMo&t=1383s)** Thank you. It's an honor to be presenting in front of you and I really appreciate the time you have given to me. Thank you. [applause]
