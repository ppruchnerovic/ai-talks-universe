---
id: 30WU_6_wplc
title: "Keynote: Using MCP for Skills Orchestration and Enterprise Integration - Jacob Wilson"
slug: keynote-using-mcp-for-skills-orchestration-and-enterprise
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "Practitioner AI conferences"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: ["Jacob Wilson"]
channel: "Agentic AI Foundation"
duration_min: 10
published_at: 2026-04-13T23:17:08Z
video_id: 30WU_6_wplc
url: https://www.youtube.com/watch?v=30WU_6_wplc
youtube_url: https://www.youtube.com/watch?v=30WU_6_wplc
tags: []
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# Keynote: Using MCP for Skills Orchestration and Enterprise Integration - Jacob Wilson

**Jacob Wilson**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=30WU_6_wplc) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: Using MCP for Skills Orchestration and Enterprise Integration - Jacob Wilson, PwC Principal, GenAI Transformation Leader

Most enterprise AI experiences break down at the system boundary, where users know what they need but not which application, process, or data is required to complete it. This session uses procurement as a practical example of a different pattern: a single conversational interface powered by MCP that hides backend complexity while orchestrating work across multiple systems. We’ll show how MCP supports both skills orchestration and enterprise integration, enabling flows such as request classification, requisition creation, status lookup, and intelligent routing between procurement systems. The result is a practical blueprint for scaling system-agnostic workflows across ERP and other back-office functions.

## Transcript

*1,836 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=30WU_6_wplc&t=0s)** All right, how we doing? Good. All right, um So, I think a lot of different talks this morning, we talked a lot about the technical capabilities, the art of the possible, how all this stuff is coming together. So, wanted to bring this to life a little bit more for you all and how this is working with you know, true enterprises today. So, quick introduction. So, Jake Wilson, I'm a partner in our analytics practice at PwC. I have the privilege of consulting you know, some AI companies who are leading the latest and greatest you know, frontier state of the art models as well as working with utility energy companies who are building and fueling the next generation AI data centers and working with other clients across kind of industry and function. So, I came from a kind of traditional software

