---
id: zfKqikfVSqA
title: "One AI Chat to Rule Them All: Connecting Enterprise Tools with MCP by Karthik Sayapparaju"
slug: one-ai-chat-to-rule-them-all-connecting-enterprise-tools
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: []
channel: "Devoxx"
duration_min: 16
published_at: 2026-03-30T17:38:49Z
video_id: zfKqikfVSqA
youtube_url: https://www.youtube.com/watch?v=zfKqikfVSqA
tags: []
transcript: true
---

# One AI Chat to Rule Them All: Connecting Enterprise Tools with MCP by Karthik Sayapparaju

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=zfKqikfVSqA) · [Conference site](https://devoxx.com/)

## Description

#VoxxedDaysCERN26

Tired of juggling Jira, Confluence, GitLab, and Slack/Mattermost? What if one AI could search tickets, find docs, check PRs, and summarize discussions, while keeping data on-premise and avoiding subscription costs?
I'll show how to build this using the Model Context Protocol (MCP), an open standard for AI-tool integration, now under the Linux Foundation and adopted by OpenAI, Google, and Microsoft.

What the audience will see:
MCP Introduction : What is MCP, how old is it, who's driving it forward (Anthropic, growing community), and why it matters - the "USB-C for AI tools."
Architecture and Implemetation : How MCP clients, servers, and the protocol work together. The local stack: Ollama + Open WebUI + mcpo proxy connecting to MCP servers for Atlassian, GitLab, and Obsidian.

Demo : Real queries across systems: Searching tickets, finding docs, checking repos

Key Takeaways :
Basic understanding of MCP protocol
See a real POC connecting to enterprise tools
Blueprint of the architecture to experiment with
Target audience: Engineers, developers, curious technologists, team leads, anyone interested in practical AI integration.

## Transcript

*1,904 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=zfKqikfVSqA&t=0s)** Cool. That's good. Um, hi ladies and gentlemen. My name is Karthik. I used to work at CERN. Um, and thanks for coming here. Welcome to the talk. Today I'm going to show you one of the uh emerging ways to connect your AI to external tools. So um to begin with um recently I this is a snippet of the summary I had with um of the summary I had with chat GBD. What happened was I wanted it to plan me a 5k run in Falar. Um so yeah it did a great job. It generated me a nice route through the foothills of Jura across the um French old farms. But I had run this route

