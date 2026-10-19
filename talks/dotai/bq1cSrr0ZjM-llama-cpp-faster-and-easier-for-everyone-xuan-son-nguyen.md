---
id: bq1cSrr0ZjM
title: "llama.cpp - faster and easier for everyone! - Xuan-Son Nguyen - Hugging Face - dotAI 2026"
slug: llama-cpp-faster-and-easier-for-everyone-xuan-son-nguyen
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Hugging Face"]
channel: "dotconferences"
duration_min: 11
published_at: 2026-09-28T14:00:21Z
video_id: bq1cSrr0ZjM
url: https://www.youtube.com/watch?v=bq1cSrr0ZjM
youtube_url: https://www.youtube.com/watch?v=bq1cSrr0ZjM
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# llama.cpp - faster and easier for everyone! - Xuan-Son Nguyen - Hugging Face - dotAI 2026

**Hugging Face**

`dotAI` · `dot conferences` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=bq1cSrr0ZjM) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Xuan-Son Nguyen, Software Engineer at Hugging Face: https://www.dotai.io/

Software engineer at Hugging Face, core maintainer of llama.cpp, and an active contributor to open-source LLM tooling and on-device AI.

Talk "llama.cpp - faster and easier for everyone!"

llama.cpp started as a single-file experiment: run a large model on a laptop. Three years on, it's a full local-inference platform. We'll go under the hood of its biggest recent gain, speculative decoding: why it's "free," and how llama.cpp drafts tokens several ways: draft model, n-gram, MTP, and the newest additions, DFlash / DSpark. And since fast tokens are only half the story, we'll finish with a live demo: one command to install, running in seconds.

## Transcript

*1,474 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=1s)** [music] [music] [music] [music] [applause] >> Hello. Hi, and thank you for everyone for coming today. My name is Sun. I work at Hugging Face, and today I'm very happy to present to you a project that I

**[0:49](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=49s)** have been working on. It's called llama.cpp, and I want to focus on our improvement that we brought into the project that allow you to use it faster and easier. All right. So, for those who haven't know know or haven't used llama.cpp, I want to quickly introduce to you what is the project. So, it's it's a project it's an inference engine written in C++ also support multiple platform as well as multiple hardware. And the format the model format that is used is is called GGML. So, to install it to your computer, very simple, you can follow this website, llama.app, and there's an instruction

**[1:37](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=97s)** for you how to how to to install it to into your computer. So, in this talk, I would like to dive deep into what we a technique is called speculative decoding, and then finally, I want to show you quickly how to how you can try it yourself. All right, so what is speculated decoding is one of the our latest improvement in performance in Lama CVP and in simple term is is to speed up the the speed for token generation. By decoding multiple token in one batch in one iteration. So, to under don't worry if you don't understand it just yet. Let's dive deeper into it. So, to fully understand how it works, let's

**[2:27](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=147s)** firstly look at a traditional generation how it how it looks like that you each time you give the model one token and then it predicts next one token. So, it works well because it's we we are doing next token generation, right? But, the problem is that each time you you call a decode path is very expensive because it's memory bound and then it's very high overhead. So, it is not good. So, uh how about what how about we can we decode multiple token at once and then also generate batch bunch of token at the same time. So, the solution we are trying to do is like to predict multiple token at once.

**[3:15](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=195s)** The key point here is that you don't need to predict them 100% correctly. So, in this example that I'm taking here for example, I give the the the model a question. Um the native anthem of France is and I I expect is the answer to be La Marseillaise. But, in this case, um my model doesn't get it correctly. It's La Totale. So, obviously I I need a way to to discard these the incorrect path. So, the model now become like the pipeline now become like uh I I want to predict the next four token, what we call draft draft token. So, the decode pass will get will give the output logit and then from here I can decide, okay, I can accept up to

