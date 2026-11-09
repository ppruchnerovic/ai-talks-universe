---
id: 6TjFjHPjVH0
title: "I Let Agents Refactor My Codebase for 3 Weeks. Then I Read the Code. — Keiji Kanazawa, Microsoft"
slug: i-let-agents-refactor-my-codebase-for-3-weeks-then-i-read
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Keiji Kanazawa"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-11-09T03:30:09Z
video_id: 6TjFjHPjVH0
url: https://www.youtube.com/watch?v=6TjFjHPjVH0
youtube_url: https://www.youtube.com/watch?v=6TjFjHPjVH0
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# I Let Agents Refactor My Codebase for 3 Weeks. Then I Read the Code. — Keiji Kanazawa, Microsoft

**Keiji Kanazawa**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=6TjFjHPjVH0) · [Conference site](https://www.ai.engineer/)

## Description

A coding agent wired unit tests to production inference, then ran them about 30 times. Keiji Kanazawa had spent three weeks letting coding agents refactor a personal research assistant. A bad digest sent him looking for a trace, and he discovered the "agent" was still a deterministic workflow. Skills had no SKILL.md, different architectural concepts were aliases for the same thing, and a daily reflection job was producing empty reports. He had approved plans without checking whether the implementation meant what its labels promised.

He rebuilt around an explicit agent runtime, clearer specifications and goal rubrics, comparing four frameworks before selecting tools for his own needs as a product manager. The working example is a video deep dive agent that extracts 440 keyframes from an inference lecture, pairs blackboard equations with explanations and lets him question individual sections. The result generalizes to slide decks, coding demos and terminal recordings. He iterates on an evaluation rubric, lets agents optimize against it and uses adversarial reviews between coding agents. The rubrics need scrutiny too: one was tuned to a single lecture and failed on five other videos. His answer to the code reading debate is to own the goals and evaluation loop while continuing to delegate most implementation.

Speaker info:
- https://x.com/gojira
- https://linkedin.com/in/keijikanazawa
- https://gojira.blog/

Timestamps:
0:00 - Introduction
0:33 - The L/Z debate over reading code
1:56 - Building a personal research agent
4:00 - The agent that was not an agent
6:33 - Unit tests on production inference
7:59 - Rebuilding with clearer specifications
9:21 - Comparing four agent frameworks
12:04 - Video deep dives from keyframes
13:59 - Rubrics and evaluation loops
16:36 - Catching an overfit rubric
18:25 - Own the goals and delegate the code

## Transcript

*3,094 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=1s)** [music] All right, welcome everybody. I'm KG Kanazawa. I let my coding agents refactor my codebase for three weeks and then I read the code. Listen on for what happened after that. So most of you here in this track probably are aware of the local polo zer debate. How many people don't know what that is? Okay. So uh okay so oppo back in AI engineer Europe a few months ago he

**[0:52](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=52s)** works at openai. He uh said reading code the liability just spend billions of tokens to get stuff done. Mario Zechner at the same conference said read the [ __ ] code. Slow the [ __ ] down. Okay, so that's the LZ spectrum. How many people here are like on the L side? Who's on the Z side? All right, awesome. So I am very very much on the L end now. I'm a product manager. I also have a AI research background. I was started off as a dev. Um but these days I I work on product and back last December like a lot of people clock Opus 4.5 really amazing

**[1:42](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=102s)** moment right when things just started to work. So I have a day job that's pretty busy. I work uh at Microsoft uh work with the Frontier Labs, OpenAI uh and Anthropic to uh provide their models to the Microsoft customers. So, but I love to listen and watch the podcasts. I never have time. So, I I set up the you know a project to create some skills to download podcasts, transcribe them, summarize. Many of you probably done the same thing. But this project then snowballed. uh I added X threads. It would go and crawl X uh you know topics as well as the pages summarize all of those. I started to add I added a scheduleuler so we'll do it all the time email inbox like I could send links and

