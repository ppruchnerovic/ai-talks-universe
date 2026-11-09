---
id: u-o0sW9nwmk
title: "From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer"
slug: from-36-to-100-how-self-improving-agents-write-their-own
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Rafal Wilinski"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-07T14:00:10Z
video_id: u-o0sW9nwmk
url: https://www.youtube.com/watch?v=u-o0sW9nwmk
youtube_url: https://www.youtube.com/watch?v=u-o0sW9nwmk
tags: ["self-improving agents", "agent skills", "MCP", "Model Context Protocol", "skills over MCP", "AI agents", "continual learning", "agent memory", "knowledge management", "Voyager", "enterprise AI", "Runlayer", "Rafal Wilinski", "AI engineering", "AI Engineer"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer

**Rafal Wilinski**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#self-improving agents` `#agent skills` `#MCP` `#Model Context Protocol` `#skills over MCP` `#AI agents` `#continual learning` `#agent memory` `#knowledge management` `#Voyager` `#enterprise AI` `#Runlayer` `#Rafal Wilinski` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=u-o0sW9nwmk) · [Conference site](https://www.ai.engineer/)

## Description

When one agent finally cracks a hard problem, what if every agent in the company learned it too?

Rafal Wilinski, founding engineer at Runlayer, shows how to go from one self-improving agent to a self-improving company. He explains why skills matter more as agents work longer (a bad start can send them down an hours-long rabbit hole) and the three problems holding skills back: they're built for developers, nobody has time to write them, and many clients don't support them. His fix is to deliver skills over MCP from one governed server, then let agents write their own skills by distilling successful and failed runs, an idea borrowed from the Voyager Minecraft paper. In one test, a distilled skill took a task from 36% success to 100%. Multiply that across every agent and you get an organizational flywheel that keeps your hard-won knowledge even as models change.

In this talk:
• What skills are, and why they matter more as agents run longer
• Using MCP as the distribution layer for skills across the whole company
• Distilling skills from agent traces, and why failed runs teach the most
• The organizational flywheel: knowledge competitors can't copy

SPEAKER
Rafal Wilinski, Founding Engineer, Runlayer
X: https://x.com/rafalwilinski

LINKS
Runlayer: https://www.runlayer.com
Runlayer on X: https://x.com/runlayer

CHAPTERS
0:00 Intro
0:32 Every hard problem becomes a playbook
1:37 About Runlayer
2:12 What a skill is
2:51 Agents can now work for hours
3:51 Longer tasks, deeper rabbit holes
4:31 Skills nobody wants to rediscover
5:21 Three problems with skills
6:01 The risk of installing random skills
7:25 Skills vs MCP
7:55 MCP as the distribution layer
8:40 The Skills Over MCP working group
10:00 Self-improving agents
10:10 Voyager's skill library
11:34 Distilling skills from traces
11:59 Failures teach the most
12:54 Result: 36% to 100%
14:04 Frontier intelligence is rented
15:23 The organizational flywheel
16:38 Your real moat

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,960 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=1s)** [music] Hi everyone, I'm Raal. Today I want to talk about self-improving agents but not in a single player mode where just one agent gets smarter. I want to talk about how we can apply that concept and mix it with network effects to get a self-improving company or maybe even an enterprise that self-improves while you sleep. Um, imagine the best engineer you ever worked with or a salesperson or a lawyer. Um, the one that every time they cracked a genuinely hard problem, they wrote down exactly how they did that and handed over the playbook to the team. So

**[0:50](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=50s)** whenever they face a similar problem, they don't have to figure it out from the scratch, right? And imagine that happening for every hard problem across your whole company and that happening automatically uh each time. That's a dream, right? But it almost never works that way. Um even when you crack a really hard problem um often times the knowledge um all that debugging um all the all the reasoning behind that is just gone. Oh sorry um all that all that reasoning is just gone when you move on to the next the next task or close the session. But I wanted to convince you that this is actually possible and we already have all the primitives in place to make it happen. If it sounds interesting, let me try to

