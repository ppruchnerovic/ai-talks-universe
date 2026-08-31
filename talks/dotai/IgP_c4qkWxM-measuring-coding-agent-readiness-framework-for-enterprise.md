---
id: IgP_c4qkWxM
title: "Measuring Coding Agent Readiness: Framework for Enterprise AI Dev – Upsun at dotAI Tech Track AI Day"
slug: measuring-coding-agent-readiness-framework-for-enterprise
conference: dotai
conference_name: "dotAI"
category: "AI engineering & agents"
edition: "dot conferences"
year: 2026
speakers: ["Guillaume Moigneu"]
channel: "dotconferences"
duration_min: 12
published_at: 2026-02-17T13:58:46Z
video_id: IgP_c4qkWxM
youtube_url: https://www.youtube.com/watch?v=IgP_c4qkWxM
tags: []
transcript: true
---

# Measuring Coding Agent Readiness: Framework for Enterprise AI Dev – Upsun at dotAI Tech Track AI Day

**Guillaume Moigneu**

`dotAI` · `dot conferences` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=IgP_c4qkWxM) · [Conference site](https://www.dotai.io/)

## Description

Speaker: Guillaume Moigneu, Field CTO at Upsun.

Description:
Stop comparing model benchmarks. The reason your AI agents can't ship Enterprise-ready code has less to do with the model and more with your codebase and tooling. Flaky tests, missing docs, unreliable builds: humans work around these daily, but agents crash hard. This talk presents spec-driven development and the 8 Pillars of Verification. A framework to measure agent-readiness and a methodology to write specs before prompts. Because without verification, you're not building software, you're generating expensive slop and debt.

dotAI Tech Track organized by dotConferences at AI Day on February 10, 2026, at Station F.

## Transcript

*2,032 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=5s)** [music] I wanted to talk today about like making coding agents actually reliable and useful. Coding agents are everywhere. You've seen that code, codecs, everything. Every week we've got something new and it's becoming quite of a mess. And we see a lot of difference right now between actually people that know how to use them and the more like vapodic trend that can lead to a lot of issues. Just to introduce myself, I'm G aka Yum. I'm Field City Web Appsson. We're a cloud application platform where you can deploy your web apps and everything like this. And I've been a developer for like 25 years now. Crap. Uh started in PHP in 1998, something like this. and I followed the trends and

**[0:54](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=54s)** now using like daily a lot of those different coding agents and tools. So what you see online is a lot of videos like okay I've got my repo on GitHub I'm creating a new PR and in 10 minutes I've got everything deployed to production working well except that that's not actually the case. It raises a lot of new issues and new blockers that we haven't seen before. So how do we make that a bit more reliable and efficient and actually the actual bottleneck is not the capabilities of the model it's our capability of actually defining correctly the input and the output we want to have and if you do a quick test um actually

**[1:42](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=102s)** I've done that last week I've used like four different models GLM opus codeex whatever with the same inputs, they produce an output that is 95% the same. So the model is not the big important part. Obviously they're going to improve, they're going to get better, they're going to make less mistake, less loops and stuff like this. That's great. But that's not the big issue. The big issue is actually what we feed into them and what we expect. Because in the end, what the model is producing is actually not really code. It's not code that works. It's actually just text. a lot of different characters that put together actually produce code and are supposed to run. So uh that's a quote by Andre software one was basically what we've been doing

**[2:30](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=150s)** for the last 20 years where we really put the focus on how we want to specify stuff all the specs all the documentation and how we create that. So the world classic waterfall model and now with that new era of software it's actually what we can actually verify and the good news is that code is actually really easy to verify if you go up on the scale something easy to verify for example a sudoku it's going to take you 5 minutes to do it 2 minutes if you're really good but verifying it is like 10 seconds on the other side of the thing like design more creative work is really hard to verify because you don't actually really know the output you want. The really good news about that is that code

**[3:18](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=198s)** is highly verifiable. We know what the code should do and we know what to expect. So we can actually test that. [snorts] One of the big difference for the past 10 years is that when you're working with developers, we're humans and we can work around gaps. I don't know Sorry, how many of you worked for clients, agencies, and stuff like this? But usually the client doesn't really know how to specify everything. The famous cay is usually like free pages for a full ecommerce website that doesn't make any sense. So as human, we think about that and we implement all the missing gaps into actual feature and new specification that we roll out. But agents actually can't do that. They

**[4:05](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=245s)** can't predict what the customer actually want. So we need to actually fix all those missing part so we can actually have agents that produce what we want. All right. So for example, oops. If you don't have any tests, we can validate what's correct or not. If we have no spec, the agent can take wrong assumption. If you have what we call flaky builds, build that works like 30% of the time. Well, it's really hard to define what's a bug, what's a bug in the test, maybe a production issue and stuff like this. And then observability and preview environment that actually allow you to test in real condition what you're doing and see the actual impact. If you don't have all that, you end up with that new term that we call AI slop,

