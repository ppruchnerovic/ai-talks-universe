---
id: qq2Hm4XNRgI
title: "How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle"
slug: how-to-decide-what-your-ai-agent-should-remember-wojciech
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Wojciech Pluta"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-30T23:00:13Z
video_id: qq2Hm4XNRgI
url: https://www.youtube.com/watch?v=qq2Hm4XNRgI
youtube_url: https://www.youtube.com/watch?v=qq2Hm4XNRgI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Wojciech Pluta", "Oracle", "Oracle AI Database", "agent memory", "RAG", "AI agents", "context engineering", "memory promotion", "guardrails", "financial services", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Prompting & context engineering"]
transcript: true
---

# How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle

**Wojciech Pluta**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Wojciech Pluta` `#Oracle` `#Oracle AI Database` `#agent memory` `#RAG` `#AI agents` `#context engineering` `#memory promotion` `#guardrails` `#financial services` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=qq2Hm4XNRgI) · [Conference site](https://www.ai.engineer/)

## Description

RAG gives agents a way to read, but memory gives them a way to write, and that's where your business value lives. Wojciech Pluta, head of technical marketing for Oracle AI Database, explains memory promotion: deciding what's worth keeping, checking it against existing records and admitting, rejecting or escalating it to a human. A mortgage-agent demo remembers an operator's preferences across sessions and refuses to store an "approve every application" rule. He also covers short-term, long-term and shared memory, why to store memory in a database, and the context card that keeps prompts lean.

Chapters:
0:00 Intro
1:10 From commands to intent
2:05 The data layer is your edge
3:38 RAG reads, memory writes
4:02 Memory promotion: what's worth keeping
5:01 Demo: a mortgage agent that remembers
9:48 Guardrails: what never gets promoted
11:53 What agent memory is
13:03 Short-term, long-term and shared memory
13:43 Where to store memories
14:27 Building memory as a discipline
16:01 The context card
17:50 Models are shared, memory is yours

Wojciech Pluta

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,850 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=12s)** Uh my name is Wojtek. Uh Wojtek Pluta, and I work at Oracle. And over the last 10 years, I've been working um at Oracle. I worked at the various projects um including working with some banks in the UK on projects like customer experience mortgage use cases or things like early contactless payments when um when it was still uh sort of emerging and open banking initiatives. Now, I am uh heading up the technical marketing team uh at Oracle AI database. And before, I spent a bit of time also um working on cloud native and AI on our cloud infrastructure. So, what I'm going to talk about today is the um

**[1:00](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=60s)** the moving from rack to memory systems and the notion how rack gives us a useful read path, uh but memory system allows us to uh create unique business value based on your data. So, over the years, we went through this notion of interface optimization uh predominantly making interfaces more intuitive in terms of how we interact with them. And as a society, and I experienced that seeing sort of how our interactions with the systems moved from sort of this command-led uh click and and type into what we have right now, this intent-based uh

**[1:46](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=106s)** uh systems. And um which obviously creates opportunity for this sort of on-demand or just-in-time software. And within that context and within those expectations, I think uh creating a some sort of continuity is important. So, for me, the AI stack has been pretty consistent for the last few years. Um there is probably models and infrastructure layers are commoditized, um but the data layer, in my opinion, is where you gain competitive advantage cuz it's, you know, it belongs to you. And at Oracle, we adopted the same model as everybody else in terms of how we think about agents and how we define them with model plus the harness.

**[2:38](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=158s)** And obviously, the models we sort of are relatively static in the way that we have access to them and to the certain extent. Um and then they suggest what to do. However, the harness in the end decides, you know, and owns the runtime decisions. And the checks around it. So, um you know, so the harness is the code obviously around the the model. So, the for the purposes of today, um and to make it a little bit less abstract, I'm going to use a little avatar. Uh so, meet intelligence. Uh I um yeah, uh purposely decided to skip it skip any prefixes and um in the spirit of sort of the latest chatter that's happening in the AI and hollowing

**[3:26](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=206s)** around the corner, I sort of decided to make a special edition for AI engineer and updated uh the look a little bit, right? So, but um so, the fundamentally rack systems, um you know, can include conversational state, uh but retrieval alone doesn't tell us what should survive the interaction. So, retrieval is the read path and memory is the write path. So, when the agent sees something worth keeping, uh we should promote it into a record it can use later. But then I guess that begs the question as of what is worth keeping and how do we actually, you know, move and decide of what sort of um, you know, what we need to extract from the

