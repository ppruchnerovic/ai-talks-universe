---
id: UlFB6efYN5Q
title: "A Song of Types and Agents - Roberto Stagi, Ratel"
slug: a-song-of-types-and-agents-roberto-stagi-ratel
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Roberto Stagi"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-07-12T00:00:00Z
video_id: UlFB6efYN5Q
url: https://www.youtube.com/watch?v=UlFB6efYN5Q
youtube_url: https://www.youtube.com/watch?v=UlFB6efYN5Q
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration"]
transcript: true
---

# A Song of Types and Agents - Roberto Stagi, Ratel

**Roberto Stagi**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=UlFB6efYN5Q) · [Conference site](https://www.ai.engineer/)

## Description

Python ruled unchallenged for a decade, sitting comfortably on the AIron Throne. But a quiet rebellion is brewing: the entire stack that actually deploys AI agents in production runs on npm, not pip. This lightning talk is an opinionated, slightly unhinged tour of how TypeScript is taking over the AI throne, why this happened and how you can prepare for it.

Speakers:
- Roberto Stagi (Ratel): Roberto is the CTO & Co-Founder of Ratel, context layer for AI Agents, EU-Ambassador at AI Socratic, and deep into the mission of making context engineering simple for everyone.
X/Twitter: https://x.com/rstagi_

## Transcript

*1,758 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=2s)** Hello, and thank you for being here. I'm Roberto, and today I'm going to tell you this song of types and agents. Uh basically a song that speaks about languages that fight each other to conquer what's the throne in the AI realm. And how I think that TypeScript might actually be winning this war. But let's start from the beginning. A few years ago, whenever someone was building uh in AI, they were certainly using Python. Like there was no doubt. All the other languages were bowing to Python because um because of its dominion uh over the AI world.

**[0:51](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=51s)** And then, when in 2022 ChatGPT was released, everybody started wondering and starting understanding that AI was becoming something more. Was going outside of the bubble that lived for years. And started to becoming something more ambitious. And together with it, Python, which was the standard language for AI, became more ambitious as well. And that's how in 2024 uh GitHub actually claim claimed the ladder and became the most popular language on GitHub. So, you know, everybody was happy. Python finally reached the top.

**[1:40](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=100s)** But little did they know that there was another contender for the throne. Another contender that was rising to challenge the claim that Python had on the throne. And this contender, as you may have guessed by now, was indeed TypeScript. But, before talking about this, let me present myself. My name is Roberto. I'm the CTO and co-founder of Reto, a context layer for AI agents. And I'm also the EU ambassador for AI's Pratic, a global community of AI builders meeting once per month to discuss the latest news in AI. I'm also a long-time JavaScript then turned TypeScript developer. And that's

**[2:29](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=149s)** basically why I am talking about TypeScript today. So let's begin. As we said, AI started moving up to the stack. It was moving from the infrastructure layer of these models, machine learning, and all related ecosystem towards the application layer. This means that AI stopped being something that you train, and it started being something that you ship inside your application. Applications started featuring AI, starting having features powered by AI. Which basically means that we started having applications that think.

**[3:19](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=199s)** And the application layer was not Python's. The application layer has been TypeScript's for pretty long time now. Don't get me wrong, like I still think that Python has its own application. Like I still think that the brain of the of the agent and all the of all the AI world is actually still owned by Python. All the training, the research, the GPU serving is all Python's. Uh Has been Python's all along and it's going to be Python's for long time yet. And um what's changing is actually the application layer. Like few years ago, if you wanted to build

**[4:09](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=249s)** something with AI built in the application, you had to use Python. But today, that's not the case anymore. And that's all uh the shift is about. TypeScript doesn't just own, you know, the UI or the back end. Started owning also the agentic layer of our application. And that's why in August 2025, TypeScript TypeScript actually passed Python as the most used language on GitHub. And the funny thing is that the reason that the GitHub reports gave was the same. Like in 2024, it said AI leads Python to the top language. While in 2025, it said AI leads TypeScript as

**[4:59](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=299s)** the first language. And in both cases, as you can see, the global developers, the number of global developers were surging. In 2020 2025, we even have one new developer joining GitHub every second. So, what actually changed in this year? Like yeah, we were flooded from like new developers. In 2024, these newcomers were reaching for Python, or even maybe existing developers were reaching for Python. And in 2025, they reached for TypeScript instead. What changed between 2024 and 2025 was actually

**[5:47](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=347s)** coding agents. The coding agents grew up like we saw established um we saw the players establishing themselves like Lava Cloud Code, Cursor, Codex. They became the default way to build applications. And the default way to uh to which these coding agents actually built the applications was TypeScript. And you know since every new app pretty much every new app is an agent today because they ship these AI and agentic capabilities, they are hungry to embed AI inside themselves. The demand to have more AI integrations,

