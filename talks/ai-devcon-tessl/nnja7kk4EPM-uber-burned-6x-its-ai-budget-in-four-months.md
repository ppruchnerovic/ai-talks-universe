---
id: nnja7kk4EPM
title: "Uber Burned 6x Its AI Budget in Four Months"
slug: uber-burned-6x-its-ai-budget-in-four-months
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-28T13:30:32Z
video_id: nnja7kk4EPM
url: https://www.youtube.com/watch?v=nnja7kk4EPM
youtube_url: https://www.youtube.com/watch?v=nnja7kk4EPM
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Uber Burned 6x Its AI Budget in Four Months

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=nnja7kk4EPM) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

AI DevCon London had a recurring theme this year: what agentic coding actually costs, and where that money goes once it leaves the budget. Amit Kushwaha (Nvidia), Tammuz Dubnov (Autonomy AI), Luke Marsden (Helix ML) and John Groetzinger (Cisco) walked through the caching tricks, the budget blowouts, and the eval gates that decide whether that spend is worth it.

What we cover:
– Why cache-aware routing is the difference between an agent workload that's affordable and one that isn't
– Uber's AI budget, six times bigger and gone in four months
– Why only $18 of every $100 spent on AI reaches code that actually ships
– How Cisco lets evaluations decide when a knowledge-base change needs a human at all

Chapters:
00:00:00 - Introduction
00:00:23 - Amit Kushwaha, Nvidia: why caching is the make-or-break optimization
00:02:06 - Getting cache-aware routing right across replicas
00:03:12 - Tammuz Dubnov, Autonomy AI: Uber's 6x AI budget, gone in 4 months
00:04:57 - Only $18 of every $100 spent on AI ships to users
00:05:23 - Luke Marsden, Helix ML: open-weight models now handle 80% of the work
00:07:54 - John Groetzinger, Cisco: letting evals decide when a human needs to look
00:09:50 - Why reviewing text diffs on a skill wastes an engineer's time

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What's your actual dollar-to-shipped-code ratio right now?

## Transcript

*1,825 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=nnja7kk4EPM&t=0s)** Back in June at AI DevCon in London, we had several talks about the part that tends to get left out of the demo. The bill. Let's first hear from Amit Kushwaha, a principal solutions architect at Nvidia, on the two things that decide how much of an agent's work you actually pay for, whether your context is cached, and whether the request comes back to the machine holding that cash. My name is Amit. I'm a solutions architect at Nvidia, and we live in the Defense Department. So looking at that workload, there are few optimizations that are already kind of present in the production systems. And these are very critical to make that workload work. Again, going back to kind of the current setup that

