---
id: WLl8D1nyaW8
title: "The Rise of vLLM: Building an Open Source LLM Inference Engine"
slug: the-rise-of-vllm-building-an-open-source-llm-inference
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 13
published_at: 2026-01-05T19:29:43Z
video_id: WLl8D1nyaW8
url: https://www.youtube.com/watch?v=WLl8D1nyaW8
youtube_url: https://www.youtube.com/watch?v=WLl8D1nyaW8
tags: []
transcript: true
---

# The Rise of vLLM: Building an Open Source LLM Inference Engine

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=WLl8D1nyaW8) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

vLLM has quickly become one of the most widely adopted open source LLM inference engines - reaching 66k+ GitHub stars and millions of downloads in just over two years.

🔗 For a deeper look at the evolution of vLLM and its roadmap, check out Simon’s “State of vLLM 2025” talk from Ray Summit:

In this conversation, we sit down with Simon Mo, co-lead of the vLLM project, to go deep on how vLLM is built, the architectural decisions behind its inference performance, how it integrates with Ray for distributed workloads, and where the project is headed next.

Simon walks through the core problems vLLM was designed to solve, including efficient KV-cache management, high-throughput inference, and scaling across GPUs and nodes. We also discuss how vLLM fits into modern RLHF and post-training workflows, the role of open source governance, and what’s coming next across models, hardware, and the broader AI compute stack.

⏱️ Chapters & Timestamps
0:00 Overview of vLLM
01:01 Early Architectural Decisions
02:11  Why vLLM Adoption Is Accelerating
04:28 How vLLM and Ray Work Together
07:00 The State of vLLM Today
10:09 Simon Mo’s Open Source Journey
12:28 Advice for AI Builders & Contributors

## Transcript

*2,438 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=0s)** Hi, I'm Simon. I'm one of the co-lead of the VLM project which is an infras engine originated at UC Berkeley Sky Computing Lab. >> Amazing. Well, I'm so excited to chat with you today because there's so much going on with VLM. VLM in the last two and a half years had 60K stars. I think that's where it's at last I checked right now and 29 million downloads. And I can't believe it's only two and a half years. If for people listening, what is VLM and what is the painoint it solves? >> VLM is an inference engine. So what it does is to take open source large language models that you can download from hugging face or proprietary language model you have today to run it efficiently on data center hardware. So think of those like GPUs, TPUs, accelerators and the job it solves is to run those model really really well.

**[0:47](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=47s)** Yeah. >> So that you can maximally leverage their ship. you get the best tokens per second, best trooper, best latency as well as broad compatibility across the whole ecosystem. >> What is some of the architectural designs you had to make? If you could take me back a little bit. >> So like pretty much VM started initially about two years ago as a lab to focus on the best way to manage what we call KV cache memory efficiently. So this is kind of the origin of von which is a paper called page attention. So the idea is to manage what the conversational states and every single token or every single word efficiently so that we can continue to maximize what we call the batch size. Think of this as number of concurrent conversation happening with the LM together in the single GPU and

**[1:36](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=96s)** over time we kind of grow this out efficient algorithm into better scheduling better distributed inference running on multiple chips and then running on multiple nodes. Yeah. And then scale out to more and more efficient model architecture of today. At today we can run trillion parameter models uh such as Ki K2 on like a cluster of hundreds of GPUs today. And we're looking forward to frankly just grow this even more. Right. >> It's it's exploding. It's fantastic. >> Like right now there's a lot of AI workloads. What's the reason now VLM is exploding? >> So a lot of AI workload today is bonded on how efficient it can be. For example, think about your conversation with SH GPT or your usage of cursor. Wouldn't it be great you just come out faster, right? And then on the service provider side, wouldn't it be great to 2x the

