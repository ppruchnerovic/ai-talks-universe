---
id: AYFcmnQrZCg
title: "AI Agents Will Upend Investing Even More Than Coding - Frank Long, Coatue"
slug: ai-agents-will-upend-investing-even-more-than-coding-frank
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Frank Long"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-11-06T00:00:09Z
video_id: AYFcmnQrZCg
url: https://www.youtube.com/watch?v=AYFcmnQrZCg
youtube_url: https://www.youtube.com/watch?v=AYFcmnQrZCg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Frank Long", "Coatue", "AI in finance", "hedge funds", "investing", "AI agents", "LLMs", "data pipelines", "semiconductors", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration"]
transcript: true
---

# AI Agents Will Upend Investing Even More Than Coding - Frank Long, Coatue

**Frank Long**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Frank Long` `#Coatue` `#AI in finance` `#hedge funds` `#investing` `#AI agents` `#LLMs` `#data pipelines` `#semiconductors` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=AYFcmnQrZCg) · [Conference site](https://www.ai.engineer/)

## Description

Frank Long of Coatue, a technology investment firm across public and private markets, bets that agents will have an even bigger impact on investing than they did on coding. He frames a hedge fund as a function that takes in outside and inside context and returns what to buy, how much and when, then breaks it into gather, analyze and decide steps. Using Korean-language semiconductor news as a case study, he shows how each step can be run by code, statistics, an LLM or a person, why every one of those choices needs tuning, and why the goal is quality, not automation for its own sake.

Chapters:
0:00 Intro
0:52 A hedge fund as a function
1:31 Give agents the same access people have
2:23 Internal context
3:28 Breaking the function into steps
4:59 Case study: Korean news
7:24 Four kinds of runners
9:08 Don't automate for its own sake
9:26 Every choice needs tuning
11:43 What are you hill climbing against?
12:38 The real graph
13:16 Beyond investing

Frank Long

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,338 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=1s)** [music] >> My name's Frank. I work at Coatue, which is a technology investment firm across public and private markets. So, in our business, what you really need to do is be able to take high conviction bets on big themes and watch those play out. I think honestly a career is the same way. And last year when I joined Coatue, the bet that I wanted to make was I think that agents will have an even bigger impact in investing than they did at coding. I know that's a big statement. We're all here because of the transformat- transformative impact that AI has had in coding, but I really believe it strongly and today I want to talk a little bit about the framework that we use to

**[0:49](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=49s)** actually realize that impact. So, at a high level, you can think about a hedge fund as a function that takes in two parameters, context external and context internal, and spits out one tuple, selection, size timing. What stock? How much? When? Right? And I think this is a good framework to actually to ground our work, which is we're trying to solve this compression problem of how do you take all the information in the world and spit out this one simple tuple and the product that we that we provide is essentially a time series of this tuple that constructs a portfolio. So, let's start from the top, which is the inputs. Very simple philosophy. We use our screens, we look at stuff, we

**[1:39](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=99s)** do work. Every single thing that a human can see in pixels on the screen, an agent in your building should be able to see via API. Uh the analogy I use is imagine you brought the smartest people ever, the greatest investors alive, and you brought them into your company, but you gave them a computer without logins to 75% of your services. It it's almost how smart the system is if it doesn't have the tools to actually action that. So, the two parts, external context, right? No surprises here. Think the news, prices, filings, all of that should be easily accessible and not via dragging and dropping, copy and pasting, like directly via API. Internal context is just as important, right? So, this is your own firm

**[2:28](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=148s)** situation. So, that might be our current positions, potential liquidity and risk requirements we have around certain names, and past case studies or um you know, history with a certain sector or stock or management team. That stuff's all super important. So, this is the foundation and I think uh no credit to me, KKR has been an amazing leader on this for over a decade. It's both technological and cultural. We have an amazing data science team, amazing, amazing processes, amazing, amazing systems that bring all this in. And just as importantly, we have a culture that is super, super rigorous and built from the ground up to capture all this insight. For decades, we've filed every single note about every single trade, about every single decision we made or didn't make, about what went well and what didn't go well, and that's poised us to

