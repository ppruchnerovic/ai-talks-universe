---
id: 606n8YC_-fU
title: "Spec-Driven Development: Specs Are the Program Now"
slug: spec-driven-development-specs-are-the-program-now
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 8
published_at: 2026-09-14T16:00:11Z
video_id: 606n8YC_-fU
url: https://www.youtube.com/watch?v=606n8YC_-fU
youtube_url: https://www.youtube.com/watch?v=606n8YC_-fU
tags: []
topics: ["AI in the SDLC & engineering orgs"]
transcript: true
---

# Spec-Driven Development: Specs Are the Program Now

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=606n8YC_-fU) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Spec-driven development is having a moment: teams write two weeks of specs and generate the code in five minutes, then throw it away and generate it again. At AI DevCon London, Simon Martinelli, Dave Farley and Shachar Azriel of Baz showed what changes when the specification, not the code, becomes the thing you actually maintain.

What we cover:
– How spec-driven development turns code into a disposable output
– Reverse-engineering specs out of a codebase nobody documented for a government client
– Why Dave Farley thinks the program is now the problem, not the solution
– Writing a domain-specific language precise enough for an agent to build from
– Why teams write better specs once they know an agent is reading them

Chapters:
00:00:00 - Introduction
00:00:24 - Simon Martinelli: two weeks of specs, five minutes of generating
00:01:20 - Modernizing a government system, spec-first
00:02:19 - Dave Farley: the program becomes the specification
00:03:58 - Designing a language for precise, testable specs
00:04:56 - Why AI can't infer your security requirements
00:05:31 - Shachar Azriel, Baz: why point an agent at specs, not tests

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which part of your spec would you trust an agent to build from today? Tell us in the comments.

## Transcript

*1,141 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=606n8YC_-fU&t=0s)** Back in June at AI DevCon in London, we had a set of talks that all pointed the same way. If the specification is the thing you actually maintain, then the code becomes an output. Something you can throw away and generate again. let's first hear from Simon Martinelli, a consultant in Switzerland who does this on real enterprise systems and has a lovely way of describing the new shape of the work. Two weeks of specs. Five minutes of generating. And something that I didn't talk about is in my opinion, specs are very sustainable or hopefully they will be sustainable in the future because currently what I'm doing is reverse engineering of existing code into specs. And if we have specs, we can probably generate the same application in different technology with a different UI.

**[0:49](https://www.youtube.com/watch?v=606n8YC_-fU&t=49s)** Maybe we don't have even a UI, we have chat or something directly from the specs and the business people can directly change the way the systems should behave without developer, so they don't need developers talking about that or looking into that. And this accelerates development. The problem is at the moment. It just accelerates development. Right. So the requirements phase and the spec phase takes some time. For example I'm working for this government for the Parliament. They are have a business case management software that we want to modernize. And I'm the only one during the proof of concept doing something with code. But we have two product only requirements engineers that work on the spec, and they have much more work to do than I have, I trust automate everything.

**[1:42](https://www.youtube.com/watch?v=606n8YC_-fU&t=102s)** So currently I'm working on on a pipeline that they can just change the model files and everything will automatically generate it. So the kind of the work moves or shifts left, so everything shifts left to requirements engineering in my opinion, because now that's obvious before we add like if it did scrum, you had two weeks to work on the requirements somehow. And then we are two weeks working on the implementation. Now you have two weeks and then five minutes and two weeks, something like that. Right. We also heard from Dave Farley, who takes the idea further than most. A program used to be a precise solution, with the problem left implicit in our heads. He thinks it becomes a precise description of the problem, and the AI does the translating. So how should programing change to keep up with all of this?

**[2:36](https://www.youtube.com/watch?v=606n8YC_-fU&t=156s)** So problem one specifying what we want with precision. In the past, the way that we did this was that a program was a precise solution encoded as algorithms. Weirdly, we kind of lost what the problem was. It's kind of implicit in our solution, but we'd keep that in our heads and we'd build a solution, and that would be a definition that we'd work to. But the solution itself was implicit. So in this in my example, this is a routing algorithm. So I'd like to find my way home is the outcome that I'm trying to achieve here. In the future

**[3:26](https://www.youtube.com/watch?v=606n8YC_-fU&t=206s)** a program will be a precise description of what it is that we want, I think encoded as specifications, translated into executable instructions by the AI that will verify that we got what we wanted and what we want now is explicitly part of if you like the program. So the program moves away from being solution focus to being a more accurate description of the problem that we're trying to solve. I'm describing a form of spec-driven development, but the specification takes the form of executable specifications tests. If you like that, both specify what we want and also verify that we got it. What it takes to achieve that program.

**[4:20](https://www.youtube.com/watch?v=606n8YC_-fU&t=260s)** I've just just repeating what I said designing a domain specific language, if you like, for specifying what it is that we want from our software with a deal of precision and then specifying what we aim to achieve in detail all of the time. And those those are all of the behaviors of the system, not just the conventional user behaviors that we might think about. We're not talking about sketchy testing of the system, but all of the behaviors of the system. So how fast would we like the results back? If performance matters, how secure do we want it to be? If we want secure our system to be secure? Because all of those are contextual, you can't have the AI to infer that to make it up, because it depends the real how security you want your system to be. You'd be stupid to apply the level

**[5:09](https://www.youtube.com/watch?v=606n8YC_-fU&t=309s)** of security to a single user game. Then you would. If you were building a system for a bank, because you'd be over engineering the game and probably under engineering the bank. So you need to be specific about what it is that you're trying to achieve And to close, Shachar Azriel of Baz, answering a good question from the audience. Why point an agent at the spec rather than have it right? Tests. And there is a lovely side effect in his answer. Once teams new an agent would read their specs, they started writing better specs. The problem that I have with tests is that they test things that nobody really like. They're not testing real life. Like teams are sitting and thinking about these imaginary scenarios that are not going to be not going to happen any time in your product.

**[6:00](https://www.youtube.com/watch?v=606n8YC_-fU&t=360s)** And there are plenty of AI code coding tools that generate tests like here, take like 100, 200, 500 unit tests. And in the end of the day, there is one scenario that you're not thinking about. The idea we chose this specific approach is we wanted to leverage data that is already there. Like, I don't want someone to think about scenarios that that should that might happen or might not. And let's use the specs to do that. By the way, the byproduct of this process, and I didn't talk about it, but I heard about it from a lot of our customers, is the fact that when they knew that the specs are used to be for the to the agents to verify the feature, it encouraged them to write better specs.

**[6:52](https://www.youtube.com/watch?v=606n8YC_-fU&t=412s)** So it's like renewable energy, right? Like, I'm bringing a new tool that improves best practices and improves and encourages product managers and designers to be more specific in the way they write specs. And I think that, like if testing was the answer, there wasn't room for this. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
