---
id: CY2VPHMhD0U
title: "Serverless Agents: Real-World Tooling with Strands SDK, MCP & AWS • Akshatha Laxmi • GOTO 2025"
slug: serverless-agents-real-world-tooling-with-strands-sdk-mcp
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Akshatha Laxmi"]
channel: "GOTO Conferences"
duration_min: 21
published_at: 2026-05-05T12:00:31Z
video_id: CY2VPHMhD0U
url: https://www.youtube.com/watch?v=CY2VPHMhD0U
youtube_url: https://www.youtube.com/watch?v=CY2VPHMhD0U
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Agentic AI", "Prompt Chaining", "GenAI", "Generative AI", "Software Architecture", "AWS", "Amazon Bedrock", "EventBridge", "Serverless Platform", "Infrastructure", "GOTO Serverless Day", "Serverless", "Event-Driven Architecture", "Serverless Compute", "Lambda", "Akshatha Laxmi"]
topics: ["Agents & orchestration"]
transcript: true
---

# Serverless Agents: Real-World Tooling with Strands SDK, MCP & AWS • Akshatha Laxmi • GOTO 2025

**Akshatha Laxmi**

`GOTO Conferences` · `GOTO` · `2026` · `21 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Agentic AI` `#Prompt Chaining` `#GenAI` `#Generative AI` `#Software Architecture` `#AWS` `#Amazon Bedrock` `#EventBridge` `#Serverless Platform` `#Infrastructure` `#GOTO Serverless Day` `#Serverless` `#Event-Driven Architecture` `#Serverless Compute` `#Lambda` `#Akshatha Laxmi`

[Watch the recording](https://www.youtube.com/watch?v=CY2VPHMhD0U) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Akshatha Laxmi - Solution Architect at AntStack

RESOURCES

ABSTRACT
In the real world, agents do not merely reason—they act.
In this presentation, I walk through how to reveal real functionality to LLM agents using Strands SDK, the Model Context Protocol (MCP), and AWS Lambda. From a minimal weather tool, I'll demonstrate how to create agent tools that are modular, stateless, and production-ready. We'll walk through how MCP allows tool execution in a language-model-friendly way, and how serverless architecture makes those tools easy to deploy, scale, and maintain.

The goal: building agents that don't just simulate intelligence, but actually use it. [...]

TIMECODES
00:00 Intro
00:34 Problem with traditional AI agents
01:53 Model Context Protocol (MCP)
06:23 Strands SDK
07:26 Example: Weather tool
10:22 Example: Database agent
12:42 Example: Tool definition
15:25 Patterns & best practices
17:11 Security
18:51 Scaling & evolution
19:37 Key takeaways
20:52 Outro

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

*3,211 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=14s)** I think you've heard a lot about AI, agent AI and how you can do it like why it fits so well with serverless. So I'm here to show how. Hopefully some of you can uh go and go ahead and implement it on your own as well. Uh what is the problem with existing AI agent? You end up with a lot of full integration complex. So you might be building some pool or agent which you want to use with uh say charg and then maybe you want to also have this with cloud. So earlier you would have to write this again and again. So each of these LLMs will be able to understand what your tool does and uh deployment and scaling has always

**[1:01](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=61s)** been an issue because most of these frameworks they assume that you are deploying all your tools on a single server. So say that you have an agent that's supposed to get the weather and then an agent that's supposed to perform database queries. Both of these don't have the same dependencies. But by installing all of these dependencies on all of your uh uh replicas, you're simply bloating it up. So it's really not uh useful to have it all in the same server, right? And uh finally, state management. If you're building your own agents, uh you might end up having to uh store the state uh and that can get really complicated and you might end up building a really brittle system. again very prone to breaking. So

