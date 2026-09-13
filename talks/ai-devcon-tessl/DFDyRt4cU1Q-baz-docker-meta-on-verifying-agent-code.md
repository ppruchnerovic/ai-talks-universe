---
id: DFDyRt4cU1Q
title: "Baz, Docker & Meta on Verifying Agent Code"
slug: baz-docker-meta-on-verifying-agent-code
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-10T15:00:16Z
video_id: DFDyRt4cU1Q
url: https://www.youtube.com/watch?v=DFDyRt4cU1Q
youtube_url: https://www.youtube.com/watch?v=DFDyRt4cU1Q
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration"]
transcript: true
---

# Baz, Docker & Meta on Verifying Agent Code

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=DFDyRt4cU1Q) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Coding agent reliability fails at verification, not generation. A lot of speakers at AI DevCon London said a version of the same thing: the hard part isn't writing the code, it's proving it does what you asked. Four of them on what they tried, and what actually pinned the behavior down.

Shachar Azriel (Baz) wrote a detailed spec, attached a screen recording of the exact bug he did not want repeated, and got that exact bug back — coding agents are built to generate features, not to fully extract a spec or verify the result. Justin Cormack (formerly CTO at Docker) wrote 350,000 lines of Rust with agents, chased 100% test coverage on the advice going round, and found the agent writing tests for a failing random number generator; what actually locked the behavior down was 1,500 tests run against S3 as a test oracle. Ian Thomas (Meta) heard "can we trust the code?" in nearly every workshop he ran, and answered it with an anti test slop initiative that uses a different AI tool to judge whether AI-generated tests are worth having. And Christopher Batey on what you do when a 7,000-line pull request lands: stop pretending you can review it, and move the human decision earlier into architecture decision records that agents are then very good at checking code against.

What we cover:
– Why coding agent reliability breaks down at verification rather than generation
– What happened when a spec came with a video of the exact bug to avoid
– Whether 100% test coverage means anything across 350,000 agent-written lines
– Using a real system as a test oracle instead of testing the impossible
– Meta's anti test slop initiative, and judging AI's tests with AI
– Moving the human review earlier, into architecture decision records

Chapters:
00:00:00 - Introduction
00:00:22 - Shachar Azriel, Baz: the spec, the recording, the same bug
00:02:01 - Why coding agents optimize for generating, not verifying
00:02:38 - Justin Cormack, ex-Docker: 350,000 lines of Rust with agents
00:03:01 - Chasing 100% test coverage, and why it didn't help
00:04:40 - Using S3 as a test oracle to lock down behavior
00:04:59 - Ian Thomas, Meta: can we trust the code?
00:06:28 - The anti test slop initiative, judging tests with AI
00:07:01 - Christopher Batey: what to review in a 7,000-line PR
00:08:30 - Architecture decision records as the human checkpoint

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What's actually pinned down behavior for you — tests, specs, or ADRs? Tell us in the comments.

## Transcript

*1,859 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=0s)** Back in June at AI DevCon in London, a lot of speakers said a version of the same thing. The hard part isn't writing code. It's proving that it does what you asked. Let's first hear from Shachar Azriel, VP of Product at Baz, who wrote a spec, attached a recording of the exact bug he didn't want, repeated, and got that exact bug back. Part of what we wanted to do is to add this to the onboarding flow of the product. So when a user is onboarding to Baz, they will have the option to integrate whichever of the ticketing systems available that they have. And because I'm reviewing every product, every feature that is being released, I asked to make sure that the same bug that happened when we integrated another ticketing system won't repeat again. I literally added a recording from a previous time

**[0:53](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=53s)** when we added another integration where the continue button was overlapping the new integration that was added a couple of days later, the developer sent me a slack message telling me, hey, I just completed that feature. Here's the link to Preview Environment. Please review it. Guess what? The continue button is exactly where I asked him not to put it. Guys. Like, I couldn't be more explicit than that. And I'm showing this because this is a really simple example, right? Like, for those of you who are part of an engineering team? Product design. This is our day to day frustration. We're writing specs. They are very detailed and we're very happy

**[1:42](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=102s)** to deliver them to the engineering teams that we're working with. But unfortunately when we see the results is not as we expected. And you can understand that if this is such a front-end simple task that's gone wrong, how like what would be the results if we're doing a complex task? So the bottom line is that coding agents that we are using are not focused on verifying features. They are amazing at generating code. And I think one of the themes that is repeated in a lot of the talks here and in other conferences is the fact that it's so easy to build right now, but the way that the coding agents are built, they are focused on generating features. They are not focused in fully extracting all the specs that we have, all the specs that we write, and they are not focused in verifying the feature as it is.

**[2:38](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=158s)** We also heard from Justin Cormack, formerly CTO at Docker, who wrote 350,000 lines of Rust with agents. He tried the advice about chasing 100% test coverage, and found the agent writing tests for things that cannot happen. What actually pinned the behavior down was pointing his tests at the real thing. I keep hearing people say, well, with AI, all you need is 100% test coverage and you're done. And it's like, so but I did try that. I started off trying to get 100% test coverage. It seemed like a good idea. And I also measured different measures of 100% test coverage from test coverage, from integration tests. And it didn't really didn't really help a lot.

