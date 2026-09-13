---
id: fwL31sNbq8g
title: "Google, McKinsey & Dave Farley on AI Code Review"
slug: google-mckinsey-dave-farley-on-ai-code-review
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 11
published_at: 2026-09-07T15:15:35Z
video_id: fwL31sNbq8g
url: https://www.youtube.com/watch?v=fwL31sNbq8g
youtube_url: https://www.youtube.com/watch?v=fwL31sNbq8g
tags: []
topics: ["AI in the SDLC & engineering orgs", "Coding assistants & agents", "Evals, observability & reliability"]
transcript: true
---

# Google, McKinsey & Dave Farley on AI Code Review

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=fwL31sNbq8g) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Coding agent reliability stops being a model problem the moment review becomes the bottleneck. Four speakers at AI DevCon London arrived at the same fracture from different directions: generating a change costs thirty seconds, reading it costs an hour, and every convention around code review was built for the old ratio.

Jack Wotherspoon (Google) on the drive-by pull request, and why a maintainer can no longer assume a human is on the other side of the code. Dave Kerr (McKinsey) argues review was never quality control at all — it's how you engage with somebody else's mental model, which is exactly what a pile of unread generated code pulls apart. Brian Douglas (Paper Compute) left an agent running for hours, came back to find it politely hallucinating progress, and now pipes every session into a Tapes database with observational memory on top. And Dave Farley (Continuous Delivery), who writes no code by hand at all, explains why he still thinks English is too vague to be the programming language of the future.

What we cover:
– Why a 30-second drive-by pull request costs a maintainer an hour
– What happens to coding agent reliability when nobody can say why a change was made
– How one person's generated code pulls three mental models apart
– Capturing agent sessions as observations instead of losing them
– Why precision beats natural language, from someone who hand-writes none of his code

Chapters:
00:00:00 - Introduction
00:00:26 - Jack Wotherspoon, Google: the drive-by pull request
00:02:46 - Why trust between contributors is breaking down
00:03:18 - Dave Kerr, McKinsey: attention and short-cycle work
00:04:53 - Maladaptive creativity and diverging mental models
00:05:39 - Why you still review pull requests and specs
00:06:12 - Brian Douglas, Paper Compute: politely hallucinating
00:07:14 - Tapes, observational memory and agent feedback
00:08:25 - Dave Farley, Continuous Delivery: natural language vs code
00:10:01 - Why vibe coding alone isn't enough

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Is coding agent reliability a review problem or a tooling problem? Tell us in the comments.

## Transcript

*1,979 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=fwL31sNbq8g&t=0s)** Back in June at AI DevCon in London, there was a thread running through the whole event that nobody had quite planned. What happens to review and to trust when generating a change costs 30 seconds and reading it costs an hour. Let's first hear from Jack Wotherspoon at Google, who works on Antigravity CLI, on the drive-by pull request and why he thinks the social contract of open source is coming apart. So here's an example. I work for Google as a developer advocate. I've been in open source for the past five years at Google, working on Google ADK, so Agent Development Kit, and most recently Gemini CLI. So what are the main issues? Breaking down the barriers with AI should be a win, right? Makes it easier for people to contribute to these projects. But what's the flip side?

