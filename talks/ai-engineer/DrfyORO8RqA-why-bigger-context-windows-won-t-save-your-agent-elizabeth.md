---
id: DrfyORO8RqA
title: "Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS"
slug: why-bigger-context-windows-won-t-save-your-agent-elizabeth
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Elizabeth Fuentes Leone"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-08T00:30:18Z
video_id: DrfyORO8RqA
url: https://www.youtube.com/watch?v=DrfyORO8RqA
youtube_url: https://www.youtube.com/watch?v=DrfyORO8RqA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "context engineering", "context window", "AI agents", "Strands Agents", "AWS", "Amazon Bedrock", "agent memory", "long-term memory", "multi-agent", "MCP", "LLM hallucination", "lost in the middle", "tool calling", "Elizabeth Fuentes Leone", "AI Engineer"]
topics: ["Agents & orchestration", "Prompting & context engineering"]
transcript: true
---

# Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS

**Elizabeth Fuentes Leone**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#context engineering` `#context window` `#AI agents` `#Strands Agents` `#AWS` `#Amazon Bedrock` `#agent memory` `#long-term memory` `#multi-agent` `#MCP` `#LLM hallucination` `#lost in the middle` `#tool calling` `#Elizabeth Fuentes Leone` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=DrfyORO8RqA) · [Conference site](https://www.ai.engineer/)

## Description

A bigger context window won't save your agent. Past a point, it forgets the middle.

Elizabeth Fuentes Leone, developer advocate at AWS, explains why agents break when tools return huge amounts of data, and why bigger context windows aren't the fix: models remember the start and end of a long context but lose the middle. Using the open-source, model-agnostic Strands Agents framework, she walks through four strategies (externalize, select, compress, isolate) with code. She covers sliding-window and summarizing conversation managers, short-term, long-term and graph memory, memory pointers that keep big tool outputs out of context, sharing pointers across a swarm of agents, capping tool calls to stop endless loops, and async handles for slow MCP tools. She ends with the anti-patterns to avoid.

In this talk:
• Why bigger context windows don't fix agents, and how models lose the middle
• Four strategies: externalize, select, compress and isolate
• Memory pointers, conversation managers and multi-agent state in Strands
• Stopping endless tool loops and handling slow MCP tools

SPEAKER
Elizabeth Fuentes Leone, Developer Advocate, AWS
X: https://x.com/lizfue

LINKS
Strands Agents: https://strandsagents.com
Strands Agents on GitHub: https://github.com/strands-agents

CHAPTERS
0:00 Intro
0:37 Why agents break on big tool outputs
1:12 Example: a log-watching agent
1:57 Bigger windows aren't the fix
2:12 Lost in the middle
2:42 What context engineering is
3:17 Externalize, select, compress, isolate
4:07 Conversation managers
5:07 What Strands Agents is
5:57 Summarizing conversation history
6:42 Short-term, long-term and graph memory
8:12 Memory pointers for large tool outputs
9:47 Sharing pointers across a swarm
10:42 Agents that never stop
11:22 Limiting tool calls
12:12 Async handles for slow tools
13:41 Anti-patterns to avoid
14:36 Cheat sheet

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,266 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=DrfyORO8RqA&t=12s)** Hi. Well, first I have to say I am Elizabeth. I am not Morgan. But the guy for the agenda they never change agenda. So we are almost the same but with different colors hair. Okay. So it's it's going to be similar. So today I going to talk about the infinite content window is a meet. Yes. Yes is because right now edge system breaks when tools returns a large amount of data. Context window overflow and the engine start to hallucinate and start the recar is degrad. So right now context engineering help us to uh give us a better

