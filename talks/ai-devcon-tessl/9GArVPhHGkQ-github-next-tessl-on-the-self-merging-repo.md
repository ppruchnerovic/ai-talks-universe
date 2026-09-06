---
id: 9GArVPhHGkQ
title: "GitHub Next & Tessl on the Self-Merging Repo"
slug: github-next-tessl-on-the-self-merging-repo
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 11
published_at: 2026-09-02T20:00:31Z
video_id: 9GArVPhHGkQ
url: https://www.youtube.com/watch?v=9GArVPhHGkQ
youtube_url: https://www.youtube.com/watch?v=9GArVPhHGkQ
tags: []
topics: ["AI in the SDLC & engineering orgs"]
transcript: true
---

# GitHub Next & Tessl on the Self-Merging Repo

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=9GArVPhHGkQ) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

The software factory arrived in the repo before anyone announced it. Four speakers at AI DevCon London got there from completely different directions, and all four ended up describing the same shift — from writing the code to designing the system that writes it.

Don Syme (GitHub Next) makes the case that we've been missing a pillar all along: it isn't CI/CD, it's CI, CD and continuous AI. He now wakes up to code improvements his repository made overnight. Paul Stack has taken it about as far as anyone — agents write every line, five gates run in CI, and when everything passes the pull request merges itself. In the last 30 days that was 295 issues opened and 217 shipped, by five people, for around $3,000 a month. Patrick Debois (Tessl), the person who gave us the word DevOps, names the reflex that's hardest to give up: when the agent gets something wrong we jump in and fix the code, when what needs fixing is the system that produced it. And Robert Overweg closes with one brain for his whole company — knowledge he can question from his phone in plain language, plus an agent that reads the internet overnight so he wakes to a briefing rather than a backlog.

What we cover:
– What continuous AI means as a third pillar next to CI and CD
– The five gates that let a pull request merge itself
– Why "the tests are the source of truth" is the line that makes it safe
– 217 issues in 30 days by five people, and what it costs to run
– Fixing the system that builds the code instead of the code
– Turning company knowledge into something you can just ask

Chapters:
00:00:00 - Introduction
00:00:19 - Don Syme, GitHub Next: CI, CD and continuous AI
00:01:33 - Why individual productivity is the wrong unit
00:02:37 - Paul Stack: five gates in CI, then the PR merges itself
00:04:14 - "The tests are the source of truth. Don't change the tests."
00:04:30 - 295 issues opened, 217 shipped, in 30 days
00:05:19 - Patrick Debois, Tessl: fix the system, not the code
00:06:49 - Specs, tests and observability as the system
00:07:55 - Robert Overweg: one brain for the whole company
00:09:28 - The cron job that reads the internet overnight

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which pillar is missing from your repo right now? Let us know in the comments.

## Transcript

*1,693 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=0s)** Back in June at AI DevCon in London, several speakers arrived at the same idea from completely different directions. Let's first hear from Don Syme of GitHub Next, who makes the case that we've been missing a pillar all along. It's not CI/CD, it's CI, CD and continuous AI. We went back a year ago and we kind of did a conceptual project. It's almost like a linguistic project in a way to say, let's take the ethos of continuous integration and continuous deployment, and let's say, actually we were missing something all along. There's a third pillar to that. There's actually three. It's not CI/CD, it's CI, CD and continuous AI. And in a way, what do we mean by that?

**[0:55](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=55s)** Well, let's start to give that some, some, some. If we're going to introduce a term like that, we have to give it some meaning. Give it some body. And when you start unpicking it, The examples are absolutely everywhere. And there are lots of people in the industry doing continuous AI, making offerings about automated uses of AI in our development processes. And you see people coming up with flows. Some of them are automated, some of them are semi-automated about continuous documentation. And then when you start to think about it, it begins to have a different feel to individual productivity, a different emphasis. The problem with piling everything into individual productivity is that all these kind of conflicting kind of goals that the individual is under, they have to be productive, but they also have to be quality.

**[1:45](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=105s)** They have to, they have to. They've got to flow. They have to serve the work queue coming in, but they also have to work on one particular item. And so the individual becomes a bit of a kind of crunch point for all the information flows going through a software project. And when you start to think of things in continuous terms, you can start to unpick that a bit and you can talk about things like, actually, I would like to have continuous code improvement in my repository. And, and, and it's actually real. And if you want to get a feeling for what my kind of day is like it's on my blog, you know, here's a typical morning. I wake up to code improvements, start my day with code that's better provided by my continuous improvement processes

**[2:37](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=157s)** so. We also heard from Paul Stack, who has taken this about as far as anyone. Agents write every line. Five gates in CI. The pull request is auto-merged. 217 issues shipped in 30 days by five people for about $3,000 a month. When everything passes, it merges itself. I'm not kidding. Okay. The reason I'm not kidding is if I show you this pull request merged just before I got on the stage. And you can see the pull request was opened by my agent. It had the first review, then this one passed.

