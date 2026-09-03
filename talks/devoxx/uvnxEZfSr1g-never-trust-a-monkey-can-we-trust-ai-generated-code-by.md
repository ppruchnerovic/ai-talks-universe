---
id: uvnxEZfSr1g
title: "Never Trust a Monkey! Can We Trust AI-Generated Code? by Baruch Sadogursky"
slug: never-trust-a-monkey-can-we-trust-ai-generated-code-by
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: ["Baruch Sadogursky"]
channel: null
duration_min: 16
published_at: 2026-04-08T18:49:36Z
video_id: uvnxEZfSr1g
url: https://www.youtube.com/watch?v=uvnxEZfSr1g
youtube_url: https://www.youtube.com/watch?v=uvnxEZfSr1g
tags: []
topics: []
transcript: true
---

# Never Trust a Monkey! Can We Trust AI-Generated Code? by Baruch Sadogursky

**Baruch Sadogursky**

`Devoxx` · `Devoxx` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=uvnxEZfSr1g) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

We’re in the middle of another leap in abstraction.

Like compilers, cloud, and containers before it, AI coding agents arrived with hype, fear, and broken assumptions. We gave the monkeys GPUs. Sometimes they output Shakespeare. Other times, they confidently ship code that compiles, passes tests, and still does the wrong thing.

The problem is simple: intent gets lost between what we mean, what we ask for, and what actually runs.

This talk delivers a practical model for software development with AI coding agents built on three equally essential ideas:

The Chasm: the divide between human intent and what is actually expressed to an AI coding agent.
The Context: the shared, explicit, and reusable knowledge an AI coding agent operates within. APIs, conventions, constraints, and domain rules replace guessing.
The Chain: the Intent Integrity Chain. A structured flow of prompt → spec → test → code, at each stage produces a verifiable artifact and is validated externally and grounded in a shared context at every stage.

Together, these form a system where intent survives implementation. Natural language becomes specifications. Specifications become tests. Tests become code. Every step is grounded in a shared context instead of assumptions and is never validated by the same model. This approach is informed by recurring failure patterns observed in real AI agents development workflows: systems passed tests, shipped successfully, yet still failed to meet intent.

## Transcript

*2,148 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=1s)** [music] >> Trust me or don't. Um we have a trust problem. Um this is me um couple of days ago um building something with a cloud code uh that looks very impressive. Um 4 hours it churned almost 300 tests, all pass, amazing code coverage 95%. Uh a lot of modified files. Um cost Okay, I ignore this line. Looks pretty impressive, right? And then I run it. And then the clicker doesn't work. Uh here we go. And then I run it and then it doesn't work. Um sounds familiar? You can relate. Um this is me. And then I'm like, what? How that happened? And then I actually go and look at the code. And I see this.

**[0:54](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=54s)** Amazing code coverage, tons of tests, everything passed because nothing really run. So, yeah. Um the problem is what I call intent to code chasm. It's this huge chasm. Wait a second, important stuff. All right, thank you. Uh yeah. So, um the the chasm between what we wanted AI to do to what it actually did. We're going to talk about monkeys and we're going to talk about how can we trust or cannot trust them. And I wanted to ask you uh how many of you use AI for coding those days? Okay, everybody, right? Yeah. Oh, I don't know hands up. I I started to count and uh yeah. Okay, hands up. That wasn't a

**[1:44](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=104s)** hard instruction. Uh hand hands up who who uses AI for work. Thank you. Who trusts AI? Um no not the same one hand, two hands. Okay, two hands, not bad not bad. Well, um we'll get back to that. So, what are monkeys? You know the infinite monkey theorem? If you give to infinite number of monkeys infinite number of typewriters, given they have infinite time, eventually they will produce Shakespeare. This is AI. The only difference is we gave them GPUs. And it's not pure randomness. But it's still very much out there. Sometimes they produce working code, amazing Shakespeare. Sometimes they produce

