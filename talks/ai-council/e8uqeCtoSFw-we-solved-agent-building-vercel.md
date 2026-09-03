---
id: e8uqeCtoSFw
title: "We Solved Agent Building | Vercel"
slug: we-solved-agent-building-vercel
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 12
published_at: 2026-06-18T22:16:13Z
video_id: e8uqeCtoSFw
url: https://www.youtube.com/watch?v=e8uqeCtoSFw
youtube_url: https://www.youtube.com/watch?v=e8uqeCtoSFw
tags: ["AI"]
topics: ["Agents & orchestration"]
transcript: true
---

# We Solved Agent Building | Vercel

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `12 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=e8uqeCtoSFw) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] The evolution of building our successful internal text-to-SQL agent that currently fields over 1200 requests a day from Vercel. From a simple prompt, to sophisticated agent, and all the steps we built and learned along the way.

SPEAKER:
Andrew Qu - Chief of Software, Vercel

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,439 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=0s)** I'm excited to show you how we Eversell solved agent building. Raise your hand if you've built an agent. Nice. A lot of you raise your hand if you've tried using an agent like Cloud Code, Codeex. Nice. So, we at Evercell, for those that don't know, we build primitives and technologies to help you build what's next. Everything that we build comes from a painoint that we've experienced ourselves building AI products, building agents, building web applications. And everything we built is to remove some of this undifferiated heat loss that you lose when you have to spin up your own DevOps, when you have to do your own model routing, when you have to do your own durable execution. Everything here is to remove those so you can focus purely on your product. We built this thing called the AI SDK. It's a simple way to only use one line of code switched to change providers, models,

**[0:49](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=49s)** and all different sorts of inference providers. We built this because we were building this thing called Vzero. It's a vibe coding text app app and we had to face the problems where every time there's a new model we switch out hundreds of lines of code in order to get the latest and greatest models in our code system. And so we built this abstraction so that you only have to switch one line of code and you get instantly the new model with the same DX and the same abstractions to work across every model. We built the AI gateway. We were tired of having different API keys for Anthropic, OpenAI, Fireworks, B 10. We just want a single way that we could just plug in any model and just get it routed to the most optimal, most close and uptime wise provider. We also built other primitives to build

**[1:36](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=96s)** agents securely. We built sandbox. It's a way to run code in untrust environments. We have firewall egress controls built out of the box and workflows. It's a way to run durable lambdas over the course of many months, if not years, and have it persist and not have to get timed out because of the 13-minute lambda timeout duration. And for a brief while, I was going around the company asking people, "What do you hate most about your job?" I was trying to do this thing where I automate some parts of people's lives with agents, especially now that some things cannot formally been uh automated with agents. And the most compelling use case I got to was our data team. Every single day, every so often, they get interrupted by sales, marketing, engineering, design, PMs to pull some one-off ad hoc metric, whether it's

**[2:24](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=144s)** about product metrics, customers, financials, leads, everything requires the data science team to sort of drop everything and write this query. And it was a big waste of time. And I felt like this is something that we think agents can be good at. you know, there's clearly lots of Texas SQL apps or agents out there. There is, you know, Hex, the sponsors of this conference, as well as TextQL. And we felt like we could build something a little bit more personalized to what Verscell needs. And so the first thing we tried was we literally just pasted the whole Snowflake schema into a generate text call and we just asked a question and we hope that it would generate working SQL. Our semantic layer is roughly I would say 300 entities deep and so you could think of it as a large amount of context and it was not very good at this. This is the very first

**[3:10](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=190s)** try. If we dumped it down a little bit, condensed what we were searching over, it was way better and it gave us conviction that we could sort of work with this and make it better. And also by the way this was like seven months ago. This was like pre-Sonnet 4 even. And so then we came to a conclusion that maybe we need to split out these steps. Maybe we need to have different system prompts and different sets of skills and tools in order to do different parts of the age exploratory process. If you think about what the data scientist actually does, they get a question like what is our AR growth month over month for the past 6 months. They break it down into the idea what they need to solve for. They go and explore the semantic layer. Then they eventually go and build the SQL, make sure it validates across all the join patterns and all the different schema definitions. And then they actually go and execute and report on it. And so we

**[3:59](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=239s)** broke down those several steps into separate sub aents. So each of the agents goes and does its processing. It comes back and it feeds into the next one. And that was good. But in between steps, it was hard to debug. And so by this point, models were good enough at holding more context during the actual loop that we were able to just keep it all into one agent run. We did this like multi-phase sort of thing where during the agent execution if it's past a certain point where it has a SQL we just strip away those tools and we only give it the ability to execute against Snowflake or to report. And so you can think of this as sort of progressively disclosing what the agent could do while it is doing the thing it's doing. And this was fine too but at this point it was still not good enough that we felt comfortable releasing it to the wider

**[4:47](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=287s)** company. And so then we were like okay but cloud code like hit this inflection point. It was like it was Opus 4.5. Everything you want to do could be oneshotted basically. And so we tried to just embed cloud code as our data science agent. By the way, we called it D0. You can see at the very top of the slides, it says D0. If I reference it, it's our data science agent. And so at this point, we were just embedding cloud code and it was amazing. You know, we were able to solve all of the problems that we couldn't solve before. We had an extensive eval set that was generated from a pre-existing data dashboard we used and for the previous generation sub aent the compaction the oneshot query it was missing out on over half the cases but this one was amazing you know we just had the same amount of data it was the same semantic layer dumped out into

**[5:34](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=334s)** YAML files and it was nailing every single question and we're trying to wonder why was this the big unlock why was cloud code the reason why the data science agent could actually be so good now and we learned that you can just use a file system. That's actually what just makes cloud code so good. And we eventually just refactored the whole D0 agent. We stripped away cloud code again. We like it was a fun experiment, but we want more control. We want more custom customizability. And we built a more minimal version that instead of having like 13 tools, one for join pattern analysis, one for loading semantic layer, one for exploring, one for checking the snowflake relations. We just dumped all the files into a sandbox and we gave the agent only read file, write file, grab, execute, bash. And this was amazing. At this point, we

**[6:21](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=381s)** basically hit PMF and we were like, "Wow, we can actually give this out to the larger Verscell audience and have them use it now." And I wrote this banger blog post um right after we did that big refactor and we published it. This was responsible for 70% of Versel page views that whole week as a small brag. And so as we evolved and as we started publishing this to more and more people internally versel we eventually hit the point where now it's getting 2,000 queries a day from internal verselians across things from customers products trends and what you see is that a lot of these people that ask questions there are certain buckets of things they ask you know if you ask about customers that knows to go and queries uh Salesforce if you ask about aggregation if you ask about trends over time there are certain sorts of patterns that you And so at this point we've started

**[7:08](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=428s)** distilling some of those common use cases into skills and we load those skills into DZ so it doesn't have to go and redo the same calculation the same sort of like weird is this an aggregation is this a customer question and it sort of knows the sort of subset of things that it needs to query against. We've even like automatically created this process where every single day we look at all the questions asked by people among Versel and we try to figure out what were the key themes and we always add more and more skills until we've eventually figured out every single sort of known data question you could ask. It's still ongoing but um we've so far distilled over 40 skills that cover every use case from customers to products. And so everything I talked about here is sort of a similar process that many of you will probably go through. You know, you'll probably build an agent from a

**[7:56](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=476s)** very simple step. You'll probably add more complexity. You'll probably strip it away, go to the file system, and then you'll add skills and then you'll add more tools and sort of like a sort of arduous process. Along this journey of building D0, a lot of teams at Versel also got the agent itch and they tried to fork off DZ and build their own version. And at every step along this process, it was sort of awkward because we would assemble these primitives, we would assemble these systems. They were still ever changing and there's no really no best way to build agents at the time. And so that's why we asked a question internally a few months ago like what if we built for agents what we did for Nex.js. What if we built a single way, a single framework that you can build agents in that uses all the best things AI SDK, AI gateway, sandboxes, workflows. You don't have to configure it. you don't have to use it

**[8:43](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=523s)** wrongly. You know, a lot of people when they forked off of D0, they use workflows in a weird way. They stump a sandbox when they didn't need to. It was a little weird to have to string together these things by yourself. You know, agents have sort of exploded in complexity. And we had to build these things to make them manageable. But now we're trying to compress it all back together. We're trying to bring back what makes Nex.js so good, but for agents. And so that includes awesome routing in zero boilerplate and one-click deployment to your favorite cloud infra providers. And so this is what it kind of looks like. This is a very early preview. You guys are probably one of the first people here hearing about this. It's akin to an nextjs for agents. So you start off with some highle concept of an agent.ts, s the system MD and then everything you put into skills, tools, sandbox,

**[9:30](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=570s)** channels, connections, they're all file system routed and they all get compiled at the end for your agent to work with. So the agent is the directory. You don't need to sort of figure out where to put your endpoint to call the agent. You don't have to figure out how to connect it up to Slack and that needs another endpoint. It's all automatically done for you because there's only a few ways you could do this correctly. And it comes with observability out of the box because it uses workflows for all the underlying execution. And this is how we sort of think about it. You know, if you actually think about what makes an agent, there's a few key pieces. There's a harness, as you all know, it's the actual agent that runs, but where it runs is actually in some sort of compute. And that compute should be durable. It should be resumable. It should be able to talk to a sandbox. It should be able to have MCPs. It should be able to have tools and spin-off sub

**[10:18](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=618s)** aents. And that's also something that if you were to do it by hand without virtual primitives or with them, it's a little awkward and you may do it wrongly or you may run to some rough corners. And so we think we have the best way to assemble all these pieces together layered underneath the harness. And then the other part which is the chatting aspect, the interface of it is also sort of a solved problem. We built this thing called the chat SDK. It is like a single library that lets you export to Discord, Slack, webhat API, even more platforms like Telegram and WhatsApp coming soon. And there's very there's a lot of configuration if you do this by hand. But we think if you combine all these pieces, then you get the amazing durability of workflows. You get to bring your own agent and bring your own harness and you get to get the UI and API out of the box for how to

**[11:07](https://www.youtube.com/watch?v=e8uqeCtoSFw&t=667s)** communicate with it. And so right now D0ero was actually rebased onto this new framework. Um it has a fun name that I won't reveal right now, but this is how it roughly looks like. So all of those 20,000 15 lines 50,000 lines of code were removed and translated into just a bunch of markdown documents, a couple TS files for scripts and tools and a bunch of channel configurations for how to respond to Slack, how to do the processing, how to do rich tables in Slack as well. And I hope to give you all a preview of the agent framework real soon. You know, we're going to release it in beta at uh limited capacity real soon. But um stay tuned for how to build agents better with the Nex.js for agents.
