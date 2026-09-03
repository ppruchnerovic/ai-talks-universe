---
id: zkX03APVj0M
title: "Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang"
slug: emulated-the-data-for-fully-autonomous-software-engineers
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Joseph Wang"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-07-31T00:00:00Z
video_id: zkX03APVj0M
url: https://www.youtube.com/watch?v=zkX03APVj0M
youtube_url: https://www.youtube.com/watch?v=zkX03APVj0M
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Training, fine-tuning & model building"]
transcript: true
---

# Emulated: The Data for Fully Autonomous Software Engineers and Companies — Joseph Wang

**Joseph Wang**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zkX03APVj0M) · [Conference site](https://www.ai.engineer/)

## Description

To train an agent that can run production software, you need training data that looks like production, and that is what Joseph Wang's team at Emulated builds. Coming from network infrastructure backgrounds, they know what happens when something like a database goes down at scale, and they argue that current post training environments do not capture it. A real task is not a tidy code diff; it is fifty to a hundred turns of solving live traffic while distributed nodes fail, configs conflict, and unforeseen problems appear mid incident.

So Emulated simulates whole companies. Imagine acting as an engineer inside a cloud provider or an infrastructure service, provisioning resources across VPCs, subnets, and security groups, meeting real bars around cost and deployment, and keeping a service alive as it grows, all inside a high fidelity environment rather than a stub. Wang's bet is that domain expertise plus faithful simulation is what lets agents learn the messy, end to end reality of infrastructure work, and he closes looking for people who have trained models or run real infrastructure to help push that fidelity further across more domains.

Speaker info:
- https://emulated.so/

Timestamps:
0:00 - Useful work over longer horizons
1:20 - Backgrounds in network infrastructure
2:26 - How environments shape capability
3:16 - Fifty to a hundred turn tasks
4:59 - Why real incidents are messy
7:11 - Real infrastructure isn't a code diff
7:40 - Acting as an engineer inside the cloud
9:37 - Deployment, cost, and scaling bars
13:29 - Why it's called Emulated
15:01 - Simulating full companies

## Transcript

*2,563 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=zkX03APVj0M&t=14s)** So, I appreciate the intro. Uh my name is Joseph and this is my co-founder Sid. Emulated is a data lab focused on increasing the reliability and autonomy of AI agents. And if you've been a AI engineer and you've watched the talks, seen the tracks, then there's probably one takeaway that all the talks have in common. And it's that we're headed towards a future where agents are able to perform useful work over longer and longer horizons with little to no supervision. So, today we're going to answer some of the questions of what this means for the data and model layers. Uh we're going to touch on some pretty cool things. Uh so, look out for them. Um like how to simulate a company within a sandbox or sandboxes for multi-node systems and

