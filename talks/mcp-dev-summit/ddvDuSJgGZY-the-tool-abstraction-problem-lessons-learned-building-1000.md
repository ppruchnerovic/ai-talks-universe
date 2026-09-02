---
id: ddvDuSJgGZY
title: "The Tool Abstraction Problem: Lessons Learned Building 1000+ MCP Tools - Sam Partee, Arcade.dev"
slug: the-tool-abstraction-problem-lessons-learned-building-1000
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: ["Sam Partee"]
channel: "Agentic AI Foundation"
duration_min: 16
published_at: 2026-04-13T23:17:11Z
video_id: ddvDuSJgGZY
url: https://www.youtube.com/watch?v=ddvDuSJgGZY
youtube_url: https://www.youtube.com/watch?v=ddvDuSJgGZY
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# The Tool Abstraction Problem: Lessons Learned Building 1000+ MCP Tools - Sam Partee, Arcade.dev

**Sam Partee**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=ddvDuSJgGZY) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

The Tool Abstraction Problem: Lessons Learned Building 1000+ MCP Tools - Sam Partee, Arcade.dev

Before MCP, Arcade was building tools for LLM agents. We've shipped over 1,000 tools—first as native Arcade tools with our own protocol and eventually adopting MCP. The main lesson: the hard part isn't writing the code, it's finding the right abstraction.

Most MCP tools today are thin wrappers around APIs. `GET /users/{id}` becomes `get_user(id)`. But this creates a mismatch—LLMs reason about tasks ("find the customer who complained last week"), not endpoints. The question is: where should tools sit on the abstraction spectrum?

**Too low-level:** The agent needs to chain together many calls. Each step is a chance to fail, and the model has to maintain context across all of them. You're asking the LLM to be a programmer at runtime.

**Too high-level:** You end up enumerating every possible task as its own tool. This defeats the point of having a general-purpose agent and your tool schema balloons, eating context and degrading selection accuracy.

In this talk:

- The common pitfalls we see in MCP tool design
- Our design philosophy for optimized tools
- Multiple real-world use cases and the tools that work for them
- Outlook on future tool development

## Transcript

*2,470 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=0s)** So, today I'm talking about the tool abstraction. Uh so, I've probably made somewhere north of 10,000 tools. That might not seem possible, but I was actually building tools prior to MCP existing. Um we had our own protocol. It was called open execution protocol. And we for a long time cared just about tools. We didn't have prompts or resources. All we cared about was, "How can I take the JSON output of a model that at the time it was GPT-3, so JSON output wasn't even guaranteed. And how can we take that output and efficiently make sure that it is one, this seems funny now, but parsed correctly. Two, that it is correct. That the outputs and the arguments and

**[0:48](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=48s)** everything is correct. And how can I ensure that result of the tool function, but also of the output of the large language model. And this became something that we deemed a machine experience, like a user experience, but a machine experience, and that I often call the tool abstraction problem. This applies to resources and prompts, too, but in a different way. Um I'm I'm going to get it primarily what does it take to make a good tool? Um and I'm going to do it in 15 minutes. So, what do most people mess up today? If you ever see something saying, like an API generator, "Oh, I'm going to take your endpoints and I'm going to make them all tools for you." Don't do it. It's not going to work. And the reason being is because the tool

**[1:38](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=98s)** abstraction and an API abstraction are meant for different things. What do you make an API for? You make it for other programmers. You make it for an interface by which an API. You make it for another program to interface with it, not a large language model. If a large language model is to read it and understand it and produce the type of output necessary to call it, the abstraction is much different. Sometimes it's higher, sometimes it's lower, but overall it is much differently catered to in terms of the audience in which you're talking to. So like you can say "Find the customer who complained last week and schedule a follow-up." This is something an agent hears, and it needs to break it down into tasks.

**[2:26](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=146s)** But to do that, you have five endpoints. And and even then, you most of the time will not have the model realize it needs to call get user ID first. And so, what you really need to do is make an abstraction that covers these five. Find calendar and submit complaint on Zendesk. That can be a tool. One tool. That might sound too catered, but in fact, the accuracy rate of that tool in both when it should be chosen in terms of selection and its result in terms of the recall of the selection and the accuracy of the result is significantly higher both in practice and in theory.

