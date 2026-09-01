---
id: z6SuFQYClQI
title: "The MCP Features Bloomberg Built for High Stakes Financial AI"
slug: the-mcp-features-bloomberg-built-for-high-stakes-financial
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 11
published_at: 2026-05-02T22:00:16Z
video_id: z6SuFQYClQI
youtube_url: https://www.youtube.com/watch?v=z6SuFQYClQI
tags: []
transcript: true
---

# The MCP Features Bloomberg Built for High Stakes Financial AI

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=z6SuFQYClQI) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: Interoperability Isn’t Enough: Building Trustworthy AI Infrastructure with MCP - Ania Musial, Head of AI Platforms Product, Office of the CTO, Bloomberg

Ania Musial leads AI Platforms at Bloomberg and serves on the board of the Agentic AI Foundation. In this keynote, she breaks down why interoperability alone isn't enough for production AI in financial services, and what Bloomberg is building on top of MCP to make agentic systems truly trustworthy.

- Bloomberg's Trustworthy AI Principles: The three pillars guiding how Bloomberg builds AI for high-stakes financial decisions: trusted data sources, transparent attributions, and real user problems
- Why MCP Alone Falls Short: MCP connects systems, but out of the box it doesn't provide the guardrails, governance, or production reliability that regulated industries demand
- Financial AI Risk Taxonomy: How mistakes in financial AI can generate reputational, legal, and market risk, from hallucinated narratives to unauthorized transactions
- MCP Interceptors Explained: The proposed interceptor framework that enables validators (inspect and block unsafe payloads) and mutators (transform, redact, and enrich data) at the protocol layer
- Interceptors for Guardrails: How Bloomberg uses interceptors to enforce citation requirements, detect unsafe actions, and block execution when policies are violated
- MCP Variants for Multi-Model Environments: How variants let a single MCP server expose optimized tool interfaces for different models, agents, and contexts without duplicating servers
- Variants and Predictability: Why tailoring interfaces per model reduces noisy evaluations and inconsistent behavior, making agentic systems more controllable
- Bloomberg Terminal's Agentic Transformation: How their flagship agentic AI application replaced hundreds of separate apps with a conversational interface for financial professionals
- Contributing Back to MCP: Bloomberg's work through the Financial Services Interest Group, including SEP 1763 (interceptors) and SEP 2053 (variants)

Whether you're building AI infrastructure for regulated industries or trying to make MCP production-ready, this talk lays out why trust has to be engineered from the ground up.

Links & Resources
- Bloomberg AI: https://www.bloomberg.com/ai
- Bloomberg embraces MCP: https://www.bloomberg.com/company/stories/closing-the-agentic-ai-productionization-gap-bloomberg-embraces-mcp/
- MCP joins the Agentic AI Foundation: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/
- Agentic AI Foundation (Linux Foundation): https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- Ania Musial on LinkedIn: https://www.linkedin.com/in/aniamusial/

Timestamps (approximate, adjust as needed)
00:00 - Introduction and Bloomberg Terminal overview
01:05 - 40 years of Bloomberg in financial services
02:02 - AI at Bloomberg and the shift to agentic AI
02:24 - Defining trustworthy AI: three guiding principles
03:22 - The infrastructure underneath: gateways, models, tools, MCP
04:03 - Why MCP alone isn't enough for production
04:30 - Contributing to MCP through the Financial Services Interest Group
04:47 - Financial AI risk: what "harmful" looks like in finance
05:53 - MCP Interceptors: validators and mutators explained
07:08 - Context governance and managing model variability
07:36 - MCP Variants: one server, multiple optimized interfaces
09:02 - How variants improve predictability and trustworthiness
10:04 - Closing: trustworthiness emerges from system design

## Transcript

*1,955 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=z6SuFQYClQI&t=0s)** Good morning. Uh just 10 more minutes and you get coffee. Um cool. So, thank you for the introduction, Angie. Uh my name's Anya. I have a product group at Bloomberg where we focus on the uh infrastructure, the developer tooling, and the systems that really power our AI applications at Bloomberg. Um I also have the pleasure of serving as a board member on the AIF. So, thank you for having me. Um and as you can tell, I'm the odd duck out. I'm actually like one of the finance bros. Um so, I will take at least a minute to shill kind of what we're doing and just kind of talk about my problems. Um so, pop quiz. Uh who here has seen one of these Bloomberg terminals before? Okay, at least five Okay, great. Um so, contrary to what you may have read on the internet recently, it's not something that you can just vibe code in a weekend.