**[3:24](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=204s)** Then it got a big old block on review. I can't do that. The agent then figured out that it had to push some changes. Right here. Keeps going. This is all context. It's incredibly important. There's the new change, and the agent was actually able to go and reproduce itself, figure out that everything was fine. These suggestions are all okay. And then it auto-merged itself and kicked in. Okay. We're not doing anything like out of the ordinary here. We're just trusting a process that we continually hone in that process. So for us, the gate is our UAT. Just because something has merged doesn't mean it automatically gets to an end user. We have this whole level of test that that goes through, and we catch regressions every single day before it goes to end users. Absolutely every single day. And it blocks our pipeline. And nobody else can, like, publish a release out there until that's fixed.

**[4:14](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=254s)** Now the most important thing is here is in our UAT repo, we have a line that says the tests are the source of truth. Don't change the tests. Always figure out if it's a regression in the binary. Okay? And what we've ended up with in the last 30 days is 295 issues have been opened. And that's issues. Not just bugs, but feature requests, etc. I shipped 217 of them. I closed 81 as either duplicates or just not things that we're going to do. The median time to triage — and this is not work hours, This is like elapsed hours in a day is 4.6 hours. And from triage the whole way through to ship, including all of those gates is 1.6 hours. Okay. There's five people. The company I work at, each of us has a Claude Code Max Pro, which is $200, and then we spend about 1500 to $2000 per month.

**[5:08](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=308s)** On the whole CI review process. We're able to ship software many times faster now for $3,000 per month than we were ever able to do before. Patrick Debois is an AI product engineer at Tessl, and he's also the person who gave us the word DevOps. He names the mistake almost everyone makes when the agent gets it wrong, we jump in and fix the code. What we should be fixing is the system that produced it. And I mentioned like build the thing that builds the thing. One of the mindset challenges that people have is even if the agent gets things wrong, they jump in and they correct a mistake. What they really should be doing is improving the system that builds the code and improves that, so they don't have to do it again.

**[5:59](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=359s)** So it's not about fix the code, it's fix the system. And a lot of systems engineers and platform people, they think in system mentality. And that's why it's also quite natural to kind of think in those terms. It's for me right now in the industry still the like one of the predominant mistakes is that you still go in and jump in and correct and take over. The mentality should change to fix the system and have the agent flow to that. So I mentioned it like what good looks like. Claude learned that we should have planning before doing something. We should have testing to see whether the agent did something well or not, or what do we pull the trick and change functionality that we didn't want?

**[6:49](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=409s)** I always say, like, I never knew I would see the day that developers would start writing documentation on their own, but they learned that actually by writing specs or whatever you call it, context, all of a sudden things become better. And then if you add observability, the agents can actually kind of observe themselves and improve, right? Nothing new, it's just rehashed with the new mindset. It's not all the agents doing that stuff, okay. So that reusability comes into not changing the context and the problems you think about. Reusable specs kind of make that and that goes to both harness components. Tools make them reusable. Now, it's very tempting to not listen to whatever happens in the production. And yes, as a dev, you've never been used to like being told, like, you know,

**[7:42](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=462s)** the only thing that matters is how your end user is having issues. And those have been signals that we've been trying to educate that like whenever you see a signal that is not performing well, change the system and improve that. So. And to close, Robert Overweg, who built what he calls one brain for his whole company. Company knowledge. He can question from his phone in plain language. And an agent that reads the internet overnight. So he wakes up to a briefing rather than a backlog. Right. I have sort of all, not all most of our company knowledge on my phone. And I can just send voice messages, voice messages, or type myself to surface the information, which is really, really valuable. So one example here I can talk through natural language. So I again forgot what we wanted to implement in our CI/CD pipeline.

**[8:36](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=516s)** And but I did remember that it was from Microsoft and they had like these four steps or something. So I just asked my, my agent, what was that thing again for the, for CI/CD things. And then it says, oh, you probably mean this and this and this and this, which was actually accurate. And then it also because it understands my context. It also asked, is this for the talk? Which is also really useful. So I just continuously have this sparring buddy. So what we're doing is we no longer search for files, but more like for ideas and context and those kind of things, which is a massive game changer. Then we have agents as well. So I have an agent that proactively does search for me, and I have an agent that is able to interpret search that I find myself. I want to show some examples here as well.

**[9:27](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=567s)** Maybe you guys have this already, right? And this is really also quite basic, but we have a cron job or I have a cron job that runs on my OpenClaw that tracks certain accounts on X, those accounts, just, on just some specific words so you can think of agentic engineering or, or any words that relate to such pipelines that I'm interested in. I follow some niche accounts as well. Or niche. I think a guy has maybe like 120K followers, maybe not that niche, but I do stay in in touch with everything that is happening. And it's almost like my newspaper because I don't read the newspaper, but I read everything. evolving around agents and AI and those kind of things. And that's being surfaced to me, daily in the morning.

**[10:17](https://www.youtube.com/watch?v=9GArVPhHGkQ&t=617s)** Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
