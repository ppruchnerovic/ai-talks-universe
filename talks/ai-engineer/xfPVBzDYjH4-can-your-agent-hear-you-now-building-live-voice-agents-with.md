---
id: xfPVBzDYjH4
title: "Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff"
slug: can-your-agent-hear-you-now-building-live-voice-agents-with
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Thor Schaeff"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-10-11T15:00:22Z
video_id: xfPVBzDYjH4
url: https://www.youtube.com/watch?v=xfPVBzDYjH4
youtube_url: https://www.youtube.com/watch?v=xfPVBzDYjH4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Gemini", "Gemini Live API", "Google DeepMind", "voice agents", "real-time AI", "speech translation", "Live Translate", "Lyria 3", "Nano Banana", "Interactions API", "Google AI Studio", "multimodal AI", "text to speech", "Thor Schaeff", "AI Engineer"]
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff

**Thor Schaeff**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Gemini` `#Gemini Live API` `#Google DeepMind` `#voice agents` `#real-time AI` `#speech translation` `#Live Translate` `#Lyria 3` `#Nano Banana` `#Interactions API` `#Google AI Studio` `#multimodal AI` `#text to speech` `#Thor Schaeff` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=xfPVBzDYjH4) · [Conference site](https://www.ai.engineer/)

## Description

An agent that hears you, sees you, and answers in your language, in real time. Here's how to build one with Gemini.

Thor Schaeff, who works on developer experience at Google DeepMind, runs a set of live demos of Gemini's real-time and media models. He builds an illustrated story with Gemini Live and a fast Nano Banana image model, using the stateful Interactions API to keep characters and style consistent between images. He has the audience scan a QR code to hear the talk in their own language with Gemini 3.5 Live Translate, then calls up an AI radio DJ that uses Lyria 3 to generate a reggaeton track on request. He explains how the Live API works: a stateful WebSocket session that takes in text, audio and video and streams back audio plus a transcript, using a native audio model rather than a speech-to-text and text-to-speech pipeline. It supports 90 languages, interruptions, tool calls and Google Search grounding. He ends with a voice and vision demo in Google AI Studio.

In this talk:
• Chaining image generations with the stateful Interactions API
• Near real-time speech translation with Gemini 3.5 Live Translate
• A voice agent that calls tools, like Lyria 3 for music
• How the Live API works: native audio, barge-in, tools and 90 languages

SPEAKER
Thor Schaeff, Developer Experience, Google DeepMind
X: https://x.com/thorwebdev

LINKS
Gemini Live API docs: https://ai.google.dev/gemini-api/docs/live
Interactions API docs: https://ai.google.dev/gemini-api/docs/interactions-overview
Gemini 3.5 Live Translate: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/
Lyria 3 for developers: https://blog.google/innovation-and-ai/technology/developers-tools/lyria-3-developers/
Google AI Studio: https://aistudio.google.com

CHAPTERS
0:00 Intro
0:56 Guess the model: Gemini TTS
2:01 Meet Thor
3:15 What shipped today
3:45 Demo: an illustrated story canvas
5:42 The Interactions API
7:07 Demo: Gemini Live Translate
10:21 Gemini 3.1 Flash Live
10:56 Demo: an AI radio DJ with Lyria 3
14:13 How the Live API works
15:07 Native audio, not a pipeline
16:06 Partners: LiveKit and Pipecat
16:31 Try it in AI Studio
17:55 Demo: voice, vision and Mandarin
19:42 Wrap-up

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,902 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=12s)** Can you hear me? Fantastic. Hello everyone. Well, hello couple people that wandered in. Um, I'm sorry the schedule has been changing around. I'm sorry you didn't find the quiet working area you were looking for. All right. Um, we are looking at some agents with Gemini API. Now, before we kick off, let's have a little listen to this. Welcome one and all to the grandest stage on Earth. You're standing right at the heart of the largest AI engineer World's Fair in history. Let's build the future together, shall we? Does anyone know what model that is? Yeah. You you you you're not allowed.