**[1:38](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=98s)** introduce myself once again. Hi, I'm Rafal. I'm a founding engineer at rum layer. We are making the golden path for AI at your company. Before that, I was leading Zapier agents and different AI teams. But generally speaking, my previous work was about making agents not just flashy demos, but reliable things in production. Um before we go into interesting parts, I want to break down my topic into three separate pieces and start by just improving agents. There are many ways to do that. We can use better models. We can use better prompting tools, harnesses and whatnot. But I want to focus today only just on skills because they are super accessible, right? At least in theory. um to make sure that we are all on the same page. A skill to me is a playbook that essentially agent can

**[2:27](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=147s)** read um when it thinks that the knowledge is relevant from the technical perspective that the term is called progressive disclosure and it means that at the very beginning the harness or a client sees just a summary of the skill or a short description of the skill. But when it thinks that the knowledge inside the skill can be useful, it can read the whole of the skill, inject it to the main context and based on that knowledge, it can change the trajectory of the agent. Why is this so important? Well, if you haven't been living under a rock for the past 6 or 12 months, your workflow probably has changed a lot. Uh, and that's because the agents got so much better. Actually, the models got so much better. And and it's not just vibes, it's measurable. Um here you can see a chart that probably you have seen

**[3:15](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=195s)** too many times already. For those who don't know, it's meter benchmark. It measures for how long agents can work independently while still having a decent chance of completing a task. And the word chance is essential here. Um we are going to go back to in a moment. But the trend is clear. The frontier capabilities, the frontier intelligence is getting better and better. They are better at multi-step deep work. There's only one caveat if that frontier intelligence is not being taken from you. And I'm fable probably just like you. But there is a catch. With great power or long task horizon comes great responsibility. If an agent can reason for much longer, it also means that it can dig a really really uh deep rabbit hole. um it can spend hundreds of tool

**[4:06](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=246s)** calls trying to defend a wrong thesis reason for hours and the next agent can do exactly the same thing or maybe even do something wrong worse. Um so the initial trajectory matters a lot and that's why skills are so important because they guide the agent towards the right target otherwise you'll waste time, you will waste tokens and most importantly you'll also waste money. Um, valuable skills are the rituals that nobody wants rediscovered. That knowledge is often not glamorous. It's probably deeply embedded within your company. And if agents would try to rediscover that knowledge from scratch, like for instance, the sequence of scripts and feature flags in order to make a nice roll back or what's the exact wording and language to use when dealing with that pesky uh enterprise

**[4:56](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=296s)** customer that's about to churn. Um, yeah, if agents would try to figure out that from scratch, they are likely going to fail. And often times that failure can be really costly. That's why I believe so many AIP PCs are failing because you're not giving agents the relevant context and the playbooks how to act within your company. So SKS are great, but I feel like they are not problem free. Um there are three most important problems and the first one is that they are local first and defcentric. What I mean by that is that um when you look at the skills ecosystem, you're going to find uh markdown files, JSON files, CLI commands, git repositories, and if you're a developer, that's great. But if you're um adop uh VP of AI or AI

**[5:46](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=346s)** adoption lead, you need to think more empathetically about how you can roll out the AI strategy across your whole company, which includes nontechnical people, right? And the challenge here is how nontechnical people can actually create and share uh the skills. Uh I love this meme. Um this is the junior developer or nontechnical person discovering command npx skills which is the most important the most popular command to install them. That's the only command I know that installs just uh not just a skill but also free prompt injections. um a wild script that requires root permissions and someone else's API key all in one run. Trust me at run layer we are scanning thousands of skills every day and there is really weird stuff inside.

**[6:35](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=395s)** Okay. Second problem is that I think we all like we all love the situation where we are facing a hard problem and there's already pray on how to deal with that situation right but often times there's there's no playbook right because it time it takes time and effort and intention and energy to reflect on a problem and leave something useful for posterity behind and the third problem is that not every LLM client support skills right if you're in cloud ecosystem, it's probably great. If you're a developer, you're probably going to manage even if the skills support is weird depending on which client you're using. Um, and once again, if you think about marketing, HR, legal, finance, those departments are probably still using chat GPT or some other weird LM client and skills might

