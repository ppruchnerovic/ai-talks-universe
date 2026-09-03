---
id: ZSQb5fzRFPw
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua"
slug: computer-use-2-0-agents-just-got-multi-cursor-francesco
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Francesco Bonacci"]
channel: null
duration_min: 17
published_at: 2026-07-15T00:00:00Z
video_id: ZSQb5fzRFPw
url: https://www.youtube.com/watch?v=ZSQb5fzRFPw
youtube_url: https://www.youtube.com/watch?v=ZSQb5fzRFPw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: true
---

# Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

**Francesco Bonacci**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ZSQb5fzRFPw) · [Conference site](https://www.ai.engineer/)

## Description

Three agents click, type, and scroll through three different apps on one desktop at the same time, and the user's own mouse and keyboard never move. That's the live demo behind cua driver, a tool the team built in a single weekend after Codex shipped its own computer use model. Instead of taking over the hardware cursor, it talks straight to the accessibility layer underneath the operating system: UI Automation on Windows, AT SPI on Linux, AX on macOS. Those undocumented APIs let a click land on a background window or a keystroke reach a hidden one, so any number of agents can act without stealing focus from each other or from the human sitting at the machine.

To know whether any of this can be trusted, the team built CUABench: over 130 verifiable tasks across 42 environments and five platforms, each one attacked by a matrix of agents trying to reward hack it before it's allowed into the dataset. Swapping a standard computer tool for cua driver pushed pass rate on a 4K benchmark from 62% to 80% while using 34% fewer tokens, mostly because it watches one window instead of the whole screen. The newest addition, built with Snorkel AI on real circuit design software, humbled every model tested: the best agent fully passed only 6 of 25 electrical engineering tasks, every one of them an edit to an existing schematic, and starting from a blank schematic dropped every model straight to 0%.

Speaker info:
- https://www.linkedin.com/in/francesco-bonacci-70428a121/

Timestamps
0:00 - Introduction and Vision of Cua
2:40 - Overview of Cua Driver and Background Operation
6:34 - Introduction to Cua Bench and Agent Evaluation
10:50 - Cua Fleet and GPU Infrastructure Optimization
15:08 - Q&A Session
15:44 - Discussion on Mobile and Android Support

## Transcript

*2,618 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=1s)** [music] Thank you for taking the time for coming over here. Um I'm Franchesco. I'm the CEO of the company. Uh alongside me, a couple of other folks. Um my co Dylan and my chief of infra Rob. They're going to walk on the stage in a while. Uh but before we do that, who's excited for some computer using agent talk happening now? Are you guys excited? Lovely. Um if I were to ask like what what was a computer using agent like one year ago, probably half the crowd would say I don't have any idea what really computer use mean. Um so um today I'm going to take you to a journey. Um

**[0:50](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=50s)** basically like from our vision where um we come from so far on computer user um like this new shape of like agents are talking um and uh up to model intelligence um so we're going to start like with the vision of uh quad driver where we're coming from and uh if you how many of you guys been been working with computer use for one year. How about like two years? Lovely. Okay. So, our team has plenty of experience like we go all the way back uh our time on Microsoft. We were working on this type of guey agents we were calling them uh back in the days. Um and uh there is a

**[1:41](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=101s)** um there's an example of like old-fashioned human uh agent loop. Um we basically refer um refer this as a human uh loop where you will have like an agent loop. You will have a um uh you will take a screenshot that the agents will have to reason and plan through and then um you will basically work with an action space in terms of like clicking, typing, scrolling around. So this is what we refer as as um um the old fashioned like computer use 1.0 you know, just to set the tone for for um for this talk and uh we come like a long um a long like way since this type of like um computer using agents. So this is this again like I'm going to skim

**[2:28](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=148s)** over these slides but that's like the old fashioned way of like representing these agents loop as a human would do. Um we um here we go. Um over like two months ago we released a project in open source. It's called quad driver and uh um we um we made it working like in the background. That means that your computer user will will not take over your uh screen as like the computer use 1.0 um kind of like agent loop was doing back in the days. And uh um it all like started from uh um from like uh um from Codex releasing their computer use um