**[3:30](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=210s)** I found they were kind of better uses of my time than trying to get 100%. You know, I sat down and I asked an AI agent to get 100% test coverage. It kind of wrote trivial tests that were like, I don't, you know, this is a stupid test. I don't care about that. And there's also a lot of weird error cases that are really hard to cover. I mean, I went through and asked the agent, like, well, why haven't we got 100% coverage from this? It was like, we don't have a test for when the random number generator in the system fails. And I was like, yeah, I don't think I want to write a test for that. Like, that's just too much error injection. Like I can see that there's a, you know, it's going to it's going to give an error or it's going to panic and that's the right behavior. I don't need to have test coverage for that on all my test suite. But I still have a lot of tests.

**[4:20](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=260s)** I mean, 75% of my code base, test coverage is between 75 and 100% for each file. Like, it's like you can still have a lot of tests without being really obsessive, about 100% test coverage, which I think is not really the right kind of aim. The great thing about copying an existing system like S3 is you've got this test oracle. You can find out what happens when you do something. You run the test, you can run it against the you can run it in my case against S3, and I have 1500 tests that run against S3 and they lock down the behavior. Ian Thomas at Meta ran workshops across the company and found the same worry coming back from nearly every team. Can we trust the code?

**[5:08](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=308s)** Their answer was an anti test slop initiative, using AI to judge whether the AI's tests are worth having. One of the things in Meta that we use a lot is called Workplace, which is essentially an internal version of Facebook. So every time anyone ran one of these assessments, they would post the results and they would share the insights they'd uncovered. And so it was a case of everybody else would then get visibility into what other teams were doing, raising up the network effect. One of the big things that came out from pretty much every single workshop was, can we trust the code? And it was one of the big reasons of the senior engineers was slightly hesitant about adopting AI tooling in the first place. They wanted to have control. They liked finessing what they were doing. They like to feel that they had the craft in hand. And that was great because it told us where we could focus on more cross-cutting efforts as a leadership group, a team that were looking to help

**[6:01](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=361s)** the adoption curve. We could find ways to to unilaterally improve people's experiences. So on the back of things like we were, we were looking at testing and how we could increase our test coverage and reduce flakiness, to Justin's comments before. Well, we were seeing that AI was great at hallucinating awful tests. It would make stuff that was really looking like it was doing something useful, but it really wasn't, and it was just increasing our overhead on CI. So we invested in an anti test slop initiative, where again, on CI, we could go and validate the changes that were being made in an autonomous way, using a different AI tool to judge the quality of the output. And these things are, again, examples of the ground-up culture that we have is that this thing started out in Horizon, but the test slop initiative that we started and the tooling that was built

**[6:51](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=411s)** was eventually adopted by infra and rolled out across the whole company. And I think to date, it still runs pretty much on every diff. That's got significant volume of AI generated tests in it. And to close, Christopher Batey on what you do when a 7,000-line pull request lands. His answer is to stop pretending you can review it and move the human decision. Earlier. Architecture decisions get their own reviewed pull request. After that, agents are very good at checking code against them. Now, I could just describe the feature I want, the feature I want which would combine this, and I'm pretty confident that our agentic workflow would build it. And then maybe a pull request is going to land, which is maybe 7,000, 7,000 changes. And then what would I be reviewing it for?

**[7:39](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=459s)** Well, I first want to be reviewing it for the systems thinking. So here's some questions which I just threw together about what I'd want to know about this change. How does the client side connect to the managed service? What does it connect to? How does it authenticate and authorize? Because this is a client side component. Talking to a multi-tenant managed service, what parts of the managed service are exposed to the internet? We're very careful about not exposing things. You know, do we ever share an API which is used by a human-usable front end versus like an agent system? What data can pass from the client to the managed? What data can pass from the managed to the client? There are different deployment mechanisms, right? We do continuous delivery virtually every commit for the managed service. But the client side, that means that we need we need to do something on our client. And maybe that might get updated once a week because it's deployed to their systems. So that's the type of thinking I definitely want to keep

**[8:27](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=507s)** in the engineers that I work with. So one thing we do now is when we're planning whatever work we're going to do in the next week is if we think there's a system-level decision that always comes as a completely separate pull request in something called an architectural decision record. If you've not come across those, Google them. It's about documenting your technical decisions along with your code so that you can. Someone can quickly learn why we made the decision, so we don't keep on discussing them again. And we've always used ADR, or at least for a very long time. And we've always used ADRs, or at least for a very long time. agentic development, all of the agents loved writing ADRs. They were very good at seeing that we had ADRs. So they wrote more ADRs, and our ADRs got longer and more verbose. And not a single human understood them, which completely defeated the point of having them. So what we did is we said from now on, we're going to start with the ADR. I, me as a human, I'm going to spend a lot of time reviewing it. I want diagrams, I want them to be visual so I can understand them.

**[9:18](https://www.youtube.com/watch?v=DFDyRt4cU1Q&t=558s)** And then humans reviewing them can really put a lot of effort into reviewing those architectural decision records. And once you've got those agents are really, really good at reviewing implementations against well-structured architectural decision records, not only when you eventually land the implementation, but all of the follow up requests then. Because one thing I don't think humans are good at is keeping all of those ADRs in your head, and then subsequent pull requests, which subtly, perhaps change your system architecture. You might not realize that something's happened. Something's happening like a new API is exposed. But what we actually do is have the ADRs constantly reviewed against all of the pull requests that come Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
