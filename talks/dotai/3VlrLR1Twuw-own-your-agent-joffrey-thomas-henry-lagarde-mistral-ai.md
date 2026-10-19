---
id: 3VlrLR1Twuw
title: "Own your agent - Joffrey Thomas & Henry Lagarde - Mistral AI - dotAI 2026"
slug: own-your-agent-joffrey-thomas-henry-lagarde-mistral-ai
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Joffrey Thomas", "Henry Lagarde"]
channel: "dotconferences"
duration_min: 20
published_at: 2026-09-28T14:00:24Z
video_id: 3VlrLR1Twuw
url: https://www.youtube.com/watch?v=3VlrLR1Twuw
youtube_url: https://www.youtube.com/watch?v=3VlrLR1Twuw
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Own your agent - Joffrey Thomas & Henry Lagarde - Mistral AI - dotAI 2026

**Joffrey Thomas, Henry Lagarde**

`dotAI` · `dot conferences` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=3VlrLR1Twuw) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Joffrey Thomas, Devrel at Mistral AI & Henry Lagarde, Software Engineer at Mistral AI: https://www.dotai.io/

Joffrey Thomas: Developper Relation Engineer at Mistral AI, Helping developers get started in the Mistral ecosystem. Previously a Machine Learning Engineer at Hugging Face getting and customizing AI for companies and getting people up to date with agents (agents course, transformers agents).

Henry Lagarde: Software Engineer at Mistral AI, one of the world’s leading open-source AI companies. Henry contributed to numerous open-source projects to explore the world of tech.
Worked at Criteo, a leader in retargeting and retail media, and Datadog, the global leader in observability and alerting.

Talk "Own your agent"

As we transition from conversational chatbots to autonomous agents, relying on closed-source APIs has become a major bottleneck for production-grade applications. To build reliable agents that handle critical tasks, developers need absolute control over their models, their data, and their infrastructure.
In this talk, we will discover why Open Source is the only viable foundation for truly autonomous agents, offering the freedom to customize, the power to secure your data, and the independence to build without boundaries.

## Transcript

*2,722 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=1s)** [music] [music] [music] [music] [applause] >> Everyone of you have was already interested in a agent for task, a document, or a question. And every time the same thing happened.

**[0:50](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=50s)** Your data left your machine, go to a network, go to a foreign server in a country that you never see. And then you use a power of a model that you can neither inspect or control. You basically have interested your intelligence to a tool you do not own. My name is Henry. I'm a software engineer at Mistral. >> And my name is Geoffrey. I'm a developer at Mistral, which means I'm talking to developer on a daily basis, but in a previous work I was a machine learning engineer deploying and customizing open source model for companies. And today we want to explain why owning your agents is a must-have pass is to open source. So, when we are talking about owning

**[1:41](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=101s)** your agents, we have to define who are we talking to. There's like general developers, there's developers, and there's companies. Sorry, there's the general public. The general public, they want tools more than they want models. They don't actually care about what model it's running. They want tools like ChatGPT, they want the AI search in Google, they want something that can run or read their mails. >> But me as a developer, I want to use the API first. I want to chase the best model to develop as fast as possible my new feature. And but I also want smaller tiny models that I can run at my place to do some strange stuff in my in my flat.

**[2:32](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=152s)** >> And those developers like Henry when they work inside companies, there are different requirements that are in place. Like what he does in his personal life does not apply to a company. A company they need control over where the model is deployed. They need models of varying sizes. Sometimes small model for specialized task, they need different architecture, MOEs for fast inference, dense for customization, or even different modalities like voice for agent voice, some some OCR for document processing, and so on. And it actually breaks when we need to factor in those requirements. Because those companies are actually our target

**[3:20](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=200s)** audiences that rely on open weights. Even like the model that Henry is working on, OCR, we can deploy it. This is normally an API model, but if needed, this is a model that we can deploy for for companies. We care about providing the best open weight model as long along our own models and our tunings to companies. So, today we're going to talk about an agent. Probably think you all know what an agent is, but never never hurts to do a a quick reminder. So, an agent is a model and a scaffold. The model does the reasoning and the tool use. >> And the scaffold is all the earnest and the engineering side around it.

**[4:08](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=248s)** So, for the loops, the hooks, the context management management, the retry if it fails, everything that's it's the engineering side. >> And you can only get a good agent if both parties are nailed perfectly. You can have the best model if your scaffold is bad, you'll end up with a bad [clears throat] agent, and the other way around is true, too. Models are actually getting bigger. This is true since the agentic shift. Uh 2 years ago, we were relying on text in, text out, simple chatbot. You were probably running yourself with 207B, and that's where you got to know us. But, since we now need to handle code, we need to handle images, we need to handle audio, we need to have [snorts] some computer use capacity to handle screenshots,

