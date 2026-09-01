---
id: u37qkpp5eB8
title: "Inside Kikimora: We Built a Dark Software Factory"
slug: inside-kikimora-we-built-a-dark-software-factory
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 16
published_at: 2026-08-17T14:30:37Z
video_id: u37qkpp5eB8
url: https://www.youtube.com/watch?v=u37qkpp5eB8
youtube_url: https://www.youtube.com/watch?v=u37qkpp5eB8
tags: ["AI coding", "Kikimora", "Kikimora software factory", "Tessl's coding transformation", "agent development", "ainativedev", "automated PRs", "autonomous coding agents", "autonomous software production", "coding agents", "dark factory", "engineering teamwork", "software factory", "trust in automated PRs", "what is a dark factory"]
transcript: true
---

# Inside Kikimora: We Built a Dark Software Factory

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `16 min`

`#AI coding` `#Kikimora` `#Kikimora software factory` `#Tessl's coding transformation` `#agent development` `#ainativedev` `#automated PRs` `#autonomous coding agents` `#autonomous software production` `#coding agents` `#dark factory` `#engineering teamwork` `#software factory` `#trust in automated PRs` `#what is a dark factory`

[Watch the recording](https://www.youtube.com/watch?v=u37qkpp5eB8) · [Conference site](https://tessl.io/devcon/)

## Description

In November, everyone at Tessl started using coding agents. By January and February, every process built on the assumption that software is slow had begun to break.

This is what happened over the eight weeks that followed: a team who each went away and built their own autonomous orchestrator, one Frankenstein factory stitched from the best of them, and a Slavic folklore creature who tidies your house at night — or wrecks it, if you're a bad host.

To get started building your own software factory, install Tessl Agent at tess.io/agent.

What we cover:
– What a "dark factory" is, and why the whole point is that nobody's inside
– The bottleneck that broke every process built for slow software
– Night Shift, the side-project orchestrator built on the rule "don't look at the code at all"
– Everyone building their own factory separately, then merging them into one
– Why the factory is called Kikimora, and what she does to a lazy host
– The stretch of time it ran in a Docker container on one laptop — until someone closed the lid
– Onboarding an entire engineering team in three weeks
– Why the real blocker is trust, not tooling: can you sign your name to a PR you didn't write?
– 90%+ of work delegated, roughly 30% faster every week or two, and a factory that triages its own issues
– Building the Tessl agent, so every company can own its own factory
– What happens when GTM, design and the People team start using it too
– What's left for engineers when writing code stops being the valuable part

Chapters:
00:00:00 - Introduction
00:00:45 - Meet the agent development team
00:01:01 - What is a dark factory?
00:01:36 - How the factory actually works
00:02:03 - November, and the bottlenecks that followed
00:03:29 - "The only way out is through"
00:04:11 - Night Shift: don't look at the code at all
00:04:36 - Everyone builds their own factory
00:05:37 - "I built Kikimora with itself"
00:06:27 - Why it's called Kikimora
00:07:43 - Onboarding the whole engineering team
00:09:11 - The CEO ships to prod
00:09:25 - Can I sign my name to this PR?
00:10:21 - Eight weeks in: what actually changed
00:12:09 - Building the Tessl agent
00:12:57 - When non-engineers join the factory
00:15:07 - The new software engineering

🌐 Try Tessl - we help you build a software factory, one step at a time: https://tessl.co/qwm
🔔 Subscribe for weekly videos on AI-native development

We're still finding out what breaks — if you're running something similar, or you think this is a terrible idea, tell us why in the comments.

## Transcript

*2,763 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=u37qkpp5eB8&t=0s)** To start with, I was like, I don't think we can do this. We intentionally ran really fast and straight into many walls. But we said, cool, this is going to be warts and all, alpha software, you can use it. It is hard to convince people that this is safe to use. And that's scary. There's, like, a big existential kind of, you know, interrobang at the end of that sentence. Your ability to write code is actually not useful. The agents can do it probably better than you can. And, fingers crossed, we all have jobs in two years. I don't know how. I work as part of the agent

