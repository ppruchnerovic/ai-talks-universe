---
id: X6l4lpA0_NY
title: "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl"
slug: harness-engineering-how-to-build-a-software-factory-dru
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dru Knox"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-06T15:30:27Z
video_id: X6l4lpA0_NY
url: https://www.youtube.com/watch?v=X6l4lpA0_NY
youtube_url: https://www.youtube.com/watch?v=X6l4lpA0_NY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "harness engineering", "loop engineering", "software factory", "coding agents", "agentic development", "AI agents", "Claude Code", "Codex", "agent skills", "skills registry", "developer productivity", "Tessl", "Dru Knox", "AI engineering", "AI Engineer"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl

**Dru Knox**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#harness engineering` `#loop engineering` `#software factory` `#coding agents` `#agentic development` `#AI agents` `#Claude Code` `#Codex` `#agent skills` `#skills registry` `#developer productivity` `#Tessl` `#Dru Knox` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=X6l4lpA0_NY) · [Conference site](https://www.ai.engineer/)

## Description

In a software factory, agents write everything your users get. Your engineers build the factory.

Dru Knox, head of product and design at Tessl, explains harness engineering (some now call it loop engineering), the discipline that takes a team from using coding agents to running a software factory. He defines a factory by three metrics: autonomy, automation and quality. He breaks the work into inner, outer and meta loops, and explains why harness engineering is hard: the field changes weekly, the work is unplanned, and the signals you need are stuck in local logs. Then he lays out three layers to build, a control plane, an agent-ready stack and improvement loops, and shows how Tessl's skills registry, Tessl Agent and Tessl Launch help you get there one workflow at a time.

In this talk:
• What a software factory is, and why the real payoff is higher quality, not just speed
• Inner, outer and meta loops, and what each one improves
• The three layers: control plane, agent-ready infrastructure, improvement loops
• Metrics to track: manual takeovers, human PR comments, PRs started without a human

SPEAKER
Dru Knox, Head of Product & Design, Tessl
X: https://x.com/drufball

LINKS
Tessl: https://tessl.io
Tessl on X: https://x.com/tessl_io

CHAPTERS
0:00 Intro
0:43 Who this talk is for
2:03 What is a software factory?
2:58 Autonomy, automation, quality
4:33 The payoff: higher quality
6:13 Harness engineering
6:43 Inner, outer and meta loops
9:08 Why harness engineering is hard
11:13 The three layers
11:33 Layer 1: the control plane
12:47 Layer 2: making your stack agent-ready
14:22 Layer 3: improvement loops
15:32 How Tessl helps
17:37 Tessl Agent
18:47 Tessl Launch
19:37 Metrics to track

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,626 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=12s)** Quick introduction. My name is Drew Knox. I'm the head of product and design at Tessle. Tessle is an agent enablement platform. We help you go from scaling skills to building your own software factory. So today I'm going to talk about a few things. The core is going to focus on harness engineering which we see as sort of the new discipline of agentic development and how you can use it to ladder up to a software factory. So before we get started a few prerequisites. This is a bit of an advanced talk in the sense that like if you aren't already using coding agents what I'm about to walk through is probably not where you want to get started. So, I'm sort of assuming that if you're working with coding agents, you're used to having a couple sessions

**[1:02](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=62s)** at a time. Uh you've gotten to a place where coding agents will for like easy tasks and maybe medium complexity tasks frequently do the right thing. This you're sort of at the sweet spot for starting to think about harness engineering, starting to think about a software factory. What I'm going to say here is not exclusive to that, but that's where you'll get your best results. So, I'm going to walk through a few things. First, I want to define software factory and talk a little bit about why you might want to build towards one. Second, we're going to then focus a lot on harness engineering, which is kind of the core practice or skill that you'll use to reach a software factory. We'll talk about what are going to be the components you work on while you're doing harness engineering. And finally, I'll walk through how the Tesla product uh briefly can help you along that

**[1:56](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=116s)** journey. But most of the topics I'm going to talk through here today work with any stack. They're mostly techniques. Tesla makes them easy, but they're not exclusive to us. Okay. Part one, software factories. What are they? There's no strict definition. I'm sure you're all probably as frustrated as I am with how quickly terminology changes and migrates in the in the industry today. But roughly speaking, a software factory is any agentic system where all of the end product of what you're building and shipping to users is created by agents and your software engineering teams effectively focus on building the factory. So they work on making the factory more autonomous, more automated, and raising the quality of what it produces. I'll go into each of those terms in just a second. That's

