---
id: A-hzeIWn5BA
title: "Build multimodal agents that reason interact and take action | DEM330"
slug: build-multimodal-agents-that-reason-interact-and-take
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Henk Boelman"]
channel: "Microsoft Developer"
duration_min: 16
published_at: 2026-06-10T20:08:41Z
video_id: A-hzeIWn5BA
url: https://www.youtube.com/watch?v=A-hzeIWn5BA
youtube_url: https://www.youtube.com/watch?v=A-hzeIWn5BA
tags: ["Agents", "Build multimodal agents that reason interact and take action | DEM330", "DEM330", "DEM330_v1", "Developer", "Henk Boelman", "Microsoft Foundry", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Build multimodal agents that reason interact and take action | DEM330

**Henk Boelman**

`Microsoft Build` · `Build 2026` · `2026` · `16 min`

`#Agents` `#Build multimodal agents that reason interact and take action | DEM330` `#DEM330` `#DEM330_v1` `#Developer` `#Henk Boelman` `#Microsoft Foundry` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=A-hzeIWn5BA) · [Conference site](https://build.microsoft.com/)

## Description

Build a real-time agent with a conversational avatar using the Voice Live API in Microsoft Foundry, no slides, just live coding. See how Voice Live unifies speech-to-text, model reasoning, and text-to-speech, then wire it into an agent that can call tools via MCP to take real actions. Walk away with reusable patterns for voice-first, tool-using agents with expressive avatars.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

To learn more, please check out these resources:
* https://aka.ms/build/foundrydiscord

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Henk Boelman

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEM330 | English (US) | Agents & apps

Demo | (300) Advanced

#MSBuild

## Transcript

*2,247 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=1s)** Hi and welcome to build multimodal agents that reason, interact and take action. My name is Hengbuhlman and I'm a principal developer advocate at Microsoft. I spent my days helping developers build with AI, and lately almost every conversation comes back to one thing agents. So today, that's exactly what we're going to build. So instead of talking about it, let me just show you. This is Hank's travel agency. It's a voice agent with a face, and it can find me flights and hotels. Let me talk to it. Hello, Hank's travel assistant here. I can help plan your flights and hotels, so tell me where you'd like to go. Hi I have to go to Microsoft build in San

**[0:51](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=51s)** Francisco. I want to fly on the 28th of May 2026. Great San Francisco is on the Contoso Travel Network. I have your travel date as May 28th, 2026. What city will you be flying from? Oh sorry, I forgot to mention that I want to fly from Amsterdam. No worries, I'm updating your options to include flights departing from Amsterdam right now. Thanks. I found the daily Amsterdam to San Francisco flight for May 28th, 2026. It is flight CT0. 09 leaving Amsterdam at 2:45 in the afternoon and arriving in San Francisco at 4:43 in the afternoon the same day the. Indicative one way fare is around $755. Would you like me to add this to a trip

**[1:40](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=100s)** for Microsoft build? Yes please. Great, I'm checking the best options for you right now. OK, I have added your Amsterdam to San Francisco flight to Microsoft Build San Francisco. You leave on May 28th, 2026 at 2:45 in the afternoon and arrive at 4:43 in the afternoon. Would you like help finding a hotel in San Francisco too? Yes, I want to stay 7 days but I have a budget of $200. Can you give me two options? Sure, I'm checking for the best options within your budget right now. Sure, I searched San Francisco hotels at $200 or less per night. I found two options. Riverside Harbor Wide World is a three star hotel at around $165 per night.

**[2:29](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=149s)** Coastal Terrace Pros Wear is also three stars at around $165 per night. For seven days I would use check in on May 28th and check out on June 4th. Would you like me to add one of these? Yes, add the first one please. Got it. I'm just finalizing the details for you now, OK? I have added Riverside Harbor Wide world. OK perfect. Add the flight back please. Got it. Hank, I'm finding the best return flight options for you right now. OK, I have added your return flight to Microsoft Build San Francisco. You leave San Francisco on June 4th at 9:45 in the morning and arrive in Amsterdam the next morning at 5:43. Perfect.

