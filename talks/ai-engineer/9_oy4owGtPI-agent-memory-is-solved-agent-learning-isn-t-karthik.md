---
id: 9_oy4owGtPI
title: "Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte"
slug: agent-memory-is-solved-agent-learning-isn-t-karthik
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Karthik Ranganathan"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-05T14:00:20Z
video_id: 9_oy4owGtPI
url: https://www.youtube.com/watch?v=9_oy4owGtPI
youtube_url: https://www.youtube.com/watch?v=9_oy4owGtPI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "agent memory", "multi agent", "shared context", "agent learning", "context engineering", "RAG", "Meko", "Yugabyte", "YugabyteDB", "MCP", "Claude Code", "Codex", "AI infrastructure", "Karthik Ranganathan", "AI Engineer"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Prompting & context engineering"]
transcript: true
---

# Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte

**Karthik Ranganathan**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#agent memory` `#multi agent` `#shared context` `#agent learning` `#context engineering` `#RAG` `#Meko` `#Yugabyte` `#YugabyteDB` `#MCP` `#Claude Code` `#Codex` `#AI infrastructure` `#Karthik Ranganathan` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=9_oy4owGtPI) · [Conference site](https://www.ai.engineer/)

## Description

One agent can remember. A team of agents still can't learn together.

Karthik Ranganathan, co-founder and co-CEO of Yugabyte, explains why per-agent memory is a solved problem but shared learning across agents isn't. When one agent hands work to another, it passes on the output but loses the reasoning, the dead ends and the context, so the next agent burns tokens re-deriving it all. He covers five misconceptions about memory, what Yugabyte got wrong building its own agents, and how fixing its RAG pipeline one variable at a time took faithfulness from 14% to 82% with about one-seventh the context. Then Heather Downing demos Meko, Yugabyte's agent-native persistence layer, resuming sessions across agents and promoting private memories into shared data packs.

In this talk:
• Why more memory, shared files and bigger context windows aren't learning
• Shared context that's governed, promotable and traceable to its source
• How tuning a RAG pipeline cut context size about 7x while raising precision
• Demo: resuming and sharing context across Claude, Codex and other agents

SPEAKERS
Karthik Ranganathan, Co-founder & co-CEO, Yugabyte
X: https://x.com/karthikr

Heather Downing, Developer Advocate, Yugabyte
X: https://x.com/quorralyne

LINKS
Meko: https://mekodata.ai/
Meko docs: https://docs.mekodata.ai/
Meko skills (GitHub): https://github.com/yugabyte/meko-skills
Yugabyte: https://www.yugabyte.com/

CHAPTERS
0:00 Intro
0:12 Memory is solved, learning isn't
0:47 Learning happens in groups
1:17 Why a database company built this
2:02 A year of failing to ship agents
2:37 The real failure: lost context
3:27 The new-teammate problem
3:57 Five misconceptions
5:02 Shared, governed, traceable context
5:42 What we got wrong
6:37 Fixing RAG: 14% → 82% faithfulness
7:27 Introducing Meko and data packs
8:36 This deck was built with Meko
10:20 Demo: collective knowledge
11:25 Sharing context saves tokens
12:20 Demo: saving to a data pack
13:25 Demo: resuming in a fresh session
14:20 Demo: sharing with another agent
14:55 Private vs shared memory
16:15 Proving the token savings
16:45 Human promotion as a training signal
17:52 How the team uses Meko
19:26 Capturing tribal knowledge
19:40 Try Meko

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,819 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1s)** [music] Good to meet you folks. Thanks for everyone who's here. Um, today we're going to talk about sharing context, right? Everything in AI is about the data you give it. Bad data, bad outputs, right? Agent memory is a solved problem, but agent learning is not. And we're going to talk about not just like you know what we're building etc. It's about how why we built it and how we're using it for ourselves. Okay. So as we said agent memory works you know there's a bunch of stuff you feed it conversations etc. And you're able to extract memories from the conversation and agents are

