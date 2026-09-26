---
id: UVOkQyeY16M
title: "Christopher Batey on the 3 Boxes You Don't Control"
slug: christopher-batey-on-the-3-boxes-you-don-t-control
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-23T15:00:12Z
video_id: UVOkQyeY16M
url: https://www.youtube.com/watch?v=UVOkQyeY16M
youtube_url: https://www.youtube.com/watch?v=UVOkQyeY16M
tags: []
topics: ["Agents & orchestration", "Prompting & context engineering"]
transcript: true
---

# Christopher Batey on the 3 Boxes You Don't Control

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=UVOkQyeY16M) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Context engineering usually means retrieval and prompts, but at AI DevCon London the sharpest version of it was about codebases that are ten and fifteen years old: what an agent needs to see before it can touch a system nobody fully understands anymore. Katie Roberts (Nearform), Simon Martinelli, Christopher Batey (CECG) and Ian Thomas (Meta) covered brownfield code from four different angles, from reverse-engineered specs to a single VR machine nobody wanted to refactor.

What we cover:
– Why brownfield code behaves more like a functioning city than a ball of mud
– Reverse-engineering use cases and entity models out of code nobody documented
– The three boxes — harness, model host, and model — most teams don't realize they depend on
– How one engineer turned a legacy VR codebase into a fleet of parallel agents

Chapters:
00:00:00 - Introduction
00:00:21 - Katie Roberts, Nearform: stop calling it a ball of mud
00:01:03 - Why brownfield code looks more like a functioning city
00:02:16 - Simon Martinelli: reverse-engineering specs out of legacy code
00:03:34 - Why lift-and-shift was never modernization
00:04:23 - Christopher Batey: the three boxes you don't control
00:05:54 - Choosing a harness you can swap without switching everything
00:06:42 - Ian Thomas, Meta: teaching one refactor, reviewing fifty
00:08:07 - The MCP server that got agents off a single VR machine

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What's the oldest part of your codebase an agent has actually touched?

## Transcript

*1,783 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=UVOkQyeY16M&t=0s)** Back in June at AI DevCon in London, somebody finally said the thing out loud. Almost every demo you see starts with an empty repository, even though nobody actually works in one. Let's first hear from Katie Roberts, technical director at Nearform, who would like us to stop calling legacy code a big ball of mud and start thinking of it as a city. I'm Katie Roberts. You might recognize me from such tracks as the latent space, where I've been emceeing for the last day and a half, and I'm here to talk to you about how you can stop maintaining and start evolving. Applying AI native engineering in brownfield code bases. Developers send more time deciphering the code and fixing bugs and resolving issues than implementing new features and improvements. Small updates become really difficult, change becomes hard. Future development starts to crawl.

