---
id: vV-LOpWHgVg
title: "Saurabh Tiwary - From Models to Agents to Discovery: Building the Full Stack of Agentic AI"
slug: saurabh-tiwary-from-models-to-agents-to-discovery-building
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Saurabh Tiwary"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-09T18:44:45Z
video_id: vV-LOpWHgVg
youtube_url: https://www.youtube.com/watch?v=vV-LOpWHgVg
tags: []
transcript: true
---

# Saurabh Tiwary - From Models to Agents to Discovery: Building the Full Stack of Agentic AI

**Saurabh Tiwary**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=vV-LOpWHgVg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,644 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=2s)** SAURABH TIWARY: Thank you. [APPLAUSE] So it is very good to be here. I used to study here at Berkeley. So good to be back. I'm going to talk about the evolution of AI from models to agents to discovery and the related infrastructure implications that it has. So obviously, almost everyone is familiar with the huge expanse or adoption of AI from Singleton chatbots about three or four years back to now, almost semi-autonomous or autonomous agents. The numbers at the bottom show you some reflection of the scale of adoption and the impact that it has had. So Kaggle has this five days of agents course, and last fall when they ran it, it's an online course. 1.5 million users registered for it.

**[0:54](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=54s)** If you look at the cost of agent task, it is 10 to 100x more expensive in terms of inference compute, which is needed, compared to non-genetic workload. So adoption is increasing, as well as the complexity of compute per interaction is also increasing. And what it is leading to is from a Google perspective, we process 3.2 quadrillion tokens every month. Now quadrillion is a very large number with lots of zeros in it. The way to think about it is 1 quadrillion is one novel per person on this Earth. So in a way, Google generated tokens, which are equivalent to three novels for every person in this world. So the scale is just massive.

**[1:42](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=102s)** And so how do we build for this new opportunity, which is coming up? And this needs different pieces in the stack. So I will-- if you start from the bottom, we have the AI Hypercomputer which includes GPUs and TPUs. On top of that, we have world class research and frontier models. Then we need data for these models or agents to do meaningful things. As these agents are starting to do meaningful things, there is a huge opportunity or risk as well for security and defense. So we need agentic security and agentic defense. On top of that, we need a platform so that people can reuse all these capabilities in a cheap, efficient, and effective manner. And that's where the platform piece comes in. And then finally, we have final end-to-end agentic task

**[2:31](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=151s)** force, which can actually do things for you. Now, a co-optimization across this entire stack is really needed to extract maximum value from AI. And in the interest of time, I won't go through all of them, but I will quickly give you a snapshot on some of these layers as we go along. So Google has had a huge investment into TPU-- 10 plus years of investment. Some of the innovations relating to liquid cooling and shared memory have been there. The latest generation of TPUs is TPU, V8 and it has-- it comes in-- this is the first time we are splitting the main line as Peter was saying in the previous talk, that there is one version which is 8t, which is for training and 8i, which is for which is for inference.

**[3:19](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=199s)** In terms of just to give you a comparative number of how the improvements on TPUs are happening, the table over here is comparing the current generation TPUs, the V8s with the previous generation, which was just released a year back last year. And these are the main workhorse today, which is the Ironwood TPU. And you can see, for example, on the table on the left-hand side, you can see that the number of FP4 exaflops available in a pod is 121 exaflop. That's a massive, massive number of amount of compute per second that we are offering, and the jump is about 3x from just the previous generation. Similarly, on the memory bandwidth side, you can see significant jumps like 2x and 4x between one generation to the next. On the training and sorry on the inference, you can see on the right-hand side. Because the inference needs are increasing very, very rapidly.

**[4:09](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=249s)** A single pod can offer 11.6 exaflops and it's a 10x jump from the previous generation. And similarly, significant jumps on the memory side. So what do we do with all these TPUs? Google obviously invests. And there are now a lot of other companies who also leverage TPUs for their model. Google is training the Gemini family of models, which comes with pro flash and flashlight. The image and video generation models like Veo and Imagine, they are trained as well. The world model, which is a new and completely exciting space for us with the genie model, is also trained over there. The AlphaFold, which is a protein folding, it predicts protein folding structures as well as AlphaGo and AlphaChip, which is used to train and build the next generation of TPUs as well. These are all being so effectively