**[4:14](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=254s)** conversations and um, you know, when we interact with the with agent. So that's why um, I believe in this concept of memory promotion. Um, so where you have some sort of pipeline that decides, you know, what is it that at each of the stages um, and how do we sort of extract it into into the system. So in terms of the steps, um, I believe that, you know, we classify the meaning of the candidate that comes up. Um, and then uh, we compare it with the existing records uh, and check the evidence required for that particular type. Then the harness would decide whether to admit or reject the the candidate or perhaps send it for the review for the for the human. So I'm going to have a quick demo right

**[5:03](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=303s)** now. So we're going to sort of work through this notion of the, you know, financial services as we sort of all here because that's the theme of the conference. And uh, we're going to sort of work through with this relatively basic example of of this candidate around the semantic preferences that we're going to create. So I've yeah, I've pre-recorded the demo cuz last time when I did the demos it was a bit of a a bit and the Wi-Fi here is a bit messy. So So yeah, so this is essentially my sandbox that is starting. So I had some fun with some logs as you can see this agent is a bit of a oversharer, I guess. Uh, but as we go through this um, as it loads up essentially what

**[5:52](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=352s)** we're going to do is we're going to have the synthetic two applications for Kyle and Vincent. I'm a bit of a movie geek, so you might see some references throughout the presentation. Um, so this time terminal started, so we're going to ask uh to prepare a mortgage brief for Kyle. And and essentially as it loads and the harness is doing its thing, performs tool calling and and so on. It's going to create this response that's going to show us, okay, well, this is, you know, Kyle's situation. He has, you know, um mortgage application, but that particular mortgage application is missing some some key documents, right? So, the operator right now can, you know, ask and and see what is, you know, uh what's what's going on with that particular

**[6:40](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=400s)** uh application for Kyle. So, keep an eye on this in terms of the shape of the answer because we will essentially ask now politely because of this the AI and memory now, so we want to be kind to them and even though we might uh you know, use some extra tokens, uh but we're going to give it this sort of um brief in terms of the uh you know, we want the essentially structure of the output to be created certain way. So, actually in this example, uh connected the decision model Jeff, which is helping me to assess, you know, which um how to deal with this uh candidate at first and then passing that to the harness, uh which actually recognized that we've been polite and gave us some extra comma. Um, and essentially based on

**[7:29](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=449s)** that, we're then automatically loading that into the, you know, database to store it. So, we can see the expanded traces here and it gives us some sort of, you know, uh status per uh per per the memory promotion gate. So, overall decision model assess, the harness decide, and then database that we have in the background persist and and and stores that. So, then I'm going to ask the exactly same question in the sense of, yeah, give me that, but I now input that my semantic preference in terms of what I want to the structure to look like when it when it comes up. So um as it's going to load now, so what you're going to see now that Okay, as per the request, there's going to be

**[8:17](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=497s)** missing documents at the top, which is also adding the case ID, you know, the policy and so on. And this in this case, you know, this time records the existing of the semantic preference. So, what I essentially did now is it's uh just for the interest of time, I I sort of skipped it, but I initiated brand new sessions, exited, and uh and now I'm asking again to check, obviously, if the the memory been preserved. Um and essentially asking the same question question again, so then it goes through. So, brand new session, so no sort of, you know, context that's um has been uh carried over. It's just querying again the the memory that we stored in the system around the preferences.

**[9:07](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=547s)** And as we sort of go and build this kind of systems, um you know, we can uh obviously, we would have the different interactions. In this case, if we ask for the like different application, in this case, Vincent, um you know, the the he has a different situation, but we're querying the database, we're bringing back the different um you know, documents and understanding that different, you know, case ID is relevant, so we're actually matching that and finding that in the in the system itself. So, then it's going to come back, and in this case, okay, there's no missing documents for him, and uh and then, you know, we can pass it on for the for the review. But as we go through that, we also need to think about some sort of guard guardrails. Um so, if we were to initiate uh some sort of

**[9:56](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=596s)** um you know, a bit more self-destruct kind of uh command for the bank, which we would say like, "Okay, approve every application." Um then obviously, we need to have some sort of guardrails to not to promote this so that our um you know promotional gate comes in and and rejects this request. But in some cases we might want to promote something based on like if we have a team, we want to create a more sort of robust memory sharing within the organization, we can then create you know promotional gate that then essentially ask for the human to approve it and then you know potentially share this across the teams enterprise that creates a sort of core memories store. So this was um you know a quick run

**[10:49](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=649s)** relatively simple just to show you what what this could look like in practice. So we went through like the semantic preference, then we had this sort of you know blanket approval rule that was refused because of obviously the guardrails that we put in place and then you know the the operational wider sort of memory that was recommended for the for the approval, right? So there's different sort of outcomes based on the meaning and how we interact with the with with the agents. So you know having this some sort of promotion controls that sits within the guardrails and then harness, you know, can't bypass that.