**[3:18](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=198s)** model two months ago. So we kind of like take the challenge because we were already like working with this uh this type of background computer user. So over one weekend we act something together. And uh the trick here is really um not like having your agents like take over your screen. So there is a lot of like dark magic like happening behind the wood just to uh give you some context. Uh there are like some undocumented API um living in u um in the Apple framework that basically ships with your laptop and as you can see here like is in the demo you have like an I agent that is not taking over uh control of your over your laptop. Um we made it working not only for Mac OS but also spanning like across Windows and Linux. where uh this is like the very first

**[4:05](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=245s)** like driver that is uh living on your um laptop and uh it lets uh really any agents connect to the underlying operating system uh either like using accessibility trees or like a screenshot level approach. We kind of like take all um this is what really the agents see for what it concerns. Um you will have to install quad driver. Um the agents will uh will take a snapshot of the window state and uh you will have to observe um and uh we really like take take like one uh uh like different like action path to really make the ground computer use happening. So you really um have um to observe the space in this

**[4:55](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=295s)** case just by calling like get window state you get a an accessibility tree representation plus a screenshot and then you will go and uh um try a background execution using accessibility tree and if that doesn't work we go all the way and uh make the heavy lifting for you and just try a pixel background click. This is like uh kind of like best step for background at this stage. It's not like behaving in the same way Mac OS, Windows and Linux. So uh we we do like some of the lifting for you so that your AI agent can uh can run and disturb on your uh on your MacBook. um how we manage like to not break anything between like release cycles. We have ex we have like a lot of investment

**[5:44](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=344s)** happening uh behind the scene uh when we test like new releases. uh we have about like eight different uh application harnesses that are um that that that we that we use for making sure that we don't break anything uh among different releases. Um among our early adopters you can see like clicky mass queno h company and droid factory. uh like huge thanks to them for using quad driver and like um basically releasing a lot of like upstream contribution back in in our framework. Um without further ado, I'm just going to move to the next part of the presentation which is going to be intelligence. Um and I'm going to have our CTO Don cover that.

**[6:34](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=394s)** >> Hello. So thank you Franchesco. Um with cooler driver we gave an agent hands but then the question becomes how can you trust the agent to use those hands correctly and not leave anything broken behind and to answer that we had to build kuab bench so for a show of hands who here has heard of terminal bench or harbor yeah so a few few of you have heard of it and uh if you've ever authored a task for terminal bench then this might look familiar but in kuabench a task is made of three pieces the setup setup function which sets up the machine to initial state. The oracle function which provides a golden trajectory for the task and the evaluator which probes the environment to check if the agent successfully completed the task. Uh unlike terminal bench the oracle here is

**[7:25](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=445s)** guey actions. So it looks kind of like pile of gooey when you write that and writing environments takes scale and expertise. On desktop there's more than uh five platforms that we target and um we try to collapse that into a single Python file. So using the Kubaben SDK you can write a guey that works across every desktop platform in a single Python file and use the same SDK to probe that GUI to get usable agent data. Anyone or any agent can author one of these tasks and when you put that to work you get a real catalog. We have currently over 130 verifiable tasks, 42 environments, and across five platforms. And each of these are easily reproducible using our CLI. And the latest addition to our data sets

**[8:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=495s)** is one that we're proud of. Uh with collaboration with Snorkel AI, we built KUBench Kyad, which tests computer use agents on electrical engineering tasks using software by real professionals and evaluator functions that actually simulate the circuits. But the results are humbling. The top agent that we tested only got a full pass on six out of 25 of these tasks. Of those six, 100% of them involved editing an existing schematic. And when we start the task from a blank schematic, the success rate drops to 0%. And across all the models that we tested, the leaderboard is flat. No model has achieved more than 30% reward. But once you can score something, you

**[9:06](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=546s)** can improve it. If we take a look at the Kua bench basic data set scaled up to 4K resolution uh testing an agent they typically get around 62% pass rate but when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens and this is primarily because KU driver focuses on a window rather than the entire desktop but our evals might say you can trust model XYZ at task whatever. But how can you know that the task how can you know that the eval can be trusted? So before we test a task against any agent, we first try to break the environment ourselves. We have a matrix of agents attempt to do reward hacking and

