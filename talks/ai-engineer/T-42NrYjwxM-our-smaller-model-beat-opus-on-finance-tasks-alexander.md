---
id: T-42NrYjwxM
title: "Our Smaller Model Beat Opus on Finance Tasks - Alexander Shevchenko, Ramp"
slug: our-smaller-model-beat-opus-on-finance-tasks-alexander
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Alexander Shevchenko"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-11-04T22:00:34Z
video_id: T-42NrYjwxM
url: https://www.youtube.com/watch?v=T-42NrYjwxM
youtube_url: https://www.youtube.com/watch?v=T-42NrYjwxM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Alexander Shevchenko", "Ramp", "Ramp Labs", "applied AI research", "post-training", "Qwen", "KV cache", "cartridges", "AI agents", "agent swarms", "penetration testing", "open-weight models", "AI in finance", "AI Engineer", "AIE NYC"]
topics: ["Inference, serving & GPU infra", "Science, healthcare & applied ML", "Security, safety & red teaming", "Training, fine-tuning & model building"]
transcript: true
---

# Our Smaller Model Beat Opus on Finance Tasks - Alexander Shevchenko, Ramp

**Alexander Shevchenko**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Alexander Shevchenko` `#Ramp` `#Ramp Labs` `#applied AI research` `#post-training` `#Qwen` `#KV cache` `#cartridges` `#AI agents` `#agent swarms` `#penetration testing` `#open-weight models` `#AI in finance` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=T-42NrYjwxM) · [Conference site](https://www.ai.engineer/)

## Description

Alexander Shevchenko of Ramp Labs explains why an application company still runs applied research instead of waiting for the next frontier model. He walks through three projects now in production: a post-trained Qwen 3.5 model that beat Opus 4.6 on financial question answering at Haiku-level latency, KV cache "cartridges" that pack 20 to 30 times more context into an agent ahead of time for tasks like month-end close, and swarms of 10,000 parallel agents that pen-tested Ramp and found seven high-severity vulnerabilities, with cheaper open-weight models catching nearly as much.

Chapters:
0:00 Intro
0:36 A bitter-lesson company
1:15 Why not just wait?
1:29 Building agents in 2023 vs 2026
3:06 Project 1: A specialist model for Ramp Sheets
5:16 Beating Opus at Haiku speed
5:58 Project 2: KV cache cartridges
7:50 Project 3: 10,000 agents pen-testing Ramp
9:30 Cheaper open-weight models in swarms
10:08 Saving time and money
10:36 Token spend management and Ramp Router
12:03 More from the Ramp Labs blog

Alexander Shevchenko

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,319 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=T-42NrYjwxM&t=12s)** Hey everyone, I'm Alex from Ramp. Um I'll be speaking about chasing capabilities while waiting for the frontier to advance. So, quick uh intro about myself. I joined Ramp around 3 years ago uh on the broader applied AI team working on a bunch of different surfaces and products applying LLMs and ML to make a great product even better. Uh to and to to caveat my presentation on Ramp Labs, Ramp is an extremely bitter lesson filled company. Over the last year, the number of use cases that use LLMs has increased 123%. While at the same time, a lot of our top features are growing in token spend, but on a unit economic basis, they're actually becoming cheaper because there are frontier models that are being released

