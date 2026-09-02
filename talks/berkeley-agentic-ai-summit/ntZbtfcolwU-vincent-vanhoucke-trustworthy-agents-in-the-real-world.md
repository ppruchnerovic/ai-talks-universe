---
id: ntZbtfcolwU
title: "Vincent Vanhoucke - Trustworthy Agents in the Real World: Physical Autonomy Lessons for..."
slug: vincent-vanhoucke-trustworthy-agents-in-the-real-world
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Vincent Vanhoucke"]
channel: "Berkeley RDI"
duration_min: 14
published_at: 2026-08-12T01:34:13Z
video_id: ntZbtfcolwU
url: https://www.youtube.com/watch?v=ntZbtfcolwU
youtube_url: https://www.youtube.com/watch?v=ntZbtfcolwU
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation"]
transcript: true
---

# Vincent Vanhoucke - Trustworthy Agents in the Real World: Physical Autonomy Lessons for...

**Vincent Vanhoucke**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=ntZbtfcolwU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*2,106 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=ntZbtfcolwU&t=1s)** VINCENT VANHOUCKE: Thanks for having me. I hope that for this crowd, I don't need to introduce Waymo. But if you don't know, Waymo is an agentic AI company because, of course, our agents are big, beautiful hunks of metals that have four wheels and are driving around in your neighborhood. We have by now thousands of agents operating in the real world, doing very long-horizon tasks to completion, and serving real customers, paid customers completely autonomously. We're right now in 11 cities, but we have ambitions to expand to many cities in the US and abroad as well. So our goal really is to provide autonomy at scale

