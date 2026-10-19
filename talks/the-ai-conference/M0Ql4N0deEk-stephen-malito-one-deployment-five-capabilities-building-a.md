---
id: M0Ql4N0deEk
title: "Stephen Malito: One Deployment, Five Capabilities: Building a Production Voice Agent on Edge Compute"
slug: stephen-malito-one-deployment-five-capabilities-building-a
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 14
published_at: 2026-10-13T18:29:04Z
video_id: M0Ql4N0deEk
url: https://www.youtube.com/watch?v=M0Ql4N0deEk
youtube_url: https://www.youtube.com/watch?v=M0Ql4N0deEk
tags: []
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Stephen Malito: One Deployment, Five Capabilities: Building a Production Voice Agent on Edge Compute

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=M0Ql4N0deEk) · [Conference site](https://aiconference.com/)

## Description

Stephen Malito presents “One Deployment, Five Capabilities: Building a Production Voice Agent on Edge Compute” at The AI Conference 2026.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,210 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=5s)** Thank you so much, Pete. Appreciate it. Yeah, so hey, one deployment and five capabilities because Telnyx has a lot of capabilities. Uh so, we'll do a little bit of an intro on Telnyx before we get deep into this because the backstory is very important for what we're going to talk about when it comes to voice AI. So, Telnyx got their start about 15 years ago just trying to become a telecom carrier. So, just basically in the voice space, doing minutes, setting up PBXs, and setting up SIP trunks to other voice systems. Fast forward a few years, we got into the messaging game. We got into the CPaaS game, building a API on top of this global telephony infrastructure that we had built over the course of that time. Um we became a licensed operator in something like 65 countries. Uh in the

**[0:54](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=54s)** United States, we are a real carrier, and that means that we have direct interconnections to companies like AT&T, Verizon, and T-Mobile. Um as AI was really blowing up over the last couple of years, uh we did the dive. Uh we started buying GPUs, and really what we started doing that was different is we stood up that infrastructure right next to our telephony infrastructure. So, all our models or all the models we host running on our GPUs next to telephony allowed us to build extremely low latency voice agents. Uh especially when it comes to running these agents that touch the public switched telephone network. Um as we continue to expand, uh we exploded that globally. So, we have these data centers live in something

**[1:41](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=101s)** like uh seven countries and around 20 data centers total at this point. Uh so, there we were, we got voice agents, everything's cooking, but now there's a new problem. Um companies need middleware, they needed do uh various data transactions or modifications in order for these AI assistants to run cleanly. So, we moved into the edge space and building out the capability to run what we're going to call stateful actors as we get into this. Databases, KV, and then more primitives like the STT, the TTS. So, let's get cracking here. Um we're going to try to do a live demo, but the Wi-Fi has not been awesome to me. So, I have two agents running right

**[2:30](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=150s)** now, well, racing to see who's going to get this deployment done first. And we'll we'll go check in on them as we as we go through here. So, our our one deployment and five capabilities killing this FrankenStack. It's almost October, people. It is almost Halloween season. So, we dubbed the FrankenStack. Those that are out there who are building with AI and they're running all of their services across all of these various clouds. So, you've got your LLMs running with OpenAI, you're using Twilio for PSTN connectivity and for mobile mobile SMS connectivity. You've got your STT going over to Deepgram, you've got your TTS going over to Cartesia, and then you're lost as to where everything ends up. So, entering in Intellanex, we

**[3:19](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=199s)** can just take care of all of these things for you. You know, the thing with voice agents, like they always work in the demo. Production is is always a challenge as all of us builders know. You got to deal with Murphy's Law, we got to deal with different stakeholders that potentially didn't give you all the information you needed to build the agent. And so, you know, what you could do in a weekend, you know, you want to answer a call, you want to send an SMS, and then maybe you want to email a transcript of that call. That's five, six different vendors, different dashboards, different logging tools. Then you got to run OpenTel, Grafana to join all the logs together and get some sort of clear observability as to what's happening with your agents. So, we're running everything real here, real

**[4:08](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=248s)** traffic. We got sub-200 millisecond round trip times because we own the network, we own the data centers. Everything with us is carrier grade. We're deploying B300s like absolute madmen. And every single time I'm talking to the CEO, he's like, "Oh yeah, 40 more get deployed today, 150 more next week." It's just one owner with us when something breaks, and we make it really easy for us to contact us when there are any issues. Many clients, we spin up Slack channels and make communications very clear and very simple. So, all these layers we're going to talk about. So, one with Edge Compute, what we're going to call the physics layer. Um, but models get faster, you can't beat physics. So, on Edge Compute, you can host the code for your agents, your

**[4:55](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=295s)** persistent actors. Uh, we allow you to host these stateful actors. They're kind of like a, you know, a Cloudflare durable object, single-threaded server with its own SQLite database attached to it. It supports very popular frameworks like LangGraph, CrewAI for cell AI agents. Something else you want to run on there, you just come talk to me and and we'll see what we can get done. Um, then we go into the agent platform. Um, so that's where we have the voice AI capabilities, STT, TTS, and the orchestration. Uh, and then lastly here we're talking about ownership, uh, and that's trust, and that's around Global Coms. So, being in the industry for 15 years, having all of this licensure and regulatory sorted out over the years is really hard in our organization and all

