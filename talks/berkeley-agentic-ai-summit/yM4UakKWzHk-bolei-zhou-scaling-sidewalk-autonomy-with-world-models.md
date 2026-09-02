---
id: yM4UakKWzHk
title: "Bolei Zhou - Scaling Sidewalk Autonomy with World Models"
slug: bolei-zhou-scaling-sidewalk-autonomy-with-world-models
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Bolei Zhou"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-12T01:36:36Z
video_id: yM4UakKWzHk
url: https://www.youtube.com/watch?v=yM4UakKWzHk
youtube_url: https://www.youtube.com/watch?v=yM4UakKWzHk
tags: []
topics: []
transcript: true
---

# Bolei Zhou - Scaling Sidewalk Autonomy with World Models

**Bolei Zhou**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=yM4UakKWzHk) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,130 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=yM4UakKWzHk&t=2s)** BOLEI ZHOU: So we have faculties from UC Berkeley, UC San Diego. Now we have UCLA. How about having UC AI Summit? So I'm a associate professor at the UCLA, and I also work with Coco Robotics. Today, I would like to share with you how we think about scale up the sidewalk autonomy with world model. So probably, most of the people here are familiar with autonomous driving. So we have a previous speaker talk about their amazing research on the road autonomy. So I have this full-size vehicles running around the cities. But for our urban environment, there are another kind of autonomy. Here, I call it sidewalk autonomy. So here is a sidewalk robot.

**[0:49](https://www.youtube.com/watch?v=yM4UakKWzHk&t=49s)** It's doing the food delivery task. So this is a robot from Coco Robotics. So Coco Robotics is a startup running this kind of last-mile food delivery service. So we have hundreds of robots running around to fulfill this task. You can see, compared to the road side autonomy, this sidewalk robot has to handle a lot of challenging settings. Let me show you some of the videos from the first-person view of the robot. Now, you can see here this sidewalk robot have to really carefully navigate on the sidewalk and avoid the collisions of obstacles. Also, the robot has to handle all the weather conditions and the lighting conditions. Also, the sidewalk originally designed for people.

**[1:41](https://www.youtube.com/watch?v=yM4UakKWzHk&t=101s)** So the robot have to properly and socially compliant interact with dynamic agents such as pedestrians and animals like dogs. So here's another video that I like a lot. Now, you can see here is a dog just lying on the sidewalk. And then the robot have to navigate very carefully to avoid stepping on the tail of the dog and achieving the navigation task. So from those video, you can see the sidewalk conditions are very challenging. Also, the robots are working compute and battery-constrained environment. So we are only allowed to use single RGB cameras to do the navigation. So in recent years, people developed a lot of AI models

**[2:32](https://www.youtube.com/watch?v=yM4UakKWzHk&t=152s)** for the sidewalk navigations, so basically, the imitation learnings to learn from the human demonstrations. So many models have been developed. My lab has contributed some of the models. Other labs also proposed some great models. So those models are trained on the video demonstrations that it can generalize very well across different conditions. But we have a challenge here-- giving so many different AI sidewalk foundation models, how can we benchmark those navigation models before the real-world deployment? So we are building up the benchmark. So here is a benchmark we built called SidewalkBench. So we want to evaluate the navigation policies or models in simulations.

**[3:23](https://www.youtube.com/watch?v=yM4UakKWzHk&t=203s)** So here, we utilize a media Omniverse, an Isaac Sim, to build the simulation environment, so we can evaluate different models and compare their capabilities, how they interact with peoples, how they avoid collisions. But if you look closely, those graphical simulation built in this graphical engines still lacks the visual realism. So compared to the real-world deployment, there is still a sim-to-real gap. So we want to address this sim-to-real gap to more fairly evaluate the model capabilities. So our solution here is creating the world simulations from the real-world videos. So we want to use real-world videos as a source code

**[4:11](https://www.youtube.com/watch?v=yM4UakKWzHk&t=251s)** to build up this evaluation benchmark. So here is a work we developed last year published at the CVPR. It's called Vid2Sim. So we can take videos, like walking on the sidewalk, then we can build a Gaussian splat reconstructions from the videos and turn this splat into this physical engines. Then we can have this kind of data-driven simulations. Then we can train and also evaluate the sidewalk robots in this kind of data-driven simulation. So here, this demo video showing you the training process, so we can train the agent with reinforcement learning. Then, after the trainings, then the model can zero-shot transfer to real world, because there is no definitely-- no visual gap

**[5:02](https://www.youtube.com/watch?v=yM4UakKWzHk&t=302s)** between the training environment and the deployment. So based on this Gaussian synthetic environment, we can evaluate all those different sidewalk navigation policies and see how this model handle different cases. But still, there is a limitation for this kind of video reconstruction, because we can only reconstruct one environment from one videos. So ideally, we want to create several variations from the same videos. So that's a motivation behind a recent work we called UrbanVerse. So we want to create multiple digital cousins from the single video. So here, the digital twins means one video corresponds to one simulation environment. The digital cousins means we can have different variations.

**[5:53](https://www.youtube.com/watch?v=yM4UakKWzHk&t=353s)** So here, we utilize the computer vision techniques to extract the sim graph from the input videos. Then we can plug in different object instances. Then we can create a different variation of the environment. Then each environment can be used for training and evaluation. So this UrbanVerse we released to the public. And we also released a large-scale 3D assets which contains 100,000 assets with the correct skills. So for this kind of environment, then we can use the environment for evaluation. We also developed pipelines to do the post-trainings with the simulation. So basically, we train the model first on videos through imitation learning.

**[6:41](https://www.youtube.com/watch?v=yM4UakKWzHk&t=401s)** Then we can put the models inside the simulated environments and further do post-training to improve their interactivity and the counterfactual reasoning capabilities. So giving all this progress, we have this recent work we call the FlowPilot that can implement this kind of real-world sidewalk navigations from a single RGB cameras. So here, this robot only have one RGB camera. Then the model will output the waypoint. Then the controller will execute the next point. Now you can see here, this robot can handle this challenging sidewalk navigations, know how to avoid the collision with the obstacles and also how to interact

**[7:31](https://www.youtube.com/watch?v=yM4UakKWzHk&t=451s)** with pedestrians properly. Another very exciting direction is this cross-embodiment transfer or deployment. By giving this sidewalk navigation foundation model, we have the research that to transfer this model across different robot embodiments without fine-tuning. So this demo video is showing you that this model can work really well for this legged robot. We also have many ongoing research that's trying to transfer the model to many other sidewalk robots, like the wheeled-legged robot as well as this electronic wheelchairs. So in the future, not only we can autonomously deliver the food, we can also autonomously deliver

**[8:20](https://www.youtube.com/watch?v=yM4UakKWzHk&t=500s)** the people on the sidewalk. So we released a benchmark and the code at our web page, so you can access the code and papers from this barcode. So here, I would like to thank all my students and collaborators. Thank you.
