---
id: wTiumem5TOw
title: "Kris Efland, Deepgram: From Speech to Action: Building the Next Generation of Voice AI Agents"
slug: kris-efland-deepgram-from-speech-to-action-building-the
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 15
published_at: 2026-09-29T17:56:40Z
video_id: wTiumem5TOw
url: https://www.youtube.com/watch?v=wTiumem5TOw
youtube_url: https://www.youtube.com/watch?v=wTiumem5TOw
tags: []
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Kris Efland, Deepgram: From Speech to Action: Building the Next Generation of Voice AI Agents

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=wTiumem5TOw) · [Conference site](https://aiconference.com/)

## Description

Kris Efland, VP of Engineering, Deepgram

From Speech to Action: Building the Next Generation of Voice AI Agents

Voice AI is taking us beyond transcription and text-to-speech to become the true interface for autonomous agents. This session explores the product and technical innovations required to turn speech into structured, actionable real-time intelligence. Kris Efland, VP of Engineering at Deepgram, will share lessons from deploying large-scale voice AI systems that combine ultra-low latency speech recognition, dynamic model adaptation, and conversational orchestration. Attendees will gain a roadmap for building voice agents that can listen, understand, and act -- bridging the gap between human conversation and AI-powered decision making.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,097 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=wTiumem5TOw&t=2s)** Up next, we are going to hear from Cris Aland, VP of engineer at Deep Graham with the talk from speech to action, building the next generation of voice AI agents. Welcome to the stage. >> Hi everybody. Nice to meet everyone. Uh I'm Chris Effin. I lead engineering at DRAM. Uh today I'm going to talk to you about the shift from basic voice interfaces to real-time production grade voice agents. At Deepgram Graham, we believe the future of AI isn't just about perceiving speech. It's about acting on it. From phone calls to drive-throughs, voice is rapidly becoming the most natural way we interact with machines. But delivering on that promise requires a new kind of infrastructure. It's real time streaming first with deeply integrated native

