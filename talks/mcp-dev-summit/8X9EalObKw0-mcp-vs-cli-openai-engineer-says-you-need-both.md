---
id: 8X9EalObKw0
title: "MCP vs CLI OpenAI Engineer Says You Need Both"
slug: mcp-vs-cli-openai-engineer-says-you-need-both
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 14
published_at: 2026-05-01T22:00:06Z
video_id: 8X9EalObKw0
youtube_url: https://www.youtube.com/watch?v=8X9EalObKw0
tags: []
transcript: true
---

# MCP vs CLI OpenAI Engineer Says You Need Both

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=8X9EalObKw0) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: MCP x MCP

Nick Cooper, is a Member of Technical Staff at OpenAI and core maintainer of the MCP Steering Committee, delivers a thought-provoking keynote on where MCP sits in the protocol stack — and where it's headed. As a co-founder of the Agentic AI Foundation (AAIF) and the person behind MCP Apps, Nick brings a unique insider perspective on why MCP isn't just another API — it's an API designed for AI.

Topics covered in this talk:

Emergent Properties of MCP — How transformation and composition of simple building blocks create powerful, complex interactions
Protocols Are Just Languages — Why thinking of protocols as communication layers (from electrical signals to HTTP to MCP) demystifies the entire stack
Token Efficiency & Code Mode — Why output tokens are the most expensive symbols we have, and how code-mode patterns (shell and function invocations) optimize context usage
MCP vs CLI: You Need Both — Nick's definitive take on the hottest debate in AI tooling — CLIs bring history, MCP brings AI intent, and the best systems combine them
MCP as API for AI — The subtle but critical shift: MCP forces you to design for models, not developers, with standard auth (OAuth 2.1), schemas, and security patterns
Intent-Driven API Design — Why wrapping existing APIs in MCP (rather than auto-transforming OpenAPI specs) produces dramatically better agent experiences
MCP for Agent-to-Agent Communication — The next frontier: tools as abilities, tasks as delegated work, and truly agentic communication when both sides understand intent
The Identity & Discovery Problem — The unsolved challenge: with thousands of MCP servers, how do we make them discoverable and establish robust identity?
This talk is essential for AI engineers, protocol designers, and anyone building MCP servers or agentic systems who wants to understand where MCP fits in the bigger picture — and what's coming next.

Links & Resources:

Nick Cooper on LinkedIn: https://www.linkedin.com/in/nicknotfun/
MCP Protocol Blog: https://blog.modelcontextprotocol.io/
MCP Apps Extension: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
Agentic AI Foundation (AAIF): https://aaif.io/
MCP Dev Summit: https://events.linuxfoundation.org/mcp-dev-summit-north-america/
Timestamps (approximate — verify before publishing):

00:00 Intro & last year's MCP talk recap
00:44 Emergent properties: transformation & composition
01:45 "MCP is dead" — addressing the controversy
01:55 Protocols are just languages
02:31 The protocol stack: from electrical signals to MCP
03:52 Token efficiency: symbols per second for AI
05:18 The cost of output tokens & asymmetric communication
05:32 Code mode: shell vs function invocation patterns
07:02 How code mode improves token efficiency
07:46 CLI vs MCP: the real debate
08:13 MCP as a specialization layer in the stack
09:00 MCP is an API for AI — the intent shift
10:13 Intent-driven design: the email API example
11:07 CLI vs MCP verdict: you clearly want both
12:11 MCP for agents: tools as abilities, tasks as work
13:24 The identity & discovery problem
14:16 Closing

## Transcript

*2,384 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=8X9EalObKw0&t=0s)** As Angie said, I'm Nick Cooper. Have a weird-sounding title of member of technical staff. Um and a lot of weird responsibilities across this whole Legen Tech AI Foundation MCP thing. Um I wouldn't necessarily consider myself as influential in it though. Uh today, the talk, unlike a lot of what else you've heard, is very exploratory, very like thought-provoking is what I'm aiming for, very not concrete. If you're around last year, it's basically the same sort of style as last year's presentation, where it was just more about what we could do. So, last year was a much, much smaller audience, much smaller space, room, significantly dimmer lighting. Um but what I talked about then was transformation and composition, these

