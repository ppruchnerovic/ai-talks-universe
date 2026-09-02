---
id: N1XoiJGyNpM
title: "Denis Akhiyarov - Are Small LLMs Ready for Coding Agents?"
slug: denis-akhiyarov-are-small-llms-ready-for-coding-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Denis Akhiyarov"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T01:53:59Z
video_id: N1XoiJGyNpM
url: https://www.youtube.com/watch?v=N1XoiJGyNpM
youtube_url: https://www.youtube.com/watch?v=N1XoiJGyNpM
tags: []
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Denis Akhiyarov - Are Small LLMs Ready for Coding Agents?

**Denis Akhiyarov**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=N1XoiJGyNpM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*652 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=2s)** DENIS AKHIYAROV: Hi, everyone. So actually, this is a bit of a personal story. So a few months ago, I was flying transatlantic and realized that as AI scientist, I can be very inefficient without a coding agent while disconnected from internet. So, I realized that maybe I should develop my own local coding agent and see if a local LLM running on my MacBook can actually handle realistic coding agentic tasks. Oh, yeah, there is a link to this repo. So, I just open sourced it recently.

**[0:52](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=52s)** And you can also see the presentation there. So, this agent is called AskMe. And it does one small thing at a time. So it's basically designed around three ideas, key ideas-- how to minimize the context that we pass to a small LLM. Because LLMs are not really good when you pass them a lot of context for small language models running locally. And the second is that we do very small actions at a time and immediately verify that action. And the third thing is we minimize the reasoning as much as possible.

**[1:42](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=102s)** Only use it on recovery loops when things go wrong. So here is an example. You give a small LLM. So in this example, it's 3.6. And basically, you want to just create a small program. Think of a Hello World, compile it and run it. But the thing fails because, actually, it compiled it into a temporary directory. But it needs to execute from another directory. So things like this are much harder for small LLMs to realize. So we have to make very, very small changes and verify them one at a time. So around this idea, we basically develop a loop.

**[2:34](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=154s)** So AskMe is a very minimal loop. It's just one file. It used to be 1,000 lines of code. Now, it's close to 2k lines of code. And so yeah, basically, you want to minimize a number of big planning steps. You take smaller steps, and only go back when things go wrong. So I evaluated this on few hundred tests. And here, this is just smoke test with two families of LLMs, Gemma 4 and Qwen. And basically, it works, except one Qwen model. This was just a sanity check that we can use it.

**[3:25](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=205s)** And then, next is actually running realistic task. So this is actually building features for an app. And what I realized is that basically, these agents can do most of the work. But the issue is that they fail to verify their work and have this full loop, observe what happens, go back and solve it. So basically, it passes most of the tests, but not all tests for developing an app. And it's the same story across both Qwen 3.6 and Gemma 4. And for the record, this was run on open router, not locally.

**[4:17](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=257s)** Because locally, it will take me ages to run this. And there is a limited memory on my MacBook. Next, so I think, basically, this wasn't an example, just creating a small agent, running locally with minimal hardness, and it shows that it can basically work locally with a very small LLM. Doesn't need a large code base like Codex or a Cloud Code. And yeah, you can look at results and how it works in this repo. I guess I also want to give some shout outs. So I actually compared it against pi harness,

**[5:09](https://www.youtube.com/watch?v=N1XoiJGyNpM&t=309s)** which is the most minimal harness that people use at the moment. It's much more efficient than Codex or Claude code. And also, I did some comparison with OpenHands. And basically, this is a even smaller than both those harnesses for working with very, very small LLMs locally. And it's still a work in progress. There is still a lot of issues. But yeah, I'm happy to receive any feedback, any questions you have. Thank you. [APPLAUSE]