**[4:57](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=297s)** those these knowledge needs more weights. And so, like tiny models are getting smaller, but like where it's even more uh where we can see the most is in the big model. What we considered big model 2 years ago was a 100B parameter model. Now, frontier models are anywhere from 1 trillion to 10 trillion parameter models. And um the good news is uh open source is catching up. But, what I wanted to say is for the following uh slides, I will be presenting artificial analysis um benchmarks. Not because it's a perfect benchmark, but at least since an agent is a model and a scaffold, the scaffold here is set, and we are only comparing the model. So, as we say in French, we are comparing cats to cats,

**[5:46](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=346s)** or and the bigger the cats the the the better it is. So, as I was saying, open source model is actually catching up. This is the the good news. Two years ago, we were um thinking open source was what a year behind closed source model. Now, I would consider it personally to be 3 months behind. With this uh kind of performances, open weights, if you're running as a company, a company is probably running in GLM 5.3 flash, an individual developer like you in the room is probably running a Quen um 27B model. And those frontier intelligence model are not that far from from um the best open weight models now.

**[6:36](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=396s)** Let's do a little bit of resource accounting. So, if you want to run those best uh open source models, if you're a company, you're probably targeting like GLM 5.3 flash. Here, we're considering like a bit uh high-end hardware like GPU with Nvidia B300 for companies and Nvidia uh 5090 for individual developers. But, in NVFB4, so a proprietary quantization type from Nvidia, you can actually fit uh GLM 5.3 flash onto a single GPU. Or two if you want to be to be a little bit more uh secure. Um If you do have uh a cluster, first of all, good for you. You are on

**[7:25](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=445s)** the more wealthier side of the companies. Uh you can actually run it on a half of your cluster. Uh and as we know, it's a MOE. MOE are not that great at customization, which gives you some room for a dense model like uh Mistral medium that you can actually fit inside your VLM deployment customize for certain needs. So everything that your agent cannot handle, you customize a model to do it. For the individual developers, you are able to run when 3.8.27b on an Nvidia 5090 that being said it's a [snorts] little bit maxed out in term of VRAM. But if you go into in four that's that works.

**[8:18](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=498s)** >> And like just to give you some cost comparison for the same developer for the same API if you buy a GPU and if you just call directly the API. So this is a like a benchmark for GNN 5.1 so it's a bit old but this is the same idea. Basically if you have one 100 million call a day 100 million token a day, sorry. You are break even. So for a large company 100 million token a day of output and input is nothing. So at two points let's just buy some GPUs. >> Let's see some of the arguments toward API models and against API models.

**[9:06](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=546s)** Let's start with the for API models. There's actually some. You get frontier performances. That's true. We saw them on the benchmark. Those frontier models are a little bit ahead in term of intelligence. But if you want to customize your agent you can you can do a lot with open source model too. It's very accessible. All of you are probably running it. There is plenty of tutorials online. You can set it up really easily. As we saw on the last slide, if you're on the lower side of requests per day um it's actually money efficient. There's like a certain break-even point that you have to hit for you to own and deploy

**[9:54](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=594s)** your own GPU or rent it. And if you're a company, uh it's actually pretty easy and they're pretty generous in term of getting started packages that they they give um for you to try it either on a cloud or directly be on their API. >> That's all of that comes with some issues, I would say. So, first, the fragility of dependency. So, you are basically vendor locked in. Because switching the model after you started implementing it, switching the API, is quite hard and quite costly. But, also, you are building on a moving target, meaning that if the >> [clears throat] >> API just change, change the format,

**[10:42](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=642s)** change the JSON response, change how the model behave, your whole uh production your whole production can break. That means that your business stop and you are losing money. Also, you don't have real control over where your data live, where the agent access, how the workflow are deployed, uh and you have what I call the hidden hidden tax. So, every loop an agent make cost token. An agent doesn't make one loop. It does multiple loops, multiple reasoning. So, for the GPU, when you deploy it, you deploy it once, you pay it once. For the API, every call cost you cost you tokens and cost you money. >> And

**[11:28](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=688s)** obviously, there's other issues like you have a huge observability issues. When you are eating an API, how can you be sure that the model and the answer you are getting is the one coming from the model you requested. We've seen it from from other model providers that if you're asking for instance PyTorch question, you get a lower grade answer from a lower grade model because your query has been rerouted to a less capable one. Or even how can you be sure that the quality you are getting is only coming from the model and not from the engineering that is done server-side. For instance, like there's not a lot of model that can natively handle videos and you could have video uh like processing in your API and that can come for only from engineering. So,

