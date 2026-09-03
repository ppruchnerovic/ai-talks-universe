---
id: j9iIotCIJUg
title: "Anastasis Germanidis - Real World Superintelligence"
slug: anastasis-germanidis-real-world-superintelligence
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Anastasis Germanidis", "Real World Superintelligence"]
channel: "Berkeley RDI"
duration_min: 14
published_at: 2026-08-09T23:27:18Z
video_id: j9iIotCIJUg
url: https://www.youtube.com/watch?v=j9iIotCIJUg
youtube_url: https://www.youtube.com/watch?v=j9iIotCIJUg
tags: []
topics: []
transcript: true
---

# Anastasis Germanidis - Real World Superintelligence

**Anastasis Germanidis, Real World Superintelligence**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=j9iIotCIJUg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,845 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=j9iIotCIJUg&t=1s)** ANASTASIS GERMANIDIS: Hello, everyone. Good to be here. So today, I'm going to be talking about some of the work that we've been doing at Runway, focusing a lot on both video generation about world modeling increasingly. And I'm going to also talk about some of the early progress and early work that we've been doing in robotics in particular. So I think everyone probably here is familiar with this graph. Every year, the time horizon that a coding LLM can solve various software tasks is doubled every year. There's been an incredible amount of progress happening in the language domain in particular with the coding agents. Yet there is this contrast. There is this incredible progress happening

