---
id: jJQoVkd5yLg
title: "Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto"
slug: why-we-deleted-our-mcp-server-and-rebuilt-it-abhi-arya
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Abhi Arya"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-08T17:00:23Z
video_id: jJQoVkd5yLg
url: https://www.youtube.com/watch?v=jJQoVkd5yLg
youtube_url: https://www.youtube.com/watch?v=jJQoVkd5yLg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "agent experience", "agent-first software", "MCP", "MCP server", "AI agents", "tool design", "document AI", "document parsing", "human in the loop", "AI product design", "Reducto", "Claude Code", "Abhi Arya", "AI engineering", "AI Engineer"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto

**Abhi Arya**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#agent experience` `#agent-first software` `#MCP` `#MCP server` `#AI agents` `#tool design` `#document AI` `#document parsing` `#human in the loop` `#AI product design` `#Reducto` `#Claude Code` `#Abhi Arya` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=jJQoVkd5yLg) · [Conference site](https://www.ai.engineer/)

## Description

Reducto gave its whole team an MCP server with a tool for every endpoint. It broke the same day.

Abhi Arya, who works on product at Reducto, argues that building agent-first software comes down to one question: who pays when the agent is wrong? He describes three approaches, auto mode, user-first, and agent experience in service of the user, and how Reducto learned the difference. A first MCP server with one tool per API endpoint demoed well but fell apart when the whole team used it: the agent built entire workflows confidently, and nobody could explain them. He deleted it in one commit and rebuilt with fewer tools that carry the structure of real work, plus a snapshot tool for live state. Then he made uncertainty visible, with confidence scores and an agent that asks instead of guessing, and added instrumentation that made the system improve on its own, until the sales team adopted it without being asked.

In this talk:
• Auto mode vs user-first vs agent experience in service of the user
• Why one tool per API endpoint fails, and what to build instead
• Making uncertainty visible: confidence scores and asking instead of guessing
• Instrumentation that turns usage into a self-improving loop

SPEAKER
Abhi Arya, Product, Reducto
X: https://x.com/abhiarya

LINKS
Reducto: https://reducto.ai
Reducto MCP server docs: https://docs.reducto.ai/mcp-server
Reducto on X: https://x.com/reductoai

CHAPTERS
0:00 Intro
0:38 3 billion documents
1:48 What is agent-first software?
2:38 Who pays when the agent is wrong?
2:48 Auto mode, user-first, or in service of the user
3:57 Stuck in configuration
4:47 Version 1: a tool for every endpoint
5:27 It broke immediately
6:27 Fewer tools that carry real structure
7:32 A snapshot of live state
8:17 Don't just hand agents an API
9:07 Failures that happen quietly
9:42 Make uncertainty visible
10:22 Ask, don't guess
11:42 One root cause
13:07 Instrumentation and a self-improving loop
14:12 Sales adopted it on their own
15:12 What agent-first really means

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,752 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=1s)** [music] >> So, I'm Avi, and I work on product here at Reducto. And before I dive in right away, I wanted to give you guys some more context on what Reducto is. Uh we're an agentic document platform, which basically means that we help teams turn messy, unstructured documents into data that your tools and your AI agents can understand. I'll jump into the agents themselves in a second, but I'd like to talk about where we're at first really quick. In the last 3 years, we've processed over 3 billion documents across customers like Harvey, Scale AI, and top five global tech companies and

**[0:51](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=51s)** hedge funds. Running at that scale means that we've seen basically every way a document can break in production, and we've iterated our product and our models to handle basically anything that you can throw at them. And getting AI to work on a clean document with a frontier model is not super hard anymore. We basically like you can throw something in the cloud, and you might get like 60% of the way there. But the hard part is production. Scanned documents, rotated pages, etc. And the model starts hallucinating because a large majority of enterprise data is unstructured. And so Reducto is a layer that sits between your model and that data. We handle all the complex layouts and post-processing, and that way we end up working with and building a lot of agents ourselves while

**[1:39](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=99s)** designing these pipelines. So, now that you know a little more about what we do, I'm going to dive into our main topic with something seemingly unrelated. Um I visited my girlfriend this past weekend, and she gave me a sticker from the movie Mean Girls. And basically, it was an agentified version of it. So, it says, "Get in, loser. We're building agent-first software." And in true software engineer fashion, I had to put a sticker like that on my laptop. And she got this from work, but she asked me like, "What is agent-first software?" cuz she doesn't work in AI. And as as I was like doing so or as I was thinking about it, I realized I have a lot of different answers. Building a really good harness, building a really good API, writing or iterating on prompts. All of these don't really

**[2:26](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=146s)** um land on the agent being put first. They're more so just optimizing the model. Agent-first software is inherently an architecture problem. And so, I think that structure, that architecture, really comes down to one question, and that is who pays for the agent being wrong. And to that, I think there are like three buckets that you can put this into. So, you have auto mode to start, where you optimize for autonomy, you write a prompt, and you let the agent do whatever it wants. And when it messes up, which it will, you won't have any idea because it's really confident about what it's doing, and you're the one that's paying for it being wrong to your customers, your users, etc. Then you have user-first. This is where you optimize the human interface, give the user all the knobs, and then you build on an agent that

