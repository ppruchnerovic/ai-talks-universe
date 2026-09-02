---
id: GfmK-v8CARk
title: "Furong Huang - Reasoning as Control: Adaptive Test Time Compute for Planning Agents"
slug: furong-huang-reasoning-as-control-adaptive-test-time
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Furong Huang"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T01:57:17Z
video_id: GfmK-v8CARk
url: https://www.youtube.com/watch?v=GfmK-v8CARk
youtube_url: https://www.youtube.com/watch?v=GfmK-v8CARk
tags: []
transcript: true
---

# Furong Huang - Reasoning as Control: Adaptive Test Time Compute for Planning Agents

**Furong Huang**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=GfmK-v8CARk) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,717 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=GfmK-v8CARk&t=1s)** FURONG HUANG: When people talk about self-improvement, oftentimes, we frame it as a model capability. The model can actually improve it's reasoning, and then started to actually learn from its own output, and hopefully, acquire some new skills. But I think model is just one layer. At the end of the day, it's going to be agentic system that is going to be deployed. And there are a lot of the infrastructure around the model, how the model is actually built. I think that's also a very interesting layer for us to understand how we can keep improving these infrastructure. And that could be even more important for very vertical applications that utilizing language models in your very own environment, in your corporate, in your own application areas.

**[0:49](https://www.youtube.com/watch?v=GfmK-v8CARk&t=49s)** And now, let's talk about what really happens in agentic system. Standard slides technical difficulty. So given a task, so you will be observing some kind of state, transitioning from an environment. And then this kind of observation goes through your thinking process. And at the end of the day, you wanted to make a decision. Maybe at every time you're going to make a decision, what is the best thing to do right now? And in order for agentic system to work, oftentimes because these tasks are very, very complicated, you want to decompose them into different agents. And you want to assign roles for them. And then probably, you want to design some kind of workflow.

**[1:39](https://www.youtube.com/watch?v=GfmK-v8CARk&t=99s)** Nowadays, I think we call it loop engineering. And then for each of the agents in your workflow, you want to decide, what is the action at every time step? And in order to do that, you need to go through a thinking process. Oftentimes, a chain of thought, for each action decision, the agent has to generate a reasoning trace. And you can see, there is this hierarchy of decision making during runtime. So starting from the very low level of thinking traces and token control, all the way to action control, at every time step of your decision making process. And then, finally, in the very high level, workflow control. Can you optimize them? And I think, today, I'm going to say,

**[2:26](https://www.youtube.com/watch?v=GfmK-v8CARk&t=146s)** foundation models are actually more and more becoming a runtime decision maker. At the end of the day, the self-improving a generic system is possible that you can improve the model capability. But you could also improve the infrastructure, improve how the model is deployed during runtime, across thinking, across actions, and also across workflows. So let's talk a little bit about what we did. Think in each of these levels. Down there in the thinking process, I think we started with the steering problem, where you have some kind of reward model. And you're hoping that you can steer your large language model to align to the specific reward. Of course, if you're familiar with the math, you will know that you have a closed form solution. And it turns out, this closed form solution gives you

**[3:16](https://www.youtube.com/watch?v=GfmK-v8CARk&t=196s)** a very short answer to the very complicated question of alignment, which is whatever your base model gives you, you just add an additional steering signal to it. And this steering signal is nothing but something related to a trajectory reward under some specific optimal policy. I know this is very complicated math. But at the end of the day, if you look at what is really doing, if you're thinking about a next token sampling from a language autoregressive perspective you're just looking at the language model's output. And then you just steer it with some kind of external signal that you can learn from your corporate data. So now, the actual discrepancy here-- sorry. I mean, I promised the slides looked way better on my laptop. But in this situation, there is a discrepancy

**[4:08](https://www.youtube.com/watch?v=GfmK-v8CARk&t=248s)** about you really want to next token generation. You want to steer your process as early as possible. But you cannot because your reward model does not really support that. You have a trajectory level reward model. But what you really want is an early steering before you actually determine your thinking process. So what we end up doing, for example, in a work transfer Q star, we started to think, OK, if the reward models are really not designed for scale up the average token sampling, let's just do the auto completion and use the reward model in the right way. Of course, this is right. But it's really, really slow. On the academic setting was my A6000 GPU. You can see, if you have to generate 500 tokens,

**[4:58](https://www.youtube.com/watch?v=GfmK-v8CARk&t=298s)** it will take you 14 hours, which is basically impossible. So you're doing it right, but you're doing it way too slow. So in a very recent work we tried to improve it by actually come up with a specific model family of reward. And we essentially design a token level reward and significantly reduced the cost by orders of magnitude. And as a result, you can see, this is phenomenal because you can do any runtime steering of the model. You do not have to train the model at all. You can even do weak to strong guidance. You can use a very small model to get a very huge model. And then you could even do multi-objective alignment in the sense that if you have very different objective, you can real-time adapt the objective to the specific user

**[5:47](https://www.youtube.com/watch?v=GfmK-v8CARk&t=347s)** need. So this is very cool. But what about the action? So we talked about steering your thinking process. But at the end of the day, your thinking process is really for service of your action. So how do you make the decision? Well, it is an agentic system. So we often know that agent systems are learned using this called imitation learning, which is essentially distilled from expert demonstration. But this oftentimes run into this kind of stuck loop problem, where your agents will repeatedly try some actions for many times until termination or you run out of your token budget. So that's very sad. So people started to think, can we do some better, smarter ways of learning through some world model training?

**[6:37](https://www.youtube.com/watch?v=GfmK-v8CARk&t=397s)** And specifically, people thought of imitating self reflection. But this is not actually self reflection. When you are trying to self-reflect, you're not actually using your self to reflect. You are actually mimicking some stronger model which teaches you how to reflect. And it turns out, it works better than imitation learning, but it's not really giving you very satisfying result. So we did a very simple thing here. We call it genuine self-reflection rather than actually imitating how stronger models think and self-reflect. We force ourselves to do the reflection in terms of choosing which action is better at this time point. And you can imagine, this is actually a world model. You're trying to build a mental model about which action

**[7:27](https://www.youtube.com/watch?v=GfmK-v8CARk&t=447s)** is better under what state. But you're also forcing yourself to understand why. This very simple thing. Worked really phenomenally. You can improve imitation learning as well as reinforcement learning. It actually improves significantly out of distribution performance. And also performs way better than previous state-of-the-art. So this genuine self-reflection really, really helps. And also, I think one really cool thing is that it actually generalizes to a general reasoning by just understanding how agents work better in a specific environment. You can see this critical learning does not relate to any general reasoning capability.

**[8:18](https://www.youtube.com/watch?v=GfmK-v8CARk&t=498s)** But somehow, it magically improves the general reasoning capability. So now, controlled decoding can steer how the agent think. And then act can actually help your agent understand how to, under what state, what is the better action. Now, finally, I think what's really exciting is this workflow control. Autonomously, decide what are your agent roles, and how do you actually optimize the topology of the agents, like the workflow optimization. So I have a very simple example here. But for the sake of time, just basically saying, this is a very fixed workflow for agentic safety kind of application. It works really well. But the question here is, can you

**[9:06](https://www.youtube.com/watch?v=GfmK-v8CARk&t=546s)** actually design such a framework, such that you have a meta designer? As the query comes, you could come up with the best agentic framework, the best harnessing that is specifically for this very specific task. Well, can you do that in an autonomous way? So people try to do this. For example, they tried this thing called one for all. And they also tried this thing for one for each. One for all basically means that you're going to find the best workflow in the world for that specific task. And then one for each is that you have to find the adaptability so that you can design the best flow for each of the query that comes into your model. So it turns out, we're thinking about this philosophy of foundation model.

**[9:56](https://www.youtube.com/watch?v=GfmK-v8CARk&t=596s)** So we don't want to actually do one of these two. But we wanted to say, can we actually pre-compute the workflow during the training time. But then, reuse them during the deployment time? And can we achieve efficiency through that kind of process. And it turns out, what we did, is we built a bank. We built a bank of workflows. And then during test time, yes, we're going to just adapt to the specific workflow real-time, really efficiently. And as you can see, the result also worked really well. You can see significant improvement of the performance. I can share a better version of the slide that is actually rendering. But if you trust me. So you will see the performance is really nice.

**[10:44](https://www.youtube.com/watch?v=GfmK-v8CARk&t=644s)** So just to sum up, we talked about self-improving agentic systems. We talked about how there are three levels of runtime decision makings that you can be very smart about how to allocate your compute resource with the limited budget, how to steer your thinking process as early as possible. So you do not have to go through the very lengthy process of thinking but in the wrong way. How do you control action? And finally, how do you do the workflow control? And with that, thank you. [APPLAUSE]
