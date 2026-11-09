---
id: BTtyguoPvBU
title: "How One Founder Manages 20 AI Coding Agents at Once - Ryan Carson, Untangle"
slug: how-one-founder-manages-20-ai-coding-agents-at-once-ryan
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ryan Carson"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-11-09T18:00:27Z
video_id: BTtyguoPvBU
url: https://www.youtube.com/watch?v=BTtyguoPvBU
youtube_url: https://www.youtube.com/watch?v=BTtyguoPvBU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Ryan Carson", "Untangle", "coding agents", "Devin", "agent management", "cloud agents", "multi-agent", "merge queue", "hiring engineers", "AI startups", "legal tech", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Enterprise adoption & strategy"]
transcript: true
---

# How One Founder Manages 20 AI Coding Agents at Once - Ryan Carson, Untangle

**Ryan Carson**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Ryan Carson` `#Untangle` `#coding agents` `#Devin` `#agent management` `#cloud agents` `#multi-agent` `#merge queue` `#hiring engineers` `#AI startups` `#legal tech` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=BTtyguoPvBU) · [Conference site](https://www.ai.engineer/)

## Description

Ryan Carson, founder and CEO of Untangle and a four-time founder, shows how his team runs software development with agents in the cloud. One "engineering manager" agent, which he mostly talks to by voice, manages up to 20 builder agents through a ticket board, with an automation that checks every builder every 15 minutes, capped review loops, QA agents and a merge queue manager. The human step he won't skip is watching the video of each feature before it ships. He also explains how Untangle now hires: candidates record themselves shipping a real feature with an agent, an agent ranks the videos, and the top five do a paid trial.

Chapters:
0:00 Intro
0:12 What Untangle does
1:02 Managing agents like managing people
1:55 The org chart in the age of agents
2:40 Talking to your manager agent
3:29 One manager, 20 builders
5:05 Review agents and QA
6:24 Watch the video before you ship
8:22 Stop coding locally
8:43 Running it across a team
9:46 The merge queue manager
11:07 How hiring changes
12:24 Ranking candidates with an agent
13:24 A paid trial project
14:50 Wrap-up

Ryan Carson

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,886 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=BTtyguoPvBU&t=1s)** [music] >> So my name's Ryan Carson. I'm the founder and CEO of Untangle. So we're building an AI paralegal specifically for family law focusing on divorce in particular. So quick audience poll. Who has been divorced? Raise your hand. Raise it. Don't be shy. Raise your hand. Who's been divorced? Okay, keep your hands up. Who knows somebody that's been divorced? Raise your hand. Everybody. Yeah. So for you watching the video, everyone raised their hand by the end. Divorce touches a lot of people. Two of my sisters got divorced. My parents got divorced and it's one of the most painful things in your whole life and I wanted to work on that problem and

