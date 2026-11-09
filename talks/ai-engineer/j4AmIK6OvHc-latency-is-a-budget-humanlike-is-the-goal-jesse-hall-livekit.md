---
id: j4AmIK6OvHc
title: "Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit"
slug: latency-is-a-budget-humanlike-is-the-goal-jesse-hall-livekit
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Jesse Hall"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-11T01:30:13Z
video_id: j4AmIK6OvHc
url: https://www.youtube.com/watch?v=j4AmIK6OvHc
youtube_url: https://www.youtube.com/watch?v=j4AmIK6OvHc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "voice AI", "voice agents", "LiveKit", "latency", "perceived latency", "turn detection", "speech to text", "text to speech", "realtime AI", "conversational AI", "LLM benchmarks", "voice LLM", "open source", "Jesse Hall", "AI Engineer"]
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit

**Jesse Hall**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#voice AI` `#voice agents` `#LiveKit` `#latency` `#perceived latency` `#turn detection` `#speech to text` `#text to speech` `#realtime AI` `#conversational AI` `#LLM benchmarks` `#voice LLM` `#open source` `#Jesse Hall` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=j4AmIK6OvHc) · [Conference site](https://www.ai.engineer/)

## Description

Your voice agent's dashboard says it's fast. Your callers say it feels robotic. They're both right.

Jesse Hall, staff developer advocate at LiveKit, explains how to build voice agents that feel human. He shows why leaderboards can't pick your models (scores measure one model, but you ship a pipeline, and errors compound from speech-to-text to the LLM to text-to-speech) and why measured latency isn't what your callers hear. He covers buying time like a person does while tools run, plays a hotel-receptionist demo that handles interruptions and a caller changing his mind, explains LiveKit's audio-based turn detection (4.5% of users cut off vs 9.9% for the best alternative), and lays out the window that matters: a second and a half end to end still works, and around 600 milliseconds starts to feel human. He ends with LiveKit's open-source benchmark you can run against your own agent, a sneak peek of a voice-tuned Gemma model on LiveKit Inference, and a checklist.

In this talk:
• The leaderboard trap, and why pipelines fail differently than models
• Measured vs perceived latency
• Turn detection from audio, and buying time during tool calls
• A latency budget, an open-source benchmark for your agent, and a checklist

SPEAKER
Jesse Hall, Staff Developer Advocate, LiveKit
X: https://twitter.com/codeSTACKr

LINKS
LiveKit: https://livekit.io
LiveKit Agents docs: https://docs.livekit.io/agents/

CHAPTERS
0:00 Intro
0:42 You've talked to one of these
1:22 Latency is a budget
2:02 Picking models
2:42 What LiveKit is
3:26 Realtime models vs pipelines
4:16 How pipeline errors compound
4:51 The leaderboard trap
6:06 Measured vs perceived latency
7:35 Buying time like a human
8:21 Demo: hotel receptionist
10:26 Audio-based turn detection
11:41 The 600 ms target
13:54 Benchmark your own agent
15:09 A faster voice LLM
15:53 The checklist

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,588 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=12s)** All right, let's get started. So, most of the agents that we build today, they do their work in the background, right? They write code for us. They do research. Uh you give them a task, you walk away, you come back, and so nobody really cares if uh a background agent takes an extra 10 seconds or even 10 minutes, right? We're used to that. But, in at some point in this past year, you've probably talked to another kind of agent. A real-time agent. Uh maybe uh it was a pharmacy refill, maybe at an airline. Um I talked to one the other day when I called a car dealership. And and so something happened on that call. You probably did the most human thing possible. You talked over that AI.

**[1:03](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=63s)** And that voice agent fell apart, and it just didn't feel natural, did it? And so um if you ask uh anybody in this industry, you're probably going to get a very similar answer of how to fix that. It's going to be speed. Uh faster models, lower latency, shave off another 100 milliseconds. Um but that is the wrong answer. Uh and so latency it is a budget, and I'll I'll tell you exactly what that budget is. But, the goal is something else entirely. The goal is being uh the voice AI being as human-like as possible. Uh an agent that listens while it talks. Uh one that knows the difference between you finishing your thought and you still thinking. Uh one that rolls with it when you change your mind. And so speed alone can get you none of

**[1:51](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=111s)** that. What gets you there is which models you pick and how you configure your pipeline. And so that's the first problem that we're going to encounter. No one tells you how to pick the right models. The leaderboards can't help you. The vendors definitely can't help you. So, let's talk about how we're going to fix that issue. So, a show of hands quickly, who here has ever built a voice agent and shipped it to real users? Okay. All right. Some of you have experience and you know the challenges that you'll face when deploying a real-time agent. Another show of hands, who here has used ChatGPT's advanced voice mode to talk with ChatGPT? Yeah, many of us have have used that, right? So, OpenAI actually chose LiveKit