**[1:00](https://www.youtube.com/watch?v=T-42NrYjwxM&t=60s)** uh all the time now, and these models are cheaper, faster, uh and better. And so, we're able to provide the same level of accuracy at a much lower cost. And so, this is a really bitter lesson filled uh pattern. And so, given all this, a question that I sometimes get, why not just wait? Why have an applied research function inside of a company like Ramp, an app application layer company, right? Um and to answer that, I would like to draw draw a parallel to 2023. Back in 2023, uh you had access to kind of like GPT-4, and creating an agent was a lot of work. Um you would have to create very, very strict guardrails. Models weren't

**[1:47](https://www.youtube.com/watch?v=T-42NrYjwxM&t=107s)** allowed to backtrack. They didn't have thinking tokens. And so, if it went in the wrong direction, it would just kind of charge ahead and not realize that it made mistakes. You had to sweat over all of the prompts where to the point where um s- some synonyms could change the behavior of of your agent because the they weren't RL'd properly on generalizing to the user's intent. You had to reduce and scope down the context as much as possible because giving too much context to the agent would just confuse it. And even back then, we decided, well, we need to ship these things. We can't wait for GPT-4.5 or GPT-5 to come out. We need to serve our financial professionals now. And we shipped things like Ramp Tour Guide and

**[2:35](https://www.youtube.com/watch?v=T-42NrYjwxM&t=155s)** many other agents even though it was not the easy thing to do. And fast forward now to 2026, building an agent is a lot easier. The models have gotten so much better that you can kind of give them MCPs and access to kind of any context and they do a very very good job of understanding what they need to do given a task. But, I still believe that we can dig a layer down and create even better experiences for our users. It's just it requires a bit more effort now. So, to present this uh some of our work from Ramp Labs, three specific cases of how we've applied research into Ramp itself. Starting with creating a specialist model. So, in November of last year, we launched Ramp Sheets, which was one of

**[3:24](https://www.youtube.com/watch?v=T-42NrYjwxM&t=204s)** the really early uh spreadsheet agents. This was before the two frontier labs had launched their versions of spreadsheet agents and we had a very good launch in November. A bunch of users from great companies had signed up and started using it. And we realized that well, this is a very general purpose spreadsheet handling agent. And a lot of the work that people do on Ramp both inside of the company, but also all of our customers accounting and finance professionals are spending most of their days inside of spreadsheets. So, we can kind of take the spread the harness and the brains behind Ramp Sheets and added into a bunch of other um surfaces within Ramp. And as we were building this out, we realized, well, we can probably

**[4:13](https://www.youtube.com/watch?v=T-42NrYjwxM&t=253s)** apply some research uh from Ramp Labs to make this even better. And we sat down and we started looking, where do models fall short on this? And back then, this was like Opus 4.6 and the place that had the most friction was when you would drop in a lot of spreadsheets into Ram Sheets and you would ask it to build a DCF or or model some financial scenario, it would spend a lot of time creating a plan at first and then researching all of the sheets that it had access to to try to get a good understanding of and lay of the land. And Opus 4.6 is a great model, but it was like pretty slow and the thinking tokens are also pretty expensive. And so, we we took a step back and and decided to train a retrieval model or kind of like a financial question-answering model

**[5:02](https://www.youtube.com/watch?v=T-42NrYjwxM&t=302s)** that would while still keeping these frontier models as orchestrators, would then be handed off to the this much faster model that would do uh financial question-answering for that planning agent. And so, we partnered with the company Prime Intellect to uh post-train a Qwen 3.5 uh 35 billion um model and we actually got above Opus 4.6, which was the frontier back then uh exact task accuracy, while also being able to serve it at high cool uh level latencies. So, a much faster, but just as smart model that could then be used in uh in tandem with the really smart frontier orchestrator. Um and so, this was like a very

**[5:49](https://www.youtube.com/watch?v=T-42NrYjwxM&t=349s)** successful um example of post-training that we had actually sent to prod as part of our Ramp Labs effort. Uh the second uh big thing that we are actually exploring up to this day is uh KV cache tricks and particularly cartridges are really interesting um family of techniques where you're able to compress a lot of context up to 20 to 30 times more context into the KV cash offline and serve it for your agent. And so if you compare it to the RAM sheets example, for example, um uh there's a lot of tasks that you know are going to happen at some point, right? Like month-end close, a month finishes and on the first of the next month a financial professional will go and try

**[6:36](https://www.youtube.com/watch?v=T-42NrYjwxM&t=396s)** to reconcile and close their books. You know kind of the ledger, the aging report and the documents that they will need to be retrieving. And so you could prepare them as context, but the agent will still need to agentically retrieve and and create a good picture and understanding of them. With cartridges, we're able to compress all of that work and build one overnight before the the financial professional starts their work on the first of the month. And once they open up the the the agent, it knows exactly what it needs to do because it has all of the the context already uh built in. Cartridges are also a much lower lift in post training because the way that they do self-play is kind of a lot more generalizable. The caveat with stuff like this is that compared to post training, this is

**[7:23](https://www.youtube.com/watch?v=T-42NrYjwxM&t=443s)** something that the labs might ship at some point is in their APIs and their foray into uh continuous learning. And even if they were to do it in the API, we would actually be happy because we are developing a lot of this tribal knowledge inside of the company um and just learning how best to apply these techniques. So even if it does ship as an API, we can just hit the ground running on day one knowing how to use them. And finally, the third example uh of applied research that we are sending to prod is our work on uh agentic map reduce and kind of agentic swarms. So more concretely, we published an article on the RAMP Labs uh blog on how we uh used 10,000 parallel agents to pen test all of Ramp.

**[8:12](https://www.youtube.com/watch?v=T-42NrYjwxM&t=492s)** Um so at Ramp we have a uh cloud agent called Ramp Inspect, which helps out with setting up all of the infrastructure and plumbing for something as ambitious as this. And we were able to spin up 10,000 parallel agents and then kind of map this work out, try to find any vulnerabilities, and then also agentically reduce on the tickets that they would create. So deduplicate them with LLMs and then try to reproduce them adversarially with LLMs to try to make sure that the vulnerabilities are real and important. At the end of all of this, we have actually found seven high vulner- high severity vulnerabilities that we all patched. Interestingly, one of the um vulnerabilities that we describe in that article is a Lua script injection that you could send over via email. And no

**[9:01](https://www.youtube.com/watch?v=T-42NrYjwxM&t=541s)** single component of that stack was unsafe. And the kind of swarm had to patch together multiple components and understanding of multiple components end-to-end in order to be able to figure this out. And the other nice thing with this is that this is all running automa- automatically. You don't need to spend anyone's time, it's just you start it and the only thing that uh failed failed passes that get filtered out is the cost of the tokens. The other thing that's interesting outside of just building out all of the infrastructure to support these swarms is that we do research into how to best use models as part of these swarms. One of the interesting insights from that same article that we published is that you can actually use open weight models that are up to five times cheaper

**[9:51](https://www.youtube.com/watch?v=T-42NrYjwxM&t=591s)** compared to the frontier reasoning. And because you're set- setting it up as a swarm, the detection rate is not five times lower. So you can kind of spend more on these cheaper tokens and have almost as good of a detection rate. Um if you follow through all of these examples, you kind of notice a pattern of a lot of them is attempts at saving on time and saving on money. So, reducing latency, which is time, and then reducing on token cost, which is money. That's actually Ramp's uh slogan, uh saving our customers time and money. Um and so, I'd like to to point to two uh products that we actually offer from Ramp that have been um influenced by Ramp Labs' research. The first one is token spend management that connects to

**[10:39](https://www.youtube.com/watch?v=T-42NrYjwxM&t=639s)** a bunch of uh your API keys and is able to give you a really good picture of how LLMs are being used inside of your company. Not only token spend on an API key basis or a user basis, but digging deeper, accounting categories, um and even things like uh tax credits that you can get by uh analyzing the spend. It also goes deeper and we create a taxonomy that uh contextually analyzes and semantically analyzes the LLM usage, so you can actually understand how LLMs are being used outside of just attributing it to a team or a person inside of your company. And then the second one is Ramp Router, which also leans into improving your the latency of your agent, where we have a bunch of routing strategies that we work

**[11:28](https://www.youtube.com/watch?v=T-42NrYjwxM&t=688s)** with Ramp Labs to develop, uh things like Nvidia Switchyard, things like smart flex offloading of work to both improve latency and um cost per tokens that you spend. And there's a bunch of different strategies already available for the the for routing, and even more coming out later. So, if you're interested in any of these two products, you can take a photo uh of the URLs or or scan the QR codes there. Give you a second. Awesome. And then I I'd also invite you to check out our Ramp Labs uh blog, where we publish um a bunch of really interesting articles that I haven't had the chance to cover as part of this presentation. Um notably one of the really interesting

**[12:18](https://www.youtube.com/watch?v=T-42NrYjwxM&t=738s)** ones is portal where we figured out a way of uh transferring learnings from one post train to another. So, you could do something like a Laura uh post train on one model, so like the Quen 3.5 that I was describing, but then transfer it to newer versions of Quen or even across different families. So, you're post training with this latent that then can be projected onto different uh models and that really amortizes the cost that you have to spend on post training. Uh more blog posts on agentic map produce, so not only the pen testing stuff that we did, but also things like um analyzing and creating taxonomies of LLM usage, which is stuff that has gone into the token spend product. Um things like self-improving monitoring where we use uh LLMs to automatically um

**[13:06](https://www.youtube.com/watch?v=T-42NrYjwxM&t=786s)** create monitors with DataDog on a lot of our product services and then as the words come in, improve those monitors automatically without a person in in the loop to try to basically create super super robust and resilient software. Um and finally semantic tagging, which is this interesting uh foray into creating this um agentic map produce over a bunch of user sessions where we can annotate and create taxonomies that are open-ended. So, not knowing um ahead of time which what are the clusters of LLM usage and trying to create a taxonomy that can then be reconciled against the spend inside of the companies. So, if uh if you're interested in this uh type of research, x.com/ramplabs where you can uh go and and check out more of our research.

**[13:56](https://www.youtube.com/watch?v=T-42NrYjwxM&t=836s)** And uh there's my Twitter if you have any other questions or uh want to talk about some use case as part of your applied research. And that's it. Thank you. >> [applause]