**[1:04](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=64s)** Anyone else? Anyone know which model? No. Any guesses? It starts with G. Gemini. Yes, it is a Gemini model. But which one? No, it's not life. That's incorrect. Yes. This is Gemini TTS. Is that what you were about to say? No. Okay. Um, so Gemini text to speech. Uh, actually a really incredible model for expressive speech. You have inline audio text you can steer it with. Um, you can stream the speech. It's a lot lower latency now than it used to be. So uh if you are in the market for some speech uh text to

**[1:55](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=115s)** speech that is Gemini TTS is a good model. Now let's have a look at uh some of the things we're doing today. Uh first of all my name is Thor. I work on the developer experience at Google DeepMind. So that mostly includes Gemini API and Google AI Studio. So if you're using the Gemini models through the API, uh you know, let me know if you have any feedback. I have my colleague Philip here as well, uh who's working on managed agents on the API. So if you're using that, uh let us know as well. So this is a bit of a a prelook at the workshop we're doing tomorrow. Um so tomorrow we'll do kind of Gemini API especially focused on um live agents uh

**[2:45](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=165s)** conversational agents real time uh conversational agents multimodal real-time conversational agents we're just packing everything in there um and so what we can look at actually there's uh been a lot of things that shipped and so specifically what we want to look at is the multimodality of Gemini and the gen media models Uh so actually this slide is already out to date because this morning we shipped a new model uh that is called anyone know which model did we ship? We shipped Omni Flash which is uh a video generation and editing model and we shipped Nano Banana Light. So Nano Banana Light is a really exciting model because it cuts down the latency of image generation and image editing quite

**[3:34](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=214s)** significantly. And so what I've done, we'll we'll do a couple demos here. Uh and one of the demos is um this example here, which I call the uh Gemini Nanobanana story canvas. Uh and I just VIP code this up uh just recently and I'm having some trouble with my mouse here. Um but so what we can do is we can come up with a story with um Gemini Life and then have it use Nano Banana Light to to illustrate that story for us. So anyone you know this is a little bit like improv theater now. Anyone has a story line they want to start with? Where are we somewhere? Okay, let's say um we're in Taipei in the 1980s.

**[4:27](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=267s)** The neon lights of Taipe's night market pulsed with an almost magical energy reflecting off the wet pavement and the chrome of passing scooters. Rain had just passed, leaving a humid mist that hung in the air. Amidst the throng of shoppers and vendors, a young woman clutched a small, strangely glowing object under her jacket. Something very exciting happened in 1980s Taipei. A new kind of drink emerged. She paused at a stall where a man was vigorously shaking a metal cup, creating a frothy, milky concoction. He handed a cup to a customer who took a long sip with wide eyes, savoring the strange tapioca pearls at the bottom. This was the birth of bubble tea, and its sweet, chewy magic was spreading like wildfire. So what you can see here is uh from the

**[5:20](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=320s)** tool call. So Gemini Life is getting a tool call um and then it's using the Gemini interactions API to generate an image on the fly. Now it still takes kind of you know two to three seconds for the actual image generation but that is um pretty impressively fast. And um what you can look at is if you're looking at the code here uh we're using the interactions API. And so the interactions API is exciting because it is a stateful API which means we can chain our interactions very seamlessly. So you could see here the first image generation that we were doing uh it didn't have a previous interaction ID but then the next generation that we were doing we're passing this previous interaction ID to the interactions API

**[6:11](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=371s)** which means that we have the previous context of the previous interaction and we can continue that in the generation. So what that means specifically for our demo here is that you can see is our first you know interaction uh it generated an image with a very specific kind of visual feeling and also with characters right and so we can continue that interaction and so we can keep the same consistency kind of across these generations. So if you haven't tried out the interactions API, uh it is our unified API for interacting with all of the Google DeepMind models as well as agents. Uh and so do try that out. It is a it is a really really cool um way to interact with everything that Google DeepMind has. Okay, so this was you know a bunch of

**[7:00](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=420s)** things that happened. Um so this was kind of on the Gen Media side. We shipped uh Nano Banana Light this morning. Now, we also recently shipped on the audio side our live translation model. Has anyone tried out Gemini 3.5 live translate? Yes. Okay, a couple folks. Uh, that's fantastic. So, what we can do is uh we can try that out as well. We can play uh a little demo. And so what I'm going to do here is I'm going to create this live translation session and I want you to scan uh this QR code on your phone. And so what this is doing here is if I now enable um my microphone. So this is getting the the microphone of my speech