**[6:36](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=396s)** more and more AI integrations doesn't fall on through Python. >> [clears throat] >> It falls on TypeScript. And pretty much all the tools that we use to build AI today already run on TypeScript. We even saw an AI lab acquiring a JavaScript runtime like last December Anthropic acquired Bun. But still, you know, okay, everybody use is using TypeScript because of the coding agents and we are having more and more demand to build uh AI to embed AI inside TypeScript application. But does this mean that we should do it?

**[7:25](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=445s)** Like this is a fair question, like it's an honest question and it's a question worth answering. And the answer in my opinion can be yes like for several reasons. The first one is that since TypeScript is the default language for coding agents today, we can expect that they will become better and better in in TypeScript because we are having more and more application in TypeScript, which are going to field the training of next coding agents. And then we are having uh deeper integrations and more native integrations from these coding agents towards TypeScript, and we can expect that the quality of the output in TypeScript is going to be better and better from these coding agents. Since

**[8:14](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=494s)** we're building applications, and uh we want to have like the highest quality of these applications, might make sense to build agents, which are the new kind of applications in TypeScript. And also, if you use TypeScript, you are actually tapping into what is probably the richest package manager out there. NPM comes with everything, uh pretty much everything, like authentication, payments, UI, infra. Like it's uh the deepest up layer tail that there is. So, since again, AI is coming towards the application layer, we need to integrate with all these right now. And tapping

**[9:02](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=542s)** inside NPM is a very convenient way to do that. Also, you have by building in TypeScript, you can have one single language throughout all your code base. You can have one single code base for the whole application. Because you can use TypeScript for your agent loop, for the tools, for the back end service, for the UI. While if you use Python, you probably have to split uh split it at least into two services. Which means, you know, one service with FastAPI, Pydantic AI, and whatever. And then another um separate React application that you need to sync between between these two with a uh with a contract, which you

**[9:52](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=592s)** have to maintain and synchronize. And speaking of contracts, with TypeScript, you can have one single consistent typing across all your all your application. While if you use Python instead, you at some point will stop at a boundary, cuz you will have your agent, maybe your back end, etc. with one consistent typing, and then you will have your React application or Vue or whatever with um another set of typing at which you need to synchronize between the two. So, if you use TypeScript, you can use Zod as a single schema throughout all your application, which is very convenient. You can define a type once.

**[10:40](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=640s)** You can use this type in the back end and uh in the model, and you can use the same type in your UI. One type, checked and went. Also like it makes sense to build in TypeScript today uh also in the AI ecosystem because we are seeing a very surge in in the AI ecosystem as well. Like take the Versatile AI SDK, for example, you can see that in just 1 year, it went from 1.6 million to 15.1 million downloads per week, which is between 9 and 10x in just 1 year. So, finally, I'd to put everything together. In my opinion, yes, it makes sense to build AI agents in TypeScript

**[11:29](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=689s)** because you have like a uh you can leverage the the de facto default language for coding agent. You can have one single language for your whole application and your whole code base. You can tap into uh fast-growing AI ecosystem. You can have consistent typing uh across all your application. And you can tap into the richest package manager that there is, NPM. So um you might ask was all this unpredictable? And the answer is actually no. Someone predicted this uh many years ago, almost 20 years ago. Jeff Atwood said, "Any application that can be written in JavaScript will

**[12:18](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=738s)** eventually be written in JavaScript." And you know, as you as you probably know in the last few years, we have a corollary of this that any application that could be written in JavaScript will eventually be written in TypeScript. And so basically, we can say that any application, even the gigantic ones, will be written in TypeScript. And be mindful that what I showed you today is just the beginning. Like, we are just getting started. You can project this in a few years and you can see that on the application layer, the difference between TypeScript and Python is actually going to widen from here. So, um

**[13:05](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=785s)** as I said, the model can still run on pip. But the agents, which is the application layer today, so the agent that called the models will probably ship on NPM. So, everything on the inference layer, you know, it's going to be Python. But everything but else, probably all TypeScript. Let me leave you with one recommendation then. Um keep training in Python. As I said, I don't see that's one going away soon. But please consider building the agents and the applications in TypeScript. Because if you don't do that now, if you overlook TypeScript, you are probably going to fall behind.

**[13:56](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=836s)** That was all on my side today. I thank you all for your listening. And please scan the QR code for the slides. Reach out to me if you agree or if you disagree, if you have any feedback, and let's get in touch. Thank you. Bye-bye.
