---
id: WJTQBENv0KI
title: "How Ramp Tests Its AI Bookkeeping Agent Before Customers Do - Ryan Stevens, Ramp"
slug: how-ramp-tests-its-ai-bookkeeping-agent-before-customers-do
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ryan Stevens"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-11-08T19:00:27Z
video_id: WJTQBENv0KI
url: https://www.youtube.com/watch?v=WJTQBENv0KI
youtube_url: https://www.youtube.com/watch?v=WJTQBENv0KI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Ryan Stevens", "Ramp", "AI evals", "agent evaluation", "benchmarks", "synthetic data", "pass@k", "accounting", "bookkeeping", "AI agents", "agent memory", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# How Ramp Tests Its AI Bookkeeping Agent Before Customers Do - Ryan Stevens, Ramp

**Ryan Stevens**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Ryan Stevens` `#Ramp` `#AI evals` `#agent evaluation` `#benchmarks` `#synthetic data` `#pass@k` `#accounting` `#bookkeeping` `#AI agents` `#agent memory` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=WJTQBENv0KI) · [Conference site](https://www.ai.engineer/)

## Description

Ryan Stevens leads applied science at Ramp and explains how the team built end-to-end evals for Stack, its AI agent for bookkeepers. He starts by breaking an accountant's job into tasks like reconciliation and variance analysis, then builds synthetic businesses with full books so agents can be back-tested on the same data again and again. He covers accuracy versus pass@k, why the latest models still fail mostly on reasoning, and the experiments that didn't work, including auto-tuning prompts. Then he shows the ones that did: removing unneeded skills, testing memories across two time periods, and scheduled regression runs that report problems in Slack.

Chapters:
0:00 Intro
0:47 What's your agent's goal?
1:16 Breaking down a bookkeeper's job
2:43 Building a benchmark
3:20 Before and after you have users
4:26 Data is the bottleneck
4:48 Building synthetic businesses
5:45 Evals are just back-tests
7:08 How each task is graded
9:14 Accuracy vs. pass@k
10:24 Picking a model
11:18 Why models fail: reasoning
12:18 Experiments that failed
13:36 Skill ablation
15:01 Testing memories
17:01 Regression testing in the background
18:07 Takeaways

Ryan Stevens

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*3,045 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=WJTQBENv0KI&t=1s)** [music] >> Today I'm going to talk about building better agents through end-to-end evals. I'm going to talk about one of Ramp's products, Stacks, a a stack R A I agent. Uh so this is a short talk briefly about me, about Ramp. Ramp, 70,000 plus businesses. Um we have card, travel, AP, AR. We're an expense management platform. I lead our applied sciences team. These are AI engineers, MLEs, product data scientists, formerly of Meta, uh and I have a PhD in economics. I care a lot about measurement and evaluation, which is what we're going to talk about today. So,