**[7:24](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=444s)** be not supported there. And sometime ago, there was this big heated debate when the skills were introduced. Um, some people proclaimed that thank god MCP is finally dead because I'm not interested in dealing with oath. I can now hardcode a bunch of CLI commands. Um, hardcode my API key inside markdown file and call it a progress, right? Um, but I think everyone missed the point. Skills can be delivering um the knowledge how to do something and tools gives us capabilities. Tools from MCPS give us capability to do those things. But MCV can be also used as a protocol to deliver the knowledge to deliver the skills. We can use MCP as the distribution layer. So instead of installing skills locally, you can create a remote MCP server which

**[8:13](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=493s)** can become the source of truth across your whole company. Clients can connect to that. They can they can search for the right skills. Uh server can enforce the policy and make sure that everyone gets the best version of the skill possible depending on a query. and for instance the role that they have assigned. We've been doing that internally at run layer for the past 6 months and it's been working quite well. Um but it's no longer just an internal thing. We see that the broader MCP ecosystem is also going that direction. Um there's already a working group called skills over MCP and while the exact API is not final direction is clear. MCP can be used to deliver the skills to deliver the knowledge across your whole company. Um yeah and while the official spec is leaning towards MCP resources the

**[9:02](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=542s)** support for resources is also mixed. So we are going with tools. Um and yeah if you remember the problem the first problem I mentioned and the third problem I mentioned which is um the problem that they are defentric and the lack of uh support for clients. MCP as a distribution layer fixes that because it's unified in and works in almost every single client, not just developer clients. So the problem of devel of distributing skills to nontechnical people is essentially solved, right? Plus you have now a centralized API. So as a VP of AI or like AI adoption, you have one place to govern and manage what's the knowledge that's getting shared and distributed across your company. Okay. So now we know how we can improve

**[9:49](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=589s)** agents because we have um skills. We know that we can use MCP to distribute those skills across all the clients and agents. But let's talk about something more interesting which is how agents can improve themselves. And whenever I uh see a new paper or a framework speaking about this topic, I always go back to um Voyager paper. Unfortunately, you cannot see the video, but it's Minecraft gameplay in in background. So in in 2023, right after GPT4 was released, so ages ago, the question was for how long multiple agents or harnesses can explore Minecraft space, right? Um they dropped the agent into Minecraft with no instructions. They set its own goals. Agent just kept getting better without even touching the weights or or model

**[10:38](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=638s)** and the prompts. And in 2023, I think it was pretty groundbreaking. How did they pull it off? Um the key thing to notice here is the skill library. So Voyager did not just explore the Minecraft space care carefully and throw the trace away. When the agent figured out something um it saved the recipe as a code that uh that consisted of the tool calls that lead it that lead the agent to the discovery. So later on when the agent decided that hey I need to create a a crafting table or a diamond pickaxe it didn't have to figure it out this whole knowledge from scratch. It could simply go to the skill uh library and retrieve it as a code as a recipe um that can be reused. And this is really important. This is the core idea that I want to

**[11:27](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=687s)** carry forward is that um exploration should be turned into reusable procedural knowledge. And we started doing something very similar at run layer. Um we let the agents do the real work. And when the run succeeds and when there is something interesting in this run, there's multiple tool calls. Um we just take that trace and we ask Frontier LM to simply distill a skill, right? And while it's super simple to distill a skill from a single run, um I think we humans and agents learn the most from mistakes, right? The real sharpening happens when the agent fails. Um so a roundout goes sideways is actually the richest signal that you can get because

**[12:15](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=735s)** it exposes the missing guardrail, the missing library, some kind of edge case that you haven't thought about up front. Um and every run or or pass or fail just feeds our distiller mechanism constantly making our skill better. Um the successes are making the skill more trustworthy because if the agent achieved the goal it means that hey this skill works and if it doesn't it actually makes skill more robust because now we know what's missing in here and it all happens completely autonomously asynchronously without human in loop and the initial results were great uh we had uh this task of trying to run some chromium fork inside AWS Lambda and we were trying to do that using sonet 4.6. So not the most intelligent model but