**[3:16](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=196s)** And how do I know this? Every paper, pretty much since Apple's tool sandbox paper, every the nerves papers that you see, all of the um individual like the what is Speakeasy I think is one of them, it's like the major project, it's basically saying if you need to call six tools, you're just basically out of luck. You have over a 50% chance of failure. And and even worse is when you get to the point where you have to call a chain of them. If you've looked at Nestful or tool composition or the Berkeley uh function calling leaderboard, any of them will tell you, chaining is the hardest thing. And so, why are we trying to chain API

**[4:04](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=244s)** calls? Like, it doesn't make any sense. There it's a different abstraction, right? And so, if instead of saying, "Hey, go get the user ID, find the user's calendar, go get and get each of the individual IDs of the events." There was just one that that composition was made up of. And yes, that's a particular example of a higher abstraction of action. But it doesn't even have to be higher. It can be more specific. The whole point here is that it's catered to a different audience. It is not a programmer, it is in fact a large language model or an agent. And chaining is in fact the hard problem. Now, we have a lot of the different uh types of abstractions in the space that I can

**[4:52](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=292s)** talk about. Um you may say it's a thin wrapper API based. I can just put a better description on it, that's all I need. Most of the time, that's going to end up in the chaining territory. Where it's going to be saying something like, I need to call six of these things to get a normal job done, like an API would, right? Um and the the the middle ground that we mostly find is make it oriented around a task specific to the agent you're building it for. And then evaluate it both on the ability of a large language model or even better, uh use Arcade to evaluate it on multiple, right? So, a suite of language models. And then also have PyTests and you know, uh a you

**[5:41](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=341s)** know, set of Jest tests for confirming those tests actually run, like unit tests. Cuz remember, you have to also not in addition to the tool being something that is callable by language model, it has to also run. Which is something that most people actually end up not testing in a lot of tools. You see a lot of tooling frameworks these days without unit tests. And it's like, okay, well, the deterministic part has to be at 100% if we're going to introduce any amount of non-determinism right? That that part has to be at 100%. So, we find that most of these succeed the best when you organize them around tasks or intents. And the reason for that is tasks and intents model the way agents make to-do lists in that Gherkin style

**[6:30](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=390s)** that mostly Anthropic is responsible for introducing into the ecosystem. Um the to-do list abstraction, just think about it. In a to-do list, how do you write stuff? By tasks you got to do, right? And so, if you model them by tasks and intents, it's much easier for an agent to select the tools. So, like, you know, get track this order right? And return report or something even that specific would be much better than getting a user. It's too abstract, right? Where you might be getting the user inside that in particular function. Uh there's some major proof of this in the ecosystem. My old team at Redis put out a great paper on this. Um

**[7:19](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=439s)** uh Block and Square um and GitHub Copilot also put out a great one. Uh there's evidence all over the ecosystem. And this talk will be online, so you can go and look at all of these things, okay? Um you can go and fact-check me until the day's end uh on all of these papers. I have been doing this for a long enough time to where I can back up each one of these statements with a paper and a citation. Um and most most likely a GitHub repo. Um, it has been a long time my team has been trying to figure this exact problem out. Um, the cool things that I'll point out in this particular set of benchmarks are um, the self-discovering flows in the block paper that is becoming a little bit more popular right now. Um, the Redis paper focused a lot on reducing the number of tokens that you use. That was really

**[8:07](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=487s)** interesting. Um, so I would check those out. Another thing we released recently, we kind of took everything that we thought of in terms of like how you can build tools. He's actually sitting in the audience, his name is Guru. He's uh, incredible engineer and he put up all these patterns that we have in our what we call optimized tools. And we we do this because it's much easier to think about it in like the in task and intent modeled towards a specific domain type way. Um, if you can look at these patterns and say, "Oh, that models this kind of task that I want to go after." There's kind of step-by-step instructions to help you get to where you need to go. So, check out the Arcade tool patterns if you're interested. Um, there's some really cool ones on there.

**[8:54](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=534s)** Um, the biggest thing I'm here to say is description quality. If you look at our over 20,000 evals, if you look at any of the things that we do, um, confirming that our tools are actually going to work, the description quality, the quality of the description and iterating on the description is what actually has a 10x lever, um, in terms of the returns that it yields. Because the description is heavily heavily uh, is is the thing that most heavily influences whether the large language model is going to select that. The name is being, you know, the second most influential and then how it is used. So, you might think that context is really, you know,