**[0:47](https://www.youtube.com/watch?v=30WU_6_wplc&t=47s)** engineering background, fell into the world of AI about 9 years ago. At that point in time, we were doing some things in emerging tech PwC and then I was like, hey, you know, being a software engineer is great, but in order to really lead teams in AI, got to understand the details. Went back, got my masters in data science at UC Berkeley, which is oddly enough, right when I completed that was the launch of chat GPT. So, it was like perfect timing. So, been living in the world of generative AI for the past 3 years. It has been the most exhausting thing I've ever done. So, what we're going to talk to you about today is how many of you all kind of um think that your procurement function could be a little bit more efficient and optimal within your organizations? Okay,

**[1:35](https://www.youtube.com/watch?v=30WU_6_wplc&t=95s)** seeing a number of hands going up. So, what we're going to talk about is how MCPs comes together with skills orchestration and integrating with enterprise applications. Um So, as part of this, you know, the context and the background is this particular client and clients we see kind of across the board, especially as we're getting into manufacturing who might be building the latest you know, robotics and other type of capabilities is you know, if you look at these organizations, whether they're newer startups or legacy kind of enterprises the challenge you're dealing with is I've got a lot of different buyers, right? These buyers could be people sitting in the research division who are you know, working on the latest AI models. They could be sitting in a robotics lab, you know, building out the

**[2:23](https://www.youtube.com/watch?v=30WU_6_wplc&t=143s)** next state of the art robotics. Um So, the problem is like none of these people want to go into these complex systems like your traditional ERPs and procurement systems to figure out how to actually go procure GPUs to go buy materials for you know, robotics and to do all these things. So, in this particular example, what we've created is a GPT app. That GPT app works with a MCP orchestrator. That MCP orchestrator is using the latest agent skills kind of format, which was published by Anthropic and you see a number of people kind of converging around today to help determine you know, when when a buyer comes in to make a request, you know, is this related to direct procurement

**[3:11](https://www.youtube.com/watch?v=30WU_6_wplc&t=191s)** you know, versus indirect. So, direct being more of like the robotics arms, the GPUs, indirect being like, hey, I need to get the CEO an ergonomic chair, right? So, regardless of who's coming in, we just need to simplify the experience and then we do all the complex orchestration on the back end using you know, techniques with MCP and agents to kind of do all that together. So, that's kind of the backdrop in terms of you know, GPT app communicating with MCP orchestrator and that is then working with the back end systems for the ERP and indirect procurement system. So, here's kind of a little bit more of a detailed architecture view of what this looks like. So, what you'll see on the left there is the MCP app and then kind of that widgets box. I think that widgets box is a standalone react

**[3:59](https://www.youtube.com/watch?v=30WU_6_wplc&t=239s)** application. So, the way this works is if I'm a buyer, I come in and say, hey, I want to buy you know, 10 robotic arms or 1,000 GPUs. Um Essentially, what will happen is that GPT app will do an MCP tool call to the MCP orchestrator. That MCP orchestrator has skills built into it to where it then understands the user's intent and basically kind of trying to classify the request as direct or indirect procurement because if it's direct procurement, it goes back to one system. If it's indirect, it goes back to another system and that whole experience looks different on the back end and the types of things you need to provide on supplier purchase amounts, purchase prices and all these things to actually satisfy the purchase requisition. So, that MCP orchestrator is doing that kind of

**[4:49](https://www.youtube.com/watch?v=30WU_6_wplc&t=289s)** initial intent classification and figuring out what it is that the user is trying to do and then based upon whether it's direct or indirect, it will then say, hey, do I have enough information I need to then make the downstream call to like the direct MCP server or the indirect MCP MCP server to then actually raise the purchase requisition for the robotics arms, the GPUs or what have you. Um So, as as part of this, so let's say in this case of the direct flow, right? So, we get the classification through the MCP orchestrator. That is again then going to trigger the direct procurement agent. That direct procurement agent will make the MCP tool call back to that system. We'll get the necessary information to help for example, validate that the supplier that they're

**[5:36](https://www.youtube.com/watch?v=30WU_6_wplc&t=336s)** requesting is the correct supplier and also can do some more advanced things over time in terms of just you know, is there a more optimal supplier based upon what you're trying to do or you know, the timelines you're trying to get all these materials satisfied by. So, that kind of comes back through what what then happens through the MCP orchestrator. So, I get my data back. Let's say I go ahead and raise the purchase purchase requisition, goes back to that system. That information comes back. Um But now what I need [clears throat] to do is say, okay, yes, here's the data, here's the confirmation from raising the purchase requisition at back end system. I now need to tell the GPT app essentially what UI resource to now load in with the data I got back from that back end system along with the response from the direct procurement agent. So, in

**[6:24](https://www.youtube.com/watch?v=30WU_6_wplc&t=384s)** that case, that's where the MCP orchestrator again kind of helps in terms of saying, okay, here's the information I got back. Now, here's the UI resource that kind of goes along with that. So, that now the GPT app can point to the correct view within the react application and then start to load in the structured content that we got back from the MCP orchestrator, which was a result of triggering the direct procurement agent. So, I think all that's interesting too cuz in the in the end too, like if you look at the the back end systems like in this particular example, one of one of the back end procurement system supports OAuth and direct flow of the user identity. The other system does not. And unfortunately, the only way you can interact with that system is through

**[7:12](https://www.youtube.com/watch?v=30WU_6_wplc&t=432s)** an API key. So, not the most secure. So, I think you heard in the previous talk too, this is where like MCP gateways are kind of helpful in the sense of yes, I can secure and put our back in front of that GPT app up front. But ultimately like if I want more protection, you know, as it relates to how like who can actually invoke these MCP servers on the back end through the GPT app and have a little bit more fine grain control. That's where those gateways come in place where you can define additional policies to also restrict like in certain scenarios like you know, for our utility energy client where we're doing transformation of kind of their operations of their data centers. Um There's very specific tools within the MCP server that you only want to invoke

**[8:02](https://www.youtube.com/watch?v=30WU_6_wplc&t=482s)** in certain scenarios. So, that's where the MCP gateway can kind of help add another level of kind of granularity in terms of like security for how you invoke even the different tools or functions within the MCP servers. So, it's kind of interesting to see all this come together just in the sense of not only can I use MCP to integrate with back end applications, but in this example too, you kind of see another pattern where you get things like you know, chat GPT where the only thing you can expose to it is an MCP. But I don't and and in those cases, you can have one MCP and you you need a little bit more control over how things get routed on the back end. So, it's kind of a pattern of using an MCP to help orchestrate invoke agents, which then also invoke other MCP servers. So, I find this one

**[8:52](https://www.youtube.com/watch?v=30WU_6_wplc&t=532s)** interesting just in terms of the pattern and then also kind of using the latest agent skills standard that you see Anthropic and everyone converging on, which is you know, all the skills and markdown files. Um What's funny about that too is it's just like another pattern of like tool calling in the sense of I'm exposing array of a list of in this case skills with the name and description versus tools name and description. But in this case, you know, we we've got the MCP orchestrator helping enumerate through that, invoking the right skills, which in turn invokes agents, which then invokes skills, which invoke MCPs. Um So, hopefully that was helpful. Just kind of gives you a context of a real world example as you think about you know, how to use MCP in terms of enterprise transformation where again, this is really simplifying in

**[9:40](https://www.youtube.com/watch?v=30WU_6_wplc&t=580s)** this case the experience for all the buyers across the research research divisions, robotics divisions, etc. Just to where they can come into a very simple app make a request. MCP does the orchestrator does all the complex routing and all the back end integration so that you know those people working on these complex systems and and robots don't have to go into these legacy applications to try and figure out how they work. So that's it. So we're out of time. Appreciate that and yeah, if you have any questions down here up front but thank you for your time. >> [applause]
