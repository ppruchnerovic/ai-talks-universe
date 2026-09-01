---
id: kAVRFYgCPg0
title: "MCP Creator Reveals the 2026 Roadmap for AI Agents"
slug: mcp-creator-reveals-the-2026-roadmap-for-ai-agents
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 23
published_at: 2026-04-13T14:00:06Z
video_id: kAVRFYgCPg0
youtube_url: https://www.youtube.com/watch?v=kAVRFYgCPg0
tags: ["Model Context Protocol", "Agentic AI", "Claude", "Anthropic", "Context bloat", "David Soria Parra"]
transcript: true
---

# MCP Creator Reveals the 2026 Roadmap for AI Agents

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `23 min`

`#Model Context Protocol` `#Agentic AI` `#Claude` `#Anthropic` `#Context bloat` `#David Soria Parra`

[Watch the recording](https://www.youtube.com/watch?v=kAVRFYgCPg0) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

David Soria Parra, co-creator of the Model Context Protocol (MCP) and Member of Technical Staff at Anthropic, delivers the keynote on where MCP has been and where it's headed. With 110M+ SDK downloads per month — outpacing React's first 3 years in just 16 months — MCP has become the de facto integration standard for agentic AI systems.

In this talk, David shares the 2026 roadmap, addresses the context bloat criticism head-on, and reveals upcoming features like triggers, streaming, and skills that will reshape how AI agents connect to enterprise systems.

What you'll learn:

110M+ Monthly Downloads — MCP's explosive growth and why it outpaced React's adoption curve
Enterprise Behind the Firewall — The biggest MCP deployments you never hear about: CRMs, Jira, Snowflake, internal wikis
Transport Evolution — Why the current streamable HTTP protocol needs a stateless redesign for hyperscale deployments
Long-Running Tasks — The new "Tasks" primitive enabling agentic communication for autonomous work
Cross-App Access — Seamless enterprise auth that eliminates OAuth flows by talking directly to identity providers
MCP Triggers — Webhooks for MCP, enabling servers to proactively notify clients of new data
Native Streaming — Incremental tool results are finally coming to the protocol
Skills Over MCP — Bundling domain-specific knowledge with MCP servers so agents know how to use them
Context Bloat Fix — Progressive discovery and tool search as the answer to the #1 MCP criticism
SDK v2 — Python and TypeScript SDK rewrites for better ergonomics, shipping in the coming months
This talk is essential for AI engineers, platform builders, and enterprise teams deploying agentic AI systems in production.

Links & Resources:

MCP Specification: https://modelcontextprotocol.io
MCP GitHub: https://github.com/modelcontextprotocol/modelcontextprotocol
Agentic AI Foundation (Linux Foundation): https://agenticai.org
MCP 2026 Roadmap (WorkOS writeup): https://workos.com/blog/2026-mcp-roadmap-enterprise-readiness
David Soria Parra on Software Engineering Daily: https://softwareengineeringdaily.com/2025/05/13/anthropic-and-the-model-context-protocol-with-david-soria-parra/
Timestamps (approximate — adjust after review):

00:00 — Introduction & MCP by the numbers
02:11 — What people built: from reference servers to SaaS integrations
03:36 — The weird and creative: Blender, Ableton, 3D printers
04:21 — The hidden story: MCP behind corporate firewalls
05:45 — Protocol evolution: remote servers, auth, elicitations, structured output
07:28 — MCP Extensions & MCP Apps
08:14 — Donating MCP to the Agentic AI Foundation
08:54 — MCP is the integration protocol: the 2026 mission
10:38 — Transport evolution: stateless HTTP for hyperscale
12:18 — Long-running tasks & agentic communication
13:44 — Enterprise readiness & cross-app access
14:56 — On the horizon: triggers, streaming, and skills
16:35 — Ecosystem work: SDK v2 for Python & TypeScript
17:44 — Building better clients & solving context bloat
19:46 — Composability through code & structured outputs
21:07 — Community call to action
22:14 — Closing

## Transcript

*3,881 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1s)** Okay, let me first make sure I don't show any of the uh Anthropic secrets. Hide all the models. Okay, great. Uh we had enough leaks this uh recently, so we don't need any more. >> [snorts] >> Um I'm David. Uh I'm a member of technical staff at Anthropic, uh one of the co-creators of MCP. Uh thank everyone for coming today. I'm talking a little bit about um you know, where have we been and where we're going with MCP. And to get you started, um I just want to talk about some of the numbers because I think they're actually quite impressive. We have now roughly, and that's really a number that's very hard to uh figure out, roughly 110 million plus uh SDK downloads

