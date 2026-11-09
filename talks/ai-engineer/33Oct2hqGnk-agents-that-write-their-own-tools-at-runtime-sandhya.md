---
id: 33Oct2hqGnk
title: "Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS"
slug: agents-that-write-their-own-tools-at-runtime-sandhya
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Sandhya Subramani"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-04T21:00:13Z
video_id: 33Oct2hqGnk
url: https://www.youtube.com/watch?v=33Oct2hqGnk
youtube_url: https://www.youtube.com/watch?v=33Oct2hqGnk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Strands Agents", "AWS", "meta tooling", "self modifying AI", "self healing agents", "AI agents", "multi agent", "agent tools", "tool calling", "agent evals", "guardrails", "open source agents", "Python", "Sandhya Subramani", "AI Engineer"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS

**Sandhya Subramani**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Strands Agents` `#AWS` `#meta tooling` `#self modifying AI` `#self healing agents` `#AI agents` `#multi agent` `#agent tools` `#tool calling` `#agent evals` `#guardrails` `#open source agents` `#Python` `#Sandhya Subramani` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=33Oct2hqGnk) · [Conference site](https://www.ai.engineer/)

## Description

This agent starts with zero tools. Ask it for something it can't do, and it writes the tool and uses it without restarting.

Sandhya Subramani, senior developer advocate for GenAI at AWS, demos meta-tooling with the open-source Strands Agents SDK. That means agents that write, load and use their own tools at runtime, and even spin up their own sub-agents. All it takes is a system prompt describing what a good tool looks like, plus three tools: editor, shell and load_tool. She walks through agentic patterns (swarm, graph, handoff, workflow), demos a travel planner that builds its own sub-agents, and covers the evals and guardrails you need before trusting a self-modifying agent in production.

In this talk:
• Meta-tooling: editor, shell and load_tool plus one system prompt
• Agents that create their own sub-agents
• Evals for self-modifying agents: goal success, tool choice, parameters, inter-agent flow
• Guardrails: sandboxed execution, constrained permissions and observability

SPEAKER
Sandhya Subramani, Senior Developer Advocate, GenAI, AWS

LINKS
Strands Agents: https://strandsagents.com
Strands Agents (GitHub): https://github.com/strands-agents
Strands Agents tools: https://github.com/strands-agents/tools

CHAPTERS
0:00 Agents that forge their own tools
0:40 Fixing code at runtime
1:24 Demo: an agent with zero tools
2:49 It writes a calculator tool
3:39 It writes a character counter
4:59 Meta-tooling with Strands Agents
5:59 What Strands Agents is
6:44 Three tools: editor, shell, load_tool
7:43 Teaching the agent what a good tool looks like
8:43 The system prompt in code
9:53 Why this matters in production
10:43 Agents that create agents
11:03 Swarm, graph, handoff, workflow
11:53 Demo: a self-assembling travel planner
14:17 Self-healing agents
15:21 With great power: evals
17:06 Guardrails: sandbox, permissions, observability
18:56 Self-improving agents
19:21 Strands wrote its own TypeScript version

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,741 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1s)** [music] Hi everyone. Um, welcome, welcome. Agents that forge their own tools. What is so great about this? Can't your claw code do this? Or can't your cursor or your code editors, can't they all write their own tools? So what am I even talking about here? Why is this such a big deal? Right? Like any all of your agents can write tools by themselves. But how many agents do you know that can fix code at runtime? Let's say you've got something in production. It's running. Everything looks great, but