**[1:03](https://www.youtube.com/watch?v=DrfyORO8RqA&t=63s)** architecture for this agent application. So we have some techniques that allows us to improve the context the context window for this agentics application. So imagine that you have a agent that is responsible to uh supervise some application. So this agent they have to retrieve log logs for that application. So every time this agent is doing the retrieve for the logs is putting data for the content window and every time this content window is going to grow. It's going to grow every time because when we have a one session and each session is going to retrieve the last session because it's going to remember everything. That's the way that agents remember and they use the content window

**[1:52](https://www.youtube.com/watch?v=DrfyORO8RqA&t=112s)** for that. In the past about probably one year ago before this agentic era we saw that just add more token that will fix it. Yeah, there's more bigger content window that is going to fix it. And today we know that is not true because we have the uh attention you curve. What is this? We have a lot of data, but if that data is super super big, the engine is going to forget the meter in the in the in the curve. It's only going to remember the first part and the last part that we sent to that content window. And I'm talking here about context engineering. But I can move. But

**[2:43](https://www.youtube.com/watch?v=DrfyORO8RqA&t=163s)** content engineer is giving the model the information it needs when it needed. Sometimes the agent doesn't need all the information inside that content window. Sometimes the content window is poison the engine because you can have a problem injection inside your content window and the content engineer help us to incorout the context window for optimal outcomes and token consumption. So today I going to show you some techniques that can help you to improve the content window. And these techniques uh I manage for a strategy. We have we have the externalize because move this that this big data to a persistent storage. You can create a memory pointer

**[3:34](https://www.youtube.com/watch?v=DrfyORO8RqA&t=214s)** to storage that data. I going to share the deck at the end. So you need to you don't need to have to. Please pay me attention and because I going to share you all the information that I going to talk share. And the second one is select you can retrieve only what is relevant. We have compress that reduce token because you can summarize and you can compact that information. And the last one is isolate because you can separate context across agents. and let's start. So the starting point conversation manager this strategy yeah we have some strategy that are a little complicated but we are going to start for the easy

**[4:21](https://www.youtube.com/watch?v=DrfyORO8RqA&t=261s)** one that we can use inside the framework. So here in this strategy we are going to use a strand engine is a framework like we are a we maintain is completely open source yes it's free and is a yeah it's open source free hence it's completely model and so here with strands you can use three different strategy inside the framework so we have sliding window that allows you to keep only the most recent messenger we have summarization inside the framework that allows you to summarize all their messenger and keep present one and the last one is a combination of two we have that you can combine summarize of older messenger with resent one so first let's

**[5:11](https://www.youtube.com/watch?v=DrfyORO8RqA&t=311s)** see what is a strand a strand is this so you only need one line of code to create the agent loop so this line here create all the agent loop behind the scene. You need to create the nose, the graph, nothing because the strands can do that for you and you have the system prom and the tools. And yes, this is simple because it's using Amazon better behind the scene. But if you want to use Lamba uh Gemini and tropics, you only need to add one line because you can do that. You import the the library for OpenAI for example and then you add the model line and that's it. So let's return to our strategy. If you want to use

**[6:00](https://www.youtube.com/watch?v=DrfyORO8RqA&t=360s)** summarization conversation manager that's the only line that you that you can add for this agent loop. So you have the summary radio that is in this case is 50% and you want to preserve preserve the last four messages. So every time that you invoke this agent in this session, this session is going to manage your content window in this way. So it's going to keep the four last messages and it's going to summarize the other 50%. And yes, this is amazing. But what happen when you have a lot of memory and you don't want to lose you don't want to lose all the memory inside that content window. So you can use well always we have shortened memory because shortterm

**[6:48](https://www.youtube.com/watch?v=DrfyORO8RqA&t=408s)** memory is when you have the recent conversation history. So you can use this uh application in the shortterm memory. But what happen when you want to return and uh you for you uh you have a new session for this agent and you don't have short-term memory. You can have long-term memory and you can create a vector database for that long-term memory. You can have different types of memory inside that vector database with different prompts that can understand your conversation and say whatever you want. And the third one is relation memory. You can use entity graph. You can go to the uh to the guy for neo forj that they can explain you more about that. You can use traversal baset or how things connect.

**[7:36](https://www.youtube.com/watch?v=DrfyORO8RqA&t=456s)** So you can understand you can use a combination of three of those. You can have long short-term memory for the me the session that you have. Then you can retrieve the memory that is in the past the long longterm memory and if you have some relation thing that you want to keep in a different way you can add for that a graph memory as well. Let's continue with the other one. So what happened with this application where a lot of logs that I told you you don't want to put that locks inside your content window every time that you invoke the agentic application that agent you can save that inside a memory pointer. So what how this work? You have the the tools. The tool returns you and a bunch of uh logs. You can use another

**[8:27](https://www.youtube.com/watch?v=DrfyORO8RqA&t=507s)** tools that is going to capable to took that logs and save that logs in a storage and you are going to retrieve an ID for that storage and for that using a strands you can have that using the agent state. In the agent state you are going to have all the information for the tools. Then you can use another tool that is going to capable to understand that logs and it's going to send um it's going to send to the agent hey the logs okay you don't need the logs to understand that but what happen is you need the logs you can go say hey this is my ID come on retrieve the logs because I needed to know so this is something that you can build in your architecture and it's something like this you can have two different tools that's the way

**[9:16](https://www.youtube.com/watch?v=DrfyORO8RqA&t=556s)** that we create tools inside the trans only with the tool decorator. So we have fetch application logs and if you can see there you have the tool context agent step state. So we retrieve that information and we save that in a memory pointer. We create a memory pointer ID that is going to preserve inside our content window. But what happened is your application is super complicated and the tools is not enough. You can use ah if I forget that you can use a multi- aenting application. So you can create a a trans swam with multi- aents but you share the context window between agents is like add garbage to the other agents

**[10:07](https://www.youtube.com/watch?v=DrfyORO8RqA&t=607s)** because no all the agents need the information between them. So you can share the information between the invocation state pointer. So you can create an ID between that swam agent swam and you can share the memory pointer between the the invocation state between that aents and that's the way that we create the swamp in a strand agent and oh my god 9 minutes I going to be fast and the next one is where the next one is what happened when the engine uh want to stop never in sometimes we have this engine that stay in the loop like forever invoking the

**[10:55](https://www.youtube.com/watch?v=DrfyORO8RqA&t=655s)** same tool the same tool again and it's never ending so you can stop that with a minimum amount on invocation inside the loop so what is the problem I said the problem to sell more soul may be available so what does happen when you not when you you don't have a clear response when you evolve the tool So you can avoid that with the tool way with the clear response and with amounts of invocation for the tool and you do like this. So you have a limited tool count. So you set max tool counts for this example is my tools search fly. You can you only can invoke that tool three times and the other tool. Yeah. Three time as well. So the agent never is

**[11:45](https://www.youtube.com/watch?v=DrfyORO8RqA&t=705s)** going to do to do this uh internal loop. It's only going to invoke that tools three times. And the last one, yes, I almost there. The last one is uh is not something that help you to the context window. is something that you can use to help your content window because sometimes we are invoking IMCP tools or IMCP or we have external API that never answer you at the time that you need it. Sometimes for example we have EP gateway AWS EP gateway it have a a maximum time that is going to receive the the answer. So if you don't have that time, it's going to uh like stop your application because

**[12:32](https://www.youtube.com/watch?v=DrfyORO8RqA&t=752s)** the delay. So you can avoid that using a a synchron. So when you use synchronous, your engine is going to wait forever for the answer for your NCP. But if you have an a sync handle, you can invoke your NCP, your external API. So then you can save that and you can retrieve the answer in the next invocation or when you need it. Yes, this is going to depend of the case that you are building and you can do that like this create MCP this is a function that use fast API and with fast API you only need to create the tools. So I going to have two different tools. One is the star lob and another one is check job status and I did a lot of test using

**[13:24](https://www.youtube.com/watch?v=DrfyORO8RqA&t=804s)** this uh a sync handle and the different is a lot. For example, if you have the different um the well the agent never stop to answer me. So because I wait then he can retrieve the information and to close this session six minutes we have the antipartis so why uh you have to avoid you have to avoid contact stuffing so you need you don't need to include everything and the kitchen you know you don't have to include everything the content window because the engine doesn't need all the information there you can only share what a need to create the answer that your user or you're asking for. You can

**[14:12](https://www.youtube.com/watch?v=DrfyORO8RqA&t=852s)** have uh native summarization. Sometimes when you do native summarization, the agent uh can uh you can uh forget what you need. If you're doing whatever superization what you may for probably in that summarization, you are not going to have everything that the engine is needed to answer you. and context population. Again, don't pass everything to the agent. The agent doesn't need all that information. And what is a good scene here? So tool returns large data, logs, database, alert information, externalize, select and use a memory pointer. Many engines need the same large data. You can share invocation between stage and agent loops or tool hands. You can

**[15:02](https://www.youtube.com/watch?v=DrfyORO8RqA&t=902s)** have clearest st you know give a clear answer for the tool and limited to counts and a thin handle. Thank you. And of course if you want to learn more about stringent we have a huge boot there. We have a lot of swag. We have a little Legos for Amazon that you can have and see you there. We have the specialist and I am Elizabeth No Morgan remember. [laughter] Thank you so much. >> [music]