**[0:48](https://www.youtube.com/watch?v=nnja7kk4EPM&t=48s)** I shared in the previous slide, in the first turn, this is your user input and you get an output in the second term. This whole thing could be cached. And this is the optimization that I'm talking about for most of the agent workloads. Caching becomes very, very important because what you are doing is pilot. By the time you are at the 40th turn, a lot of context has been created, but you don't need to do all the work. If you are caching your output inputs properly, then you only need to do work on the new tokens that are being generated in this whole workflow. So at the end of kind of this, this fourth term, for example, most of this is cached and you don't have to do any work on it. The new part is only where you run your GPUs and actually to make the work,

**[1:40](https://www.youtube.com/watch?v=nnja7kk4EPM&t=100s)** if the caching was not enabled, you can imagine a lot more work needs to be done, and there's consequences on one performance on time to first token and different kinds of metrics. So caching becomes kind of a must have in most of these agentic developments. And as you see, the vast majority of output input tokens by the end could be cached because it's just building up on the previous display. The caching itself is not the full story, especially when you are serving these models on multiple replicas. Your terms have to kind of get on the right replica. For example, if you turn one in, the previous slide landed on replica one, and this is just an example of you could have a model serving multiple times. So these are three replicas

**[2:29](https://www.youtube.com/watch?v=nnja7kk4EPM&t=149s)** of the same model that you are using neural network things. So turn one ended up on replica K. If you do a round robin kind of a setup the turn you might end up on some other replica. But this replica does not have the cash that we talked about. So the other thing that becomes very important in a kind of setup is to make sure that your turns land on the same replica where your cash is stored. So this is what is kind of shown here in the cave where routing, where turn one lands on replica one, we make sure that the turn two also lands on replica one, so that we can leverage the cache that is stored already on that side. We also heard from Tammuz Dubnov of Autonomy AI, with the numbers that made the room go quiet. Uber increased its AI budget by six times

**[3:19](https://www.youtube.com/watch?v=nnja7kk4EPM&t=199s)** and got through the whole increase in four months. And of every $100 spent on AI, about 18 reaches code that actually ships. Now, in the rush to AI Native, some people are doing it wrong and it can be really, really expensive. Everybody heard of Uber and what's going on there? Okay. So this came out just to I think 3 or 4 days ago. Uber has increased the area spend since 2024 by six x. Now that seeks X growth was completely used within four months. They are out of AI budget for the rest of the year. And we asked them what the impact is of training with like fully a need that everybody get all the tokens you want. That's like the upward CFO conversation that you guys have magically not had. You will get an answer saying

**[4:08](https://www.youtube.com/watch?v=nnja7kk4EPM&t=248s)** AI costs are getting harder to justify, people are more and more tokens. But me as a business leader, I'm not seeing how there's a link to actually moving faster on features. And that's the really, really big gap. It's just throwing more LLM compute that's not fixed organization. You actually want to be a native and give the people who can decide the ability to execute Microsoft. And a similar phenomenon, they gave everybody cloud code. And now they're taking it away. Because just giving cloud code to more and more people in an organization is a wonderful way to burn money. It is not the right way to speed up the work. And now if we actually want to see like what is all these token budget, where is this bending going to? Somebody is not a deep dive managing over 2400 companies and how they use AI. And you can see from any $100 that you spend on AI, only $18

**[5:03](https://www.youtube.com/watch?v=nnja7kk4EPM&t=303s)** actually goes to meaningful code that actually gets shipped to users. A lot of it goes to stuff that gets reworked bugs that AI also generated, and you get this wonderful loop of spending more and more money in less because of the alignment and basically how the model is trained. Luke Marsden, CEO of Helix ML, is running a bootstrapped company, so he feels every token. His finding is that open weight models on hardware you own now handle about 80% of the work. So take three months of token budget by the machine and keep the ability to reach for a frontier model when you genuinely need it. most of my day now when I'm doing technical work is that I'm reviewing these specs, and I find the two lines in the spec where the agent got it wrong, or is making a poor design decision, or

**[5:56](https://www.youtube.com/watch?v=nnja7kk4EPM&t=356s)** is unaware of some other area of the code, and you just comment on those two lines, and then it then becomes fairly mechanical for the agent to get the code change all the way through to to being close to being ready to merge. So and then the pull requests that come out of it are quite nice, because we put quite a lot of effort into telling the agent to take screenshots of changes that it's made. So I quite often review pull requests now by just looking at whether I like the change. And that's quite powerful. And you can also link, we also link automatically to the spec that was used to to construct it. Now I want to talk briefly about token costs, privacy and Donald Trump. The total costs are exploding.

**[6:51](https://www.youtube.com/watch?v=nnja7kk4EPM&t=411s)** We spent a lot of money now on tokens, which as a bootstrap startup is kind of painful. But we also have one of these machines, these open weights models like GLM 5.1 and so on, and can now do pretty much 80% of the work that you need to do. And so if you take as a meaningfully sized organization kind of your next three month token budget and instead invest in some hardware with like eight RTX six K pros in it, and then you use something or you build something that allows you to easily switch between different agents and different models. Then you can avoid getting locked into, like the OpenAI anthropic ecosystem, but you can still kind of burst out to like Claude

**[7:41](https://www.youtube.com/watch?v=nnja7kk4EPM&t=461s)** Opus 4.8 if you've got something really hard. But for all of the tedious stuff, you should be using local models where you just have to pay for the electricity, in my opinion. to close, John Groetzinger at Cisco, on spending your humans as carefully as you spend your tokens. When a knowledge base article changes, a model, rewrites the matching skill and runs the evaluations. Small changes that pass release themselves. A person only gets pulled in for the big ones. So a lot of people will say wikis over docs go to die. And of course, largely I do agree with that because people just don't really maintain docs. But when you have a strong culture like we do, our docs are not really dying or actually seeing the opposite. Our docs are becoming more important to ground the agents, but what we're seeing is that a lot of people are building agentic systems

**[8:30](https://www.youtube.com/watch?v=nnja7kk4EPM&t=510s)** that blindly try to use any content, or they'll have agents that build their own memories on supporting stuff, using that, and then the memories drift from the content, and then you end up having some answer come out to a customer. And that's just completely unaligned with the article that it says it uses a source, and then everyone just loses faith in the entire system. Right? And that's the problem we've been struggling with for the last couple of years. So we're trying to figure out how do we keep these more in sync in a way that we can actually trust it. And that's what the system that these engineers built is that when the article changes, we kind of pipeline that, right. Think of like a GitHub action triggering when we update a knowledge base article that goes into a pipeline with an LLM that reviews the changes, determines if it's a minor change, moderate major, and then makes the change for itself to update its skill. And then it runs the evals. If the evals pass, great, everything's good. If it's a minor change, just changing a typo or wording

**[9:19](https://www.youtube.com/watch?v=nnja7kk4EPM&t=559s)** and the evils pass, I don't really need to have my human gate. That new version, just let it automatically release. But if you're doing a more complex change, a major change, maybe you're introducing a new topic. Maybe that's something that you need some more quality control. And that's where you insert your human right. Your humans either go far on the left or far on the right, but in between you should not be wasting your time, should not be caring about a text diff. If your engineers are reviewing text diffs on a skill, you are wasting a lot of time. That is just unnecessary, at least in my experience. So new topic means new eval, right? You need to build a new evaluation. Of course you can let the LM do that, but you need to really tell it what success looks like in order for it to build a good evaluation. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
