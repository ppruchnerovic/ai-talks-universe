---
id: Bdrs3uAX0_M
title: "AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph"
slug: ai-coding-agents-are-breaking-big-codebases-dan-adler
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dan Adler"]
channel: "AI Engineer"
duration_min: 12
published_at: 2026-10-04T19:30:20Z
video_id: Bdrs3uAX0_M
url: https://www.youtube.com/watch?v=Bdrs3uAX0_M
youtube_url: https://www.youtube.com/watch?v=Bdrs3uAX0_M
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Sourcegraph", "enterprise AI", "AI coding agents", "large codebases", "monorepo", "code search", "code graph", "legacy code", "technical debt", "batch changes", "code migration", "software supply chain", "developer tools", "Dan Adler", "AI Engineer"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Coding assistants & agents", "Enterprise adoption & strategy"]
transcript: true
---

# AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph

**Dan Adler**

`AI Engineer` · `AI Engineer` · `2026` · `12 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Sourcegraph` `#enterprise AI` `#AI coding agents` `#large codebases` `#monorepo` `#code search` `#code graph` `#legacy code` `#technical debt` `#batch changes` `#code migration` `#software supply chain` `#developer tools` `#Dan Adler` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=Bdrs3uAX0_M) · [Conference site](https://www.ai.engineer/)

## Description

Claude Code can make the change. But what if you have 90,000 repositories to make it in?

Dan Adler, CEO of Sourcegraph, makes the case for the people who own the huge, decades-old codebases that run banks, cars and airlines. Coding agents are producing a tidal wave of code, and those codebases are starting to decay through duplicated code, drifting standards, brittle dependencies and new vulnerabilities. Agents understand code by searching, but you can't grep what you can't see. Dan argues that large-scale code visibility is infrastructure, and introduces Sourcegraph's Agentic Batch Changes for making changes across thousands of repos from a single prompt.

In this talk:
• Why most software engineers work in large, long-lived codebases
• How AI-generated code accelerates codebase decay
• Why context, not model quality, is the bottleneck at enterprise scale
• Making and auditing changes across thousands of repos

SPEAKER
Dan Adler, CEO, Sourcegraph
X: https://x.com/DanielNealAdler

LINKS
Sourcegraph: https://sourcegraph.com
Introducing Agentic Batch Changes: https://sourcegraph.com/blog/introducing-agentic-batch-changes

CHAPTERS
0:00 Intro
0:12 Owning a large codebase
0:37 The software that runs the world
2:02 A tidal wave of AI-generated code
2:57 Codebases are starting to decay
3:57 Owning a codebase is harder than ever
4:31 "I don't know what this code does"
5:11 Codebase owners deserve better
6:06 A call to dev tools builders
6:31 "I have 90,000 repositories"
7:21 Agents love to search
7:51 You can't grep what you can't see
8:21 There will be much more code
8:56 The code graph
9:21 Agentic Batch Changes
10:21 Case study: Mercari
11:11 How many repos do you really have?

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,019 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=1s)** [music] Hey, welcome everybody. I'm Dan Adler, CEO at SourceCraft. It is uh great to see you all here today. Thank you so much for coming out and joining us. Um, this is a talk today about the unglamorous but loadbearing work of owning a large complex codebase and why AI and agentic coding tools today make that job more difficult and more important than ever before. Just to start, the software that runs the world is not pretty. It's not new. It's not clean. It's how everything actually works.

**[0:49](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=49s)** 72% of software industry employment is in companies with more than 500 people. These are the large enterprises of the world. These are the companies managing thousands of repositories and decades of codebased history. Few of your peers work at startups at the hot companies you may hear about on social media. And even fewer of them are actually like ex soloreneurs making a living off of their um social feeds. Most of us work in large longived code bases. Those code bases are how your bank account will reject a transaction in real time if you hit your limit. They're how your insurance carrier calculates the reimbursement rate for a policy holder with dual coverage. It's how a chip and a warehouse scanner will actually allow Amazon to tell you when your socks arrive. It's how your Uber estimates an arrival time. It's how an airplane uses