**[0:50](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=50s)** every single uh month. And that's not just, you know, clients or server authors doing their thing. This is like uh agents SDKs from OpenAI pulling in us in as a dependency, LangChain, um Pydantic, AI, thousands of tools and frameworks that are like really defining what we're doing in the uh agentic AI space, pulling us in um as as a dependency. All speaking MCP. And to put this a little bit into context, um the one of the most successful open-source projects in the last decade, React, um took roughly 3 years to reach that amount of downloads. MCP did this in 16 uh months. And I don't think this is there to brag,

**[1:38](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=98s)** but it's to tell you really that there was an ecosystem that was really in needing a standard uh to connect um the tools and systems that you work with to AI systems. And what it means is that people came to adopt it um because the alternative at the time was to build 16 times the same integration for a proprietary API, build your own platform, or build even your own um chat system at the time. But besides the raw numbers, if you step back where we started in November 2024, which feels to me like ages ago, but it's not even 16 months. Um

**[2:25](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=145s)** I want to show you what people actually built because I think it's an interesting uh part. When we launched it in November 2024, we had a bunch of set reference servers for MCP. The most standard things you would imagine to fill in the gap that we filled was most needed. Postgres servers, SQLite servers, file system servers, Git servers, of course memories, and the most basic things that now are built into every platform such as search and fetch. >> [sighs] >> And then very quickly really the key integration showed up. The the soft the the SaaS companies like ClickHouse, Notion Zapier really connecting their tools um to or their systems with MCP to the ecosystem. And this is the part where I think MCP

**[3:13](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=193s)** really grew up. When you start taking away from like a little like projects where like you have a fetch server going to something like a Slack integration is a real big unlock to truly enable agents and at the time chat um systems to interact with um your with the things you actually do care about on a day-to-day um basis at work. And then of course, because you all are uh very creative, way more creative than I could have ever been, things also got a little bit weird. We had some really interesting people doing uh fun stuff with connecting Blender up, um connecting Ableton up. Um one of my more favorite things was people uh connecting MCP servers to 3D printers or synthesizers. And apparently uh someone even built like a Fantasy Premier League um MCP server. So if you if you want to

**[4:02](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=242s)** do that, that's also a thing. And that I I love that creativity that all of you have shown in not just doing the most obvious things like creating, you know, the the a company-wide MCP server, but really taking it a little bit step further and using it as a creative outlet for uh some of the work you want to do. But then the most important part is something that I think very few people talk about. Because behind every corporate firewall, we're quietly wiring MCPs to systems of records and to the company data all day long. That's like your Salesforce CRM, your Jira tickets, internal wikis, Snowflake warehouses Snowflake warehouses, or HR system. And it's actually I think one of the biggest deployment surfaces of MCP, and you

**[4:50](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=290s)** never really see it or hear about it on Twitter or Hacker News. These are companies and people like you who have built like internal MCP servers to attach to attach the AI systems um to the actual uh um to the actual businesses and really make put or find a way for how we on a day-to-day basis um really use agentic systems to get work done um as knowledge workers. And I think it's to no surprise that even at Anthropic some of these internal MCP servers that we have that connect to our knowledge base, that connect to Slack, these type of things are some of the best far most popular ones because they're the ones to really help you in your day-to-day work to get things done. And this is I think where MCP now lives today. It's really in the

