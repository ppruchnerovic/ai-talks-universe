---
id: XqF-IFHBCkM
title: "Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel"
slug: redesigning-how-software-gets-built-with-ai-agents-sonar
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-07T15:30:19Z
video_id: XqF-IFHBCkM
url: https://www.youtube.com/watch?v=XqF-IFHBCkM
youtube_url: https://www.youtube.com/watch?v=XqF-IFHBCkM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI agents", "software development lifecycle", "SDLC", "agentic engineering", "AI adoption", "developer productivity", "code review", "AI code quality", "platform engineering", "engineering leadership", "Sonar", "Gitar", "McKinsey", "Tariq Shaukat", "AI Engineer"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI agents` `#software development lifecycle` `#SDLC` `#agentic engineering` `#AI adoption` `#developer productivity` `#code review` `#AI code quality` `#platform engineering` `#engineering leadership` `#Sonar` `#Gitar` `#McKinsey` `#Tariq Shaukat` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=XqF-IFHBCkM) · [Conference site](https://www.ai.engineer/)

## Description

Most companies say they've deployed AI agents. Fewer than a third say it's paying off. What do the rest do differently?

A panel with Sonar CEO Tariq Shaukat and Ali-Reza Adl-Tabatabai, former CEO of Gitar (now part of Sonar) and former head of Uber's developer platform, moderated by McKinsey. Research with Sonar found the teams getting real results from agents change three things: their process, their tooling and, most often overlooked, their people and roles. Tariq explains why lighthouse teams alone don't spread new habits, and why engineers need to make implicit knowledge explicit and get great at critical thinking, because AI always sounds sure. Ali covers how big companies can borrow from small teams through their platform orgs, and walks through how trust builds step by step: from AI reviews, to blocking on issues, to autofix, to auto-approve and auto-merge.

In this talk:
• Three factors behind teams that scale agents: process, tooling and people
• Why role models and lighthouse teams aren't enough on their own
• The skills that matter now: explicit thinking, critical thinking, generalists
• How trust grows from AI code review to fully automated merges

SPEAKERS
Tariq Shaukat, CEO, Sonar
X: https://x.com/tariqshaukat

Ali-Reza Adl-Tabatabai, Former CEO & co-founder, Gitar (now part of Sonar)
X: https://x.com/aadltaba

LINKS
Sonar: https://www.sonarsource.com
Gitar by Sonar: https://www.sonarsource.com/products/gitar/
Sonar on X: https://x.com/SonarSource

CHAPTERS
0:00 Intro
0:57 Research: what helps teams scale
1:51 Process, tooling and people
3:04 Meet the panel
3:19 Lessons from Sonar's own transition
5:38 Lighthouse teams aren't enough
6:18 What big companies can learn from small teams
8:37 Measure first
9:36 Automate whole workflows
10:21 Automate the grunt work
11:04 What this means for people and orgs
12:43 Make the implicit explicit
13:08 Critical thinking
14:28 The era of the generalist
15:07 Will we trust agents to validate code?
16:02 From reviews to blocking to autofix
17:52 Auto-approve and auto-merge
18:36 Where this is heading

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,569 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=1s)** [music] >> Um we'll get started. I'll introduce my fellow panelists in a second, but just to set the context of what we are going to talk about. Um you know, in the last 6 months or a year or so, almost every company has been trying to deploy AI or agents in their workflow. Um we did some research on this, and I'm sure it's the same for a lot of organizations around the world that they have seen this. Basically, 80-90% of the companies that you ask, they say we have deployed AI or agents in some shape or format. But when you ask them how many of them have actually scaled, or how many of them are seeing business impact from it, it's less than a third. Um right, and there are a lot of reasons

**[0:48](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=48s)** behind that. We have seen a lot of companies doing it in POCs and small environments, but not actually across end-to-end um organizations. So, what gives, right? Like, what was the reason why that doesn't happen? Um we worked with Sonar um Tariq to figure out what are the key factors that actually helps organizations scale if you're deploying AI in your software development life cycle. Um and we saw some really good results. Not surprising, right? Like, anybody who's doing this at scale is actually seeing pretty good results in terms of PR throughput, PR cycle time, um self-reported productivity gains in tasks in the SDLC. Um and we put these organizations on a scale of maturity, essentially. So, if you think about where companies are today, most of them are in what we call Horizon 2, where you have human-guided and validated agents that

