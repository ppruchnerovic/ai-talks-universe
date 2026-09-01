---
id: j5U7_G8kvkY
title: "Chenguang Wang - From Training to Evaluation: Open Recipes for Building Agentic AI at Scale AI"
slug: chenguang-wang-from-training-to-evaluation-open-recipes-for
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Chenguang Wang"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T07:52:21Z
video_id: j5U7_G8kvkY
url: https://www.youtube.com/watch?v=j5U7_G8kvkY
youtube_url: https://www.youtube.com/watch?v=j5U7_G8kvkY
tags: []
transcript: true
---

# Chenguang Wang - From Training to Evaluation: Open Recipes for Building Agentic AI at Scale AI

**Chenguang Wang**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=j5U7_G8kvkY) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,636 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=1s)** CHENGUANG WANG: Hello, everyone. My name is Chenguang Wang. I'm currently an assistant professor at UCSC. And in the meantime, I'm also, I think, working with Emily also closely at Scale AI as a research advisor. So today, I'm going to talk about basically, the post-training to evaluation, what we've been working on, try to build the frontier, hopefully, agents using what we have already at the Scale AI. Let's get started. So I think I can spend a little bit of time on talking about if you guys don't know Scale AI. So the mission of the company is, really, just try to build a reliable AI systems for the world's most important decisions.

**[0:50](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=50s)** I think it's founded by Alex in 2016, and it's pretty big right now with many employees and the offices across US and also other countries as well. But I will get straight to today's topic. I will cover mainly two topics. One is the post-training as part of in the title briefly, but only briefly because we only have 10 minutes. I think the second part, we'll be talking about evaluation. And I try to bring some synergy between those two components. So I will start just with the general idea about the current research focus at Scale on the post-training part, which is trying to raise. A research training is also like this, moving from RLHF

**[1:41](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=101s)** to a rubrics-based RL. So I think this is a practice we got from basically working with frontier labs to providing the data, services. And we figured out this is something really important for post-training. So there's definitely challenges over there. How to really design effective reward and how to use that reward with RL and how to make a reward even better during the training during RL phase. So we have been publishing at Clear this year SML. Hopefully, we get something also at the NeurIPS, so on and so forth. It's in the middle of the response. But we are able to push the boundary of GRPO. By using a rubrics-based reward paradigm,

**[2:31](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=151s)** just basically improve the performance and is able to also gather some interesting recipes or basically insights from the process of training and also working with the data, how to basically play with this flywheel, the data and RL part. Hopefully, I can get something for the takeaway for you guys today right. So the first thing I want to focus on is really this RL recipe. We actually realized it's important. I really want to highlight or avocado this. It's basically the rubrics-based reward. So this is important because in general, so if we want to make RL work.

**[3:19](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=199s)** So previously, I think the training is on the so-called variable domain, where you can pretty much know-- for example, coding or math-- you can pretty much know whether this is true or false. You pretty much get ground truth verification. But in many real-world cases where we really care about-- frontier lab we really care about is really you want to make this work for domains where there is no verifier. Whereas it's not a verifiable domain. So we need to find out a way to make it work for those open-ended domain. Could be science, could be something else. Could be for our personal tasks. So we are trying to basically set up this paradigm where we ask basically a criterion or evaluation criterion and turn that into verification,

**[4:13](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=253s)** something like that. So we are able to really, I think, build a new reward model, which is not basically distinguish a better response versus a worse response. We are trying to say which one is backing basic better and is ranking-based from rubrics so it can scale up to real-world scenarios. And we build a reliable pipeline like we show, I think, in these two figures where we can start with something simple and gradually build a very high quality rubrics and use that in RL phrase. And we witness improvements on open-ended tasks. That's a takeaway. And then, this is a natural extension of the first work is also on rubrics, where