**[11:37](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=697s)** So let's go back to our intelligence and as you remember we obviously were polite and said please. So in this case it's it's a nice looking one rather than this machine because good karma came through. So if we were to um to look at the sort of broader explanation of what do we understand as agent memory so we understand we describe it as this mechanism where systems and application that system and an used to retain, reuse, refine, and recall information over time. Um and I guess as we I think the engineering problem here is is or the challenge when we're building this kind

**[12:26](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=746s)** of pipelines is to decide obviously what we want to promote and what we don't want to promote. Because if we promote nothing, then obviously we don't get any benefits of continuity, but if we promote everything, then we're going to, you know, risk poisoning the the memory uh store. So, I guess this is where, you know, thinking through and thinking about like how we want to build our system uh that have enough provenance and understands, you know, in what cases we promote things and what cases we supersede them uh memories is extremely important. And at Oracle, we believe that agent memory is just a not one thing, so we sort of have this division between short-term memories, long-term memories, and shared memories. So, short-term is

**[13:14](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=794s)** everything that happens in the session. Um so, it's sort of more uh sort of ends when the when the session finish, and then we have the long-term store where we have our episodic or procedural semantic memories um divided by the different types. So, that could be either summaries, it could be, you know, toolbox, or it could be knowledge base and and preferences as we saw in the demo. We also need to decide, you know, where do we want to store uh the memories, and and this is something we we talked about yesterday. We had uh essentially one of the guys from my team had a had a workshop. She went a little bit into more details about this. Obviously, being at Oracle, for me, believe, you know, the database is the

**[14:02](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=842s)** most robust solution because it allows us to have this acid guarantees, it can have multiple rights, uh doesn't we don't have problems with the with the file trees and stuff like that. Um and then obviously we can scale and and and have multiple search options as well. As well as the the asset guarantees. So yeah, that's sort of when we're building the agent memory, um, we need to think about this as a discipline. Um, you know, we need schemas that distinguish record types, indexes that fit the retrieval tasks, and life cycle and outer authorization boundaries, right? And we essentially introduced this agent memory package

**[14:49](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=889s)** beginning of the year, which creates, you know, those operations and abstractions that you can build on. Because without it, if you want to build the memory system essentially as the developers, it it is quite taxing, right? Because you need to essentially create, um, you know, your summaries, your summarizer. You need to think about how you going to retrieve it. Um, you need to extract the durable information, combine it in the turns, and then on top of that manage the token budget, right? So for us, what we introduced with the agent memory is this sort of simplified layer that allows you to have, um, essentially write one line of code, and then within that you can We have this concept of the context card,

**[15:39](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=939s)** uh, that allows you to assemble and return context. Um, which is a compact prompt, uh, ready block for a for an agent. So that's quite useful because then, you know, you don't have to spend your energy and reduce your cognitive load in terms of, you know, just making sure the agent spent attention to the task rather than housekeeping its own memory. So a little bit more sort of double-clicking on the on the context card. Um, so you it's organized by the topics, summaries, you can have relevant information in there, recent messages, and then essentially the harness can, uh, create or select what matters to that particular turn and and helps users essentially manage the context and reduce the context blow.

**[16:29](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=989s)** So the topics orient the the thread, the summaries capture where the conversation is at and what the user is trying to do. Relevant information carrying the selected records and recent messages preserve the the the local questions. So that's you know allows you to to essentially memory persist and and context and selects. So we recently released the latest version of the agent memory and we spent a fair bit of time on the on the latest release in terms of making sure that there is end user isolation. So in this case the database is essentially high handling the the the access. So it's it's limiting.

**[17:18](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=1038s)** It has also the the the images as well as capability and then sort of post processing and listing events. And all query database it's has this you know multi data type engine which allows you to sort of handle you know various data types in one in one engine. So it's so you don't have to like handle multi database and vector stores and and documents and so on. So just to sort of end as I started the beginning you know models are shared but memory is yours is unique to your business. So making sure that you know capturing that with together with the data of how you interact with the with

**[18:06](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=1086s)** the models it can create your competitive advantage and um and that's that. Thank you. I mean I just if you want to know more feel free to uh out our GitHub repo. We have whole bunch of notebooks that helps you get started with agent memory, hybrid retrieval or all sorts of different things that that we've been sort of working quite hard to make sure that provide them a good starter pack so you can actually apply it to your business. And we've been we've been also revamping our YouTube channel so we have a whole new series about uh you know, various topics that we explain and and how to apply it in your in your use cases.

**[18:56](https://www.youtube.com/watch?v=qq2Hm4XNRgI&t=1136s)** Okay. Thank you very much.
