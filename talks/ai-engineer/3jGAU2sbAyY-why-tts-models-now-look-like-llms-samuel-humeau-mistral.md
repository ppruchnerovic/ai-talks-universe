---
id: 3jGAU2sbAyY
title: "Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral"
slug: why-tts-models-now-look-like-llms-samuel-humeau-mistral
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Samuel Humeau"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-05-09T17:00:07Z
video_id: 3jGAU2sbAyY
youtube_url: https://www.youtube.com/watch?v=3jGAU2sbAyY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral

**Samuel Humeau**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=3jGAU2sbAyY) · [Conference site](https://www.ai.engineer/)

## Description

The dominant architecture pattern for text-to-speech in 2026 looks a lot like an LLM — an autoregressive transformer generating sequences of tokens, one frame of audio at a time. Samuel Humeau from Mistral walks through why the field converged there, how neural audio codecs solve the information-density problem (audio carries ~200kbps of signal; you can't feed that raw to a transformer), and what the streaming trick actually is that makes voice agents feel responsive before the full audio has even finished generating.

The talk uses Mistral's just-released open-weight TTS model as a running example — live demos of voice cloning from a few seconds of reference audio, a voice agent answering real conference schedule questions, and a breakdown of the codec-to-backbone-to-decoder pipeline that produces it all. There's also a frank section on what's still unsettled: how to handle streaming text input (tokens arriving from an LLM in real time rather than a fixed block of text) and why getting that right is the next meaningful latency win in agent pipelines.

It's the kind of talk that makes the system feel less like a black box — not by oversimplifying, but by showing exactly which engineering choices are load-bearing and which are still open problems.

Speaker info:
- https://x.com/DrSamuelBHume
- https://www.linkedin.com/in/samuelhumeau/

Timestamps:
0:00 Introduction and Mistral's new open-source TTS model
2:06 Text-to-speech in AI agents and latency
3:33 Live demo: Voice cloning with 'Paul'
6:00 Voice cloning capabilities and multilingual examples
8:01 Historical context of audio generation
8:55 Transformer-based architecture for TTS
10:00 Challenges of information density in audio
10:55 Comparison of bit rates: text vs. audio
11:39 Using neural audio codecs
13:10 Backbone transformer and frame-based generation
14:56 Text conditioning and model architecture
16:08 Latency performance metrics
16:22 Future outlook: Streaming text input
17:35 Q&A: Generating text and audio simultaneously
18:24 Q&A: Availability of voice cloning features
19:35 Q&A: Philosophical take on speech interfaces
20:44 Q&A: Next steps for streaming audio and text input

## Transcript

*3,399 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=14s)** So I'm I'm from ML AI uh and we are going to talk about uh speech generation and text to speech. Uh there is an occasion uh we released last week our first texttospech model and it's open source so I really encourage you to uh check it out. It's an extremely strong textto-spech model. We are very proud of it. Um, and for this occasion, uh, I thought we could review some of the recent trend in text to speed architecture since there is a dominant uh, trend uh, emerging these days although this can change like uh, very quickly. Um and uh so this talk is slightly academic and addressed to people who wants to know a bit more about how you uh do text to speech. Uh this being said, we have a

**[1:02](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=62s)** few years before the machines do all the science for us. So we might enjoy it. Uh today um I'm Sam. Uh yeah, I work at Mistral as AI scientist. Before I was at Facebook fair when it was called Facebook. Uh and Mistral a few words about the company. It we are a frontier lab. We have we've been founded uh a couple of years ago. Uh we produce frontier model uh but we're also a B2B business. We we help organization uh in their AI transformation which is kind of a buzz word but literally every company is transforming with AI. We help them by providing them tools, product and uh dedicated people to help them in their custom needs. Um back to the text to speech. So there

**[1:51](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=111s)** are a few offline use case of uh speech generation like the the famous listen to the blog or listen to the article. But nowadays the the king use case for text to speech is uh its usage within agents and in particular it's used to interface uh with a chat agent. typically in a pipe like this uh where you have a central chat agent that does text to text but does it extremely well and you want to talk to it so you add a speech to text and you want it to speak to you so you add a text to speech u as everybody in this conf will tell you the latency is key here uh so you can reduce the latency on the left by having the speech to text done in real time so that when you detect the end of turn you already have the transcript

**[2:39](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=159s)** it's already done. Uh, and we're going to focus a bit on the right side today. Uh, it's also very important that as soon as you have the first audio packets, you you you start to um to voice them out. This way, the perceived latency is lower. In fact, since your LLM can stream uh some text to you, uh actually what you ultimately want is something like this. If you're going to interface a chat assistant uh which is a real time text input text to speech where uh as soon as you have the first token of the LLM uh the the machine starts to speak. We're going to talk uh about it in the in the end of the talk. I want to focus a bit uh at the beginning at the output side uh and what it what it means to stream

**[3:29](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=209s)** audio. So to illustrate this, I have uh this app that I vip coded for the occasion. Um and so we're we're going to uh to use this texttospech model that we released that I mentioned and we are going to hear Paul. So Paul is an actual human being that sounds like this. >> The persistent anxiety that fills the rest of my life is calmed for as long as I have the flavor of something good in my mouth. Um, so this is uh like some actual recording on some uh actual person named Paul and we're copying his voice. Uh, >> so with the sunshine and the great bursts of leaves growing on the trees just as things grow in fast movies, I had that familiar conviction that life was beginning over again with the

**[4:17](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=257s)** summer. >> Um, so let's focus first on what's happening here. Uh as you can see with the copying the voice and the the first audio pocket >> happens first and we can start to emit audio which greatly reduce the perceive latency even though the full computation of the the audio happens a few seconds later. So in if you use it in an agent. So here I crafted a small agent using a speechtoext uh one of our uh LLM and uh this very text to speech so we we can speak to Paul um and hey Paul uh can you tell me what's the title of the session at 12:20 please? The session at 12:20 p.m. is titled

**[5:06](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=306s)** Reichi Mini, Giving a Body to AI by Andres Marafiot. >> And what was the session at 11:15, please? >> The session at 11:15 a.m. is Beyond Transcription: Building Voice AI that actually understands conversations by Herve Breden. >> Did you enjoy it as much as I did? Thanks. >> I don't have personal experiences or emotions, but I'm glad you enjoyed it. >> That's all I can do. Um, so the important thing here is that since the audio packet arrives first, you still have a a decent latency and you can enjoy the conversation with the agent uh despite the fact that the audio is still uh not generated fully. And so we're

**[5:56](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=356s)** going to dig Oh yeah, sorry. Uh I want to make a one degration. So I mentioned the the voice cloning here. Uh this model can like only need a few second to clone the voice of someone. Uh so again this is how sounded and this is how we generate text. >> So with the sunshine and the great bursts of leaves growing on each >> it really sounds alike. It's also very good at inferring how a person would speak in in another language. So for example, this is a voice, a French voice maybe >> and if we generate >> and so with the sunshine and the great burst of leaves growing on the trees just as things grow in fast movie. >> Yeah. So we can clearly recognize her

**[6:45](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=405s)** and we can clearly recognize a very strong French accent which as a French myself I do enjoy. Um, I can I can even clone my own voice. So, this is how I sounded during the recording. >> Hi, this is Sam. >> And uh this is how I >> and so with the sunshine and the great burst of leaves growing on the trees, >> it works pretty well. So, this way in my time of delusion and at the peak of my ego, I can discuss with myself uh on on a complicated problem, which is nice. Um and so it's becoming so easy to uh impersonate a voice that it's it's becoming very easy to to configure. Um so it's a small degression but currently actually a lot of large company they do

**[7:32](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=452s)** have a concept of vocal identity and they do care in their branding about how they sound uh in their advertisement in particular. But I think this uh concept will becoming more mainstream and just as like a lot of company uh define how their website appear as their brand identity, it would be the same for the voice identity. Um oops sorry uh back to how we do it uh in general. So uh all right this is this is an audio uh physically it's the pressure of the microphone that we measure from time to time like uh several thousand of times per second. So it looks like this. And historically to generate the audio uh there have been a lot of uh attempts a lot of systems like in the prehistoric

**[8:21](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=501s)** time you have like stitching of uh words that were spoken like uh in the French train system SNF for for those who knows. Um and then a new generation arrived. Uh at some point the trend was to generate each sample one after the other. Then another era was generating the whole audio at once. But as we can as we saw it, it's very interesting to have the beginning of the audio generated first so that we can start to play it out. So it seems that most labs have converged to some common patterns and obviously the the first one is inspired by large language model. We're trying to uh transform the problem as a language modeling problem because humanity is extremely good at modeling sequences of token. So pretty much uh everybody is using an auto reggressive

**[9:11](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=551s)** decoder backbone and uh generate audio one piece after the other. Now um as I said we really don't want to generate one sample after the other. So what we want to do is generate like patches of audio one after the other. Um, so the expected system looks like this where you you have an encoder that transform like a frame of audio something like 80 millisecond into something that ideally is a token because humanity is very good at uh modeling sequences of token and then you have a decoder that does the opposite. Uh now for text it's pretty easy because transforming the text into tokens well it's easy right? you can take like words as token and it it works pretty well even though we we do much better. Um,

**[10:00](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=600s)** for audio it's much harder because one token doesn't have a lot of information. Like one token of a vocabulary of a thousand, it's 10 bits of information and the audio requires much much more uh like a much larger bit rates. For example, a standard quality MP3 that's 200 kilobits per second. And so in order to transform this into a sequence of token like and not have thousands and thousands of tokens, uh we need to somehow compress it and reduce the size of it. Maybe drop what's not needed. Uh an interesting point of comparison is tech text captioning. Uh because if you drop all the acoustic information and you you just focus on the text like with a subtitle track, uh you actually drop most of the information. It's a massive

**[10:48](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=648s)** reduction and and you only have uh a few bits per second uh remaining. So here in this in in this demo I use uh our realtime speech text to measure my bit rate in terms of uh tokens per second of text and um I'm a very competitive person and very I'm very good at speaking. Uh yet I I'm barely 15 bits per second of uh actual information. you you can try to uh to to to beat that, but like in the grand scheme of things compared to 200,000 uh bits of information per second, that's not a lot. Uh obviously uh we want to use something that allows to recover like acoustic uh features like the voice and uh and other aspects and not just the

**[11:36](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=696s)** the semantic information as in the text. So the codec that are used uh typically reduce the audio to about a few thousand bits uh per second. Um in our case for instance uh we treat the problem with uh sorry we cut the audio as uh with pieces of 80 milliseconds so 12 frame per second and we transform each frame into several tokens like 37 in our case. So we reduce the problem to about 500 tokens per second. I'm not uh going to dig too much uh on how we do train these codecs but obviously first we train them uh we train them by reconstructing a very large set of audio and using a

**[12:23](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=743s)** bottleneck here uh the the training procedure constrained uh the reconstruction to go through a step where each frame is u decomposed into several tokens. uh to do this typically it's guided so that the model drops the information that is useless and only retain the one that is uh useful and so we guided via some losses uh reconstruction losses uh adversarial losses and uh particularly like for for the for some of the tokens we try to make sure that they contains the text information so you can reconstruct the text from it. Still 500 tokens per second is a lot of

**[13:12](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=792s)** tokens. Uh and you you could put them one by one aligned as a sequence like this. Uh but it would make a lot of step of the main transformer that is uh at the core of the system which is you it's huge. Um in our case it's 4 billion parameter sorry which is which is still a lot even though it's not like extremely big now. Um what most people do then uh is uh have having one step of the backbone per frame and a smaller model here uh typically a dev transformer that um recomputes all the the tokens of one frame. uh at at each step. So this way you still have a lot of tokens, you

**[14:04](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=844s)** still carry a lot of information but the computation is much faster. So this is the the main uh pattern that we see. Uh even though for that last bit like the model we release does not follow this pattern, we actually uh defer on that part. I'm not going to dig too much on it, but just so you know, each frame which is represented by 37 tokens in our case, we do generate these 37 tokens at once using a diffusion model. So it's slightly different from the the vanilla text to speech nowadays. I encourage you by the way to read our technical report which contains all this information. Uh also it's a pretty cool uh use case of flow matching uh models which is similar to diffusion model.

**[14:53](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=893s)** Uh now the the main part is conditioning actually uh because so far we're just generating audio but we are not conditioning it on text. So it's not really a text to speech it's just speech um and to conditioning there for conditioning there is way more variance across labs and papers and implementations. Um you have typically two categories. uh there are the the people who focus on uh producing the audio once you have the the text and some of who focus on having a stream of text. Typically the first category will tend to provide all the context at the beginning and then produce the audio as we saw. Um and typically the second category will also

**[15:42](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=942s)** add some context as the audio is is produced. uh the model we release is in the first category. So what we do is we provide the audio of the voice we want to clone. So a few seconds then the text to pronounce uh and that's our context in our case. Um yeah, regarding the latency, so it it's pretty fast. Uh if you remove the network and with a single GPU, you have 17 milliseconds between the moment where you input your text and the moment where you have the first audio you can play. Uh regarding realtime text input stream, uh which uh is our next step for us. uh there is no uh real there is no clear

**[16:33](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=993s)** there is not a clear winner first uh it's still possible you know like to to generate independently the text and and stitch them out but obviously you will have a lot of continuity problem um and there are several patterns the two main ones are people who interle audio and text so as soon as there is a new text they they put the text in the same uh layer uh and some other who have a dual stream architecture where you have a stream of audio and a stream of text uh and you kind of blend them together during the um the inference. Um how am I doing on time? That's there's two minutes remaining. Thank you. Uh the takeaway is uh check our uh open source model please uh read the the

**[17:23](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1043s)** technical paper and I hope you learned a few things today. WE DO HAVE two minutes. Uh how you spend them is up to you. Yeah. >> Um you said that your model first takes hold of the text and then produce the audio. But on the example that you showed of the voice agent, it seemed like it was generating the text and the audio at the same time. >> No. Um so the question was like hey on the demo it looks like we are generating the text and the audio at the same time. Um, no. For the for the voice agent. Hello Paul, it's me again. Can you say anything like I don't know a poem? >> I'm afraid I can't recite poems. >> It's just so the text is produced in one

**[18:10](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1090s)** go. It's just that I'm using a small LLM that is very fast. So it it's nearly immediate and then the audio is uh is produced later. >> Yeah. Yeah, >> thanks for model by the way. I know that the weights are open. Is the voice cloning also open? >> Yeah, there is a small asteris here. Um, we we didn't release this part like the the encoder part. Uh, which means it's the only thing that is missing for you to clone your own voice. uh it's a feature that we only serve like uh in a proprietary fashion for now. So what you can do is

**[18:59](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1139s)** use the texttospech model, use one of the open voices that we provide. Um we may provide more uh in in the future. Uh yeah, so far we just didn't want to give everybody the ability to clone any voice. >> Yeah. architecture like what's your take on >> what's my take um so on the consumer side you will always have the impression

**[19:50](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1190s)** to speak to a single system that hear what you say and output something right so it's purely an architectural uh model here. Um my take on this is that we can go very very far by just using speech as an interface. Uh especially because these central LLM they are extremely capable but they also do a lot of things. Uh so just for the sake of being able to use any agent that has been released uh with the same interface it has an advantage uh you know to uh to interface. So you can you can go very far with just interface especially if you are uh doing this kind of thing where you stream the uh the text token that's are output by the LLM.

**[20:41](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1241s)** >> Yeah. Last question because I'm out of time. Sorry. >> Yeah. So the next steps on the inter function which accepts both audio and text sounds that real time what do you see is the possibilities with that feature. >> Um no so so I I I didn't say that our next step would be this right I I just said that there are several patterns to handle a stream of text as input as opposed to like a finite amount of text. uh we actually don't know which one we'll we'll choose. So whether it's interled or another solution like uh delayed uh sequence modeling for instance so it's unclear which architecture is best at least to to us at least to me. Uh what it what it

**[21:29](https://www.youtube.com/watch?v=3jGAU2sbAyY&t=1289s)** allows is lower latency because as soon as you have the first bit of text that are produced by the LLM you can start voicing them out. So you you it in this agent that was not clear because the the utterance were very short. But imagine I ask Paul to generate a full page of text. Um it it would be nice if I don't have to wait the end of the text generation to voice it out. >> So it also kind of >> Yeah, absolutely. Yeah. >> Thank you.
