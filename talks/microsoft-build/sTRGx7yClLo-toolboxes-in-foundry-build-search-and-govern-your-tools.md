---
id: sTRGx7yClLo
title: "Toolboxes in Foundry: Build, Search and Govern Your Tools | LIVE163"
slug: toolboxes-in-foundry-build-search-and-govern-your-tools
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: ["Atul Aggarwal", "Seth Juarez", "Zhuoqun Li"]
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-05T15:22:46Z
video_id: sTRGx7yClLo
url: https://www.youtube.com/watch?v=sTRGx7yClLo
youtube_url: https://www.youtube.com/watch?v=sTRGx7yClLo
tags: ["Atul Aggarwal", "LIVE163", "LIVE163_v1", "Seth Juarez", "Toolboxes in Foundry: Build Search and Govern Your Tools | LIVE163", "Zhuoqun Li", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration"]
transcript: true
---

# Toolboxes in Foundry: Build, Search and Govern Your Tools | LIVE163

**Atul Aggarwal, Seth Juarez, Zhuoqun Li**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#Atul Aggarwal` `#LIVE163` `#LIVE163_v1` `#Seth Juarez` `#Toolboxes in Foundry: Build Search and Govern Your Tools | LIVE163` `#Zhuoqun Li` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=sTRGx7yClLo) · [Conference site](https://build.microsoft.com/)

## Description

Today, each agent often wires tools directly, with its own authentication, credentials, and integration code. Toolboxes in Foundry are a new way to build, search and govern all tool types across all of your AI agents without rewiring them every time, powered by runtime tool search, unified endpoint and guardrail integration.

To learn more, please check out these resources:
* https://aka.ms/Foundry/Toolbox/Docs
* https://aka.ms/toolbox-build-blog
* https://aka.ms/Foundry/AgentService

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Atul Aggarwal
* Seth Juarez
* Zhuoqun Li

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE163 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Introduction and Welcome with Seth, Linda, and Atul
00:00:05 - Seth's Confession and Initial Skepticism on Foundry Toolbox
00:00:19 - Discovery of Toolbox's Utility in Keynote Features
00:00:41 - Introductions: Linda (Product Manager) and Atul (Engineering Manager)
00:00:54 - Defining the Problems Toolbox Solves: Authentication, Multiplicity, Governance
00:02:43 - Simplified Developer Workflow Using Toolbox and MCP Endpoint
00:04:54 - Tool Search Capability and Auto-Ping Mechanism Explained
00:07:07 - Accessing Individual Tools and Handling Authentication with Work IQ
00:08:40 - Live Demo: Creating and Managing Multiple Toolboxes and Skills
00:13:17 - Toolbox Availability, Governance Controls, and Upcoming General Release

## Transcript

*2,619 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=sTRGx7yClLo&t=0s)** Hello, my friends. Welcome back to the build stage. I'm so excited to be here with my friend Linda and Atoll. Now I have a confession to make. So Linda and I worked on the same team for a little bit and about about, I don't know, it was a month ago. Yeah, about look, she's, she's remembering. She was like, she was like, hey, there's this new Foundry toolbox thing. And I was like, hold on, I don't know if it's going to work. And she's like. You are raw. She's like, you are wrong Seth. And guess what, friends? You you actually were raw. It's actually true because we used in the keynote, we used some of the features in Toolbox and it really helped us out. So before we get started, why don't you introduce yourself? We'll start with you, Linda, and then Atul. Yeah. Hi. I'm Linda. I'm a product manager in Microsoft Foundry. Fantastic.