**[5:00](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=300s)** TPUs designing for TPUs in some sense. So all of these are heavily leveraging our TPU infrastructure, both for the training as well as on the inference side. Now, once we have the hardware and the models, then we need a platform through which people can build agents relatively easily. And building agents is not just like writing a prompt, et cetera. There are lots of complexities in it. And so there are four key problems. One of them is building it. So we have capabilities like access to all different types of models, agent development kit, and AI Studio to build agents. Then you need to scale them, govern them, and optimize them. So start with building, scaling, governing, and optimizing. On the scale side, they are capabilities or a Managed Runtime so that you can scale from a single instance

**[5:50](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=350s)** of that agent to millions of agents. Governance becomes a really key or important factor because as these agents are starting to do meaningful things, you want things like agent identity, agent registry, and agent gateway to make sure that the agents are working within the right confines, the identity systems that they are using are separate from the user because they can do things beyond what the user is able to do. And finally, once you deploy an agent into production, you want to optimize them. So things like training, simulation, evaluation, observability, all these capabilities need to be there so that you can keep on improving the agents once you land into production. So these become key pieces. Now one additional thing that we do is across this stack, Google itself builds on top of it. So there are agentic solution that Google is

**[6:41](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=401s)** building on top of this stack. So, for example, there are areas in biology. For example, there is AlphaFold or AlphaGenome, which is there. On mathematics side, we have AlphaEvolve and AlphaProof. On the physics and chemistry side, we have Gnome, Fusion, et cetera. And on climate and sustainability side, we have AlphaEarth as well as WeatherNext, which is a world class leading weather prediction model. And these are all built on the stack that we are talking about. Here are some examples of the impact that these final solutions are having. So, for example, AlphaFold is being used in a wide variety of applications. So in plastic pollution. So identifying or designing plastic resistant or eating enzymes for antibiotic resistance structural biology. One key area is neglected diseases.

**[7:33](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=453s)** So there are a lot of diseases out in the world where the pharma companies don't invest enough because there isn't enough economic incentive for that. And what AlphaFold is doing is lowering down the cost and the ease of exploring these drug designs, which has material impact. Then malaria vaccine, as well as drug delivery. AlphaEvolve. This is a general purpose optimizer which is there. It is used heavily inside Google for data center optimization across along with a whole host of other applications. But also it is used by other customers. So, for example, it is used for route optimization. It is used for quantum error correction, as well as by e-commerce companies for improving the forecasting demand model and has significantly.

**[8:20](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=500s)** If you think about it like these are very different types of application and has huge improvements across each one of them. So what does this all mean? As we go through this stack and as the models keep improving, what is this all leading to? And this is what we believe that where we are heading towards is this autonomous discovery loop. And the example on this particular slide is about biology. But this is much more generic. What we are having is we are having all these building blocks coming together. So, for example, for data ingestion, we now have agents which can digest large amounts of literature. There is AlphaFold has a very large protein database which is available as well as experimental logs. Then you can do hypothesis generation on top of it.

**[9:12](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=552s)** So there is AI co scientist, which can debate different hypothesis, generate novel solutions. And you can use them from a modeling perspective using AlphaGnome and AlphaFold to simulate these hypotheses and see the effects of that in seconds. And then finally, you can execute on it through AlphaEvolve and Gemini robotics to run wet lab tests and see what the data is and also feed it inside this particular loop. And so what can happen is a research cycle, which used to take years from beginning-- like input of data to outcome of the product-- can now be done in hours and days. And this is just one segment, like biology is one example. But this is going to impact almost all facets of human discovery, which is there.

**[10:02](https://www.youtube.com/watch?v=vV-LOpWHgVg&t=602s)** And this is super, super exciting phase that we have. And with this, I will end my talk. And thank you for your attention. [APPLAUSE]