**[2:31](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=151s)** it would go crawl those links and send me you know kind of the summaries and then it kind of snowballed. It became what Andre Karpathy t calls an LLM wiki, right? And so, um, I basically at this point I realized this is no longer like a set of agent skills. This is my agent, you know, and so I decided, hey, I'm going to go full boore and I want to actually make rewrite this thing or or reorient this thing to be really agent scope. So at this point it's all kind of deterministic workflows. Download YouTube transcribe it step by step right but I also started to build some agentic workflows on top of that LLM wiki like doing deep research like doing daily self-reflection of my cloud code usage

**[3:23](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=203s)** and then creating skills out of that suggesting agent instruction improvements. So I said, "Hey, I wrote a spec uh for the agents and I said, "Hey, I want to have an agent runtime with a registry of agents that I create. They're going to run on schedules. They're going to do all the things that I wanted to do like the self-reflection monitoring this system itself." Um, and then I had by this time, uh, Codeex was taking off. So, I had Codeex and Claude kind of take turns implementing stuff, reviewing each other's code, fixing each other's bugs, and things kind of slowly started to work. One day, I read one of the uh digests and I realized it it wrote a sentence that really belonged in

**[4:11](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=251s)** another section of the digest, you know, basically kind of misattributed stuff. So, like a good AI engineer, I'm like, I'm going to go do some error analysis. I want to look at traces of the agent, what it did, maybe write some eval so it'll improve in the future. And I said to cloud code, hey, tell me for this particular session where the traces are. And cloud code says, you know what, we we don't actually have that because um it's not really an agent. And so, uh then I went and looked at the code in a little bit more detail. Um, and after a little while I said to claw code, you know what? I do not agree with this design at all and that I undoubtedly approved.

**[5:00](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=300s)** Okay, so I I had, you know, written a bunch of specs having it write a bunch of plans, right? And then it said the words like agent skills and I was like, okay, fine, you know, keep going. Uh, who has this experience? you tell an agent, you know, you want to do you want to do something and it's like, okay, fine. And then it's not what you asked for, right? So now, and so while I'm kind of like struggling with that, I, you know, then I go look at the code in a little more detail. Um, and so remember this is started off as kind of a deterministic workflow system, right? So it's got, uh, steps and it had actions which are like the YouTube download or transcribe, whatever. And then I had told it to add skills and actions, right? Agent skills. What you'll notice here is like it says

**[5:50](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=350s)** two things. Skills and actions are actually the same thing. And then agents are are something else. And when I go and look deeper, these are all like the same thing. So you know the they have these plausible names for these constructs in the system, but they weren't what they say they are. So like a skill was not really an agent skill. It had no skill.m MD. It had no scripts. The agents of again were not running on agent SDKs, right? And at this point, I'm pretty kind of like uh disappointed and and I'm kind of thinking, well, what am I supposed to do? So like uh as I've worked with a coding agent to try to fix things, next day I get a email alert from one of the token providers and it's it's basically

**[6:38](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=398s)** like this is like first week of the month. You have blown past what your normal budget is for the month. And so this is this is like $100, but it's like five times more than I was normally spending in a week, right? Um, it turns out Codeex a lot of people back when were saying, "Hey, Codeex is like the genius suite, right? It's the one that you want to give your coding jobs to. Maybe you have Claude create the plans and the designs, but you know, Codex is the one you want doing the coding." Well, Codex turns out it wired up all the unit tests to production inference. And over the, you know, the last day before I got that alert, it had ran like 30 cycles of unit test where it was burning production tokens. I also looked at some of the a you know

**[7:26](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=446s)** runs of, for example, the daily reflection agent uh that I've been running. That's the one that looks at my coding agent sessions and suggest improvements. It ran every day, but when I looked at the content, they were empty because again, when it was doing that skill action agent refactoring, it just completely broke stuff. So that none of the prompts are actually running to create what I had asked it to do. So what does somebody do at this point, right? I just start over fresh because at this point I don't trust cloud code. I don't trust codeex. I do not trust them to go and do a full refactor of this system because I had been telling