**[1:37](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=97s)** are executing tasks across SDLC. But very few companies are on the Horizon 3 on the right-hand side, where it's fully end-to-end automated workflow, right? With human oversight. Um and the things that we found when we were doing this work with them was there are three factors that actually help this, not surprisingly. One is redesigning your process workflow, which is you are not thinking about a traditional SDLC, you are thinking about redesigning the entire workflow end-to-end. You are thinking about how agents are changing that stuff. Second is tooling, obviously. Whether you have good agents, whether you have good harnesses, whether you have good context layers, etc. But the more critical thing that people have often overlooked is the people part. Right? So, when we were doing this work, we have recognized this across many, many, many pilots or scaling that we've done is that

**[2:25](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=145s)** boundaries of how you traditionally define your roles, what a software engineer was, what a product manager was, what a designer was, they have started to blur. And organizations that have recognized that those boundaries are changing and have actually remodeled their entire operating model around that are the ones that are seeing the promised land of 10x productivity from AI and agents. And And as we were doing this work with him, we'll talk about it a little bit more. We saw that, you know, people who were skeptical about this, like, "Hey, agents will do the task, but we don't need to touch anything else." They gradually then were converts into, "Okay, this makes sense. We need to rethink and reshape how our orgs are going to be organized." So, with that, I will invite our panelist Tariq CEO of Sonar, and Ali, CEO of Gitai, to the stage. We'll have a Q&A. We'll leave some time at the end for questions if we

**[3:14](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=194s)** can, so you guys should also ask, but please Awesome. Um I think to start with Tariq, I'll probably ask this question to you first, you know, for companies that are going through this transition, going to Horizon 2 and beyond, um what are some guidelines or learnings that you have that you can share with them on what things they should watch out for as they're transitioning toward a full-scale end-to-end orchestrated agentic pipeline? >> Hi, everyone. Um thank you, Prakhar, for having us here today as well. You can all hear me, I assume. You can hear okay? Yeah, okay. You need it higher? Okay. Little bit higher? All right, perfect. Um So, you know, we we as Prakhar said been going through this journey of how do you use AI responsibly in the organization? How do you actually uh transform an

**[4:01](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=241s)** organization? If you don't know us, we started off as an open-source project 18 years ago. Uh so, while we're very proud of everything we're doing in the AI world, it has been a bit of a transformation for our engineering team to get used to the new tools, to really figure out how to adopt it in a native way. And um a part of this has really been about being super clear about what the objective is. And the objective was never for us token maxing or anything like this. We don't really like that uh type of idea. The idea is how do you really generate real value. Um and so, see being super clear about what you're measuring was really important for us. I think the second piece is um being very deliberate about what the process is that we're putting in place, right? And if you heard my talk I just gave a little bit ago, we've orchestrated everything around how do

**[4:49](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=289s)** you actually do this guide verify solve model inside of our company as just like we recommend doing it inside of everyone else's company. And so, this notion of how do you construct the tooling is really important. How do you construct the systems that we're talking about is really quite critical uh as well. Um getting the team to trust the agents, right? As working with the McKinsey team, we actually looked at what we're doing and our team had built a bunch of agents themselves. But, there are things like PRD agents and how do we really capture what's in the PRD and use that to generate the e-vals that we're using to generate the the the um uh I output verification, these things um were not natural to the team. And

**[5:36](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=336s)** part of what we needed to do was set up these lighthouse teams to really try and highlight the best practice ways of doing this. Frankly, the part that has been most surprising to me is that I thought that once you have these lighthouse teams who were operating in this way, the other teams would be able to follow super quickly. >> Yeah. >> Almost through the role modeling. And what we found is that's not actually the case. That that role modeling gives you part of the way there, and you can set up the tooling, and you can do all of this stuff, but the next piece of of actually getting them to think differently, to understand why they're using these agents, etc., is one of the critical missing links here. >> Since the last time. Ali, maybe a question for you. We have seen that smaller teams actually have a much better chance of scaling agents because

**[6:25](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=385s)** there are less dependencies, less um challenges to overcome. What can organizations that are at much larger scale learn from those um teams, right? >> Yes, so first of all, uh it's great to be here. Uh I'm Ali. I was previously the CEO of Gitarr, and now we're actually part of Sonar. Um and uh before joining Sonar, I was the CEO of Gitarr. In Gitarr, we were a small startup. >> Yeah. >> Um only about five, six people. >> Yeah. >> And uh we were building an agentic solution for validating PRs. Uh so, the entire workflow for PR validation. And then before that, I was at Uber, where I was responsible for the entire developer platform organization. So, it's an organization I built responsible for