**[2:41](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=161s)** to power that. LiveKit is the open-source real-time framework and infrastructure for the most human-like voice agents possible. Uh agents that can hear, see, and speak with the person on the other end. Uh and so, not just voice, but also video, uh data, and even physical AI. But, because voice is is challenging, uh we're going to actually focus on voice during this talk. And so, um what we're going to uh look at is is voice agents. They basically have um three models uh that work together as one system. So, your speech-to-text, your LLM, and then your speech uh text-to-speech. So, three slots. Now, I do have to acknowledge that there are

**[3:28](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=208s)** real-time models as well. And and real-time models, uh they are a newer concept. They're getting better and better, uh but they're not right for every use case. And just the fact that there are real-time models even adds more complexity to our problem of trying to figure out which model is best for our voice pipeline. So, here is what you have to choose from. Hundreds of models, dozens of providers, uh and show of hands here, who has picked a model just because they saw it at the top of a leaderboard? Yeah, most of us. Um but here's why that doesn't work for real-time agents. Leaderboards score components, but you are shipping a cascade, a pipeline. So, let's say that your caller wants to

**[4:16](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=256s)** book an appointment on Tuesday the 3rd. Your speech-to-text hears Tuesday the 30th. And so, from that moment on, it doesn't matter how smart your language model is, it's now confidently booking the wrong day, and every error flows downhill from there, and the layers below it have no idea. And so, those leaderboard scores, they came from clean audio in a quiet room. Uh but your callers, they're calling on a speakerphone, in traffic, with kids in the backseat. So, those leaderboards never met your users. Uh and there's a name for this, the leaderboard trap. So, this the score measures the model, but again, you're shipping a conversation. But everyone building voice agents,

**[5:03](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=303s)** they're asking, you know, what is the best speech-to-text model, LLM, TTS? But the real question is, which stack should I ship? So, the these are two completely different questions, and the only only one of them has a leaderboard, until today. Uh we're going to talk about that more in a bit. So, let's say you fall into this trap, you pick your models based on the leaderboard, and now you start measuring things. This is the next problem. You're probably measuring the wrong thing. You see, your TTS provider uh reports time to first byte, and that looks great on the dashboard, uh but bytes are not sound. And so, we've measured popular providers that are actually shipping hundreds of milliseconds of silence at the beginning

**[5:51](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=351s)** of their audio. And in the worst case, up to 3/4 of a second of nothing but silence before that first audio comes in. So, time to first audio is actually what your caller hears. And so, this is the distinction that this entire talk hangs on. This measured latency versus perceived latency. So, what your dashboard says versus what your user hears. The dashboard says it's really fast, but your ears say it's slow. Same story for language models. Time to first token is a text metric. So, your TTS can't start speaking though on a token, right? So, it needs an entire sentence. So, that that number matters for for voice because it needs the entire first sentence, but the model

**[6:43](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=403s)** ranks differently on that. So, a model that streams back back a model that streams tokens the fastest is not necessarily the model that finishes a sentence first. Now, if if you let's say you do measure all of this perfectly, there's another part of the conversation that the benchmarking that gets completely ignored. And that is that a real agent doesn't just chat. It needs to do things, right? It has to look up orders, check availability, book rooms, right? And so, a tool is going to take time. 2 seconds, 10, 40, or more seconds. And no model choice is going to be able to hide a 40 or more second latency. So, think about what a human receptionist would do here. They they

**[7:32](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=452s)** don't freeze while the the booking system loads, right? They say, "Give me a sec. I'm looking up your your account, right?" They they buy time. And they listen while they keep working. And that is that human-like behavior that we're looking for. So, why can't an agent just keep talking and do things asynchronously? Well, it can. And here's the shape of that, and this is the only code that you're going to see. Uh but this is a normal tool. Uh there's just one thing different, and that is this line right here. Uh the first update hands the mic back to the agent while it keeps uh working in the background. And that's the whole trick. The conversation and the tool stop sharing a thread. Uh and so, don't take my word for it. It Listen for yourselves.

**[8:21](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=501s)** >> Thanks for calling the Live Oak Hotel. How can I help you? >> Can I book a room? >> Of course. What dates are you looking at? >> October the 10th through 12th. >> October 10th to 12th? And for how many guests? >> Two. >> I have queen with two beds, king, double, queen, or suite. Which Would you prefer a city or ocean view? >> Ocean. >> Who should I put the booking under? >> Jesse Hall. >> You're all set for October 10th to 12th in a king room with an ocean view for $582.40 on the card ending in 1111. Shall I go ahead? >> Actually, you know what? I need to change the date to December the 20th

**[9:10](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=550s)** through the 24th. >> December 20th to 24th? That brings the total to $1,164.80 for December 20th to 24th. Shall I go ahead? >> Yes. >> You're all set. >> Okay, so we had to speed up some of the parts there because of time, but the the the agent kept the conversation going. There were no awkward pauses. The caller even interrupted it and it kept going. And the caller also changed his mind in the middle of things and the agent just rolled with it, right? This is the human-like behavior that we're looking for. So this is again not one model being good, this is an entire system being good. This is the infrastructure, the framework and the models all working

