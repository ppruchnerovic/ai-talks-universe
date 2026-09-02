---
id: kVVqs1zqV3U
title: "AI Launchpad 2026: Pavo"
slug: ai-launchpad-2026-pavo
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 11
published_at: 2026-06-23T22:57:04Z
video_id: kVVqs1zqV3U
url: https://www.youtube.com/watch?v=kVVqs1zqV3U
youtube_url: https://www.youtube.com/watch?v=kVVqs1zqV3U
tags: ["AI"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# AI Launchpad 2026: Pavo

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `11 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=kVVqs1zqV3U) · [Conference site](https://www.aicouncil.com/)

## Description

Pavo builds systems-first intelligence for the enterprise: self-evolving knowledge systems, agent societies, and world models that learn from experience to optimize business outcomes.

SPEAKER:
Rishabh Mehrotra - Co-founder & CEO, Pavo AI

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,004 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=0s)** I'm Rishabh. The same guy over there. Uh I'm the co-founder CEO of Pavo AI. And my background is in machine learning. Did my PhD about 12 years ago around machine learning. Uh as Yang mentioned, spent some time at Sourcegraph building coding agents. Prior to that, I was at Spotify trying to make you guys listen more podcasts and more music. And uh because why not? Like music is fun. There's a piano over there. Now, one of the biggest learnings I've had in the 15 years of my career so far in the industry is the importance of these production systems and how hard it is to improve them. Right? I mean, if you spend 5 more minutes on a platform like Tik Tok, that 5-minute time spend is of insane value to the platform and they can monetize it a lot more. Now,

**[0:47](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=47s)** this is where a lot of these systems are very hard to improve. And this is what we're going to talk about in the next 10 minutes today. Right? How do How do we compound systems and improve them over and over again? And that's what we built Pavo for. You give Pavo a system, a production system, it'll understand it, it'll try to improve it, and keep on improving it. And that's what we call compounding systems intelligence. Now, each of these businesses have a bunch of these metrics, right? I mean, these are the four keywords which pop up in literally almost all the quarterly reviews and the board meetings across all companies. And behind each of them are these systems which are powering these metrics. Right? The pricing system, notification system, the fraud system, the personalized ranking systems.

**[1:35](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=95s)** The subscription modeling systems. Now, why do you care about them? Because if you make these systems half a percent or 1% better, the company makes a lot more money. Right? I mean, we are all capitalistic at heart, hopefully. Then, improving these systems a lot of like economic value to these companies. Right? And this is This is true across all of the companies across the the sector. Right? I mean, look at search, fraud systems, credit underwriting notifications, forecasting, pricing. There is just a common aspect like you improve these systems and the businesses improve their bottom line and revenues. Now, why is this hard to improve this system? It is hard because to improve each of them, you have to go through the loop from hypothesis to data to try approaches to evaluate whether any of them is useful, to actually test in production, and then see if it worked,

**[2:23](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=143s)** encode it back, if it didn't work, go back and redo it, and that run the loop again and again and again. And this is where the best of tech companies on the planet have been running these systems, but most teams can only run them, and I fit this loop once or twice per quarter per system. And that is the industry-wide bottleneck. Now, why is it hard? There are two problems here. One is knowledge. The other is agency. The knowledge of how does the system work? And the agency of running the loop, and that running the loop is very very brutal. Right? And if you take a step back, I mean, your your your systems are a bunch of code files, a bunch of experimentation logs, your the the logs that spit out on DBT Labs, on your data warehouse, half-run notebooks, the story of what was being done, the user

**[3:12](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=192s)** stories, and this is all the scatteredness around each of these production systems. Right? I mean, in the literally like the the AI Council has talked about a bunch of semantic labs or semantic layers and DBT models. But these are just touching one of these dimensions of entire systems, and to iterate a system, you have to understand it deeply. Even if you understand the system well, you still have to run the entire loop, and running the loop is it's hard, right? I mean, it's hard even to to make a presentation work here. Uh Now, running the running the loop is hard because something is happening, and I'm not sure why. I'm just going to stay around here. Stay with my laptop. Uh now running the loop is hard because of n number of reasons. One of them being that you have to run

**[4:00](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=240s)** each of these steps, right? And there are different individuals running these steps in in inside your companies. Right? You have data scientists and data engineers and ML engineers and DevOps and back-end engineers. And this is why most of the opportunities which you have, they never get explored. And you leave a lot of money on the table. Right? Now what needs to change? What needs to change is not the loop. The loop remains sacrosanct. That has been the only thing which has been working in the tech industry for the last few decades. The question is who can own the loop? Right? Who understands the systems? What can it do? This is where we want Power to compile the tribal knowledge of what a system is, how it works, and then run the loop. Right? And then keep running it. Keep trying out ideas, improving my system day in and day out. This is what we mean by compounding system intelligence. Right? This is where Power comes in.

**[4:48](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=288s)** It's a systems improvement platform which will first try to understand what a system is, try to try out ideas, ship to production, and then encode what works, and keep on compounding. Now high-level, it's a three-step process. We connect to the system, we create a tribal knowledge understanding of your systems, and then we execute work. Now let me walk through what each of them looks like. One is let's start connecting, right? I mean we we have access to the code bases, the experimentation logs, uh the the the the data warehouse, the dashboards. To run a system understanding, you have to get connected to most of your engineering systems here. Right? And this is where like over the last year and a half, we've been building these self-deploying substrates so that you don't have 50 forward-deployed engineers deploying

**[5:35](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=335s)** these across 50 companies. So a lot of autonomy has gone into developing this deployment substrate. Discovering, right? You're literally entering wild systems inside companies, and you're trying to discover what even exist. Then you're trying to understand the hierarchical distillation from code to pipeline logic to data to business and consolidating it together. This gives you access, just access. And once you have access, then you start compiling this book of tribal knowledge. This is a cheat sheet of one search system. Right? What is the ranking logic? Where is my ranker deployed? Hey, what sort of goals do I have for my team right now? What sort of metrics are we running right now? Hey, we have run a bunch of AB tests and experiments over the last year and a half. What have we learned from them? This is hard because this is spread across your code bases, your data infrastructure, your engineering systems. And look, I mean, this is what

**[6:23](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=383s)** I needed to know when I was working on your Spotify radio and making it better. And once you combine it together, that gives you the book of tribal knowledge. Right? And now to make this happen, you're looking at multi-level knowledge artifacts. You've done some innovation on experiential learning agents because knowledge is hard. Just knowing what exists doesn't give you the right to improve the system. You have to earn new knowledge by applying and experimenting. So, that's why you start deploying these experiential learning agents inside tribal knowledge. And once you have that, then you also have to make sure that this knowledge is correct. Right? And you literally don't have ground truth when you are entering a customer systems. Right? You're trying to understand and create these autonomous ground truth on the fly. Now, once you compile tribal knowledge, you get knowledge. And that knowledge gives you zero economic value. Because knowledge doesn't mean anything unless

**[7:11](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=431s)** you act on it. And once you have start acting on it, now improving your system is hard because you have to go investigate what's not happening. Where have you left money on the table? Come back with ideas, try out these ideas, do a bunch of offline evaluation, try some of these in production, and then see did it work or not? If not, go back to the drawing board and redo that again and again. This is a complex loop of execution which you have to run well. Now, this is where like we've done a bunch of work around learn task decomposition, trying to decompose complex tasks into modules. You're trying to do like budget-like exploration because you're taking bets. Humans have been taking bet. I was taking bet at Spotify. This might work, let me put in some more humans here. This may not work, let's just kill that project. Right? And then you're doing it in execution environments which are running inside companies. To do this, you're writing code, you're

**[7:59](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=479s)** thinking, you're communicating. You're writing production code, training production models, creating data sets, creating offline evaluation, creating agent pipelines. You're keeping the human in the loop. You're giving quantified results to the human so that they can remain in control of these systems. Then, to make it work inside enterprises, it lives in your infrastructure. It then shifts in your infrastructure. And then this is where the compounding happens. Every project builds on top of the previous state. If you're not compounding, then you're just running episodic tasks that won't lead to continuous system improvement. Just won't. Now, this is where we've done a few breakthroughs along the way to make this happen. Right? I mean, zero knowledge execution being one. That if you you can't Not going to go into details, but you just can't have agents access to environment variables inside your

**[8:46](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=526s)** companies. Right? We've done a lot of work around lifelong learning agents. In classical machine learning, you the environment changes is independent of the agent and learner. And now, once you agent starting owning the system, then the agent is causing the environment to change. So, there's a self-induced property of distribution change here, which is a new learning paradigm in itself. Then, you're trying to understand will a change I make make a causal impact in metrics or not. Right? Can you predict the causal impact of the intervention because that becomes a new bottleneck. So, we're developing system-level world models for each of the systems we are iterating on. Together, this gives you the view of like you own a system, you try to understand tribal knowledge, you try to try out a few different iterations in production, and hey, that gives you a metric win.

**[9:34](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=574s)** And then you go back and iterate. This is loop two. Loop two doesn't take you any much longer because you already run loop one once. This is where compounding actually becomes real. Right? So, we've done a bunch of work over the last year and a half with a bunch of customers touching feed, marketing, email optimization, lead scoring, developing a bunch of task, developing artifacts, impacting metrics, and then looking at total number of users which power systems have touched. So, this is where system compounding comes out and plays in production. So, we are hiring. We are onboarding new partners. Today, the focus is entirely on consumer and marketplaces companies. So, if you are a champion, if you are a VP of product, if you are a good talent trying to work on system iteration and world models, we'd love to kind of talk with you and and take the discussion private.

**[10:24](https://www.youtube.com/watch?v=kVVqs1zqV3U&t=624s)** Thank you. >> [music]