**[8:14](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=494s)** it to do it for the, you know, previous three weeks, right? And it didn't do a a particularly good job at that. So, I built a new head. I wrote a fresh set of specs. Again, I'm a product manager. I'm not about to go write this myself. I'm still going to use a coding agent, but I'm going to start fresh with hopefully better specs, some some rubrics in terms of giving the agents better goalposts of where it should aim for. Um, and I I wrote, you know, I created this new agent runtime. Everything is an agent. There's a registry of different agents. And what I ended up with looks, this is like uh almost 3 months ago. It's like what the all the coding age look like these days, right? So in the middle I give a coding agent SDK instructions on what I want built. That's kind of the

**[9:04](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=544s)** middle section that creates an agent that has a canvas that it can output uh you know what it's doing, right? So and remember the part where I'm like I don't trust cloud, I don't trust codeex. So I actually do a bake off. Okay, four different frameworks. For each one, I tell the coding agent, I want you to create this experience where I type into, for example, the cloud code. I would say I want you to build an experience where I type into cloud agent SDK that I interact with. It will create an agent for me. That agent will output stuff on the right. Right? So, I did that with four different ones. Each one differently. With codeex, I would say use codeex itself to to to create the

**[9:53](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=593s)** agents and then run the agents, right? So I settled ultimately on cloud code and codeex um co-pilot CLI. I work at Microsoft. I use it probably 90% of the time at work. The rest cloud code, it's really good. Copilot app, if you have, you know, we released it about a month ago, that's really good. Uh I I use it all the time. I really love it. For my personal projects like this one, I use cloud code uh and codeex. Pi is the interesting one. Pi is the framework. Who who knows what pi is? Yeah, pi is the agent framework that was written by Mario Zuckner, the guy who said slow the [ __ ] down, right? And so, u it actually is u this is the screenshot of the one

**[10:44](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=644s)** created by Pi. Pi did a really nice job. Really nice looking experience very very quickly. So I'm really impressed with it. One thing though, it asks me questions targeted at an engineer like Mario Zer. It'll it asks me things like hey you know the SQL light uh database that we have to keep track of all the agents well do you want to do this or that or like do you want to architect the TypeScript uh APIs to look this way or that way and these are like I don't know like I think this is like pi speaks like a love language for Mario Zechner right for like hardcore engineers it's not what a product manager needs to needs to like think about so I love it but it's not the one I'm

**[11:35](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=695s)** and I don't think it's the one that you know millions of people will be using to to build agents and run agents, right? So now that I got again, I started to build everything back, adding the transcripts, adding the summaries, adding email harnesses on top. I'll get back to this in a second. And as I'm writing it, so the YouTube stuff that I wrote previously, that was all text, right? It was just taking a transcript of the YouTube and then summarizing the text. I see this lecture float by on YouTube um or by Doresh Patel, his podcast or YouTube channel. There's this guy Reiner Pope who did a a lecture a blackboard lecture on LLM inference kind of the

**[12:24](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=744s)** math and and how you think about uh the workloads of LL inference on GPU clusters and I work that's that's my day job. So, I'm like, uh, roof line analysis. I really want to understand this stuff. And so, I decide, hey, this time I'm going to go not just do the text, but I'm going to go dig deep into the YouTube images themselves. So, I build a video dive agent where now I'm going to go, you know, basically take key frames out of the video for that video. I had like 440 of them. And then I use an AI eval rubric to get the best shots, pull out the blackboard equations, and then put them into uh a canvas that I can

