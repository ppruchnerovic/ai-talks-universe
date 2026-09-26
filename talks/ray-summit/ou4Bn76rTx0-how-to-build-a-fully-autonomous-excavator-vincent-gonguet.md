---
id: ou4Bn76rTx0
title: "How to Build a Fully Autonomous Excavator | Vincent Gonguet (Bedrock Robotics) | Ray Summit 2026"
slug: how-to-build-a-fully-autonomous-excavator-vincent-gonguet
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["Vincent Gonguet"]
channel: "Anyscale"
duration_min: 15
published_at: 2026-09-17T16:01:51Z
video_id: ou4Bn76rTx0
url: https://www.youtube.com/watch?v=ou4Bn76rTx0
youtube_url: https://www.youtube.com/watch?v=ou4Bn76rTx0
tags: []
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# How to Build a Fully Autonomous Excavator | Vincent Gonguet (Bedrock Robotics) | Ray Summit 2026

**Vincent Gonguet**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=ou4Bn76rTx0) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

"Bedrock Robotics just deployed the first fully autonomous excavators on commercial construction sites for paying customers. No one in the cab, an end-to-end machine learning model running on board, doing real work for hours.

Vincent Gonguet leads technical foundations at Bedrock Robotics. Before Bedrock, he led Llama safety at Meta Superintelligence Labs and product groups that expanded internet access for over 300 million people. In this talk, he covers why construction is the strategic bottleneck autonomy should solve, how Bedrock retrofits its partners' existing machines, and three ways Ray powers the stack: heterogeneous CPU and GPU pipelines, mining ambiguous multimodal field data from over 50 machines, and a closed-loop simulator that models everything down to soil deformation.

Liked this video? Check out other Ray Summit keynote sessions: https://www.youtube.com/playlist?list=PLYnBpswCtPo4

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,193 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=0s)** Good morning everyone. It's great to be here at the race summit today. At Bedrock our goal is to bring advanced autonomy to the built world to heavy machines starting with construction. And as you'll see as you'll see today many parts of our technical stack rely on Ray and so we're very grateful for the community building in the open. Always leads to better technology. And so today I wanted to give you a sense of what we're building why and also touch on three key applications of of Ray across our development pipeline. There's also you know the nice thing with robotics is you the best way to show it is with videos. So hopefully we'll have a lot of like nice videos and

**[0:46](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=46s)** content to keep to keep the audience entertained. But first an update on our progress. Last week Bedrock Robotics deployed the first fully autonomous set of excavators on three commercial construction sites for paying customers. What does it mean? No one's in the cab of the machine. The machine operates reliably for hours productively and safely. Our system understands the terrain and the plan and completes tasks entirely on its own. This isn't just a demo or simple automation. This is an end-to-end machine learning model running on board performing real work today.

**[1:35](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=95s)** But why are we doing this? We're developing this autonomy because the world needs to build and needs to build fast. We're living through a time of unprecedented demand for infrastructure. The speed and scale of these projects is just enormous. And there's a year-long backlog for contractors big enough to tackle this type of work. And the whole physical backbone of our economy from manufacturing to ports to power grids to data centers depends on the construction industry's output. And it's become a big strategic bottleneck for our country and for the world. At the same time, productivity in construction has fallen

**[2:23](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=143s)** year-over-year since 1965. This is not for the lack of inventivity and hard work of this industry. It is just hard work, complex work. Uh and at the same time, you we've seen other industries see sharp increases in what they could accomplish with technology and software. The labor shortages also only getting worse. 92% of contractors say it's next to impossible to find the skilled workers that they need. And some of our partners expect more than half of their workforce to retire in the next 5 years. So that's what we're focused on. Designing solutions to alleviate our capacity issues. And we want to do it in the simplest way

**[3:11](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=191s)** possible. So we outfit our partners' existing machines, saving both us and them the cost of new equipment. Those machines are incredibly amazing pieces of technology and incredibly complex. Um and the install happens right on the job site. Uh it's hard to move those machines around. Uh in just a few hours, fully reversible, and the machine can still be operated by humans as needed. So let's talk a little bit more about how we do it. Um so this is the set of sensors uh that we put on the machine to bring autonomy from set of cameras uh a mount that can adapt to different machine sizes and machine types, uh lidar uh to be able to see the terrain,

**[3:58](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=238s)** um and then a set of sensors uh to be able to locate machine and have kind of the precision work, um and state-of-the-art compute uh that we can put inside the machine uh so that we can run those models on board with with low latency. And so, as you can see, and we'll talk more about this and the relevance to Ray, every single log that we have to deal with is intrinsically multimodal. It includes video, multiple streams of video, uh lidar, all kinds of sensors and telemetry. All of those operate at different frequencies, which we need to process extremely efficiently to do our work. The other thing is that construction is

**[4:49](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=289s)** not something you can script. It is some of the most dynamic, high-entropy work that you can imagine. And so, to build, we're building with expert crews um that we help multiply uh and provide kind of increases in productivity. Learning to be a an operator on those machines is not something you learn in a textbook over 30 hours and get a driving license. This takes years, thousands of hours. And it's a real craft. Um and so, this is not something you can learn in a scripted way, and as a result, we have to think about collecting data in situ, in context of those sites that are highly dynamic.

**[5:38](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=338s)** The craft of doing construction can also vary significantly region to region based on things like soil, local techniques, job site setups. A few weeks ago we learned about the Texas way of digging. Those are real things. Um And so we have today over 50 machines out in the wild and we're gathering one of the largest repositories of operator know-how from different environments, site conditions, and scopes of work. We'll see that a little bit more later. Um and so these machines are running every day and just incredible to see the variety of tasks happening on those sites. So three applications of Ray uh at Bedrock. First