**[0:47](https://www.youtube.com/watch?v=sTRGx7yClLo&t=47s)** I'm Atul. I'm a partner engineering manager at Microsoft. So I I'm a huge fan of founder, you know, I worked there for a long time. Why don't you set up the problem that toolbox is supposed to solve? Yeah, I would say toolbox is really solving the problem. When tool starts to scale up with agent adoption scales up. Think about like 5 agent that you're building. You want to connect to 5/10/20, a hundred different tools. Some of the tools are using open API, some of them are MCPA 2A skills building tools. And those tools have different authentication, authorization, different protocols. So our developers need to write custom code to handle the wearing of different authentication and protocols. So that's the first problem. The second problem is think about when I have like 5/10/20 tools and when I try to use my agent

**[1:38](https://www.youtube.com/watch?v=sTRGx7yClLo&t=98s)** for a specific task. Not all of the tools are actually needed, but the tool definition got exposed in front of the foundry the model so easily, so the token usage context window got blown up really easily and quickly. So it's basically a combination of authentication, multiplicity of tools so far, but I feel like there's another another more things. Yeah, the last was actually the governance where I want to make sure that all of my tools have some real policy applied to it. And right now developer need to write custom code, integrate with different policies 1 by 1 based on which tool they're calling, which agent framework they're using. It's a lot of custom work, not really easy to scale up. It's hard to reuse whatever they have written. So authentication, multiplicity of tools and governance.

**[2:28](https://www.youtube.com/watch?v=sTRGx7yClLo&t=148s)** And this actually really bit us when we were starting because I just thought, oh, let me just map the tools myself. Why would I not do that until Why don't you give people a sense for like the kind of code that people need to write and how this makes life toolbox, makes life better for devs? Absolutely. It's really easy to get started. The first step developers typically do is they curate all the tools they need for their agents to do the task. Imagine you have 20 to 30 tools at your disposal and all the tools have different protocols that they need MCPA to a open API. They may have different authentication needs for their enterprise. So once you have curated the tools, you simply create a toolbox and attach all the tools into the toolbox. What Toolbox gives you as a response is basically an MCP compatible version endpoint which you can attach to your

**[3:20](https://www.youtube.com/watch?v=sTRGx7yClLo&t=200s)** agent and then agent just interacts with toolbox to invoke the right tools on demand. When as Linda talked about the context board build problem, Toolbox enables you like you just simply add a tool search tool. And then once you have tool search tool enabled in toolbox, then Toolbox internally takes care of routing and selecting the right tool for your agent task at hand without exposing all the context of the tools and their description to the agent. And that saves, you know, multi fold context bloat, token usage and cost, right? And finally, if for governance, you simply create a guardrail in Foundry, attach the guardrail in the toolbox and then you simply toolbox starts working for all the pre tool

**[4:11](https://www.youtube.com/watch?v=sTRGx7yClLo&t=251s)** post tool invocations. The guardrails are applied out-of-the-box. It's really that simple. All you do is click a few steps, create a toolbox, invoke the toolbox, and that's it. It works across all the frameworks, it works across different compute infrastructures and that's it. So one of the things that I was telling you, the reason why I was I stressed about it originally is because if you put too much in a tool, in an MCP tool for example, it could potentially pollute your procedural memory. Yeah, context space. But you, you had already solved that in your mind. You talked a little bit about it. Why don't you expand on that a little bit on how this fixes that? Yeah. So basically that's the tool search capability. Yeah. So with tool search, we only find and receive the most relevant tools based on users query.

**[5:01](https://www.youtube.com/watch?v=sTRGx7yClLo&t=301s)** Based on each times the user prompt, it will find the most relevant tools to the for a specific user prompt. But we understand some of the tools you want to expose to the model all the time. So we have also that ping capability where you can ping a specific tool so it's always exposed to the model. And also toolbox can be smarter gradually based on the behavior and the conversation has been happening with the toolbox. We will learn from your conversation and auto ping some of the tools in the toolbox. The customer doesn't need to do anything their most frequently used tools called auto ping. And so that's the cool part, right? Because I worried about having to actually set up all the tools correctly, but it you don't have to be with tool search. But let's talk about the process. Is it?

**[5:47](https://www.youtube.com/watch?v=sTRGx7yClLo&t=347s)** Effectively you're only exposing tool search as a single tool, so the LLM calls it, then it puts that tool called back on the thread. Tell us how this works. Yeah. So when you enable tool search, when you call the MCP endpoint as the list tools prior, they only see two meta tools, tool search and call tools. So the model will be prompted to call the tool search and find the most relevant tools and then you use models judgment to call which tool they think is most relevant. So this is even smarter than I thought. So there is a there. There's only two tools that you're exposing. Find it, call it. Yeah yeah. Is there a way for, and I don't know if there's a way that maybe there is a better answer for this and I don't know it, but let's just say I have like a customer ID and I just want to do a tool binding. Is there a way to pass through tool bindings that way in Toolbox?

**[6:35](https://www.youtube.com/watch?v=sTRGx7yClLo&t=395s)** Like if I don't want to put a customer ID in there every time, is there a way for me to just put that into the tool somehow? How, how does that work? How do I fill tool parameters out myself? So you as you configure the tools it really needs. Let's say you're configuring an MCP endpoint. You just define the parameters. You just defined what's the MCP endpoint to invoke and what are the authentication modes and credentials. That's it. Once you have created that tool, just attach it to the toolbox and there you go. That that is amazing. But then the other thing you can do and, and we found this out is from a toolbox. I'm able to access individual tools as well. Is that right? Tell us about that. So you can access individual tools, it's you can select from Enraged tool catalog we have and actually I feel we're releasing a few more tools like work IQ Fabric, IQ browser automation, etcetera.

**[7:23](https://www.youtube.com/watch?v=sTRGx7yClLo&t=443s)** So customer can select whatever tools they want and bring their custom tools if they. Want and, and the part that I that to me is, is really cool that I, I cannot stress enough is actually super hard to do is the authentication, especially with things like work IQ, right? Tell us about that. So work IQ has a lot of tools you can have Teams, Outlook, there's a biz dev chat and it exposes multiple tools behind MCP endpoints and A to a endpoint. So if you're really looking for an all up A to a agent interaction, you just configure the work IQ biz dev chat and it can interact with all the work IQ tools under the single load. So all you do is attach one work IQ tool behind the toolbox and it starts working. You have again you configure the right authentication credentials to work IQ on how you want to interact it.

**[8:12](https://www.youtube.com/watch?v=sTRGx7yClLo&t=492s)** You want it as an MCP endpoint, configure it as an MCP SO tool and that's it. Attach it to toolbox, it starts working. And that's the part where I, I kind of didn't see have the foresight that you all did was the authentication and the governance. Because those two pieces are actually harder than just, hey, let's just attach a Jason schema to the actual LLM call. You have to do much more, much more than that. All right, So I want to see it in action. Do you have something you can show us? Yeah, let's do it. So what I have here is a Phoebe toolbox that has a few operations and you can see in my toolbox I have attached three tools and a custom MCP server was that looks up my inventory. Control. Plus a couple of times my old eyeballs are like, there you go.

**[8:59](https://www.youtube.com/watch?v=sTRGx7yClLo&t=539s)** Oh whoa whoa whoa whoa. Not that old. Holy cow, Linda, you already proved me wrong once in front of everybody. You don't need to make me old, too. All right, here we go. How about this? There we go. It's perfect. Cool. So we got the custom MCP which has more than 210 tools behind that which can look up my orders, look at my inventories, I have open API tool and also a knowledge base integrated with that looks up my. Hold on. So because I I, I got this got lost when I was zooming it. This is a special toolbox area. Yeah, I see. And so you can actually create multiple tool boxes for multiple reasons with any combination of tools, of course. OK, So that's what I think that's the part that was lost on me as well. Sorry. So keep going. Keep going. Yeah. So this is the tool I have, but also I'm also adding a bunch of skills.

**[9:48](https://www.youtube.com/watch?v=sTRGx7yClLo&t=588s)** That's what we heard from customers. And that's the other part that we could tell us about the skills that are in here. Yeah. So the skills here is really for just help my agent to know how to use the tools. Tools is really telling what to do and skills is how to do it. I see 2 problems we have been hearing from customers. One is they want a private skills catalog where they can manage and source version. And the second one is they want the auto discovery and auto loading of skills and they want to be able to update their skill, iterate over their skill without redefining their code. So that's how Toolbox MCP endpoint is powering with it. And see, that was the extra thing, and I totally messed because it's not just that you attach tools. Yeah, because it's the description of the tools and the

**[10:37](https://www.youtube.com/watch?v=sTRGx7yClLo&t=637s)** parameter descriptions that really influence the procedural part of the LM call. Correct. But you're saying you're augmenting that additionally with skills. Yes. OK OK. So how does someone attach a toolbox to their? That's super easy. OK, let's see. So here I have my endpoint. I can simply copy this as an MCP endpoint. I have my agent code written here. This is sorry Control Plus a couple times. Yes. Nice. Perfect. So this is an agent that I wrote with Microsoft Agent Framework. You can use any agent framework as a tool set and I just integrate with my toolbox MCP endpoint. That's it. I don't need to write another 1000 thousand lines to integrate with different tools I have. And this is the part Atoll that I want you to speak to a little bit because effectively what you're

**[11:26](https://www.youtube.com/watch?v=sTRGx7yClLo&t=686s)** doing is your multiplexing a specific collection of tools for a specific job that multiple agents can use with the write authentication and you attach it to the LM as a single thing. Is that is that about right? Tell us about that. That's about right. So all you do is now if your agent earlier had exposure to 50 tools, their descriptions, there are their parameters. Now all of that code is switched to one MCP endpoint. That's like a tool. That's the tool that gets attached to agent. Agent invokes the toolbox and toolbox knows what is the right tool to call it. No context bloat, no token consumption, high consumption. You just give the intent to the toolbox and toolbox MCP endpoint will find and give you the right endpoint. Especially if you've enabled search.

**[12:15](https://www.youtube.com/watch?v=sTRGx7yClLo&t=735s)** With search, yes. Because there's just two tools going into the procedural memory exactly and behind the scenes are how are we, how are we using? Is there like an LLM call behind the scenes for toolbox? We really use algorithms like BM25 to search that space of tools. So let's say you have 5200 tools in your toolbox. Then we have the CPU bound algorithms. Today BM25 is the popular one. We will have more LLM powered search capabilities coming up soon in the toolbox. So once you give the right intent, Toolbox takes care of finding the tool and giving you the right output and no context bloat. Again, this is almost friends like Rag but for tools. Yes yes. And I'm having this realization now like after she's like, hey, you're on set totally wrong.

**[13:05](https://www.youtube.com/watch?v=sTRGx7yClLo&t=785s)** Because it makes sense that if we would do Rag for information, doing a RAG kind of approach for procedural or process things that we want to call makes perfect sense. So we have about 48 seconds left. What should devs know about this? Can they use it today? Tell us about that. Yeah totally. We're in public preview now. All the feature that I have talked about the unified MCP employing to search capability, bring your own guard reel and we also have a lot of things coming soon that. So we are going general availability for Toolbox this month. We have a lot of governance controls coming up. Customers will be able to view the dashboards with, you know what is the tool getting involved, how much token it is consuming, what's the ROI control apply all the policies, all the network traffic going out with MCP tools, making sure data exfiltration, prompt injection risks are minimized. So a lot of governance controls you'll see lighting up

**[13:56](https://www.youtube.com/watch?v=sTRGx7yClLo&t=836s)** in Toolbox soon. Well, I'm a huge fan, Linda. Thanks for proving me wrong and making an awesome feature for folks to use. Thank you so much and we'll see you after this.