**[2:48](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=168s)** kind of the core idea of a factory though is everyone on your team effectively becomes internal tool builders and then you're building a system that produces your product. So I mentioned three key metrics. These are sort of like the pillars you need to think about when building towards a software factory and they sort of go in this order. So autonomy is effectively how much human intervention do you need to get to the right answer. So how many times you need to correct the code or provide a nudge on how the agent should be building. Automation uh oh sorry I've gotten them flipped here. Uh autonomy is the first one. It's how much do you have to do humans have to correct? Automation is how much can you let them run, right? How much do you need to review or build trust in the solution before you accept

**[3:40](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=220s)** it? They sound quite similar, but there is a difference. You can have high autonomy in the sense that agents frequently are oneshotting the problems you're giving them, but low automation because you don't trust it yet. And so you're reviewing all of the code directly. You are manually verifying everything. So they are distinct things that obviously have a connection, right? You have to build up autonomy first before you can move to automation. The final quality, probably the most self-explanatory, how good is the product that you're actually producing for your users? These metrics are like your usual user analytics, your uh test quality, your test coverage, etc. As you work towards a factory, you're going to go improving autonomy. then approving automation all while keeping

**[4:30](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=270s)** quality constant and then the sort of payoff at the end. Why would you want a software factory is that ultimately we think you can raise quality once you have a factory. So talk about this a bit. I think most folks look at factories as a way to ship faster. They'll say like oh yeah you'll get a little bit of slop but my god you'll you'll launch so much more features like the cost return the ROI will be worth it. I think that's a very shortterm phenomenon, right? As agents are sort of coming online and getting better. In reality, yes, you will move to higher velocity with a factory. But every team has backlogs of bug fixes or improvements that they wish they could be making that they just don't have time to do or explorations that they wish they were they were doing. With a software factory, the idea of a backlog

**[5:23](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=323s)** kind of goes away. And so you actually just have much more capacity to work on test quality improvements, architectural refactors. So at Tesla, we believe that yes, at first as you transition, you will want to keep quality constant or maybe like a very small dip, but that the ultimate payoff is you should see better quality uh in the code that you're producing. Also, it's great for your overall team collaboration styles. So once you've moved to a software factory, it's much easier for people who aren't in technical roles to contribute ideas. So it's easier to explore more and to have more perspectives coming in and contributing while your engineering team is much more focused on building the underlying system that everyone is using to push features out to your users. So I think ultimately it leads to a more dynamic and inclusive uh development experience.

**[6:16](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=376s)** So, how do you get to a software factory? Harness engineering, uh, as a sign of how fast terms evolve, it's also started to be called loop engineering over the last couple weeks. Um, this is really the core discipline that you're going to take to get towards a software factory. At its core, harness engineering is, you know, I mentioned the software factory is building your product. you are building the loops that automate and improve the quality of your factory. So what do I mean by loops? What are the loops that you might be working on? There are three core concepts each at maps to a certain phase of development. So you have your inner loop which is as the coding agent is working on a PR before it has put it up. Right?

**[7:07](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=427s)** So these are very fast iterative loops. You want them to be cheap. You're expecting the agent to run them all the time. Improvements here will drive better autonomy. The they help catch things and correct the agent without your uh coming in and human intervention. Once the PR is up, you move to the outer loop. So this is where you're going to put more expensive exhaustive checks that don't make sense to run over and over again as the agent is iterating on features, but they do encode things that otherwise a human would have to verify to build confidence in the system. And so this is because they're more expensive, but they are taking away human review time. They can be worth it, right? So this is where you might put something like aentic QA or where you might say like run mutation testing to check the quality of our test suite. This is for expensive things you want to

**[7:59](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=479s)** run once when the PR goes up and then have the agent iterate on on the results. Finally, you have the metal loop. This is where you'll drive quality. So the metal loop sits outside of the development process. It observes your coding agent logs. It looks at PRs, your issue tracker, user feedback, and it's basically finding mistakes that are making their way through the pipeline to your users or that you had to correct as a human to stop that from happening and it feeds back into the inner and the outer loop to make sure that that mistake is not made again. So the outer loop is what really kind of once you have the infrastructure for each of these loops, the outer loop or sorry the metal loop is where you're going to be