**[0:49](https://www.youtube.com/watch?v=UVOkQyeY16M&t=49s)** Anyone who stuck in this space as well becomes very demotivated. And it's nobody's fault because every decision on this code base was made with the best possible intentions. Nobody wants the code to get like this, and it's sometimes referred to as the ball of mud pattern. I don't think of brownfield code as a ball of mud. I think of them much more like a city. A city is very successful, and it's something that's evolved over time. And brownfield systems tend to work like this. They work incredibly well. They have huge numbers of customers working on them, and that is why they've been around for five, ten, 15 years while maintaining complex user demands, while at the same time working through problems like performance, security and scaling that come with that. And like the city, they've evolved as a response to the needs

**[1:39](https://www.youtube.com/watch?v=UVOkQyeY16M&t=99s)** and there are areas in that functioning city. So this is actually London. I took this last weekend from one of the top of the skyscrapers. I'm very pleased with this picture. It's lovely, but you can see on this you've got paths through the city which are very, very clear. These are these are the well-trodden paths, the ones that we all know where it's going. And then there are less well maintained spaces, dead ends and the places that you really wouldn't want to get caught in alone late at night. So this is like your code base, and you want to evolve it into something that is easier to build on, that's more understood, and you get that high level view so you can start working through. We also heard from Simon Martinelli, who does modernization for a living and is blunt about what it isn't. Translating COBOL into Java is not modernization. That is lift and shift.

**[2:29](https://www.youtube.com/watch?v=UVOkQyeY16M&t=149s)** What he does instead is reverse engineer the specification back out of the code, get the business to check it, and generate from there. that. What I do mostly is software modernization. So I'm doing modernization for enterprise applications for about eight years now. And there I just changed the process. That means I extract use case and entity model from code and tests and documentation. Maybe I have confidence here or whatever, because usually the documentation is spread around multiple artifacts that we have, and then we have the entity model and the use cases. They will be revised or reviewed by the business people. And then we generate the new code, because there are a lot of IDs that we can directly transform, maybe from COBOL to travel.

**[3:19](https://www.youtube.com/watch?v=UVOkQyeY16M&t=199s)** So that's also something that anthropic is, is telling us. But that never worked. So we did that like 30 years ago COBOL to see or call to C++ or something. But that's not helpful because that's just lift and shift. And modernization is not lift and shift. Modernization is rethinking how people are working with the software, integrating features that maybe are not there. And because of this reverse engineering, we also have a positive feedback from the end users because we are not transforming from one technology to another, because regarding our use case and entity model. And we can integrate new features because usually you don't do that. So the guideline when we started with the modernization project two years ago was we want to have the exact same system

**[4:11](https://www.youtube.com/watch?v=UVOkQyeY16M&t=251s)** just in another technology, and you don't add new features because we don't want to introduce new bugs. And now we can just do that because we just change the specification. Christopher Batey has a warning about something you've just inherited without noticing your harness, your model hosting, and your model are three boxes you don't control. And if your provider goes down at the same moment as your production outage, and that model is the only way your engineers know how to debug. Good luck. The next thing I wanted to dig a bit deeper into is have a real think about the dependency you want to put on the producer of your digital product. So if we go back to this diagram and we've accepted that, maybe we don't understand how agent workflows actually produce code. If we were to break it down a bit more.

**[4:58](https://www.youtube.com/watch?v=UVOkQyeY16M&t=298s)** So I'm breaking down the producer box into three things. We've heard the first one, I've called it interface, but in most places we'll call it harness, like in the keynote. So there's an interface for how you do that, right? That could be Claude Code. It could be OpenCode. It could be Codex. It could be some automatic workflow based off your, your your GitHub issues. Then you've got the thing which is hosting your model. Right. So that could be directly it could be the anthropic API, but you could be hosting your own. You could be using a third party which reached between them. And then you've got your model. So really your black box is made up of three things that you don't understand. It's called Claude Code. It's an API which perhaps at 330 on an afternoon stops working. Anyone experienced that? Does anyone feel the most productive? Once the Americans wake up and and make the anthropic APIs. Go down? And then you've got the model, which obviously you don't understand. I'm not saying you only see on this day, if anyone wants to explain

**[5:48](https://www.youtube.com/watch?v=UVOkQyeY16M&t=348s)** how opus works to me, I'm very happy to hear it. So we can choose not to be quite so coupled to that workflow. We can use a harness which is open source. What's the benefit of that? You know, when on profit goes down, I just switch to open API with a single command and I carry on. I obviously get different results. Every model gives you different results, but it's a good to have the way that you're building your digital product be able to flip between providers. You could go as far as to hosting the models themselves. That limits the models. You could do use something like so, and then if you want, you could use a model with open weights or at least an open source way, the way you that's trained. I don't think any of that is that important, apart from being able to switch between providers very quickly. If you've got a production outage and suddenly at the same time, let's say your favorite AI provider does, and the only way your engineers can debug production is with that model.

**[6:36](https://www.youtube.com/watch?v=UVOkQyeY16M&t=396s)** Good luck. anticlockwise. Ian Thomas at Meta on about the least inviting brownfield. There is low level VR code on one very powerful windows machine full of patterns. Nobody wanted to go near. One engineer taught the agent how he would do the refactor, found the same shape all over the code base and became the reviewer instead. Refactoring in VR means that you're going to be spending a lot of time in your windows PC looking at some pretty gnarly low level code at times. And there's a lot of legacy patterns that we'd built up over the years that needed to be refactored out. And people tended to shy away from these things because there's a higher risk of breaking things. You know, these are the refactorings and not something that you would undertake for fun. But one of the engineers thought, okay, well, if I can teach the AI

**[7:26](https://www.youtube.com/watch?v=UVOkQyeY16M&t=446s)** the way I would think about resolving these refactorings and then go and find patterns that are similar across the code base, what can we achieve? And again, roughly half the time spent in achieving his goal. But he went out and found multiple areas where this pattern could be reapplied and set the agents off in a kind of team pattern, so they would go and work in parallel. And then he was actually more as a reviewer and just being a critical architectural oversight, making sure that it was doing the right thing and not making any kind of gross miscalculations on how we actually wanted the system to look afterwards. And moving on from that, like I said, we had a challenge with VR in that you're kind of constrained to one machine. But one of the engineers who was thinking about this from the what is the what is the machine actually need to render and what what can we do that doesn't require us to have this massive PC with a huge GPU in it?

**[8:19](https://www.youtube.com/watch?v=UVOkQyeY16M&t=499s)** If we provide better context to the models when they're doing work, would they be able to work in our more standardized on demand worlds? And the result of this was an MCP server that was a bridge between the data that backs Horizon World. So all of the things that explain how world state looks, how how things are built, the models, the kind of textures and everything that are in the worlds, it taught the models exactly what it needed to know about how horizon works, so they could go and work largely in isolation and in multiple on demand environments. And so that removes the whole windows PC barrier. And it meant that we could parallelize the work in a lot more effective way. And again, the AI was cleverer. It knew more about the the world that we were working in than it did before. So we got better outputs as well.

**[9:10](https://www.youtube.com/watch?v=UVOkQyeY16M&t=550s)** So not only was it more efficient and we could parallelize more, we actually found that the quality of the work went up to. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