**[0:51](https://www.youtube.com/watch?v=j9iIotCIJUg&t=51s)** in math and in coding. But some of that progress actually doesn't transfer as well to tasks that have to do with interacting with the unpredictable real world. So whereas every day we hear of an amazing an unsolved problem conjecture being disproven, LLMs still fail at rudimentary tasks such as running a vending machine business effectively. And I think the reason why really has to do with how effectively we train those models. For coding and for math, we have this luxury of having sandboxes that we can run at effectively infinite scale.

**[1:43](https://www.youtube.com/watch?v=j9iIotCIJUg&t=103s)** And so we can scale rollouts inside sandboxes very, very easily. For a lot of the real-world problems that we care about, we don't have a simulator that we can run very easily, that we can scale rollouts, and it's very time consuming and very expensive to scale rollouts in the real world. And so one way of approaching this-- and this comes to no surprise, given the panel and the section that we're in-- is this idea of world models. And a lot of people are familiar with world models from the David Ha paper in the 2010s. But actually, that concept goes back into the mid-20th century in cognitive science and some of the early kind of model-based RL work as well.

**[2:35](https://www.youtube.com/watch?v=j9iIotCIJUg&t=155s)** And it's effectively this idea that the way we operate as humans is we constantly predict and try out things in our heads. We try to understand what the outcome of actions that we take in the world will be before we take those actions, and that helps us plan what to do. But in order to do that effectively with agents, we need to have this simulator of experience that an agent can use to predict what happens if the agent takes specific actions. And when it comes to real-world experience, what is the best way to bootstrap such a simulator? I think video is the most general modality that we have that allows us to simulate real-world experience. It's the most abundant kind of source of real-world scenarios.

**[3:29](https://www.youtube.com/watch?v=j9iIotCIJUg&t=209s)** It can teach us about physics. It can teach us about all the tasks that humans care about. And video is even more of a general presentation than that. It's not just about real world, human scale video that's captured by a camera, but it's also video can be used to represent scientific observations from many different scales, both temporal and spatial scales. And it can also be used to capture observations from the digital world, which is especially relevant if you want to teach agents to work with the variety of interfaces that we use every day. And so our approach at Runway has been predicting the world by predicting the next frame. Essentially, we believe that pixelframe prediction

**[4:18](https://www.youtube.com/watch?v=j9iIotCIJUg&t=258s)** and pixel generation is the right auxiliary task to train at massive scale and build models that have really powerful representations of the world. And then you can use those models for a variety of downstream tasks that you care about in the real world. And so just to give a sense of where the quality of video generation has gone, I'd like you to take a moment and look at those two videos and just think, if you can tell apart which one is-- one of them is generated. One of them is real. Can you tell apart which one which? SPEAKER: The right one is generated. [INDISTINCT SPEECH] [LAUGHTER] ANASTASIS GERMANIDIS: That's correct.

**[5:04](https://www.youtube.com/watch?v=j9iIotCIJUg&t=304s)** I think the right one is indeed generated. What about this one? I believe that it's the left one this time. What about this one? So the left one is generated in this case. So we run this as a user study. We ran it with 1,000 participants. And it's actually reliably less than 10% of participants could tell apart what was generated and what was not generated. So whereas if you're very familiar with video generation,

**[5:56](https://www.youtube.com/watch?v=j9iIotCIJUg&t=356s)** if you look at those videos for a long time, you will be able to tell apart which one is real and which one is not. It's becoming more and more difficult. So from a quality perspective, we've really kind of crossed some threshold where it's easy to trick human perception. And so this has been a very long journey over the past decade or so of increasing the compute and data scale that we put into video models. So these are some of the milestones. Gen 2 was the first text-to-video model we ever released a few years ago. And Gen 4.5 is the latest base model that Runway has released. So there is a massive improvement in the ability of these models to simulate physics, to have dynamic motion, to really

**[6:46](https://www.youtube.com/watch?v=j9iIotCIJUg&t=406s)** feel very plausible real-world video. And so there's been all this amazing progress for creative video generation. But how much of this progress actually translates into the stuff that we care about for physical AI? It turns out it's quite a lot. Video generation can be used to simulate a lot of long tail scenarios that are basically impossible or incredibly expensive to simulate otherwise. And we have pretty robust ways of measuring that. Obviously, there's a lot of work in physical evaluation, but there is some really great benchmarks that allow us to really compare real world video from generated video across a lot of different categories of content of physics.

**[7:37](https://www.youtube.com/watch?v=j9iIotCIJUg&t=457s)** So from solid mechanics to fluid dynamics to thermodynamics and optics. And even there when it comes to actually beyond plausible video, if it's actually physically accurate, we see that increasing compute scale really reliably improves the physics of those models. The bitter lesson really applies to video models. And we see that predictably across all the video models that we've trained. And so the next stage towards actually making those models useful for the real world is making them real time and interactive. For a lot of the use cases that are relevant for real world problems, like in robotics, that's a very important thing if you either want to build a simulator or a policy model

**[8:28](https://www.youtube.com/watch?v=j9iIotCIJUg&t=508s)** on top of a video model. And the way we do this, and our approach, is really taking the foundation video model that we have, the base kind of diffusion model that generates video, that's bidirectional, and making it autoregressive and causal. And then doing another stage of distillation to make it real time. And what this allows is making the model interactive and allow you to explore counterfactual scenarios very easily. If I take this action versus this action, what's going to happen? And you get frames generated on the fly based on the actions that you take. And there is this increasing trend as we're building world models of increasing the generality of the world models

**[9:19](https://www.youtube.com/watch?v=j9iIotCIJUg&t=559s)** and also increasing the flexibility of the world models. So one of the early world model in the original paper of David Ha was trained on a particular kind of racing game. There were a lot of work in World models specific for narrow domains, like in self-driving kind of footage. So generating cars moving in the road to World models that were released last year, like Genie, that were really high fidelity, kind of mostly static environment, allowed static environment navigation, and a lot of the progress that we've been focusing on has been, how do you make those world models actually dynamic? How do you allow simulating, not just navigating a static world, but actually taking actions in the world

**[10:09](https://www.youtube.com/watch?v=j9iIotCIJUg&t=609s)** and ideally taking actions by multiple agents? So in this case, you have two different agents that basically you instruct at the same time and you're simulating the outcome of that. And one of the variants of the world models that we've built has been in robotics specifically. So this is GWM robotics, which is an action-conditioned video model that's specific to simulating the outcomes of actions of single-arm or bimanual arm robots. And we've seen that in a lot of cases, the rollouts that are generated by those models are, again, very difficult to tell apart from ground-truth teleop data, for example, and it's able to simulate very fine-grained interactions with cloth or other kind of non-rigid objects.

**[11:03](https://www.youtube.com/watch?v=j9iIotCIJUg&t=663s)** And what this allows is making evaluation much more scalable. Essentially, you can use any policy model, which could be a VLA or another policy model, and you can predict what happens as an outcome of a particular action and then feed that back into the policy model. And what we've seen is that those GWM robotics and the world models that we're building for robotics actually match the real world quite well. So if you take a policy model like Pi 0.5 and you have some ground-truth teleop data, and you're rolling out the exact same actions inside the world model, you're seeing very good correlation between task success in the real world versus simulation.

**[11:53](https://www.youtube.com/watch?v=j9iIotCIJUg&t=713s)** And so you're able to massively scale how fast you can evaluate policy models by doing that inside the video model, instead of doing that in the real world. And in the future, this becomes also a great foundation for doing RL inside the world model and being able to scale interactions much further or much faster than you would in the real world. And one of the most important aspects of building world models is this ability to simulate failure. A lot of traditional video models have this bias towards success. It's much more easy to generate a video of someone shooting a goal successfully than not. But that's something that's very important when building world models, because if you want to evaluate

**[12:43](https://www.youtube.com/watch?v=j9iIotCIJUg&t=763s)** how well a policy works, you want to be able to reliably have the policy model fail if it performs their own actions. So the ultimate goal of world models is really to increase the number of observations that we put into it. We believe that learning simulators is a much more scalable approach towards building environments where you can train agents in situations where it's very difficult to build traditional simulators, to author them by hand, or it's very expensive to actually perform those actions in the real world and gather data. And that's all on my end.

**[13:31](https://www.youtube.com/watch?v=j9iIotCIJUg&t=811s)** Thank you for your time. [APPLAUSE]