**[0:55](https://www.youtube.com/watch?v=ntZbtfcolwU&t=55s)** and to become the world's most trusted driver. I like to always show this notion of trust as a central feature of the Waymo story because it's not just about safety, it's about consistency. It's about repeatability. It's about predictability. A lot of the same features that are factors in the trust that we place in agentic agents, in general. If you're already tired of my joking around about the parallels between autonomous driving and agentic AI, I'm sorry, I'm just getting started. There is actually a lot of parallels to be made between physical AI on one end and agentic AI on the other hand.

**[1:42](https://www.youtube.com/watch?v=ntZbtfcolwU&t=102s)** If I talk to my roboticist friends, and they look at what's happening in the world of agentic AI today, they really look at it with a smile, because all of the hard problems that we've been experiencing in the past 20 years in robotics are exemplified in agentic AI. It's really about how do you build a system that has enough affordances to do things that are interesting in the real world but that also you can trust, and that can evolve in the real world, doing real tasks safely and with a good stability and consistency. And all of those problems were first really exemplified in the physical AI world and are now

**[2:30](https://www.youtube.com/watch?v=ntZbtfcolwU&t=150s)** hitting the agentic AI world. So I want to take a few lenses to look at agentic AI from the perspective of somebody who's been looking at physical AI for a while. And one lens we can take is the lens of industrial automation. So industrial automation is traditionally the art and engineering behind taking a whole bunch of components that mostly do their work but will occasionally fail, and stringing them together, like on an assembly line, for example, and harness them to provide very high levels of reliability, safety, autonomy over very long time horizons and at scale. There are lots of lessons that we

**[3:20](https://www.youtube.com/watch?v=ntZbtfcolwU&t=200s)** can draw from industrial automation for agentic AI. I'm just going to pick one. One of the lessons that I've seen in this space is that it's all a game of nines. At a certain scale, you can get away with 99% repeatability. As soon as you scale up, you need to go to 99.9 or 99.999, and so on and so forth. Every nine typically means you need a different solution. Every 9 that you earn is not earned by just improving your system a little bit, getting a better model, or reducing the error rate, you have to redesign your system for the level of reliability that you want. So another angle that we can look at agentic AI from the perspective of physical AI is the angle of autonomy.

**[4:11](https://www.youtube.com/watch?v=ntZbtfcolwU&t=251s)** So in autonomous driving, we have those five levels of autonomy. You start from no automation to driver assistance systems. Waymo operates at level 4, very high automation. If you think about coding agents or AI agents, there is this same gradation of you write your code by hand all the way to you just yolo it and just let the agent write everything for you. One of the lessons from AV in that space is that level 3 is a weird beast. Level 3 is not a very pleasant place to be. It's very bad for cognitive load. It's very bad for safety. It's very bad for productivity. And we've seen this in agentic AI as well. When people started moving from code completion to agents and having this mixed scenario where sometimes the human is

**[5:03](https://www.youtube.com/watch?v=ntZbtfcolwU&t=303s)** in charge, sometimes the agent is in charge, and this interface between the two is very uncomfortable. The other thing that we've learned in the AV space is that level 2 and level 4 are very much different beasts. So very different design decisions, very different approaches. And you can't really just graduate your way from level 2 to level 4. You have to rethink your system dramatically. And we're seeing that in agentic AI as well. The code completion systems that you used to use are not exactly a simplified version of the agentic systems that you use today. Another lens that we can take is more of the dynamical systems perspective.

**[5:49](https://www.youtube.com/watch?v=ntZbtfcolwU&t=349s)** So there is a lot of work that's been going on in control theory in the robotics space, where you study essentially nonlinear dynamical systems. And agentic systems are essentially extremely nonlinear dynamical systems. So maybe a lot of the physical math that goes on there is not translatable, but the concepts and the way of thinking about it-- notions of observability, controllability, stability realizability. The last one is, can you actually do the task? All of this is actually a very relevant to the task. One of the lessons in that space has been-- and it's a lesson that has been adopted by the agentic AI world from the start--

**[6:44](https://www.youtube.com/watch?v=ntZbtfcolwU&t=404s)** is that if you want to optimize for closed-loop behavior, meaning if you want to optimize for long horizon, you need a very different reward system than if you're trying to optimize for open loop. So in the robotics space, this is something we call the dagger problem. And there are many names for that in different fields. It's the idea that if you're trying to-- if you have a system that is a multi-step system and you're trying to minimize the error at every step, you may end up in a place where you end up making very correlated errors. And at the end of the day, your system ends up in a very different place than where you want to take it. So optimizing one step at a time hasn't really worked. That's why we do long-horizon planning. That's why we do reinforcement learning. That's why we think of long-horizon tasks with a different objective functions.

**[7:32](https://www.youtube.com/watch?v=ntZbtfcolwU&t=452s)** One of the ways that we approach this problem is by optimizing one step at a time, by imagining the future, and by looking at the long horizon and dreaming up what the long horizon would look like if we took a specific action. That's where basically world models are coming into play. And so at Waymo, we've been working on world modeling to optimize our system for long-horizon planning. We have our own world model, which we've called the Waymo world model. We're very, very creative. And that enables us to do evaluation and simulation of a long-horizon behavior for our system in closed loop and with very good fidelity. So a few of the ingredients of a world model are-- well, first

**[8:23](https://www.youtube.com/watch?v=ntZbtfcolwU&t=503s)** and foremost, realism is a big part of it. The way we've approached it is we started off from a very good video generative model, Genie 3 from Google DeepMind. As you can see here, it's got some notion of physics, but it's got all the notions of physics. It can handle Minecraft physics as well as real-world physics. But we really want our role model to follow real-world physics, not just video game physics. We also want the model to handle the real-world generative visuals, not just video game visuals. So we've basically taken the model and fine-tuned and adapted it to the Waymo use cases. So in this case, you see we have all the cameras that

**[9:13](https://www.youtube.com/watch?v=ntZbtfcolwU&t=553s)** are on the Waymo car. You have the LiDAR. We've grafted a LiDAR generative capabilities onto the model as well. And we're able to-- this is a 30-second rollout of a completely imagined scene from this world model. Another important factor in world modeling is controllability. You want to be able to imagine counterfactual events. You wanted to dream up what is possible if you take any action. And so you don't necessarily want to follow exactly what has happened in the real world. For example, you want to change, instead of turning right, you want to turn left or go straight and still have the model render essentially something very high fidelity. And so we're able to generate imagine new scenarios that

**[10:04](https://www.youtube.com/watch?v=ntZbtfcolwU&t=604s)** are very realistic irrespective of the action that we take. We also want to be able to control different aspects of the scene. So through language we can say, hey, generate that scene in the morning, generate the same scene at night, change the weather conditions. You can have cloudy weather, foggy weather. Change the appearance of things, change the general conditions. We want to be able also to very finely control the scene at a very fine grain. Imagine if you move a car from one lane to the other, what would happen as a result? So in the controls, basically, we can condition the entire model on all the cars, all the pedestrians, all the lane geometry of the model.

**[10:55](https://www.youtube.com/watch?v=ntZbtfcolwU&t=655s)** And then the next stage is really about generalization. If we only are able to simulate the kind of data that we see in the real-world today, it has some usefulness. But really having a world model really shines when you're able to go and extrapolate in scenarios that you've never observed or that you potentially never want to observe. So we've never encountered an elephant on the road, but we would love to be able to simulate different animal encounters like this. One funny aspect of this is that if you do nothing and you just train the data on Waymo data, Waymo has never seen an elephant on the road. So you say, give me an elephant, the model will give you no elephant whatsoever. If you try to tweak it to improve its generalization and world knowledge capabilities,

**[11:45](https://www.youtube.com/watch?v=ntZbtfcolwU&t=705s)** it will try really hard to give you an elephant, but fail in funny ways. You have an elephant-looking truck because it knows about trucks very well. And it has some notion of an appearance of an elephant, but it can't quite square the two together. And then if you do it right, then you can actually have a full-on elephant on the road. And the model really understand the different things. And what's interesting is that our LiDAR has never seen an elephant, but it's able to generate very reasonable LiDAR renderings as well. So we can simulate scenarios like what happens if we drive through a raging fire. We have never experienced that. But this is not a completely implausible scenario. We can simulate having snow on the Golden Gate Bridge.

**[12:36](https://www.youtube.com/watch?v=ntZbtfcolwU&t=756s)** We can simulate having somebody in a costume walk by us. So this is actually a very realistic scenario. Every Halloween we will see people in costume walking around in various stages of inebriation sometimes. So we want to really, really zoom in on, hey, this thing that you see on the road here, that's actually a human being. That's a very vulnerable person. And so we want to make sure that our system recognizes that this is something to pay attention to and to drive safely around, not just the random moving blob that moves on the street. There is actually a very significant amount of safety that really derives from us understanding

**[13:24](https://www.youtube.com/watch?v=ntZbtfcolwU&t=804s)** the semantics of the scene, and we need to basically be able to validate that. I only have 15 minutes, so this is a very high level. But I really want to stress that there is some interesting connections between physical AI and agentic AI. I think physical AI is agentic AI taken to the next frontier. Lots of lessons that can be learned from robotics, from automation, from autonomy, that can be applied to non-physical agents as well. World modeling is a very interesting direction in general. I want to ask the audience that is working on virtual agents-- what is your world model? Do you have a very good high-fidelity simulation of your environment? Because that's a key to being able to do long-horizon planning and building some resilience and long-range autonomy

**[14:20](https://www.youtube.com/watch?v=ntZbtfcolwU&t=860s)** into your system. With that, thank you. [APPLAUSE]
