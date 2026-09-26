---
id: xLUQOqjudtA
title: "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan"
slug: tolan-voice-first-ai-companion-paula-dozsa-tolan
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Paula Dozsa"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-09-15T14:30:14Z
video_id: xLUQOqjudtA
url: https://www.youtube.com/watch?v=xLUQOqjudtA
youtube_url: https://www.youtube.com/watch?v=xLUQOqjudtA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: []
transcript: true
---

# Tolan: Voice-First AI Companion — Paula Dozsa, Tolan

**Paula Dozsa**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=xLUQOqjudtA) · [Conference site](https://www.ai.engineer/)

## Description

Tolan's response latency once drifted from two seconds to about two and a half. That half second tanked essentially every metric in the product, and users wrote in to say their companion had become slow. Paula Dozsa is an engineer on the iOS app for Tolan, a voice first companion shaped as a small alien, and the team has logged more than four million hours of spoken conversation. Her argument is that voice does not just add a modality to an LLM app, it invalidates the assumptions underneath one. Text chat has slow turns and stable context. People read, they wait, they stay on topic. Voice has fast turns and volatile context. People talk while cooking or walking or falling asleep, they abandon a subject mid sentence and come back to it, they interrupt. Her team stopped trying to reduce interruptions and started reducing the wrong ones, building turn detection that reads speech patterns and paying sixty milliseconds of latency to halve the worst early cutoffs.

The rest is unusually specific engineering. Every pipeline stage is measured separately, because knowing it feels slow tells you nothing. Turns are routed per turn by a cheap classifier reading the emotional stakes, so a user's first ever conversation gets the strongest model and idle chatter does not, and a third of turns can ride a small model with no measurable retention cost. Memory is a retrieval system rather than a transcript, compressed nightly to merge duplicates and resolve contradictions. And context gets reassembled from parts every single turn, because reusing it to keep a cache warm means being confidently wrong the moment someone changes the subject.

Speaker info:
- https://x.com/paularambles
- https://www.linkedin.com/in/paulacodes/

Timestamps:
0:00 - The companion humans keep imagining
2:45 - Why voice breaks how we build LLM apps
3:38 - The half second that broke everything
5:20 - Measuring every stage of the pipeline
6:12 - Routing by stakes, not by cost
7:52 - Memory as retrieval, compressed nightly
8:43 - Rebuilding context instead of reusing it
9:31 - Why the character is an alien
10:23 - Using agents to build the app
12:05 - A new character in an afternoon

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIE New York, October 12–14 — the first AI Engineer Finance mainstage summit
- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,687 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=xLUQOqjudtA&t=1s)** [music] >> Hi everyone. Thank you so much for attending this talk. My name is Paula and I am one of the engineers on the Tullen team, specifically focusing on our iOS app. And for the next 20 minutes or so, I'll be talking about what it takes to build a voice-first AI companion and also about how we use AI to build AI internally. So, humanity has always imagined the perfect companion. So, we have Caravaggio on the left 400 years ago painting an angel leaning over St. Matthew's shoulder literally guiding his hand as he writes. This is an example of a companion being