**[2:24](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=144s)** number of users that you can actually use? So this is where efficiency really comes in because every single token cost something on the compute cycle. That's why VLM really is at the center where we support a whole ecosystem of model on hardware so that you can run those efficiently at a great performance so that you have a lower cost of per inference token. Our fundamental goal is to build the fastest and easiest to use inference engine. This will allow you to really lower the cost of inference via our approaching open source to be able to run the best model on the best ship at the best efficiency. So that when you're building product and scaling out your user base, you have a lot more rooms to play with and fundamentally a lower cost means better ways to run products as well. Yeah,

**[3:11](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=191s)** >> speaking of the efficiency, lower costs and all that, VLM is known for inference, but now also with post training, we're seeing a lot of inference also on the post training side with reinforcement learning with human feedback and all that. What are your thoughts there? Uh, as as far as that, >> yeah, so VM is being used a lot in the reinforcement learning ROS stack. In fact, we have this exact glue that is Ray. We're gluing together VLM and the training framework as well as all the scheduling and placement together. So a lot of open source RF today use VLM and Ray to exactly achieve that efficient scale out of what we call roll out stage as well as reward scoring stage and both of the these are the important part of the RO workflow to be able to generate sample responses interact with the environment and score to make sure that

**[3:59](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=239s)** you are learning from the best output and best experimental roll out today. So a lot of this require VM to be able to be again high throughput, highly efficient but also reliable, numerically stable and deterministic. So you can debug while when run is the algorithm learning the right to use as well as maximally flexible so that you can actually integrate it with however you design your RO system algorithm today. >> Yeah, a common question I actually get is how do VLM and Ray work together? >> Yeah. So VLM and Ray actually works in a pretty much kind of like a sandwich. Yeah, >> where VM calls Ray internally. So when you run VLM on a distributed mult setup it already initialize ray and use uh all the rep primitive like runtime environment placement groups all the and

**[4:48](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=288s)** then in the future of what we announced today with the GPU objects and we're looking forward to that do that and so this where ray leverage and use vm and there's a part where >> on top of ray you can a lot of folks do run vom inside ray serve ray data in all the ro engine. So where you really see that as a rabb service you see that the framework is using VM and VM internally is using RA and then just collaborates and work together and integrate with other framework like the training side of things side of things all together in the same ecosystem runtime. >> It's fantastic and you know even better now there was a recent announcement with Ray joining the Linux foundation and the Pytor self foundation and VLM is also part of that. What are your thoughts

**[5:35](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=335s)** there regarding an open source? Uh >> foundation is kind of the way to go for open source project. This is where you really invite more and more user and collaborators and adopter to work together and where foundation kind of ensure the governance of the project going forward. So it doesn't change in fact it doesn't really change how the road map is organized and it doesn't change much of how the project itself how we get more new contributions manage the issues managing the technical side of things rather it is there to make sure that important industry collaborators have a common governance model and to work together on it ray and VLM are part of the PyTorch Foundation which originated and host PyTorch right and also So deep deep speed which is a

**[6:23](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=383s)** training system is also >> it's like winning the the training >> and then this is where you see not just like companies working together on open source but also the technical side of things we have deeper integration all together >> what are your thoughts right because you're talking like the whole the whole AI comput stack right you have like the training and inference you have the distributed computing layer and then you have like that the orchestration layer um and it's fantastic because now technically having that uh ability to have that governance in a in this in in under the Linux Foundation. Yeah, I'm I'm with you and I'm excited to see the contributions and hopefully the community growing with that. We're here also at race summit 2025. I know you're giving a talk about the state of VLM. Can you summarize for us what is the state of VLM right now? >> Yeah. Well, so this is a talk we kind of give we're hoping to give every year. >> I will link it by the way in this video.

**[7:11](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=431s)** >> Last year we talked about VM really excel in what we call dense models in cases where we serve large llama for 5B. This year the state of VM really focused on on the API side we're becoming the universal API for people to integrate with. On the model side we're growing the ecosystem of models our model providers. On the engine side we completely revamped the engine core over the last year for better performance and better compatibility with each other. And then on the hardware side is about again this ecosystem of frontier ships but also extreme accessibility so that you can actually not even work know too much about the VM internal to be able to add new kernels add new chips and then finally we're talking about the state of