**[0:49](https://www.youtube.com/watch?v=33Oct2hqGnk&t=49s)** something is failing. Then what happens? you have to probably bring it down, fix it by yourself and then restart it and then work with your clot code or whichever editor you're using and then bring it back up, right? But imagine if your agent was smart enough to figure out, oh man, there is a bug here. Something's not working. I'm falling falling into an error. I need to fix myself. And it realizes what it can do to fix itself. Writes its own tools all writes its own agents and fixes itself. How cool would that be, right? And that's what I'm here to talk to you about today. Let me quickly show you a demo because I think I like leading in with demos so you know what you're getting into. So, let's start with that. Right. So, here I have a and you can see

**[1:37](https://www.youtube.com/watch?v=33Oct2hqGnk&t=97s)** my screen. I'm hoping it's big enough I can zoom in. Okay. So, I have a simple agent here called agents.py. This agent, we can go over the code in a bit, but this agent has nothing. It's just got it's just got a pretty cool system prompt and then it's calling the system prompt and it's got three tools and if you look at the tools package there are actually no tools files that are written. So technically this agent has no capability by itself, right? It shouldn't be able to do anything, right? All it should technically hallucinate because of the LLM that is running under the hood. But let's say I say something like okay so first I'm going to start running this. So we know it's running. Okay. So in runtime right now this is running. Now I'm going to say hey you

**[2:25](https://www.youtube.com/watch?v=33Oct2hqGnk&t=145s)** know what um help me calculate something uh some complex math equation right when I say this this agent which technically has nothing available is going to be calling the three tools that it's got and we'll look into the tools that it's got in just a bit and it's going to say oh you know what let me create a math calculator tool because that's what you're asking for. And it's not just going to create, it's going to let me use this tool that I'm creating right now at runtime without having to rerun it. So, okay. So, it's clearly gone ahead and created. So, let's look at tools again. It's created the math calculator tool and it's saying, okay, I do all these things. I've got min, max,

**[3:14](https://www.youtube.com/watch?v=33Oct2hqGnk&t=194s)** blah, blah, blah. It's gone and created this entire new tool. So, it's saying I can do all these things, right? So, let's say calculate uh oh yikes uh what's the square of blah blah blah some number right I'm just typing out a random number so now it's calling that math calculator tool that it just wrote by itself and it's giving me the answer not just that right so let's say I give it something completely out of blue and I say uh cool whatever count number of characters in my word. Okay. So then, so then it's like, okay, so it's going to check if it can use any of the tools that it's currently got access to. It doesn't. So what it's saying is, okay, let me write a tool to count the number of characters

**[4:03](https://www.youtube.com/watch?v=33Oct2hqGnk&t=243s)** you want because clearly it knows that it does not have the capability to do it. And so it's going ahead and it's creating a there we go. Even before I could finish speaking, it created a character counter for us. So, let's say um do it for this word. And it's not even a word. I'm just going to put random things. You know what? I should have actually done something that I could count so I can validate it. But the thing is it's calling a tool. It's calling the character counter tool and it's telling me that it's got 28 letters. Let's do it something we can test. So, I'm just going to do it for these three letters, right? We'll see if it knows. So, I'm not even telling it what to do. I'm just typing three letters. It knows that it has to do it and it's doing it. How powerful is this? So, what I want to leave you with today is show you how you can build something

**[4:52](https://www.youtube.com/watch?v=33Oct2hqGnk&t=292s)** like this where you can use it. I think it's pretty powerful and how we can implement it in our work day-to-day work. Very niche. So, now let's get down to the code. This is an idea called meta tooling. and I'm using an open-source framework called Strand Agents. And my name is Sandy and I work at AWS. And we at AWS built Strand agents as an open-source a aentic harness that you can use to run your LLMs with, right? And so, um, how show of hands, how many developers do we have in the room? A quick show. Oh, most of you. Brilliant. I'm talking to the right audience. If not, I will change things around a little bit. So, if you guys like getting into the code, I'm going to get into the

**[5:40](https://www.youtube.com/watch?v=33Oct2hqGnk&t=340s)** code with me. Right. So, the main thing we need here for agents and I have a slide deck that goes with it is we need just three types of tools. The editor, the shell, and the load tool along with the system prompt that lets us implement this function. So I'm going to quickly go to my slide deck that helps us understand this better. Like I mentioned, this is strand agent. This is our agentic AI harness and you can use your own LLMs, bring your own models. Another cool part because this is uh an harness is the fact that if let's say tomorrow there's a new the state-of-the-art LLM that comes out, you don't have to rewrite all of your system prompt. You don't have to rewrite the structure. You don't have to change your

**[6:27](https://www.youtube.com/watch?v=33Oct2hqGnk&t=387s)** entire architecture. you can keep it as it is and whichever model you use you can just replace it. So it also lets you experiment with model performance without really rewriting your entire architecture. So it's super super powerful. Supports MCP AA all of that cool stuff. Has a bunch of model providers. Um you can get started. So what do we do? Very simple right? Five lines of code. Uh import agent from there import shell. Shell is the very first tool that we need because we need to give it access to the directory. We need to give it access. It needs to know what it's running, where it's running, where your codebase is located. So that is just one of the tools that you need. And then if you ask it what can you do, it understands what's going on under the hood. So to techniques technically start

**[7:14](https://www.youtube.com/watch?v=33Oct2hqGnk&t=434s)** being able to use it on the fly, right? So then let's get into what I actually just built a couple of minutes ago and I showed you over here. What am I trying to do? The idea because this is communitydriven, AWS manages it and maintains it for you. People write a lot of pre-built inbit tools, but there's also community written tools. And so all you need is three tools to be able to start implementing matter tooling. So what do you need? First of all, you need to have a system prompt that tells your agent what a good tool looks like. How does that work? We have to start with the at tool decorator function. That's how it knows it's a tool. Excuse me. That's how it knows it's a tool. And then you tell it what a tool looks like

**[8:02](https://www.youtube.com/watch?v=33Oct2hqGnk&t=482s)** and where it should be stored, right? And so you call the system prompt there. That's all you say. And then you can give it access to different tools. I highlighted load tools from directory equals true because that is what enables you to enables the agent to start letting it run the tools that it's generated at runtime dynamically. And we later on decided we should just make this into a fun into a tool by itself. So now that's become the load tool. So now when you go and say hey create two create five new tools for yourself and start using them it's going to know what it's going to do. So let's go back to the code that I showed you earlier, right? Same thing. It's got the system prompt and here I'm saying you are the meta tooling agent that creates your own tools and custom tools at runtime. So

**[8:51](https://www.youtube.com/watch?v=33Oct2hqGnk&t=531s)** I'm defining the tool template and telling it what a tool looks like. I'm giving it the tool specification of what it's supposed to look like. And then I'm giving it rules for what it's supposed to do and where it's supposed to write into. And I'm also telling it always check if it if it exists or not. only if it doesn't exist then write a new tool and I'm telling it so I'm giving it three tools editor which allows it to write the shell tool which shows it what it has and the load tool which allows it to load from the directory the tool from the directory dynamically and this is all you need and it takes just one line of code right system prompt equals system prompt three different tools and this is just code so that I can chat

**[9:39](https://www.youtube.com/watch?v=33Oct2hqGnk&t=579s)** with it continuously. And so when I do this, it's actually able to start running create five random tools for yourself. And so it's going to start creating these five new tools. And the power of this is like I said, when you're deploying code into production, you need you might want a way to for the agent to be smart enough to figure out what's wrong and to be able to answer questions for itself. Let's say you're you're building this app that's supposed to book flight tickets domestically, but let's say you have one user who's saying, "No, no, I want a flight ticket from, I don't know, India to Hong Kong." And your agent gives up because it's not been explicitly programmed to do that, or it's not been trained to have access to be able to do that. But do you just

**[10:27](https://www.youtube.com/watch?v=33Oct2hqGnk&t=627s)** want it to fail? Do you want it to run into an error? Do you want to give it back to your deployment to your engineering team and have a turnaround of two weeks and then come back? No. You want to be able to solve it. So this is one of the ways by which you can handle that right. So again let's get back to the code and we have more cool things coming up. Now I was speaking about tools that can this agent that can write it own write its own tools. Can it also write its own agents? Yes it can. And I have another demo for that but wait until the last few minutes for that. Right. So when we talk about agents that write their own u agents also we want to understand agentic patterns. We have three primary patterns. The first one is swarm where you have sub agents that work with each other in parallel. So they work on a task in a combined

**[11:16](https://www.youtube.com/watch?v=33Oct2hqGnk&t=676s)** fashion and they take different parts of the task themselves. Then you have a graph where the result of one sub aent gets fed into the other sub aent and then there's a handoff and then you could also have workflows that have a combination of all of these. Right? So with the workflow, you could have a parallel set of sub aents calling each other. And then there could be nodes and graphs and all of that cool stuff. And so this and so they all of this can be created by just the agent itself. We don't need to. We can do it our own selves, but we don't necessarily need to. So um let's quickly go check how that looks. Um so this is the exact same thing. This is for my meta agents. I'm doing the exact same thing. I've given it three tools over here. I'm actually

**[12:04](https://www.youtube.com/watch?v=33Oct2hqGnk&t=724s)** if you look at my agents file, it's pretty empty and I'm saying agent as the tool file template. So I'm saying just break it into two to four sub agents. I'm keeping it simple. No swarm, nothing fancy here. Simple demo and use it. And this is the tool spec for what an agent should look like. And I'm happy to share the code with you after this, right? And these are the rules that it follows. Same thing, right? One line is all it takes. system prompt equals system prompt three tools and then say so I'm going to start running this now python 3 agent.py pie. And so I'm flying to Hawaii or whichever place to some uh to Hawaii. Let's just say Hawaii. Help me plan my itinerary.

**[12:54](https://www.youtube.com/watch?v=33Oct2hqGnk&t=774s)** Okay. So this is all I'm telling it. I'm not even telling it, hey go make your own agent or go create your own rule. This is all I'm telling it. This is how your customers would chat with it, right? they just tell them what their problem is and they expect you to figure it out. Right? So, this agent is going to be like, "Oh, great. Um, here I'm going to be printing out I'm going to be creating these into three focus sub aents. The flight agent, the activities agent, the itinerary agent, and it's calling the editor tool three times, one for each of these." So, I see that it's already created the activities. Yeah, it's creating It's pretty fast. It's creating the activities agent. It's created like a flight agent that's doing something. It's created an itinary agent. The let me call out that the one thing this can't currently do right now is access real-time information because

**[13:41](https://www.youtube.com/watch?v=33Oct2hqGnk&t=821s)** I've been given it a tool that has access to real world API. Right? So assuming you add that on you can ask it what's the weather like and it'll be like you know what let me write a tool that can always grab the latest weather in whichever location and recommend stuff. So based off of that, it created those agents. And if you look at it somewhere here, it should technically be calling those agents. There we go. See, it's calling the activities agents. And then it's saying these are the ma main airports. These are the best beaches. These are what it is, and this is what you have to do. And so how amazing is is it that you can now have your agent. So you now your focus is not just building a good agentic system that can get the job done. You would also maybe want to start thinking about healing, writing

**[14:29](https://www.youtube.com/watch?v=33Oct2hqGnk&t=869s)** self-healing code, about creating an agent that can sort of go over itself, look at what bugs are there and fix itself. Had this been a longer session, I usually do longer sessions. I usually ask the audience to ask it to do crazy stuff and I try breaking it. And what happens is this actually ends up breaking. you'll see a bunch of errors coming up and this thing is just talking chatting away. So I need to probably set the max token somewhere here but um and so it actually ends up erroring and breaking but it recognizes that it's erroring and it says oh man I'm ering let me fix myself and it would go and fix the same fix this exact same tool or agent that it's got here. So now if I'm like I don't want Hawaii why do you make it for Hawaii do for something else going to be like sure let me do it let me update the agent. So it's super super powerful. But then again we have to keep

**[15:18](https://www.youtube.com/watch?v=33Oct2hqGnk&t=918s)** in mind that this is just autonomously doing things by itself. With great power also comes great responsibility even greater responsibility. So what do we need to do with it? Right? We need a eval. What are some inbuilt evals that str agent has? We we have totally eight different evals. The first one is at an overall session level. We want to figure out if I told it hey book my flight tickets is it actually booking? Did it achieve the end goal? That is part one of it, right? End goal achievement. Second thing we want to look at it is at a trace level. Um was it actually helpful? If I say what is my balance and says my balance is 500 bucks, is that the expected type of answer? Part one. Part two, did it make up the answer? Is that the actual answer that you're supposed to get? You need to be able to

**[16:05](https://www.youtube.com/watch?v=33Oct2hqGnk&t=965s)** evaluate that. But it doesn't just end there. What about tool access? Right? What about did it use the right tool to get to that answer or did it use the wrong tool? And within that specific tool, did it use the right parameter? Is the account ID actually one two three or is it supposed to be is it messing up? We want insight into what is going on so that we can trust it and reliably give it access. Again, not just it doesn't just end there. We also want to understand inter agent dependency. When we're building multi-agentic systems, we want to look at the overall outcome and the overall response if it's the way you wanted it to be. You want to make sure that it's calling the different tools and the different sub aents in the right sequence. And you also want to take a deeper dive into what the messages, the

**[16:53](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1013s)** inter agent communication looks like and if that's up to the mark. All of this together gives us the full end to end agent conversation within our session. This gives us the insight. Again, this also isn't good enough, right? We want to make sure it doesn't cause undue damage. If this meta tooling or this meta agent can spin off tools and agents, it can also modify and delete. Do I want it to delete my data? Do I want it to delete stuff that I have put all of my effort into building? No. So, what do I do? I have to have guard rails in place. Four different types of guard rails. The first one is your environment. We need to make sure that we're sandboxing the environment. And when I say sandboxing the environment, it's not your typical sandbox where your agent is in one container and you're

**[17:43](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1063s)** protecting it from the rest of the world. We want the environment in which this code is executing to be sandboxed and Strands recently launched a feature about I think a few weeks ago where we can sandbox the code execution environment and that is what guarantees that it doesn't touch the rest of your code execution environments and it doesn't mess up everything else and it doesn't write into wrong places and delete from the wrong places. Right. Next we have to constrain the tools. We have to constrain permissions. We have to constrain the who's got access and who can ask it questions and what types of questions we need to ask and observability. All of your evals, your hotel, your telemetry, all of that data needs to be there in order to be able to

**[18:31](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1111s)** say that, hey, reliably and say, hey, I think I can go ahead and build an agentic system that can think for itself that it can do more than what it's just been set out to do because it can fix things when things are broken on the fly, on the run, and it can solve more capabilities than it has been initially taught to. This is the starting of self-improving agents and the self- evvolving agents. At some point, I'm convinced they will take over the world and I'm I'm going to be at risk. But until then, I think this is incredible. And if anything, if I want to leave you with anything, I would want you to I would want to leave you with a quick idea of where Strands is,

**[19:19](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1159s)** where Strand started with and where we are at now. We started with building their own tools. We we moved to getting them to update uh to create agents by themselves. Now it's at a point where they can update their own source code. Fun fact, we created Strand agents three years ago internally. It was supposed to be this internal thing before agents was even a thing. And it was so powerful that we said, you know what, let's just open source it and give it back to the community. And we wrote the Python version of Strands. And the Python version of strands wrote by itself the TypeScript version of Stand. So, it did update its own source code. It's pretty powerful. I'm pretty psyched. And if if this is my call to action, if uh this sounds interesting to you, reach out to me. Scan these and we can have a

**[20:08](https://www.youtube.com/watch?v=33Oct2hqGnk&t=1208s)** conversation later. I'm happy to share my slide deck and my code with you. Um and we can chat offline. Um thank you very much. This is my LinkedIn. Uh, we have 30 seconds to go, I think.
