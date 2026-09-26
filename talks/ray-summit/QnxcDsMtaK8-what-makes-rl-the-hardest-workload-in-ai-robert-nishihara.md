---
id: QnxcDsMtaK8
title: "What Makes RL the Hardest Workload in AI | Robert Nishihara (Anyscale) | Ray Summit 2026"
slug: what-makes-rl-the-hardest-workload-in-ai-robert-nishihara
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["Robert Nishihara"]
channel: "Anyscale"
duration_min: 9
published_at: 2026-09-17T16:01:47Z
video_id: QnxcDsMtaK8
url: https://www.youtube.com/watch?v=QnxcDsMtaK8
youtube_url: https://www.youtube.com/watch?v=QnxcDsMtaK8
tags: []
topics: ["Training, fine-tuning & model building"]
transcript: true
---

# What Makes RL the Hardest Workload in AI | Robert Nishihara (Anyscale) | Ray Summit 2026

**Robert Nishihara**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=QnxcDsMtaK8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Reinforcement learning is one of the hardest distributed systems problems in AI: training, inference, and environments all running in one loop.

Robert Nishihara, creator of Ray and co-founder of Anyscale, breaks down the anatomy of a reinforcement learning workload on the Ray Summit 2026 Day 1 keynote stage: the components an RL system has to coordinate, why the combination of large-scale training and large-scale inference in a single loop stresses infrastructure in ways neither does alone, and how Ray was built for exactly this shape of problem.

Liked this video? Check out other Ray Summit keynote sessions: https://www.youtube.com/playlist?list=PLYnBpswCtPo4

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,365 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=1s)** Every workload in this diagram is powered by massive amounts of compute. But GPU compute alone is not enough. To turn raw compute, raw GPUs into a working learning loop requires a platform. And as the complexity of the hardware has grown and as the importance of the learning loop has grown, this platform has become essential. The platform needs to solve two broad buckets of of problems. The first is what I'd call workload challenges. Think about everything that one user needs to run one workload on one cluster. This is about how do I scale my data processing pipeline to petabytes of video data?

**[0:49](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=49s)** Right? How do I take my training job and make sure it's fault tolerant and it recovers really quick quickly from failures? How do I maximize throughput for my inference pipeline or inference deployment? These are the types of challenges you have to solve to run a single workload. And then there's everything around the workload, all the problems that arise when you have many users, many um many workloads, many clusters. These are the platform challenges that also need to be solved. So we're going to cover both of these and I'm going to start with the workload challenges. And to illustrate this, I'm going to describe the software stack that makes up an individual AI workload. So in the software layers, the most familiar is the training and inference

**[1:36](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=96s)** engine. Think PyTorch, JAX, a VLLM. This layer is responsible for running the model efficiently on the GPU, right? Squeezing the most performance out of the underlying hardware. Under that, you have the distributed compute layer. This layer is responsible for solving the distributed systems challenges of scaling. Think about process lifecycle management, process placement, um coordination, resource management, failure handling, data ingest, and data movement. These are the types of challenges solved here. And that's where Ray sits. Now, these two layers together are sufficient. You can use them to build and scale any of the workload, any AI workload. But we've increasingly been seeing a third layer of higher level workload

**[2:25](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=145s)** frameworks emerging on top building on top of the lower layers. And these include all of the RL frameworks. Think about Veral, Nemo RL, Sky RL, Slime, Miles. It includes data frameworks, inference frameworks. And together, these different layers form uh the software stack for running one individual AI workload. Now, if you're wondering, where's Kubernetes? That will come soon. Once we get to the broader platform challenges around the workload. Right now, we're just talking about a single workload. So, to try to bring this picture to life, I'm going to walk through a concrete example. Okay? I'm going to choose a specific workload, and I'm going to focus on reinforcement learning. Because so much of the progress in AI