**[6:26](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=386s)** and you'll see that in a bit more details, every stage of our development pipeline is some combination of CPU and GPU. Highly heterogeneous. Second, the data we're collecting because of this complex craft uh is highly ambiguous and needs complex processing before we can use it downstream for all the different types of applications. And third our simulator is the ultimate full-stack complex workload. Obviously it needs to run autonomy so that we can test it and improve it. But it's also simulating the world around the machine computing all the different metrics on the variety of tasks and scenarios at

**[7:13](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=433s)** scale. So let's dig into each one of those to give you a better sense of of how we're using this type of technology. So this is a a high-level uh view of our physical AI development pipeline. Uh we go from data collection to mining and labeling and preprocessing training and then simulation and eval. As you can see, none of those stages is uh homogeneous load, just like a set of uh GPUs or GPUs easy to coordinate. Um, and so that is one of the big value adds of something like Ray. Um, also we need to think about scheduling all those different tasks. Uh, we need to be able to scale them

**[8:01](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=481s)** efficiently. And obviously we care about cost and thinking about how to best distribute the workload across the different um, sets of uh, infrastructure providers. So I talked about the data starting in big. So what does it mean? For many robotics companies, the way they collect data is in kind of data factories. Um, having folks with headsets, you know, collect, you know, like folding shirts and moving things around, making coffee, you name it, like any type of task. Construction doesn't work like that. Um, it varies based on unforeseen conditions. It's a high context type of work.

**[8:48](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=528s)** And so just to process the data that we get, we have this complex data understanding problem that we have to solve. It means reverse engineering from what you're looking at, what was the task? What was the domain? What were the objects? What was the goal? And so to do that work, we need a set of well-coordinated and um, and optimized workflows uh, that use traditional classifiers, vision models, VLMs, agentic loops, embeddings, and more. And so let's take a quick look. So based on the earlier videos, you might think that construction is kind of boring, but it's actually problem-solving at scale. It's manipulation in the case of an excavator with a giant 100,000 lb arm.

**[9:39](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=579s)** Those are a few cool examples that we mined from our data set um from you know, building a a road to float on top of muddy soil. Those machines can get stuck and have to kind of climb out of the of the mud. Uh you can see jackhammering rocks. Like did you know that excavators can change tools and they have this wide variety of tools? Um you can use the the arm like a crane to lower pipes into a trench and it doesn't stop there. We've seen people picking up logs and even emptying puddles uh to after kind of a big rain. And so how do we deal with this complexity? Well, we build simulation. A complex closed-loop simulator. And so at Bedrock,

**[10:26](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=626s)** simulation sits between every code change and every machine. Uh let's walk a little bit through the different types of loops that we have leveraging simulation. So, first kind of the the developer loop. So, let's say you have a new improvement to the autonomy stack and code or a new model checkpoint. You want to see okay, like is it is that feature going to improve or regress? So, you run simulation on set of well-picked scenarios that you know, are targeted to the piece of the stack that you're trying to improve. Then every day we integrate all the different features and improvements and model checkpoints from our team and run that through a battery of tests, large-scale sets of simulations and diverse scenarios so that we can compute metrics and catch regressions before the

**[11:14](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=674s)** model makes it into the field. And once the teams feel close to a release candidate, we run an even wider set of simulation across all the types of tasks that we want to run, all the adversarial edge cases, um and then compute, you know, our safety, productivity, and reliability. This never fully replaces real-world testing. It is vital. It is the ultimate uh integration test for all those things. But simulation is the way to scale. It's the way to accelerate our development velocity. So, it's the way to make sure that we improve in the right directions. Um and so, we validate with simulation in the loop, which requires a high-fidelity terrain and

**[12:03](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=723s)** physics simulation, a sensor simulator reproducing all the same camera, lidar, telemetry mix that you've seen, you know, happening on the machine, um and having all those different types of behavior policies and goals being tested. This is what it looks like. I just a few examples of what it means to scale up in in sim. You can see different terrain conditions that we kind of want to start in in different areas, different goals for the machine, maybe different type of depth or, you know, different trucks that you're going to interact with, or different types of weather, different types of light. One thing you can notice on the video is that one of the unique problems that we have to solve is that our robots are changing their environment.

**[12:52](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=772s)** Um this is a pretty rare case in simulation. And so, we need to simulate all the soil deformation. Soil is a complex fluid. You have dozens of parameters you can tweak to try to match reality. So, this is a use case that you can only scale in sim. And we're obviously just getting started in the diversity of tasks and scenarios that we want to run. So, simulation needs to scale. You can see a little bit on the right, um the anatomy of of a of a sim run, um, so we have a kind of this rate task that is kind of monitoring two big pieces, running the full autonomy stack, as well as simulating the world and the sensors around the machine.

**[13:41](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=821s)** Uh, that get then that also gets distributed to the right workload, uh, so that it can run on time, uh, you know, at an optimized cost every day. And then logs all the information, all those videos that we can then post process and run metrics on. And so all of that is Ray again, enabling us to schedule well, those heterogenous heterogenous jobs, and and scaling an entire fleet of of tests, um, as efficiently as possible. So to wrap up, we talked about three key applications of Ray at Bedrock. Those complex workloads at every stage of pipeline, a complex data understanding problem to prepare our data, and a simulator that needs to run

**[14:29](https://www.youtube.com/watch?v=ou4Bn76rTx0&t=869s)** everything and simulate the world at scale. So what's next? Maybe you guessed it. Well, more machines. Orchestrating machines, machines working together with new types of tasks, data and sensors. So you can imagine how then you need to simulate different models running in parallel, interacting together, interacting with crews on the site. So that is what keeps us excited about the technology, and we're excited to work with the Ray community to be able to get to the next level of complexity. Thanks again for the whole community here. Uh, and if you want to help us build this, please get in touch.