**[2:31](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=151s)** somewhat working code. And sometimes they produce absolute garbage. Speaking about garbage, um you remember the movie Back to the Future? You remember the engine called Mr. Fusion? How Mr. Fusion works? What it gets in? Garbage. What it gets out? Energy. AI is exactly the opposite. You put a lot of energy in and you get garbage. Sometimes sometimes you get Shakespeare, right? So, that's exactly the thing. So um human software is not great. But we do our best. We do our best with good intentions. We work in this profession to produce good software. With professionalism. This is our job. We try to do the best as we

**[3:18](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=198s)** can. With tests and with QA that we hopefully run and not skip. And with end result observation. In the end of the day we go and look at this thing that we wrote. We also have commonish context. Everybody in the process know what we want to produce. With AI none of that applies. It doesn't have intentions. The professionalism is just a monkey typing on typewriter. Tests and QA you saw exactly what happens. End result observation does not exist like because it doesn't have eyes to observe anything. And there is no context. Every time you pop up in new AI session against an LLM model

**[4:07](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=247s)** it knows nothing about anything except of the pre-trained bunch of data that it will try to guess what do you want next. So, we noticed that it's not very good. This is a um a research from Coda, I think one of the sponsors of uh of this conference. And you can see how 76% are in the quadrant of low confidence in shipping AI generated code and observing high hallucinations. 76%. That's a huge number. And you'd say, "Okay, that's like today. In half a year the models will get better and we will be in another place." But it's been for couple of years already

**[4:55](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=295s)** where the models get constantly better. And our confidence in their code actually go down. So, if you look at the well, Stack Overflow kind of biased, right? Because people there are the ones who doesn't trust AI but to begin with. But even there you see how the number of people who trust AI actually declines throughout the years. Last year more people trusted AI than this year. And this is worrying. This is weird. The problem is context. So, I'll ask you a question. Who thinks AI does a great job in automated PRs to open source frameworks? No one thinks that. You all heard

**[5:45](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=345s)** terrible stories about how open source maintainers actually suffer from the avalanche of crappy open source of crappy PRs. About the imbalance of an effort to generate crappy PRs versus to review crappy PRs. But the statistics that the research says something entirely different. 86% of those AI PRs eventually get merged. 86% of the code that is in those PRs is actually good. The problem is that AI doesn't know how to open those

**[6:33](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=393s)** PRs. And this is something that the model cannot know. This is something that we can teach it by providing more context. And here is an experiment that I personally did. Um I wrote a piece of context, a skill that is packaged on how to be a good open source citizen. And here are the results. Without context a PR is just terrible. Couple of items here. There was issue that already claimed by another developer. AI went ahead and open another PR on the same issue. There was alternative issue issues that was completely ignored. There is an AI policy in this repo that got completely ignored.

**[7:22](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=442s)** But when we explained all this to our model, when we provided context, suddenly it went from 0% to a 100%. It is about not about the smartness of the model but about the context. Uh all right. So, how do we provide context? One of the ways is spec-driven development. Spec-driven development is about context. It's about us telling the model exactly how to behave in a certain situation. And spec-driven development is all the rage right now. Right? There everybody are talking about it. ThoughtWorks. There are research papers. InfoQ. Um Microsoft created GitHub created one of the most popular spec uh driven

**[8:13](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=493s)** development frameworks. Um Martin Fowler talks about it. And of course Andrej Karpathy talks about it. Everybody talk about spec-driven development. What is spec-driven development? We go to the model and explain to it how [snorts] we should write software. All the features in detail with a spec breakdown to tasks, everything it has to know. And then what do we do after we have the spec? Make no mistakes. The entire industry of spec-driven development is that. It closes the chasm between intent and spec. And then ignores the part of the chasm

**[9:01](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=541s)** between the spec and code. We suppose to trust that the code that will be generated from the spec will actually be good. And as we just saw we cannot trust the monkeys. One of the problems is circular verification. Who's in charge of producing the code from the spec? The monkeys. Who are in charge of testing this code? The monkeys. What can possibly go wrong? This is uh President Reagan and this is uh Secretary Gorbachev meeting in uh Reykjavik, Iceland in 1988. Uh talking about nuclear disarmament and