**[0:48](https://www.youtube.com/watch?v=9_oy4owGtPI&t=48s)** able to reuse them. It's per agent. However learning is never done in isolation. It's when a group of agents come together and need to work with each other, they have to now start learning and sharing, right? And that is an unsolved problem because we're infrastructure people and infrastructure built for a single agent to do memory is often not the same infrastructure that is needed in order to learn, right? We're going to talk a little bit more about that. Okay, so by way of background, I'm Karthik, one of the co-founders and a CEO of a database company, Yugabyte DB, right? So what the hell are we doing here? Why are we building a aentic data infrastructure? What are we doing doing that? Right? We actually found this the hard way. We run agents for ourselves.

**[1:37](https://www.youtube.com/watch?v=9_oy4owGtPI&t=97s)** We run two agents internal to the company. Hagen for customer support and growth vector for a coordinated go to market between sales and marketing. And we run two agents externally for our customers and users. The first one is Perf Advisor, which is an agentic database admin, right? So it runs databases for our customers as a database company. Pretty useful. And Voyager, which helps them migrate and modernize from other databases to a cloudnative one, right? So four agents. We failed to ship anything and make it work at all. It was really hard. We've been trying for almost a year before we realized we were failing at the data problem right and if a database company is failing at a data problem be it for agentic it becomes personal right so yes it became personal we're like what the

**[2:25](https://www.youtube.com/watch?v=9_oy4owGtPI&t=145s)** hell's going on and when we then realized that a lot of people were asking us like yes we can do scalable vectors we can do scalable graph we can do scalable relational or people came to us and said more scale more performance less cost we're like wait a minute at some point this is ridiculous right it's breaking the laws physics. So what is the real failure? Right? When you cut everything o apart and just go to the core, it's because agent A, my agent is doing some work and I need to work with say one of you guys, say maybe Heather, right? My who's going to be showing a demo and I am not able to give that context. I'm only able to give the output. The output being an MD file, a PDF, a document, a something. But I'm not able to give the reasoning behind it. Right? So what does this lose? This

**[3:13](https://www.youtube.com/watch?v=9_oy4owGtPI&t=193s)** loses reasoning. This loses the deadends, the number of failures you've had before you actually succeeded. And it loses the whole context. Right? That means Heather's agent is going to be rederiving all of this stuff. And it's not for free. You're burning tokens and paying somebody else for it. This is the same as a group of humans working together. When a new person joins the team, they're going to be told, "We're going to do X." And they come up with 50 reasons why we should do something else. And each time, yes, we considered that two weeks ago, two months ago. That's not how humans operate. We actually bring the person in and says, "Okay, look, this is the context. This is the history of the project. This is how it's done. Now, let's go from here." That context is missing for agents. So, five things, misconceptions. Okay,

**[4:01](https://www.youtube.com/watch?v=9_oy4owGtPI&t=241s)** really quick. More memory. Agentic memory is not learning. It's just more memory, right? Like it's more expensive. Shared state is not shared knowledge. Just because you can share something with somebody else, like an MD file or something, doesn't mean you have shared knowledge. Rag transcripts, let me rag everything, is not equal to learning and quality. It just means there's a whole bunch of garbage there and now LLMs get to burn even more tokens to give you even worse results. Fine-tuning is not scalable. You cannot, you know, save and persist lessons that agents have come up with through fine-tuning and building custom infrastructure. And a bigger context window is the shest way to quickest failure in an expensive manner, right? Because it doesn't do anything. Your context rots. Every single one of these is a architecture gap, right? So

**[4:51](https://www.youtube.com/watch?v=9_oy4owGtPI&t=291s)** this is what we realized we needed to plug for ourselves, right? Right. And we've been finding a lot of users are are really enjoying and really liking this approach of thinking about context. Firstly, if there's a context that agent A can share with agent B, it closes the lost context problem. They're working on the same context. Second thing is this context can degrade. That means not everybody can contribute to that context. It's just like code. Not anyone can contribute. You need to go through a process of supervised promotion. And only then does it make it durable. And lastly, you need to be able to ask your the question, where the hell did this piece of information come from? It makes no sense at all. And be able to trace it back to something, a data source, a person, a conversation from which it was

**[5:39](https://www.youtube.com/watch?v=9_oy4owGtPI&t=339s)** extracted. And that's the first step to improving your context. So we started building this by assuming how hard can it be. So the first thing we did was it's just a knowledge base. We throw everything in the knowledge base. is going to be great, right? And how wrong we were. We built a whole distributed rag pipeline, extremely scalable, very elastic, amazing. It was just amazing, right? And it didn't do anything good for us. And then we said, you know what? This whole shared stuff doesn't work. We'll let every agent spin up a tiny database. We're a database company. How hard can it be? Tiny Postgress, make it efficient. Well, we realized that every repeatable workflow was being reinvented on the fly. Didn't work at all. And then we said, "Okay, fine. we'll just have some backend that does a whole bunch of processing and you know we'll just you know not even bother

**[6:26](https://www.youtube.com/watch?v=9_oy4owGtPI&t=386s)** with the UI cuz agents don't need UI and then we realized we couldn't tell what was going on. No human in the loop equals really bad results. Okay. And then we thought okay at least we have the rag pipeline. Well, it turned out even that was shitty because, you know, we took all the best components from the, you know, whatever the academia academia says and we put it all in there and we got poor numbers. 14% faithfulness using an MD benchmark, public benchmark, 20% on a PDF, 57% context precision using all of this other stuff. And when we actually started looking and tracing and doing our traces and tuning and experimenting, we realized a lot of things were off. And as we improved them one variable at a time, we were able to jump to 65 74 82. Right? And here's the kicker. Our

**[7:15](https://www.youtube.com/watch?v=9_oy4owGtPI&t=435s)** context chunks, which is the context size, went down from over 7,000 chunks to about a,000 chunks. So 17th the context size, a lot higher precision and a lot less money burned on tokens, right? So that's where Mako comes in. What is Mako? It's a agentnative persistence layer that takes all the mistakes we made and all the things we got right and puts it into one box. Right? And the way Mako works, it exposes a data pack, right? As a database company, we don't call it a database because it has multiple types of databases. Vector, graph, relational, no SQL, whatever, right? And what it does is stores aspects of the context, knowledge base, memory, conversations, observability, a lot more, right? And

**[8:03](https://www.youtube.com/watch?v=9_oy4owGtPI&t=483s)** what it enables is it enables agents to come in and push pieces of their context into a private space and promote that to a shared space, right? And then other agents or humans that come in can now go against that promoted highquality context and quickly retrieve stuff and you can now continue to add more people and more agents and do the handoff efficiently. Right? Hopefully that makes sense. Um the idea is take the durable repeatable workflows and make it infrastructure. Okay, before we go into a demo, right, a confession. This slide deck that you're looking at was built using Makeo as the context persistence layer, right? The way it worked was Heather, who's going

**[8:51](https://www.youtube.com/watch?v=9_oy4owGtPI&t=531s)** to give you show you the demo, actually wrote up an outline and created a data pack in Mako and simply sh sent sent me a share request, right? And she said, "I'm doing the demo. Here's the outline of my demo. Here's the rough talk track that needs to lead up to it because that's what makes sense." I took it and I'm I'm sure she used some agent harness. I don't know what it is. I really don't know. I didn't ask her. I didn't even have a meeting with her. She just sent me this. I plugged it into my cloud desktop and said, "Take this outline and break it down for me." And it gave me a few bullet points. This is what you're talking about. I'm like, "Okay, great. I want to change a couple of things." Changed a couple of things and said, "Here's the new outline. Can you build me my slide deck based on this?" And it did. And that diagram on the left, it built a really crappy diagram, right? It didn't look good at all. So, I said, like, you know what?

**[9:38](https://www.youtube.com/watch?v=9_oy4owGtPI&t=578s)** Everyone's saying this uh cloud design is the rage, so why don't I give that thing a go? And it actually did a better job. So, you know, there you go. That image came from cloud design. Everything else came from cloud desktop. Shot it back to Heather and, you know, Heather took the final pass over it to get hook it up with the demo and here we are. So, we barely talked, right? We didn't need to. We just shared context and our agents did the work and uh you know, you can go you can watch it. I think maybe I'll invite Heather to talk to this slide and and the thing after. I hope the demo's good because I haven't seen it myself. So, yeah. The idea is to watch collective knowledge grow over time, right? What Nico provides uh that I was able to use

**[10:27](https://www.youtube.com/watch?v=9_oy4owGtPI&t=627s)** for this is a resumability. So resumability I'm going to show you is being able to start a session and then kill it and then start it again with the same agent. Right now if you do it with something like cloud desktop, they have projects for this, right? Right? So if you do a cloud project, everything's together or if you turn on memory. But in this case, I guess like two months ago, I turned off all the memory on all of my idees because it doesn't matter what if I use something while I'm on the go, like a mobile app. Maybe I use chat EBT that isn't as sophisticated, right, as some of my coding idees. And so maybe I want to continue working on that topic. I can do that because all of the context is shared in our cloud now. And by sharing I mean that obviously chatbt is a different um agent but it's still my account so I should be able to get to

**[11:16](https://www.youtube.com/watch?v=9_oy4owGtPI&t=676s)** it right but because we're security focused and security minded we don't want like just any agent to get to it so I have to promote the kind of memory that that agent can also retrieve in like a collective pool and because you do this the cost itself goes down tremendously because the first time I figure stuff out I'm going back and forth with my LLM I'm burning lots of tokens to get to an end goal, whether that is code or it's just a knowledge work. But the next time that I want to retrieve it from another agent or another session, it doesn't need to burn through that. It just calls to the Miko memory and then it brings it right back with far less token. So, we're already saving a lot of token spend. The alternative to this would be to just again keep things in empty files or keep things where you have to constantly traverse with every single agent's LLM

**[12:05](https://www.youtube.com/watch?v=9_oy4owGtPI&t=725s)** and burn through tokens again and again in order to retrieve. Does that make sense? The difference here is just an MCP tool call. So to kind of prove that out because we have sensational internet here, I have recorded this for you at a little bit of a faster speed hopefully. All right. See this is resumability. So here I'm saying that I want to store um the conversation in a certain data pack, right? Let's call it the early access launch and I want to put a piece of information in it. In this case, um our signup emails failed. True story because we actually only used the SCS's sandbox instead of the prod. So uh we kind of went over the limit there when we were testing things. And that's a good piece of information for maybe our our ops team, right? So in this process, it's

**[12:55](https://www.youtube.com/watch?v=9_oy4owGtPI&t=775s)** calling data pack create uh because I've connected the MCP server to clot here and I've created a skill that will tell it what to do. You can decide how often you want it to call or if you just want to do it judiciously here. And so now it's storing the incident fact as a searchable memory with memory add. And then it's done now. So the data pack has been created. there's a conversation in there and it'll be retrievable in the in the future sessions. That sounds great. Awesome. Now I've killed that session and notice I'm not in projects. This is just a new chat window. Now I'm going to ask the same question so I can resume. Before I had to again have to make sure I turn on cloud memory or turn or put it inside of a project, but it's not in either one of these. I could be logged

**[13:43](https://www.youtube.com/watch?v=9_oy4owGtPI&t=823s)** in with the same account in like claw.ai, which would be technically a different agent. So I'm trying to prove that you can at least resume your sessions after maybe days with the same agent. So the fail result there was actually that it tried to search first instead of creating uh a conversation a new conversation here. We want to save everyone that we do. So it's the MCP server instructing to create a new conversation for it so we can store this. And see now they searched Mo and it found that hey this is what happened back in May and it was able to pull things back out. All right for sharability. Let's go ahead and get this done. If you notice this is a completely different IDE. In this case it's codeex. Um so

**[14:31](https://www.youtube.com/watch?v=9_oy4owGtPI&t=871s)** I've asked it questions like okay um do you have any known cause for the signup emails that are failing? And so it's gonna look and it's gonna look and it says, "Nope, I don't see anything. I don't see anything. I'm looking." Um, it did say that it saw that there was a brand new uh data pack that it's connected to, but it can't actually see anything. And why is that? Because I actually haven't shared that private memory from my claw desktop yet uh into a shared space. So right now, those memories are still private. If you notice the early access data pack is seen because I have connected it but I just haven't promoted it yet. So in that case I'm going to go to sign out. I'm going to sign in with my other account here to show you that yes I do have

**[15:20](https://www.youtube.com/watch?v=9_oy4owGtPI&t=920s)** access to this data pack and I need to promote that piece of memory into a shared knowledge space. Allow it to go ahead and and go through and then I it says it doesn't see it but I said well same question. Let's try it again. So, now that I've promoted it into that space, sped up for your pleasure here [laughter] because we all know how long-winded our LLMs can get. Um, now it can find that piece of memory. It can find the piece of memory because I've allowed that one piece to go. It's very fine grained. It doesn't have to be. You can open the whole data pack if you want as a maintainer to it, but this is much more ideal if you're just trying to give bespoke pieces of information, maybe best practices, maybe something that is

**[16:08](https://www.youtube.com/watch?v=9_oy4owGtPI&t=968s)** the ongoing process that you want to keep going. And then like the last part of this is the cost. How do you even know that it saves you tokens? If you go into your data pack, you can look at the conversations that are stored in there and how they were done because we give you embedded language traces for free in this. And you can actually look at the decision trace all the way down to the tool call and prove whether or not it called as much and burned as many tokens. Right? So, human promotions today kind of equal the training signal for self-improving orchestration tomorrow. Every human that says this is worth keeping is kind of a

**[16:57](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1017s)** labelled example of what good promotion looks like. So, you can actually start training maybe in the future an agent that's trained on your taste and your preferences long term. But right now, we're keeping the human in the loop. Those calls are just a signal, but this is actually how it starts to learn. The biggest lift that I saw is that when something goes wrong, maybe in a support situation, it's hard to constantly have calls call the same server that's down all the time and then it's tails all this time. Hey, do you know if this is down? Is that down? Slack starts blowing up. How do your agents handle that? They're all also wasting tokens calling the same thing. If they had access to the data pack, the first agent would hit it and then tell everybody that it happened and all the other agents would know that it already happened.

**[17:52](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1072s)** Yeah. So, yeah. So, thank you, Heather. Like, I think you know, pretty awesome demo. I think uh if you folks were following along what happened, Heather was was in charge of the early access and launch of Mako, right? and obviously used a data pack which is Mako to launch Mak Makeo right recursively and uh you know the first few people had a lot of trouble accessing their data packs on Mako and you know we you know she created a data pack for troubleshooting issues with Mako a different data pack and so that's the thing that she was talking about uh a lot of us in the company you know it's shared with us so we're all able to look at it load it into our agents and able to iterate with it the folks that are in engineering they load it straight into their you know cloud cloud code or codeex or like you know whatever the coding agents are

**[18:39](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1119s)** like I I myself more of a cloud desktop kind of user I use it for other things like you know some a user that wanted to get access couldn't get access apology email like go through cloud help me design it have a I have a data pack actually that is my voice of how I speak and same thing for posting on LinkedIn that thing can get tiresome if you want to keep writing it in your voice you know sometimes training a data pack for the context to do so will help so a lot of these things get automated straight away and it gets you know makes it much much quicker to assemble right and obviously if a new person comes into the team very easy to share this context with them have them get up to speed have them contribute to it either willingly or unwillingly right sometimes they're just doing things they don't even know and you extract patterns out of it oh this is really great we should make this a thing right so so like um yeah so I think these are some of the things

**[19:28](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1168s)** anyways I think the bottom line is we're trying to get it closer and closer to how humans work which is how can you capture tribal knowledge how can you share that How can you give controls over sharing and how can you actually tell what's going on? Right. >> Yeah. >> Um Yeah. So >> you should you should try it for free. >> Yeah. >> If you want. >> Yeah. Try it for free. Yeah. I think the left side is you know the website makeata.ai which will take you to a login. There's a free tier. You can sign up and just hook it up to one of your agents and you know get your agents to start learning right right away. And the right side is Discord. We'd love to hear from you if you do try it out. You know do drop us a note. We're working on improvements. That's how we communicate what we're building. So do join us on Discord, right? We'd love to see you guys there. So I think that brings us Yeah. Thank you. Thanks. Yeah, if we have Yeah, we're right on time actually. Yeah. So yeah, thank you. If you guys

**[20:15](https://www.youtube.com/watch?v=9_oy4owGtPI&t=1215s)** have questions, please feel free to connect with us on the site. Thank you. >> [music]
