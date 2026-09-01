---
id: aC6xuKBVHD4
title: "The MCP Gateway Pattern Big Enterprises Are Quietly Adopting"
slug: the-mcp-gateway-pattern-big-enterprises-are-quietly-adopting
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 10
published_at: 2026-05-22T14:00:06Z
video_id: aC6xuKBVHD4
youtube_url: https://www.youtube.com/watch?v=aC6xuKBVHD4
tags: []
transcript: true
---

# The MCP Gateway Pattern Big Enterprises Are Quietly Adopting

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=aC6xuKBVHD4) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Jake Wilson, Partner in PwC's Analytics Practice and GenAI Transformation Leader, brings MCP out of the lab and into a working enterprise blueprint. In this keynote from the Agentic AI Foundation, he walks through a real client implementation where a single ChatGPT app replaces the painful experience of navigating ERPs and procurement systems for buyers across research, robotics, and operations.

Most enterprise AI experiences break down at the system boundary: users know what they need, but not which application, process, or data is required to complete it. Jake shows a different pattern - a single conversational interface, powered by MCP, that hides backend complexity while orchestrating work across multiple ERP and procurement systems.

What's covered:

- The Buyer Problem: why research, robotics, and operations buyers never want to learn the ERP, and what that costs the business
- ChatGPT App plus MCP Orchestrator: how the front-end app delegates to an orchestrator that classifies intent before touching any backend
- Direct vs Indirect Procurement Routing: GPUs and robotic arms go one way, ergonomic chairs go another, and the agent figures it out
- Anthropic's Agent Skills Standard: how skills (name plus description in markdown) become a new tool-calling primitive layered on top of MCP
- MCP Calling Agents Calling MCP: the orchestration pattern that lets one MCP endpoint route across many backends
- UI Resources and React Widgets: how the MCP orchestrator tells the GPT app which view to load with the data it got back
- MCP Gateways for Security: enforcing policy when one backend supports OAuth and the other only takes an API key
- Fine-Grained Tool Authorization: restricting which MCP tools can be invoked in which scenarios, especially in regulated environments like utility and energy

This talk is for enterprise architects, platform engineers, and AI leaders building MCP-based systems that need to connect to real ERPs, real OAuth flows, and real legacy infrastructure - not just demos.

Links and Resources:

- Jake Wilson on LinkedIn: https://www.linkedin.com/in/jacobwilsonpwc
- PwC GenAI Practice: https://www.pwc.com/us/en/tech-effect/ai-analytics.html
- Anthropic Agent Skills documentation: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Model Context Protocol spec: https://modelcontextprotocol.io
- Agentic AI Foundation: https://agenticaifoundation.org

Timestamps (approximate, please adjust):

00:00 Jake Wilson intro and PwC analytics practice
01:22 Why enterprise procurement is broken for technical buyers
02:43 The architecture: GPT app, MCP orchestrator, backend ERPs
03:51 Detailed walkthrough: react widgets and intent classification
04:46 Direct vs indirect procurement and downstream routing
05:13 The direct procurement agent and supplier validation
06:03 UI resources: how the orchestrator tells the front-end what to render
06:54 OAuth vs API key: when backends disagree on security
07:18 MCP gateways and fine-grained tool authorization
08:15 The orchestration pattern: MCP invoking agents invoking MCPs
08:54 Anthropic's Agent Skills standard as a tool-calling primitive
09:27 Closing thoughts on enterprise MCP transformation

## Transcript

*1,892 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=0s)** All right, how we doing? Good. All right, um So, I I think a lot of different talks this morning, we talked a lot about uh the technical capabilities, the art of the possible, how all this stuff is coming together. So, uh wanted to bring this to life a little bit more for you all and how this is working with uh you know, true enterprises today. Uh so, quick introduction. So, Jake Wilson, I'm a partner in our analytics practice at uh PwC. Uh I have the privilege of consulting, you know, some AI companies who are leading uh the latest and greatest, you know, frontier state-of-the-art models, as well as working with utility energy companies who are building and fueling uh the next generation AI data centers, uh and working with other clients across kind of industry and function. Uh so, I came from a kind of traditional software