**[9:58](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=598s)** together. And that's exactly what no component or model benchmark can see. Now there's one more axis to this that the leaderboards miss entirely and this is knowing when to speak and when not to speak. So humans negotiate turn taking in a matter of just a a couple of a hundred milliseconds, mostly from tone. And a pipeline that it waits for the entire transcript to come back, it's already late, right? So we built a turn detector that is based on audio itself. So it listens to the rhyme, the pitch, the intonation of the speech of the audio and then we published the numbers on this. So at the same latency budget, the best alternative cuts users off 9.9% of the time.

**[10:49](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=649s)** Ours is 4.5% and the eval harness is open source. You don't have to trust me, you can run your own data through this and see what you get. So let's go one level deeper for a minute. The gap between your caller's last syllable and your agent's first audible bite. So end of turn detection fires from audio before the transcript lands, the language model is already running on a provisional transcript and if the final words match then you just saved a half a second. And then the TTS starts on the first complete sentence, not the last token. And so the the the first audible bite is when the human stops waiting. And so every model that you choose, it shows up

**[11:36](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=696s)** here in this window, and this window has a fixed size. If you can stay within a second and a half end to end, the conversation still holds, but you're you're right on the edge. If you can get closer to 600 milliseconds, then it starts to feel really human. And so the question is never how fast can I go, but what is the most human-like agent that I can fit inside this window? So back to latency as a budget, but human-like is the goal. So if we add all of this up, the question that we asked at the beginning, what models should I pick? That was never actually answerable. And so we built the thing that we wish existed. Here's how we built the benchmark. We take a complete working agent. The

**[12:25](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=745s)** first one is that hotel receptionist that you just heard. And it it takes real bookings. It has a real back end. And it's also open source. You can look at the repo. And we run hundreds of simulated callers against it. The the simulator interrupts. It mumbles. It changes its mind, just like a real caller would. And then we don't score it on vibes, but we score outcomes defined the way that we would define them for a human. And so did the right reservation land in the database? Did a caller get cut off? Are the names and dates correct? Are there were there any invented tool calls or any leaked personal data, right? So we measure all of those things against human equivalent behaviors. That's the

**[13:13](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=793s)** bar. And then completion alone isn't enough, because completion can actually be gameable, right? So a model can kind of guess its way to complete, right? And so we penalize what a completion a completion score can't see. If like if it asks questions that didn't need to be asked or if it takes 10 steps to do something that should have only taken two steps. And then we swap the stack out. The same agent, the same scenarios, but different models. Every model sees the exact identical input byte for byte. But this creates benchmarks against our agent example. There are as many benchmarks as there are agents. So the benchmark is actually

**[14:01](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=841s)** yours. You can run this exact thing run your agent through this exact benchmark and get your scores. And so this is how you catch surprises. The whole thing is open source, the methodology, the eval sets, the agent itself. You can point the same thing at your agent and let us know how it performs for you. Now here's an important fact about LiveKit is that we don't make STT, LLM, or TTS models. Every provider plugs into our stack. So we don't have a horse in this race. We just watch all of them run a lot. And so we can confidently pick the winners. And so what you're looking at right here is a sneak peek of the Gemini 4 31B model on LiveKit inference. But this isn't just an off-the-shelf

**[14:49](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=889s)** Gemma 4 31B. It's tuned specifically for production voice agents with long prompts, many tools, and tight latency budgets. It passes voice evals at 88% and it starts speaking in about 380 milliseconds. So that's over two times faster than the next model. Making this the actual the fastest high-quality voice LLM available today. And so this is actually going to going to launch tomorrow on LiveKit inference. So again, our goal is to have the most human-like agents possible while sticking to that latency budget. So if you remember one thing from this talk, make it this one. A voice agent isn't a chatbot with a speaker stacked onto it.

**[15:38](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=938s)** It's human-like infrastructure. A real-time system that senses and responds the way that a human, a person, would. The moment that you treat it that way, every decision is going to get clearer. The budget, the metrics, the models, and the bar that you test against. So here's the checklist. You can take a photo of this. Set your latency budget first. Measure perceived latency. Spend whatever budget is left on model quality, not on speed that doesn't matter. And then anything over a second it should go asynchronously so that the conversation never stops. And then just test the conversation, not the components. And then keep testing in production. So here's the benchmark. Uh scan the QR code. You can check out the benchmark. You can run this against your own

**[16:26](https://www.youtube.com/watch?v=j4AmIK6OvHc&t=986s)** agents. And at uh remember at some point in the near future, you are going to call a voice agent, and you're going to talk over it, and it's not going to fall apart. It's going to act like a human would in that scenario. So go build that. Thank you. >> [music]