**[0:52](https://www.youtube.com/watch?v=wTiumem5TOw&t=52s)** voice foundational models. I'm going to walk you through what it takes to get there, the challenges we see across industries, and what breaks when teams try to scale their solutions, how to move from a working prototype to an operational and capable voice agent. So, Deepgram builds the foundational AI stack that makes voice possible, endto-end deep learning, scalable infrastructure for massive data handling, and the ability to train and host thousands of models. Our goal is to create the foundational AI that can perceive, understand, and interact through speech. Voice is core to our experience as humans. There over a billion voice interactions happening in enterprise every single day. From call centers to sales meetings to medical appointments and drive-throughs, this is happening at

**[1:42](https://www.youtube.com/watch?v=wTiumem5TOw&t=102s)** a massive scale. These use cases are all being transformed today by our customers and our partners using real-time voice AI. We power telefan and contact center platforms, service assistant agents, customer co-pilots, complex medical transcription and pronunciation, and even drive-through voice agents. But building this tech reliably is where it gets really tricky. So customers building voice agents often tell us the same things. Speech is high volume. It's error sensitive and timing is very critical. Perception, quality, and cost are the hardest three problems. Voice isn't just text with audio. It introduces turnt, emotion, intention, and a deeper kind of

**[2:31](https://www.youtube.com/watch?v=wTiumem5TOw&t=151s)** human interaction. What I mean by that is that we are talking about human behavior. Humans multitask, right? We take turns. We apply and synthesize context and express emotion. And we do it all in real time. When a customer begins interacting with a voice agent, the human mind is conditioned to implicitly expect the AI to mimic these dynamics while still being functional and efficient. That's a tall order. And that's also the problem. Most voice systems today struggle with fluid turn taking, detecting interruptions, responding with context and real-time responses, or taking actions as they end

**[3:20](https://www.youtube.com/watch?v=wTiumem5TOw&t=200s)** up being just an audio tour guide repeating off information that they already have stored. This is what makes voice so uniquely challenging. It's not just about accuracy or annunciation. It's really about human behavior. So let's talk about the typical journey teams go through when they're building these voice agents. In the prototype phase, the focus is on speed. Uh the focus is just on speed, right? You want to get something to work. Teams often put up with high latency, missed words, or brittle pipelines because they're focused on just getting the concept working. But once you move into production, things start to change. You need barge detection. You need end of turn handling. You need higher accuracy. And you have a need to have a much tighter feedback loop. At scale though,

**[4:09](https://www.youtube.com/watch?v=wTiumem5TOw&t=249s)** the bar gets even higher. You need sub 200 millisecond latency. Compliance ready deployment options become mandatory. Full observability and orchestration across your speech and reasoning reasoning layers is fundamental. Voice is not like other interfaces. It requires a purpose-built stack that solves the unique challenges with voice. So to solve this you need more than just accurate speech and text models. You need runtime orchestration which includes turnt logic interruption handling pro prompt contextualization or rewriting. You need async processing and h to handle function calls to stream in the relevant data. And these are really table stakes for truly fluid real-time

**[4:59](https://www.youtube.com/watch?v=wTiumem5TOw&t=299s)** interactions. Without them, your agent will feel robotic and the experience is going to feel clunky and slow and it's going to frustrate your customers. So, Deepgram has created an endto-end voice platform across all of these capabilities. Realtime transcription, natural and customizable voices designed for interruption handling and end of thought detection with ultra ultra low latency. This also includes a full set of event hooks to trigger downstream logic instantly, allowing voice agents to take multiple actions behind the scenes quickly as the conversation is happening. We offer domain specific accuracy across complex industries and subsecond latency, which is critical for natural conversations, not just a pretty voice. Above it all, we're built for

**[5:48](https://www.youtube.com/watch?v=wTiumem5TOw&t=348s)** enterprise use cases and our platform scales with for very high concurrency without any degradation. We offer self-hosted deploys to meet privacy requirements of healthcare and financial services. And we understand how to accurately transcribe alpha numeric and complex terms even with background noise in addition to meeting our global customers varied security requirements across every major go. So, our unified voice agent API was architected with your use cases in mind, allowing the agent to seamlessly listen, think, and speak. You can start streaming your audio in, and the Deepgram voice agent will leverage Deepgram's speech to text to listen. That text output is leveraged by your LLM of choice to produce a thoughtful

**[6:36](https://www.youtube.com/watch?v=wTiumem5TOw&t=396s)** response using Deepgram's customizable and natural sounding voices. Depending on your use case, you then need to tie in your business logic into your agent and provide additional actions to integrate with your other systems. Well, what while I described was happening under the hood, all of this complexity is completely abstracted away for you and orchestrated within a single API interface. Rather than stringing those listen, think, and speak functions together to build your own voice agent, Deepr handles all of this for you, producing a true speech-to-pech experience. Voice needs to be evaluated differently than text. So recently we introduced the concept of vaky vaqi. So this is our voice agent quality index and this tracks

**[7:26](https://www.youtube.com/watch?v=wTiumem5TOw&t=446s)** uh latency interruption rate and response coverage. These are measures that we feel are reflect the real world usability of an agent. This helps our customers benchmark agents where it actually matters. Enterprises also need voice infrastructure to run where they are. Public private cloud onrem dedicated endpoints. We support all of it with deep dedicated and our EU and APAC hosted endpoints. This is crucial for regulated industries and global operations. So, let's get started with our demo. All right.

**[8:17](https://www.youtube.com/watch?v=wTiumem5TOw&t=497s)** So, here is our medical voice assistant. So, let me turn it on. Hi. Let's switch to drug dispatch. All right. I'd like to start a new dispatch. And the patient's name is John Jones. His medical record number is ARV643R2. Uh the medication name is methtoresate. The dosage is let's say a thousand grams a day. Uh and the pharmacy is the CVS on market in San Francisco. >> What is the frequency of the medication? >> Yeah, let's go ahead and dispatch the drug. >> The drug has been successfully dispatched.

**[9:03](https://www.youtube.com/watch?v=wTiumem5TOw&t=543s)** >> Let's switch to clinical notes. What is the patient's name? >> The patient's name is also John Jones. Uh his date of birth is November 1st, 1986. Uh he's a male and his medical record number is ABC ARV16453. >> What is the date of visit? >> The date of visit is October 31st, 2025, 10:30 a.m. This is a standard check-in. uh and the provider is uh Etna. So you get the idea, right? It's working in real time. Okay. Lastly, I want to talk about not just what is here today, but I want to also talk about what we're

**[9:50](https://www.youtube.com/watch?v=wTiumem5TOw&t=590s)** working on next as we are making some huge advancements uh in the nextG speech architecture. So today the current approach is is what we call a cascade. So it's basically sequential processing with text conversion. So this applies speech to text, then you put an LLM in the middle and then you have text to speech back out. So this cascade uh works with both single mode or multimodal models. While this approach works very well with many of today's use cases, it does result in some loss of emotional and contextual nuance. So we're leading the way towards the fully a fully endto-end speech-to-pech architecture where instead of cascading text through the various components, we do direct conversion uh via latent space embeddings. This new

**[10:40](https://www.youtube.com/watch?v=wTiumem5TOw&t=640s)** architecture will pass through through it will pass through intonation, pacing and full context inside the conversation. Here you see two graphics of the word hello. The top one is represent they're both represented of the utterance 15,000 times. With the current approach, it's a single representation. Everyone speaks the word and then we convert it into text, right? It only comes out to one way. H E L L O. With the new architecture we're building, you can see the 15,000 different distinct points on the bottom draft representing the full attributes of someone's voice. This, in other words, it's a full human-like representation of voice, showing how intonation, pacing, emotion, and context are all preserved all the

**[11:27](https://www.youtube.com/watch?v=wTiumem5TOw&t=687s)** way endto end. So, let's just zoom in a little bit and talk about how Deepgram is uniquely building observability into the fabric of our endto-end speech-to-pech architecture, which we call Neuroplex. This isn't just a single model. It's a modular stack where each major stage in the voice pipeline has adapters between components. Automated speech recognition, large language models, and custom voices. What makes this powerful is that each of these components and each adapter exposes intermediate hidden states with debugging capability that lets us inspect outputs at any stage. That means we can trace, measure, and improve not just the final result, but what happens at every step along the way in real time. Neuroplex logs when audio is being received, when the system is

**[12:16](https://www.youtube.com/watch?v=wTiumem5TOw&t=736s)** listening, when it's thinking, and when it's speaking. It tracks how long each stage takes down to the millisecond and surfaces issues like latency, latency spikes, margins, or miss turns. This level of observability will be essential for the future. If you're building real- time voice first systems, you can't afford black boxes. You need to know what's happening, when it happens, and why. And that's why we've built Neuroplex. So, I want to close with five takeaways for anyone thinking about deploying these real-time voice agents at scale. The first one you got to keep in mind is voice is not text. It's it's often noisy. It's frequently multilingual. and the assumptions you made about building chatb agents just don't hold up. You can't change human

**[13:04](https://www.youtube.com/watch?v=wTiumem5TOw&t=784s)** nature. Second, orchestration is critical to get to sub sub 500 milliseconds round trip from your LLM. Latency isn't about model speed alone. It depends on how tightly your speech and reasoning layers are all integrated and coordinated. The third accuracy isn't enough. You could have the best transcription in the in the world, which is ours, but if your agent cuts people off or can't recover from an interruption, the experience falls apart really, really fast. Number four, you need new metrics. The industry uses a a term called WER, word error rate, and it's fine for transcription. But for agents, you need to track real world behavior. Latency, interruption rate,

**[13:54](https://www.youtube.com/watch?v=wTiumem5TOw&t=834s)** uh response coverage. These are all critical in terms of understanding how agents perform uh in your enterprise and against one another. And then the the final one is deployment flexibility is essential. Enterprise voice agents need to run in both public and private clouds on prem or in mission or region specific environments. This affects both compliance and the user experience. So these are the principles we we've succeeded with across multiple industries from healthcare to call centers to drive-throughs. This is the ML playbook, MLOps playbook for voice. So if you want to play with this tech live, please visit our playground. Uh you can scan the QR code here and you can you can play with this yourself if you want to do it live today uh at the booth and come talk to us. We're at 232

**[14:44](https://www.youtube.com/watch?v=wTiumem5TOw&t=884s)** uh and we've got it up and running and you're more than welcome to come play with it. Thank you so much for your time. [Applause]
