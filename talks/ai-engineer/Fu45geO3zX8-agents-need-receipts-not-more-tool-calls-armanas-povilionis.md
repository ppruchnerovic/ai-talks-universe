---
id: Fu45geO3zX8
title: "Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio"
slug: agents-need-receipts-not-more-tool-calls-armanas-povilionis
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Armanas Povilionis"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-07-18T00:00:00Z
video_id: Fu45geO3zX8
url: https://www.youtube.com/watch?v=Fu45geO3zX8
youtube_url: https://www.youtube.com/watch?v=Fu45geO3zX8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Science, healthcare & applied ML"]
transcript: true
---

# Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

**Armanas Povilionis**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Fu45geO3zX8) · [Conference site](https://www.ai.engineer/)

## Description

In this talk, I’ll show an agent publish a service, another agent discover and invoke it, and a signed receipt that proves what happened. The point is simple: if agents are going to buy, sell, and compose work across hosts, logs and API dashboards are not enough.

Froglet is an open-source protocol and node for agent-to-agent compute. It reduces named services, data-backed services, and open-ended compute to one signed flow: Descriptor  to  Offer  to  Quote  to  Deal  to  Receipt. The same surface is exposed through MCP and OpenClaw/NemoClaw as one froglet tool, so agents can publish, discover, invoke, and verify work without custom glue for every provider.

The hot take: agentic commerce should start with verifiable work, not checkout pages. Payment rails can change. Receipts, identities, workload hashes, and deal state need to survive across models, hosts, and marketplaces.

see froglet.dev

Speakers:
- Armanas Povilionis (Alithea Bio): Technologist and systems strategist working at the intersection of AI, infrastructure, biology, governance, and incentive coordination.

## Transcript

*2,245 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Fu45geO3zX8&t=0s)** Hello everybody. I'm Armandus. I work at Alifeia Bio where we focus on life sciences topics. More specifically, we work on immuno-oncology and immunopeptidomics. While we work on science topics, we use ourselves and provide our clients agentic automation or agent AI solutions. However, we found a certain gap which we would like to discuss today and we have a solution which we're working on which we would like to share. It's called Froglet. But to start with, I would like to ask what do you think is most valuable work that agentic automation can do? My guess, uh scientific research

