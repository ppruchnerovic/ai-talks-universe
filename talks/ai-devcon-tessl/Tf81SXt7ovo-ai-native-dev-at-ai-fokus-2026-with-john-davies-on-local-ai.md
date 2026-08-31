---
id: Tf81SXt7ovo
title: "AI Native Dev at AI Fokus 2026 with John Davies on local AI models"
slug: ai-native-dev-at-ai-fokus-2026-with-john-davies-on-local-ai
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 9
published_at: 2026-05-26T15:36:44Z
video_id: Tf81SXt7ovo
youtube_url: https://www.youtube.com/watch?v=Tf81SXt7ovo
tags: []
transcript: true
---

# AI Native Dev at AI Fokus 2026 with John Davies on local AI models

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=Tf81SXt7ovo) · [Conference site](https://tessl.io/devcon/)

## Description

AI Native Dev at AI Fokus 2026 with Baruch Sadogursky (@jbaruch) hosting John Davies on running local AI models

## Transcript

*1,417 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=0s)** record. Go live. Now we wait a little bit until it starts and then we'll do it. Hello and welcome back to AI Native Dev by Tesla coming to you live from AI Focus 2026. Um John is my next guest. Welcome John. >> Thank you. Uh and John so your your

**[0:51](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=51s)** topic is local basically running on AI models and this kind of stuff. So let me ask you they are not very good are they models >> that's controversial. >> Okay. >> No abs u absolutely nope. You're you're wrong. Uh they are incredibly good. today's um I have models running on my phone that are better than chat GPT from last year one year ago. I have models running on my laptop that are better than chat GPT and um the best models in the world and and I use chat GPT as an example but Claude Sonnet and Opus um as of November last year that's 6 months back >> okay so but it's still 6 months back we are now the frontier models now are 6 months better

**[1:38](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=98s)** >> okay so if you're if you're writing code uh absolutely um the the frontier models however if you're writing code and um just gen generically working on code. It doesn't have to be running on your laptop. You can still use the the GLM 5.1s. You can use the Kim K2.6. Um you can use um mini LLM mini LM um M2.7 and you can run um DeepSeek V4. They're all open source. They're all open weights or open weights I should say rather than open source. And while you can't run them on your laptop, you can still run them in anyone's environment that has that. And >> and and still we will have mostly so the advantages are are mostly cost or are

**[2:28](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=148s)** there others especially if you are not running it in >> Okay. So let's let's put them to I if you're running the the the four that I've just mentioned. Um yes cost is a big thing. You're looking at about a 20th of the cost. So if you're running through some sort of general coding stuff that doesn't need to go out to your customers. I run mine. Mine sit and run all night. Numerous laptops and uh machines around the company were running on Kim K 2.6 most of the time. Um and these models by the time the video comes out will all be out of date by because they they change on a weekly, you know, basis literally. Um but if you're running uh models on your local machine, there are they'll run pretty good for coding, but I use them for coding. I mean there are so many other things you can run them on. >> Yeah, that makes sense. So, so yes, so obviously price is is is a very big factor, especially considering how the

**[3:17](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=197s)** Frontier models are getting more and more expensive almost every day. So, that's a good alternative. Um, let me ask you, how do I know that, you know, I'm spoiled by all this uh uh fake um subsidized token economy and I'm like, hey, I'm used to run the Frontier models for 10 bucks a month. Now suddenly that's not the case and uh I have this for that if I'm going to run local models I won't get the same results what I need. How do I know for what the local models are good enough for me so I won't have to compromise on quality? >> Okay so let's if we can just break slightly from coding. Um, coding is one

**[4:05](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=245s)** of the most uh demanding tasks in in this. Um, so if we're going to concentrate on coding, then you need really the latest most powerful models because you're competing against everyone else and and they're all going to be a couple of weeks behind you. You you want to be up there. But if you're running you're running rag, you're running um you're going through your emails, you're going through other people's emails, you're you're running um text to image, image to text, text to speech, speech to text um as will be transcoded by this very video, etc. All those models run 100% as good as and in many cases better and faster locally than they run in the cloud. >> How about text ordering? How about um like general reasoning? >> Two different things you mentioned there.

**[4:52](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=292s)** >> That's two different examples. Yes. >> Text authoring. I don't think any models are brilliant at text authoring. Models read really well. They read, you know, very significantly better than they write. Um same as uh no disrespect, but when you speak English, I can tell the media you you understand English fluently 100%. >> Yeah. >> Um but you don't speak it the same. And so just as a model you a model can read and it reads beautifully well and it but they don't write particularly well >> um for reasoning the even the small models running on the machines are really really good and certainly for for going through PDFs for trans transposing for reading multiple languages for decomposing photos pictures they're as good as if not in many cases been proven to be better than the proprietary models >> interesting so okay so so quoting Aside,

**[5:42](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=342s)** another very I would say hot right now are all the personal assistants, all the clothes for different different flavors. I I I think they are a very good candidate for switching from cloud frontier subscription models to to those both because they run 24/7 so they burn through a lot of tokens but also because those models are good enough for what they are doing. >> Totally. I mean you you should always be looking for the most efficient, cheapest and fastest model to do the job that you need to do. And if you're downloading video, trans transcoding it, translating it um basically looking for information in in that, then the local models literally

**[6:29](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=389s)** run on a phone today will do that. We use them for we go into a meeting, they're busy picking up all the information and and basically busy processing it. >> Yeah. So basically your personal assistant that go through your emails that you know look at your calendar send you important information prepare you for meetings and this kind of stuff. Oh absolutely this is all >> and and and let's get to one of the most important parts privacy. A local model is not by definition on its own is is is totally private but you can certainly make it private if it sits on your phone or it sits on your laptop. Um you can be off the internet and if you're recording a conversation it is totally yours. We we're living in Europe and it's um privacy is important here. >> Yeah. And data locality and all this kind of stuff. >> I mean you use one of these American things, it's all been everything's been

**[7:16](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=436s)** taken off and using for training and before you know it, it's uh it's it's published on the internet, whatever it was. >> That's very true. That's very true. All right. Okay. So rule of thumb, when do we start looking at something that other than Frontier subscription models? >> I would suggest everything except coding. uh and coding unless you've got the sort of topof the range latest 128 GB Mac. Um everything but coding but literally everything everything we run is local. >> Brilliant. Okay. So I don't know about you folks but for me that's kind of a very um I would say revolutionary concept. I mean, I assume that the local models can do some stuff, but what you are saying is is is really interesting,

**[8:04](https://www.youtube.com/watch?v=Tf81SXt7ovo&t=484s)** and I will definitely give it a try for for more than I would do um before. >> You're going to get lower latency. You're going to get faster inference out of a small Quen 3.5 4B model than you will out of chat GPT. >> Well, that's uh that's very impressive, >> John. Thank you very much. >> Thank You stay tuned for one more interview of Yan Native Dev by Tesla at AI focus right after this. >> Perfect. Thank you. >> Thank you. >> Yep. Sorry for being a little bit dramatic, but