**[7:49](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=469s)** um here into the session. And now if you go in and you select your preferred language. So we're seeing here we're getting some German. So someone is listening to me now speaking in German. And so if you are uh now listening to this, so you probably need some headphones. So if you have some noiseancelling headphones, you can now listen into this talk in your preferred language. And so Gemini live translate is a really incredible model. It's near realtime translation. So as I'm speaking, as soon as the model is recognizing kind of the context of what I'm speaking about, uh it will then start translating in real time to your desired language. So I see someone is listening in there. Do do you get some audio out? Can you hear it? Yeah. Does

**[8:38](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=518s)** it sound good? Fantastic. See, um, so this is this is really exciting because you know in a conference like this obviously we have a very very international audience and so I can speak in my preferred language. So I could switch to German now for example. the powerful Gemini live translates. Um, it is a a really incredible model. Um, it automatically detects the language the speaker is speaking and then translates it in real time uh into our preferred language. Okay, we have uh a

**[9:27](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=567s)** very international crowd here today. Uh, who's listening in in uh Chinese? Are you listening in Chinese? Oh, okay. I didn't understand that, but okay. Um, so that is Gemini live translate. Um, if you want to try it out, you can add it to your um applications now. It is available on the Gemini API. So, do try that out. uh it is a really incredible model and uh would love to hear kind of what you're what you're building with that. Now obviously we're looking at uh agents, right? Can your agents uh what's it the title of this talk? Gemini made up this title. So I uh can your agent hear me

**[10:16](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=616s)** now? I think that that is the title. So our most recent real time conversational model is called Gemini 3.1 Flash Life. Now, if you've talked to Gemini before in the Gemini app, that is exactly the model that you're speaking to. And so, we can do a little demo here. So, this demo was vipcoded by Gemini in Google AI Studio. And if you remember the good old times, you know, when you were listening to radio, you know, not too long ago, you could phone up the the the radio host and you could ask for a song, right? You could wish for a song. So, it's the same idea here. We're using Gemini Life to be our radio DJ and then we're giving Gemini Life an API, a function call to the

**[11:06](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=666s)** Gemini API to then use LIA 3, which is our music generation model to then generate some music for us on demand. Okay, let's uh try this out. We're we're just going live demo to live demo here. Let's let's see. Well, hello there. You're live on the live jukebox right now. What absolute banger are we cooking up for you today, mate? To get this track properly sorted, I need a bit more of an idea. What genre are we thinking? Upbeat synth pop, smooth jazz, something with a bit more well. And what's the vibe lyrics-wise? Give us some details. >> Yeah. Can we get like a really high energy ragaton, please? About the AI engineering world's fair here in San Francisco. >> Now that sounds like a proper belter, mate. high energy regaton about the AI

**[11:54](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=714s)** engineering world's fair. Brilliant. Right. To make this absolutely top of the pops, any specific bits of tech or big names you want thrown in, or are we just going for that huge festival vibe? >> Yeah, just surprise me, please. You got it, my friend. Prepare for a huge musical surprise generating that track right now. Mixing that regaton rhythm with the tech buzz for the World's Fair. It's going to blow your headphones off. Fair. What a feeling. Let's go on the floor. Neural networks firing up. Groundbreaking for sure. Clever algorithms dancing. Tech pioneers mingling. This is innovation. Baseline is pulsing heavy. Can you feel the heat? Sin stabs electrifying. Move in your feet. This is how we are.

**[12:50](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=770s)** Yeah, that that was pretty cool. You went multilingual there as well. Nice one. Cheers. >> Cheers, mate. Glad you like the flavor. Keep those big ideas coming. This jukebox never sleeps. What are we spinning next then? Feeling. >> All right. Um, yes, you can try this out yourself. Uh, it is is a a demo that was built in Google AI Studio. Uh so if you want you can fork this in AI studio and continue yourself. Um I know this application might not necessarily be that useful for your business context, you know, if that's something you're looking to do, but I think the individual components are definitely useful. So if you're building real-time conversational agents, uh you know, you want them to be