**[3:15](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=195s)** Thank you very much. You're very welcome. Your Microsoft Build San Francisco trip now has the outbound Flight 7 night hotel stay and return flight. Safe travels. So quick recap, I spoke to it like a person, it answered like 1, I could interrupt it and it went and did real work finding flights and hotels, interact, reason and act in one experience. And all of that runs on The Voice live API. It is a single unified API for real time speech to speech voice agent. Instead of wiring up speech to text a model and text to speech yourself, it brings them behind one connection and handles the hard conversational work for you, the listening,

**[4:06](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=246s)** the turn, taking the interruptions. For this demo, I'm running the newest features we shipped here at Build The voice is Serena, one of the new neural HDV three voices. It understands me through the Maya Transcribe 1 integration for fast, accurate multilingual speech input. The face is Selena, one of the brand new full body standard avatars, and it all runs over a web RTC connection, so the whole conversation happens in real time straight from the browser. Now let me show you how this is built and how you can customize it in three steps. Step one is the most important part, the agent behind it all that is the brain of the wall solution

**[4:58](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=298s)** and it lives in Microsoft Foundry. The great thing is that Voice Live connects to your Foundry agent out-of-the-box. There are two kinds, Prompt agents, which are general available and hosted agents which are now in preview and as of built Voice Live for prompt agents is general available. Today I'll show you a prompt agent and it takes only a few steps to build. O let me build 1 live. I'm here in Microsoft Foundry on the top. I go to build, then agent and I click new agent and that is really it. We have an agent now we just have to shape it. First.

**[5:43](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=343s)** I pick a model. Then I give it instructions. I tell it that it is a travel assistant, and because this is a voice agent, I keep its responses short and conversational, with no markdown and no emojis, since none of that makes sense when the answer is spoken out loud. Next, I give it access to the Contoso Travel MCP server, which is where it gets its flight and hotels from. I set the agent to auto approve the MCP calls so it can call those tools without stopping to ask. And now I can test it right here in Foundry. Before I wire up any voice, let me try it. And there we go. The agent decided to call the travel tools, got the result back and gave them to me.

**[6:34](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=394s)** That is the agent doing the job with no voice yet. 2nd is the voice. out-of-the-box, you already get a lot. Voice Live ships with a huge catalog of prebuilt neural voices, hundreds of them across a dozen of languages and locales, usually with several voices and personalities per language. So before you customize anything at all, you can simply pick a voice that fits in whatever language your user speaks. The newest of these are the Neural HD voices, and we're now at Neural HD version three. What's make them special is that they're more context aware. They read the meaning of what they are saying and adjust their tone, their pacing, and their emphasis to match. So they sound less like a narrator reading a label

**[7:25](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=445s)** and more like a person having a conversation. They will pause, they will lift a question, and they will soften an apology. For this demo, I picked Serena, one of the new Neural H3 voices, straight from that gallery. No training, no setup. I just select the term. And if you want to go further, this is where it gets fun. There is a new speech model, My Voice 2, that's a multilingual and even more emotionally expressive. And if you want the agent to sound like me, I can use personal voice to clone my own voice for a short sample. So the agent does not just sound clear, it sounds on brand. Let's take a look at that. Creating a personal voice in Microsoft Foundry takes just a

**[8:15](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=495s)** few minutes. I start my Foundry project open fine tuning and create a new fine tuning task for the base. I pick Azure Speech Text to Speech. I set the type to Personal Voice and give it the name Hank Bullmann PV. First Foundry asks me to record a consent statement in my own voice. With the consent captured, I move on to recording the data that will train the voice first. Foundry gives me a few tips.

**[9:05](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=545s)** Record in a quiet room, use a good microphone and keep a steady volume. Then I can record my voice sample. Hi, I'm Hank and. Welcome to my travel agency. Tell me where you would like to go and I'll find you the perfect flight and a great hotel. Just ask and I'll take. Care of the rest. Next I review everything except the training, uses my account credits, agree to the terms and submit. Training kicks off and after a short wait hang woom on PV shows U in my list completed and ready to use. To try it out. I open a new voice in a text to speech playground and press play Hi. I'm hang.