**[0:47](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=47s)** engineering background, uh fell into the world of AI about 9 years ago. Um at that point in time, we were doing some things in emerging tech uh PwC, uh and then I was like, "Hey, you know, being a software engineer is great, but in order to really lead teams in AI, got to understand the details." Uh went back, got my master's in data science at UC Berkeley, uh which is oddly enough, right when I completed that was the launch of ChatGPT. Uh so, it was like perfect timing. Um so, been living in the world of generative AI for the past 3 years. Uh it has been the most exhausting thing I've ever done. Um So, what we're going to talk to you about today uh is how many of you all kind of um think that your procurement function could be a little bit more efficient and optimal uh within your organizations?

**[1:35](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=95s)** Okay, see a number of hands going up. Uh so, what we're going to talk about is how MCPs comes together with skills orchestration and integrating with enterprise applications. Um So, as part of this, uh you know, the context and the background is uh this particular client and clients we see kind of across the board, especially as we're getting into manufacturing, uh who might be building the latest, you know, robotics and other type of capabilities, is you know, if you look at these organizations, whether they're newer startups or legacy kind of enterprises the challenge you're dealing with is I've got a lot of different buyers, right? These buyers could be people sitting in the research division who are, you know, working on the latest AI models. They could be sitting in a robotics lab, you know, building out the

**[2:23](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=143s)** next state-of-the-art robotics. So, the problem is like none of these people want to go into these complex systems like your traditional ERPs and procurement systems to figure out how to actually go procure GPUs to go buy materials for, you know, robotics and to do all these things. So, in this particular example, what we've created is a GPT app. That GPT app works with a MCP orchestrator. That MCP orchestrator is using the latest latest agent skills kind of format, which was published by Anthropic and you see a number of people kind of converging around today to help determine, you know, when when a buyer comes in to make a request, you know, is this related to direct procurement versus indirect. So, direct

**[3:12](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=192s)** being more of like the robotics arms, the GPUs, indirect being like, "Hey, I need to get the CEO an ergonomic chair," right? So, regardless of who's coming in, we just need a simplified experience and then we do all the complex orchestration on the back end using, you know, techniques with MCP and agents to kind of do all that together. So, that's kind of the backdrop in terms of, you know, GPT app communicating with MCP orchestrator and that is then working with the back end systems for the ERP and indirect procurement system. So, here's kind of a little bit more of a detailed the view of what this looks like. So, what you'll see on the left there is the MCP app and then kind of that widgets box. I think that widgets box is a standalone react application. So the way this works is if I'm a buyer

**[4:02](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=242s)** I come in and say, "Hey, I want to buy, you know, 10 robotic arms or 1,000 GPUs." Um essentially what will happen is that GPT app will do an MCP tool call to the MCP orchestrator. That MCP orchestrator has skills built into it to where it then understands the user's intent and basically kind of trying to classify the request as direct or indirect procurement. Because if it's direct procurement it goes back to one system, if it's indirect it goes back to another system and that whole experience looks different on the back end and the types of things you need to provide on supplier, purchase amounts, purchase prices, and all these things to actually satisfy the purchase requisition. So that MCP orchestrator is doing that kind of initial classification and figuring out

**[4:52](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=292s)** what it is that the user's trying to do and then based upon whether it's direct or indirect, it will then say, "Hey, do I have enough information I need to then make the downstream call to like the direct MCP server or the indirect MCP MCP server to then actually raise the purchase requisition for the robotics arms, the GPUs, or what have you." Um So is is part of this So let's say in this case of the direct flow, right? So we get the classification through the MCP orchestrator. That is again then going to trigger the direct procurement agent. That direct procurement agent will make the MCP tool call back to that system. We'll get the necessary information to help, for example, validate the the supplier that they're requesting is the correct supplier