**[0:48](https://www.youtube.com/watch?v=zfKqikfVSqA&t=48s)** multiple times already. So I um asked it to create me a new route but it generated me new route again. Great. But this time there was a lot of lot of uphill but my body was sore. My legs were still recovering from the previous run. So I had to give it more context again to like give me a flat route or something like that and then add it to the calendar. But obviously all this power is missing um in the host application like it cannot perform actions, it cannot create calendar events for you. So over the last couple of years we've been trying to solve this lack of context problem by copy pasting things from various sources. Um and then this is very tedious, right?

**[1:38](https://www.youtube.com/watch?v=zfKqikfVSqA&t=98s)** like you have multiple sources and each time you have to each time you're writing a new prompt you have to give it more context from various sources and the other way um we have this thing called rag um which stands for retrieval augmented generation wherein you dump all your resources into a vector DB create embeddings and um hope that the algorithm does the search good search for you and inject the relevant resources. When a user prompts for um something into the LLM context and then now your LLM has a with the elaborated context, it can give you a good reasoning. Um and the last choice you can give give

**[2:28](https://www.youtube.com/watch?v=zfKqikfVSqA&t=148s)** it more power by writing a custom integration. Let's say um from the previous example, if I wanted my host app to have access to my Straa, so I didn't have to give it all the training context, I should have written a custom integration to the Straas API and give it all the authentication um stuff. That way now it has more power. Now it has access to the tools. Um it can make some it can perform some actions, create resources and fetch some resources. But if I want to extend this um if I want more integrations then I have to write custom integrations for each external service. Now that's a problem. Um and we've like tried to solve this and

**[3:18](https://www.youtube.com/watch?v=zfKqikfVSqA&t=198s)** integration problem before in software engineering with patterns like facade the classic add another abstraction layer. So then came something called model context protocol which was made open source by um anthropic towards the end of 2024 in November and then they donated it to the Linux foundation. Now it has endorsements from all the biggies like OpenAI, um Google, Microsoft etc. So essentially the it essentially has three big um components. You have the host application um and then the MCP servers and external

**[4:06](https://www.youtube.com/watch?v=zfKqikfVSqA&t=246s)** server services. So your LLM AI logic sits in your host app. So this new component called MCP client sits in the host application which facilitates the communication with um the external systems. It makes structured calls to MCP something called an MCP server based on the specification from the model context protocol. Um it doesn't do the actual API calls but it does structured calls to the MCP servers. MCP servers are standalone applications. Um by standards they are maintained by the external services themselves which do the major work of calling the real APIs. So

**[4:53](https://www.youtube.com/watch?v=zfKqikfVSqA&t=293s)** moving forward when you boot up your host app like a quick glance on how this hold handshake goes the MCP client introduces itself and then MCP server uh validates the request and responds with a persistent connection and then makes the client aware of the aware of its capabilities like tools for instant for instance. So tools are essentially like function calls which you can which the MCP client calls to perform actions, fetch resources, create resources or patch resources. So these tool definitions with their schemas are injected into the LLM context um by the host app. And then when a user prompts

**[5:43](https://www.youtube.com/watch?v=zfKqikfVSqA&t=343s)** like you can see in this example when a user prompts read my messages um the diagram is could be misleading but when the user prompts read my messages LLM looks up um if it has some tool available where it can actually check messages from a certain app in this case we're using Mattermost which is like an internal messaging app um like Slack at CERN So with its available context, it's going to check for messages, call the MCP matter server, and then that would do the actual API call and return you the messages. Um, in this example, I'm also going to ask me as a user, I'm going to ask the host app to summarize me these messages and anything that

**[6:30](https://www.youtube.com/watch?v=zfKqikfVSqA&t=390s)** sounds like an issue, um, create GRA tickets for me. Um yeah, let's actually look at this in runtime. I'm going to So this is the Mattermost MCP server that I've um created with very simple tools. You have get channel messages. Um the relevant part here is the name of the tool and the description. the description is more important because when the MCP when the LLM actually looks at the available tools, the description is what makes it decide if it wants to call the tool or not. So in this case, it's going to see from its

**[7:18](https://www.youtube.com/watch?v=zfKqikfVSqA&t=438s)** system prompt that it can fetch messages from this matter channel by calling this specific tool. So I have these couple of um sorry if it's if the font is too small but I have these couple of um servers defined in the config. Um the picture will be more clear but let me fast forward go forward. I'm going to send messages in this private channel and um issue something which sounds like issues. Let's say EDH document creation failed. Um, budget code not found for DAIS. Classic issues that I used to see back

**[8:10](https://www.youtube.com/watch?v=zfKqikfVSqA&t=490s)** then. Um, this is the cloud atlashian server of uh mine. There are no tickets in the backlog as you can see. So what I'm going to do is I'm going to ask my host app to summarize me. Um so by the way this is open web UI and I'm running one of the GPT models behind the scenes. Um so you can see the available tools here. We have mattermost and the remote at server. The matostmost one is running locally and have and I'm using the remote at lashions uh implementation. We'll look at the last one later but I'm going to ask it to summarize me the

**[8:59](https://www.youtube.com/watch?v=zfKqikfVSqA&t=539s)** discussion that happened in MCP demo channel. Hopefully this goes through. Um, okay. Guess I'm cursed with the demo effect. Sorry. I'm just going to quickly restart this. It shouldn't take long. Maybe the connection I created before is expired. Okay.

**[9:57](https://www.youtube.com/watch?v=zfKqikfVSqA&t=597s)** Can you summarize me the Just the same prompt. Fingers crossed. Yeah. So, the request went through um it fetched these messages from the channel and you have the summary here. There are it listed down. Yeah, you have these two issues and I think this is just the meta data of the user. So I'm going to ask it to create issues for me in Jira. um tickets for me

**[10:46](https://www.youtube.com/watch?v=zfKqikfVSqA&t=646s)** and Jira from for what it thinks issues as in um can you create tickets in Jira for me for for the above mentioned issues. Tik Tok. Tik Tok. Okay maybe. Yeah, looks like it went through. Um, I can see two logs here corresponding to the two issues mentioned in mattermost.

**[11:36](https://www.youtube.com/watch?v=zfKqikfVSqA&t=696s)** So if I reload this dashboard, I should see two tickets. Nice. So moving forward, um this has just been text input and text response. What if um the conversation was more cohesive and visual? What if users can actually interact with components rendered in the host app like some um HTML UI sandbox type frames? Um yeah, there's a a bunch of folks from Shopify have been driving this community forward. They have their own solid use cases. Um this is an example where you ask the host app. I mean, if you're in a new city and

**[12:23](https://www.youtube.com/watch?v=zfKqikfVSqA&t=743s)** you have been asking it a lot of questions without having to context switch a lot, you could just just ask it to book you an Uber back to the hotel if you're tired and then it would like render you the render you an interactive um component in the host app and then you can just request an Uber. Another example, um, things to do in Las Vegas strip. Instead of just getting raw text and directions, um, imagine if the host app returns you some nice 3D map of, um, the place and then you can just zoom in, zoom out, look at the buildings, um, perhaps even ask more questions. But yeah, um to conclude, all this stuff is pretty sorry, um pretty fascinating

**[13:14](https://www.youtube.com/watch?v=zfKqikfVSqA&t=794s)** to me. Um I'm pretty sure a lot of new patterns will emerge. Um tighter security models for what LLMs can access and what they can't. I would say you can think about a tool that you use. If if this MCP thing inspires you, you can should think about a tool that you regularly use and then try to build an MCP server or if you're lucky the servers already exist in Docker registry. In my case, when I discovered this, I try to use I try to implement it with my Obsidian where I make my notes on a very regular basis. Um, I keep conversing with AI, keep asking it technical questions or anything general about like a new city I

**[14:02](https://www.youtube.com/watch?v=zfKqikfVSqA&t=842s)** go go to. And then I instead of me having to like copy paste stuff into my notes, I can just ask it to um summarize the discussion and create a point list in my notes. Like let me just try to do it here. Can you create a note summarizing today's discussion in my obsidian world? Hopefully it can infer from this. Yeah. Um, it asks me to feel free to

**[14:58](https://www.youtube.com/watch?v=zfKqikfVSqA&t=898s)** copy paste the summary from the chat itself. But can you call the tool available? Another two seconds. Then I think I can like skip this part. It should Oh my god, it created Jira issues. But it's okay. Um, but you get the point. This was working at home, but I don't know what happened to it now. Um, but you get the point. It it could have just like created notes for me um on my Obsidian with the nice with a nice title and a summary so I can refer to it later. Um, yeah, that's it. Thanks a lot uh for attending and

**[15:48](https://www.youtube.com/watch?v=zfKqikfVSqA&t=948s)** hopefully you learned something new.