**[5:41](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=341s)** corporate and enterprise environment. And of course, in order to enable all of this, we have gone through a lot of changes over the last uh 16 months. And I'm I'm very lucky to have um some of the the brightest um and the most um um like some of the brightest minds in in some of the biggest companies um to help me with some of the decisions we're making around this. And so we have like of course um moved away from uh or not like taken MCP from what was originally like a standard IO only, like a local server only, to really enable remote servers. Like earlier last year, uh we have done a lot of work around authorization. And we have helped people to really understand what are the security implications of deploying MCP servers.

**[6:28](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=388s)** We have in addition added new um types or uh new um primitives to the specification to help people um uh to build richer um to build richer MCP servers such as elicitations. We have added structured outputs, which sadly is still a little bit of an under uh misunderstood concept that really enables things like uh code mode. And then most recently, we have taken a step in to trying to find the right pattern for how to do long-running tasks, which is effectively uh agentic communication um with uh primitive called tasks. And in the same vein, we have of course and done a lot of work on our governance structure, and we have most recently introduced something called SDK tearing, which helps all of you to better

**[7:16](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=436s)** understand the kind of guarantees an SDK that we provide um makes towards its stability, towards how closely it follows the specification, and how much it gets updated. And then of most recently, we have added extensions, uh which of course is a way for uh us experimenting with new features um around MCP um that really enables a more richer um space that if in a core protocol was not possible. And one of the most fun things in that space that I'm sure you will see a lot about is MCP apps, which is this like ability for MCP servers to provide interactive UI patterns uh to a front to an MCP client that can render them, and then with uh with an agent or with an with a chat system interact with

**[8:03](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=483s)** this. And this leads to some really really cool demos that I'm sure uh over the rest of the the the two days, you will see a a lot of those really fun things. Um uh >> [sighs] >> And then last but not least, by the end of last year, of course, and this has been you you just listened to 20 minutes of this before, uh we have uh donated MCP to the agentic AI Foundation. And I think this is an important step for a project to really grow up and make sure that there's a neutral place so that all of you can be sure that this is not going to go anywhere and that this still will stay open um and that this will uh be something that as um as an industry, we're going to work together uh to move forward. So in my mind,

**[8:56](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=536s)** today MCP is the integration protocol. This is what you reach for when you want to enable agentic systems, and when you want to particularly in companies and enterprises connect your systems of records, connect your internal systems uh to to um agentic systems. But of course, not everything is perfect. Um there's been of course uh things we need to do as as a community, as a protocol, um as an ecosystem that and we still have a lot of work ahead. In my mind, 2025 was about figuring out if a thing like MCP um is needed in the ecosystem. I think the

**[9:45](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=585s)** answer is clearly the resounding yes. But 2026 is going to be about making sure that MCP and um is ready to be really helping people to productionize agentic system. Because while, you know, we maybe on on Twitter and other aspects or other websites have the impression that everything is already fully agentic, the reality is in companies this year is where we will really see um agentic systems to um make a big impact on how we as knowledge workers are interact with um with AI. And so MCP will have a critical part in that and so for us it's important to make sure that as a protocol and as an ecosystem we are ready

**[10:31](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=631s)** to provide the right thing for people uh to do this in the best possible way. So, what do we need to do? On the protocol side there um we got a few things right and I think in general the protocol is in in a what I would say an okay state. I think there are things that we need to greatly improve and there are things that work quite well. Um one of the main things that we need to get right and one of the most focused areas within the MCP community at the moment is the evolution of the transport and you will hear more about this throughout the next 2 days, but it's been clear that while the current the current streamable HTTP transport protocol works okay for most use cases, it is challenging for

**[11:21](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=681s)** particularly large hyperscalers, for large deployments, um to deploy MCP servers efficiently due to its likes ways for how you need to effectively handle stateful sessions or alternatively reduce the set of abilities that your MCP client or MCP servers can do significantly. And what we're trying to do with this with this new um approach to transport is enable the full specification in a stateless way such that everyone can scale this in a in a more most natural way how you would have always scaled your web services in the past. So, this is a work that will land um in the next 1 or 2 months and make it into the the revision of the specification in June. And I really want to thank uh our

