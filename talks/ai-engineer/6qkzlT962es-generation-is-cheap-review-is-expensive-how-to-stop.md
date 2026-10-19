---
id: 6qkzlT962es
title: "Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i"
slug: generation-is-cheap-review-is-expensive-how-to-stop
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Generation Is Cheap", "Gabriel Martinez"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-09T20:00:07Z
video_id: 6qkzlT962es
url: https://www.youtube.com/watch?v=6qkzlT962es
youtube_url: https://www.youtube.com/watch?v=6qkzlT962es
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI slop", "code quality", "code review", "AI coding", "vibe coding", "software engineering", "engineering judgment", "technical debt", "pull requests", "Ruby on Rails", "conventions", "G2i", "Gabriel Martinez", "AI engineering", "AI Engineer"]
topics: ["AI in the SDLC & engineering orgs", "Coding assistants & agents"]
transcript: true
---

# Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i

**Generation Is Cheap, Gabriel Martinez**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI slop` `#code quality` `#code review` `#AI coding` `#vibe coding` `#software engineering` `#engineering judgment` `#technical debt` `#pull requests` `#Ruby on Rails` `#conventions` `#G2i` `#Gabriel Martinez` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=6qkzlT962es) · [Conference site](https://www.ai.engineer/)

## Description

Slop isn't AI-written code. It's work that looks finished before the thinking is.

Gabriel "Gabo" Martinez, engineering manager and self-described slop warden at G2i, explains what slop really is: what happens when generation outruns judgment, when ambiguity gets cleared with guesses and nobody notices there was a choice to make. He's not anti-AI, but argues we need to sober up. Code is still a liability, agents make a messy codebase messier faster, and quick prototypes convince stakeholders the hard part is done. He covers the pressure to merge faster than you can review, thousand-line PRs, 20-page AI docs that push the thinking onto reviewers, and why generation is cheap but evaluation is expensive. His fixes are conventions, diagrams as the review surface, small reviewable changes and clear ownership, inspired by Rails, plus why G2i built ORC.

In this talk:
• What slop is, and why it's about missing judgment, not AI
• Why code is a liability and AI makes the ball of mud bigger
• Incentives that push teams to merge faster than they can review
• Conventions, diagrams and small changes that keep humans in control

SPEAKER
Gabriel Martinez, Engineering Manager, G2i

LINKS
ORC by G2i: https://orc.ai
G2i: https://www.g2i.ai
G2i on X: https://x.com/g2i_ai

CHAPTERS
0:00 Intro
0:37 What slop is
1:12 The real danger: choices nobody saw
1:52 Time to sober up
2:27 What agents can't replace
2:51 How we got here
3:06 Code is a liability
4:01 A bigger ball of mud
4:11 Lines spent, not produced
5:01 Accountability
5:31 The prototype illusion
6:50 "It's not free"
7:25 Pressure to merge faster
7:45 Performance anxiety
8:45 Thousand-line PRs
9:30 The 20-page doc problem
10:14 Generation is cheap, review isn't
10:29 Twitter hype and the Ralph loop
11:39 Why code shape still matters
12:34 Diagrams as the review surface
13:18 Cognitive overhead
14:13 Lessons from Rails
15:43 Why we built ORC

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,833 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=6qkzlT962es&t=1s)** [music] Hi everyone, my name is Gabriel Martinez. I go by Gabo. I'm an engineering manager and resident slop warden at G2I. And I'm here to talk about slop. I'm here to talk about slop because I'm rather passionate about the topic. And by passionate, I mean angry. The term slop has been beaten to a pulp, but the thing it points at has long been around. Only now it happens at warp speed. All right. Slop is what happens when judgment when generation outruns judgment. Slop is not AI generated code. I don't mean to

