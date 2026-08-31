---
id: erRPuV1EQ_c
title: "Develop and integrate AI agents with Google Workspace"
slug: develop-and-integrate-ai-agents-with-google-workspace
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Pierrick Voulet"]
channel: "Google Cloud Tech"
duration_min: 13
published_at: 2026-05-21T18:59:51Z
video_id: erRPuV1EQ_c
youtube_url: https://www.youtube.com/watch?v=erRPuV1EQ_c
tags: ["pr_pr: Google I/O;", "ct:Event - Technical Session;", "ct:Stack - Cloud;", "Enterprise agentic workflows", "Google Docs agent API", "Gmail Agent API", "Google Agent AI integration", "A2A Protocol", "Agent Development Kit (ADK)", "Google Workspace developer platform"]
transcript: true
---

# Develop and integrate AI agents with Google Workspace

**Pierrick Voulet**

`Google I/O` · `I/O 2026` · `2026` · `13 min`

`#pr_pr: Google I/O;` `#ct:Event - Technical Session;` `#ct:Stack - Cloud;` `#Enterprise agentic workflows` `#Google Docs agent API` `#Gmail Agent API` `#Google Agent AI integration` `#A2A Protocol` `#Agent Development Kit (ADK)` `#Google Workspace developer platform`

[Watch the recording](https://www.youtube.com/watch?v=erRPuV1EQ_c) · [Conference site](https://io.google/)

## Description

Extend your AI agent's capabilities into Google Docs, Google Chat, and Gmail. Explore the Google Workspace developer platform and discover how to build agents that act as a seamless bridge between your custom application and the Google Workspace ecosystem.

Resources:
Google AI → https://goo.gle/49RGf7r
Google Workspace → https://goo.gle/4wwH0fZ
Google Workspace MCP servers → https://goo.gle/3PsNBaG
Codelab - Gemini Enterprise Agent Platform → https://goo.gle/4wyTTGr
Codelab - Gemini Enterprise app → https://goo.gle/4wziBpY

Watch the cloud sessions from Google I/O 2026 → https://goo.gle/Cloud-at-IO2026

#GoogleIO

Event: Google I/O 2026
Speakers: Pierrick Voulet
Products Mentioned: AI/Machine Learning, Cloud

## Transcript

*1,719 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=0s)** [MUSIC PLAYING] PIERRICK VOULET: Hi there. My name is Pierrick. And today, we are going to explore how Google Workspace and Google AI fit together to enable agents for everyday workflow and automation. The AI race is not slowing down, and the landscape is continuously evolving. It feels like there are major launches of models, concepts, tools, products, protocols, and frameworks every week. And we are now past the chats most people are familiar with. These innovations make it increasingly simple to build, deploy, and publish production-ready agents, whether it's for individual or for organization use. Think about it.

**[0:48](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=48s)** What if you could have your own agent in a CLI, automatically update drive files with the latest documentation as you work on issues? What if you could have your own agent that processes incoming Gmail messages for urgent requests and automatically blocks time in calendar. What if your organization could provide an agent that monitors Google Docs and notifies people in Google Chat, depending on their roles. Well, Google Workspace and Google AI make that possible. Google's AI ecosystem is made of several layers that span from infrastructure to agents and applications. That makes it possible for anyone to integrate solutions of any shape from anywhere. You are a user?

**[1:35](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=95s)** Use pre-built agents. You are a builder? Build with agent designers. You are a developer? Develop agents with frameworks and tools. You are a service provider? Publish agents in the Google Cloud marketplace. You are an IT? Restrict user access to trusted agents and tools. I think you got the point. But you know what? At the end of the day, all AI solutions are still pieces of software. Do they execute differently and rely on different technologies than before? Definitely yes. But their potential still depends on three core pillars like any other software applications-- data, actions, and interfaces. Now, do you know a platform trusted by billions of users and millions of organizations

**[2:24](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=144s)** for collaboration, productivity, and getting things done on a daily basis? That's right, Google Workspace. It comes with Drive to find, share, and manage files; with Docs, Sheets, Slides, and Forms to collaborate and co-edit in real time; with Chat and Meet to connect from any device; with Gmail and Calendar to stay on top of things; and many others, such as Classroom, Sites, Keep, Task, and Vault. Many of these applications became increasingly AI-assisted in the past few years. My two personal favorite features are the AI overview thread summaries in Gmail, and Ask Gemini that's available from the sidebar. If you are part of an organization,

**[3:13](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=193s)** you might also have access to additional AI features with Gemini in Workspace. I personally rely extensively on Take Notes for Me in Meet. I can now focus 100% on the discussion and catch up later if I have a meeting conflict. And when it comes to AI-native applications, Workspace added NotebookLM last year and Workspace Studio earlier this year. NotebookLM is an AI research and thinking partner grounded in trusted information provided by users, such as financial reports, market analysis, or internal strategy documents. It can create resources in many formats, such as overviews, slides, or infographics. Workspace Studio, on the other hand,

**[4:02](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=242s)** makes it possible for users to streamline and manage tasks by building, managing, and sharing personal AI-enabled workflows made of starters and steps. Here, I create a workflow that automatically sends me a daily news summary in Google Chat. See how the flow can rely on AI-powered steps? The Ask Gemini step relies on a web search to retrieve the recent news in this case, but it could rely on other sources and take more complex decisions, as well. Also, this flow is mine, and it's editable, so I can control and adapt it as they see fit over time, like adding a new step. Now, what happens if the AI solutions provided

