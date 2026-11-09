---
id: 1FDAowpMReo
title: "Introducing Tessl Verifiers: Enforce AI Coding Standards in Every Change"
slug: introducing-tessl-verifiers-enforce-ai-coding-standards-in
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 4
published_at: 2026-10-02T07:57:10Z
video_id: 1FDAowpMReo
url: https://www.youtube.com/watch?v=1FDAowpMReo
youtube_url: https://www.youtube.com/watch?v=1FDAowpMReo
tags: []
topics: ["Coding assistants & agents"]
transcript: true
---

# Introducing Tessl Verifiers: Enforce AI Coding Standards in Every Change

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `4 min`

[Watch the recording](https://www.youtube.com/watch?v=1FDAowpMReo) · [Conference site](https://tessl.io/devcon/)

## Description

Your coding agent knows the rules. But does every change actually follow them?

Introducing Tessl Verifiers, a way to write rules for your repo in plain language and automatically check them on every code change.

Verifiers are designed for standards that traditional linters and tests can’t reliably enforce, such as:

• Every user-facing error tells the user what to do next
• Every API route uses your typed response helpers
• No handler logs request headers, tokens, or passwords

Each verifier returns a clear pass or fail, so you can use it like lint or tests: run it locally, in pre-commit, or make it a CI gate.

In this video, we cover how Verifiers work, when to use them, how to create your first verifier, and how to start enforcing your coding-agent standards in CI.

Verifiers is generally available now.

Get started:

## Transcript

*757 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=1FDAowpMReo&t=0s)** Hi, I'm Macy and I'm here with Amy from the research team and we're going to be talking about Tessle verifiers today. So Amy, maybe before we get into what exactly they are and how they work, maybe you could talk to me a bit about the problem we're trying to solve. >> Yeah. So what we've seen is that as agents write more code and people write code faster, there's been a real problem at the review end. So PRs kind of pile up and engineers end up having to review lots and lots of PRs. They're trying to kind of steer the agents to know follow conventions that they care about or kind of consistently make a good user experience. It gets pretty overwhelming to stay on top of all the PR. So we started from that point of kind of

**[0:47](https://www.youtube.com/watch?v=1FDAowpMReo&t=47s)** realizing well how can we give more tools for expressing what you want from the [music] code, what expectations you've got, what invariants you want to fix. So there are a number of ways I feel to kind of improve the reviewer [music] experience and and one of them is code review. How are verifiers meaningfully different from code review? >> So it sits basically between code review and linting which would be how you do kind of deterministic checks. So somewhere in between where we still have something that needs a little bit of judgment, but we can make it into a really clear rule that a single judge call could look at a file and say yes, that rule is followed. So it feels more like a checklist than it feels like an open-ended ask to an agent to go and [music] investigate. So we've seen it sit alongside code review really nicely

**[1:34](https://www.youtube.com/watch?v=1FDAowpMReo&t=94s)** because what you can find is that in a code review, the agents might be finding the same kinds of things over and over again or your human reviewers might find the same things. So they might keep on having to say to an agent, >> you know, remember this detail that I told you before. Remember this detail before. And we don't want to then rely on the agent always remembering to find that thing. We want to codify that rule. We want to make sure it gets followed consistently. >> Maybe we can dig into like [music] what exactly a verifier is kind of what the form factor is. So these are rules about invariance that you want [music] to have followed in your codebase that we can check using a model as a judge. If I give a couple examples from our own codebase, we've got one that says in our front end [music] whenever we show an error message, we should also show you

**[2:22](https://www.youtube.com/watch?v=1FDAowpMReo&t=142s)** what to do next about it. [music] Or we say that all of our userfacing text should be in US English, not UK [music] English, which we have a hard time with because we're in London and we'd like to stick the use in in different words. So this is another big difference with [music] uh having multiple rounds of code review for example because these are narrow rules you can afford to run them on every single commit in a CI [music] and that's what we do. So we run tens of thousands of judgments and the bill is normally around what one or two code reviews u will cost. >> Oh wow that's really cheap. >> It's really cheap. Yeah. >> So how do I get started with verifiers? So, the simplest way to get started is if you've installed our CLI [music] is to talk to the Tessle agent in the CLI.

**[3:10](https://www.youtube.com/watch?v=1FDAowpMReo&t=190s)** You can either go into that and just ask it open-ended. How would I set up verifiers? [music] Or it's got a couple of nice loops that you might want to run off the bat. You can trigger. So, one of them is review my PRs and tell me what I could do about them. So, if you run that, [music] you might find it suggests skill improvements or llinters, but it might also suggest [music] verifiers. Thank you so much for showing me all things verifiers. Um, really cool. Sounds really powerful. If you guys want to get started with Tesla verifiers, you can go to tesla.io/agent and you can ask the Tesla agent all about them. Or you can visit our docs and get started that way. Thanks for watching. See you next time.
