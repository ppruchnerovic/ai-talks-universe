---
id: ptwholFiAZg
title: "Agents Open 1,000 PRs. Who's Reviewing Them?"
slug: agents-open-1-000-prs-who-s-reviewing-them
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 6
published_at: 2026-08-28T11:00:34Z
video_id: ptwholFiAZg
youtube_url: https://www.youtube.com/watch?v=ptwholFiAZg
tags: []
transcript: true
---

# Agents Open 1,000 PRs. Who's Reviewing Them?

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=ptwholFiAZg) · [Conference site](https://tessl.io/devcon/)

## Description

Coding agents can write thousands of lines and open thousands of PRs. Automating code review is the only way that keeps up — and trusting the review is the hard part. Macey Baker and Colin Hallett walk through Tessl Code Review, and why review is where your accountability actually sits.

What we cover:
– Why reviewing and trusting agent-written code became the bottleneck
– How automated code review reads the intent of a PR, not just the diff
– Review lenses: versionable review skills you can scope with globs
– Why owning your review standard in-repo beats configuring someone's web UI
– Where automated code review fits inside a software factory

Chapters:
00:00:00 - Introduction
00:00:11 - Why reviewing agent-written code is the bottleneck
00:00:55 - What makes Tessl Code Review different
00:01:30 - The trust problem with AI code review tools
00:02:03 - Review lenses: scoped, customizable review skills
00:02:42 - What changes once code review is automated
00:03:14 - You own the standard: review config in your repo
00:04:01 - Code review inside a software factory
00:04:34 - How to get started

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which part of your review process would you automate first? Tell us in the comments.

## Transcript

*854 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ptwholFiAZg&t=0s)** Hi, I'm Macey, and I'm here with Colin, and we're going to talk a little bit about a new feature that we're shipping called Code Review. So what problem are we trying to solve with code review? So coding agents are great at writing code, can write thousands of lines, open thousands of PRs. Writing code is no longer the bottleneck. However, reviewing it and trusting what it can do is completely the bottleneck. Essentially, review is where your accountability sits. It's kind of the final gate between the code you write, or your agents write, and what gets shipped to the customer who you really want to trust. That accountability is kind of a key feature built into our code review tool.

**[0:49](https://www.youtube.com/watch?v=ptwholFiAZg&t=49s)** So there are a number of kind of third-party tools that do this. We've used a few. I'm curious how Tessl's version of code review is different. So one of the big differentiators with Tessl code review is that it's very aware of the intent of your PR. It reads the summary, the title. It understands what you are trying to get to with this change. Some companies might have a real fix-forward philosophy where they don't want too rigorous reviews and they just want to ship, whereas other ones might have a very strict set of requirements. You don't need to tell Tessl code review this. It'll know, right? And it will review accordingly. One issue that we found with existing code review tools is an issue of trust. You know, they'll find a whole host of issues, but it's really hard to

**[1:40](https://www.youtube.com/watch?v=ptwholFiAZg&t=100s)** know if they're true, if they're accurate, and if they match your standards. If you have code review implemented, but you feel you have to review that as well, it hasn't really taken anything off your plate. So how does Tessl's code review help focus review compared to, say, other tools that do something similar? So we have a concept of review lenses, and these are essentially skills a conversion you can evaluate, you can distribute and you can customize them to exactly your repository standards. You can then scope them using globs to certain sections of your code base. So you can have a lens specifically for random design, or a lens specifically for security. Tessl code review ships with a really great set of defaults,

**[2:30](https://www.youtube.com/watch?v=ptwholFiAZg&t=150s)** so you don't actually need to configure it to already get value from it. But I think where the real power comes is from being able to fine-grain and fine-tune your reviews. So what might someone expect to change if they set up Tessl code review? So I think one of the first benefits that people will see when they set up Tessl code review is they spend a lot less time babysitting a PR to completion. So as you start customizing and configuring Tessl code review, you'll find that the knowledge and learnings will compound. So your reviews will get better, you'll trust them more. And your agents will be able to work more autonomously in a way that works for you. So one of its kind of key benefits is that you own the standard of review.

**[3:20](https://www.youtube.com/watch?v=ptwholFiAZg&t=200s)** It's a file in your repo. It could be a skill, your configuration file. You own it. You can version it. You can share it how you want. It's not some setting in some web UI of some other code review product. It's not some black box where you don't know what's going on and how it runs. You really own the standard. One thing about being able to version your review lenses is that you can now apply a consistent set of reviews across every repo. But not only that, you can obviously account for specific repo differences with other lenses, but it means you can have the baseline level of review across your organization, across your code bases. Obviously, you know, we're pretty deep into factory land here at Tessl. What's your opinion on kind of where this sits in sort of our big factory plans?

**[4:12](https://www.youtube.com/watch?v=ptwholFiAZg&t=252s)** So Tessl code review is a first-class component of a software factory. Software factories run relatively autonomously. Ship a lot of code. You need to be sure that that code is trustworthy, and it's a thing that you want it to do. This is why Tessl code review integrates directly into your software factory. So how can we get started with Tessl code review? The easiest way to get started is getting the Tessl agent, aim it at your repo and say, hey, set up code review for me, and it'll set up the workflows, it'll set up all the actions. It'll set up your configuration files and also help you customize your own review lenses. You can also just point your agent of choice at our docs on our website. At tessl.io

**[5:01](https://www.youtube.com/watch?v=ptwholFiAZg&t=301s)** and ask it to set up code review. Thank you so much for watching. Thank you for your time. If you want to get started with code review, you can do so at tessl.io. And we'll see you next time.