**[4:53](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=293s)** which is like tons of code that may or may not run, we're not sure, but has been produced by an agent, maybe not even reviewed by someone. and you you don't actually know all the side effects and the edge cases. So over time that's going to degrade your code base. So the first thing I want to talk is actually specdriven development. I won't go into too much detail there. You can find a lot of things online. Thank you Jerome. Uh but basically instead of actually just giving a prompt waiting for the coding agent to generate something and then like crossing fingers that everything's going to go fine, actually start by writing specs. specs and test really defining what you want the code to do the new feature to what to do and how to test it and then you generate and you validate and then you

**[5:41](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=341s)** go again if it doesn't work so that's more like a loop once again define specs try it validate it go back I'm sure you've seen some stuff about Ralph Wigan from Entropic which is basically that concept pushed to the max where they do like 10 different loops and then compare the output. We don't want to do that. If you have like good specs, you should end up with just one run. So once again, why it's important, we're locking the intent of what we want to do. We can review all the different change in the spec and then we can build up our documentation and the full specification feature by feature and we know the success criteria. That feature should allow the user to do X and stuff like this.

**[6:31](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=391s)** >> [snorts] >> But what I really want to talk about today is actually how we can automate verification. We want to give our agent some autonomy. The first part is testing. And as developers, we all test. It's usually not part of the budget. We don't have time to do it. So we just roll out in production and hope everything's going to be great. But now with agents development, we really need to cover those test. And unfortunately you can't trust really the agent to generate the test right now because if you generate the test sorry in the same context as the code it's going to all the tests are going to pass. So you need to spend some time on the test validate all the different edge cases and everything like this. You also need to make sure the tests are running really really fast because you want to run them

**[7:18](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=438s)** a lot. If you're doing end to end test with playrite, that could take like five 10 minutes every time you want to to do something. Documentation and spec, I've already talked about that, but we want to make sure all our specification are always up to date with the project. Code quality is super super important. There are a lot of different standards out there. If you're using PHP, you could use PHP stand. If you're using NodeJS, you can use biome and stuff like this eslint. But basically running the llinters and the verification every time with some code static analysis really help like cleaning a news code syntax issues and stuff like this. And what's really important is also making sure that those standards are enforced on a team level not only yours but making

**[8:07](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=487s)** sure that all the developers in your team follow the rules from the organization. Build is super important. We all need to build our source code into production artifacts. So we need to have a build pipeline that goes fast and actually build the stuff and if it breaks make sure we get good debug so we can reinject that into our agent so we can actually fix the build issue. I'm sorry I'm really speeding up through the slides but I will give you the link preview environment and that's what we've been doing at Epson for like 15 years now is giving you a way to actually test in real production condition with the actual production data on a test environment not just the front end but the full database cache cues anything like this. So make sure

**[8:55](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=535s)** you can run test and also share that with stakeholders in a real environment that is similar to production. Observivity it's one of the big one but making sure that a change that has been deployed work the way you want but doesn't have any performance side effects as well. It's really important because agents have no idea right now about the infrastructure and the behavior of your code. So you need to make sure that you actually track how that new code is performing because it might work. But if you take 10 seconds to generate a transaction, it's not good enough. Security, I think we've all heard about that, but making sure we don't introduce vulnerabilities with like different outdated dependencies, obvious stuff

**[9:45](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=585s)** like this. So having some kind of scans as well, we've got a lot of companies doing that like IDO where you can actually do automated scaling of your codebase every time and standard as well. Um making sure you've got rules written everywhere. Um when I used to work in agencies 15 years ago, we were relying a lot on what I call tribal knowledge, which is like, hey Mark, do you know how this was done six months ago? Yeah, sure. It wasn't by that guy that left. We don't want that. We want to have everything written. How our agents are guided. What they know, the context, the knowledge, everything about the project and the team should actually be documented to work. All right, just a quick recap on of everything. But does it work? What

**[10:33](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=633s)** should it do? Does it meet standards? Can it compile? Can it be tested? Is it working? Is it safe and consistent? That's basically my eight different pillers. Um I've done a quick checklist on GitHub if you want with like to assess yourself and your teams. So you can scan the cure at the G right there. But basically just to make sure you're actually doing like there are 10 criterias for each of those pillers. So if you want to actually start a new project and get the foundations right. Once you get all that, want me to go back too quick? All right. Um, the important thing is the flywheel after that where basically when you get some improvement, you get better agent production. Okay, everyone

**[11:23](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=683s)** got it? Um, so your agents are working better, they've got more autonomy, you end up with a better project infrastructure overall. And then the agents can also improve those infrastructure. So you get into a more virtuous cycle about everything. If you build a verification layer, right, then the agents can actually work on their own and do some good stuff. If you want to read more about that, um, OpenStack is the framework I use for actually writing the specification and stuff like this. Really good. It works with any agents and you can follow, uh, Andre Kpati and Jason way. They've done a lot of talks and written a lot about all that concept of autonomy and verification. Thank you. And because I'm trying to build my LinkedIn audience, if you want to connect, please. Thank you so much.

**[12:15](https://www.youtube.com/watch?v=IgP_c4qkWxM&t=735s)** [music]