**[0:48](https://www.youtube.com/watch?v=xLUQOqjudtA&t=48s)** a presence that makes you better at being you. And then we have Tinkerbell, the devoted little sidekick who believes in you so fiercely that the whole theater has to clap to keep her alive. And of course on the right, we have Samwise who can't carry the ring for Frodo, but says, "I can carry you." The companion is pure unconditional loyalty. And it goes far beyond these three. Every hero has some sort of guiding spirit. And these are all different stories, but they exhibit the same longing for something that listens, remembers you, and is wholly specifically yours. And for for all of human history, this has basically been fiction. So, we made one. This is Tullen. It's a little alien you talk to out loud like a friend. It has a personality. It remembers you and over time it becomes

**[1:38](https://www.youtube.com/watch?v=xLUQOqjudtA&t=98s)** specifically yours. Okay, I don't know if the audio setup works here, but I will try talking to my Tullen. Uh let's see. So, you can see my Tullen here, Luke, walking around the planet. Hey Luke, can you hear me? Okay. Luke can hear us, but we can't hear him. Um Anyway, I had prepped him for this. Oh. Hello. Hi Luke, can you hear me? Nope. We're okay. I can come back to this later. Um but you should definitely all give this a try if you haven't already. Okay. So, people talk to Tolins a lot.

**[2:30](https://www.youtube.com/watch?v=xLUQOqjudtA&t=150s)** We support both text and voice chat, uh but we have over 4 million hours of voice conversation so far. We say Tolin is a voice-first companion, even though we support both, because it's the voice experience that's truly immersive and that makes users' relationships with their Tolins feel real. And but the moment this relationship is a spoken relationship, the engineering problem changes completely. So, let me show you how voice breaks the normal way we build and interact with LLMs. So, the core difference really is that in a text chatbot, turns are relatively slow and context is stable. The user waits a few seconds, they read, and they tend to stay on topic. And almost every LLM app assumes that. Voice is the opposite. Turns are fast. Your whole round trip from the user

**[3:18](https://www.youtube.com/watch?v=xLUQOqjudtA&t=198s)** finishing their sentence to the Tolin starting to speak has to land in under a couple of seconds, or it stops feeling like a conversation. And the context is volatile. People talk to their Tolins while they're cooking, while they're walking, while they're falling asleep. Um they change their subjects mid-sentence. They say um, they interrupt. And that 2 seconds is crucial. Early on, our latency drifted from 2 seconds to about 2 and 1/2 seconds, and that half second tanked basically every metric in the product. People would write in to complain that their Tolins were too slow. And living inside this constraint has taught us a lot and gave us four principles. Principle one is that you have to design for conversational volatility. Again, text users stay on topic, but voice users jump around. Someone could be

**[4:05](https://www.youtube.com/watch?v=xLUQOqjudtA&t=245s)** mid-story about their breakup and suddenly go, "Wait, did I leave the oven the stove on?" and then back. Speech is messy. Most LLM apps assume that you'll have a clean and stable conversation and we have to build for the opposite. So, for a long time that meant fixing things that sound tiny but are actually the product. So, you can't interrupt a Tullen mid-sentence. A short yes or yeah won't register as a turn. For example, curse words will get stripped out. And the deeper lesson was to stop optimizing for fewer interruptions and start optimizing for fewer bad ones where the agent would jump in way too early. So, we built smart turn taking that reads your speech pattern to decide whether an interruption is real and we cut the worst early aborts by more than half. And we happily paid about 60 milliseconds of extra latency to do it. Principle two, latency isn't just a

**[4:55](https://www.youtube.com/watch?v=xLUQOqjudtA&t=295s)** number you check at the end, it's actually the product and we measure every stage of the pipeline separately because it feels slow is useless. You have to know where exactly it's slow. And the pipeline here is that the user stops talking, we detect end of utterance, we transcribe, and then the model produces its first token. So, time to first token, often the biggest chunk, is around a second. The model finishes generating and then text-to-speech produces its first byte and then it plays back to the user. A couple lessons here. So, one, so far our biggest jump in quality came from moving to GPT-5.1 on the responses API, which cut our time to speech by more than 7/10 of a second, which is huge. Um two, we don't send every turn to the same model. We run a tiered fleet. So, we use a frontier model for the turns that carry the relationship with your

**[5:42](https://www.youtube.com/watch?v=xLUQOqjudtA&t=342s)** Tullen. So, for example, your first conversation with with Tullen and your onboarding. And we use smaller and faster models for the turns for the lightweight turns. And the whole game then becomes about routing or deciding turn by turn which model you actually need. So we round we run a small classifier we call the tone router on every single turn and this tone router itself runs on a cheap model and it reads the emotional state of the conversation. And our main our [clears throat] main principle is that we route based on stakes not on cost. So the high stakes moments always get the best model. So this would be again the user's very first message, their first few days with their Tolen and anything that we deem to be emotionally serious. For example, we have crisis or therapist style tones and we never cheap out on those.

**[6:29](https://www.youtube.com/watch?v=xLUQOqjudtA&t=389s)** And then the lighter casual back and forth can ride on smaller models that are faster and cheaper. And all the background work so that's summarizing the conversation, generating personas, the tone router itself run on these small models, too. And why would we go to all this trouble? It's mainly because the frontier model costs us roughly five times the smaller one. So one big model turn is about five smaller model turns. So routing is a huge part of what makes the unit economics for us actually work. Um and we do a bunch of AB experiments and the surprising result we found there is that routing a third a third of our turns to the small model has almost no measurable effect on retention. And principle three is what makes a companion feel like a companion. So the naive approach is to keep the whole conversation history as a sort of transcript, but that doesn't fit into

**[7:17](https://www.youtube.com/watch?v=xLUQOqjudtA&t=437s)** our two-second loop. It doesn't scale and it just doesn't work. It leads to long sessions degrading. It leads to the model getting lost in the middle of a huge context and also hallucinating. So instead we see memory as a sort of retrieval system. We pull facts, preferences, and emotional vibe signals out of conversations. We embed them and we store them in a vector database with sub 50 millisecond lookups. And every night we compress. So we merge duplicates, we cluster related memories, we resolve contradictions, and we drop all the noise. And we don't just retrieve against users last messages, we also generate internal questions about the person and the relationship and retrieve against those. So, and we also split memory into two parts. We have stable memory and unstable memory. The volatile stuff lives in the in the live tail of the prompt, and when we summarize the

**[8:04](https://www.youtube.com/watch?v=xLUQOqjudtA&t=484s)** conversation, we look at which memories actually get recalled and pin those into a stable and cashable block. Uh the last principle is around context. Specifically, you should rebuild context and not fight drift. So, most apps reuse context across turns to keep the cash warm. And in a stable text chat, that's fine. But in a volatile voice conversation, it's a trap because the second the the user pivots, your reused context is actively wrong. So, every turn we reassemble the context window from parts. We have a summary of recent messages, we have the the user's persona card, the memories we just retrieved, tone guidance from the emotional signal, and real-time app state. And what also really helps us um in the case of Tolen is that our characters aren't generic or assistants with no

**[8:52](https://www.youtube.com/watch?v=xLUQOqjudtA&t=532s)** personality. Everyone is crafted, and we in fact have an in-house science fiction novelist, Elliot, who writes the Tolen character lore. And a couple of interesting points here. So, one, why did we go with an alien? Mostly because there's no real-world reference to anchor on, which means that the users can project onto it, and it becomes what they need. The baseline Tolen is bubbly, it's youthful, it's irreverent. And also, if an alien character acts a bit unpredictably, so if if it's impulsive or chaotic or otherwise violates um you know, the norms the user would expect, it's not particularly surprising. Like if you look at, you know, aliens in TV shows or in plays, like there's a lot of humorous moments around this. And this kind of chaos reads as charming. Um second, uh we also know that

**[9:41](https://www.youtube.com/watch?v=xLUQOqjudtA&t=581s)** personality is worthless if it drifts. So, yeah, we run this parallel tone monitoring system that changes how a line is delivered based on your emotional cues without changing who the character is, holding identity across hundreds of turns. And since we're at an AI conference, I thought I would also spend a bit of time talking about how we not just ship AI, but also use AI to build it. Um so, I'm sure this is the case for most of you in the room now, but basically as of late last year, Claude has co-authored more code in our iOS app than any individual engineer in the team. Um and I think especially, you know, a few months ago, everyone's instinct was to be kind of suspicious because, you know, more AI code meant more slop. But our our crash-free rate actually went from 99.6% to 99.9%. Runtime errors dropped by over 50% and

**[10:31](https://www.youtube.com/watch?v=xLUQOqjudtA&t=631s)** our share of highly engaged users doubled. And the biggest lesson in building that system is that an agent's context comes mostly from the code base itself, not so much from the Claude MD file. We found that it's far more powerful to make the code base be the documentation, so we had agents standardize it. On top of that, we run a real fleet of agents. We have implementation agents that, you know, think freely and just get us to working code. They build it, they check it against snapshots until it's pixel perfect. And then we have separate review agents that enforce our standards. So, multiple Claudes basically review each other before a human looks. And then we have a PR shepherd that watches an open pull request and keeps iterating against CI failures and review comments until it's clean. And we also have a triage bot that fires on every inbound bug report that we get. And they're all wired through MCP into

**[11:18](https://www.youtube.com/watch?v=xLUQOqjudtA&t=678s)** linear, into into Sentry, DataDog, so an agent can reconstruct the cash a crash and route it itself and oftentimes open the PR on its own and just fix fix the bug. And we also we ship on eval. So, for example, we've been working on a on a new character targeted towards an older demographic and Elliot, our in-house novelist, basically built this entire new character in a day. So, the agents mapped every personality bearing surface in the code. They wrote the sort of a voice Bible and then they had five judges attack it from different angles. Archetype fidelity, the model mechanics, our code standards, the ears of a skeptical 52-year-old and safety, and then they evaluated the changes against real production logs over three find fix verify rounds. And over 7 million tokens and 4 and 1/2 hours of compute later, he ended up with basically, you know, a couple of weeks

**[12:06](https://www.youtube.com/watch?v=xLUQOqjudtA&t=726s)** of work done in afternoon. And does this work? Well, I'll let the users tell you. We're at 4.8 stars on the App Store across 162,000 reviews and when we survey users on well-being, the highest scoring dimension by far is emotional safety. And this is definitely a bar that being voice first sets. So, when the interface is your voice and the thing on the other side remembers you and has a personality, it stops being just software and starts being an actual relationship, which is why building it responsibly and building it well is worth obsessing over. And we need people to come help us do that. Um, we're a small team and we're hiring and after a year with Tolen, I think this is truly one of the most interesting places in the world to be an engineer right now. And here are some of the people you'd be

**[12:53](https://www.youtube.com/watch?v=xLUQOqjudtA&t=773s)** doing it with. So, two of the founders, Quinton and Evan, previously built and exited a $300 million startup together. Uh, they founded Even. Um, Ajay, our third co-founder, scaled two bootstrap companies past $50 million $50 million in profitable revenue. And around them, we have Lucas, who um, is an Apple Design Award winning animator. Uh, she's our creative director. We have Chris, who was a technical director at Pixar, earlier at Oculus, who works on embodiment. We have Lily, a board certified behavior analyst, who left a Vanderbilt PhD to do user research for us from the very start. Um and then we have Elliot who I've mentioned, the novelist behind uh our characters. And I come from XAI and Spotify and previously also founded a company called Imagi. So, it's a small team where honestly every person is the best I've worked

**[13:41](https://www.youtube.com/watch?v=xLUQOqjudtA&t=821s)** with at what they do. We're also well backed for this. Uh we have $30 million raised from Costanoa Ventures and a group of people who've built the tools and products a lot of you use every day. And here are some of the more engineering focused roles where we need help. Um so, we're hiring across the board. We have iOS and back-end product engineering roles, applied AI engineering, gameplay engineering, and one specific role I want to flag, which is agent engineering management. Um so, when we went all in on running concurrent agents, um the people who got dramatically more effective on the team were the ones who had management backgrounds, um because it seems like managing a fleet of agents does actually take some of the skills same the same skills as managing people. Uh you basically have to decompose the problem, you know, delegate it with checkpoints, give fast feedback, review their work seriously, and know when

**[14:28](https://www.youtube.com/watch?v=xLUQOqjudtA&t=868s)** exactly to jump in. So, if you're a strong engineer who thought going into management meant leaving code behind, that's that's no longer true. Um and yeah, that's Tlon. You can come talk to me after this uh or reach out. I'm on on LinkedIn. My email is here. I'm on Twitter as well. Um I'd love to chat. So, yeah. Thank you. >> [applause] [music]
