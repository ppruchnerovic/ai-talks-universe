---
id: FkVhfw5_6pw
title: "Tiny, Framework-Aware Code Diffusion: Training a Mixture-of-Experts on a Consumer GPU"
slug: tiny-framework-aware-code-diffusion-training-a-mixture-of
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 25
published_at: 2026-08-23T07:00:20Z
video_id: FkVhfw5_6pw
youtube_url: https://www.youtube.com/watch?v=FkVhfw5_6pw
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: true
---

# Tiny, Framework-Aware Code Diffusion: Training a Mixture-of-Experts on a Consumer GPU

**Speaker not identified**

`PyData` · `PyData` · `2026` · `25 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=FkVhfw5_6pw) · [Conference site](https://pydata.org/)

## Description

Welcome to the PyData & PyCon Yerevan 2026 video collection - our biggest edition yet, held on 24-25 July in Yerevan, Armenia.

From data science and machine learning to Python tooling, production systems, research, and open-source technologies, these recordings capture the ideas, experiences, and practical knowledge shared on stage.

🌐 Website: https://pydata.am

📅 24-25 July 2026 · Yerevan, Armenia

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*3,175 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=5s)** Hello everyone, welcome uh thanks for attending this session. So our topic today we're going to explore um small and sovereign systems or let's say domain specific intelligence two AI systems on one single 8 GB VRAMm system. Uh and basically we what we achieved was due to a a very interesting experiment. Uh we wanted to uh address some of the challenges that we had in like with the with the generic LLMs and and and training them, budgeting them and basically addressing uh cost performance issues. Um well most of us

**[0:54](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=54s)** some years ago or like uh even like a few years ago uh purchased some devices which by like day-to-day we are using most of us are not having those enormous VRAMs and system resources and stuff. So what should we do? Um well I ran a experiment with uh basically my agents and uh which were b trained before I run this experiment and uh well the it was just one engineer one laptop and addressing two problems. Uh the first thing I want to go through is uh thee decoder like which is a uh mixture of expert diffusion coding model a tiny

**[1:46](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=106s)** model or a tiny toy uh we we can address it as a tiny toy which was an uh like multi-step fast training SLM capable of generating more than just code completion or code suggestion. So we know that like most of us engineers or developers we don't need the frontier compute power to uh do the to get the work done that we want like may maybe many of the generic users they they don't care about the architecture and what they are doing but since we know what we are doing uh the right size and the right measures always accomplishes

**[2:35](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=155s)** the uh requirement. So the result was the result of this experiment was uh a 10 million parameter coder SLM and also uh and another interesting thing that we achieved was like training an Armenian uh texttospech and speechto text pipeline with like utilizing already existing tools. Um I by the way I cannot speak Armenian. I don't have the domain knowledge but it's just um it's basically um like what I I I could have scraped and like going into the grammar and finding out how the language works. So uh the part a of my talk will address

**[3:26](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=206s)** uh training of the mixture of experts mixture of the diffusion coder. So the 10 million parameter diffuser coder uh was was an achievement of like um experimenting with uh GPTbased LLMs. So GPTbased LLMs or like all of us or most of us must know Andre Karpathy anyone I I yeah sure. So uh yeah he released a repository which was addressing like how to how to make a nano GPT and like similar approaches. But uh that sparked some ideas of working on uh diffusion base uh and and

**[4:15](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=255s)** having having a customized tokenizer uh not a hogging face tokenizer but a super BP tokenizer to to achieve uh masking and uh unmasking and and and achieving speed uh and almost like accurate uh let's say results. So we know that like most codes live in a narrow world. So and code LLMs are enormous, opaque and costly to run. Uh the infrastructure to host them is pretty costly. And um this experiment was targeted to accomplish um like a front end or and some of it like backend uh development with

**[5:03](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=303s)** TypeScript native languages and its frameworks. So uh the question was can a 10 million parameter model uh on a laptop specialized per framework and um it was able like what we trained was uh able to generate code by unmasking uh not like the traditional uh token decoding and like predicting the next one and predicting the next one. So the mass discrete we use the mass discrete diffusion uh for for and and not auto regressive methods to achieve this also um like the the entire flow was uh stitched together based on multi-layer experiments. I'm going to

**[5:52](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=352s)** discuss more and share the code as well. Um so the result was uh 9.58 million parameters for experts on one 8 GB uh VRAMm laptop. Uh and uh the first phase was to train that our tokenizer and uh also introduce the router which was able to uh detect um like the domain specific expert and route to the specific destination that the model is required to uh send the request. So uh the standard what what went wrong was uh during our experiment was uh the standard MOA collapse uh

**[6:42](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=402s)** mixture of expert the experts collapsed midway and and we couldn't generate a readable or compilable code and uh the router entropy uh was like pinned at the maximum and we couldn't basically get it working properly. Uh but what what basically went wrong was um uh was like stitching a load balancing loss to routers zlos. Um the cheap supervision basically breaks the collapse. So the cross entropy on the main router uh was uh basically derived from the source repository. We try to label the source repositories when training the uh

**[7:33](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=453s)** tokenizer and uh and and our uh our data set so that the router understands what is where and what means what. Uh so and and and uh and uh we used uh basically a composite objective from some uh research papers from Wong at all uh for code diffusion models uh plus a two-stage uh curriculum uh which was general generic pre-train and following by a fine-tuning and the result was our forearm abolition same corpus uh and like the matching ground of the compute and with uh our routing meaning uh mixture of expert and

**[8:24](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=504s)** diffusion on we were able to uh basically reach to uh like perplexity levels that was usable and uh like with with like the the model was also trained with a dense and no mixture of expert variant And it basically it was unusable. Um and uh what router was doing across the dnoising step was uh committing more tokens as as as it was getting unmasked it was it was basically committing more tokens and then it was caching uh the assignments uh after like uh basically getting the entropy and committing all of that. it was caching the steps and skipping ahead

**[9:14](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=554s)** which was basically um like achieving the uh the stability that we wanted a usable stability. Um so this what what we this is like the result was not a stateofthe-art uh small language model or a or a coder diffusion model. It was just a a experiment, diagnostic and analysis contribution. A recipe that fits into our day-to-day um development or developer machines and like some small tasks that we can uh basically run on our local machines and get some work done. And the code that I'm going to share with you in a

**[10:03](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=603s)** repository uh is reproducible uh from like the first step to the last and uh you can you can experiment with it, you can uh fine-tune it, you can change it and experiment with it as as you like it. So dos and don'ts uh a tiny mixture of experts. Um I have to say that uh we need like what what we learned from training this was measuring the routing uh with entropy and a specialization and not only the loss um the it we don't always need like complex methodologies or complex uh solutions to um to to basically uh like uh debug or or or supervise what is going wrong. uh

**[10:53](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=653s)** we we can just use cheap supervision for uh for example we use repo labels uh to break the collapse and um we have to we we basically decided to abolate uh to isolate the cause uh to understand like what produces a better stable usable result uh and also like uh in order to like fit it like we didn't uh basically chopped the model and uh like uh quantized it to to to fit into a into 8 GB of VRAM. We we tried to train it from the ground up to be to be able to fit into our uh basically uh infrastructure and the uh and machines. So uh but uh we

**[11:48](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=708s)** need to be like um we need we need to be honest as as well when when we are training uh our models the the uh the result of the training the benchmarking and uh and uh uh like the results we are obtaining needs to be uh needs to be realistic and usable. So this model can achieve uh like code generation for small tasks with a huge domain uh knowledge. Uh meaning that it can it can basically uh understand your entire codebase and satisfy uh your requirements with small code generations, enhancements and uh suggestions uh but uh won't replace uh an engineer. It won't replace a very large uh model, but well, it's cheap,

**[12:37](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=757s)** it's free, it lives in your device. You can fine-tune it, you can make it uh run better and bigger tasks. And the part two of my uh talk would address what we experimented with the Eastern Armenian language uh and training a pipeline that is um that that tends to address and contribute to basically uh pro providing uh businesses users or or anything with with with with usable um let's say services or products. So um we know that like some languages uh Armenian is one of them uh are very hard for uh models to to to to be understood because of

**[13:27](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=807s)** their grammar because of their uh linguistic system. So uh what I tried al although I don't have the domain expertise in this but I used some friends uh u help to achieve this and use uh used like um already existing uh technologies to with like some tiny tricks and hacks that that we could uh basically uh achieve uh Armenian voice model uh to be which is which is uh basically producing um let's say usable results. So for this uh we I think most of you should should should have heard about Kakoro which is a 82 million parameter model and uh it just understand Phenom tokens and it's

**[14:20](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=860s)** it's language blind so it doesn't care what language it is. So th this is this was a good choice among all other models because it doesn't care about uh what system the language uses. It's it's not like uh it's basically language agnostic. So and every uh eastern Armenian phenom already you can map it to basically it you can map it u exactly to its vocabulary table. And uh then we we used the G2P which was uh which was basically uh the the tool the intermediary tool uh to write Armenian G2P uh and and and be a feeder to the Kokoro model and uh the result was an

**[15:09](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=909s)** intelligible Armenian with no model retraining. It was just a normal fine. So uh there were three local parts and one standard interface. So the user can speak to the platform and it gets uh basically we have a validator step and then uh we can route any LLM into the in into the pipeline and the customized Kakoro with Armenian uh training data can produce a reply uh which can be played for the users and Um there is there was a step uh which which we wanted to like the result of the

**[15:58](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=958s)** previous step was an Armenian uh spoken let's say sentence but with American English accent. So we couldn't really use it. Uh so the result was using another tool which is Canada. So the Canada is used to convert uh or take your source audio. you can record a source audio in your native accent and then basically inject it, brute force it into Kakoro to produce more accent accurate Armenian uh basically u Armenian spoken output. So, and uh what we tried and what what didn't work was vibe voice. We we we tried wibe voice uh it didn't produce

**[16:49](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1009s)** really usable uh outputs. The the problem was the accent and the accuracy of the phenoms and also with the with the like with the finetuning f like retraining the entire cakoro from ground up was was an expensive uh step. it. I mean, you you can still train it on your on your machine, but it takes much longer like uh maybe uh for me it took around 4 days with uh with like multi-step training meaning uh it was paused sometimes and then resumed and it wasn't so so usable. Um so yeah what we achieved was like uh with a low error rate well it's relative but yeah low

**[17:39](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1059s)** error rate uh or character error rate Armenian um Armenian uh whisper uh benchmarked output and um well basically on on the like six to eight times of the real time uh speech to text on the 8 GB of GPU and uh the entire pipeline which again I will share uh in a future update we can connect um and uh just just a single script to bring the whole pipeline up without uh training or anything and it's it's measurable it's it's reproducible uh what we did for this um well we basically exploited language blind phenom models um IPA G2P

**[18:28](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1108s)** And uh also like using voice converter for speaker identity uh keeping every component of open AI compatible endpoints and all of that. Uh and and also like we verified the real o audio uh that that uh that used to train and retrain the model and also it was an it was a local first uh approach. So uh and and we the the don'ts uh for low resource voice are like as you can see and read on the on the board. I'm not going to uh go through it but um well um what we learned was like we should we shouldn't assume that fine-tuning stage always actually improves this stuff. Uh

**[19:19](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1159s)** it didn't for us it didn't unfortunately. So uh the two projects were basically uh aimed to prove that with the right size and right architecture you can achieve uh things that uh are are labeled as myth or it's advertised as myth that that you need like very expensive hardware to do some like u let's say u some mid-level work and uh like also So like the local first all of us are or most of us uh are a bit paranoid about like what AI can do. Uh I'm I'm sure that uh like you saw that couple of days ago uh you heard about open AI's

**[20:09](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1209s)** agent breaking into augface server. So uh like live having your own infrastructure and models into in in your in your own uh in your own uh machine helps securing and also uh keeping your uh your stack cheap uh maintaining cheap. So um thank you for your attention. I am going to uh answer your question now and also uh for code and uh the repositories uh unfortunately I'm not going to be able to like demo right now but uh the repository is there code is there you can just uh in your in your free time you can go download it and like clone it and uh use the code however you want it's open source it's

**[20:58](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1258s)** there. Thank you. Thank you so much. Thanks. >> Okay, we have five minutes for Q&A please. >> Um, okay. Uh, hi. Thank you. Uh so first question uh about first project uh why it was why this exact choice of the architecture why not just small language model why mixture of experts uh why this combination and also uh in addition like uh what did you mean by routing uh I I just don't understand terminology what was sure the routing part it's >> thank you for the question So the reason of mixture of expert was so for dense models when you're training dense models dense models need more generic data and

**[21:48](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1308s)** a more supervised training uh meaning when you're when you are picking your data sets you need to label them properly you need to uh you need to train them in a specific way which is by by its nature um let's say more expensive to train and also they don't understand that for example I I'm sure you've seen it like you're asking something uh from from generic LLMs you're asking something uh uh like react related but uh it generates like some other frameworks or or you're asking some JavaScript code but it forcefully generates something like uh TypeScript you need JavaScript it gives you TypeScript you want something in HTML but it forces you to use react. So the

**[22:38](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1358s)** the reason of router the router itself understands what is the requested language it and its frameworks. So when you're asking okay I need this we like in front end we have react and react native yes the backbone is the same but their characteristics their nature is different. So you need a smart supervisor to say okay this is react native so I am going to delegate this task to the trained um expert to satisfy the requirement. >> Thanks and each expert is a separate model trained separately >> each so the beauty of it is imagine that you have a bucket but you are dividing your bucket and on top there is the

**[23:28](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1408s)** supervisor router. So each one is trained on like on top of your base. The core or base is Typescript which we did was TypeScript. Typescript is was the base uh basically expert. Then we added the frameworks in the router. So it understood that okay in the domain of Typescript I have this uh like frameworks. Yeah. >> Okay. Maybe one quick question. >> Yeah. One quick question. Uh what is G2P? What is IPA? >> G2P and IPA. These are like tools uh that you can basically um train a voice model based on its wavelength. it understands uh the the audio wavelengths and you can feed it

**[24:18](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1458s)** into an into a audio um something like a multimodal model that understands audio and vision and text. So uh Cocooro is an audio model. It's it it produces um like uh audio results. G2P is is the tool that you can use to take out any languages phenoms and then feed it into the model. So it the cooro is a language blind model by the way. G2P helps that language blind understand the language. It extracts all the uh wavelengths and everything the phenomes the characteristics and injects it into the model. >> Okay, I think that that's it. Let's do a thing.

**[25:04](https://www.youtube.com/watch?v=FkVhfw5_6pw&t=1504s)** >> Thank you. Thank you so much. Thank