**[12:08](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=728s)** friends at Google and Microsoft um in in and a lot of other people to help us really shape this next iteration of the protocol. Second, um again this year I think people in the last few people have built honestly quite simplistic MCP servers. I think this time around we're going to see more and more usage of um of agents that want to get connected to um like a platform like the the Anthropic platform or an OpenAI platform and we will see an increased need to um deal with long-running tasks. And what we consider and in the protocol have added recently is this concept of task, which is nothing else but if it's a it's in the grand tradition of MCP we're not great at naming because it's effectively just doing agentic communication, um but we

**[12:56](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=776s)** still call it tasks. I don't know why, but that's what we do. Um and um this will enable uh long-running autonomous work and I think this is increasingly important because model capabilities are clearly clearly um increasing uh at a at a super fast rate and so the ability for a model to do increasingly long task will just go and continue this year. And with that we need to make sure that the protocol is ready that you can take some of these long-running tasks um and and use them on MCP servers and run these long-running tasks there. Um We have an early experimental prototype of task in the protocol since November, but there's a lot of things that we need to still get right. And that's what we're going to work on in the next 2 months also for this June specification release. And then last but not least again one of

**[13:45](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=825s)** the big focuses of the uh of the of the current road map for the next 2 months is making MCP uh increasingly ready for enterprises. And while I think the current authentication specification uh authorization specification is quite good, there are still a lot of things that we want to get right. And one of the most exciting things that you will hear later more about is uh this thing called crop uh cross-app access, which is really a nice way for seamless integration such that you connect to an MCP server and the without having to go through an OAuth flow because magically it will just talk to your identity provider and already get the right token requires because you're as a as a person at work are already logged in. So, this will enable an enterprise a much more seamless integration such that people

**[14:33](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=873s)** don't have to worry about logging in anymore and that honestly uh MCP becomes less and less um a thing that an an average user has to engage with, but it just magically works. And that's where we want to get to um to the point where things like MCPs are um a thing that just work and that a user um does not have to think about. And then on the horizon we have a few things that I think are really really interesting. Two things that are particularly interesting to me, three things that we are going to focus uh in in general. Number one is triggers, which is nothing to say that basically we want to have webhooks in MCP, um which means that that MCP servers should be able to tell our client that they have new data, that they want to have an interaction, and ask the client proactively to actually start engaging with the server again. And I think this

**[15:21](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=921s)** unlocks a lot of use cases around productivity that I think will enable a new way of how we build MCP servers and new interactions that I think are more richer for users. And so I'm really excited about that kind of work. Second, of course, um this is a a long-standing issue that MCP has no native streaming support and this was very deliberate in the early days because streaming is hard, streaming is difficult to do, and streaming has a lot of complexity. But now I think it's really the time for us to look at streaming again and making sure that you can get incremental tool results. And then last but not least, we do want to serve and I think this will land as an extension in the next uh few weeks. We do want to finally serve skills over MCP servers so that you can bundle up domain-specific knowledge with an MCP server and tell the user and tell the

**[16:09](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=969s)** agentic system on the other side how to best use your your MCP server. And I think this will unlock particularly um good use cases for a large MCP servers that really want to make sure to explain how to use certain subpath of the MCP of their of their server. So, I'm really really excited about that part and I think it's going to be a very interesting way to serve skills um in in a more centralized way. Okay. So, that's the protocol side. That's, you know, that's let's that's us doing our work um and just a bit of a brief over overview. But I think there's a thing that we still need to do in the ecosystem that is quite important. Number one, what we're going to do is I think some of the SDK shapes and um I I can hold my hand up here for being um