**[9:50](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=590s)** Gorbachev like, "Yes, we are going to disarm all our nuclear weapons for sure. Trust us, bro." And Reagan was like, "Doveryai no proveryai." Which means trust but verify. And that's exactly what we should do with AI. The key is whatever AI does, someone else has to verify. When Soviet tell you we're going to disarm, you are going to check. It's exactly what we're doing. Let's see how it should be done. So, the first artifact in our process is the prompt. We tell the AI what we want to get out of it. And it is created by humans. And it's a text document. It can definitely and should definitely be checked by other humans. This is our

**[10:39](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=639s)** verification. Then, we ask the monkey to generate a spec out of our prompt. It will ask us some questions. Do you want this button blue or do you want this button green? And it will write it in a format that is still human readable. It means that humans can go ahead and read it and verify it. The specs are different from the prompt because they are both human readable and machine possible. They are executable specifications. And this is brilliant because we can actually verify it by human eyes, but then executed by an algorithm, keeping the monkeys out of the loop of executing of

**[11:30](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=690s)** those specifications. So, the specifications verified by humans, but being executed as tests by the machines, no monkeys involved. Once we have those specifications, we can ask the monkeys to generate our code. We say, "Okay, go ahead. You have your specs. Generate the code out of it." Who is going to verify this code? Humans? Are we going to read this code? We are not going to read this code. We don't read other people's code. Barely. We don't read our code if it's 6 months year old or older. We definitely not going to read machine-generated code.

**[12:18](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=738s)** And that means that the only hope to verify it is by other machines. We have this verification in the executable spec. If we can run the spec, we know that it's actually works. The problem is that the spec is a piece of text that a monkey wrote. If we just let it sit there, the monkey will go and adjust the spec to match the code. So, what we need to do is to forbid monkeys from touching the spec. And we can do it by locking the assertions. Hashing,

**[13:07](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=787s)** making them read-only, putting them away from the hands little hands of the monkeys will guarantee that when we need to run them against the code and check that the code matches the spec, the spec is untouched. So, how does it look the entire thing? Software definition documents or whatever PRDs or whatever you call them are the prompt. This is what product people and business people write and we all review. LLM create the specs. And everybody read the specs and say, "Yes, this is exactly what we meant in our software definition documents." Algorithm generates the tests. This is the black box of executable specifications. There is a translation

**[13:55](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=835s)** that goes through pseudo language of the spec and generate actual tests for our code. And then LLM implements the test with verified assertions that are locked away. And it will keep iterating on the code until the test passed. Now, as we said, no one is going to read the code. The code becomes a side product of the specs. And the specs are those that people can read and agree upon. So, this works. Now, it also reminds us of waterfall. Remember how we go from the specs, break down, and then never looked at it until it's implemented, and it's terrible? The problem with waterfall is not that

**[14:43](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=883s)** the process is somehow bad. The process problem with waterfall is very long circles. From the time that someone wrote the spec to the time that someone look at the software with waterfall can be years. This is not a problem with our process. The intent integrity chain is going very fast. You will see the results almost immediately. And if something is wrong, you can go back to the spec and fix it in the spec and let it regenerate again. So, it's not a waterfall, although the process might look like because of the fast feedback and the speed of entertainment. Does it exist? Well, it does. Intent integrity kit is the implementation of

**[15:34](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=934s)** intent integrity chain. And it is a spec-driven process that actually goes all the way into the generating the code. It's obviously open source. You can go ahead and play with it. And never trust a monkey. This is the QR code when you see the slides and the link to intent integrity check kit and everything else. Obviously, five stars is the only rating that works. JBaruch everywhere. Talk to me here or anyone else. And what's this Amsterdam, by the way, the hashtag no one mentioned. It should be trending by now, right? After this, it will trending for sure. Intent integrity chain is the other hash code that you will make trending right now. And speaking of JBaruch, it's the same URL that in this QR code. Thank you very much.

**[16:22](https://www.youtube.com/watch?v=uvnxEZfSr1g&t=982s)** >> [music]