**[5:39](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=339s)** and also can do some more advanced things over time in terms of just you know, is there a more optimal supplier based upon what you're trying to do or you know, the timelines you're trying to get all these materials satisfied by. Um so that kind of comes back through what what then happens through the MCP orchestrator. So I get my data back. Uh let's say I go ahead and raise the purchase purchase requisition goes back to that system. That information comes back. Um But now what I need to do is say, "Okay, yes. Uh here's the data. Here's the confirmation from raising the purchase requisition that back-end system. I now need to tell the uh GPT app essentially what UI resource to now load in uh with the data I got back from that back-end system along with the response from the direct procurement agent. Uh so in that case, that's where the MCP orchestrator again kind of helps

**[6:28](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=388s)** in terms of saying "Okay, here's the information I got back. Uh now here's the UI resource uh that kind of goes along with that. Uh so that now the GPT app can point to the correct view uh within the um uh React application and then start to load in the structured content uh that we got back from the MCP orchestrator, which was a result of triggering the direct procurement agent." Um so I think all that's interesting too cuz uh in the in the end too, like if you look at the the back-end systems, like in this particular example, uh one of one of the back-end procurement system supports uh OAuth and direct flow of the user identity. Uh the other system does not. Uh and unfortunately, the only way you can interact with that system is through an API key. Uh so not the most secure. So I I think you heard in the previous

**[7:17](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=437s)** talk too, this is where like MCP gateways are kind of helpful uh in the sense of yes, I can secure and put our back in front of that GPT app up front. Um but ultimately, like if I want more protection, you know, as it relates to how like who can actually invoke these MCP servers uh on the back-end through the GPT app and have a little bit more fine-grain control, that's where those gateways come in place uh where you can define additional policies uh to also restrict like in certain scenarios like uh you know, for our utility energy clients uh where we're doing transformation of kind of their uh operations of their data centers. Um there's very specific tools within the MCP server that you only want to invoke in certain scenarios. Uh so, that's where the MCP gateway can kind of help

**[8:05](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=485s)** add another level of uh kind of granularity in terms of like security uh for how you invoke even the different tools or functions within the MCP servers. Um so, it's kind of interesting to see all this come together uh just in the sense of uh not only can I use MCP to integrate with back-end applications, but in this example too, you kind of see another pattern uh where you get things like uh you know, chat GPT where uh the only thing you can expose to it is an MCP. Um but, I don't and in those cases you can have one MCP um and you you need a little bit more control over how things get routed on the back end. So, it's kind of a pattern of using an MCP to help orchestrate uh invoke agents which then also invoke other MCP servers. Uh so, I find this one interesting just in

**[8:53](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=533s)** terms of the pattern um and then also kind of using the latest uh agent skill standard that you see Anthropic and everyone converging on which is, you know, all the skills in markdown files. Um what's funny about that too is it's just like another pattern of like tool calling uh in the sense of uh I'm going to expose an array of a list of in this case skills with the name and description versus tools name and description. Um but, in this case, you know, we we've got the MCP orchestrator helping enumerate through that, invoking the right skills which in turn invokes agents, which then invokes skills, which invoke MCPs. Um So, hopefully that was helpful. Just kind of gives you a context of a real-world example uh as you think about you know, how to use MCP uh in terms of enterprise transformation where again this is really simplifying in this case the experience for all the buyers

**[9:43](https://www.youtube.com/watch?v=aC6xuKBVHD4&t=583s)** across the research research divisions robotics divisions etc. Just to where they can come into a very simple app make a request MCP does the orchestrator does all the complex routing and all the back end integration so that you know those people working on these complex systems and and robots don't have to go into these legacy applications to try and figure out how they work. So that's it. So we're out of time appreciate that and yeah if you have any questions down here up front but thank you for your time. >> [applause]