**[3:17](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=197s)** expose us to AI. So, if you think about it, I probably can't just take all of those things, jam them into a context window, and get my magic three numbers and go home, right? It can't be that easy. You probably have to break down this function a bit further, right? So, maybe the first step is I take in that external and internal context, and I gather it, right? I want to gather it, I want to filter out what's relevant and not relevant. Okay, well, I pulled some news articles about the NBA. That probably isn't material to stocks, but oh, well, this is actually related to some local permitting that might actually impact data centers, like there's a lot of nuance in this gather step. Um then you'll see probably next step is I

**[4:06](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=246s)** need to analyze that information and form a view. Right? I actually need to think about what that means for the markets, public and private. Uh and then I need to take that view and turn it into a decision. A decision object has these three parameters, right? These three sort of sub sub pieces. So, you can see every single step has an input and an output and the input for the subsequent step is the output that the previous function generated. I think as an engineer, this is a way for me to conceptualize the problem in a way that makes a lot of sense. But even this it [snorts] really can't be as simple as writing three functions, right? So, let's just to up really appreciate the scope and

**[4:54](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=294s)** understand the full complexity of the problem, let's look into the first step, a tiny sub piece of tiny sub piece of just gathering information and let's do a case study on interpreting the news, right? So it's probably no secret to you guys that you know, news from Asia and Korean Korean media outlets has been super important this year because semis, AI have been a huge huge theme in the market, huge theme. And I think this is an area where AI is poised to have a lot of impact is reading uh Korean language news better than our completely non-Korean speaking staff, right? Uh I think I have a good thesis that this might be a good use case. So you can imagine the first step is

**[5:41](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=341s)** I have uh articles. I need to collect the articles, right? So, this could be an MCP, this could be a CLI, license the data feeds, clean the data feeds. There's actually a lot of ways to do this. And a lot of dimensions of freedom for how you can even just write this simple piece. How do I chunk it? When I pass it to the LLM, do I want to pull the images as images? Do I want to pull the images and then turn the images into text? There's actually a lot of knobs here, and I almost think about those knobs as like hyper parameters in a traditional machine learning system, right? I think about each of these knobs as something for me to tune and optimize against. Obviously, filtration, we talked about it. Korean

**[6:28](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=388s)** They're probably Korean NBA fans, right? There's probably a bunch of stuff that's not necessarily material to the the names and themes and stocks in our portfolio that really, really matter, right? So, I want to make sure that I filter those out. There's this like translate/extract/should I summarize? Should I extract this into some sort of structured form? Again, so, so many ways to do this, so many ways to experiment how to expose information to the model. And one of the reasons this is hard is it keeps changing. And obviously, checking. Checking like our own internal notes, our own internal views, potential conversations we've had, meeting recordings against these things. We actually need to cross-reference those things. Actually, the idea of pulling

**[7:16](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=436s)** information from disparate sources and cross-referencing them, that's super powerful. So, you'll see on on the right here I have code, LLM, LLM, code, person. There's many, many ways to run these functions. I think about Uh oh, yeah. And finally, update. Potentially, we update our views. So, there's many ways to run these functions. I think of each line as having a runner, and uh the most obvious one is code. Code is very good. It's fast, it's cheap, it's reliable. So, for something like if the price-to-earnings ratio is less than 15, I should just use deterministic code for that. Runner number two is statistics, classical machine learning, and

**[8:04](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=484s)** you can imagine fitting a line to a regression for specific pattern. This is very powerful because you can model much more complex relationships than just pure deterministic code, right? And for even more complex relationships, the reason we're all here, LLMs, AI agents, that's another type of runner, right? So, for something like summarization, that's the state of the art right? It's probably totally impossible to build a a bunch of if statements that can summarize better than a model modern LLM. And of course, uh people. People are important runners in the system, right? So, uh imagine a function meetings the management team of a company. I probably don't want to send, I mean, I like the new Unitree robots, but I probably don't want to see it send an LLM or an AI agent in to do that. I probably don't want to send an if