**[5:02](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=302s)** you train the model, but the policy will change. Your policy becomes better, better code. But there is still something is changing. So you have a reference policy, you have some current policy, and you figure out what is missing in the current reward and generate better rubrics or online rubrics where you can integrate this into the reward model. Where then you can pretty much just train better, better and be more robust to downstream tasks. So this kind of online rubrics evolution aligns very closely with the recent trend in, I will say, self-improvement or recursive self-improvement line of work. We are moving towards there. And the second part, I think that's pretty much-- I just want to highlight a few research on the post-training.

**[5:52](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=352s)** And I think in evaluation space, I think definitely Scale's main focus is really basically driving those insights from the training and talking to the customer and then build the worl's basically worldwide leaderboard for those frontier models to be on. So there's many going on, but I would just want to highlight a few projects recently. So many of you guys, definitely, it's really a working demo of agents. It's like SWE agents or coding agents. I think Scale invest a lot in this domain try to build a reliable benchmark to try to understand what's the true capability of the agents. Of SWE agents.

**[6:41](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=401s)** I think you guys know benchmarks such as SWE Bench, SWE Bench Pro, where you can pretty much just think about the problems like there's some text description about the problem in GitHub, and you just need to ask to generate a patch, which can eventually just fix whatever bug in the original repo. But I think in the real world is much messier, where I think as an engineer, we are not only just looking at the PR and looking at the issues and the generator response as a patch. You need to deal with those writing a unit test sometimes. You need to even figure out the problem by just basically go back and forth looking at the repo, ask some questions, and answer that question so we can figure out what to do next. So that would be some insight that we

**[7:30](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=450s)** can borrow very differently from working with benchmarks such as SWE Bench, SWE Bench Pro. So we released this new benchmark called SWE Atlas right. I think it's widely adopted by frontier labs right now. And other than SWE, another focus of the agent eval we are building is in this professional reasoning domain or this kind of AI for science domain. I think, definitely, I don't need to say too much about HLE, which is like a professional reasoning benchmark. I think people are still trying to hill climbing, try to become better from a model families. And also, we are also working on this drug discovery bench, which is trying to really build some real-world health care

**[8:20](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=500s)** environment, where we just work with experts, generalists, real-world drug discovery tasks, where we start from the concept and then deliver actually the drug. We recently also released a preprint on that regard. And we are also working on tool use. So there is a debate on what is the best tool interface. Is this a CLI or is this MCP. I think we got an interesting conclusion just high level. We found out once a model becomes really capable, like a recent cloud 4.8 or GPT 5,5 or 5.6, that doesn't matter. The model will learn to use the best tool interface possible

**[9:15](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=555s)** in a real-world scenario. So that really doesn't matter. Unless you basically you give the same back end to write, the interface really doesn't matter. And then we're also working on this computer use agents. We are trying to benchmark computer use agents. So we are trying to scale up the computer use agents environment benchmark, because each of the computer use benchmark is really very expensive to run. So it's multimodal. And there's many, many details you need to consider in terms of verifications. So we think about a way to actually based on some existing high quality benchmark and really just generate long horizon, more challenging, more real-world tasks from based on those existing benchmarks. I think we showed that we can pretty much bring down

**[10:05](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=605s)** the performance of the original OSWorld, where the state of the art of the OPUS new version is something definitely beyond 80%. Bring it down to something 30%. So there is a way we can construct real-world data sets synthetically but in a very high quality way. This is pretty much what I want to just final slides, technical slides where we can pretty much build a synergy between evaluation and post-training. Just draw insights from post training and try to build a better RL environments. And also draw insights from evaluation failure mode and try to build a better post-training algorithms. Hopefully, this can run forever. So we got those better eval and better training result as well. So just closing, I think Scale is

**[10:57](https://www.youtube.com/watch?v=j5U7_G8kvkY&t=657s)** working with many different frontier labs, governments, and also enterprise and robotics on this physical AI. And another advertisement, we got this third edition of the Agency in the Wild workshop accepted at NeurIPS. The deadline is coming soon, in the end of this month. I'm one of the core organizers there. So we have a wonderful panel of speakers and panelists. [INAUDIBLE] is there. Joshua is there. Java is there. So feel free to submit, and see you guys at Sydney. Yeah. That's it. Thank you. [APPLAUSE]