**[0:49](https://www.youtube.com/watch?v=u37qkpp5eB8&t=49s)** enablement team, which specifically focuses on the Dark Factory, which I believe is what I'm here to talk about today. A dark factory is the idea of building software in a more autonomous way. In a very autonomous way, in fact, where we are not supervising the software anymore. And our dark factory goes by the name Kikimora. The concept of a dark factory is from manufacturing, and you have a factory building, but the lights are not on because there are no humans inside. I don't think that's where software engineering is going, but it was a kind of forcing function to say, well, this is the world we think we're going to. So let's be a bit controversial, I guess, to try and force people to see that things are rapidly changing and also to encourage debate. So the very simple version is

**[1:40](https://www.youtube.com/watch?v=u37qkpp5eB8&t=100s)** you create a Linear issue, the factory picks it up, it solves it with an autonomous agent. So it's not an interactive session. It just does it in the cloud and it opens a GitHub PR. It then babysits this GitHub PR. So if you go and comment on it and request some changes, it's going to do that until you merge the PR. That's it. So I think a lot of people have talked about the November period when Claude Code and other coding agents really start to produce good output. That is when everybody at the company shifted from, oh yeah, I'm using coding agents, to, oh, you're not using coding agents? Why not? The journey everybody goes on after that, it's just one of bottlenecks, right? Like, as soon as you start getting faster, you realize, like, all these other processes start to break down because they assumed the thing before them was slow. So I'd say around January, February was where we started hitting big bottlenecks.

**[2:34](https://www.youtube.com/watch?v=u37qkpp5eB8&t=154s)** Software engineering was speeding up, at least from an external perception of other companies. And you got Anthropic coming out and saying, hey, we rewrote Bun from Zig to Rust in two weeks. And so there was a conversation at the senior leadership level, but like, cool, what do we need to do to drive our own kind of pace of change up? Other people are already using software factories inside their companies to build their products. We knew that we needed to not be left behind. We've just had engineers using AI in whatever way works for them. And I think in practice that was most developers running single sessions or maybe parallel sessions with Claude Code, still raising PRs kind of in their name and asking for human review. It was very, like, AI-enhanced but still very siloed work.

**[3:23](https://www.youtube.com/watch?v=u37qkpp5eB8&t=203s)** We realized we're not being ambitious enough by quite a long way. I think there was a very clear moment where we just decided the only way out is through. Like, we have to just stop fighting on every frontier, one at a time, and we have to just say, what's a fundamentally different model that at least has, like, the solution baked into the problem, Okay, so I think everybody is largely here and everybody may have heard I'm going to talk a little bit about personal experiments I've been doing with harness engineering, software factories. It's been a slight change in topic, and we're actually going to do an improv workshop. Just kidding. No, no, no, don't worry. We're going to. I wanted to see who would react the most terrified.

**[4:11](https://www.youtube.com/watch?v=u37qkpp5eB8&t=251s)** The beauty of being able to work on side projects is you can take more opinionated, ambitious stances right away. And so Night Shift was my own internal orchestrator that I made for side projects, where the goal was, don't look at the code at all. Night Shift was a good proof point to leadership that, hey, there is something there, and it was cool and it was visible and it was real. I think it was Macey had the brilliant idea that we all go and build our own dark factory separately, each of us, and then we get together and create a big Frankenstein of dark factories that is the best of the best. This would be ludicrous in traditional software engineering, right? But in this particular case, given how quickly you can iterate to build some sort of prototype of that factory, it was really the right decision.

**[5:04](https://www.youtube.com/watch?v=u37qkpp5eB8&t=304s)** Some people went and they tried off-the-shelf products. So things that were sort of already building towards factories and automations, some people built their own from scratch. And the funny thing was they all came back and they all looked different. And at first we sort of viewed this as, like, oh crap. You know, maybe this is just, like, needs to be a full custom rig. Nobody agrees. But as we started to sit down and compare notes with each other, we realized that there were a lot of familiar or even identical components being built. Next up is Maria. Maria stole the spotlight a little bit. She had kind of a mic drop moment where she was like: I built Kikimora with itself. She basically had built this orchestrator on, say, what, like a Thursday, and then told it to improve itself over the weekend.

**[5:56](https://www.youtube.com/watch?v=u37qkpp5eB8&t=356s)** I mean, that's a dramatic simplification of what happened. But this orchestrator did it all by itself. The proof is kind of in the pudding. It was very easy for anyone to come and try making an issue through this. They just had to go to Linear and make an issue. They didn't have to install anything, run anything on their laptop, nothing at all. It was already running on my laptop. This made it very easy for people to validate that this kind of works as an interface. I chose the name. Kikimoras are Slavic mythical creatures. I'm Slavic, Bulgarian. I thought I would choose something coming from my culture. Kikimora is a creature that lives in your home, and she comes at night and she helps you tidy up. She helps you with the chores, but only if you're a good host. If you are lazy, if you don't tidy up, she's actually going to do the opposite.

**[6:50](https://www.youtube.com/watch?v=u37qkpp5eB8&t=410s)** She's going to mess everything up for you and prank you. I thought that was an excellent parallel to what I think the Dark Factory is. It was interesting for the week and a half or so when the whole team was using Kikimora for the Dark Factory. I was running inside the Docker container inside Maria's laptop. Every time she went home, she went on the tube. She lost internet connection and the thing stopped working for a bit. A big welcome to AI Native Dev London 2026. We also had an event around that time. At some point I wanted to attend a talk and I left my laptop unattended, and I asked colleagues, please don't close it. And of course, somebody closed my laptop in the middle of another member of the team doing something very important through the dark factory.

**[7:40](https://www.youtube.com/watch?v=u37qkpp5eB8&t=460s)** Yeah. And you have some issues. If I could go back again, the one thing I'd change would be to get more buy-in to this concept of loop engineering being the way forward. The biggest thing I think once the software factory got to production and we started using it, it felt overwhelming in terms of what there is to learn. It felt like there was kind of a huge barrier to kind of adopting it. And I definitely know other people felt that as well within the company. There is such an immense shift you have to make as a software engineer. If you're going to adopt this factory approach, at some point you have to flip the switch. It was a very tight timeline. So we had three weeks to onboard the whole engineering team. In fact, Rob Willoughby, I remember that he went to leadership in the first week to warn them that we might be behind schedule. Yeah, it felt like a reach.

**[8:33](https://www.youtube.com/watch?v=u37qkpp5eB8&t=513s)** I mean, we smashed it, but I wasn't sure that we were going to get there. It was not trivial to get there. It was tough and we had to do a lot of work, as I said, like authentication running in the cloud, all of these things. But ultimately we had a running prototype before those three weeks were up. In fact, I would say that's maybe even too long. It should be like a week to get on board, three weeks to get used to it. We really pushed leadership actually to use it, to show culturally that, hey, this is a bet that we're making. We want people to use that. Our CEO, Guy, actually shipped a database migration to prod via the dark software factory without anyone on engineering knowing about that. So that was a bit of a, oh, maybe we need some thinking on this.

**[9:25](https://www.youtube.com/watch?v=u37qkpp5eB8&t=565s)** I think cultural change on the engineering side is less about velocity and more about, can I trust the results of this enough to sign my name to this PR, which is what we're functionally asking people to do. There are a lot of people who are like, I need to be certain that this will work perfectly. I'm not going to try it unless I see data that it works perfectly. And your shift needs to be, okay, I'm going to adopt this way of working, and then I'm going to make it work perfectly. You can't drip feed that. You just have to bite the bullet. We're trying to pitch to engineers who have come up in a discipline that has said your ability to write code is the most important thing, because that is something that is unique about you, and you're very well paid for that. Now there's a fundamental shift. Your ability to understand the system, or the way it's all put together, or the interlocking of technical constraints, business constraints

**[10:16](https://www.youtube.com/watch?v=u37qkpp5eB8&t=616s)** and all that kind of stuff, that's where your value lives. I think for me, we've demonstrated that we can move so quickly. And I wouldn't have believed anyone who said, you're going to be here in eight weeks time. I would have been like, what? We don't even have a software factory, let alone people using it and let alone all of these capabilities. The amount of time I spend in an IDE now has exponentially decreased. Way more than 90% of my work is now being delegated to the, to the cloud. And then the 10% is largely things like the front end changes that I want to spend more time crafting. We are shipping faster. I think every week or two we go about 30% faster than we did the week before. And it doesn't seem to be tapering off yet. The biggest surprise I had was how much it can improve itself without me doing anything.

**[11:04](https://www.youtube.com/watch?v=u37qkpp5eB8&t=664s)** If I give it the right data, the only thing I did was give it simple instruction, go look at the logs and find general patterns for improvement. We started off having one person each day on support, but then pretty quickly we're like, hang on. We have a software factory that can improve itself. Let's have it automatically triage the issues. If you'd said to me certainly two months ago, but even a month ago, we would quite easily have been able to try some of these ideas, I would have been like, I don't think we can do that easily. We think every company is going to need to own their own factory. And in fact, we think that is what software engineering is going to become. Actually, there's a lot of plumbing that goes into building a factory that, however you shape it, you're going to need.

**[11:52](https://www.youtube.com/watch?v=u37qkpp5eB8&t=712s)** And it's actually pretty annoying to build. But what we want to do is we want to make it really easy to jump to the interesting part, like the part that's actually going to drive impact for your business. There's actually a huge opportunity there to say, let's build a factory-building agent. And so that's where the Tessl agent was born. In many ways it will look and feel like a coding agent. You work in your terminal. It has, like, a headless automated mode. But its purpose isn't really writing code. It's helping you identify workflows, extract them from all of your current silos of working, and then helping you sort of format them for agents, upload them to our skills registry, which we use to track workflows, then create automations and improve them. As we brought this concept to customers, we started to see customers get excited by building their factory.

**[12:42](https://www.youtube.com/watch?v=u37qkpp5eB8&t=762s)** But we're there to help make it easy, not just the building part, but also the kind of keeping up. You're never done building the factory. And so you sort of need a factory copilot. As the pace of software development at Tessl accelerated, it always felt like our website and kind of marketing messages just to sort of not keeping up with what we're building because we're building a lot. Right. And so we moved our messaging framework into the monorepo so we can auto-generate with the factory sales collateral or website changes. So more and more of these factory capabilities are exposed to the broader organization as a whole. And it's been amazing to see, not just the productivity boost, but the excitement that the whole team has around using the factory.

**[13:35](https://www.youtube.com/watch?v=u37qkpp5eB8&t=815s)** A designer on my team came to me and was like, I just shipped my first PR and I've never felt more empowered in my life. And now we have the GTM team using the Dark Factory. We have the People's Team using the Dark Factory for tasks that are nothing to do with coding. As we see our kind of non-development teams embrace the factory, we are also coming across all sorts of gaps and things that are harder. And we've been using those learnings to build those back into the product itself. And, like, through the course of history, anytime you find a technology that makes something valuable, more approachable to a wider set of people, and, like, transition somebody from doing the thing to enabling others to do the thing, that is always the way that we drive foundational shifts. And

**[14:25](https://www.youtube.com/watch?v=u37qkpp5eB8&t=865s)** the reality is, once you do start using a software factory and it is running a lot of code for you and you're seeing a lot of success, it does change your mindset and shift how you think about how software is going to be built. When I was at AI Engineer earlier this year, Theo gave the closing keynote. And one of the points that he stressed is that our ambition isn't big enough. There are so many things there that we can solve so much quicker, so much faster, that needed entire engineering teams to be commissioned in order to deliver those products that can now be delivered by one really strong product minded individual. Like, there are some really amazing human problems that we're going to be able to deliver on a lot quicker than we would have been able to. To me this is the new software engineering. This is what it looks like. We haven't figured out the details yet. And being one of the people who works on it

**[15:16](https://www.youtube.com/watch?v=u37qkpp5eB8&t=916s)** and figures out those details is extremely exciting. Faster better cheaper. Pick two. No, in this case, it's all three. You have them at your fingertips. It's inevitable that this will be doing all of the implementation work. Help the process and try to adapt your thinking into something bigger.