**[3:13](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=193s)** recently is due to reinforcement learning, and a larger and larger fraction of compute is going to reinforcement learning. So, I'm going to walk through um the anatomy of a reinforcement learning workload, talk about what it takes to run and scale it, and why it's actually hard from a distributed systems perspective. So, there broadly there are two different parts to reinforcement learning. There's training, just training the model, and data generation, which is using the model to generate new data to then update the model. And to break it down a little more, the way data is generated is through an agent coordinating uh closely with an environments, a reward model, and inference server. And these processes actually, these groups of processes operate in in in

**[4:01](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=241s)** very tight coordination. So, the inference server will generate an action, which will be sent to the environment. The environment will execute the action and create a new state of the world, which will be sent back to the inference server, and they work in a tight loop. And that and data rollout data is generated that way. And then when the rollout data is generated, it can be scored by a reward model. And then shipped back to training to actually to train the model. And so, let's talk a little bit about this flow of data. So, if you look at the training side, suppose I have two data parallel replicas, two FSDP replicas. Now, as I'm shipping the rollout data from the data generation component to the training component, it may seem like a simple point-to-point transfer. I send the data, batch it together, feed it into training.

**[4:49](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=289s)** But remember, rollouts are sequences, they have different lengths. And so, when you batch them together, you can end up with a lot of padding, and that can decrease training efficiency. And so, even this little step of moving data from point A to point B actually requires some global coordination to intelligently pack the rollouts together into batches and shuffle them around to minimize padding. So, it looks a little bit more like this. Right? Now, let's look in the other direction. I'm trying to describe some of the distributed systems challenges that arise when scaling reinforcement learning. So, looking in the other direction, I've now updated my model, I want to ship the weights back to the inference server to then use it to generate new data.

**[5:35](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=335s)** Again, it looks like a simple point-to-point movement of data, but training engines and inference engines shard the weights differently. So, they're actually the the weights need to be re-sharded as they're moved. And not only that, when they arrive at the inference component, inference itself is not just one thing. Often inference can be decomposed into a pre-fill stage which handles processes input tokens and is more compute bound and a decode stage which generates output tokens and is more memory bandwidth bound. And interestingly, to get good performance now, each of these you have two different groups of processes each with their own compute resources, each with their own hardware requirements. To get good performance, you actually need to tune the ratio of pre-fill workers to

**[6:23](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=383s)** decode workers. And how do you do that? The appropriate ratio there depends on the sequence length characteristics of your query. So how like input tokens versus output tokens. And that kind of makes sense because pre-fill handles the input tokens and and decode generates output tokens. And so you end up tuning these different the ratios of these different process groups. But when you're doing RL training, you're often training on a mixture of different problem domains. And each problem domain may have different sequence length characteristics. And so to really get the best performance, you may actually want multiple inference deployments each tuned to a different profile of sequence length characteristics. Right? And of course, if you have multiple inference

**[7:10](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=430s)** deployments, that complicates your weight sync, right? That complicates your routing strategies. That complicates your failure handling. Okay. So, we just What did we just illustrate? We just talked about some of the major components and movement of data between different processes in an RL workload. And we mostly described the distributed systems challenges that arise from coordination across different components. There's actually a large set of challenges we didn't touch on at all, which is managing the complexity within each individual component. And we didn't talk about it, but each individual component has its own failure handling strategies, and its own hardware requirements, its own topology requirements. Training will run on, you know, reserved GB300s, where you have to

**[7:58](https://www.youtube.com/watch?v=QnxcDsMtaK8&t=478s)** reason about rack topology. Uh environments will run in on sandboxes on hundreds of thousands of CPU cores. Um the the reward model may be bursty and require more elasticity. The agent can be IO-bound and really needs to be heavily multi-threaded. So, there's each component has its own unique set of challenges and uh tricks to make it scale. So, all of this complexity, some of which we talked about, but a lot of which we didn't, is why we need this type of picture. This the value of this software stack. It's the reason that nearly every RL framework uses this stack, builds on Ray, to manage the complexity of running one single workload.
