---
id: Q9ycQHbDdJs
title: "Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio"
slug: agents-need-receipts-not-more-tool-calls-armanas-povilionis
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Armanas Povilionis"]
channel: "AI Engineer"
duration_min: 10
published_at: 2026-07-20T00:00:00Z
video_id: Q9ycQHbDdJs
url: https://www.youtube.com/watch?v=Q9ycQHbDdJs
youtube_url: https://www.youtube.com/watch?v=Q9ycQHbDdJs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio

**Armanas Povilionis**

`AI Engineer` · `AI Engineer` · `2026` · `10 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Q9ycQHbDdJs) · [Conference site](https://www.ai.engineer/)

## Description

In this talk, I’ll show an agent publish a service, another agent discover and invoke it, and a signed receipt that proves what happened. The point is simple: if agents are going to buy, sell, and compose work across hosts, logs and API dashboards are not enough.

Froglet is an open-source protocol and node for agent-to-agent compute. It reduces named services, data-backed services, and open-ended compute to one signed flow: Descriptor  to  Offer  to  Quote  to  Deal  to  Receipt. The same surface is exposed through MCP and OpenClaw/NemoClaw as one froglet tool, so agents can publish, discover, invoke, and verify work without custom glue for every provider.

The hot take: agentic commerce should start with verifiable work, not checkout pages. Payment rails can change. Receipts, identities, workload hashes, and deal state need to survive across models, hosts, and marketplaces.

see froglet.dev

Speakers:
- Armanas Povilionis (Alithea Bio): Technologist and systems strategist working at the intersection of AI, infrastructure, biology, governance, and incentive coordination.
X/Twitter: https://x.com/PovilionisA

## Transcript

*972 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=1s)** What is the most valuable agentic automation work? I think scientific research is quite high on that list. After a decade working in life sciences collaboration projects, I think that more tools alone will not enable automation of scientific research. Because science work relies on collaboration. For agents to collaborate autonomously, we need a chain of verifiable receipts. We need a solution which can provide these receipts proving every step,

**[0:50](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=50s)** ensuring that every result can be trusted, and enabling collaboration at scale. Let's step back. Imagine an Imagine agents as cooks in the kitchen. Giving them more tools improves kitchen's efficiency. Better knives, more pans, more ovens boost the speed and quality. But it only enhances local work. Scientific work is not cooking alone in your own kitchen. It is closer to running a Michelin star restaurant. The outcomes depend on suppliers and their produce,

**[1:40](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=100s)** the level of service that you can provide, and an ability to consistently deliver the same quality dish again and again and again. You can cannot bring everything into one kitchen. The challenge isn't local tools. It is aligning the entire supply chain. Today we already have plenty of tools for agents and agent automation. On other hand, we also have data and specialized analytics algorithms, which are distributed across organizations and and and live in silos. At Alifeia, our vision for Froglet

**[2:32](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=152s)** is very simple. As agentic workflow automation matures, organizations will not just give agents more tools, they will allocate them budgets. We already kind of doing it in a primitive way, allocating them token budgets per task. The next step is a bit broader. It's allowing agents to manage their own budget for anything that they might need, discovering services, requesting data, negotiating execution, paying for work in cross-organizational

**[3:21](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=201s)** boundary setting. At that point, the agent is no longer just a cook with a better knife. It starts acting like an executive chef, finding suppliers, ordering ingredients, coordinating kitchen the kitchen work, and keeping a record of everything what's happening. That is why we're building Froglet. The protocol for a agents to discover, transact with, and receive verifiable receipts for external data and services and service providers. Froglet is designed to sit in between of

**[4:11](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=251s)** many moving parts. And that's why we are not replacing existing tools and protocols. We integrate with different payment rails, with different agent and harnesses, execution environments, and even network transport protocols. It does not require that everyone has the same software stack. It just requires that everyone has the same interface. For more details, please visit froglet.dev. Where you will be able to run to see how to run Froglet locally with just one command. Or you can even try Froglet remotely

**[4:59](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=299s)** with just one prompt. So, in essence, close scientific collaboration often turns into a bespoke enterprise project. That can take years and cost millions before even first reusable workflow exists. On the other hand, the Froglet's mission is to simplify that much more. Once your organization has deemed that the resource is shareable, a provider should be able to expose it for Froglet. An agent can discover it,

**[5:47](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=347s)** understand its terms, request the work, and receive verifiable receipt. That costs few thousand tokens and takes minutes. Let's deep dive a bit deeper. So, here is our Froglet Dev website, and here you can see um a walkthrough button. If you click on it, you will have a much more detailed review of what's happening, and you can read documentation in even more detail. So, first of all, the Froglet network consists of homogeneous nodes. Every single actor in the environment

**[6:37](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=397s)** runs the same core um node. It just plays a different role. There are requesters, there are providers, and there is a marketplace, which is a just a Froglet running the specialized service. What it solves is how to find how for a requester to find the providers, how to trust them, how to battle pay or settle, and how to prove that execution has happened. Whenever you're generating a new node, you're generating a key pair for identity and signing. And every time you execute anything with

**[7:29](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=449s)** Froglet, it uses your keys to sign on the chain. And the chain consists of everything what you do, from descriptors to offer to quote to deal for invoice and finally receipt. Therefore, you cannot tamper with any part of this chain. Otherwise, the chain will be broken. And to discover services, providers of services, just register and describe their services to the marketplace. Marketplace itself provides the services for providing descriptions and for indexing what's what is existing what services existing

**[8:16](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=496s)** on the marketplace. Once a requester requests an index of available services, from there on, it continues direct communication with that requester. It doesn't need a middleman. So, the requester and provider communicates with each other directly, and it all happens in one interaction: requests, signing, execution, and receipt. On a payment side, we have a system where it where all payments, if it's not free, has two parts. One is a base payment, and another is success fee. So, base payment protects the providers that they wouldn't be attacked by uh

**[9:07](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=547s)** multiple requests. And success fee is providing the requesters from malicious providers. In essence, the Froglet [snorts] itself is not an AI agent, but it is created specifically for agents as an interface to find each other. As an interface to find the data and services cross borders and execute these deals directly with each other. So, coming back to recap, a froglet lets agent to discover external scientific resources,

**[9:58](https://www.youtube.com/watch?v=Q9ycQHbDdJs&t=598s)** execute work across organizational boundaries, and it gives every transaction a verifiable receipt. Together, this opens the door to autonomous scientific progress. We hope you will join us and enjoyed this talk. Thank you.