**[1:52](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=112s)** what MCP is and how it helps with this. So if you don't already know what MCP is, it's model context protocol. What it does, it's it provides a standardized tool description that your LLM can understand. And it doesn't really matter which LLM you use. uh they all will be able to understand the tool that you have built as long as you're providing it in that MCP format. So uh simple analogy would be that if you are uh if you have ever used type-c come on every one of you have you can just connect any device to your system through the type-c port. So and that can give input to your system or receive output based on whatever application you're using. So like if this did not exist, imagine how

**[2:42](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=162s)** many cables you would have to carry. Imagine how many ports your laptop would have to keep so it can accept all your different peripherals. So in the same way uh MCP does this for you. So you really don't need to be uh building the same agents again and again. As long as you uh are exposing it in the MCP format, all your LLMs can understand what you're trying to build. So some of the main characteristics of MCP, it's language model agnostic. Like I said, it does not uh really care which LLM you're using. It's just the format that you're providing your agents in so that any LLM can understand or client can understand what your tool does. Then since it is so standardized, it is also

**[3:32](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=212s)** built for uh realtime interaction. So most of our interactions with LLM are chat based, right? It's a back and forth that's happening again and again. So all the state is being stored by your LLM, by your chat. So MCP really does not need to store the state. So can you relate to what I'm going to next? Lambda is stateless. So lambda and MCP are like the perfect combination. Um since you uh always talk about uh having event driven whenever you chat with the uh LLM it's an event to it. So it really fits with all the principles that lambda stands for. Now let's look at what an MCP tool actually looks like the description.

**[4:19](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=259s)** So here's an example MCP tool. Uh here are some of the things you'll need to provide for your LM to understand what your tool does. So it needs to define the input schema that you're going to uh need for your tool to work and uh you can provide like what is the data type or uh whether the data is required or not as well and then it's supposed to have a name about which uh tool you're going to be using through the LLM and you'll also need to give a description. It also takes some more additional uh fields like output schema in case that the tool is actually doing something in a different application. So the LLM has to tell what to do to that tool. In that sense, you will have to give the output

**[5:06](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=306s)** schema. Uh so these are that's like one of the other optional uh fields that's required here. So uh a little bit about the MCP life cycle, how a client interacts with the server. it first creates an initialization request. So, uh these are all the things that your MCP server needs to take care of. If any one of these fails, the connection really does not happen with the uh LLM or the client. So, your server needs to ensure that the initialization is taken care of. So, there is uh in the event that comes to the server from the client, there will be a field called method. you need to ensure that all the possible cases that come for the method from the LLM are taken care of. So the first is initialization. Uh you need to send back

**[5:56](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=356s)** that the initialization has happened back to the client and then the tool call can happen. Uh there is also another method called tool listing tool/list and then there's tool/all and then at the end it just disconnects once it's done with its uh interaction with the tool. Yeah, I think you're all convinced about why we need why serverless and MCP are the greatest combination. So I'm not going to go talk much about this. Uh now let's talk about how strands comes into the picture. So uh strand SDK is like a new new framework that helps you build agents, MCP servers and MCP clients. So some of the key features of strands it SDK is that it has a clean abstraction over all your LLMs and it also has some built-in

**[6:48](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=408s)** tool support like HTTP requests calculator as a simple one and there are more complicated ones as well that are already built into the SDK and it also has model driven orchestration. So what this would mean is that it uses uh the models to plan, orchestrate and also like verify whether uh which uh tool it needs to use because you'll have a range of tools that you're adding and it also has great AWS integration uh with EC2 and Lambda and ECS and so on. So let's go through a simple example, a weather tool. So this is kind of like the hello world of MCP servers in my opinion. So I'll just go through the

**[7:36](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=456s)** code and show you how it works. So first you'll have the agent. Uh this is in terms of a MCP server that is agentic. You also need not have it as an agentic uh tool. It could just be a regular tool as well. But this one is an agentic one. So it uses strands uh agent here and you we are also defining a system prompt about what it really needs to accept and uh how it needs to give the output and uh we use like environment variables or secrets manager to store your API keys and uh the agent uh class from the strands is able to take the system input and any other tools that you need or are inbuilt like the HTTP request one is inbuilt. and which model you're using and you can just feed it the prompt

