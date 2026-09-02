---
id: b8vjG0bK46g
title: "Trevor Darrell - Real World Reasoning Agents"
slug: trevor-darrell-real-world-reasoning-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Trevor Darrell"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T01:35:36Z
video_id: b8vjG0bK46g
url: https://www.youtube.com/watch?v=b8vjG0bK46g
youtube_url: https://www.youtube.com/watch?v=b8vjG0bK46g
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Trevor Darrell - Real World Reasoning Agents

**Trevor Darrell**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=b8vjG0bK46g) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,600 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=b8vjG0bK46g&t=1s)** TREVOR DARRELL: And I'm going to tell you today about recent work at UC Berkeley on real-world reasoning agents and, in particular, agents that can see, feel, and reason about the physical world. We already have agents that can see, but they actually don't always see that well. If you look at the visual encoders in today's VLMs and agentic VLMs, they're well designed for internet vision tasks, but they're not always that well designed for physical AI tasks or even precise internet vision tasks. You can take an image, put it in a visual encoder, run it through an LLM, and get a nice caption. You get another image, run it through the same architecture, and maybe get the same caption. You probably didn't realize those two images were actually

**[0:51](https://www.youtube.com/watch?v=b8vjG0bK46g&t=51s)** different, but you got the same caption out of these encoders. I mean, do you realize these are different images? It's actually hard to see. And you probably have to look back-- and there's some small details there. And you probably have to look back and forth between the images to actually notice the difference. And that's exactly what we don't allow most visual encoder architectures and VLMs or agentic AI systems to do. So let's do it. That's what we did. So we engineered a new representation we call a stateful visual encoder that's specifically designed to look for small differences or what we call state changes in the world, specifically in images here. But it could generalize to other signals as well. So here's a basic visual encoder diagram.

**[1:44](https://www.youtube.com/watch?v=b8vjG0bK46g&t=104s)** Take an image, encode it, or rush it through-- push it through a number of layers to encode it and put it into LLM. We make a very simple modification, so simple you'd be surprised that it's novel of allowing cross-image weights in the middle layers of the encoder to specifically be tuned to detect changes that are too small to normally be encoded in the representation. And with that, you actually can have a change in coder give you a very detailed caption, mention what's changed, or if you need to see whether a little box has been checked or not in a web interface. It's much, much easier to do this without tremendous brute force attack. How do you build this general idea?

**[2:32](https://www.youtube.com/watch?v=b8vjG0bK46g&t=152s)** There are a lot of different approaches. We compare them all in the paper. I won't go into details. And I'll refer you to the paper. It has significant improvement in a variety of real-world tasks like medical image report generation or image editing control or geospatial image change detection. And we have lots of result tables, as you would expect in our wonderful project page and paper. Please check it out if you're interested in that stateful visual encoders. So that's the seeing. I want to explain the broadness of the interest here. We go from seeing manipulation, touching, and eventually reasoning. We want to manipulate things in the real world the way

**[3:22](https://www.youtube.com/watch?v=b8vjG0bK46g&t=202s)** people can. Huge challenge of physical AI right now. Robots generally can't do these things. We want to be able to screw a light bulb in and have it turn on. And I'll show you our work on this that's called T-Rex. This is in collaboration with colleagues at NVIDIA. Current foundation models are amazing. They can reason. They can plan. They can act. But they're still not so good at reacting. And tactile is still the under-- I think underappreciated modality. Certainly, a lot of real roboticists know this, but a lot of the AI roboticists think, oh, you can scale your way out of it without actually understanding dynamic forces in the real world. I'm not sure that's right. Human intelligence is dual process.

**[4:10](https://www.youtube.com/watch?v=b8vjG0bK46g&t=250s)** And we really need agentic systems that are dual or triple process. We need this idea of a slow-fast architecture. And so we've embodied all of these ideas in our approach we call T-Rex, both a data set, data collection, and an architecture that has multi-process dual-process architectures. Has tactile sensing and reactivity. And it can learn both how to feel in the dexterous manipulation sensor and, for example, a sharper hand, which is what we use when to change the forces based on what it feels, when to adjust the slip to catch something that's about to slip, or put just enough pressure on to peel a card off of a deck. This is our platform. And here's an example of our performance.

**[5:00](https://www.youtube.com/watch?v=b8vjG0bK46g&t=300s)** So you can see we have two sharper hands. We have cameras mounted on the head and the wrists. And you can see the readout of the tactile sensors in the lower right tile. And we can do tasks that previously were impossible for previous approaches that didn't have tactile reactive policies, for example, squeezing a toothpaste out of a toothpaste tube. We did not actually yet ask the robot to brush its teeth. Maybe next time. Here it has to feel to separate the two cups out of a stack. Here, it's actually feeling the tile to actually recognize which of the three types of tiles it is, just by the feeling of the indentations

**[5:50](https://www.youtube.com/watch?v=b8vjG0bK46g&t=350s)** on the tile in mahjong. And here, it's able to grab a key and insert it into a lock and twist the lock. I think this is a little bit overnamed. It's really just pipette manipulation with liquid. And our T-Rex model can squeeze the bulb to push just the right amount of liquid out of it. Here, we can extract a card out of a deck. And I think finally, we get-- screwing a light bulb in, I think, is the final example. And it knows how to put enough pressure on it to not crack the light bulb. And those eggs that I mentioned earlier were all real eggs. They were not hard-boiled eggs. So if you're interested in this, I

**[6:39](https://www.youtube.com/watch?v=b8vjG0bK46g&t=399s)** encourage you to look at our web page and paper and, importantly, our data set, which may be one of the most important artifacts of this project, Berkeley project with strong collaborators from NVIDIA. Last but not least, I want to talk about world motion models. How do we now reason in 3D in a very abstract way? We all know how to predict the 4D future. We can look at the world, look out at a car, see maybe key features on the car's wheel. And we can imagine how those are going to move in time. And now, we can build and we've seen earlier today amazing world models that are generating live video pixels of-- predict every pixel in the future going forward. It's wonderful. But if I just want to maybe adjust something on that wheel

**[7:28](https://www.youtube.com/watch?v=b8vjG0bK46g&t=448s)** as it goes by or tighten a bolt on the wheel like an F1 pit crew, I don't need to predict what the trees are doing. I don't even need to predict what much of the car is doing. I want to predict the affordance or the geometry or how that wheel is moving over time-- what was, what is, and what will be across time. So this is our latest work on world motion models, where we build a motion model of dynamic 3D world trajectories. It's actually a world motion model over SE(3) trajectories. It's poses, for those of you who are geometry literate. And so much of the physical world can be abstracted as the motion of rigid frames evolving. And ours is the first very general framework for predicting and completing and eventually

**[8:19](https://www.youtube.com/watch?v=b8vjG0bK46g&t=499s)** doing things like MPC over this representation. So we have a general model where we've tokenized the six degree of freedom posed frame and have it stacked over time with multiple different reference frames, one corresponding to all the different objects or rigid portions of a body in the scene. So this is a world model over SE(3) poses. We call it a World Motion Model. Other than that, it's very general. And in many ways, the same as a pixel-- as a world model that generates pixels, we train it by denoising sequences. And we can run inference either to predict the future given the past; to predict the future conditioned on actions given the past; to inpaint or motion plan;

**[9:12](https://www.youtube.com/watch?v=b8vjG0bK46g&t=552s)** or to retarget, solve for dynamics, et cetera, et cetera. And we have a very efficient neural network architecture-- sorry, transformer-based architecture that does this. I'm just going to show you in my one minute left some demos, where all of these are being modeled by our World Motion Model. And you can, given text, cause the robot to learn motion trajectories to solve a certain task, either directly or using something like Motion predictive control to solve the motion. Here's examples with the Omomo data set, where we have human-object interaction. And we need to generate the motion of a humanoid in order to perform a manipulation task on an object in the world. Our model outperforms baselines on that.

**[10:00](https://www.youtube.com/watch?v=b8vjG0bK46g&t=600s)** And similarly, interacting with the world with objects and hands. So you've seen quite a diversity of different projects. This is World Motion Models. It'll be on arXiv soon. Keep your eye out for that. And I only showed you a few of the applications. Others are hinted on the bottom of the slide. Very general model. Very cool. That's all I wanted to cover today. Give you a teaser on three great projects at Bayer that see, feel, and reason in motion about the real world. Thank you. [APPLAUSE]