**[1:37](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=97s)** radar to uh adjust trajectories. How your paycheck gets issued. It's how your office air conditioner ticks on and on and on and on and on. These are the things that keep the world moving. We are all completely utterly dependent on massive decades old super complex code bases that have been built over many many years by thousands of engineers and coding agents are writing more better code today faster than we have ever seen before. A title wave of code is coming for you. It's coming for your code base and for all of your engineers on your team who are trying to just keep their heads above water. Every one of us has felt this pain, this

**[2:25](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=145s)** flood of AI generated code that we now have to review and make sure is healthy for our codebase and we're exhausted by it. And look, there are now code review agents. I'm sure there's a lot of them around this room right now. There are tools designed to help you measure your code base's health and so on. And look, the new the major coding agents will start to pull this stuff in. The models will get better over time. We'll keep putting sandbags down to keep this flood held back, right? We're going to keep finding these local maxima to help ourselves sort of avoid this problem. But meanwhile, what's happening is that these code bases, these massive ones that keep the world running are beginning to decay. millions of lines of code, tens of thousands of repositories, way too much to fit into a context window or even just to clone and GP in

**[3:13](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=193s)** real time. That's just not possible. And this is causing big problems. We're publishing new features, new patches at record speed. There are different coding standards being applied in different places by different agents across the codebase. There's duplicated code proliferating. You you already have a library that does this, but your agent doesn't know that. There's cross-ervice dependencies that are becoming more brittle. There are slight deviations in standards that are creating more insidious hidden issues across the codebase. And maybe more important than anything else here, there are new vulnerabilities being uncovered by agents every single day. They require constant constant oversight and upkeep of all of these massive legacy code bases that nobody wants to think about or deal with. The job of owning a codebase is harder today than it has

**[4:03](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=243s)** ever been before. And at the end of the day, the problem here is actually the volume of code. The call is coming from inside the house, right? The very tools that are speeding all of us up and letting us write more code faster than ever are also the tools that are creating the conditions that will cause these massive code bases that run our world to begin to fail. Every day I talk to technology executives at these large companies and they are feeling this so viscerally. The same pain that I imagine many of you are feeling too, right? I want to give my devs the best tools possible. But just today, I overheard a dev say, "I don't know what this code does. AI wrote it for me." This is a tech leader and executive at a top 10 car manufacturer.

**[4:52](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=292s)** When you're writing vehicle autopilot code and you have thousands of engineers in your org that you have to manage, you want to enable, this is terrifying. All right, here we go. So what I um deeply believe is that these codebase owners deserve better. Today's agentic dev tools are not meeting the moment for this. The infrastructure to see and understand a 50,000 repo codebase is not being built or sold by OpenAI, by anthropic, by cursor, by the rest of them. This is a hard and unique problem. Their agents are so unbelievably good at smalling at solving the small-cale problems that

**[5:40](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=340s)** most developers deal with every day that they are their demand is growing faster than ever before. And this bigger problem of these code bases beginning to fall apart is going unnoticed. So this session this is a call first of all off to celebrate the people the owners of these code bases people around the world who are actually keeping them alive and keeping them running. most of our software engineer peers around the globe. So, thank you all so much for what you're doing. But this session is also a call to dev tools companies out there, to the agent harness builders, to people who are building the infrastructure for these agents to help build the the infrastructure, the the ability to go see and understand these massive scale repositories and give that to their agents.

**[6:36](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=396s)** This is a great quote that I heard from um a tech leader at uh one of the top 10 US banks. Tens of trillions of dollars in assets uh in custody or administration. Sure, Claude Code can uh make this change, but I have 90,000 repositories to make it in. This is actually a specific quote about a specific supply chain vulnerability, an npm thing. won't get into it, but if you're a bank and you're seeing agents uncover and create these new vulnerabilities at an unprecedented pace and you're being told to go use cloud code to solve this, that's a problem. Good luck doing that in 90,000 repositories, mapping out how these code bases all come to together, what's actually living in production across your company, across your product offerings. Because at the end of the day, right,