**[3:14](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=194s)** can't really do much, which is basically just a chatbot experience. You've both capped the user's understanding of the product because now they can't prompt it, and the agent's capability within as well. And lastly, the bucket that I think wins here is agent experience in service of the user. This is where the agent's capabilities are structured to give the model um rich and scoped capabilities where it can do things that the user really wants, aiding and enabling them, and even where the human can still verify the work that it's doing. This framing is what turns agent experience into less of a question of the model and more of a question of context, capability, and overall self-improvement. And here's how I discovered these buckets and came to that last point. At

**[4:03](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=243s)** Reducto, we've been building tools that basically automate end-to-end document work through pipelines. Think that we first parse a document, then we classify it, or maybe split it into sections, and then extract from it. Um and that's in use cases like invoicing, contract management, and all these things that require human input. One thing that I noticed early on was that any of the users, especially our sales team at Reducto, was spending all their time in configuration instead of outcomes. And that's a larger problem across the board because legacy interfaces were designed for kind of building that pipeline. Meanwhile, in this kind of agentic work world, we're increasingly focused on the final deliverable and how can we get the user to that point as fast as possible. So, the clear move to get here for us

**[4:51](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=291s)** was an MCP server. Let the agent do the heavy lifting and only burden the user with thinking about their use case and writing a prompt. To get some validation for the direction, I threw together an MVP with Claude code, and every API endpoint that drove our app was given an MCP tool in one massive file. I gave it a really pointed prompt. I put it in the Slack, and honestly, it was pretty nice. Um to some extent, it should have worked in that setting. I knew exactly what I was doing. I was building a really curated demo, and that's why the standalone demo told me nothing at all. The real test happened when I gave the MCP to everyone on the team, and immediately it broke. And here's how. Someone would feed it a half-baked description from a customer call or

**[5:40](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=340s)** maybe a Notion page, and the agent would just start going. It'd build the entire workflow end-to-end, but very confidently, it would tell the user that everything it did was right, but neither the user nor the agent could explain what the workflow actually did. And that is the root awakening of auto mode in production. The agent never really said that it's not sure. It handled with every tool that it had, and there was nowhere for a human to really validate or think about what was going on. We built something that could communicate with our system, but we hadn't built something that could actually work with it. And you'd think that the fix here is more detail on the system prompt or more model guidance, but realistically it's architecture. The whole file that we used to talk to the MCP, I deleted the

**[6:28](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=388s)** entire thing in one commit. And what replaced it wasn't more tools. It was mostly fewer tools, but they carried the structure of actual work. So for example, instead of one create step of this workflow to uh call over and over, and just praying that the agent assembled right in the pipeline, I built tools that understood how our internal dashboard or our product works. For example, a common use case with Reducto is to route our classify endpoint that classifies documents into an extract node. And what that does is basically extract information downstream. And instead of basically letting the model guess this or figure it out through the prompt, I turned it into a single classify to extract tool. And after each step, the agent gets contextual guidance

**[7:18](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=438s)** on what actually comes next, with certain tools even chaining automatically like this one. Rather than the agent having to guess or think about what is right versus being told what's right. Now the agent doesn't get to freelance the parts that we know are true. And since agents are stateless, we even added a snapshot tool. So this is one call that basically hands back the live state of our pipeline from the context of the entire flow to the errors that were surfaced with like really specific error codes. And that way they can reference what's actually there instead of guessing variable names, hallucinating, etc. By moving context out of the prompt and into structure, the agent stopped guessing and started referencing. And because the tools only let pipelines take the shape

**[8:07](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=487s)** that we as the engineers on the product wanted, the human could follow exactly what happened and we could explain the agent's outputs to downstream users of this MCP tool. So, to avoid auto mode, you don't hand your agent an API, you hand it tools that carry the overall expertise such as the right patterns, the state, and the validators so the correct path also becomes the simplest path that the MCP can take. So, we can build good pipelines now. We're done, right? Not really. Thinking back to auto mode, the agent was confidently wrong and no one could see it. Um that what we just talked about fixed that for building. The tools made the structure really legible and the human could follow what the agent did. But now the problem showed up at

**[8:55](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=535s)** runtime. When the outcome itself that the agent is trying to build goes wrong, who can tell? For example, if we had a really bad schema or maybe the user didn't really specify the actual use case, how can we tell that the agent did something wrong? And with agents it goes wrong quietly. So, instead of a seg fault or some actual error, um the pipeline runs across 100 documents and maybe it misses scan on page 30 or maybe the user didn't specify what types of documents were going into the pipeline. And basically both of these things are the same failure. The agent itself is very confidently wrong and the uncertainty that the agent has is completely invisible. So, everything that we did to fix this basically came down to one uh change, which was making