**[13:03](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=783s)** sometimes it succeeded. Um but it was just you know it's not production ready to have 36% success rate. Um so what we did is we flipped the flag for self-improving agents. Um and once in one run the one of the agent invocations cracked the code our skill distiller create a reusable skill. It was uh then included in all the future runs and the success ratio went to 100%. So yeah, that's great. It's like a developer with better attitude towards documentation. Um and the success rate is the easiest number to show. But good skill is narrowing the search space. It makes the agent uh it narrows the search space and agents starts doing uh stops doing tool calls and it's exploring less branches.

**[13:54](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=834s)** it's w w w w w w w w w w w w w w w w w w w w wing less tokens and and less money. But putting savings and accuracy aside, I think there's also a deeper reason why you should be distilling skills. Um the problem is that frontier intelligence is rented or borrowed. It can disappear. I think yeah, we all miss Fable. It was a great model, right? It can deprecate it or it can get dumber. Like we complain every single day on Twitter, on Slack that Opus is really dumb today, right? So while we have the access to the best version of that intelligence, we should be using that to discover and persist those use useful procedures. We should be building a catalog of how the works gets done inside our company as a collective subconscious. And how we do it? Well, I believe we

**[14:45](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=885s)** already have all the pieces of the puzzle here. Um, we have skills as a way to retain procedures and improve agents and guide models. We have MCP as a unified distribution layer for those skills. And we also have a central repository, the knowledge base for all of those skills, which is constantly being updated and fed with new data. Um, yeah, we also have the continuous learning flywheel for one agent. But what's interesting is what I promised you at the very beginning, the network effect. Um, so what happens when you multiply that by every agent and every single client in the entire company? At run later, we call it selfimproving organizational flywheel. Um, we group a bunch of similar runs and try to distill a skill. It passes through our various

**[15:35](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=935s)** series of checks like whether it's not containing some kind of prompt injection or maybe PII um and bunch of other stuff. Once it's good, it's landing in our skill library and thanks to our MCB gateway, it's being served to each and every client and agent within the company. What we end up having is a constantly evolving knowledge base which is always up to date, continuously updated with new alpha fed with new age edge cases. So once one agent figure outs a really hard problem, it's getting distilled into a skill persistent in all or organizational library. So whenever someone else um has the same problem in the future, they don't have to figure out the solution from scratch. They don't have to know uh what's the exact sequence of this magical commands

**[16:24](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=984s)** that are going to restart the database or roll back the production. They can simply um reach out to the playbook. they have. And why is this so important? Because I believe like 50% of us probably already had an existential crisis thanks to the models. And the thinking goes along the lines of u okay so models are becoming commodity. Everyone here has access to them. Um cost of software is going to zero. Everyone is can be rebuilding my product. Um at least on the surface. In fact, so many people are walking today across the expo and they are thinking, hey, everyone's building the same thing, right? So, what is my moat? Um, and I believe the mode can be in building this flywheel and distilling the knowledge

**[17:14](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=1034s)** through this flywheel because it's like your own hard one lessons distilled governed of how your company uh does things you know and it's captured compounding raising the floor for everyone across the company giving them access to the best knowledge available. Um, it is also a way to be resistant against model intelligence deprecation and it's a great way to lowers your costs without ever changing a model. So yeah, that's probably one thing that competitor can't copy your internal culture and your identity and yeah that's pretty much it. Uh, thank you for coming if it resonated with you. I'm Rafal. I'm working at run layer. We're figuring out the AI golden

**[18:05](https://www.youtube.com/watch?v=u-o0sW9nwmk&t=1085s)** path for you. I'm open to talk about skills, MCP agents, whatnot. And this is exactly what we are building at run layer. Thank you. >> [music]