**[16:58](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1018s)** part of the the the problem that I've created the Python SDK. Um is that some of the shapes there are not great and I think um we need to greatly improve the ergonomics and the usage of these MC of these SDKs. And so we're going to ship um a Python uh SDK V2 uh and we're going to ship a TypeScript SDK V2 in the next few months that really make a a more better approach and a more ergonomic approach to how to build MCP clients and how to build MCP servers and get rid of a lot of the crap that has been accumulated over time. Um and of course we're making sure that if you point Claude or another uh model uh at your old code base that it will be smoothly translating this to the new code base uh hopefully without hitches. Second, and that's less what we need to do but uh what we as an ecosystem really

**[17:47](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1067s)** need to do. We need to go and build better clients. If there's one thing that I'm really worried about and really, you know, maybe complaining about um in the ecosystem, it's the current state of clients. And this is I think the root cause of a lot of the um criticism MCP is currently getting. One part is, for example, that people complain continuously about context blow in MCP and I'm sure un- unless you live under a rock, um you must have heard that people are uh blaming MCP for uh for context blow. But the interesting part is that um we already know the mechanisms for how to go around context blow. This is called progressive discovery. And the idea

**[18:36](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1116s)** behind progressive discovery is to not take all the, you know, 20, 50, 100 MCP tools you get from MCP server and just naively dump them into the context window, but use a more modern mechanism such as tool search to only load the tools when they're needed. And these are things that this is very similar in its uh its general idea for how things like skill work skills work of like loading things only when they're needed. And there are many ways to implement this. Um platforms like OpenAI and Anthropic offer these um as um as features, but it's also a a bit there's you're also able to implement that yourself. And in this example here, you see on the left side

**[19:24](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1164s)** how uh Claude Code used to um a load MCP tools before it implemented tool search and you have like 22% of a about 200K token window taken up by MCP tools and then on the right side um all of this is now deferred in the current uh implementation of Claude Code where it loads them only when needed. Second, people love to use um uh really compo- uh compose or bluff one ability, for example, from CLIs, which is this composability through bash commands. You can take a CLI command, you can pipe it to another one, and people often say, "Oh, this I can't do this with MCP." But, of course, you can. And I think this is a mechanism we have not seen much explored yet, and I want to see the ecosystem explore more, which is

**[20:12](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1212s)** composability through code. And the idea is pretty simple. If you give your MCP client, um, a basically an interpreter and al- ask the model to write code, and that code then calls MCP, then you get composability. And this is where structured output comes in, because structured output allows the model to reason about the return types. And so, I want to see more of this, because I think in experimentation, we know that this is an exciting thing where you can greatly optimize, um uh the maybe, you know, uh, latencies, uh, and gr- relieve, um, and get to more richer expressiveness in how your client can interact with MCP calls. And in this example on the on the on the slide, you see how you can connect them together and then, uh, emit finally, without ever

**[21:01](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1261s)** going back to inference, more complex objects. Okay. So, that's the protocol work that we need to do. That's the ecosystem work we need to do. But, last but not least, we need you as a community. One of the the coolest parts about this this journey, and it's like, honestly, still mind-boggling for me that I'm standing in front of uh, 200 300 400 people, um, after a year of done my little specification. Um, but what's the most important is your feedback. You see things on a day-to-day basis, uh, in environments that I I might not know, that we, uh, as the core maintainers and the maintainers of the MCP, do not know. And we need to hear from you. We need to hear from you what are the things you're excited about. I want to hear from you, uh, do are you excited about skills in MCP? Are you

**[21:48](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1308s)** excited about triggers in MCP? Wha- and quite frankly, also about your criticism, because criticism is one of the things that gets us going and improve our things. Things like the new transport specification came out of people coming with very real concerns, uh, and basically telling us that we got parts of it wrong. And the best part is that, um, hopefully, we're still humble enough to say, "Okay, we got it wrong. Let's go and fix it together." Cool. So, with that, thank you, everyone, for being here. I'm super excited for the uh, for the remaining talks, um, about the the different areas with we how people are building MCPs, how people are using MCPs, and part of how we are developing, um, the specification. I'm going to be around most of the day, so try to find me if you have questions or anything like

**[22:35](https://www.youtube.com/watch?v=kAVRFYgCPg0&t=1355s)** that. Thank you so much. >> [applause]