**[9:42](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=582s)** number one, it's not. The description, more than anything, because of the position that it is most commonly placed by an agent framework, in the positioning of the context window that is sent to the large language model, being in the schemas, which is usually towards the bottom. If you look at any needle in a haystack paper, the description is what is most likely going to be the thing it last thought about. Last thought about. It last, uh, you know, after it's selected the tool. It's most recent, uh, you could say piece of memory in the context window. And so, that's really important. Um, we found even in our nightly evals, we had 10x fewer, um, errors when we specifically went through and did optimization

**[10:30](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=630s)** strategies towards only the descriptions. It was around 9.something. Um, don't do more than about 600 words. Ideally, keep it to a action verb to start, and then a short task intent enabled or reformed sentence. Um, you can look at a lot of our examples online. Um, and all of them will show you, uh, kind of how we specifically model our functions like that. Um, and the uh I'm going to say this wrong. I believe it's Hash. Um, Hash and all, um, is a really interesting paper about how they went from, you know, being able to do, uh, a a a very small amount of activities with bad descriptions to a an entire chain of activities, and they describe it a

**[11:18](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=678s)** little funny. Um, like zero-shot equals 16. It's, uh, they were able to make the model perform a much longer chain, like we talked about earlier, the tool chaining problem, uh, chain of activities just by changing the description. Um and so the 10x lever of all of this and how to make the tool abstraction better is the the description. Tool selection, dynamic tool selection has been released across a number of different places. Really what you'll see here is a concept called progressive discovery. And progressive discovery is something where you're introducing context over time. Um and there's all types of experiments that are out here, but really the the best thing that this does is not necessarily helping with the abstraction, but helping with the amount

**[12:06](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=726s)** of context that you're utilizing. But if you look at any of these individual papers that you see down here like MP MCP0, um all of them will point out themes that I've pointed out in this talk, which is that the description really matters. The task intent really matters. The selection time really matters at runtime. The context window positioning of the scheme is really matter. Um and so it's important to add here. And uh I know I want to leave some time for questions, so I will just say skip skip last takeaways. Uh tool count cliff is real. If you have more than 20 or so tools ever since Apple sandbox, your agent's not going to know what to do. You can fix that somewhat with selection at runtime, but even progressive discovery is not going to fix the whole

**[12:53](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=773s)** problem. Chaining inside tools is more likely to be that agent abstraction and chaining is the hard problem. Moving composition logic inside of your tools and then making them task intent enabled functions that you choose from is a much much better recipe for success. And then lastly, descriptions are the 10x lever. Don't just write them and forget about them. Think about them all the time. Descriptions are what matter the most. And you might not think they are, but they are. Um and that's fact. So I'll leave a little bit of time for questions. I only have 2 minutes 30 seconds, but thank you very much. Yes.

**[14:03](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=843s)** So, the question was about task intent-based tools, and then what if the input is based on a uh like a previous event type? Is that kind of Wonderful yeah. Enumerate.

**[14:51](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=891s)** I would say enumerate. So, the the point here is um I'll give it I'll kind of give it back to you. Um you want the flexibility. You don't want it to be to give the example of the one I had. Like, you don't want to be getting the user every time they're getting the email and the calendar every single time. You want the flexibility to say, "Oh, I might also want to go to this in the the abstraction enumerate them and name them differently." Um now, you might say, "Okay, what about then the number of tools and the problem that that brings about?" Well, that typically you break into sub tasks or sub agents. However, the the promising point that we're about to reach in the future with progressive discovery will hopefully be a better answer to that as we move on. I would argue if you're making your agents broad

**[15:40](https://www.youtube.com/watch?v=ddvDuSJgGZY&t=940s)** enough such that they're responsible for that broad of an activity. If you have to enumerate more than 40, you should probably rethink your agent. Um it's too broad. Never have that broad of an like an agent scope shouldn't be that broad. You're giving it too much responsibility. Anything else? Good question. Yeah, yeah, why not? Oh, actually I think we just reached zero seconds. I'll reach you after. All right. Thanks everybody.