**[8:26](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=506s)** you'll get the response back. So this is just an agent. Now how do you convert it into an MCP server? So let's take a look at that. You'll need to have a class you you need not have it as a class but this is one of the best uh practices that you can have. So it needs to uh make sure that all of the MCP life cycles are taken care of. So as I said earlier we will need the initialization. So we have a handle initialize uh request and then there is the process request which also goes to the tool list when the LLM is requesting to list what all tools are there in this MCP server and then also the tool call which is handled by the handle uh weather request. So uh if you provide this much uh the LLM is more

**[9:14](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=554s)** than happy to connect happily with you. So this particular MCP uses the transport of HTTP and not SSE. So this is how you could just make it as an MCP server. Just converting a simple weather agent into an MCP server. Now uh let's look at a demo. So the top part is showing that Claude has connected with the MCP server and the bottom is a sample example. Now what's happening in the architecture? So we have the MCP which is having the definition of your tool. Uh the client like cloud, chat, GPT, any of your uh LLM or you could even build your own clients uh is talking through the MCP and the MCP also has the server behind

**[10:05](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=605s)** it. So because the MCP is there, the client is able to talk to the server and the client knows what are the tools that are available. So this is just an example that there is a query, search and action that can be done. But this is typically how the architecture is. Now let's look at a more complex example, a database agent. Say for example, you're a business analyst at a uh company that is an e-commerce company. It sells like clothes and shoes and stuff. And uh your boss tells you, "Show me the revenue summary of the last 30 days." So you might not immediately know which databases to go and uh get all the data from. So this database agent can do just that. Uh when you have the MCP, you can just do it through your

**[10:53](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=653s)** RLN. So the architecture is as follows. Our MCP server will be on the lambda. it will uh talk to the Postgress DB that we have set up and uh fetch the data that it needs and sends it back to the uh client which is claude in my case. Uh so like I'll just go through the code a little bit. Again here we have the qu uh query agent first uh just a simple agent which you can directly interact with if you want to. uh so here I'll just go through one of the uh functions that is there in the whole MCP server which is the generate business insight. So again we are creating a model uh and then the agent

**[11:43](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=703s)** is getting a system prompt about what it is what it is supposed to do. So it's a business analyst it's supposed to focus on the trends and patterns and then it needs to be specific and provide more context. So with this information it can identify which query it needs to execute and summarize the data in a way that uh the user can understand. So again here we have the MCP handler which defines the tools and handles all of the life MCP life cycles that are required. So uh yeah so MCP is using JSON RPC. So we are handling that request in the class

**[12:32](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=752s)** and uh we're also doing some form of request routing so that the data is coming from the SQL DB and uh yeah so this is how the definition will look to the LLM. Here we are defining that the uh qu name is uh the query business data the description what it does input schema here we need a query like the query would be show me the revenue for the last 30 days so in a natural language so it really doesn't have to be your SQL uh traditional SQL statements it can just be natural language now again this is the demo since my internet is not good this uh I have I have added the screenshots. So, it's

**[13:20](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=800s)** able to give the uh revenue and which days were the highest uh revenue generating uh in the last 30 days and uh it even adds the start date on its own because it knows from today to the last 30 days when is it supposed to uh like cut off now deployment. So, until now I've been uh talking about more of the MCP. So let's go to the lambda side of things. So here I've used CDK. It's just so simple. You only need to make sure that the dependencies are zipped along with your uh lambda uh zip as well. Or you can just add it as a layer. And layers are again amazing because if you have multiple different tools that running on different lambdas which have maybe