**[0:48](https://www.youtube.com/watch?v=8X9EalObKw0&t=48s)** ideas of emergent properties of MCP. And what do I mean by emergent? I mean that like by combining these simple building blocks, we get much more complicated interactions, much more valuable experiences to users or businesses or even server providers. I think actually the two talks before me demonstrate this really well. Like transformation was taking one layer and transforming it into another one, as we saw from WorkOS. And composition was this idea of maybe we don't just need one wall of text or one giant application. Maybe we need an environment that merges multiple UIs together in some way that's meaningful and understanding. Now, over the past year we've seen a lot of this. There's a lot of composition, a lot of transformation, there's a lot of MCP. There's a lot of gateways, communication systems, the protocols are

**[1:37](https://www.youtube.com/watch?v=8X9EalObKw0&t=97s)** proving dramatically with new features like tasks, as well as MCP UI, the latest and so far only extension to MCP. But then of course we've heard the other news that have obviously to everyone in this room MCP is dead. Um So, how do I think about this? I think about it sort of mostly at a higher level in that protocol like I have a sort of background where I used to like teach high school kids in that in like computer science. And protocol is a very confronting word. It sounds technical, it sounds confusing, it sounds unapproachable. They're just languages. And when you speak a language like to another person, it's very similar to how computer system speaks to another system. And then once once you have that dialogue going, you

**[2:25](https://www.youtube.com/watch?v=8X9EalObKw0&t=145s)** want it to be efficient, and then you start to wonder what can you do with it moving forward. Now, so just as I said, protocol is just another form of communication, and what can we layer upon this and transform it? So, in the case of computers, we start with well these days electrical or light. Then we build layers on top of this, we get to TCP, we get to HTTP. Every layer up we're constraining and specializing and building new layers that add new functionality. We get to REST, we get to Open API. Every layer added new verbs, more structure. And MCP is just an extremely high layer compared to this, but it also touches on lower layers. Like we see MCP servers, but we also still use standard IO MCP servers. These layers of abstraction, these

**[3:13](https://www.youtube.com/watch?v=8X9EalObKw0&t=193s)** layers of standardization, create standard patterns for observability, authentication, just the general structure and security of such things. Like for example, do you trust your agent with a private key? Maybe. I sometimes do, as a lot of people here I expect have done as well. But I probably shouldn't. And these specializations and standard layers create injection points. Like one of the active discussions for an upcoming feature for MCP is interceptors. And that's recognizing that we need places to inject standard policy controls, security controls, or just telemetry. Now, with all these layers, it's a common like lesson in computer languages that's sort of a bit past now that if you really want to get be efficient, you

**[4:01](https://www.youtube.com/watch?v=8X9EalObKw0&t=241s)** need to be low level. Like it used to be that like, oh, if you actually want to get performance out of the system, I have to know assembly. Or then I have to use C++. Or then I have to be on device. And the layers themselves get higher, like the computers today use obnoxiously large amounts of memory and RAM and compute compared to the standards that we had say 30 years ago. When it comes to efficiency of a protocol, a reasonable way to refer to it is very similar to languages itself, which is symbols per second or just concepts per second. Efficient communication means you can express a complex idea. So, it means you can use fewer symbols, fewer words, fewer sounds, or fewer tokens. They are essentially the most expensive symbols we have today.

**[4:48](https://www.youtube.com/watch?v=8X9EalObKw0&t=288s)** Uh they cost money, but they also cost time. And when a model's running to a task, these tokens are also asymmetric. Like the model's output costs more than the input. Now, there's a function of this that's like billing and inference and GPUs and this sort of thing, but also time. Like it takes a long time to wait for something, be it a person or an agent or a model, to think of your input and generate a response. So, there's always this asymmetry in communication. Um now since output is more expensive and time is precious, we always want to be very efficient and get as much value from this output per round of input as we can. And we're seeing this in MCP. So, early exploration of MCP, as many talks today have demonstrated in ways,

**[5:37](https://www.youtube.com/watch?v=8X9EalObKw0&t=337s)** was MCP was function calling tools. Like it's just for most people yet another way to get more tools to the model. And then that comes with the inevitable problem of we've seen an explosion of MCPs. I don't have statistics at hand, but I'm I'm confident there are thousands upon thousands of them. And then if you want to expose some reasonably large amount of these to a single model, a single turn, you'll quickly run out of context. You'll spend more time explaining schema than explaining the problem that you have. So, we see two sort of patterns evolving that are very common for this. There's shell file system-like invocation. Um I personally am very Plan 9 pilled, if you will. And this is where everything's a file system, resources are just files, tools are in some way executable. The other pattern is very similar, but

**[6:27](https://www.youtube.com/watch?v=8X9EalObKw0&t=387s)** it's code-like, where your tools become functions. Typically these days in TypeScript or Python, but strictly speaking in any language. Both of these things to me are just another layer up. They're exploration of code mode. Like shells are just we don't usually think of it as a programming language, but Bash is one. It's surprisingly capable. If you've ever investigated it, I don't recommend it. Um but it's amazing what you can do in Bash. Like asynchronous programming exists in Bash. Now, how do we handle this layer? It's just another layer in this stack of things. Like we went from electrical to Open APIs. We've added more expressiveness, more specification. We're now subject to say typing in a language or the

**[7:15](https://www.youtube.com/watch?v=8X9EalObKw0&t=435s)** expectations of a file system. And we're doing this because of this higher layer, we can be much more efficient in token efficiency. By giving the model code, it can give us concise code that can filter output, reduce it down, just optimize how much context we're doing. And then also by combining commands together, sometimes the model knows that we need to do A then B then C. It doesn't necessarily need to hold our hands for this. It can write a program that expresses the same action. And then related to this, and I'm sort of working into the like obvious question that's in a lot of people's minds of CLIs versus MCPs. Unless you're doing something compute-bound, like your chances are your model needs to interact with the outside world. It

**[8:02](https://www.youtube.com/watch?v=8X9EalObKw0&t=482s)** needs to use resources it finds there, tools it finds there. Perhaps it takes input prompts from elsewhere. Really it needs a context for the model, i.e. MCP. MCP, however, is a specialization like MCPs ultimately over HTTP or standard IO. Like it's another layer in this stack. There's code mode potentially above it, uh raw communication primitives below it. And those raw primitives always work. Like we could just use bytes. The model actually is probably quite capable of generating abstract binary output. Um it would be an interesting experience. So, we don't do that. We use libraries such as HTTP, we layer on top of it as I mentioned like REST or Open API, and

**[8:49](https://www.youtube.com/watch?v=8X9EalObKw0&t=529s)** then we layer on top of that MCP. So, we have these bidirectional primitives, a simpler landscape of tools, and also it brings us like pulls us forward to the latest standard. Like the biggest thing for me about MCP has been true for the full past year, which is the intent that it brings people to focus on. Like MCP is more than just an API. Computers have had APIs forever. MCP is an API for AI. So, when you're starting an MCP project, you're thinking about how will the model use these tools? And also you're thinking about how do I make sure it's secure? What is the best practices here? How do I make sure it's observable? How do I do like the right thing, as it were?

**[9:37](https://www.youtube.com/watch?v=8X9EalObKw0&t=577s)** And MCP describes that foundation. Like there are millions of authentication protocols online. MCP says let's use OAuth 2.1. There are lots of ways to express functions, like transformations of input to output. MCP has a standard schema, it specifies they're JSON-encodable. It also like does this very subtle thing that it tells you you're building this for an AI model. You're not building it necessarily for another developer. You're building it for this thing that has vaguely known properties. It's continuing to get better and that's what you should target. So the example to me is always for gateways that transform open API specs. Like if you consider an email system, like it has when when you think of it and draw it on a whiteboard or something, it'll

**[10:24](https://www.youtube.com/watch?v=8X9EalObKw0&t=624s)** be send email, receive email, maybe list emails. Like it's very easy to come up with a few verbs. But then when you actually think in depth about it, you get huge amounts of functionality. You add drafts, you add labeling, you add folders, you add categorization, you have contact management. Your simple API is actually potentially by itself hundreds of tools. And that's great. Like it's very functional, but it can be confusing for a model and so in building an MCP server, you think what does the user want? The user wants to create a draft or send an email. So you build a very high-level API that makes it simpler for the person and that's the intent you bring to API design. Now this

**[11:11](https://www.youtube.com/watch?v=8X9EalObKw0&t=671s)** Oh, did I Ooh, I sort of missed a slide, sorry. Um but so uh with this API design, this is then my answer to a lot of the thoughts on CLIs versus MCPs. Which is if you have nothing then you can build anything to make it available to the model. Like you can build a CLI, you can build an MCP. If you have an existing API, you could just transform it, pick it up and ship it to a model. I would advise not that. I would advise writing a CLI around it or writing an MCP around it to bring that intent to what you're doing. As for whether or not one is better than the other I actually sort of feel it's not a decision between one or the other. It's actually clearly want both. There's a big history of CLIs that exist like on

**[12:01](https://www.youtube.com/watch?v=8X9EalObKw0&t=721s)** the proverbial shelf out there. And there's MCP servers that are people bringing AI intent and the most powerful systems will really combine both of them. Um now towards the end, I wanted to touch upon this looking forward. So last year I spoke a lot about like crazy transformative things and we've seen some of them and a lot of them didn't work. But what else is there? And MCP for agents. So the agent word comes up a lot. Um it's possibly the most ill-defined term in computer science. MCPs it's M and C on P. So it's tool protocols, it's context protocols, but at a high level, it really is sort of like an agent-to-agent protocol. Like tools are sort of abilities, tasks now are

**[12:49](https://www.youtube.com/watch?v=8X9EalObKw0&t=769s)** delegated work. Messages, inputs and outputs are structured and explicit, but no one really treats it like this yet. So I'm quite excited to see like MCP is the basis for agentic communication because this is the next level of intent, which is you need a simple detailed API to express the intent to an email server. But if the other end is also an AI capable company or product or service it's as good as the client at interpreting intent and so you should really open it up and let it be a truly agentic communication. Um and then the last sort of thing is actually not so much a thought, but more of a call for input. So like participate on MCP discords, like look me up on LinkedIn or whatever and just directly message me because the biggest problem

**[13:37](https://www.youtube.com/watch?v=8X9EalObKw0&t=817s)** that I think we've shortly going to run into is this discovery of identity. Which is we've all built these layers, we've all built complex compositions of these things. It's extremely difficult to discover what is best. Like MCP has been so wonderful in creating this beautiful landscape of options, of clients and experiences, but there's so many of them that itself is a difficult thing to digest across many providers, many clients, many hosts. And so we need to try to work together to discover what is a robust form of identity that we can use everywhere and that makes things discoverable and easy to find. Um and that's it. Thanks everyone. >> [applause]