**[9:44](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=584s)** uncertainty really legible. In our system or with Reducto, uh failures carry information. So, with Extract, we output confidence scores, bounding boxes, all of this information about what went wrong, and we were able to build tools that feed that information back into the model, which actually helped optimize the extract schema over time, and get more accurate document outputs. But, that's just the outcome uncertainty. The agent also has to surface its own uncertainty. When it hits something ambiguous, um two ways to read a field or a document type that it hasn't seen, it shouldn't guess, and it shouldn't just pause exactly where it is. And rather, it should ask, "I can read this two ways," and tell the user, "What did you mean?" And so, basically in our evals, we started

**[10:33](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=633s)** failing the agent for building any shaky assumptions, and we gave our harness uh prompt guidance to use the ask user question tools, etc., that Cloud Code and other like frontier harnesses offer, instead of guessing. So, we rewarded asking instead of guessing. And judgment doesn't live in the agent alone. This entire pipeline is still overseen by the user, and the confidence and the reasoning of the agent was then outputted as basically prompt guidance in the MCP. So, now every time you make something new, it explains to the user what it did and why, so the user can then review it, inherently acting in service of the user. The agent basically satisfies what you wrote, and not the um outcome that you wanted. So,

**[11:23](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=683s)** what happens if you make the uncertainty basically a bit more legible, and you keep the final judgment where it can actually be accountable in the hands of the human, then that one clarifying question does the work of all three, giving the model context, capability, and also adding a human in the loop to actually build that judgment and verify things as well. So, going back to kind of all of these failure modes overall, we had initially an auto mode that nothing nobody could inspect. We had wrong answers that basically arrived in silence. And then an agent that passed the test by reward hacking or hiding what it did. And underneath, they're basically one shape where the agent had more autonomy and more access than the human could verify. And that intelligence lives in the

**[12:13](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=733s)** construction overall. So, building the pipeline, generating the schema, and pulling in the right context is where the agent is more most powerful and where a mistake is the cheapest because the human is right there. By building for that interface, we were able to also have user satisfaction go up with the MCP because they could really see what was going on. And by using Reducto for the document layer, we can guarantee accurate parses and extractions for parts of the pipeline that we can't trust agents with. Where the agent operates, it earns trust by being verifiable, correct, and building trust in service of the user. And the whole conversation we had about legibility overall is what inherently pays off. Agents are just intelligence in a box and the harness that you

**[13:03](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=783s)** surround them with is what provides them with the ability to deliver these outcomes downstream. And so, once we reach this point, we focus on instrumentation where every MCP session, the prompts that were sent from the model were logged, and we even asked like our sales team and other people on the team to basically export their cloud code sessions to understand how how was behaving. Where humans overrode the agent, where confidence of the model ran low, and where it asked questions. And because we added all this instrumentation, um it flowed back into the long-term guidance that the MCP had overall. So, the system got better at building pipelines by building more pipelines without us rewriting by hand. This then became a self-improving loop per org or per user that was building these

**[13:51](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=831s)** pipelines. The foundation became overall the same decision where we kept the model very guided and very inspectable, and the information around it became everything else that actually guided the model. And so, one thing that kind of told me that we were doing something right with these improvements is I never like explicitly told the sales team to use the agent to build pipelines, but rather I just exposed it in our Cloud Enterprise as product tools. And the sales team and various other people on the team started basically wiring it into their workflows. So, before they had a customer call, they would use CircleBack or Slack and basically learn about the customer and then use the MCP to basically ask them questions about the customer and then build a pipeline for that customer downstream.

**[14:41](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=881s)** So, when an agent's experience was built really in service of the users that were using it, we weren't pushing people directly toward it and rather they reached for it and actually started using it as a company-wide resource. And that's where they also started to trust the output enough to put this in front of high-value customers because the demo didn't just work, but the human actually said, "Hey, I built this. Come check it out." And it actually paid off in these sales calls. And I hope the Slack reactions can also help gauge that a little bit. So, overall, a few months ago I would have told you that agent first is means that you have the best model, the best inference speed or intelligence of the model. And with models getting better from closed source to open source, from expensive to cheap,

**[15:30](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=930s)** I think it now means almost the opposite of what it sounds. To some extent, the agent doesn't go first. And to build for agent experience means you have to consider the agent being in the loop with the people who have to answer for the work downstream. So, it's not just what does the agent connect to? Everyone's agent connects to everything nowadays, and Claude can make a new connector for you immediately. But, regard Beyond that, it's when your agent is really confidently wrong, who finds out and how fast did they find out? If you build for that, then you can build for something that people will actually trust with real work. And yeah, that's about it. Thank you, guys. And also, we're at Reducto's at a booth P8, and we are hiring for a lot of positions. So, please come check it out

**[16:19](https://www.youtube.com/watch?v=jJQoVkd5yLg&t=979s)** at reductoai.notcurious. Thank you. >> [music]