**[0:48](https://www.youtube.com/watch?v=z6SuFQYClQI&t=48s)** Joke. Okay, good. Um so, with the remaining uh 9 minutes and 30 seconds, I hope to convince you at least like a tiny bit that, you know, while interoperability is lovely and connects our systems, it's really building this trustworthy infrastructure that helps it be viable for us in production. Okay, quick history lesson. Um for more than 40 years now, Bloomberg has been uh serving leaders in the global financial industry to really um have trusted sources of information that they can use to make really critical financial decisions. So, you see our clients over here. Um we have folks on the buy side like asset managers, portfolio managers, hedge funds, you know, those people who are really advising clients on investment ideas and opportunities. Uh we have folks on the sell side. So, those who um like traders or research analysts, investment bankers, and

**[1:36](https://www.youtube.com/watch?v=z6SuFQYClQI&t=96s)** corporations who are really like managing these types of uh investor relations and helping facilitate transactions between buyers and sellers. So, across all of these participants, the common thread is really that these financial decisions they're making are really in high-stakes and very highly regulated environments, right? Which means that across the industry, there are significant expectations around transparency, accuracy, and market integrity. Now, for the past 15 years or so, AI is really incorporated into multiple Bloomberg products and has really become an important part about how we deliver insights to these kind of participants and help them navigate markets and turn this type of information into action, right? And with Agent AI, we've obviously [clears throat] entered new phase. Okay, so what do we mean by trustworthy

**[2:26](https://www.youtube.com/watch?v=z6SuFQYClQI&t=146s)** AI? Well, back in January, we released our flagship Agent AI application, announced Ask B, and it's really transformed how these kind of customers might discover insights and interact with them on the Bloomberg terminal. So, previously, they were using like hundreds or thousands of applications to find these things and now they have a conversational interface to interact with it. Uh this has really transformed or really helped us shape how we understand what it means to build trustworthy infrastructure for AI. So, for us, this means uh three guiding principles. Uh number one, we have to derive answers from uh trusted source of the information, so like real things down to the data point. We have to provide transparent attribution so that uh financial professionals can independently verify that we're what we're telling them is correct.

**[3:13](https://www.youtube.com/watch?v=z6SuFQYClQI&t=193s)** Uh and we have to, most importantly, build features that solve uh real user problems. So, maybe not your problems or my problems, but those uh investment professional problems. Uh and none of this isn't possible without uh the right infrastructure and the right uh you know, open source projects underneath. Um so, inside this network, there are gateways, there are models, there are tools, there are agents, and obviously, there's MCP. So, from an infrastructure perspective, uh what does this mean? Well, all those security bits that we heard earlier, we need we need those nines, that's just like table stakes. Um but we also need to uh provide visibility and controls into the system behavior at runtime so that you can uphold these types of principles. Uh and we also have to empower platform teams like we heard earlier to really enable continuous product improvement as the technology really evolves.

**[4:03](https://www.youtube.com/watch?v=z6SuFQYClQI&t=243s)** So, none of this is possible without MCP obviously, but what we found is it doesn't give you the out of the box the guardrails, the correctness, the governance, and that production reliability that you need in order to make something like this happen. Okay. So, how are we you know upholding these principles when we do our product development? Well, some of it actually comes directly through engagement into MCP. So, I'm going to give you a couple of examples of work that we've done mostly through the financial services interest group as part of the contributors to that. So, thanks to Samba who's on the technical committee who's really representing us there. And so, two examples I can think of are interceptors and variants. So, I've talked a lot about trustworthiness which is a core tenant

**[4:51](https://www.youtube.com/watch?v=z6SuFQYClQI&t=291s)** of responsible AI. And you can think about it through a very simple lens that I have up here. So, AI systems should be both helpful to their users and harmless to the markets and to the clients. So, what does harmful actually look like? Well, unlike or more so than general consumer AI, mistakes in financial AI systems can generate real reputational, legal, market risk. There's a like a lot of money and a lot of commas on the line. So, the types of risk that we're trying to avoid might include things like um the disclosure of non-public information, unauthorized financial advice or transactions, market manipulation, misconduct, misleading or dare I say hallucinated financial narratives. And to mitigate these types of risks, we really develop a financial specific

**[5:39](https://www.youtube.com/watch?v=z6SuFQYClQI&t=339s)** taxonomy of safeguards that guide our systems to this like happy green quadrant over here. Now, the challenge becomes integrating these types of uh services consistently uh as data's flowing between these tools and across various boundaries. So, this is where something like the Interceptor framework might come in. We heard that from Nick earlier. So, what do Interceptors do? Uh the proposed Interceptor framework uh enables messages to be intercepted, as you might expect, uh validated, and transformed at various extension points throughout the life cycle of the protocol. Um so, you can think about that at like directly in viewing controls at the protocol layer that get like deterministically executed. And there are two types of Interceptors. Uh those who like Kubernetes webhooks, this might sound a little bit familiar, but there are validators and there are mutators.

**[6:25](https://www.youtube.com/watch?v=z6SuFQYClQI&t=385s)** Uh so, what do validators do? They allow you to question, uh is this safe? So, you can inspect payloads. You can also block things if it makes sense per your policy. And mutators allow you to make this safe. So, you can transform payloads, you can redact things, you can enrich them if you need to. Uh what does this uh what does this allow us to do? This can uh allow us to inject these types of controls that we have over here, uh you know, call these types of guardrails, um even uphold uh principles like making sure that we have citations. So, the trustworthiness here should be fairly self-evident. You know, we can detect these safe unsafe actions, we can uh block execution when necessary, and we can make sure that these things are verified as they're crossing boundaries. Cool. So, that gives us a way to uh have some control over like context

**[7:12](https://www.youtube.com/watch?v=z6SuFQYClQI&t=432s)** governance. Um now, what do we do with uh the sea of models that we have and the availability that comes with that? Um sorry. I forgot that I had a a thing. Um if you're interested in this type of topic, um SEP 1763 has a good conversation about it, and my colleagues uh Kurt and Canice are going to be giving a uh in-depth talk about this later at 2:55 uh about the protocol. All right. So, let's talk for a minute about uh variants. So, in our environment at Bloomberg, we have many flavors of models. Uh they could be open weight, they could be commercial, they could be uh homemade, grass-fed, fine-tuned for finance, you know, the types of things that price bond valuation in real time. Um and in this case, we're talking about large language models, and there might come a time where um you know, you really want to uh um

**[8:00](https://www.youtube.com/watch?v=z6SuFQYClQI&t=480s)** uh provide the same type of capability or expose it to different types of interfaces or different types of models. Uh so, I have an example here. It's called get portfolio. If you're allergic to finance, think of it like get file system as an example. Um and you know, I want to expose the same type of capability, but in like slightly different situations. So, the first one might be a coding assistant, you know, you're you're you're chugging along, you want something that's uh really IDE friendly for what you're working on. Uh the second one might be something that's much more automated. You have a reduced amount of context that you can take. And the third one might be a conversational interface. Um an alternative might be, you want to expose this to three different model families. Maybe one speaks JSON, the other one's really good at markdown. The other one's optimized for for um XML. So,

**[8:47](https://www.youtube.com/watch?v=z6SuFQYClQI&t=527s)** naively what you could do is build three of these separate MCP servers, you know, one for each agent type. Or naively, you could create one generic tool that doesn't really serve any of these agents optimally. Uh and that's where something like variants might come in. So, variants enable an MCP server to expose multiple parallel versions of the same tools. You can optimize them for different models, for different agents, for different contexts. It also allows you to choose a default, so it just works like a default behavior. And you can also allow clients to dynamically select the right ones for the requests, so you can give them a little bit of a hint. Um Now, what does this do with have to do with being trustworthy? It sounds like I've just given you some more flexibility, but arguably no. Uh uh variants actually make AI systems a bit more predictable. They make them

**[9:35](https://www.youtube.com/watch?v=z6SuFQYClQI&t=575s)** [clears throat] more controllable, evolvable. You avoid duplication by bundling these different configurations the same capability into like a single structured unit that you can now manage more efficiently. So without variance, I also find you get more noisy evaluation results and inconsistent behavior. But with with variance, each model really gets the interface that's designed for it, which is quite nice. If you like this type of work, it's being formalized in SAP 2053. Okay. That was a bit of a whirlwind introduction into finance. The core idea is really simple, but you know, I believe that the trustworthiness that we're looking for really emerges from the ground up and it's through how we design our systems. And if this is a space that you're interested in or that also keeps you up at night, you know, we'd really love to have you

**[10:21](https://www.youtube.com/watch?v=z6SuFQYClQI&t=621s)** involved. So these the ideas are being shaped through the MCP community, through the financial services interest group, and look forward to the projects that will be joining the AAIF and in the broader community. So come through. Thank you. >> [applause]
