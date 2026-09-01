---
id: 4JKzfCdwiSo
title: "How Engineering Teams Automate Quality at Scale"
slug: how-engineering-teams-automate-quality-at-scale
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 9
published_at: 2026-01-11T14:00:08Z
video_id: 4JKzfCdwiSo
url: https://www.youtube.com/watch?v=4JKzfCdwiSo
youtube_url: https://www.youtube.com/watch?v=4JKzfCdwiSo
tags: []
transcript: true
---

# How Engineering Teams Automate Quality at Scale

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=4JKzfCdwiSo) · [Conference site](https://tessl.io/devcon/)

## Description

How do you move from AI hype to AI-native production?

Most teams treat AI like a search engine. The top 1% of engineering organisations are building autonomous workflows that achieve near-perfect test coverage.

In this episode, we go inside the engineering rooms of Meta, Thoughtworks, Coinbase, and ServiceTitan to uncover the exact frameworks and agent workflows making this transition possible.

On the docket:
• Ian Thomas (Meta): How unsupervised agents jumped test coverage from 60% to 93.5% using automated runbooks.
• Wesley Reisz (Thoughtworks): Using the RIPPER-5 framework to stop AI hallucinations and structure agent execution.
• Sepehr Khosravi (Coinbase): The context rule for preventing AI laziness and ensuring high-fidelity output.
• David Stein (ServiceTitan): A tactical blueprint for migrating hundreds of legacy metrics without breaking production.

Whether you’re a solo developer mastering Cursor or a CTO looking to automate your entire sprint, this conversation provides the tactical runbook for going AI-native.

Ian Thomas: https://www.linkedin.com/in/anatomic/?originalSubdomain=uk
Wesley Reisz: https://www.linkedin.com/in/wesreisz/
Sepehr Khosravi: https://www.linkedin.com/in/sepehrkhosravi/
David Stein: https://www.linkedin.com/in/steindavidj/
Simon Maple: https://www.linkedin.com/in/simonmaple/
Tessl: https://www.linkedin.com/company/tesslio/
AI Native Dev: https://www.linkedin.com/showcase/ai-native-dev/

## Transcript

*1,967 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=0s)** Initially the wins were people saying oh I'm using dev mate and then there was equally some people that were suffering and that was when we start to experiment with things like unsupervised agents. >> You've been interacting with an LM and it has to have the context of what you're doing. So what the ripper 5 model does it tells the LLM that ask me questions analyze the codebase of where you're at. >> Treat your AI like a basic junior engineer. If you don't give him the full requirements of the task he's not going to be able to figure it out. When you have hundreds of metrics written in C, you break it down into basically a bunch of similar tasks that can be verified in a standardized way. One of the things that are really nice about communities is that everyone, you

**[0:46](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=46s)** know, you get so many different people at different levels of their experience and adoption. And and this kind of like leans into one thing that you mentioned as well, which is like these maturity models. I guess there's maturity in terms of how an individual is using it as well as a team. Talk us through the maturity models and why they're important. >> So the the thing about the maturity model, I intended it to be used for a team, but there is a a dimension on there which is about individual productivity as well. So you can reflect on your own kind of performance and ways that you're getting value from it. Um the benefit of it being a team based thing is that it opens up the conversation within your team. Yes. And so you can generate uh ideas and have action plans that are specific to you because every team's going to have slightly different context or different levels of ability and different interests. So that's great. Um we tried to model it in a way that was going to be fairly agnostic of the tooling and

**[1:34](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=94s)** and be durable because again the value I think is that you can have these models and you can repeat the the assessments time after time and see how you're progressing. Um and we do subtly tweak it every now and again but um generally it's kept fairly consistent and then yeah like say the teams run these assessment workshops and they can have the discussion and that's that's where the real value lies. >> Yeah. Yeah. Let's talk about value and wins. What were the what were the big wins that you saw and and how did you share that across the community? So initially the wins were people saying I'm using DevMate which is part of our tool set in VS Code that we work with dayto-day and I'm finding ways to use this to like understand the code base better or or what have you and there were some early examples of people just sort of going for a big problem and and putting a prompt in and they were

**[2:20](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=140s)** getting a bit of lucky and then there was equally some people that were suffering that that wasn't working at all. >> Yeah. Um but then we found there was kind of repeatable patterns emerging around things like um test improvements or how to make code quality improvements or reducing complexity of code. Yeah. And and that was when we started to experiment with things like unsupervised agents and you could say okay with this category of problem um say like we've got test coverage gaps we want to go and find all the files that are related to this part of the codebase related to this on call say >> uh find the ones that have got the biggest coverage gaps and then using this runbook that we've put together go and go and cover them go and produce diffs that help us to >> bridge the gap >> and that was the sort of thing that we lots of hours of manual work and >> as this sort of evolved we found

