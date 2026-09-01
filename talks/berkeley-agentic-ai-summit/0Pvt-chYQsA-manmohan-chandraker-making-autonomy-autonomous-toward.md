---
id: 0Pvt-chYQsA
title: "Manmohan Chandraker - Making Autonomy Autonomous: Toward Mental Models for Discovery and Intuition"
slug: manmohan-chandraker-making-autonomy-autonomous-toward
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Manmohan Chandraker"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-12T01:36:06Z
video_id: 0Pvt-chYQsA
youtube_url: https://www.youtube.com/watch?v=0Pvt-chYQsA
tags: []
transcript: true
---

# Manmohan Chandraker - Making Autonomy Autonomous: Toward Mental Models for Discovery and Intuition

**Manmohan Chandraker**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=0Pvt-chYQsA) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,507 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=1s)** MANMOHAN CHANDRAKER: Hey, everyone. It's good to be back at Berkeley. I'm going to be talking about autonomous agents and maybe a little bit about humans, too. All right. So I think all of us here will agree that physical AI lives in the open world, we have endless edge cases that arise after deployment, and we have teams that go into continuous discovery and development loops to fix these edge cases. And all of these must be fixed with traceable released evidence. Now, the physical world is also rapidly becoming executable, right? So we have all of these CI/CD frameworks that can continuously run loops, we have agents that can deploy code, we have simulations to bridge gaps to data, and all of this points to a future of self-improvement. However, physical stacks are complex

**[0:53](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=53s)** and require real-world experimentation. And a lot of real-world knowledge, human expertise, is something that lives beyond static data. It requires us to have scientific ideas, it requires us to have expert workflows, and physical interactions with systems. All of this means that experimentation and discovery is something that requires a lot of compute, a lot of data, and a lot of human talent for us to run in physical workflows. So in the next few minutes, I'm going to be talking about making autonomy autonomous in collaboration with humans, and how we can have discovery frameworks that are grounded in execution, how we can reflect human intent in agentic workflows, and hopefully sustain participation in AI native economies.

**[1:44](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=104s)** All right. So let's take this example scenario. Suppose you have an autonomous driving team, and you observe that you have an issue with perception for pedestrians. That would go to a simulation team who would need to figure out a way to handle these. Maybe pedestrians are thin structures, and it requires us to have better 3D reconstruction. So the team can come up with, let's say, Gaussians splatting or a new method for Gaussian splatting that can then be validated on real data, and eventually they can write a paper about it or publish a spec sheet. Now, what if I told you that this whole process is something that is run by a team of agents? The only input that comes from the developer in this case is to generate ideas, to improve 3DGS, to work with pedestrians for autonomous driving,

**[2:32](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=152s)** test it on a particular family of GPUs, validate it on real benchmarks, compare to baselines, and publish a paper. So the team of agents here plays a set of specific roles. In particular, they produce research that is verifiable, they deploy code that is executable, they come up with ideas that are grounded in the physical world, and, in general, follow a process of scientific discovery that's traceable and verifiable. So let's look at how this works. You have the input command. The agents define the task that must be solved. In this case, OmniRe, a framework from NVIDIA, is something that they decide to improve upon. They come up with hypotheses for dimensions where improvement is possible.

**[3:20](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=200s)** Specialist agents then launch a set of different experiments. All of these experiments are evaluated, i.e., they are validated and falsified on an Elo-rated tournament. Eventually, there's one idea with the highest Elo rating that would survive. This is a new method that comes up in this case, which has been implemented on real GPU hardware, so the gains are measurable. It is something that can be evaluated on real benchmarks. And then a team of writer and reviewer agents can come in and write a paper about it. So, how good is the system? Well, so we took a few of these papers, and we submitted them to a CVPR '26 workshop on physical AI-related topic with permission

**[4:09](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=249s)** of the organizers. By the way, we are not trying to game the system. But three out of four papers that we submitted did get accepted. One of the papers got high praise. The paper that was rejected did have formatting issues with the equations and all, so we believe [INAUDIBLE] too in this case. But overall, this is not a system which is just for ideating and for writing papers. It's a system which is performing traceable and verifiable scientific discovery. So, how does this work? Everything rests on a verifiable substrate on top of which we can work. We define a context-free grammar, which allows us to come up with ideas that are grounded. Every candidate method is something that mutates on top of a verified reproduction. So everything is something that we can measure,

**[4:58](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=298s)** it's something that we can validate and falsify. Finally, every claim that is made by the system is something that we can trace to a real log or a real line of code, a real GPU run. So the central engine that drives all of this is essentially this verifiable substrate. And how do we go about building this? Essentially, we reverse engineer the process. So suppose we have a knowledge repository, suppose we have papers. Can we then follow this scientific process to come up with a code that wrote this paper? So how does that work? Let's take this example. We have a paper out here that has never been publicly implemented, so it's not like Claude or GPT knows about this paper. We analyze the paper, we determine

**[5:48](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=348s)** what are the new ideas, what are the factors that are giving us improvements over baselines. And those are the things that are then produced in the code for this paper. The code is something that is physically verified against real data. Improvements are suggested for the code, and this is something that we can then validate on real benchmarks by comparing to real data. So this then forms the verifiable substrate on top of which discovery can happen. Now, if we have a full-blown application like autonomous driving, then what would be the execution loops that build these verifiable substrates in that case? Fortunately, over the years, for autonomous driving, we have been working on many such agent substrates that do data analysis for us, that do simulation, that do AI model training and validation.

**[6:36](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=396s)** So, for example, given a bunch of computer vision and machine learning tools, we can have data agents that can analyze all sorts of edge cases. Given an input from the user, for example, get a car to change lanes, cut in, or cut out, we can get our simulation agents to reconstruct the 3D background, to reconstruct all the dynamic agents in the scene, deploy diffusion models that can come up with novel reactive behaviors in challenging edge cases, and finally, other diffusion models that can do photorealistic rendering. Or our development agents can take all the ODD specs, they can take all the data tools that we have, the simulation tools that we have, and do AI model training and validation. So once we have these autonomous systems that are driving autonomy, what does it

**[7:23](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=443s)** mean for the role of the human? And I believe that will define new loops, where as data starts moving from static to interactive, we'll start harnessing tacit expertise, which gives us a handle on the lived experience that drives mental models that allow us to reason about not just how experts act, but why experts act. Intents from these mental models then drive the world models that do not now work with just aggregated preferences, but have traceable contributions. The attribution mechanisms that we have now will allow for trusted adoption, which then leads to continuous participation of humans in the AI loop. So how do we build these mental models? Well, we have the execution in the discovery pipelines that we talked about.

**[8:11](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=491s)** All traces from these discovery pipelines are then ingested, and with the claim-back verification methods that we have, we can convert them into evidences. These evidences are distilled into beliefs, and the usage of each belief by the system is something that comes with an attribution. This is something that can be used for coding tasks where we can solve more tasks better. Importantly, we can also have less user interventions, less tokens being consumed, which essentially points to better user and system alignment. This is something that can also be used for physical tasks like Gaussian splatting, et cetera that we are talking about, where we can get mental models to adopt different personas, for example, a quality and a speed persona. And these are things that come out of the discovery loop, and we can have a controllable steering of these mechanisms. So to summarize, we have talked about execution loops that

**[9:02](https://www.youtube.com/watch?v=0Pvt-chYQsA&t=542s)** are built on data simulation and DevOps, these are the verifiable substrates on top of which discovery loops can happen, which have grounded ideation, verification, and traceability, and finally, human participation through intent loops that work with tacit expertise, mental models, trusted attribution, and eventually co-evolving partnerships. Thank you, everyone.