**[14:08](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=848s)** similar dependencies, you can just use the lambda to make sure uh that your lambda is not uh bloated and uh everything else is the same as how you would have done in a regular uh kind of lambda deployment. You are giving the environment variables. I have just done the DB host and the DB uh environment variables but generally you should be using secrets manager. This is just a uh example. So I've done it this way and uh it literally everything else is the same. You might need to give uh access to bedrock if you're using bedrock but if you're using any external uh LLMs you really don't have to. It really does not need any other access. If you're using RDS, you'll have to provide that. Uh permissions literally it's so minimal

**[14:58](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=898s)** that there is barely any security risk there. So uh we also need to make sure that we apply appropriate timeouts and memory because sometimes the LLMs uh if you are using an agentic MCP might take little more time than you would expect. So you just have to be careful of that. Now let's talk about patterns and best practices and how strands helps you achieve that. So the first point is stateless design. Uh we are uh making sure that the tools are individually deployed. So nothing that is separated. I mean like uh you're making sure that there is a separation of concerns. So

**[15:48](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=948s)** anything that's related we are deploying together. For example, the query database it had multiple queries which all are done to the same database. So uh there we are able to group stuff and where it is not needed we're able to separate stuff like the weather agent really does not need to be deployed with the uh database query. So it provides such a clean uh separation that uh you can scale to no end. And uh coming to uh tool composition uh since we're using strands, it can intelligently detect which query we need to use. As long as we are mentioning it there and adding it as a tool to the agent, it is able to know which uh uh tool to use. Even if they're all in the

**[16:38](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=998s)** same lambda, it is able to easily uh detect that. And uh finally configuration management and error handling. Uh since we are using Python again and strands SDK it provides really clean error messages which help us to easily erh manage the errors and again the best practice is to use uh uh secrets manager to get your secrets. So the whole ecosystem is safe. Some security considerations that you might want is that we must use param parameterized queries. For example, in my case, it was a database agent we were talking to. If the uh query that's coming was malicious uh like already had

**[17:30](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=1050s)** some quotes closing or uh having some kind of SQL statement that was going to damage my uh database, it would be so risky. So it's really useful to have parameterized queries like in the weather agent we had the location as a parameterized query to the LLM. So that should never be an issue. Next, I think you all would have seen this again and again and again. Principle of least privilege. Uh of course like you should really only give access to what that lambda needs. So in our case we don't need that much access. We only need bedrock and maybe RDS if you're using but again that is something you need to consider and uh also using secrets

**[18:20](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=1100s)** manager. Uh one more point to consider is that LLM uh can be exploited. So using guardrails is also a very uh good consideration in terms of security. And uh maybe also you should uh look at the LLM's uh privacy policy and how you can opt out of training uh the LLM with your data if you are working with some very uh confidential things. So uh coming to scaling and evolution uh so lambda obviously provides horizontal scaling so you can easily keep making replicas of your uh you don't have to do it automatically does it. So it just scales whenever you have

**[19:09](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=1149s)** demand and then uh you can deploy tools as separate separate functions like we had the weather agent in a separate function and query agent as a separate function and uh your uh LLM can easily discover any new tools that you have created in the same server. So you don't have to keep making that connection on your own. LLM can do that for you. Uh so here are some key takeaways of today's session. Uh agents need tools that uh help them take take actions. Like LLMs are so generalized that they really are not good at one specific thing. So if you want them to be, you can build the tool and give that

**[19:57](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=1197s)** information to them. It could be a rag pipeline. It could be like a manual function that has to do something specific or it could be anything uh literally but it needs to give that context to the LLM so that it can perform perfectly and uh again serverless fits the MCP model perfectly because they both have the same advantages you uh would expect and uh since they are so well aligned it's easily one of the best patterns ever. And uh NCP also enables portability because it's again language model agnostic. It doesn't matter which LLM you're talking to and you don't have to store state because the chat is doing that for you. And uh all the patterns

**[20:46](https://www.youtube.com/watch?v=CY2VPHMhD0U&t=1246s)** that we discussed here, they work at scale. Yep. So that was my session. I hope you all liked it. If you have any questions, please go and uh ask me. I'll be here around. So, thank you all.