**[0:48](https://www.youtube.com/watch?v=WJTQBENv0KI&t=48s)** three things. What's your agent's goal? Design those evals, and then how did we get uh value from the evals that we designed? Uh so I'm particularly opinionated about this, that people try to identify a process that they don't really understand. And the first task in uh building an agent for a process is breaking down the job, the tasks, and what success looks like. So, this is what a bookkeeper's job tends to look like. So, they want to close the books. We're not going to do a ton of accounting today, but generally they have a set of tasks that they're trying to accomplish. When we're building our benchmark, uh we created a set of categories. These are three of them. There's going to be a fourth that you're going to see a little

**[1:34](https://www.youtube.com/watch?v=WJTQBENv0KI&t=94s)** later. Um and then we thought about what success looks like. Um once we knew the tasks, once we knew success, we sat down with bookkeepers, we sat down with accounting firms, and then we wanted to understand exactly the full end-to-end process to solve a specific task. This is an example of a reconciliation. A reconciliation is actually a pretty simple exercise. You have on the left-hand side, you have an ERP uh that represents the accounts payable ledger. Those are bills that you have to pay. If you don't know the term accounts payable, I didn't until a few years ago either. And then on the right, you have the system that has the bills. In this case, you can pay your bills with Ramp. You need these two systems to have the same numbers. It's a pretty simple exercise. What does an accountant do? Well, they

**[2:22](https://www.youtube.com/watch?v=WJTQBENv0KI&t=142s)** go into Excel. They bring in the data for the ERP row by row. They bring in the data from the system that is accounts payable. Do they reconcile? Do they tie? Yes, no. And then they figure out why they don't, and then they make them tie. Pretty easy to identify this process if you understand exactly what it is. So, we want to build a benchmark. Uh I'm going to interchangeably use terms like benchmarks, evals, verifiability, because frankly, I think it's a soup of language that are all trying to do the same thing. These are the four sets of categories of things that we wanted to eval. There's reconciliation, what I just described, data entry, variance analysis, it's why

**[3:11](https://www.youtube.com/watch?v=WJTQBENv0KI&t=191s)** do numbers move, schedules and accruals, not going to go deep into there, but it is a complex thing that an accountant is doing. So, this is just like a very high-level schematized version of how to think about the process of building evaluations. You can think about the state before you have users or at least enough users that you think you have a good distribution of data. And then with users. So, before you have users, remember all agents are doing is they're calling tools that hit a database. That's it. You don't have users. You need simulation. You need synthetic data. I would highly recommend anytime you're building an agent for an area where you don't have enough users, you should build synthetic data. Um

**[4:01](https://www.youtube.com/watch?v=WJTQBENv0KI&t=241s)** we built this benchmark in partnership with a company called Mercore. Uh, they were a great partner for this. Um, you don't have to build it with a company, um, but simulation is pretty important. Once you have users, things get a little easier, if not harder. We're not going to talk about that phase in this talk. I only have 18 minutes. That would be longer than an 18-minute talk. Um, so data is the bottleneck to evals. I think that's an obvious statement, but I want that to be like very clear that to evaluate, you have to have clean data to do things on. So, how do we design the evals? Like, how did we think about making a data set, a set of task criteria that we would get value out of?

**[4:48](https://www.youtube.com/watch?v=WJTQBENv0KI&t=288s)** Uh, so we built synthetic businesses. Uh, this is an example of one of our synthetic businesses. Uh, they're a D2C lifestyle company. Uh, they use Amazon. Uh, there's some complexity to how they do their accounting. They have a calendar year. They want to do just close at the end of the month. They're multi-channel. They get revenue from Shopify, Amazon, a bunch of different stuff. Uh, the details of this are not that important of who this company is, but what we also did is we built a set of documents or data for this company. We built their ERP. We built their customer list, their vendor list, the accounts payable, everything that would be needed for a synthetic business, uh, in order to do good offline

**[5:36](https://www.youtube.com/watch?v=WJTQBENv0KI&t=336s)** evaluation. Uh, all we're doing here, by the way, is just backtesting agents and measuring success. Like I said, um, people use these terms interchangeably. My training is as an MLE. Uh, before I came at Ramp, I was the first MLE at Ramp. Um, and I think one of the problems on the discourse on evaluations, verifiability, and benchmarks, uh, is that they're just trying to find labels. They're just trying to find ways to measure success for things. Um and they're all sort of saying the same thing. Uh but really you're just looking to run back tests. You're looking to run your agents against the same set of data

**[6:25](https://www.youtube.com/watch?v=WJTQBENv0KI&t=385s)** day over day over day to find ways to optimize it. I sort of have a theory that the industry's been a little um uh I the term is not hurt, but I think we had it good when it's just coding agents cuz Git by nature allows you to replay things in the past. State is always captured. When you start to think about production agents, how do you capture state over time so you can replay? Uh we're in a nice place when we have no users. We build that state and we keep that state the same over time. But that's really just our goal. We're running a back test. We're measuring success. And so this is is sort of what the trajectory of the process looks like. We

**[7:13](https://www.youtube.com/watch?v=WJTQBENv0KI&t=433s)** build a task, in this case a reconciliation. We call these things worlds. It's a term that Mercor um came up with and I quite like it. Uh a world could also be your production data, a snapshot of it. There's no reason to swap that in. It's the same thing. We have the agent run and then we just evaluate on the final output. You can see the criteria that we have. For each task we tended to have anywhere from 10 to 20 criteria. We didn't judge the trajectories um themselves like were the right tools called, were the right skills invoked? Did it take an efficient path? We do care about latency, cost, and like success. Um

**[8:03](https://www.youtube.com/watch?v=WJTQBENv0KI&t=483s)** there are different reasons you might care about trajectories, but when you're initially building your agent, you just want it to be right, to be cheap, and to be fast. How it gets there is a little bit less important. Uh so, that's not what we focused on. And like I had said my mini rant before, in this as example, we're looking for a few things that define success. If I were just in MLE, I would say these are the labels. Um the thing I want to say is the process to build this whole thing was 4 to 6 months before launching this agent. And I think that level of time investment in evals uh is typical in companies that are trying to build agents for

**[8:51](https://www.youtube.com/watch?v=WJTQBENv0KI&t=531s)** areas that are not fully optimized uh by the frontier models. You're throwing something as a coding agent, sure, it'll probably work great out of the box. If you're in a front an a frontier area, an area that's slightly orthogonal to what they're optimized against, um you need to spend some time building these things. So, how do we measure performance? I'm sure there's a lot of people in this room that have seen these metrics. Um one is accuracy, that's pretty simple. So, like I said, this given task had six criteria, four of those six are right, 67%, so partial credit counts. Uh the other way um that you'll see reported a lot is pass at K. Um this is an example of three runs on this given agent. Uh in

**[9:41](https://www.youtube.com/watch?v=WJTQBENv0KI&t=581s)** the first run, it got four right. Second run, it got five right. Final attempt, it got six right, so it got all of them right. Pass at K is an all or nothing metric. Um you could think for areas where the cost of error is very high, maybe like accounting, uh pass at K might be the thing you're optimizing for. You need everything to be right. If an accountant can't trust that one of the steps is wrong, then they may not use your agent. Um so, this is pass at K. You can see pass at one is zero, pass at two is zero, and then pass at three is one because it finally solved it. Okay. So, now I'm going to talk about that's how we built the evals. That's what our evals were. I'm going to talk about all the things

**[10:28](https://www.youtube.com/watch?v=WJTQBENv0KI&t=628s)** we now do with these evals now that we spent that four to six months, now that we spent all the money on it and time. I mean, the first obvious case, right, is you're going to like pick a frontier model. You're going to be like, which model is best at this? Um this is a little old. This is from a blog post we wrote when Stack launched. Um as you could sort of see at the time, uh the Opus models uh were the highest performing. That's still what we see when we rerun these benchmarks. 55 is the best model. What you'll also see is accuracy is very high. Pass at one is very low. These aren't saturated yet, which is great. Um it's great for us, too, because we find harness optimizations allow us to get extra pass at. Um so, it means you can't just throw a frontier model at this problem and have it

**[11:17](https://www.youtube.com/watch?v=WJTQBENv0KI&t=677s)** solved. We dug deeper into why the models are failing to spot areas for optimization. Uh so, we looked at things like reasoning failure. Does it have all the data? It's just reasoning through it incorrectly? Uh does it not gather the right information? Does it not follow instructions? Um and then like reflection failure, which is I would actually call it other. Um interesting result that we see is that for accounting, it's reasoning failure. What that means is that these harnesses are pretty good at actually gathering the right amount of data. Accounting is not that difficult of an gathering exercise. Accounts payable is like something I could explain to like a five-year-old, so you could sort of get a well, sophisticated five-year-old. Um so, you could sort of get uh what files

**[12:05](https://www.youtube.com/watch?v=WJTQBENv0KI&t=725s)** you would need. Uh and so, what this sort of says is like, you know, the models, they just ain't that smart. Uh and we've got some room to run here. Uh, what was interesting was Music Spark actually did really well in this. Um, so we ran a ton of experiments. These are all the things that failed. Um, I sort of like this because like you'll see papers of like these awesome things that they did to optimize and tune their agents and they don't show you the 30 things that failed. Actually want to highlight one. I'm going to go on like a mini side quest for a moment here. Uh, Jeepa, auto tuning, auto researching skills. No good. Uh, it might be our agent, um, but I think the idea of hill

**[12:53](https://www.youtube.com/watch?v=WJTQBENv0KI&t=773s)** climbing with evals on text space is not the first thing I would do here. Uh, intuitively it's difficult to understand why it would work, i.e. how you can get direction on a gradient. Um, we did not see success here. We were still not seeing success. I just want to call this out because I think there's a lot of noise on auto research. Um, the Karpathy famous tweet is about tuning ML models, which obviously it has a gradient, it has a direction. It's also a finite space it's searching over. Great. Um, so one lesson to take away from here is maybe don't think that auto research is going to solve your bad agent problem. So here's some experiments that did work. Um, I'm going to talk about two.

**[13:40](https://www.youtube.com/watch?v=WJTQBENv0KI&t=820s)** I'm going to talk about skill ablation and trajectory distilled memories. So I'm an MLE by training. Uh, usually what you do is you build a bunch of features, uh, throw them in a model, and then you might do like a leave one out feature, or you might add features back in. It's all just trying to assess the incrementality of a given feature on model performance. Uh, agents with many skills, many tools. We didn't do with tools, we did with skills. Tools are a little bit more difficult to deal with, but you could do a similar thing. Uh, we just tried to trim the number of skills saving context. That's your goal. Um, and what this basically shows is if you look at no skill baseline, basically this is you could just think it's like

**[14:27](https://www.youtube.com/watch?v=WJTQBENv0KI&t=867s)** the raw model, whatever's in the weights, um versus uh, removing uh, uh, versus like adding the skill. I I think I've reversed these actually. I think the negatives are like it's good with the skill and the positives is bad with the skill. Regardless, um, what you can see is there's definitely differences in skills being there versus not being there. And this created a candidate set for us to then be like maybe we should delete these skills, compress these skills, basically make things more efficient. So, skill ablation, you should do it. Tool ablation, you can also do. Trajectory distilled memory. So, a lot of people talk about memories. Uh, I think the rise of personal agents, people talk about the memories and how good they are, blah blah blah.

**[15:15](https://www.youtube.com/watch?v=WJTQBENv0KI&t=915s)** Um, but people don't really test their memory systems. Um, or at least I don't tend to see people testing their memory systems. They'll have a prompt, they'll compress some information, they'll put it into some store, uh, and then they'll read it back. Uh, so, one little innovation we did here is what we call roll forward worlds. So, it's a little complex, so I'm going to walk you through that chart on the left. Uh, but basically, uh, you do the same task over two time periods. You write a memory after the first task, uh, and then you either inject the memory in if you want to cheat a little bit, or you let the agent search over a set of memories, um, for the same task in the following period. So,

**[16:04](https://www.youtube.com/watch?v=WJTQBENv0KI&t=964s)** in the example I have here is like uh, we want to match some records, do a reconciliation. There's some implicit customer rules and how they like to do that. Uh, those will be not fully encoded, but you can infer them from the success criteria like you have to learn these rules in order to be successful at this task. We have a memory prompt that then compresses, writes, and then we rerun it, and it reads again. And what we actually saw that there is a ton of alpha here. Like the types of memories that were written for tasks really depended on the prompts, and then success was pretty in like also dependent on those prompts. We saw a

**[16:52](https://www.youtube.com/watch?v=WJTQBENv0KI&t=1012s)** very large gain. This was actually one of the biggest gains we saw from having uh, these types of evals. So, uh, you have a great data set uh, that you can run evals on. The thing that I think people don't do enough of is what I call regression testing. I'm not a big believer in CI gating based off of agentic evals as someone that's seen a lot of non-determinism, a lot of 80%, 70% passage. Uh, CI gating is not usually the best idea, but instead what we do now is we have an internal platform that hosts our evals that people can add the evals to. This top uh, picture you see is an example of stack. We have a bunch of different

**[17:39](https://www.youtube.com/watch?v=WJTQBENv0KI&t=1059s)** cases. We actually tag these cases so that we can cluster and organize them a little bit better. We set a recurring schedule, so these should run in the background every week, every day, whatever. We run it, we see how things perform. We have a background agent that then looks at like failures, regressions, all of those things. Uh, and then we get a Slack message that tells us, "Ooh, it looks like something's regressed. Go investigate it. Here's what I think broke." So, getting the value out of your evals is important. So, takeaways. I'm at time. Break down a job into discrete, you know, tasks. Build realistic environments. Focus on extracting like value as much as possible Um, and then figure out how to consistently put those into workflows

**[18:26](https://www.youtube.com/watch?v=WJTQBENv0KI&t=1106s)** to measure performance. Cool. Thank you for listening and yeah, appreciate the time. >> [applause]
