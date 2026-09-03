---
id: O0qyaJSLg38
title: "Ranjan Sinha - Speaking the Same Language: NLIP for Agent Interoperability"
slug: ranjan-sinha-speaking-the-same-language-nlip-for-agent
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Ranjan Sinha"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T01:44:38Z
video_id: O0qyaJSLg38
url: https://www.youtube.com/watch?v=O0qyaJSLg38
youtube_url: https://www.youtube.com/watch?v=O0qyaJSLg38
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Ranjan Sinha - Speaking the Same Language: NLIP for Agent Interoperability

**Ranjan Sinha**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=O0qyaJSLg38) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,595 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=O0qyaJSLg38&t=4s)** RANJAN SINHA: Well, hi, everyone. So an agent speak in different languages. You need to write custom code, glue code adapters, and that doesn't really scale too well. And that's really the Tower of Babel problem. So NLIP is the universal handshake that makes seamless interoperability real. So if the agent speaks NLIP it speaks to everything else that does. So think of NLIP as the HTTP of intent. And it follows a very similar approach of being minimal and neutral. So HTTP is a neutral uniform way to transfer resources between heterogeneous clients and servers.

**[0:58](https://www.youtube.com/watch?v=O0qyaJSLg38&t=58s)** And NLIP is a neutral uniform way to transfer meaning or intent between heterogeneous agents and clients. So it came out of a working group of academia and industry researchers and practitioners, and it was sponsored by the enterprise neural systems group and the AI Alliance. And it is now a ECMA standard. And TC56 is the technical committee that drove NLIP. And JavaScript was also standardized by the ECMA body. And the contributing organizations are on the right-hand side. Now, the AI-based software systems or agents

**[1:48](https://www.youtube.com/watch?v=O0qyaJSLg38&t=108s)** are being deployed in a wide range of applications. So agents serve different functionalities and operated by different organizations, they must interoperate through a common communication protocol. So let's look at the left diagram. So a traditional protocol. So agent one speaks language A. Agent two speaks language B. And what passes over the wire is language P. Now, in a traditional protocol they all have to be the same. So A is equal to P is equal to B. And if there is any change in the schema or change in fields, it typically breaks. And that's really the hard coded integrations. And that is tight coupling. And that creates issues with interoperability version

**[2:37](https://www.youtube.com/watch?v=O0qyaJSLg38&t=157s)** management. And if you look at the right-hand side, that's the domain-- that's where NLIP comes into the picture where you have agent one that speaks language. Agent two speaks language B. And what passes over the wire is P. And A doesn't have to be equal to B, doesn't have to be equal to P. So it promotes flexibility. But the condition is that, there needs to be intelligence at both endpoints so it can translate between these messages. And given the current trends, you'd expect intelligence to be available in solutions and systems and it continually improves. So NLIP provides a very simple open common standard protocol for applications, agents, and services

**[3:27](https://www.youtube.com/watch?v=O0qyaJSLg38&t=207s)** to communicate with each other. It assumes intelligence at both endpoints to enable the semantic understanding. And it follows a request and response paradigm to ensure that the meaning or intent is refined and confirmed before the agent gets to act on it. And if a message is ambiguous, the agent doesn't just fail, it will ask for clarifications. So that's really the request-response paradigm. And it is built for enterprise reality. So if you deploy an enterprise or otherwise some serious application, some of the requirements for the protocol are on the right hand side. It needs to be secure. You've got to have safeguards. It's transport agnostic. And essentially, it uses the existing infrastructure. It's not rebuilding the wheel.

**[4:16](https://www.youtube.com/watch?v=O0qyaJSLg38&t=256s)** Suppose multimedia communication is efficient. I have some charts to show that. It can be implemented in multiple languages. And it is an open standard so governed by ECMA. And we've also submitted that for the ISO standardization. And so that's currently in progress. Great. So now coming to the NLIP specifications, it is deliberately minimal. So if you see the message model, it's a lightweight JSON. It is just five fields. And out of these five fields, three are mandatory. So you have the content which essentially is a lightweight JSON envelope which

**[5:04](https://www.youtube.com/watch?v=O0qyaJSLg38&t=304s)** contains the information that is exchanged. The format is you specify is it text? Is it structured? Is it binary? And then your format is essentially a refinement. If it is text, what language that text is in. And encoding for a binary content. And then there are two optional fields that suggest a parsing hint. And you can have more additional content in the message. But that's really it. And the core and data model, these five fields. And if you compare with some of the more popular protocols that's used, let's say A2A or MCP, you're looking at 60 to 99 to the full data model, having 166 to a 480 fields. So in that sense, it's very lightweight.

**[5:55](https://www.youtube.com/watch?v=O0qyaJSLg38&t=355s)** And in terms of it's very simple to implement over standard transports. So you have the bindings for HTTP, for WebSocket for AMQP. And these are specified in the ECMA specifications. And you can access that from the GitHub page. And it is secure by design. So it's mandatory. So you have three profiles from basic to rigorous enterprise profiles and addresses various AI-specific risks, besides just the transport security. Now, NLIP can interoperate with various single vendor protocols in two modes. The first mode is NLIP is an outbound API and single vendor protocol, an outbound API, and you use the translation agent and LLM pod to translate between these two and in mode B,

**[6:47](https://www.youtube.com/watch?v=O0qyaJSLg38&t=407s)** if it can interoperate across multiple domains and each of these domains, you can have multiple agents that speaks in their own language using different agent frameworks. But as long as they are NLIP aware, they can all communicate with each other. And so this is a very powerful feature. Now, several proof of concept applications have been developed by companies and universities and across multiple domains. So you have telecom to shopping, to sustainability, to multimodal customer support, and so on. And a lot of these are also available on the project page. So I'll dive a bit deeper into the customer support, where in this case a customer submits a voice request.

**[7:39](https://www.youtube.com/watch?v=O0qyaJSLg38&t=459s)** It's a query that is then-- it's an audio that's then converted to text using a speech to text model, NVIDIA ASR. We then use NLIP over HTTP and send that information to the channel recommender, which picks up the most relevant subreddit channels for that query. That's then sent using NLIP over HTTP to the search agent that picks up the most relevant topics from those channels, ranks them, and sends it back to the customer. Essentially, a customer query picks up the most relevant topics from Reddit and the customer gets those responses. So we compare NLIP with A2A for this workflow. And we use a very similar symmetric identical timing

**[8:33](https://www.youtube.com/watch?v=O0qyaJSLg38&t=513s)** harness for NLIP and A2A I've used three variants of A2A. And we also have a phase level instrumentation that message creation, connection, and send to really understand what timing is going. And the total latency is really a summation of these three phases. We use two machines, two data sets containing several customer queries. And so the average total latency across the queries on both the phases where we use NLIP, you'll see the NLIP is in blue. And then you have variants of the A2A SDK to cache optimize A2A to a lightweight Python, A2A on the right-hand side, and you'll find that it's the minimal nature of A2A is displayed here. Of course, I would say it's preliminary experiments.

**[9:24](https://www.youtube.com/watch?v=O0qyaJSLg38&t=564s)** You can do a lot more complex workflows and experiments. And that's something that we'd like to do. And if you'd like to participate, that'd be terrific as well. But it gives you a sense as to it's a very lightweight message envelope. Now, for practitioners, it will boil down to when do we use these protocols? You can choose NLIP when you're looking at-- when you have a use case that is around requires heterogeneous protocol interoperability or semantic flexibility or cross protocol mediation and choose A2A when you have governance and audit needs or task-centric or long running workflows, strict schema enforcement deterministic execution, and you can even choose a hybrid when you have mixed workloads and NLIP at the coordination layer,

**[10:13](https://www.youtube.com/watch?v=O0qyaJSLg38&t=613s)** and then A2A at the government layer. These are various guidance that we are working based upon our experiments and evaluation. But the important thing here is that the protocol selection should be guided by the workload characteristics. Currently, we have several protocols, essentially, long-tailored protocols. You have domain-centric protocols being introduced for payments and shopping, and so on. So how do we work across these protocols and communicate in an interoperable manner? And that's where the NLIP fits in. So to summarize, it's essentially-- it's a standard based semantic protocol that connects clients to agents and bridges different agent protocols. It's simple, it's open, it's lightweight, it's neutral. And think of it as the HTTP of intent,

**[11:03](https://www.youtube.com/watch?v=O0qyaJSLg38&t=663s)** and it is built for the intelligence era. And in preliminary experiments, we observed that it was efficient during message creation and transport. And for practitioners, you can choose NLIP based upon agent workload characteristics. Now, you'll find the details of NLIP on the project page. It has been integrated with ag2 framework as well that's downloaded tens of thousands of times daily, probably a million in a month. So if you're interested in your feedback, of course, we always welcome that. It's a very active committee. We meet weekly and continue to develop this protocol. And if you have any use cases in mind, participate in evaluation or contribute to NLIP.

**[11:53](https://www.youtube.com/watch?v=O0qyaJSLg38&t=713s)** We'd love to hear from you on that. So there are emails and other contact details on the project page. So with that, thank you very much. [APPLAUSE]