**[9:52](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=592s)** And that's my own voice. Recreated A foundry from a single short recording 3rd to the face. This is the lifelike part, and it's my favorite. I can give it a full video avatar or I can use a photo avatar powered by Microsoft Research phase at one model. It takes a single photo and turns it into an expressive talking head. No video shoot, no training. I gave it one picture and it came to life. Let me show you how. I'm in Microsoft Foundry in the fine-tuned section and I select Create for the model. I choose Erchit text to Speech avatar. I set the type to Hoto avatar and I give it a name and a short description.

**[10:40](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=640s)** In the data step, I ick my data source. I can bring my own or I can create one with AI. Next I register my avatar talent. This need a consent video, a short clip. I select the consent video and I can preview it on the right to be sure it loaded correctly. I review the configuration and submit the job and finally processes the video and trains the avatar. When training is done, my avatar shows up in a text to speech avatar playground right next to the stock avatars. Here it is listed as Hank one. Then I pick a voice and here I'm using my custom personal voice, the one from a moment ago. I type what I want the alvater to say and

**[11:28](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=688s)** select Generate. When it finishes, I switch to the generated video tab to see the result and I can download it right from the file list below. Hello, I'm Hank, your travel. Buddy and that is the whole thing made personal, my face, my voice from a stock alvater like Selena all the way to Hank 1. So let me bring it all together. This is the exact same demo you saw at the start. Hank's travel agency. The same agent, the same voice, live connection. The only thing I've changed are the voice and the face. The avatar is now Hank Wan, the one I just trained, and the voice is my own custom personal voice. Let's take a look.

**[12:22](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=742s)** Hello, Hank's travel assistant here. I can help plan your flights and hotels, so tell me where you'd like to. Go Hi, I would like to go to New York next weekend. I want to leave on a Friday and return on a Monday. I'm travelling from Amsterdam and I'd like to have a cheap three star hotel. Got it. I'm searching for affordable three star hotels and flights from Amsterdam to New York for your Friday to Monday trip. Got it. Amsterdam to New York, leaving Friday and returning Monday with a cheap three star hotel. The daily outbound flight is around $535. It leaves Amsterdam at 7:15 in the evening and arrives

**[13:14](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=794s)** in New York at 8:43 that evening. The return is around 615 dollars. It leaves New York at 6:45 in the evening and gets into Amsterdam the next morning at 8:13. For hotels, the cheapest 3 star option is Skyline Square Adventure Works at around $155 per night. Which Friday and Monday dates would you like me to use? I would like to go next weekend. Thanks. Since today is Thursday, I understand next weekend as leaving Friday, June 12th and returning Monday, June 15th. Would you like me to put together the trip with the Skyline Square Adventure Works Hotel for those? Dates.

**[14:01](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=841s)** Yes please. Got it. I'm checking the best options for you right now. OK, I have added everything to Hank. New York Weekend You fly Amsterdam to New York on Friday, June 12th, leaving at 7:15 in the evening. You stay at Skyline Square Adventure Works from Friday, June 12th to Monday, June 15th. Your return flight leaves New York on Monday, June 15th at 6:45 in the evening and gets into Amsterdam the next morning at 8:13. Sounds awesome. Thank you very much. You're very welcome.

**[14:48](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=888s)** Have a great weekend in New York. And there it is, same agent, same capabilities, but now it looks like me and it sounds like me. And that is the wall point. You build the agent once and then you can make it yours. So that is how you build a multimodal agent, that the reasons interact and takes action. We started with an agent in Microsoft Foundry. We gave it a voice and a face and we brought it all together with voice life in real time, speech to speech. And the best part is how little of this you have to build yourself. The hard conversational work is handled for you, so you get to focus on the experience.

**[15:37](https://www.youtube.com/watch?v=A-hzeIWn5BA&t=937s)** If you want to try this yourself, everything from the session, the Agent of voices, the avatar, you can access it at AK Delta Mesh slash build 26 slash demo 330. Thanks for watching Reason interact act. Now go build one that's yours.