**[13:14](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=794s)** explore that YouTube. This is how I do most YouTube these days. I don't watch the whole YouTube. I go to my system and look at the canvas of the detail. So, let me just show you uh what that looks like. See there's no audio but basically this is the summary of that YouTube where it it you know it breaks it up into chapters it shows the blackboard equations that's in the lecture it provides explanations for those and then I can you know jump to a a particular section of the YouTube I can highlight an equation I can start to chat with it uh or chat with the agent to say hey explain this part a bit better for me, right? And the way I did

**[14:02](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=842s)** this um is with a rubric. So with the eval framework so again I don't in the old um six months ago what I was doing was I was telling an agent to this is the spec for for your work. It creates a plan and I either approve it or I don't. Now I also tell it how I want the outcome to be. So the goal rubric for what the agent should work toward. So part in the particular case. So I really went deep on this particular YouTube because I wanted to get the system really really right so that does the right thing. Um, and it turns out this generalizes to other types of YouTubes, for example, AI engineer videos that have like u you know slides uh not just blackboards or

**[14:52](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=892s)** that have uh people showing off VS Code or cursor or something or terminals. So, it works on all of those. But to to get there, I went deep with this one video, worked on the rubric to say, hey, here's what I want from this canvas output. I want everything well explained. I want everything simple. I want to be able to jump to the right places in the video. Right? And this process itself was something that I iterated on. Now, these rubrics, guess who wrote them? AI agents, right? I did not write these rubrics. I directed the agent to say, "Hey, this is how I want the rubrics to be created." Um, and and it works great. Now you have to iterate quite a bit. But what I then what I do is I hill climb,

**[15:43](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=943s)** right? I set the rubric. I let the agents hill climb to optimize toward that rubric. Once it's done a pass to generate the canvas based on that then I go back and and and I see look for example if if there's something I don't like in the result canvas I go back and tell the agent hey let's change the rubric in a particular way because I want it to look like this. So in the very beginning what happens is all those blackboard equations they were just clumped together at the beginning and then I would see like a big wall of text. It's not what you want right so I you want the each equation accompanied by the explanation interle in the right order. So that's what I worked you know I I

**[16:29](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=989s)** basically told the agents to update the rubric to represent uh that's what I wanted. And guess what else? I caught the agents cheating again. So what happened was I I wasn't reviewing the rubrics completely either. It turned out the agents created one rubric that was really really just completely uh set up to succeed on that one RER Pope video. Uh so it was basically kind of benchmaxing uh you know kind of trying to game itself to succeed at that one video. But when I ran it on like five other videos, it didn't do well because it was just so tuned to that video that it it didn't do well. But actually, when when I told the agent to go fix it, you know, don't

**[17:18](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=1038s)** don't try to just game yourself to be good at that one video, it actually generalized better and it got overall better scores on everything. So yeah, and then so that's basically a loop, right? It's a it's a loop of um it's a loop of creating some rubrics with an agent. It's a loop of now once you've created a rubric it it uh hill climbs to get to the best uh best possible outcome and then I loop on top of that uh to to iterate on the rubric itself to improve the rubric uh so that the outcome gets gets better. So that's one level of looping. There's also other looping claude and codeex at this point. Remember the part where I'm like I don't

**[18:07](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=1087s)** always trust what they're doing. I have them check each other. Okay, like in these adversarial code reviews where I have them deeply look at what they're doing and then suggest fixes. And this goes for like several rounds. So another loop. So basically where I've landed at this point, I was all the way at L. I looked at the code, but I'm back double double down on L, right? I own the goal. I tell the agents what I want. I tell the agents how they should output, how they should work, but I still don't read the code for the most part, right? Um, it's definitely not every line. So, I'm never going to get to Z. Uh, I'm

**[18:56](https://www.youtube.com/watch?v=6TjFjHPjVH0&t=1136s)** always going to be on the L spectrum, right? And that's the right place for me. So, tokenaxing is what makes a product manager an AI engineer. And I want to thank you for being here. I want to thank everybody who creates the AIS and the tools that makes it possible for a product manager like me to create these experiences that I've wanted to build for years. So, thank you again [applause] >> [music]