**[4:52](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=292s)** from Workspace are not enough? In this case, you can join the thousands of existing Workspace developers and start building your own custom solutions. You can use a no-code approach with AppSheet, a low-code approach with Apps Script, and a pro-code approach with any other tech stack. There are extensive APIs and libraries to retrieve data and take actions on behalf of users, such as accessing Gmail messages or creating calendar events. In this particular example, I have an Agent Development Kit function tool that creates calendar events for users. Most Workspace application UIs are extendable using add-ons. So it's possible to meet the users where they are. In this case, the user opens the sidebar in Gmail

**[5:43](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=343s)** to ask their travel concierge agent to plan their trip based on the information in the message that's currently open. Then, they can decide to move to chat if they have other ongoing discussions to take care of at the same time. Google is continuously releasing new model context protocol servers and tools for Cloud and Workspace that you can rely on, as well. They are dedicated to agents, and they are much easier and safer to use than building custom API wrappers. It's important to note that everything is client-agnostic. Using Google's AI tech stack is not a requirement to build custom solutions that rely on these features. But if you do, it comes with products and tools that make it easier to build agents that integrate with Cloud and Workspace.

**[6:32](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=392s)** Developers can combine Gemini CLI and Antigravity with Google-managed or custom app CPs to orchestrate workflows that bridge local development environments with real-time organizational data. Here, Antigravity is configured with Workspace MCP tools so that agents and skills can rely on them when needed. For example, an agent could send a chat message to a given space after completing their task. Agent developers can rely on Workspace MCP tools as well. The ADK framework makes it easy to do that by registering the tools, and by defining when and how to use them in instructions. The next layer of the stack is the Gemini Enterprise Agent platform.

**[7:19](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=439s)** It's the unified platform to build, deploy, manage, and scale enterprise grade models and agents in production from Google Cloud. It comes with 150-plus pre-built models, including Gemini models, and the possibility to use custom ones with tuning, training, and experimentation. The agent designer and agent runtime tools enable builders to create collaborative agents using open source frameworks, sessions, memories, MCPs, code executions and more. The governance and monitoring tools allow continuous observation, evaluation, identification, and tracing. And the search tools enable a RAG vector and AI searches. In fact, in the context of Workspace, the agent platform search is a key integration point

**[8:09](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=489s)** because of the connectors that are currently available for Gmail, Chat, Drive, Calendar, and People. With this, agent developers can search for users business data at runtime by using the dedicated agent search API or Google-managed MCP server. The ADK framework makes it easy to do that by registering the tools and by defining when and how to use them in instructions, like we've seen before. Now, did you notice I did not talk about user interfaces yet? That's because there is none in agent platform. You need to use APIs and integrate agents with your own UIs. In the context of Workspace, we can use add-ons. And the travel concierge agent, you already know, is a great example of that.

**[8:59](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=539s)** It's an add on built with Apps Script, and it relies on agent platform APIs to manage sessions and turns. We created this Codelab if you want to learn more. It contains step-by-step instructions on how to build this type of agent. Check it out. In case you do not want to integrate agents with your own UIs, you can rely on the last layer of the stack. Gemini enterprise aims to bring the best of Google AI to every employee for every purpose. Its web app is a key component to achieve that goal. But it's more than just a web app. Gemini enterprise is a complete platform built to discover, create, share and orchestrate agents across an organization, with secure foundation

**[9:50](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=590s)** and global business context. It comes with governance for security and control, and it supports all kinds of agents, agents developed using no-code, low-code, pro-code tools, agents authored by Google, the organization partners, or third parties, and agents that can run from anywhere, whether they are built using Google's AI tech stack or not. In the Cloud Console, admins can set up data stores. Here is an example of Workspace data stores connected to a Gemini enterprise app. Admins can also register agents running from any agent platform, using the agent-to-agent protocol or the Cloud Marketplace. These agents can use tools based on Workspace APIs

**[10:41](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=641s)** or Google-managed MCPs and rely on the authentication mechanism of Gemini enterprise. In the Gemini enterprise web app, on the other hand, users can interact with the agents, models, tools, and data stores configured by the admins. They can also create personal no-code agents from the agent designer through prompting and manual editing. Here, I'm creating one that relies on drive collector tools, for example. Now, what if you want to integrate Gemini Enterprise Agents with Workspace application UIs? Well, the solution is similar to the one used for agents running on the agent platform. You need to use the provided Gemini enterprise APIs. We created this Codelab if you want

**[11:28](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=688s)** to learn more about all this. It contains step-by-step instructions on how to build these type of agents. Give it a try. All right, everything I discussed so far is available, but you might be wondering what's coming next. There are a few things I recommend monitoring-- connectors and MCP servers. They empower agents with a growing number of tools. The A-to-A and agent-to-UI protocols, they standardize agent communication and generative UIs for greater collaboration and distribution. Full-duplex models, such as Gemini Live, they unlock a new set of interactions and use cases. And last but not the least, skills-- they are getting more popular, and they already proved to be a great complement to MCP tools for agents.

**[12:18](https://www.youtube.com/watch?v=erRPuV1EQ_c&t=738s)** I'm dropping a few more useful links here to help you get started. Have fun exploring all these tools and solutions. Until next time, see you online! [MUSIC PLAYING]