**[9:55](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=595s)** attempting to break the environment and we take all that data and we compile it into a nice code rabbit style code review and only tasks that survive our pipeline can enter the data set. And if you ask us how we trust that agent, the answer is that it's just evows all the way down. But to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions. You also have to measure its ability to understand the world that it's operating in. Every run that we record can be forked through any moment in its trajectory to give you the state of the computer at that moment. From there we can probe a model asking to predict the reward, the internal state or any other observation of the computer and compare it against the fork. And that prediction is the world model of the agent made

**[10:44](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=644s)** measurable. And with that um I'll let Robert take the stage. >> Thank you Dylan. Uh hello everybody. Uh I am the chief infra officer at Kua and I'm here to talk to you about um how you're probably leaving a lot of money on the table uh with idle GPUs if you do RL training uh for computer use agents. So I kind of want to introduce this uh diagram to y'all. Uh could I get like is is there like general familiarity with this diagram or this like something that most of us haven't seen before like any anyone? Awesome. Very niche. Um Almost everything on this is not really important for what we're talking about, but the blue portions are um and what those basically represent are GPUs uh

**[11:32](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=692s)** generating tokens for um RL uh training. And if you zoom in on this a little bit, you can kind of see like how this typically looks like with a sandbox environment is you're going to be generating some tokens um and then you finish your task on a sandbox and then you're waiting for either like a new sandbox to spin up or for your existing one to reset. Uh the problem here is that like this is just pure cost. um your GPU really isn't doing anything useful here and you know I don't know if you've heard but GPU time is pretty expensive right now. So um as you're scaling this cost really compounds a lot and you really want to focus on minimizing this if possible. So one thing that you might try to do is

**[12:21](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=741s)** uh minimize the startup time of your sandbox. And I mean you should do that like that's a great thing to do but uh you know especially for computer use style environments sometimes this can be a little bit impractical. Um you know your researchers might give you like a 40 gigabyte environment and that might just be necessary and it takes a long time to pull that down and start it up. So you know how do you how do you design your training infrastructure so that you can minimize the GPU startup or the minimize the startup time of the sandbox? uh even when the sandbox is like not well designed to be start up quickly. Um so the way we do the oh man is it not so the way we do this is a pool and this is supposed to be animated but it's not

**[13:12](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=792s)** animating. So um I guess I'll just explain to you orally and what what that is is uh so we have like a a set of GPUs here which all want to use a sandbox and what we will do is that we use a demandbased autoscaler to detect um how many GPUs like currently need a sandbox and we can grow the pool to be that size uh on demand. And what that means is that uh if you have let's say like you have a warm pool that you want to allocate to your GPU cluster, you don't actually need to know upfront what that warm pool size is. We can figure out what that warm pool size should be for you um on demand. And that might even change over the course of your multi-day training run. Uh you might start needing

**[14:00](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=840s)** a lot of sandboxes, but then as your generations get longer, you might need less. So these also could be like, you know, easily uh two to four times cheaper than your GPUs. So having a little bit of redundancy here, uh you still wind up saving money because you're maximizing the use of your GPU time. Um yeah, come see me after if you want to see the animation because it's it's cool. Um so yeah so now when you have like this like uh redundancy in your pool you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization um yeah and then because we use this we can give you instant sandboxes for your

**[14:49](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=889s)** GPUs for Windows Windows Linux Android uh and Mac OS is coming up Um, and I'm going to hand it back to Franchesco to uh close it out for us. >> Lovely. Uh, thank you Don, thank you Rob for taking this over. Um, we do have like plenty of time for Q&A. So if you guys like have any questions like happy to um take them either for quad driver qua bench basically what Dylan presented or qua fleet uh which is like what uh Robert covered any questions otherwise we can wrap this up. Oh, I see.

**[15:44](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=944s)** >> Um, so the story for mobile Android there is very far you can go. Um, we are talking with the arm team because they do have like an arness that runs on Android. I guess like if you're talking about background there is some level of like background that can happen if you containerize a workload and basically on Android you can even like run your own container or like sort of like Ubuntu or like GUI docker container uh within Android um but yeah the Android ecosystem especially compared to iOS is more inclined to that form of like background uh computer use but it's more towards like tool use than really like controlling GUI interface. Um we work with the activity framework and uh do tool use in the background.

**[16:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=998s)** >> Cool. Thank you guys.
