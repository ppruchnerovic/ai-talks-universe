---
id: jxKihBelsH0
title: "Teach AI agents to manage context with Elastic Agent Builder | DEMSP395"
slug: teach-ai-agents-to-manage-context-with-elastic-agent
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 17
published_at: 2026-06-04T13:45:09Z
video_id: jxKihBelsH0
youtube_url: https://www.youtube.com/watch?v=jxKihBelsH0
tags: ["74755fa7-4099-43f3-98b4-01cb5032629e_M9Z7-DEMSP395-1", "AI", "Agents", "DEMSP395", "Deepti Dheer", "Developer", "Mike Richter", "Teach AI agents to manage context with Elastic Agent Builder | DEMSP395", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Teach AI agents to manage context with Elastic Agent Builder | DEMSP395

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#74755fa7-4099-43f3-98b4-01cb5032629e_M9Z7-DEMSP395-1` `#AI` `#Agents` `#DEMSP395` `#Deepti Dheer` `#Developer` `#Mike Richter` `#Teach AI agents to manage context with Elastic Agent Builder | DEMSP395` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=jxKihBelsH0) · [Conference site](https://build.microsoft.com/)

## Description

Solve AI context limits by enabling agents to manage their own memory. Learn how to prevent bloated prompts and context drift during long tasks, reduce input token usage while ensuring enterprise data governance and scalability. Walk away with next steps for deploying the dynamically loaded skills, conversation context store, selective compaction, and secure external data connectors from Elasticsearch 9.4's Agent Builder  in the Microsoft ecosystem.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Mike Richter
* Deepti Dheer

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEMSP395 | English (US) | Developer tools & frameworks

Demo | (300) Advanced

#MSBuild

Chapters:
0:00 - Mike Richter introduces himself as Microsoft Partner Solution Architect
00:00:20 - Overview of discussion topic: Elastic running in Azure
00:03:00 - Elastic’s vector support for RAG and Agentic applications integrated with Microsoft Foundry models
00:05:11 - Elastic’s approach to bridging contextual gaps across disparate data sources
00:08:15 - Discussion on dispatching responses securely and improving data compute efficiency
00:08:35 - Introduction of real-time demo
00:10:48 - Explanation of skills as building blocks and creation of custom financial exposure skill
00:12:22 - Introduction to ESQL as a query language for tool creation
00:15:23 - Workflow demonstration for sending summaries to Slack channels

## Transcript

*2,621 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=jxKihBelsH0&t=0s)** All right. Welcome everyone. My name is Mike Richter. I'm a Principal Partner Solution Architect at Microsoft and we have. Yes Deepti. Hi everyone. I'm, I'm Deepti here. The product manager for Elastic primarily focused on agent Builder. Over to you. Cool. So today we're going to talk to you about Elastic running in Azure, and I'm just going to take a few minutes talking about the great partnership between Microsoft and Elastic. So my mission as a partner solution architect is to help our partners build and sell solutions on Azure. And I can't think of a better partner for that partnership than Elastic. So can you show me?