**[3:09](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=189s)** actually we can go and use the tools to go and query the data to find make do the analysis and then generate the tasks for itself to go and then fix the tests and add the coverage uh and I think the end result was something like 93 and a half% coverage was achieved which when we were way less than 60% to start off with so >> um many diffs landed >> and it sounds like like you know huge productivity gains >> you introduced a really interesting um framework called ripper er or riper back >> ripper 5. Yeah. Um why don't you introduce that to to the audience and then we can kind of like delve deeper into >> it. It's first to be fair. I did come up with it. It was uh we discovered it on a blog post or a cursor forum that was in I think March of of this year or so when we first ran across it. But what it stands for um it's really it stands for

**[3:58](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=238s)** research, innovate u plan, execute and then review. So, it's that plan execute model, but it goes a little bit deeper. >> And the reason why I think it's so important is you've been interacting with an LM, you've been in a chat console and you're trying to do something and >> you it has to have the context of what you're doing. You don't always are in the same mindset. You may be trying to research a particular thing, but it jumps into coding or you may be planning and it jump it jumps into coding or you're coding and it's it's not really doing any planning. So what the ripper 5 model does is it provides a set of instructions that um you can pass as a command. We're using cursor. So we pass it as kind of um property for our our our um our our IDE to be able to have this context. So we give it a command.

**[4:47](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=287s)** We say we're in research mode. And what that does is it it tells the LLM that asks me questions, analyze the codebase of where you're at, for example. Um, but don't do is as important as what it can do as is what it can't do. Don't do coding. Don't do planning. Right now, I just want you to understand what the code is, what my what my spec is actually trying to do, so that way I can provide more details to refine the spec. So, this ripper 5, it's kind of like an execution model of how you work with the LLM and we do that in pairing with the with the developer. >> Why is context so important? Yeah, I think you kind of got to treat your AI like a basic junior engineer. If you don't give him the full requirements of the task, he's not going to be able to figure it out, right? So, we need to

**[5:35](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=335s)** make sure all the details that the AI needs to know, we're providing it. >> And I think >> one really good way to do that as well is with MCPS and setting up some sort of documentation MCP because there's often time a lot of gaps in our code where the AI will read through your code but still not understand what's going on. But when we give it access to our documentation, it can read that and fill in those gaps which really really boosts the productivity of what you can produce. >> Yeah. Amazing. And actually in the session I asked one of the questions which was about how you know how to know when to give you know enough context without giving so much context that it actually degrades the performance. Um and I guess that's what a lot of the things like when we talk about cursor rules and the always apply and the apply manually. It's for exactly that reason. And I suspect when we look at if if you wanted if you had a huge amount of context that you wanted to provide, you were probably more likely to say

**[6:22](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=382s)** actually there's too much context here. Let's add this either manually or add it more intelligently. Apply intelligently so that way you're not actually bloating context for no reason. Yeah. Yeah. Super interesting and actually a really really crucial part. Um okay, one more curse rule and we'll jump into uh Claude. >> Yeah. Yeah. Let's do it. You can have a bunch of different rules. I think one that's particularly interesting, Claude shared this themselves, is relating to this context we just talked about. Often times if you get close to the end of your context window, so you've used up like 90%. Then you ask the AI for something, it will give you a short answer because it's just trying to get something out before it runs out of context. But if you type in a prompt like this or something similar, you can tell it, hey, >> your your context is going to end, but like don't worry about that. You can compact it. Actually give me the best answer. And that's one useful tip. What would happen if you just said to an

**[7:08](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=428s)** agent, you know, here's my environment. I need you to migrate this, create a plan and do it yourself, >> right? What what what would be the problems? >> So for a product like this, when you have hundreds of metrics and each of them are underpinned with a bunch of code written in C, you know, with all the issues I mentioned before about not all the context necessarily being exactly where you need it, there's a lot of complexity in that. You can't just open up even the state-of-the-art coding tools like cursor and say hey please like migrate all of our metrics into you know into this new abstraction on this new framework and by the way convert from C into writing SQL with a YAML for metric flow on top you it doesn't uh it doesn't work to do that is what we found >> um in order to get traction there you have to really break down >> the you know break down the mountain of

**[7:57](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=477s)** that problem into small pieces it sounds kind Obvious if you say in this way you break it down into standardized into you break it down into basically a bunch of similar tasks that can be uh verified in a standardized way. >> Yes. >> And then you assign a long you you basically construct a long task list with fa with with phases for individual sections of the task like move these first five metrics is you know the first phase and then the next and >> and who's doing this? Is this is this humans doing this? Is this humans with agents as an assistant? Right. So humans are you know choosing the the task list right like are enumerating okay these are all of the metrics that we're going to enumerate that we're going to migrate in phase one and these are the metrics that we're going to migrate in phase two so humans are making those choices as

**[8:44](https://www.youtube.com/watch?v=4JKzfCdwiSo&t=524s)** well as like what the target architecture is that we're going to be putting these things into and humans are also you know with some help from like AI tools are constructing the you know all of the context that's going to go to the coding agents to actually enable them to do the migration work for those pieces H.