**[13:37](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=817s)** multilingual, you want them to have capabilities, uh tool calls. So in this example, we were just giving the agent a tool call to generate music with LIA 3 uh on demand. Now obviously this could also just call out to your CRM and get some you know customer information or it could create you know a new ticket on the back end. Um so you know really what I want you to take away is kind of this real time multimodal conversational uh experience that you can build. And so the way that you can build with this model, so the the Gemini 3.1 flash real-time conversational model is through the life API. So the life API is a low latency real time voice and vision uh API. So you can build multiodal uh

**[14:28](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=868s)** life real-time interactions. And so what this means is you have this stateful websocket API where you create a session and then over this websocket you can send in real time text, audio and video frames to the model and the model will then respond in real time back in audio chunks. And these audio chunks you can then stream uh in your application. Uh and in addition to the audio, you also get the transcript of what was said. So if you've worked with voice agents before, this is a little bit different from kind of your cascading voice agent pipeline because this is a native audio model. So the model itself does not go through text, but rather the intelligence is baked into the audio

**[15:18](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=918s)** model. So the audio model can understand the speech naturally and natively and can then respond back in any of the 90 supported languages. So this is what allows us to to switch very fluidly between different languages. Um so kind of the key features here, yeah, multilingual support. So 90 uh different languages currently supported in the preview. Um we can barge in, we can interrupt the model, right? If our DJ is talking a bit too lengthy, uh we we can we can barge in, interrupt it, we can give it uh the tools and we have the audio transcription as well. Now, if you're building real time conversational applications or real-time um multimodal applications,

**[16:05](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=965s)** uh you know, real-time media can be quite challenging to scale. So, we have a great lineup of partners. So, you know, LifeKit, Pipecat, they all actually here in the expo as well. I recommend you go visit them. They do some really really cool stuff to allow you to get up and running quickly with the Gemini Life API. Okay, so if you're now um you know, you're like, "Okay, this sounds great. I want this." Um the easiest way to try this out is through Google AI Studio. So we spend a lot of money on this domain, AI.studio. So I do appreciate if you use that one. Um so we can get some ROI there. So ai.studioife. You can try out the model. You can talk to it and you can understand the capabilities that are available.

**[16:54](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=1014s)** So let's do that now. Uh so we're just going to AI.dev. We also have AI.dev. Um yeah, please do use that as well. That one was was also not not so cheap. Uh there we go. AI.devlife. And so here uh we can also try out the live translate model if you want to. Uh but we can here select our Gemini 3.1 flash uh live model. We can select a different voice. Uh for example, I like puck here. And then also we can enable grounding with Google search. So obviously the model is trained on a lot of information but it does not have access to real time information, right? And so by giving it access to Google search, it can actually go off and it's

**[17:42](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=1062s)** basically like a built-in function call. And if we ask it about today's weather or you know why Germany played so well in the World Cup, uh we can we can do that and it can use Google to to look that up. Okay, let's give this a try. >> Hey, can you hear me? >> Yes, I can hear you perfectly. How can I help you today? >> Can you see me? Yes, I can see you clearly. You're wearing a black shirt and a black hat sitting in front of a blue background. Anything specific you wanted to show me? >> Yeah. What does it say on my sweatshirt? >> I can see the word Gemini printed in yellow letters. Anything else you'd like me to identify? Uh, okay. I think my uh my Mandarin

**[18:48](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=1128s)** didn't work out so well there. Uh, can you also speak Mandarin, please? >> Yes, I can speak Mandarin, too. What would you like to say now? What's about? >> All right. If you don't read Mandarin, I do apologize. I was just asking the model what it has eaten, and I just said it doesn't need to eat because it's it's a model. So, uh, yeah, there we go. All right. So this is the easiest way for you to get started with uh Gemini ai.studiolife.

**[19:37](https://www.youtube.com/watch?v=xfPVBzDYjH4&t=1177s)** If you want to learn more about building with Gemini and the Gemini live API, join me tomorrow morning in uh room 2009, I think. Check the schedule. It it does change every once in a while. Uh but other than that, Dankur, thank you. Cheers.