**[5:43](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=343s)** of our infrastructure, and really gives you the advantage of taking use of our carrier grade network. You know, we are stacking and racking, we're co-locating, we're owning everything we can. And that's why, you know, you've got 50 primitives on one control plane, you've got 140 countries where you can get numbers and voice, and then, you know, things like WhatsApp Business for everything in between. We support 100 languages in real time, and then it's all one API, one bill, one CLI tool for deploying. So, we're going to talk through next the voice inference SMS email edge compute. I have a demo running. We're going to go take a look at that in a minute. And I swear, you know, being a a solutions engineer, uh I always abide by by the three B's,

**[6:32](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=392s)** you know, be bright, be brief, be gone. Uh so, I'm not going to keep anybody hanging out here any longer than I need to. So, let's take a look here and see and see how we're doing on the agent side. We got a build failed, but let's check how our agent is doing. Uh so, I instructed uh Open Code to build an agent for me, so it kicked out this AI auto care agent. Uh chose a model for me, which was GLM 5.2. Um all of these hosted by Twilio Flex. Uh I also often use Kim K2.6 for for the voice agents. It seems to work really really well. Sometimes you have to tune your prompt a little bit if you're moving from Open AI or Anthropic. Uh but, I think most people are very pleased with what happens. Um this agent is for like a

**[7:20](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=440s)** auto care customer assistance. So, someone wants to call in, they want to check on their car, what's happening with their tire rotation, oil change, whatever it is. Uh we support a slew of built-in variables, as well as you can build your own. Like, known customer numbers, the phone number, the vehicle, the vehicle type, the service, and all of that. Um with every single one of these requests that comes in, uh we have the capability to have this dynamic webhook variable where we'll fire out the information collected on that initial transaction. So, like the phone number the call came in on, the caller's phone number, and then other session metadata. So, we can go and retrieve that from databases, from other cloud services to be used with this AI assistant. In addition to, you know, custom solutions like that, we also support a

**[8:07](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=487s)** number of integrations just straight out of the box. So, you don't have to go and build from scratch. So, if you're already using Airtable, you're already using Salesforce, whatever it may be, even some that might not be listed here, you may ask us about them. We we might have an integration in cooking up for it. You can also connect over an MCP server and I like to call that architecture the responder-thinker architecture. So, oftentimes we have existing agents that are performing different functions for us, but they're using like higher-level reasoning models. They're They don't respond fast enough for the the human conversation, which is like a 200-ms delay. You know, I say something to you, 200 ms, and then beyond that, oh, this

**[8:55](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=535s)** is really weird. Why is this so slow? Or any faster than that, oh, wow, is this person on drugs? So, you know, guys go out there. It's way too fast for you. I don't know what's happening. So, with the responder and thinker, Telnyx will take care of that responder function. We will talk to the patient or person very quickly, and at the same time we'll fire off that request for the MCP server, wait for a response, and then provide the information. So, it can be very, very smooth. Even with like webhook tools, we can add in like messages that will allow us to kind of provide a little bit of filler. So, we can add filler messages if we know it's going to be like 2,500 ms in order to get some transaction completed or look up some data. And it makes it more of a a natural conversation with each one of

**[9:46](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=586s)** these people that come in. So, this is our open code. He is checking on the build error. Let's see what Mies van der Code is doing here. He's my Hermes agent that's running on my Mac mini at home. What do we got here? We got a dry run is completed. Our smoke test is complete. So, we'll come back to him and check if our function is going. Oh, we're still building. Oh, no. The demo gods are not with me. All right. So, we'll just keep talking

**[10:34](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=634s)** through the agent build and all of our options. We can pop over here to the voice tab and we can also see all of the TTS models that we support, language boost, voice speed, expressive modes. On the transcription side, you know, we're hosting Deep gram flux, Nova 2, XA, all the ones that you love, all the ones that you hate. We also have noise suppression that's available to us. So, AI acoustics, we have Chris. You can set your attenuation limit. You can add background audio. You know, basically everything that you want when you're building voice AI agents. And then now let's go to one of these calls that's actually completed. Oh god.

**[11:38](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=698s)** Okay. Maybe the Bob demo? I don't know if you guys have seen our uh have seen our robot walking around. Um we've been spending in up with it with voice lately. Um so we've been having these conversations with them asking Bob like what was on his mind. Yeah, here we go. So a conversation with our robot that was out there, just asking what was going on. Um it was like Black Kingdom Bob. Um he's a little bit of a shifty one. Um I can also play the whole recording here. I can review any summarization, any missed opportunities, sentiment analysis. I can dig down like what in like into the deep costs. Um

**[12:24](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=744s)** Pricing is extremely clear with Telnyx. Uh as you can see cost for each part of the pipeline, call control, voice assistant, noise suppression, uh the LLM model that was used for inference, the WebRTC component, SIP trunking, recording. Everything all under one roof with Telnyx. Um getting back to that thing we're talking about with one bill. The metadata for the call that I was talking about. So when these calls come in, what data do we have to do lookups? All of like the session information from Telnyx. And then, you know, kind of like what's important is going to be like the channel. So if it's SMS, if it's a voice call um if they were calling from somebody's phone, we'd be able to see that here. But we called from WebRTC, so we only see the user agent name. And I just need my

**[13:10](https://www.youtube.com/watch?v=M0Ql4N0deEk&t=790s)** deploy to finish. Yeah, anyways. Hey. What can I say? Demo gods not with me today. Um we've got a booth back over there. Uh I'd love for any of you that want to learn more about Talos next and what we do and deploying these agents across all of our different services, all of these various primitives, come over and see us. And like I said, be bright, be brief, be gone. I'm gone. Thank you.
