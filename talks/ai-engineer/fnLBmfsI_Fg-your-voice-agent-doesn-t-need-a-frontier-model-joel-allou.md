---
id: fnLBmfsI_Fg
title: "Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft"
slug: your-voice-agent-doesn-t-need-a-frontier-model-joel-allou
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 6
published_at: 2026-07-20T06:25:15Z
video_id: fnLBmfsI_Fg
youtube_url: https://www.youtube.com/watch?v=fnLBmfsI_Fg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=fnLBmfsI_Fg) · [Conference site](https://www.ai.engineer/)

## Description

My AI voice tutor doesn't run on a frontier model. It runs on a small one, and the reason isn't cost. It's that voice lives or dies on latency, and the scaffolding around the model is what makes it feel smart anyway.

When you build a voice agent the clock is brutal. A pause longer than a held breath feels broken, so your real budget is time to first token, not benchmark score. A big model that thinks for a second has already lost the room. So the model choice gets made for you: pick the fastest one the latency budget allows, then make up the intelligence elsewhere.

I'll show how that plays out in an AI voice tutor I built on a small, fast model. The model never has to remember what the student knows, plan the lesson, or decide what comes next. Deterministic systems do all of that and hand the model a tight, structured brief each turn. What's left for the model is the one thing it's genuinely best at, which is talking. The scaffolding isn't a cost optimization bolted on afterward. It's the thing that lets you use the cheap fast model at all.

Seven minutes. The latency budget that forces the decision, what moves out of the model to survive it, and where a small model still falls down no matter how much scaffolding you give it.

Speakers:
- Joel Allou: Joel builds voice-first AI tutors. Solo founder focused on agentic systems for personalized learning, with a particular interest in infrastructure that makes flow agents reliable.
- Ornella Bahidika (Microsoft): Ornella Bahidika is a Product Manager at Microsoft, where she develops solutions that help organizations optimize collaboration, workplace technology, and AI-driven experiences.

## Transcript

*893 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s)** Hi, I'm Ornella, and that's Joel, and we built Ace, a live AI voice tutor. It run on a small model on purpose, and I want to tell you more why that's not a compromise. Quick gut check. That silence on a voice call, that the difference between a tutor and a broken up. When a voice agent pause for even a second, your brain says it's dead. So, when the answer fit a leader of every instant stay, which for the smallest, biggest model. In voice, that instant is actually a backward. Because our budget was never IQ, it's millisecond.

**[0:49](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=49s)** The AI model need to start talking in about 950 milliseconds. A frontier model that think for a full second has already lost the room, no matter how good the answer is. So, we made the model small and took the hardest part jobs away from it. It doesn't decide when happen what's happen in the lesson. It had It doesn't track what the student knows. It doesn't explain what's next. We have a system in place to do that, and they hand the model a summary every turn. What's left for the model is one thing it's really good at, talking. And that's the theory. Joel, go on and show them what it actually feel like. >> Yeah, if maybe I can add some color to

**[1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s)** what Ornella was mentioning. So, if you think about the models of today, especially the frontier model, let's take Claude 4.7, which is uh from Anthropic. The model is really good at reasoning. You can give it a problem, in this case a lesson, and it can reason through it, it can reason through what the student asking and it can come up with the answer. But that is actually precisely the problem. Because the reasoning can take couple of seconds and those seconds are really valuable when you are building voice applications. So what we are doing is saying, "Hey, let's extract all of the thinking away from the model so that the model focuses on only what matters, which is speaking in our case."

**[2:25](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=145s)** So all of the thinking is extracted into a state machine. So for Ace, we have thought about all the scenarios that are needed for a lesson. We have built a state machine that is able to coordinate each step to the next and we also added intelligent layer on top to derive some of the mastery that a student might need for the lesson to be complete. So everything when it comes to what happens next, when it comes to what needs to be displayed, when it comes to how to actually answer a question, it's all done outside of the model. And we simply feed that output to the model to speak out. And so let's go ahead and look at an example and see how that works in real time.

**[3:12](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=192s)** So the first video here is without the implementation we've done. So it's a simple Opus 4.7. We ask a very simple question and as you can see the model is thinking, it's reasoning and it takes couple of seconds to return the answer back to the user. Hey, what In this video, we've added all everything we just talked about on Haiku 4.5, which is a much smaller model. Same question, but now you see that the answer comes in about 900 milliseconds. And so that's the beauty of building around the model. So by removing all of the thinking, all of the logic, all of the reasoning from the model and actually putting it within the code, we actually saves a lot of time and allows us to use smaller models which are cost effective and actually better at

**[4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)** real-time voice applications. And as you can see, this feels almost instant and again that's because all of the smart parts have already happened prior to the model actually speaking. But I have to be honest because this isn't necessarily free. It has a cost, right? A small model like the Haiku 4.5, if it doesn't have any scaffolding, tend to drift on long structure and really needs strict rules in order to be able to stay organized. So the scaffolding piece is the price. But the good thing is you pay it once and in code, right? Not on every single turn. So here's a rule. Pick the fastest model that your latency budget allows and then spend the rest of

**[4:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=291s)** your time actually building the scaffolding. So [snorts] in our case, right? Maybe you build a state machine, you build a reasoning process, you think about scenarios, what happens if this happens, how should your model handle it? Everything that comes with the logic, everything that comes with the harnessing, you do that outside of the model and then allowing the model to focus on that one thing that is really good at. And so that's true for voice applications like A is, that's true for real-time applications where latency is of priority and that's really true for anything that is high volume, right? In those cases, the model is the smallest part of the system. So this is Joel and Ornella and we are building A is again and if you have any

**[5:39](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=339s)** questions, let us know. Thank you. >> Thank you.