**[0:48](https://www.youtube.com/watch?v=jxKihBelsH0&t=48s)** Oops sorry. OK. So I just want to talk about the partnership and, and what it means for our mutual customers. So the important thing to understand is that it's very easy to buy Elastic on Azure, right? It's available in, I think about 15 different Azure regions right now and they're adding more of those regions. If you are a Microsoft customer and you have Azure commitment dollars, you have a Mac agreement. If you work for a big company, you probably have one. If you're not aware, you can use those dollars, those commitment dollars for Azure to purchase Elastic. And you could do that through Elastic's cloud offering or through the Microsoft Marketplace.

**[1:36](https://www.youtube.com/watch?v=jxKihBelsH0&t=96s)** So that gives you one single Azure bill. So it makes procurement of Elastic very simple for our enterprise customers. The Elastic Cloud offering, they have their hosted offering and their serverless offering now available on Azure. They are, like I said, 15 different regions all over the world and adding more. And so that means if you've got your Azure workloads running in East US or one of the supported regions, you can talk to Elastic. No egress costs, no latency, no additional latency going to another region. The integration with with Elastic is enterprise ready, right? So you can use your enter ID you sign into the Microsoft portal.

**[2:24](https://www.youtube.com/watch?v=jxKihBelsH0&t=144s)** You can use that same identity to go into the elastic portal to create your indexes to create your agents, do everything you need to do inside of Elastic. You can talk to Elastic their managed service over private links. So Elastic essentially is part of your V net in Azure. So for our customers who have those compliance requirements, they need to make sure that they talk to the data sources privately. All that works even though it's running in either Elastic's cloud or running through the marketplace. That is all happening for you. And then as we all know, Elastic has first class vector support right there. Solution is really built for those RAG and Agentic applications inside of Azure.

**[3:11](https://www.youtube.com/watch?v=jxKihBelsH0&t=191s)** You can of course reuse your Microsoft Foundry LLMS, right? So if you have that Mac agreement and you have Ptus and you're using our models, Anthropic, Open Eye, all that stuff through Foundry, those can power your agents inside of Elastic as well. And of course, the Elastic Agent builder, which DT is going to be talking about is available running in Azure. And I'll just wrap this little instruction to say that I've done a lot with Elastic. What DT is going to be showing you. I have built and built demo applications. So if you want to learn more, you can talk to her. You can come see me. I'm going to be actually staffing the apps and agents, the yellow booths right after this, right after this session. So if you want to talk about apps and agents,

**[4:02](https://www.youtube.com/watch?v=jxKihBelsH0&t=242s)** you want to talk about agent builder on Elastic, I'm happy to show you what I built and talk to you more about that. So I'll hand it now to DT. Thank you, Mike. And one more thing that if you want free credits or up to $1000 of credits of Elastic, please head to our booth right here. And you know, we we can help you with, you know, any other questions on Elastic. So just to, you know, summarize, yes, we are Microsoft, but what does Elastic really do? What are we doing in the world of AI, you know, with Agent Builder? So let me bring all of you back to the to the problem first, which is, you know, we have these desperate systems, which means we have data in those systems and these state in these systems are just sitting

**[4:51](https://www.youtube.com/watch?v=jxKihBelsH0&t=291s)** right there and in and having their siloed context. Now what happens is when it comes to whether its AI, whether its running your own business, leveraging AI, this context, the siloed context really breaks the whole theme of what's really needed to be done or what is needed to be executed from an AI perspective, right. So what we are trying to do in Elastic is bridge that context gap by not just bringing in, you know, data into Elastic, but also creating the data that sits outside elastic in these different systems and give them a good wrapper of context retrieval and give you a response that is not just high quality, but then it's also token optimized. Now how do we do that? So this this architecture, you know, in a nutshell, you

**[5:43](https://www.youtube.com/watch?v=jxKihBelsH0&t=343s)** know, shares our approach to solving the context gap, which is gather the if you look at the lowest tier, you gather your information or context from these different sources. That means whether your data isn't elastic or outside elastic in the different ecosystems of Microsoft, we build your own agents, your build your own capabilities around skills and, you know connectors. And that's what pulls in all the, you know, the context that is sitting in these systems. And then we dispatch them to those entry points or endpoints, which could be and your agent in Microsoft Foundry or agent on your MCP Copilot Studio, or for that matter, you know, any other, any other endpoint outside the ecosystem of Microsoft.

**[6:35](https://www.youtube.com/watch?v=jxKihBelsH0&t=395s)** So what are really those building blocks? When we say context engine, what does that context engine really curtail? So that so that comes to the building blocks that we have. So of course we have agents and skills that are really building your or, you know, building on top of your data connectors that are just just fetching the context from these different systems. And then we have plug insurance, which is, which can be your, your domain specific skills and connectors that we that really help gain us more, you know, domain level knowledge and attachments that that could be dashboard attachments or for that part, any file uploads that you have that are needed to add context to your agent. But what all brings together is our context engine. And what context engine is really doing is really mapping your data into or aligning each of the data that

**[7:27](https://www.youtube.com/watch?v=jxKihBelsH0&t=447s)** is sitting in silos and setting up right definitions at, you know, so that it does not have to churn and compute it again and again to understand what does that data even mean. So if I take an example personal, you know, phone number, e-mail, first name and last name, they technically can constitute your personal information, correct? Now Elastic understands or meta or meta sizes that as personal information metadata. And now tomorrow if you are retrieving Salesforce data that has customer data and the same fields first name, last name, e-mail, phone number, it understands that it is actually taking in the personal information. What ends up happening is now the behind the scenes, our agent then understands that hey, this is personal information, should I really dispatch as a part of the response.

**[8:18](https://www.youtube.com/watch?v=jxKihBelsH0&t=498s)** So which is where it is fairly secure. At the same time the compute or that understanding of the data is quickened. So we actually reduce the token usage from almost 2027 to 34%. Now we have heard you know all this, so let me show you how does that work in real time. So, so this this demo really shows that let's say you are a bank customer support team and who has some case data that is, you know, currently inelastic. But at the same time, your data like policy documents or engineering issues that are currently sitting in GitHub, which are your different systems are you know, don't don't know

**[9:08](https://www.youtube.com/watch?v=jxKihBelsH0&t=548s)** or don't communicate with each other. Now let me show you how Elastic Agent Builder does that for you. And it is done in a super easy, conversational manner. How so? For example, let me start with the simplest question. How many interactions happen by channel, phone, e-mail or chat? Oops. So the agent builder is computing the the response behind the scenes and we are very fairly transparent with what we are computing. So it shows you what what all tool tools were called or you know tomorrow, what skills or plug insurance were called. So that you have you as a developer have a holistic understanding of what is going on with your agent. That removes that black box tendency that some agents have and really gives you a transparent reasoning throughout the sessions when you're running these agents.

**[9:58](https://www.youtube.com/watch?v=jxKihBelsH0&t=598s)** What's more is its not just running giving you reasoning, it is also giving a very holistic response as well. So in this case it needn't just be a summarize summary of your an AI summary that is generated, but it can also generate a dashboard for you that you can actually save now. And this is agent like basic in a nutshell. Now what what we are powering our users is to actually customize this agent for you. So what you just saw was in bare minimum, what the agent can do and what all you know what was what all part that agent. But again, we understand every business and every business unit has a, you know, a specific need. So now I'll show you how you can even customize

**[10:46](https://www.youtube.com/watch?v=jxKihBelsH0&t=646s)** that agent. And one of the ways to customize is not just by giving custom instructions, but also skills. Now skills to those who don't know they are just the building blocks. They really help you in keeping your agent in a swim lane, which means that we you can give them a specific set of instructions format that they can follow. You can also associate the different tools that you need as a part of that skill. So elastic, we do provide, you know, a comprehensive set of skills that you can just go use, but at the same time, we understand again that it could be the needs could be domain specific, it could be industry specific. So which is why we also power power you by to, you know, create your own custom skill. Now, in this example, I'm creating a financial exposure report

**[11:38](https://www.youtube.com/watch?v=jxKihBelsH0&t=698s)** skill that is, you know, that is just generating a financial summary on demand and you know it, it is like I'm giving it holistic instructions. And I'm also, you know, adding tools to the skill. What's next? Tools. Tools are nothing but elves on the shelves. They are the actual soldiers on the on the ground, right? So again, here we have we are providing A comprehensive set of, you know, tools that you can just go to use. And again, they are, you know, they will be helping in some in the most of your agent executions. But we also understand you may need some specific tools that you need for your business for which you can actually create your own tool. And there are multiple ways to do it. One way is through the E SQL way, which is our query language.

**[12:26](https://www.youtube.com/watch?v=jxKihBelsH0&t=746s)** So you can create a tool using that query language. You can index, you can create a tool with your index workflows and even MCP. The next example is actually showing you how to an example of a tool that was created by an indexed data. So when I say indexed data, this data was inelastic and all I did was create a tool to look up that Financial Policy through by just indexing it. Now we are and so, so right now what whatever you're seeing is in the realms of elastic, the data is inelastic and everything is inelastic. But what about when we have connectors, so like SharePoint, like SharePoint Server, Slack. So this is where we get into the broader context,

**[13:16](https://www.youtube.com/watch?v=jxKihBelsH0&t=796s)** breaking that context silo. So this connector, so we have a good network of connectors that are that primarily do Federated search, you know, with different these systems and really retrieve the data that is most important to you. How? Oops. There's some, yeah. So how does that all come together? Let's see. So if I have this complex query, it is asking me is I'm asking the agent to create a dispute book for all the dispute related customer issues that have been raised in the in the past based on my data. It is actually doing what it is actually calling my

**[14:04](https://www.youtube.com/watch?v=jxKihBelsH0&t=844s)** custom skill that I just created. And at the same time it is giving me again a super comprehensive response that I can literally use, you know, and refer whenever I want. What's more is that to that response, I can also say, hey, can you retrieve a specific policy which is currently located in a SharePoint document or a SharePoint folder to and associate with that case with that specific case ID And it is able to do that. So here you can see the the relevant policy that is relevant to that specific case. And all of that is having in in the same same location, same conversation without having to go out of elastic.

**[14:51](https://www.youtube.com/watch?v=jxKihBelsH0&t=891s)** What else? What if I have engineering dependencies? So for that we also have a GitHub connector. All I'm doing is, hey, can you check if there are any GitHub dependencies or open engineering issues that really impacts the case resolution and which is what you know, the based on the skill that I designed based on, you know, the other tools that I designed, it is giving me a rank of OK, some of the issues that are directly impacting your case here. What's more is that I want to say I like the summary. I want to send it to my, you know, stakeholders over a Slack channel. Now this could also be teams we have, we already have that interview, but now specifically for Slack, I just created a workflow to say, hey, please send this summary to a specific Slack channel.

**[15:38](https://www.youtube.com/watch?v=jxKihBelsH0&t=938s)** Now what it's doing is actually taking my approval to make sure that I do want to take on the step. We understand that the right operations are fairly complex and sometimes they can also be risky. So we just want to make sure that you approve to the to such writing actions and the next and the result you have a comprehensive response of the comprehensive summary of that same thread in your Slack channel that is then shared across with your with your team. So this is like one of the ways, or I would say the simplistic way of how agent builder can really minimize the context gap and at the same time really deliver the value of the data that you know, that are currently sitting in silos, bringing it together and giving you a comprehensive prehensive, you know, responses that you can then use and make really quick business decisions.

**[16:28](https://www.youtube.com/watch?v=jxKihBelsH0&t=988s)** Thank you very much.