**[4:04](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=244s)** this much token, which is correct. And then the next time I predict it will be like repeat, I predict bunch of token and then I the verification pass it will look into the the logit and say, yeah, we can only accept up to this much token. All right, so if you want to look even closer into detail, I would suggest having a look at this beautiful video from Bagel AI. Um okay, so what we want right now is a some a way to generate multiple token in one iteration and then extra to that we want to make sure we get the most correct token as possible. In our work we want the the acceptance rate to be high. Okay, so what are implementations that

**[4:53](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=293s)** we currently support in llama.cpp? The first one is the basic N-gram. Uh it is quite similar to predictive keyboard that you have on your smartphone. So, the way it work is that it had like dictionary of all the of the commonly used N-gram. And yeah, yeah, it's very simple. The problem with N-gram is that it hit or miss. So, the acceptance rate cannot be guaranteed to be high. So, the next idea that we can think about is to use a smaller a smaller very fast draft model. So, in this guy for example, I can use a main model is a big one like 32 billion parameter and then a smaller one, 3 billion. So, it the way it work is that the same

**[5:43](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=343s)** sequence the same question is given to all of the two model and then this small smaller one can generate draft token very fast. So, yeah, it does work for a while and then uh right now uh we have something is called MTB, which is used by many frontier open source model. So, the way it work is like you have only one model main model now, but then the hidden state is being passed to different heads. So, you have the uh the normal NLM head for the very next token and then the MTB head uh sees multiple token prediction head for specifically for predicting these um next draft token.

**[6:31](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=391s)** Okay. So, the problem now that there's like a small problem now is that this MTB head itself is also a transformer. So, it's it's auto regressive. It's hard to predict token one at a time. So, it is still fast because the MTB head is small, but can we speed up even further? So, now we enter realm of what we call D-Flash, diffusion-based NLM. Now, we use diffusion base to generate all of the um all of the draft token in one pass. So, in most case, it will be faster than MTB. And then we also have D-Flash, too. Uh I won't go too much into detail here. You can uh see the the paper for for more details you want, yeah. Sorry, I don't have much

**[7:19](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=439s)** time. And um so, the latest innovation in this area is called DeepSpark. So, DeepSpark is like semi um auto regressive where where they have a a diffusion model and then a very lightweight um sequential model. And in exchange to that, it it also gives the very very good verification something called confidence score for each token. So, it know how when to discard this token. >> All right, so let's look at some benchmark result we have here from Unsloth. Yeah, we have almost double speed for most of the NTP model. And then for this last we can go a little bit higher like up to two one two

**[8:08](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=488s)** to one three times faster than no Dflash. Yeah. So, how to use it? You can go to hugging face hub to search for llama compatible uh model with the keyword shush you laugh and then you can add Dflash this park NTP whatever you want. For example, I can show you here. The first model is like the original one no NTP and see the next one is with NTP. And for the most case inside the model page, you can see all of the instructions that allow you to to run this model. For example, I'm taking this one for example and then when you scroll down you can see a list of instruction here. Yeah.

**[8:55](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=535s)** So, let's look at the quick demo that I want to show here. No, sorry. Not this one. Yeah. So, I want to clear and then uh given I already installed llama.cpp onto my machine, I can just run it and this time I run it with NTP. Yeah. So, I'm using llama.cpp so it allow me to interact directly with the model via my command line interface. Yeah. So, it's quite fast. How about we are going to llama server? Yeah. So, llama server. It will spawn a small server at this address that you can try it locally. And then from here, you can select this model.

**[9:42](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=582s)** For example, I'm Yeah, I'm using the 4B, for example. Yeah. Otherwise, I can try Shemafor, why not? Yeah, and it will be loaded shortly. I hope so, yeah. All right, maybe I try another model. No, it's it's loaded, yeah. All right, fine. Okay, so I can chat directly with it. And so I can maybe take a quick screenshot like this. No, I cannot paste it here, but I can What I can do is drag and drop, and what do you see? All right. I I It can show you It can show you what tell you what it is it's seeing on

**[10:29](https://www.youtube.com/watch?v=bq1cSrr0ZjM&t=629s)** screen. Yep. So, that's all for today. Thank you for listening. I hope you enjoyed [applause] my talk. >> [music]
