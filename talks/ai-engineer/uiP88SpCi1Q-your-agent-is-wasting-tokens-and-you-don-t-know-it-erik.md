---
id: uiP88SpCi1Q
title: "Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS"
slug: your-agent-is-wasting-tokens-and-you-don-t-know-it-erik
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Erik Hanchett"]
channel: "AI Engineer"
duration_min: 6
published_at: 2026-06-28T22:00:14Z
video_id: uiP88SpCi1Q
url: https://www.youtube.com/watch?v=uiP88SpCi1Q
youtube_url: https://www.youtube.com/watch?v=uiP88SpCi1Q
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS

**Erik Hanchett**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=uiP88SpCi1Q) · [Conference site](https://www.ai.engineer/)

## Description

I deployed an agent to production and the bill was not good. Not because the model was bad, but because it was doing too much. I was using the most expensive models for simple inference calls. The context was filling up. And my tool loops ran longer than they needed to. The agent worked fine, it just cost way more than it should have.

This talk covers three small changes I made that dropped my costs without hurting quality. Each one was a few lines of code, and none of them required changing my prompts or switching models. I'll cover things like prompt caching and model routing. I'll show code.

Speakers:
- Erik Hanchett (Amazon Web Services): Erik Hanchett is a Developer Advocate at AWS who helps developers build with frontend, fullstack, and AI/agent technologies through hands-on tutorials, talks, and videos.
X/Twitter: https://x.com/erikch

## Transcript

*1,000 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=0s)** Hey everyone, my name is Eric Hanchett. I am a senior developer advocate at AWS and I'm going to talk to you about how you can save on token costs. Now, I'm going to show you five ways that you can reduce your token costs while using and creating agents. So, the first way you can do that is to cache your system prompt. Let me show you some code. Now, I'm using AWS's Strands agents. This works with all different providers. This is a little bit of pseudo code, but the idea is that you can add cache prompt equals default. And what that'll do is on the first call of your agent, it will send the full system prompt over and then on every

**[0:48](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=48s)** subsequent call, it will have a much reduced system prompt being sent over. So, it'll be cached. You can also cache the tool prompts and messages as well. This may sound obvious, but you want to look into routing your different messages based on the difficulty. So, here's a code example. Let's imagine that you have a task that's very difficult. You may want to use one of the newer frontier models. However, if it's something simpler, you want to use a cheaper model. In this case, maybe we use Claude Haiku for a cheap something cheap and then use Claude Sonnet for something a little bit more difficult. And then you can use an if statement. You can even have another model that's very cheap decide which

**[1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s)** model to use. So, you can play around with this, but I highly recommend don't use the most expensive model for everything you're doing. You want to use multiple different models based on the use case. And then try to route to it inside your agent. Another good tip is to offload the tool result. Let me show you some code on here. Once again, I'm using strands agents. This is a a manual way to do it. There is some additional APIs that the strands agents offers to do this. If you have a large tool result that's coming back, you can store it locally or in the cloud and then use some kind of summarization that saves on tokens. So that way when it's being called over and over again, the tool result isn't added

**[2:24](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=144s)** into the context every time every time the tool loops or every time the agent loops. So if you can find any way that where you have this tool result that you don't necessarily send it on every single call back to the large language model, that will save a lot of tokens for you. And like I said, there's a few APIs to do this, but it essentially you can do the summarization technique. You can also cap your tool loops. So when you're dealing with the agent loop and it decides to do a tool call, I've had this happen often where it calls the tool over and over and over again. And if you don't cap that tool call, then it might run 10, 20 times. It might get into an infinite loop, which would be very bad for your token usage. So always set a max iterations of how

**[3:13](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=193s)** many times it will loop. A good thing you can do before you deploy your agent is to run some observability tools and take a look at the tool call use for every single tool and then see how long each one of them is running and how many times they're looping. And that way you can get an idea of how efficient the tool call is. Last but not least, we can trim the history. So if we're using a multi-turn agent and we are talking back and forth, you will find at times that the conversation history will get very large on every single call, that whole conversation history will be sent back to the large language model. And this can eat through hundreds, if not thousands, of tokens.

**[4:03](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=243s)** In Strand's agents, we have something called sliding window conversation manager, which which this does is it looks back at the last 10 messages and only sends those back. And you can set this to whatever you want. And that way you're not sending these huge message histories back to the agent every single time a new message comes in. The downfall of this, or the trade-off of this, I should say, is that you will lose the message history from the beginning. The way you want to deal with that is you can use uh some sort of summarization of the history and then put that into the context window. So, rather than sending all of it, you may send a small amount once you hit this sliding window. Uh this will save you a lot of tokens. So, in conclusion, we have five things.

**[4:53](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=293s)** Cache the system prompt. And if you can, maybe the tool prompt and messages. Route by difficulty. Don't use the same expensive model for everything you're doing, for every single task. Offload these big tool results. So, if you have a large tool result, you can summarize it and not have it being sent in the agent loop and overloading your context. You can cap those tool loops. Make sure you use observability tools to see how long tool calls are taking and how many loops they're they're doing and and then try to iterate over that. And then, of course, trim the history if you're using a multi-turn conversation with your agent, so that way the whole conversation isn't being sent over and over again for very long conversations. Thank you for listening to my very quick, almost lightning talk today. If

**[5:42](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=342s)** you like to go deeper, find me on LinkedIn at Eric Hanchett. I also blog at programwitheric.com. And then you can find me on social media at EricCH. Love to talk to you guys more. Thanks.