**[7:12](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=432s)** you know, making sure that all developers are productive and happy, and that the company is moving at a very fast pace in terms of velocity with high quality. So, I've kind of seen both um large company and running developer organizations in a large company, and then operating in a startup world. And uh when we started Gitarr, uh we actually weren't AI-first, and then we quickly transitioned to become AI-first. And once we made that transition in terms of adopting AI internally, as well as building AI products, we saw both an acceleration in demand, but also we were able to get a tremendous amount done with a much fewer, smaller sized team. So, I've kind of seen both sides of things. And I think as you think about how do you take the learnings from a small

**[7:59](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=479s)** company and scale it up into a large company, actually large companies have a structural advantage because typically as you scale your engineering org and you get to a large enough size, you have a platform team, which was exactly my responsibility when I was at at Uber and you know, the roles I had in the past like at Google and Facebook were all about platform organizations. So, there's already an organization there that's responsible for driving standards and making sure that developers are productive and and happy. And I think there's a couple of principles that are important to follow as a platform team when you're looking at how do we adopt these tools? One is to have really good metrics in place. I think you you mentioned it, but this is not always an obvious thing for large

**[8:48](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=528s)** organizations because it's actually very hard to drive enough standards across the organization so that then you have telemetry that you can actually get to understand how fast am I able to ship code into production? What is the productivity of engineers in terms of throughput? What does the quality look like? How often am I erring and going back to the beginning of my workflow? And what's the sentiment of engineers? As we are speeding things up, making things more productive, are engineers actually feeling it? So, I think it's very, very important to have that kind of developer productivity and metrics in place as a baseline so that as you add AI and agents into your tool chain and into your PDLC, you can actually measure and and iterate and quickly improve and adjust. So, I I that's number one.

**[9:36](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=576s)** Number two, I think again you mentioned is very important also to look at it in terms of the entire life cycle and not in terms of introducing tools into one specific part of the life cycle. So, think in terms of the entire life cycle and in terms of entire workflows. So, how can you automate entire workflows and take make developers more efficient by offloading entire workloads to agents that can autonomously act and deliver outcomes that are the outcomes of those workflows. And I think the third thing um I you know, in my experience as part of a platform having run platform teams in the past is to make sure you're actually paying attention to developers' time. And optimizing for keeping developers in the flow >> Yeah.

**[10:22](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=622s)** >> and automating away as much grunt work as possible. Um and >> to do grunt work. >> No, but agents are perfect for that, right? So, if you can really deploy agents to taking entire workflows that are grunt work off the plate of uh folks, then that's where you get I think big not only productivity gains and velocity increases, but also developers feel it and you get the high sentiment, which is equally important if not the most important thing I would say. So, that's how I would kind of approach the problem. >> Yeah, makes sense. Um I think maybe a question for you. So, as agents get more embedded into the workflows, the LLMs get better at their job. We assume that there will be a point when you have a fully automated end-to-end orchestrated SDLC or PDLC.

**[11:10](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=670s)** What implications does that have on people, on org, on operating model of the future for any software organization? >> Yeah, I think um there's there's a you know, the models are clearly getting better. Uh I recommend Tropic talked about the fable models and you know, I'm looking forward to getting my hands on it to start start using it, right? Um I I think you can you can see a world in which this this software factory idea really starts to come to life. Um I think you used the keyword, in my opinion, which is orchestrated, right? Um because I don't think that there's going to be a world in which you can be completely hands-off. I think the question is how much do you leave to the machine, how much you leave to the agent, and how much do you um how much do you control on the outset.

**[11:59](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=719s)** So, what is the specification, what is important to you, what does success look like are all really important elements. You have to, I think, continue to have people who are involved with this. So, from a skill set standpoint, there's a lot of talk about how software developers need to become architects and and orchestrators and managers of agents, things like that. And I think there's a lot of truth to this. One thing that I think is an incredibly important skill set is there's a lot that we keep in our head. If you think about how you design software, how you build software today, there's certain things that are in your PRD, and there's a bunch of things that you just know, right? My company likes to do things this way, my company likes this sort of code, we like this dependency, we like the whatever it is. And there's going to be a lot more that needs to be made explicit as opposed to implicit, right? And that's actually there's a skill set

**[12:48](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=768s)** associated with this. So, I think in addition to being an architect and all of that, you have to start thinking in a much more explicit way. This is thing number one. I think thing number two, you know, my kid my my oldest son is about to go to college and he's like trying to figure out what to study and all of this. And the piece of advice that I keep giving him is the most important piece is to be critical amazing at critical thinking, right? Because the the point that I read on Twitter and I'm I'm shamelessly stealing it is that AI always gives you very high conviction plausible output, right? Um it always sounds correct, it never admits to any doubt whatsoever, it never says I think the answer is this." It always just says, "The answer is this." And I think the job of the people in the system is going to be to say, "Where do I need to question it? Where do I need