**[12:18](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=738s)** having an open weight model allow you to compare what you get inside the model weight directly and asking the API. It's more the next point is more about agent than just API models, but like if you have repeatable task, something that you need the same outcome every time, with an agent you get different execution. So, this is a clear problem of agents. I've noted that um tweet actually from Sayak, who is the CEO of um of OpenCV, where he did an experiment with his

**[13:06](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=786s)** agent on following a ball with a GPT Astra. Uh so, it took actually 8 minutes and 18,000 token to just do some segmentation on a 15-second video. Uh actually, he works at OpenCV, so he knows what he's doing, but that still sends a bad message. Not everything is an agent task. You can do much cheaper, you can do much better with just regular computer vision as as tools. So, it's less sexy, but like you should be less of a narrow man trying to build Jarvis and a little bit more of a Mario and Luigi building good pipes than than than being Iron Man. The last thing is as a company, you have some internal

**[13:55](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=835s)** knowledge and relying on a third-party provider, you are actually giving those providers a life feed into your organizational logic, your internal code base, your emails, your drive, sometimes your connectors and and so on. And even if that comes at like some speed gain on the short term, that is something that will be paid on the longer term. I always find it funny how a few years ago we were like, "Oh, no, I'm not sharing cookies." And like now we are like, "Yeah, I'll connect my agent to my entire life, from my smart watch to my drive to everything, basically." >> And so, this come with a kind of a paradox where for your agent to be smart, you have to

**[14:42](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=882s)** give him as much context as possible. So, you have to connect it to your server CRM, to your database, to your Google Analytics, to your processes, to your Notion, to your drive, to whatever you want. And so, the more intelligent you want it to be, the more sensitive data you need to get you need to get access to. And so, this come with some structural leak. Your company have some PI. Your company maybe under some sensitive data. We can think about the banking system. We can think about defense or even just medical data that you cannot share outside of your perimeter. And so you need a clear air-gapped environment. So you can audit, KYC your client,

**[15:32](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=932s)** and really knows if your agent had access to information that he was supposed to and not leaked some information to a customer or to another client. So please, stop the leak. Because basically the most secure data transfer is the one that never happen. So if you you stay in your environment inside your VPC and inside your on-prem, there is no issue for you to to deal with agent. To do that, I will just present what I call the sovereign stack. It's how you can build an agent end-to-end thanks to open-source technologies. So first, let's build your agent.

**[16:20](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=980s)** You will choose an open-source model on Hugging Face. You will quantize it, you will fine-tune it, and you will do some embeddings thanks to open-source technology like Postgres. You can build your agent uh for from the prototyping thanks to Llama CPP or Ollama, and push it into production with vLLM. Of course, we I already mentioned it we already mentioned it before, but an agent is nothing without an LMS and a scaffold. So you can build your own if you are brave enough. Use LangChain, use some open-source already existing um uh LMS or use LMS for example. That will allows you to clearly state what your agent has the right to do and what tools and API he has access to.

**[17:10](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=1030s)** And at the end, my favorite part, observe. You can plug directly what you have into your already existing observability stack. Hotel is that for you is there for you. So you can use long fuse miss long fuse to plug it to your open telemetry stack, create your dashboard, monitor your health, monitor some regulation in your agent behavior. And have some understand how your agent behave and how your agent connect to the rest of your environment. If you want to go a bit deeper on what the architecture kind of looks like, this is your local stack. So you have your LMS agent with your agent orchestrator, your

**[17:57](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=1077s)** memory with your rag is a tool that you can connect. And you can do directly some calls to llama.cpp that will embed uh your favorite model on your GPU. And so nothing leaves your environment. Of course, the production one looks a bit bigger. But the idea is the same. Your LMS agent it's exactly the same. Maybe you will fine-tune it because the model is a bit different. But instead of calling llama.cpp, you will just call your vLLM instance. The good thing about vLLM is that you can have multiple uh models on the same GPU or on multiple GPU and it will just do the

**[18:46](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=1126s)** interaction and like the correct forwarding to the correct model at the correct time. And since we talked about observability, all of this already expose some metric, some traces. So you have nothing to do. And we like when we have nothing to do as a developer. So directly you have your metrics, your dashboard, everything in Grafana or we have our friend from DataDog, or in DataDog. So, let's take back and like unleash our power. Like get back our privacy. Start building our own things. And rely on our own data, on our own network, and on our own server. Let's get back where our common sense

**[19:37](https://www.youtube.com/watch?v=3VlrLR1Twuw&t=1177s)** uh takes the advantage of open source and auditability. Thank you very much. >> Thank you. >> [applause] [music]