**[0:49](https://www.youtube.com/watch?v=fwL31sNbq8g&t=49s)** And this is one that I've seen a lot, and it's the drive-by PR, right? So you have, you're using a library or a framework or whatever it may be, and something goes wrong. You say, oh, I've got the error message. Let me just go and fix this. You know, I know it's an open source project. Let me go and contribute to this. So you just throw in your stack trace, you clone the repository and ask your agent to fix it. So that takes like 30 seconds on your end. But the flip side, and we'll assume that this is actually good code generated. We'll assume that for this scenario. Then you've got the maintainer who actually has to go and review that. So they're going to take their time, at least at Google. We still kind of hand-review each PR that goes in. We have like code reviews that are automated. And we'll review the code, agent first, but then it still gets to a point where a maintainer looks at the code and ships it

**[1:39](https://www.youtube.com/watch?v=fwL31sNbq8g&t=99s)** with all the security vulnerabilities and everything. Right now, that has been at scale. We make sure that humans see everything. So then they go and they post some feedback, you know, hey, maybe you change these two things and the drive-by PR really is someone prompted it, but they had no expectation that they were actually going to have to follow up or do anything. Right. So it might have been a good first judgment, being like, hey, I can try to fix this, but they're not going to come back. So you just have a prompt and forget it. Where now it's either the maintainer needs to come and kind of take over that pull request, and it just kind of floats away into the abyss. The second one is agents, like we showed in that quick example of ten subagents. It's super easy to parallelize work. Unfortunately, we have not figured out how to do that as humans

**[2:28](https://www.youtube.com/watch?v=fwL31sNbq8g&t=148s)** for our own brains, so we might be able to create code super, super fast. But the burden on the maintainer if we spin up ten pull requests in a minute. It's not going to take 10 seconds to review all that code generated. So there's a disconnect there. And trust is somewhat breaking down. Like I mentioned, you don't necessarily know whether or not a human is on the other side of that code, whether it was even looked at. So when someone puts up a pull request, normally you would have gone back and forth: hey, why did you make this design decision? Nowadays, I don't know when I told me to or Claude told me to. So now the thing is, there's not actually trust there. You can't actually assume that whoever put up that code even knows what's going on.

**[3:18](https://www.youtube.com/watch?v=fwL31sNbq8g&t=198s)** We also heard from Dave Kerr of McKinsey, who came at this from an angle I didn't expect. When one person generates a pile of code they don't understand, three things drift apart: their model of the system, the system itself and their colleagues' model. Which is why he thinks review is not quality control. It's how you engage with somebody else's mental model. Death by a thousand cuts. I'm going to briefly talk about this because you probably know about it. Your attention just gets destroyed. Short-cycle work that you're doing. Being able to work on everything kills your attention. We're constantly multitasking. I think most of us are feeling things like this. So how do you deal with it? Focus. Creating space for the work that you're doing. Running tasks to completion.

**[4:08](https://www.youtube.com/watch?v=fwL31sNbq8g&t=248s)** Recognizing when you're engaging in displacement activities. Prioritizing. Creating protected time. Pressured speaking. We'll get past this one, except for the fact that your AI speaks to you like someone who's on cocaine. It's like nonstop, doesn't listen. No space for interruptions. That's pressured speaking. It's awful to listen to. What's even more awful is when a bunch of your colleagues take all the pressured speaking from their AI and throw it at you, and then you're like, God, it's coming from all directions. So what do we do about that? Compress signal to noise. Like, what's the high-level message? What should this mean? Not what's the 30 pages of stuff that is your stream of consciousness that I don't necessarily want to see? So this is the key one. I'm interested in maladaptive creativity.

**[4:57](https://www.youtube.com/watch?v=fwL31sNbq8g&t=297s)** So this is going to get a bit philosophical. Mental model. On the left is me building a system, my model of it. Mental model on the right. In the middle is the system itself, similar but different. Next mental model is the model my colleague has. They're slightly different, but they're sort of roughly in sync. Because we talk a lot, we make small changes. We have to look at what we've written. Now, when AI does a lot of this for you and it does it very fast, the mental models start to look like this. One person can create this palace of stuff. They don't really necessarily know what's in it. What they've created is very different to their mental model. The mental model from the person who is trying to understand it is even more different when people say to me, you don't need to review pull requests, you don't need to review specs.

**[5:46](https://www.youtube.com/watch?v=fwL31sNbq8g&t=346s)** That's, that's wrong. You do, because it's not about quality control. It's about engaging with the mental model so that they can see what someone has built and how it works. Because part of my job and your jobs is also to understand that system so that we can fix it and maintain it. This is the hardest thing to manage, but it's the thing that I think will help people the most. So you share, you collaborate, you build your models together. Brian Douglas, you may know as bdougie, is at Paper Compute, and was it GitHub before that? He left an agent running for hours and came back to find it had achieved almost nothing while cheerfully reporting progress. His phrase for it is politely hallucinating. So the agent was

**[6:32](https://www.youtube.com/watch?v=fwL31sNbq8g&t=392s)** it wasn't learning, it was just politely hallucinating progress. It would actually celebrate wins of like, hey, we finished a thousand turns. We did it absolutely right. You guys know that from Claude. It would basically just do this and this is back in February. So yeah, this would have been like 5 for Codex and like one of the Opuses. But what I'm getting at is like this was like a nice construct for me to take that context and go serve it back to the agent. So a lot of folks we talked to upstairs, like, they have a skill where they kind of sit and look at their sessions at the end of the week, and then they summarize, like stuff that's been done, good for you. That's great. But you're definitely like top-notch when it comes to like using agents. But I don't do that. So instead I just dump all the context into a Tapes database. So at the time we were using SQLite,

**[7:20](https://www.youtube.com/watch?v=fwL31sNbq8g&t=440s)** we've actually moved on to Postgres for limitation reasons. SQLite has single-player methodologies. Only one person can write to the database. This setup was actually ten Pokemon agents running simultaneously, 1,000 turns each, and learning. It's constantly piggybacking. So. So I have the Tapes database, which has all the raw data. So this is the log for agents. And then I have this memory folder that I this is a concept I got from a Mastra blog post on observational memory. And this is like taking your 1,000 sessions and then writing an observation. So think about the end of the day. You open up your journal like, man, I saw this amazing talk from Brian Douglas from San Francisco, California. It was amazing. He had a great shirt on, his glasses. I'm just kidding. I don't know if you did this the other day, but these are observations at the end of your sessions. I was just dropping these in markdown.

**[8:08](https://www.youtube.com/watch?v=fwL31sNbq8g&t=488s)** So if these get written by the agent, the agent gets me human-readable feedback. So things like when I found out, oh, the MCP has no idea. We've not talked to any MCP. We have no context of the awareness of the entire world. We should build that into the into the loop. And to close, Dave Farley, who is having none of it. He puts natural language up against what a programming language actually gives you and finds it wanting. Worth saying. He writes no code by hand himself. This is not nostalgia. How does natural language measure up to that? Because natural language, somebody said today, I think they quoted Andrej Karpathy saying that the programming language of the future is English. I don't like that idea very much for the reasons that I'm talking about.

**[8:59](https://www.youtube.com/watch?v=fwL31sNbq8g&t=539s)** It's not precise enough, it's too vague. Natural language helps us. How does that measure up? Helps us to organize our thinking about a problem? Well, it's too vague, really. Natural language is open to misinterpretation. If anybody's been around. I can't really see you very well. But if you've got a gray beard like mine and you've been around enough, I bet that you've been in a situation where somebody coming down from on high and given a very vague instruction to a bunch of programmers, has gone away and then been really disappointed in the results because they didn't tell us in enough detail, that's really common. It's really easy to misinterpret what the goal really is. Natural

**[9:49](https://www.youtube.com/watch?v=fwL31sNbq8g&t=589s)** language is always open to interpretation. Time flies like an arrow. These are some time flies. Liking arrows. Vibe coding alone is simply not good enough. If we're just chatting with the computer to express our needs, that's not enough. We need tools that allow us to be more precise than that, to be more specific than that, to be better prompters of what it is that we want to achieve. That doesn't mean that we need to look at all the code, and are only allowed to do this in a programming language. I'm in the category of, it's been a long time now since I've. So I've written any code by hand because my AI agent writes all the code, but I've been more precise than just natural language in some respects.

**[10:42](https://www.youtube.com/watch?v=fwL31sNbq8g&t=642s)** In specifying what I want from it, I'm able to get what I want from it by using a precise, prescriptive version of natural language in order to be able to prompt it. And that's what I'm really talking about here. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