**[8:48](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=528s)** actually driving from a certain percentage of like how AI native am I? You're going to be driving it up by investing in your metal loop. Before we get into like what are the components, what do you do to actually accomplish this? I think full disclosure upfront harness engineering at least uh raw unassisted harness engineering is hard for a few specific reasons that basically come down to human psychology. So the first hopefully this one will go away over time but it's a new discipline and it's changing very fast and so a lot of teams that get into harness engineering you basically become an AI researcher just to try and keep up. you're reading papers, you're watching blogs, you're coming up with best practices that go out of date the next week and then two weeks after that and actually at some

**[9:41](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=581s)** point they become antiatterns and you don't want to do them anymore. Uh, and so there just like a lot of time and space you'll devote to keeping up with how to do harness engineering. And so if you want to get into this discipline, you need to have a sort of upfront approach to how you're going to solve this problem. How are you going to make time and space to keep up with the knowledge that's changing every week? The second, and this one is more durable in my opinion, harness engineering is fundamentally unplanned work. So you will start shipping a feature. You have no way to anticipate will agents fail? How will they fail? How long is it going to take me to fix it? And all of that work that you're going to do to try and make the agent better competes with shipping, right? So it will slow you down from getting the features out. And we all know that is just a perpetually hard trade-off to make. You either don't

**[10:32](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=632s)** do it and you get stuck in the local maxima of the agent never improves or you do it and you miss your deadline for the feature and you get in trouble and so no one ever does it. The final piece is that once you've solved these initial problems to like make time and space for harness engineering, you'll find that a lot of the information you want access to is not available. it's hidden away in local coding agent logs or it is on someone's machine somewhere. It's in someone's head. A lot of the signals that you want to see to make agents better, you need to do some work to move your workflows onto surfaces where everything is saved and publicly available for later optimization loops. Okay, with all that aside, then what are the pieces that you should be working on as you're doing harness engineering?

**[11:23](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=683s)** I've broken it into three layers. These aren't by any means standard terms, though if you want to help me make them so, I would be forever grateful. The first layer, and these are sort of like in the order you need to do them as far as Tesla is concerned, is you have to get your control plane right. And so I mentioned how most of the data that you want to have access to to make agents better and move towards a software factory is not legible. If you move your workflows into for example at Tessle we have all issue all work starts as an issue on the issue tracker. It gets sent to a headless agent running in a sandbox. The agent puts up a PR and then engineers engage with comments on the PR. So it still has manual correction. It still has manual interface but now all of your touch points with the agent are legible. So we

**[12:15](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=735s)** can you can then point tools at them to pull that information down and make things better. Typically the three things that everybody comes to when they're trying to set up a control plane. So you have some way of tracking issues and kicking off agent work from that. You're going to have some way to review. GitHub PR review is probably like the easiest. Uh and then you're going to have some way to uh standardize and distribute workflows, playbooks, things that make the agents better. Typically, that ends up being something like a skills registry or a shared GitHub repo where you push skills that improve agent quality. Next is a massive grab bag that I call agent it, which is uh if anyone's ever tried to move like a project that had a lot of local config into something that someone else can set up and you realize with horror all of the dependencies that

**[13:06](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=786s)** you thought were cleanly isolated and are not, you basically are going to have to go through the same thing with agents. There's going to be all these things that you thought were easily accessible by an agent, right? Like CLI, API access, giving a way for the agent to click through your product to build it. I I promise it's worse than you think. Like there's no one who has come in thinking like, yeah, yeah, yeah, it's not going to be that hard for us has left saying that at the end. And so there's just like a lot of pieces you'll work work through. And this is probably the most unplannable and most like spend a week, spend two weeks and just get it done. But it will come through things like writing writing down in your company brain how you get work done, what are your workflows, etc. You're going to have to give access to all your internal services, which will require

**[13:55](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=835s)** governance and like API access questions. You're going to want to give a way to access production logs. Uh, and that's going to have its whole own question of like what's your compliance stance, things like that. Uh, and then you'll need an environment where the agent can execute the code that it is running. There's infinite more, but they're generally pretty company specific, and you'll just work through as you try to get agents to put code up without you intervening. You'll quickly learn what are the problems. Finally, this is where you'll end up spending most of your time. These are the improvement loops. So these are the things I mentioned before the like inner outer metal loop. These are components that tend to go into your metal loop. So repo maintenance. You're going to want things that sweep your codebase every day, every night, every week, something like that to look for problems. You're going to want playbooks for common