**[13:36](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=816s)** to um well, where do I need to poke? What are the things" kind of the same way that you do this with your team, right? If you have somebody joining your team, you have an intern joining your team, you're going to kind of know where to poke. You're going to know where to look. What questions to ask, what to look for. I think that skill set is also super important. Last point to the question you and Ali were talking about, you know, um there's a lot of resistance that I see in the organizations we work with to this idea of smaller teams, right? Um and this idea of of working in a smaller atomic unit. I think the the the the pushback when you get underneath it, in my experience, is almost always, "But I'm a front-end person and I'm not a back-end person or I'm a this you know what I I'm and we

**[14:23](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=863s)** have historically gotten to a world where we segregate roles quite a bit. We silo people. And I think this is the era of the generalist, right? And I'm not saying that somebody who knows nothing about software generalist, but like your software engineering generalist is, I think, going to be a much more important uh thing than do you know, you know, are you super deep in front-end or server-side or whatever it happens to be. >> Yeah. >> Um I think following up on that, Ali, I know you've talked about this at other forums as well. A lot of the coding part of the SDLC is, quote unquote, solved. And so, focus, rightfully, is shifting now towards other parts, um the requirement generation, the validation, the testing, etc. Do you think we are at a point or we will get to a point in the next 3 months, 6 months where the trust in the agents to automate all of this will go high?

**[15:11](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=911s)** Because right now, I think everyone is skeptical of whether you can automate your validation, your testing, your integration testing, etc. How do you see that? Has it shifted already or is it on a curve to shift? >> I think uh trust is the the keyword here. And uh trust I think is going to come time. And so uh you know, what we're seeing is our users uh over time as they work with the tools uh and they see the precision of the AI, it's that precision that gives them the trust that then uh allows them to unlock more and more levels of automation. >> Yeah. >> Uh to the point where, you know, changes can completely autonomously kind of flow through into your code base into production. >> Yeah. >> Um for example, um in with our users in

**[16:00](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=960s)** Guitar and the automation that we have in Guitar, the typical pattern we see is at first they just use reviews. And look at the CI failure analysis that we produce. >> Yeah. >> Uh and over time when they see, "Okay, actually these are very precise actual bugs in the code that are being uncovered." They say, "Okay, uh I'm actually not going to give the agent some teeth. I'm going to now set up some rules to block if there are any issues that are uncovered by the agent." So, now you've kind of moved one step in the automation to Not only do you have reviews that you trust, now you're actually trust them enough that they're high the signal enough that you're blocking. Then typically what happens is they start playing around with automated fix

**[16:46](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=1006s)** uh features. Okay, let me let me ask the agent to go ahead and fix some of these issues. >> Create a PR to see how >> Yeah, fix the CI failures, fix all the issues that you're uh uncovering. And then when you see the precision of that, that okay, actually the fixes are working as well. Uh it's producing fixes that don't introduce new problems, they pass build, um and they can iterate to actually pass the build until it's green, then they unlock auto fix. So, now they've taken one more step towards, "Hey, I'm going to When a PR is created, a review happens. If there are critical issues, it gets blocked. Then the system start iterating and makes everything green, fixes all the CI failures, all the um you know, good review issues. And now you've delivered green PRs that are ready for somebody to approve. And then here's where the big shift is

**[17:34](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=1054s)** beginning to happen now, which is you know, uh there are some parts of the code base and some kind of PRs that I'm comfortable having the system approve. Right? And so now we're beginning to see users put in rules to say, "You know what? If you're touching this part of the code base, it's not critical. Or if the PR is making this type of change, go ahead and automatically approve it." So now you've gone from PR creation all the way through approval. And now only thing that's left is somebody to come in and and merge. And that's the next step as well that we're seeing happen, too, which is go ahead and merge, fix any kind of merge conflicts. And now what you've got is fully autonomous end-to-end PR creation through merge is fully auto- automated. But it doesn't come immediately. Right? It comes with using the system, building trust that the agent that

**[18:22](https://www.youtube.com/watch?v=XqF-IFHBCkM&t=1102s)** you're working with is actually uh precise. Um there's enough context that's flowing in. You know, I've set up enough rules and guardrails that I'm now comfortable with the system being fully autonomous. Right? So I think to answer your question, we're rapidly approaching that. It's I think within the next year uh we'll see more and more teams, you know, along this journey. And some of these uh teams that I'm seeing are actually in large companies. Which is uh pretty interesting. >> Um I think that's our time. Thank you so much for being here and answering questions. Thank you. Thank you all. >> [applause]