**[0:48](https://www.youtube.com/watch?v=BTtyguoPvBU&t=48s)** just make it a little less painful. Started off as a consumer app. Quickly pivoted to B2B and we sell to family law firms now and thankfully product market fit is there and we're growing really fast. So that's really fun. So I've built and sold four companies. My last startup we scaled to about 110 people and I learned a lot about managing people and it turns out managing people is like managing agents. And so I'm going to share with you how we manage agents at Untangle and how everything I've learned managing people kind of fits there. So I'm hoping to teach you some of those things. I'm also going to show you how we hire. I think hiring is very different in the age of agents. I've hired a lot of people over my career. I've made a lot of mistakes and I'm going to share how we're hiring now at

**[1:35](https://www.youtube.com/watch?v=BTtyguoPvBU&t=95s)** Untangle and I think how it's really working. And then I'm going to show you a live demo. So let's get started. This is me on X and this is Untangle if you want to know more about us. If my little clicker works, you can do it. Okay. So what does the org chart look like now in the of agents? How do you run your agents? Um, so the way we do it is pretty straightforward. So we have humans at the top, um, and obviously we set priorities, we talk to our customers, we're doing all the human stuff. But what we use are manager agents, and these are literally just sessions. So we use Devin, love Devin. We do all our engine in the cloud. Um, I've done [clears throat] everything, you know, from coding by hand to, you know, using

**[2:24](https://www.youtube.com/watch?v=BTtyguoPvBU&t=144s)** cursor to here and we're in Devin. But we have a manager session and I'm going to show you this. It's literally just a session. I I call it engineer manager, um, and it never writes code. And I mostly talk to this agent, um, and it manages a bunch of children. So I'll talk to you about how we do that. We also I mostly use audio to manage this agent. Um, I don't know about you, but I'm not a fast reader. I'm definitely not an agent and I prefer audio. I can ingest audio a lot better for some reason than reading. So I talk mostly to my manager agent over audio. I'll show you that. Um, I just find it I I can absorb it. I can understand it. I can see what's happening. It's much more natural. So I'm going to show you that as well. Now the manager agent uh primarily works from a ticket board. We use linear.

**[3:12](https://www.youtube.com/watch?v=BTtyguoPvBU&t=192s)** Doesn't really matter what you use, but this is kind of the source of truth about what needs to be built. Every ticket should be one PR, um, which is how we we work and that the manager agent knows which tickets to pull based off dependencies. It's like pretty basic engineering manager stuff here. But this is where it gets interesting. So each manager agent uh concurrently manages up to about 20 builder agents. Um, this number varies. Like it can go anywhere from five to probably 25. Um, this is somewhat bottlenecked by your ability to talk to the manager agent and understand what's happening. Um, uh I think if you push too hard on this, you you quickly spin out of control. Um, I find we can concurrently manage about 25 builders. Um, now the key here is

**[4:00](https://www.youtube.com/watch?v=BTtyguoPvBU&t=240s)** that the manager is talking to these builders. You never go into these sessions. You never talk to them. You never manage them. You never do anything. Um, it's all done through the manager agent. And usually what it's doing is answering technical questions that don't I don't need to answer um or unblocking small things. Um, I also have an automation that forces the manager agent to read all the children sessions every It's like every 15 minutes. It says 10 but I've decided 15 is about the right call. You You You have to You have to build an automation. You can't trust your Android manager your manager manager manager agent to do this, right? It's not deterministic. So this is basically a script. Again, in Devin, it has automations. You just tell it, hey, every 15 minutes, go read every single child,

**[4:47](https://www.youtube.com/watch?v=BTtyguoPvBU&t=287s)** push things along, keep things moving, right? Um, and then any questions go back to the manager agent. So who's tracking so far? Do you understand what I'm saying? Okay, good. And probably a lot of you are doing this. I'm not claiming this is rocket science, but this is what we're doing right now in prod and it's working right? Um, each of these builder agents uh has a uh a review agent that it calls upon. Um, Devin has built-in reviews. Probably every code harness you have has built-in reviewers. Um, we typically stick to a three uh review max where uh we allow the builders to loop about three times with reviews. If they still have any important bugs that have been fixed after three, then they bubble that back up to the manager agent. And if the manager agent needs to, it bubbles it back up to me, right?

**[5:34](https://www.youtube.com/watch?v=BTtyguoPvBU&t=334s)** Um, that seems to work pretty well. Okay, so what's happening under the code under under the hood here? Like all the normal stuff, right? You've got code plus tests. You've got a QA agent. This is actually an additional uh process that we run. Um, it actually spins up a child of the builder to run QA. Um, y'all, this is cheap. Like you should be spinning up as many agents as you can as long as you're not holding up your merge queue, right? So I This works well for us now. Um, uh uh a wonderful engineer named Dale recently joined. He helped install this QA process. I think it's working pretty well so far. The thing that you're all going to encounter is just merge queue slowdown. Um there's this fine balance of just you know pecking your PRs to death um versus just getting them merged, right? Um

**[6:24](https://www.youtube.com/watch?v=BTtyguoPvBU&t=384s)** the other thing I love love love love is videos. So Devon has this built in. Um if not, you should build this. Um it's hard. Um every builder records a video of the feature being used and passing tests. So if it's a UI facing feature, you've got to look at it, right? Um this is how we know that what we've built looks good, how it works, right? So in Devon, it's a built in feature. It's called test and basically it it builds test cases and then it records a video and it gives you greener or red on those on those tests. And if you get a video that's all green, you can watch it and know what we think is happening is happening and visually it looks good, right? So this is the human in the loop where a human has to say ship it. So the manager session will will let me know

**[7:13](https://www.youtube.com/watch?v=BTtyguoPvBU&t=433s)** there's a video ready for you. Watch it, right? So I watched the video and this is the hard part. You've got to zoom in and understand like what is this PR doing? Um what am I watching? Um so I usually read a summary of like what is this thing? What is this supposed to do? I watch it and I engage and I would encourage you. This is the part where you want to cut corners. You got to watch the video. Like there is no this is the part of the bottleneck you have to engage in as a product owner. Um got to watch the video. Got to pay attention. Usually has to be on your laptop. Um I I I this literally before this talk I was on my phone, you know, talking to my manager my manager agent and it said there's a video for you. I watched it and I just couldn't see it well enough and I was so [snorts] tempted to be like it's okay. Ship [laughter] it. Like no. Get back to my machine. Watch

**[8:01](https://www.youtube.com/watch?v=BTtyguoPvBU&t=481s)** the watch the video. Um this is working. Like you know we we ship a lot of PRs uh at high quality this way. We've iterated, you know, hundreds of times on this process and I I feel pretty good about this. Now, this will change tomorrow [laughter] and probably will be useless a week from now, uh but it works well today. Um uh the thing I will say is like if you're coding locally, stop. Like you really need to be coding with a a cloud agent. I I don't care if it's Devon or whatever it is, but if you're running local dev, you are screwing up. You're holding yourself back, you're holding your team back, you're holding everything back cuz you can't do this. Um so that's where we're going and I feel strongly about that. So how does this work at scale? Well, you know, say you have 10 folks um uh in the who are working on things,

**[8:51](https://www.youtube.com/watch?v=BTtyguoPvBU&t=531s)** typically they'll have an engineering manager uh session each. Sometimes they'll have two, like right now I have two running. Um and what's beautiful is that these things talk to each other. And so uh again in Devon this is built in, it's probably built into whatever harness you use. The sessions all need to be able to talk to each other and they all need to know who each other is, right? And they're really good at this. Like this is such a delight. So what you'll see if if you if you zoom into any sessions, they're messaging each other, it's clear, it's straightforward, it's fast, it's good. Like you should be allowing your sessions to talk to each other. Um and again, if you're not, you are holding yourself back and you're probably shipping worse software. Um so they all talk a lot um and it's

**[9:38](https://www.youtube.com/watch?v=BTtyguoPvBU&t=578s)** not chit chat or stupid stuff. Like this is important stuff that they need to know to unblock each other. Um which is very useful. However, you still need what we call a merge queue manager. Um so this is how we coordinate this just wave uh of PRs that come in. You know, you have things like database migration numbers. These need to be coordinated. Like if all the agents are trying to grab these things, you constantly collide, right? So the merge manager just helps all that go away. It also is a little more intelligent about how the merge queue is happening. So, this is really nice. Um, it's working well for us. And again, these are just sessions. This is not like something special. These are just sessions in Devon, and I and I I name them so I understand what's happening.

**[10:27](https://www.youtube.com/watch?v=BTtyguoPvBU&t=627s)** Um, and it's pretty straightforward. You know, the talk from the gentleman from OpenAI, you know, said basically you got to unhobble. Just unhobble the thing, right? So, set up the roles and then unhobble the model, right? Um, and I think just having a merge manager say, hey, make all this better, uh, really works well. All right, who's tracking so far? Good. Who thinks this is Raise your hand. Oh, one guy. Two. Wait, one? Come on. People are brave. I already we have to talk afterwards. Where where are you? Um, okay. And then we use GitHub merge queues. That's fine. It's not rocket science. It works pretty well. So, All right. Next up, how we hire. Um, so who's hiring engineers or employees right now? Raise your hand.

**[11:14](https://www.youtube.com/watch?v=BTtyguoPvBU&t=674s)** Yeah, decent number of you. Um, I think everything has changed. Every everything you used to do about hiring employees is over. And none of it makes sense. Um, it's all outdated, and I would encourage you to do something like this. So, we don't do number one, any sort of pre-screens. We don't do any video chats. We don't do anything with people, um, it for most of this process because it will bias you. You'll like their hobbies. You'll like the way they talk to you. You'll think they're interesting, and it's all noise. None of it is signal, right? All that matters is can they operate an agent, right? Can they do that? So, the way we do that is we ask candidates to submit a 45-ish minute video, whole screen recording,

**[12:01](https://www.youtube.com/watch?v=BTtyguoPvBU&t=721s)** um, and we ask them to ship a feature, PR typically, on a app that they already maintain. And we just we just ask them to record that. No instruction, no guidance, no nothing. And just want to see like how good of an agent operator is this person, right? So um that is free. We don't pay for that. That's basically how you get in the door. Um and what we then do is we feed these videos into a ranking agent and basically say watch the video, watch the transcript, stack rank these people. Um now this what's interesting is I did this and I didn't trust it the first time. I didn't like what it said. Um and what's ironic is it actually was correct. Like the person that was number one I I should have hired them. Um but I didn't trust it cuz I was I was

**[12:50](https://www.youtube.com/watch?v=BTtyguoPvBU&t=770s)** biased. So you stack rank them. Now this is just a lot of video to watch. You could watch all these videos if you want. If you have time, do it. But I think you'll find actually a very intelligent model is pretty good at understanding like how how good is this person. Um what's interesting though is uh candidates will mumble um or uh sometimes or they won't think out loud, which is kind of fascinating so you can't really tell what they're thinking or doing. Um which is interesting. So that's something to sort of note. Um and some talk a lot. [laughter] So you never know. Uh then we basically pick the top five and we invite them to a paid project. So we pay them a fixed fee for 16 hours of their time. We actually give them a seat on Devin and we ask them to uh to get a real PR ready for merge.

**[13:39](https://www.youtube.com/watch?v=BTtyguoPvBU&t=819s)** And we have them sign an NDA. Um and we record all the video. This is 16 hours of video. Um we basically use Loom and then we feed all the videos into uh our our agent basically Devin and we say hey you know which one should we pick? I actually watched all 16 hours of these videos for the last round. It was brutal, but it did give me a good read on the people. Um and then you basically pick one. You pick your finalists and then what's important is that you don't do calls before this. Um you will get biased, you'll get confused, you'll try to pick somebody you shouldn't. And I would just call the finalists and say, hey, you know, we think we'd like to hire you. Let's talk a little bit. Um

**[14:25](https://www.youtube.com/watch?v=BTtyguoPvBU&t=865s)** and that gives you the final sort of human read, but you're going to watch videos of these people for hours. Like you're not really going to need that call. Um but I think there's a little bit of of of human connection there that's important. I think this is how everyone's going to hire. Like this works. Um you know, I've hired hundreds and hundreds and hundreds of people in my career. This is just way easier and way better. Um and I think it's where we're all moving to. So I'm actually going to finish 3 minutes early. Um if you want to know more about Untangle, just go to untangle.us. Um I'm on X like just all the time. I've literally been on X for 20 years. Um and so that's where I live and breathe. So if you want to know more about uh leading companies, managing agents, um that's where I am. If you're interested in family law and your

**[15:14](https://www.youtube.com/watch?v=BTtyguoPvBU&t=914s)** passion about making divorce less painful, um get in touch. Um and that is all I have to say. Thanks everybody. Appreciate it. >> [applause]