**[14:46](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=886s)** development practices. So how to add a feature to your CLI. You're going to want to find a way to identify repeated tasks and automate them and ideally as quickly and easily as possible because otherwise people won't do it. And then you're going to want something that looks at the output quality just on a consistent basis and brings back improvements and learnings to the rest of your codebase. So say things like, oh, I saw the agent made this mistake. Let's update a skill on add like the playbook you have for adding features to the CLI. Let's update that so it doesn't make this mistake again in the future. So those three control planes Tessle sort of exist to try and help you solve them. As I mentioned, everything I've said before here are just techniques. You could go do them all yourself if you wanted. There's plenty of tools that do that. So I'm going to talk a little bit through how Tessle will help you if you

**[15:37](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=937s)** want to use us. To start, why would you want to use us? So we focus really hard on making it relatively iterative and sustainable to get to the cutting edge. So we try to make it like a bunch of small lifts rather than one massive snake eating the moose all at once. We're batteries included. So we solve the knowledge gap by saying we will keep up and you will have an agentic experience that basically knows the best practices of harness engineering is kept up to date on your behalf. We have a real commitment to being modular and open. So we don't think every component of a factory is going to be bestin-class with a single company. We want to make sure you can pick and choose what is the most important piece for your stack. And then like I said, we focus on making it easy. So we have automated loops for you that you can install and just react to the changes

**[16:29](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=989s)** that are proposed. And we really try to make sure it's just incremental steps so that you six months later like, oh wow, we're like 40% there to a software factory. We never had to stop and delay shipping or anything like that. So the first place that Tesla helps is in setting up your control plane. We have a skills registry where you can publish and version the workflows and the automations that you're working on with built-in governance things like security reviews, quality reviews, controls for who can publish and update what. We also have easy connectors for issue trackers to GitHub. Right now we're focused on linear to GitHub. So you can basically file a linear ticket and get it to run a GitHub workflow uh with more connectors coming soon. Uh and then we also have a suite of tools for code review. So this make it easy to set

**[17:20](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=1040s)** up your standards for agentic code review as well as more targeted checks. See here an example of something that like a workflow that has been posted to the registry being scanned for security quality uh and how much it actually improves the agents output. After this, I'm going to play a video while we talk. See how this goes. So, uh, we have an agentic experience called Tesla agent, which will help you with creating and then maintaining your improvement loops over time. So, the first thing that we do is we will help you with that change management of like how do I actually make the time to find repeated tasks and set them up in automation. So the agent will mine through PRs, issues, things like that and find like every week you do a hunt for flaky tests. Why don't we just set

**[18:13](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=1093s)** that up as a skill for the workflow and then we'll put it in automation on a GitHub action. So we help you actually make time to do the automations just like one workflow at a time. The second is that we come with a lot of out ofthe-box maintenance tasks. So I mentioned you want to have weekly scans for things like architecture quality, code duplication, uh how good are your test suites, do you have any security vulnerabilities? So if you use Tesla, you can just sort of like oneclick install a bunch of those things and just get weekly improvements to your codebase without any other effort. And then finally, we offer a way to turn any skill into an automated workflow. So it's through a command called Tesla launch where you effectively take a sk a skill that codifies a workflow. You can then pick a particular coding agent that you want to handle it. Tesla agent can be one of them. But for most coding

**[19:04](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=1144s)** tasks you probably want to use something like codeex, cloud code, gemini. We have access to all of them and we will run them in a sandbox that has the appropriate permissions. Can be long running. Uh we'll have GitHub token so that it can put up a PR and respond to comments as you leave them. Uh, so it just makes it really easy to automate workflows like that. And so with these things together, we just make it really easy to get started and just one at a time find an improvement, take a workflow, turn it into a skill, ship it to everyone, and then get your improvement loops going. The what you're going to want to focus on as you're doing this work is driving down manual takeovers, driving down human PR comments. So these are like metrics that you can track to see like how far am I towards software factory. And then over time you want to see more PRs initiated without human

**[19:55](https://www.youtube.com/watch?v=X6l4lpA0_NY&t=1195s)** input. That's a sign that you're automating more. And then of course you want to first hold quality constant and then aim to drive it up after that. That's it. If you want to learn more Tesla booth is just that way. Please give a scan, come over, see us. We'd love to chat. Um thank you all for your time.