**[0:52](https://www.youtube.com/watch?v=Fu45geO3zX8&t=52s)** automation would be quite high up that list. However, from my experience, adding more tools to agents will not suffice. Because science and especially lives in in specially in life sciences is inherently collaborative process. And in order to enable agents to collaborate, we need a way to have a verifiable chain of receipts. What do I mean? We need a solution which can provide these receipts proving every step, ensuring that every result can be trusted, and enabling repeatability as well as collaboration at scale. Having these pieces in mind, let's go to

**[1:44](https://www.youtube.com/watch?v=Fu45geO3zX8&t=104s)** the next step. So, stepping back, um we imagine agents as cooks in the kitchen. Giving them more tools or better tools, it improves kitchen's efficiency. Better knives, more pans, more ovens definitely boost the speed and quality. But it only enhances the local work. On the other hand, scientific work is not cooking alone in your own kitchen. It is closer to running a Michelin-star restaurant. To overcome this the the outcome depends on

**[2:32](https://www.youtube.com/watch?v=Fu45geO3zX8&t=152s)** providers and quality of your produce, high-level services, as well as an an ability to consistently deliver the same quality dish again and again and again. You cannot bring everything into one kitchen. The challenge isn't local. It's not local tools. The challenge is aligning the entire supply chain that it's repeatable and consistent. Today, we have already agents with plenty of tools and increasing in volume, number, and quality. And we also have on the hand data and specialized analytics algorithms and compute which is distributed across

**[3:20](https://www.youtube.com/watch?v=Fu45geO3zX8&t=200s)** different organizations and siloed. So, our vision is that whenever AI agent workflow automation matures, organizations will give to the agents not only tools, they will give them budgets. We're already kind of doing this in a primitive form by allocating tokens for token budgets for a specific task. But, what I'm talking is a bit broader. It's allowing agents to manage their own budgets to achieve their own goals. Whether it's to discover services, request data, negotiate execution terms, or pay for work across organizational

**[4:11](https://www.youtube.com/watch?v=Fu45geO3zX8&t=251s)** boundaries. At that point, an agent is no longer just a cook with a better knife. It starts to act like a chef. Uh like a executive chef, uh finding suppliers, ordering ingredients coordinating work at at the kitchen, and finally keeping the record of what has happened. That is why we're building Froglet. An open-source protocol for agents to discover, transact with, and receive verifiable receipt from external data uh data and service providers. For more detailed information,

**[4:58](https://www.youtube.com/watch?v=Fu45geO3zX8&t=298s)** obviously, go to our page froglet.dev, uh where you will find um general descriptions on how it works, what it integrates with. It Froglet is designed to be in between the moving parts. It's not designed to replace, it's designed to integrate. Integrates with different payment rails, it integrates with different agent harnesses, execution environments, and even transport protocols. And it doesn't require that every node in the network uses the same software stack. That's the beauty. We are not forcing everyone to use the same to to work the same way. We're just asking everybody to use the same interface. In the web page, you will find how to

**[5:45](https://www.youtube.com/watch?v=Fu45geO3zX8&t=345s)** run froglet with just how to install it locally just with one command. Or even how to run it remotely just with one prompt. So in essence, what we are saying is closed source and the collaboration often turns into a bespoke project, enterprise project that can take years and cost millions before any reusable workflow exists. On the other hand, froglet's mission is to make transaction layer much lighter. Once an organization decides that the data or resource or service is deemed shareable

**[6:34](https://www.youtube.com/watch?v=Fu45geO3zX8&t=394s)** and it's exposed on froglet, an agent can discover it, understand the terms, request the work, and receive a verifiable receipt. That setup costs few thousand tokens and takes minutes. Now, if I may, let me open our website for quick second. So if you land our if you go and land our homepage, you will see a couple of things. First, a lot of helper information which allows you or your agent to read through and understand how it works. And most of the webpage is focused on agent use.

**[7:23](https://www.youtube.com/watch?v=Fu45geO3zX8&t=443s)** But also we have some helpful documentation for you. Let me go through a couple of steps in the demo. So first of all, we define that froglet node by itself is not different implementations at each site. It is actually exactly the same node. It just plays different roles, whether it's a provider, requester, or marketplace. Marketplace itself is just a Froglet node, which is providing certain services. And what does it help to do? It It helps to find, to trust, to pay, and to prove that the work has happened. That is it. We're not trying to replace

**[8:11](https://www.youtube.com/watch?v=Fu45geO3zX8&t=491s)** any of functionalities of other tools or protocols. Whenever you are generating a or creating a new node, it generates a key pair for identity and signing the artifacts. And during the execution, everything is being signed with that signature. Meaning, everything is being signed in a chain, and the chain is only valid if all data points are not tampered with. And in in terms of discovery, request uh providers are publishing what services they uh they uh they're providing to the marketplace using the same protocol. And requester

**[9:00](https://www.youtube.com/watch?v=Fu45geO3zX8&t=540s)** requests a known marketplace just to provide lists of services that are available on that marketplace. From that that moment on, once the requester identifies the service that they want to work with, the communication is direct. There is no uh third party. And everything from quote to deal to execution and receipt happens in one interaction. Let me jump forward a bit. So So far, what I showed you is just a node talking to a node. Where agent comes in uh are the plugins that we placed inside the Froglet core. It integrates with different execution

**[9:50](https://www.youtube.com/watch?v=Fu45geO3zX8&t=590s)** environments and different harnesses, whether it's Open Claw, Nemo Claw, it's acts as an MCP server or plugin, and it's primarily designed that it is used by an an agent. The primary interface for humans should be an LLM. An LLM should drive usage of Froglet, whether you are a provider or a requester. So now maybe let's jump to a terminal

**[10:40](https://www.youtube.com/watch?v=Fu45geO3zX8&t=640s)** and I will show you a couple of things. First of all, I will show you how to how you can use Froglet remotely, meaning that there is a Froglet node running in a remote server where you can access and get a 15 minutes trial identity which you can play with. Second, how to run a Froglet locally on my machine here on a Docker. And third, how I will ask my Claude to interact with local installation and actually configure a service and try it out. So first of all, what we what I would like to do is to run a command to check whether Froglet try.froglet.com.dev actually exists and it works. That's fine.

**[11:28](https://www.youtube.com/watch?v=Fu45geO3zX8&t=688s)** So now what I can do is to create myself a token. And this this creates a temporary token for 15 minutes. And you can see it here created. And then what I can do also in exactly same manner, I can have access to the specific provider token. And this is a specific provider which adds two numbers. It's very simple example service provider. As you see that the tokens are different. That means that froglet nodes are different. Now, in order to execute this service,

**[12:17](https://www.youtube.com/watch?v=Fu45geO3zX8&t=737s)** what I need, I need to create a payload. So, I created payload which includes many things including schema, what kind of service I'm targeting, also which provider, and finally what input I'm providing it to. So, I'm providing it seven and [clears throat] five, 7 + 5. Now, what I need is to provide this payload to my remote remote froglet. And this executes, I need to get a deal ID. And this is where I have a receipt of actually deal happening. Now, deal has an ID already, but it

**[13:10](https://www.youtube.com/watch?v=Fu45geO3zX8&t=790s)** might have happened [snorts] that it takes some time to so execute. So, I take a for command for loop to actually wait for it, but it depends on the load on that temporary small node that uh that runs on on the cloud. And here we have an answer. It's 12. Fantastic, we have a correct answer. Um, so we have a entire loop finalized. Now, in order to run it locally, um what I need is to install it here. So, first of all, I will clear everything. As you see, the uh the the directory is empty, and what I do is I what I run is HBS Froglet Dev Agent, and what it will do, it will download

**[13:59](https://www.youtube.com/watch?v=Fu45geO3zX8&t=839s)** and install agent on a Docker. Let's wait a second. It's actually already there, so it just confirms that it doesn't need to download anything and it's working and it's running. And now I can see that uh there are two Froglets running, um but if I look at at the actually not IP addresses and ports, but I actually look at the node ID, I see that this is one and the same ID. And that means that each each Froglet can assume different roles, and at the same time can assume multiple roles. And we have here two roles as a provider and consumer at the same time. And just to prove that I'm running it on a

**[14:48](https://www.youtube.com/watch?v=Fu45geO3zX8&t=888s)** Docker, here it is, running on the same ports, same IP addresses, my local ins installations. So, now Claude, if I open my Claude, first of all, what I need to do uh is to see where Froglet MCP is enabled, and it is. That's fantastic. And what I will ask it to do is, first of all, I will change the permissions that it doesn't bug me. And what I will ask it is use from from that um CP only. Do not install anything.

**[15:42](https://www.youtube.com/watch?v=Fu45geO3zX8&t=942s)** And um let's be very specific. Let's see if it understands constraints. And I have here prepared a couple of steps. I won't do it them one by one. I'll actually ask it to do it all at once. In steps and provide the specific output. Great, it even goes ahead and um uh checks what is running. And what I'm asking it to do is first of all to see what was the status is life, which already did above.

**[16:31](https://www.youtube.com/watch?v=Fu45geO3zX8&t=991s)** Then if provider and runtime is healthy, then I want it to publish an artifact from a template, which is exactly the same template add two numbers. >> [snorts] >> Then uh what I want it that it actually finds and calls that service and invokes it locally. Uh asking it to add again five and seven. And it can wait a bit because it's an asking for a call. And then show the output what it got. So if if we go if we go down here, here is what we see that it actually executes all commands. And what we see that is actually um done

**[17:22](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1042s)** exactly as we asked. We It has a result some 12. And it It can create anything that you want. It can connect to You can ask load to connect to your database and provide row by row access for for uh for a payment or you can have a just your GPU running in the background and welcome the requests for computa- any kind of computation. In essence, it's a very simple way how to use it, but it packages a lot of um underlying protocols and underlying tools where now you're not shoving everything into a uh LLM context. It just has a services that it needs to interact. And

**[18:10](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1090s)** underneath there is a receipt, there is a payment, there is a execution environment. And uh there is a negotiation and marketplace uh hidden and it's uh doesn't stuff your LLM with context. So, going back to the slides. Some reason it scrolled down. Going back to the slides. Um So, what we what we have uh on our hands. Uh we have an open protocol called froglet which um has multiple things. First of all, uh it uh provides a way uh to to find resources outside the organizational boundaries.

**[18:59](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1139s)** Then it allows your agents to actually execute uh remote uh commands. And third, uh what it allows, it allows to have a verifiable receipt of receipts of what has happened. And I think that actually enables a collaborative science. That enables a progress of a perpetual science automation. So, please join us either via Froglet or Althea Bio. And please join us on GitHub. And thank you for listening.