**[1:02](https://www.youtube.com/watch?v=zkX03APVj0M&t=62s)** distributed clusters. Um and if we have a little bit of time, we'll also go into some of the work that we're doing with post-training pipelines and how these new types of sandboxes are affecting post-training infra as well. So, where Sid and I come from, um our backgrounds are in network infra, distributed databases, and sandbox infra. And these are all areas where the workloads are mission critical. We all saw a couple months ago that uh when something like DynamoDB goes down, so does US East 1 and half the internet. Um and working on these systems, we saw model capability gap when it came to operating and building these systems at scale at scale and thinking about uh the consequences of architecture and system

**[1:52](https://www.youtube.com/watch?v=zkX03APVj0M&t=112s)** system design over the course of years. >> Yeah, so it led to a pretty uh natural question, right? For such mission-critical services, why is it that my model or my agent is so proficient at handling the application layer, but is struggles when it comes to reasoning through infrastructure complexities? For example, things like MVCC on a database engine, which can lead to corruption issues, which is one of which was one of the roots of the DynamoDB failure a few months ago. >> So, like with everything in NML, uh the gap in models is usually a gap in data. Models typically are only as good at as data is. Um and to really highlight this point, right? Model capability has never uh

**[2:41](https://www.youtube.com/watch?v=zkX03APVj0M&t=161s)** regressed whenever you introduce more high-quality data. Um so, with that being said, what is the data gap then? What does data look like right now? And how is this influencing the model capability gap here? So, if you look at any of the frontier or recent benchmarks, like SweBench Pro, Terminal Bench, or something like Frontier Code and Deep Sweep, um the tasks only operate within the code base. Uh the agent is given a pretty large uh task uh and over the course of 50 to 100 turns produces a couple thousand-line PR. Um but it doesn't do all of the work that a human does. It doesn't do uh what a PM does with talking to customers,

**[3:29](https://www.youtube.com/watch?v=zkX03APVj0M&t=209s)** understanding their problems, what an engineer does with trying out different approaches, performing performance testing them, um and owning the underlying infra for the code base over the course of not just months, but years. >> And this is really the gap that we're closing. We've taken software engineering companies and we've put them into containerized environments. so this includes uh include like organizational contexts like projects, incidents, customer conversations. Uh the agent also has to deal with issues that only appear at scale like network failures between distributed nodes, data corruption, and clock skew. And through all this, we also want the agents to reason about orchestrating through distributed clusters and also

**[4:17](https://www.youtube.com/watch?v=zkX03APVj0M&t=257s)** thinking about things like operational blast radius while solving live traffic. And the result is that the task that these agents have to complete or we want the agents to learn is that environments are far more complex and long horizon than a simple code diff. So, let's just let's bring a picture into the mix because it tends to make things more interesting. Uh here's an example we've built of an SCD consensus cluster that a typical production service might rely on. So, an old environment uh might tended to operate and work primarily on that little blue square entitled SCD source code in the bottom right there. But, a lot of the fun and the model capability gap that results from it is

**[5:05](https://www.youtube.com/watch?v=zkX03APVj0M&t=305s)** really in everything that surrounds it. So, you you start with the tickets, projects, postmortems. What are the train wrecks? Why did they happen? How did customers feel about them? And often times those aren't necessarily up to date. Um the agent has to incorporate all that when it's reasoning through the actual change that current environments have it make. After it makes that change, uh you need a kick kick off rolling deployments. Those deployment systems can often times be complicated, have conflicts, may not work. Um and all through that, when you're finally migrating off of from old hard onto new hardware, um you run into unforeseen problems which you

**[5:52](https://www.youtube.com/watch?v=zkX03APVj0M&t=352s)** did not sort of the the the the the the agent has to reason through in real time, just like a human would, right? You have um failing nodes. You have stale deprecated nodes. And while all of this is happening, the service can't go down because there is a blast radius to serving live traffic. You have to observe and monitor your service. All of these components in in in the system is really uh what sort of exemplifies like a full end-to-end infrastructure task. >> So, what Sid is describing here is an environment in a single node sandbox where we're simulating uh distributed cluster with multiple nodes, flapping nodes, lagging learners um in a single sandbox. And you can get pretty far with

**[6:40](https://www.youtube.com/watch?v=zkX03APVj0M&t=400s)** this, right? Like you can see that there's live traffic, there's a lot of operational issues that a real engineer would have to deal with. And you can make this pretty long horizon by just say doing multiple deployments instead of just one. But really what we're seeing is that this is not enough. Uh this fits into standard post-training pipelines in the sense that a standard post-training pipeline is kind of boring. Uh it's kind of homogeneous. You know, everything just runs harbor, everything is a single sandbox, containerized. But real infrastructure uh doesn't work like this. Uh this isn't how real companies run. And uh even though you can use something like deterministic simulation to simulate network failures, it doesn't represent what you might run into if

**[7:29](https://www.youtube.com/watch?v=zkX03APVj0M&t=449s)** you're building an AWS-scale service. So, I did see I think a couple people at AWS. Somebody had Viceroy open on their laptop. Um fun times. Um but let's imagine here that we are all AWS engineers or GCP engineers. Azure, too. No shade, right? Um, and we are building a cloud service. Um, it can also be some infrastructure service like DataDog, Vercel Superbase. Uh, all of these services run into the same problems. You start off with a shiny piece of software. And this piece of software can service a single customer pretty well. Um, maybe it's running on your machine. If you're working for NLB, it should be a load balancer, right? If you're working for AWS Lambda, it'd be some sort of serverless runtime. But, uh, it needs to actually run somewhere. So, if you're

**[8:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=500s)** infrastructure engineer, next step is you get into resource provisioning. Um, and this is already where the single node sandbox starts breaking down. How do you provision resources within a single sandbox? You can't exactly simulate something like EC2 or Cloud Run right? Um, so you get into this host provisioning. Uh, it also includes provisioning of other resources like VPCs, subnets, security groups. Um, and you need to expose this through some sort of API because your customers are going to want to do things like, "Oh, give me this shiny piece of software." Or, "I don't want it anymore. It cost too much. I'm going bankrupt. Delete it, please." Um, and so you're going to need some sort of front-end API. And if you have enterprise grade customers who really

**[9:07](https://www.youtube.com/watch?v=zkX03APVj0M&t=547s)** care about quality, then you're going to have to meet certain bars like throttling authentication authorization. You can't really like go without these things, right? Uh, if you're AWS, then that's CloudTrail, too. Um, and then beyond this, uh, software is living. People forget this all the time, especially like investors, right? Like they'll be like, "Oh, you wrote it. You're done." Um, but software is living and you probably need some sort of software deployment component as well. Uh something whenever you have an update to roll out roll it out. Um and God forbid something goes wrong, roll it back. Uh you need to manage all the different versions and make sure your deployments are gradual to limit your blast radius. And we're just kind of getting started

**[9:56](https://www.youtube.com/watch?v=zkX03APVj0M&t=596s)** with this. There's all sorts of things that you need to think about like health monitoring with awareness for network partitions. Uh and then how do you communicate with your host so you can change configs on the fly. Um maybe your customer actually wants to call your endpoint, so you need DNS and cert management. And then, you know, your our service grows a bunch, you need to keep track of all your resources, what's going on, fraud and stuff, then you need admin consoles, uh telemetry, billing if you're making money, um all sorts of things. And with all of this, I think there's like one more slide for is it scheduling? Yeah. Um >> I think the point is fairly clear at this point. Beyond beyond a certain threshold, there is a

**[10:43](https://www.youtube.com/watch?v=zkX03APVj0M&t=643s)** critical mass at which sandboxing on a single node uh can only get you so far. And that's why we envision the the future being going towards a world where environments do provision real infrastructure. >> Yeah, so what this is is um a multi-node sandbox with access to real infra, real cloud resources. Uh we kind of put a cloud in box, so cloud box could be another name for this. Um and as you can imagine, changing the sandbox type so drastically here affects post-training pipelines as well, which um I think we might be running a little bit low on time, so we won't get like too much into it. Um but yeah, like uh one really cool thing, too, is like you can put a post-training

**[11:31](https://www.youtube.com/watch?v=zkX03APVj0M&t=691s)** pipeline in the sandbox, um and there's some cool stuff with model training and RSI that you can get into there. Um so, you know, then this begs a question, uh this is all cool stuff, Joseph. Uh thank you, Sid, for speaking. Why are you leaking all of this alpha, right? Why are you like telling all your organizational secrets and telling everybody like, "Oh, okay, you know, how do you build a system like this?" Um it's because uh we're really interested in these challenges here. We think they're very fun. Uh you know, we think they're really cool. We think that you guys are cool people, uh or maybe I'm just lying, who knows. Uh and we want to share these challenges with you uh in case you're interested in working on them as well. As you can imagine, there's a lot of

**[12:18](https://www.youtube.com/watch?v=zkX03APVj0M&t=738s)** different problems that we haven't touched on here. Like, for example, spinning up the entire stack for something like AWS Lambda takes hours. Um how do you fit that into a post training rollout? Uh and then there's cost as well. How do you efficiently manage this? How do you make sure the sim-to-real gap, even with real resources, it still exists, right? You still have to have live customer traffic. You still have to have uh problems that only appear at a certain scale. So, you know, if you're a distributed systems engineer, um you know, if you know, this stuff if you train models before, um if you think that this stuff is cool, uh then you know, we'd love to talk. Uh we'd love to talk, uh kind of like see where your opinions are, uh hear what you've worked on, maybe that's like, "Oh, Kubernetes." And you have like

**[13:07](https://www.youtube.com/watch?v=zkX03APVj0M&t=787s)** opinions. Well, everybody has like opinions on like auto scaling and rolling deployments and whatever, but like really niche opinions, right? Like, at CDO. Um yeah, we'd love to talk to you and hear what you have. Thank you. >> Yep. >> Um what's your like primary goal with emulator? >> Yeah, um that touches into why it's called emulate in the first place, right? Uh, the real world is very, very complex um and how we as a industry emulate the real world is incredibly contrived and low fidelity. So, emulated goal is really how do you make these agents own systems like this, uh, maybe beyond systems, entire companies, by emulating the real world with full fidelity.

**[13:56](https://www.youtube.com/watch?v=zkX03APVj0M&t=836s)** Yeah, go ahead. >> Next question is, are you predominantly focused on like infra and you have a lot of containers, actually hardware kind of related stuff, or are you also like full RL environments like a digital twin? >> Yeah, of course. Like, the question is like, you know, infra is really cool. Um, in 2026, all of us are on an infra's comeback, and it's very sexy. Everybody wants to work on it, right? But, there's other types of RL environments as well. Um, there is, uh, other workflows that you really want to capture that aren't necessarily infra related. Uh, so the reason why we're starting with infra is,

**[14:44](https://www.youtube.com/watch?v=zkX03APVj0M&t=884s)** um, there's a couple. Well, the first most important one is it speaks to our background the most. Um, we think that domain expertise is something that informs how high quality your data can be. Uh, especially with boutique nature of data nowadays. Um, and the second is that when we're simulating full companies, infra is the easiest to approach. Uh, if you think about like any infra company out there, whether it be Superbase or Modal, uh, or any dev tools company, the problem statement is pretty clear. Uh, engineers kind of know what they want. If you are working for Modal, you know that your users want GPU sandbox, very low latency, very low cost. You don't want to fail halfway through your training run. Um that's what you care about. So, the

**[15:31](https://www.youtube.com/watch?v=zkX03APVj0M&t=931s)** problem statement becomes much easier. Whereas, if you are, you know, a a company in the YC summer 2026 batch, you're probably still trying to find product market fit, right? >> Yeah. At the same time, there's also lessons learned that going really vertical on a single domain like infrastructure do translate into other horizontal domains. So, we're also um exploring going deep into one and scaling out that way. >> All right. Uh really appreciate it. Uh appreciate the questions. Um we'll probably step out and we can like take a couple more uh outside just to make sure the next speaker has room. Um yeah. Uh I thank you guys for listening. >> Appreciate it. >> [music]