**[7:59](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=479s)** VLM in terms of distributed where we really leverage ray and kubernetes and different kinds of way to distribute and paralyze to make sure you can serve the biggest model of today. What are you most excited about as far as the the upcoming updates and >> I'm most excited about really getting the model and hardware team to work together? Yeah. Right. So VM is at the center where for model providers they always want to integrate with the zero model support. For hardware of course is to make sure all the new newest and best chip are there. And I just cannot wait to everybody work together on VLM to make sure that whenever a new model comes out it works on all the hardware on day one. Right? Whenever new chip come out, all the model all out there today will get immediate boost. So this is really much a future I'm looking

**[8:46](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=526s)** towards >> and exciting that it's open source. Why do you think usually we go to open source as far as AI infra? >> Open source is not just easy make sure that it has high quality software. It has places where you can go and fix bugs and and talk about where you want it to be and also is a way just to company invites everybody to work together. So the way I will run project is to really make sure that we can be extremely open-minded and be welcoming to whoever wants to improve. How can people start contributing also to >> view on the AI which is our GitHub page you can see go first issue we have contributor guides and pretty much you can go everywhere from documentation to fixing the API server adding test to like if you want to go deep adding new models improving distributed algorithms

**[9:34](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=574s)** or to implement the GPU kernels there's a lot of different area and breast that we have experimented with we have thousands of contributors today in fact we're probably going to 2,000 very soon and we really welcome everybody to join in on this effort and work together. >> It's fantastic. It's very exciting and I feel like you can feel the the energy also here at Race Summit 25. We have a little living room situation here but you know it's uh you've been question you've been also involved in both Ray and Vlm, right? >> Yeah. Yeah. Yeah. So VM is not my first open source project. >> Yeah. So Rey has been in my past life a very important part where where I kind of learned the craft of building open source community right and as well as building making sure that you are delivering what the users really want

**[10:21](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=621s)** you to build this where I learned the PI mindset to make sure that we're building the right things for the users and but is where I really understood the power of community in fact like >> I started at any scale in 2019 and this is where All the journey begin about open source. I love that. >> Yeah, >> that's fantastic. Was that the start of open source for you or what was the first time you ever got? >> The first time I ever done open source is at Berkeley about 2017 2018 where we like that's when Ry was incubating uh within uh the sky computing lab. Uh at that point it's actually for rise lab and there's another project on inference called clipper. That's where I really get to know and as an undergraduate student get to know the art of open source. How do you organize community? How do you improve feature? How do you

**[11:09](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=669s)** in fact what is machine learning serving at that point? And over time we're seeing it evolve so much but one thing never changed that is open source is the way to go >> right >> and it's so you were probably at the time when RL was still in the trend then it lost some timing and then now it's back. What are your thoughts there? We actually um were try to at that point like 2018 2019 Philip was a CTO of any scale like we actually try to build a demo together where you can serve an agent to play pawn on your browser ahead of time. Exactly. Where Philip was demoing the PPL algorithm, demoing our lib environments. Things have really changed now like we we went from just playing games with simple signal simple environment to really just interacting

**[11:57](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=717s)** with the real world right it's not just about text LM anymore it's about the video about multimodality it's about robotics so much more really getting it and becoming real with reinforcement learning >> right I think like over the last like seven eight years we have seen the transition but every ner every lesson learned every paper has been contributing into what we have so far and going forward. So, I'm quite excited about the future. >> So exciting. For some closing thoughts, any advice you would give to AI builders today. >> Well, let's get get it started. Run code, play with code, ask, leverage AI to learn better and like just trust and keep an open mind because open source community really really wants to help you succeed as well. Yeah. >> And let's all work together.

**[12:45](https://www.youtube.com/watch?v=WLl8D1nyaW8&t=765s)** >> Yeah. Let's contribute to open source and connect to the community. So, I mean, thank you. so much for being here. You're absolute natural on camera.