**[8:52](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=532s)** statement into that meeting. I think there's many cases where, because of judgment and the ability to navigate the real world and all of these things, a person is the best runner for a given piece of the function. And I think this is like a super super important point. There is no glory in automating things for the sake of automating things. The goal is not to take as many things and make them LLM as possible for us. The goal is, for any given piece of this function, what can I do to maximize absolute quality? And if you actually think about the function, it probably looks something like this. It's probably not just a linear statement of a bunch of different things. There's probably all kinds of branching logic and all kinds of ways to actually fork this. So, maybe I want to collect the

**[9:40](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=580s)** information and then translate it, and my main goal is to extract quotes and check those against sources to make sure that these are actually the things that people said, and and that's my approach. But that might be totally wrong. Maybe actually what I want to do is I want to dedupe, and then I want to filter, and then I want to pull external figures, or maybe I want to do something totally different. I actually want to I'm passing in a note first, and I actually just want to find other confirmatory data points, or maybe I'm trying to write team. Uh there's a million different ways to configure this. So, yet again, more hyper parameters within the control flow right? So, so many ways to think about just this very simple problem, a polling, filtering, summarizing, aggregating the news for LLMs. And each of these boxes

**[10:28](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=628s)** probably has an optimal runner, right? So, uh the optimal runner might be deterministic code for collection, right? I'm polling last 24 hours for a given source. That's deterministic code. Filtration, decision models, maybe. LLMs, statistical methods, a combination, right? So, this probably understates the complexity. The reality is most things are multi-runner. Most things have deterministic code plus LLM plus statistical method or human with LLM in conjunction. Uh the reality is this it's probably combinatorics between my four buckets, and there's even more buckets than that because within the LLM category, I can tune the model.

**[11:15](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=675s)** I can choose big model, small model, medium model. I can tune thinking effort. X high, high, medium. I can tune harness. I can choose the harness. I can choose which skills load with the harness. I can choose which hooks load with the skills. So, yet again, more hyper parameters within my search space. I have an absolutely enormous amount of hyper parameters within my search space. And this is just for this one tiny problem, right? I'm just filtering the news. So, the way uh to think about breaking down these problems is what can I actually compartmentalize in a way that we can understand and evaluate because that's what I'm hill climbing against, right? Otherwise, I'm just tuning these things. I'm okay, well, that should actually be a machine learning system instead of an LLM. That should be a little model that we train. Oh, no, that should actually shouldn't be a model at all. That should be an if statement or

**[12:03](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=723s)** Oh, man, LLMs are really, really bad at translating that to portfolio impact. It should really be a human on that step, but they're using uh a deterministic system to help them search and pull the information. It could be all different things, right? And if you don't have a North Star to hill climb against, you're just kind of you're just fidgeting around. And I think I cannot convey enough that this is just one tiny thing we do. Imagine every single data source that we pull in, there's probably more than just three transformations to get them to the intermediate output. So, the actual graph of Kensho and funds like Kensho, it actually probably looks Oh, not like this. This is my screensaver. The actual graph probably looks something like this, right? It's probably massively complex. In each

**[12:51](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=771s)** of those nodes, we just talked about at least 10 hyper parameters with at least 20 different valid values for them. So, the search space is is basically infinite. And figuring out how to actually lay this out in a way that you can comprehend both from technical perspective, but also absorb culturally, organizationally, that is the great challenge of applying AI in investing. And beyond investing, what we're really talking about is creating a state machine that can take information from the world and understand it well enough to make coherent decisions. There's use cases for this far and above wider than just investment firms. In policy, in nonprofits, in drug discovery, in corporate strategy, I

**[13:39](https://www.youtube.com/watch?v=AYFcmnQrZCg&t=819s)** think one of the most exciting things for me about being in forms like this is talking to other people in dis- different spaces with different problems that kind of congeal on the same problem space. I'd love to keep talking about this. I'll hang out in the hallway afterwards. Here are my socials, and thank you everyone for your time. >> [applause]