**[0:49](https://www.youtube.com/watch?v=6qkzlT962es&t=49s)** define it as some concrete objective thing that can easily be sniffed out, although there are tells. Slop is output that looks finished before the thinking is finished. It is work product where ambigu ambiguity was cleared with guesses, where trade-offs were left to chance, where ownership was not taken. Output was produced, sure, but understanding was not. And the real danger is not simply that the machine made a bad choice. The danger is that the engineer never noticed that there was a choice to make. They never hit the ambiguity. They never felt the constraint. They never discovered the edge case that would have changed the design. The work arrived already smoothed over and with it the unknown unknowns stayed unknown. But software is a record of choices.

**[1:37](https://www.youtube.com/watch?v=6qkzlT962es&t=97s)** Technical choices, product choices, operational choices, userfacing choices. If we do not see those choices, we cannot own them. And if we do not own them, we are not really engineering. We are just accepting output. We are just a code monkey hitting the merge button. I'm not the purist that's come here to tell to tell you that AI is bad. It's not bad, okay? I'm here to describe some of the patterns that have led to our drunken AI stuper. It's absolutely understandable given the advancements made since December 25, how we got to where we are. But we need to dial it in. We need to slow down. We need to sober up. Agents can seem to make magic. And the internet would make you believe it is so. They can write code, scaffold screens, and with right

**[2:25](https://www.youtube.com/watch?v=6qkzlT962es&t=145s)** tuning can build whole features or systems. But they cannot replace the human work of deciding what matters, understanding what is being built, interpreting ambiguity, owning the system for the long haul, exercising judgment and restraint at the system architecture level, and arguably the most important important knowing what not to build. SLOP is not about AI as a tool. Rather, it is about the absence of judgment. So, let's talk a little bit about what got us here. In a world where anything is possible, deciding what to build is more important than ever. People have gotten overly excited and built behemoths of spaghetti product nonsense. It's almost as if they've forgotten that any line of code you write is a liability, that the best code is no code at all. The cost of creating code is falling, but the cost

**[3:15](https://www.youtube.com/watch?v=6qkzlT962es&t=195s)** of understanding a software program is not. And I want to be clear here. I'm not saying every line of code needs to be personally read, blessed, and understood in isolation. That has never really been the standard. Large systems have always contained more detail than any one person can hold in their head. But the logic has to be understood. The main flows, the boundaries, the data model and product behaviors have to be understood. Good software has a kind of harmony to it. Not in some precious aesthetic sense, in a practical sense. The code should reflect the shape of the domain. AI can generate code, but it cannot magically give a messy system coherence. An agent can operate with much more effectively inside a codebase that has structure, patterns, clear boundaries, and rationale. But if the system is already a big ball of mud, the agent

**[4:03](https://www.youtube.com/watch?v=6qkzlT962es&t=243s)** does not rescue you from the mud. It just builds the ball bigger, faster. Just because you can generate another component does not mean the product needs another component. Dystra had this great line. If we could count lines of code, we would not think of them as lines produced, but as lines spent. It is the cost of building. AI makes it easier to spend lines. It makes it easier to spend on files, abstractions, and complexity. But at the end of the day, you own the bill. That bill shows up as confusion, brittle flows, features nobody wants to touch because they don't fully understand. It shows up as product surfaces that technically do everything but feel like a maze. Think about that special kind of B to bloated B2B software where every task requires training where every screen has 12 escape hatches and nobody

**[4:52](https://www.youtube.com/watch?v=6qkzlT962es&t=292s)** can explain whether the complexity is there because users needed it or because teams just kept adding things. Teams should be held accountable for work they are producing. Accountability is the key word here. Taking ownership over the product you're building and having a way to tie that to positive or negative reinforcement. Just in the mere fact of knowing that someone else will review your work will force engineers to pay just a little bit more attention to the finer details and be a bit more meticulous, especially if there are accountability metrics that can be made visible for each chunk of work product. We're entering the age of bloated bloated products with spaghetti UX on the order of worst kinds of B2B ERPs you may have ever been trained to use. Today, anyone can buy code an application in an hour and end up with a working clickable prototype.

**[5:39](https://www.youtube.com/watch?v=6qkzlT962es&t=339s)** And that has changed expectations because once people see software appear that quickly, they start to believe software can be built that quickly. They see a few prompts turn into screens. They see a terminal session produce something that looks real. And to be fair, sometimes it is real enough to be useful. Sometimes that prototype is a great way to explore an idea. But the problem is that stakeholders do not live in the codebase of off that stakeholders that do not live in the codebase often experience that prototype as evidence that the hard part is over. They're not thinking about the parts where real battleh hardened engineers earn their keep. It's outside the happy path. Figuring out co how to cohesively integrate a new feature set. The the work involved in clarifying requirements. the work of actually manually testing a feature set to ensure that it works as a

**[6:27](https://www.youtube.com/watch?v=6qkzlT962es&t=387s)** human should expect and that the UX isn't complete garbage. They're not at all thinking about the most timeconuming bits, the human parts, the last mile where the judgment lives. This is where someone has to read the code, test the behavior, own the trade-offs, notice the missing requirements, and decide whether this thing deserves to be a part of the system. Here's a tweet that emphasizes the point I'm trying to make here. It quotes the creator of SQLite who on the topic of pull request says, "You say, 'Oh, it's free. No, it's not free. What you're doing is asking me to maintain it for you, to document it for you, to test it for you, to maintain it for you for the next 25 years. That is not free." And this really struck a chord with me. I couldn't have said it better. It's easy to yeet a PR, but who has to own that thing? Who's responsible for the

**[7:16](https://www.youtube.com/watch?v=6qkzlT962es&t=436s)** repercussions of what that means? So external pressures from stakeholders coupled with pressures of competing with slot misters begets mucho slopp. I'm sure most of you have seen this in the wild where the bad engineers, the ones who don't review the details, that don't refine the spec, that aren't detail oriented, end up producing more faster. The folks who pay attention to the detail and go above and beyond are the ones that might seem like they're doing less and moving slower. How this propagates is it yields performance anxiety where in team environments can pressure engineers to merge PRs faster than they can judge leading to code being merged without full understanding. Short-term thinking getting that PR in wins over long-term code health. I've

**[8:05](https://www.youtube.com/watch?v=6qkzlT962es&t=485s)** personally felt this anxiety where engineers around me were merging at an incredible pace and I felt constant anxiety that I was not moving fast enough. And I can admit that it led me to merge code that I didn't necessarily review with a level of detail that I normally do or should have. I've seen horror stories of people merging code they don't fully understand or haven't even tested themselves. At the end of the day, we're all human. We are driven by incentive. And if incentives are driving people to get PRs in, then we're going to be in for a rude awakening. Rewards should be centered around producing value. elegant, well-factored, pragmatic system design and around clarity of test and evaluation harnesses. There's just something that really grinds my gears about seeing a multi,000line PR. There's no way in hell that a human can fully understand all

**[8:54](https://www.youtube.com/watch?v=6qkzlT962es&t=534s)** the important bits of a change that big. It is our job as engineers to optimize for this new world, to decompose needs into its simplest chunks, which lends to understanding. understanding simpler code surfaces and controlling of our code bases. AI is supposed to have been eradicating jobs and engineers are supposed to be moving at the rate of token production. So there is a lot of pressure to be in producing more faster. What AI is really doing is producing more faster. More characters that eat more human time. I've seen this happen in the most mundane ways. You give someone 10 bullets of scope, a few user journeys, something intentionally lightweight, and they come back with a 20page document. Maybe it looks polished with fancy pros.

**[9:44](https://www.youtube.com/watch?v=6qkzlT962es&t=584s)** But now I have to spend hours figuring out whether there's any real thinking inside it. That is AI generated work in the worst sense. It does not clarify the problem. It expanded it. It took ambiguity that should have been resolved by the person doing the work and handed it back as a larger artifact for other stakeholders to do it. In code, a vague task becomes a large PR. A small feature becomes a pile of files. The output arrives with the shape of completion, but the real work has just moved to the reviewer. And that is the part that we need to be honest about. Generation is cheap, but evaluation is expensive. If AI produces more than humans can possibly evaluate, it has not accelerated the team. It has created a bottleneck.

**[10:32](https://www.youtube.com/watch?v=6qkzlT962es&t=632s)** One thing that I find particularly annoying is Twitter. You've got all these self-proclaimed experts and clickbaiters summarizing some talk or promoting some truths that we've always known as if there's some novel genius idea. The Ralph loop was one of those. It was made to sound like a novel agentic breakthrough when it's just a while loop. Somehow we've completely forgotten that lines of code is a garbage metric for productivity. But then we decided that it's different than deciding the engineer who burns the most tokens must be producing the most. We used to break a feature into small atomic pieces we could reason about. Small enough to hold in your head and actually review. Now we type two sentences and expect a whole not fully thought out feature set back in one shot without really understanding it what it

**[11:20](https://www.youtube.com/watch?v=6qkzlT962es&t=680s)** is we're asking for. The key point I want to highlight here is that we do not forget the ground truths we've always known. 60 years of software wisdom hasn't been invalidated by AI. Composable code, good patterns, and solid practices remain essential. A friend recently challenged me on why I spend so much time thinking about guard rails for agents, coding conventions, architectural styles, and and constraints around how the system should be shaped. His question was basically what's the point if the agent writes the code why should we care about what the code looks like and to an extent I agree there will eventually be a world where much implementmentation detail is completely abstracted away from humans that has

**[12:08](https://www.youtube.com/watch?v=6qkzlT962es&t=728s)** been the soft the direction of software from the beginning we went from machine code to assembly which another of level of abstraction up got us to C then Java then languages like Ruby where the primary design goal was programmer happiness. Just like in languages, we built abstractions for garbage collection and manual pointers, AI is abstracting away the imperative bits. It does not remove the need to understand how a system comes together cohesively. This is why diagrams matter so much, not as decorative documentation after the fact, but as a way of making systems legible. When a agents can generate thousands of lines of implementation detail, humans need a compressed review surface. service boundaries, data flows, state transitions, and failure modes. A good diagram lets us see the shape of

**[12:56](https://www.youtube.com/watch?v=6qkzlT962es&t=776s)** the system in a way code often obscures. We can leave the main process or workflow as the reviewable surface with implementation details pushed to the leaves. That is why I vouch for declarative code and architecture patterns that create layers humans can actually reason about. The goal is not just code generation. The goal is human knowledge, human understanding, and human review. We need to optimize for that human layer. Cognitive overhead is a tax every engineer has to pay before they can make a meaningful change. It is the time spent figuring out where code belongs, which pattern to follow, and what proper implementation actually means. AI does not remove this tax. Unless tamed, it exacerbates it. An agent can generate five plausible patterns in five

**[13:46](https://www.youtube.com/watch?v=6qkzlT962es&t=826s)** different styles. And now the human reviewer has to reverse engineer not just the code but the intent behind it with proper conventions intent is more easily gropped. The answer to this is conventions standards documented flows small reviewable surfaces and clear ownership boundaries and definitions of done. The more obvious the path, the less room there is for slop to hide. I want to give special recognition here to Rails and its place in my heart. Rails matters here because it shows what happens when a framework aggressively reduces decision surface. When conventions reduce your overhead rather than ending up with 10 different ways to structure the same concept, you end up with one.

**[14:33](https://www.youtube.com/watch?v=6qkzlT962es&t=873s)** It may not be perfect in everyone's subjective opinion, but it's understood and it works. In my career, between my first and second 4A with Rails, I had a gap of four years. It was beautiful to come back after that gap to see that the same patterns in de facto libraries were still the same patterns and de facto libraries. I could hop right back into a codebase and immediately understand intent without needing to parse through architecture. It allows engineers to easily move between projects laterally with minimal ramp up. The same can't be said about other language ecosystems. JavaScript environments with a single correct way of doing things are superior for agentic development because agents aren't confused by dozens of competing

**[15:21](https://www.youtube.com/watch?v=6qkzlT962es&t=921s)** approaches. This is well supported by the official Rails doctrine. It explicitly names optimize for programmer happiness and convention over configuration as core pillars and describes convention as a way to eliminate recurring decisions and lowering the barrier to getting started. It is the reduction of cognitive overhead. Everything I've talked about today is what led us to build ORC. Not only because we think the answer, not only because we think the answer is more agents and definitely not because we think engineering judgment can be automated away. We built ORC because we kept seeing the same failure pattern. AI could generate code but the surrounding discipline was still missing. The planning, the review, the adversarial checks, the context management. Over

**[16:10](https://www.youtube.com/watch?v=6qkzlT962es&t=970s)** time, we found ourselves repeating the same human processes to fight slop. break down the work, manage context, weigh out your options, and make sure the output enters the codebase in the way the team can still reason about. ORC is taking those lessons and baking them into the workflow. It is not a magic box that makes correctness disappear as a human responsibility. It is a system for preserving that responsibility while letting agents do more of the lift. The goal is not to ship more generated code. The goal is to ship software that is still coherent, tested, maintainable, and owned after the generation happens. Because the future is not vibe coding better, faster. The future is orchestration with judgment. Thank you all for your time and remember, don't get sloppy.

**[17:14](https://www.youtube.com/watch?v=6qkzlT962es&t=1034s)** >> [music]