**[7:24](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=444s)** what's really funny about all this is that, if we know anything about LLMs, is that they just love to search. It's like a new hire getting up to speed on the codebase. It's how agents build models of the world. The repo architecture that you're plugging into your agents.md files, like, let's be real, that's barely moving the needle here. This agent is going to grap gp gp gp gp its way to codebase understanding. That's simply how it works. But understanding is a context problem. You can't gp what you literally cannot see. This is tools and infrastructure that's needed. And the infrastructure to go see and search and really deeply understand a 500 or 5,000 or 50,000 or half a million repo codebase is not

**[8:12](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=492s)** being built by the agent builders today. And so that's where what we're solving, what we're working on as a company. This is what source graph is built around, right? Give this a second. If you'll let me sort of take a moment and predict the future of our industry. These massive code bases are not going away. In fact, there will be more code. There will be much much much more code out there in the future. And we believe very deeply that building tools to give agents the ability to actually see and understand and evolve those large code bases is essential for the future. And where this comes from at the end of the day is having a graph that code graph in mind. The foundational graph of

**[9:02](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=542s)** your codebase including search and then the actual compiler accurate output. Um, if you go and and do that analysis that is essential to give your agents the ability to go and understand how to make changes effectively. Visibility is infrastructure. And we've actually built a lot on top of this, right? We're not stopping here. Actually, just today we launched our new um our new agentic batch changes product into beta. This is a frontier agent uh and its job is to let the owner of a massive codebase actually execute code changes across hundreds or thousands of repositories at once starting with a single prompt. This is a product that will iteratively roll out changes across that that codebase. Self-heal respond to CI status PR comments. Use coding agents

**[9:50](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=590s)** where it makes sense, where judgment is needed. Use deterministic scripts where it's not. and provide tracking and auditability to be sure that you've covered 100% of the places where that patch is needed, where that change is needed. Because like I keep saying here, at the end of the day, this is an infrastructure problem. When you're putting code out there into the world, you need to make sure that it's actually going to keep your codebase healthy, that it's actually going to make be able to um adapt to the places where your codebase is beginning to fall apart. Here's a great quote from an early access user um uh actually at Merkari, a global um shopping tool out of Japan. Incredible company, massive codebase, hundreds and hundreds of independent microservices running in production. This user was using um this product to go actually patch a GitHub uh code

**[10:38](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=638s)** injection issue where you have to set environment variables correctly. Um he ran this on two repos where he knew this issue existed and then said yeah go explore the rest of our codebase and found 80 other potential vulnerabilities across their codebase in other places. This is like bas this is like config files. This is basically just going and doing that scan patching them all in one go with a sort of deterministic script that can go make sure it's making that change consistently effectively across 100 of the places where that risk exists. That is what confidence is all about in the agent coding era. So yeah, I'll stop here. If you're wondering right now about like how many repos in your codebase, how many forks are there out there, how many um copies of repos are there out there, how many repos have your in your developers brought into your um company and are now being plugged in as a library or an API

**[11:27](https://www.youtube.com/watch?v=Bdrs3uAX0_M&t=687s)** somewhere in your codebase that's live in production that you're not aware of. That's the sort of thing that we're here to help. Right? If you're wondering what code is deployed right now and how you can go scan it all and see it all and make sure it's all updated, come talk to me. And uh tonight we're actually hosting a event here in SF called Code Cocktails and Cuttovers. Come on out, join us. Um come find us. Bring your gnarliest codebased stories. This is where we want to uh talk and hear from all of you about what you're trying to deal with and how you're dealing with the title wave of code that's coming for you. Cool. Thank you. I'll stop there. Any questions? Thank you. >> [music]
