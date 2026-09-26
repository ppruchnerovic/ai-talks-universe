---
id: svSCh3e7cuI
title: "Hugging Face's MCP Server: Only 62K of 10M Calls Matter"
slug: hugging-face-s-mcp-server-only-62k-of-10m-calls-matter
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-18T13:30:26Z
video_id: svSCh3e7cuI
url: https://www.youtube.com/watch?v=svSCh3e7cuI
youtube_url: https://www.youtube.com/watch?v=svSCh3e7cuI
tags: []
topics: ["Agents & orchestration", "Training, fine-tuning & model building"]
transcript: true
---

# Hugging Face's MCP Server: Only 62K of 10M Calls Matter

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=svSCh3e7cuI) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

MCP and integrations are the plumbing nobody wants to talk about, but Hugging Face's own production numbers make the case: out of every 10 million protocol messages, only 62,000 are the tool calls anyone actually wanted. At AI DevCon London, Shaun Smith, Maximiliano Firtman and Matthias Lübken showed what's actually breaking in the connective tissue between agents and the tools they're supposed to use.

What we cover:
– Why a stateful MCP handshake burns four calls before an agent gets any real work done
– Web MCP: letting a front end declare its capabilities instead of making agents guess from pixels
– Where to put guardrails when you can't control what the model decides to call
– Why Figma's own MCP server still reinvented components that already existed

Chapters:
00:00:00 - Introduction
00:00:25 - Shaun Smith, Hugging Face: running MCP in production
00:01:54 - Why the protocol is so chatty
00:02:07 - 10 million calls, only 62,000 that matter
00:02:32 - Maximiliano Firtman, Codemia: web MCP and the guessing game
00:04:40 - Giving the front end capabilities, not pixels
00:04:57 - Matthias Lübken: guardrails in the plumbing, not the prompt
00:07:15 - Marc Sloan, Tessl: an agent that reinvented what Figma already had

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What's the chattiest part of your own agent stack? Tell us below.

## Transcript

*1,524 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=svSCh3e7cuI&t=0s)** Back in June at AI DevCon in London, some of the best talks were about the least glamorous layer of all protocols, gateways and the connective tissue that everything else depends on. Let's first hear from Shaun Smith at Hugging Face, who's been running an MCP server in production for over a year and has the numbers to show how much of that traffic is just the protocol talking to itself. Good morning. My name is Shaun Smith. As Alan kindly introduced I work at Hugging face on open source connectivity and MCP and agents initiatives. in production, the MCP kind of gives us a couple of challenges. And the main challenge is comes back from that initial design, right? Which is that if I have a kind of a client and servant pairing,

**[0:51](https://www.youtube.com/watch?v=svSCh3e7cuI&t=51s)** there's an assumption in the protocol that the the relationship between them is stateful. So what's actually happening here is, is that the client will make a request to the server, and the server says I've initialized. And then the client sends back a notification and they've kind of hand shaken. So we've already kind of two messages from the client to the server in before we've actually established a session. After that, the client then will normally check and say, right, well give me the list of tools, give me the list of prompts, give me the list of resources. We're so we're now kind of we're at four calls in before we've actually even we've actually even serviced anything. And then finally we'll get a tool call in the information.

**[1:39](https://www.youtube.com/watch?v=svSCh3e7cuI&t=99s)** We'll go back to the client. Now again kind of typically what what we'll see in these kind of scenarios is if we've got state at both the client and the server, that starts to get rather rather tricky to manage. And it's also very, very chatty. So I kind of ran this I think it was on Sunday morning. This number kind of varies a bit based on the mix of clients we've recently seen. But at the moment, for every 10 million protocol messages that we get. So these are the kind of MCP protocol methods and calls, 1.2 million of them are initialize events, which can may be interesting, but actually only 62,000 of them at all calls. So the kind of overhead of managing that stateful connection is, is quite high from from a protocol level.

**[2:32](https://www.youtube.com/watch?v=svSCh3e7cuI&t=152s)** We also heard from Maximiliano Firtman on what he calls web MCP. Right now, an agent using your website is playing a guessing game screenshot. Guess click screenshot again. His argument is that the front end should offer capabilities instead of pixels. the problem is that Asians are burning when the browser is just a guessing game here. So it's observing a screenshots, the Dom or the accessibility tree. Then it's inferring what needs to be done. So I need to click there. I need to click on the date picker. Then I need to take another screenshot for example. I need to activate over that inferred data such as I need to click on that calendar icon to actually see that there is a calendar that is been open.

**[3:23](https://www.youtube.com/watch?v=svSCh3e7cuI&t=203s)** And of course we need to repair or repeat this because yeah, when I click on the calendar, I need to take a new screenshot and then see what's happening on the page. So this is consuming a lot of again, tokens. Okay. Time and context from our window from our context window. So it's a problem. So we need a new solution. That's kind of the idea. And web MCB is here to try to solve solve some of this problem. Maybe not all the problems but some of the problems. Because when will let the front end expose capabilities and not just pixels. So without Wembley the Asian is watching is analyzing is inferring over

**[4:14](https://www.youtube.com/watch?v=svSCh3e7cuI&t=254s)** pixels selectors Dom guesses or retry. And with retry loops again every time it clicks in each retry. And it's using image models or multi-modal models that are consuming more tokens and a lot of time to analyze what's on the screen and where to click. And now we are passing from inference to a contract that we as a web developer define. Matthias Lübken has been embedding a coding agent into a product, and he's clear eyed about the limits. You cannot control what the model decides to call, so you put your guardrails in the plumbing around the tool call instead. there are some ways you can actually help. If you are not able to define the tools or you cannot. You don't know anything up front.

**[5:03](https://www.youtube.com/watch?v=svSCh3e7cuI&t=303s)** There's a couple of ways to guide the agent as well. And these are extensions. So there's different level of extensions. I'm going to talk about the eventing mechanisms in Pi where you can basically write these extensions. And we've seen this in pi at with with pi the coding agent in the beginning. And the example where we're listening to events, there's different types of events, different agent life cycles, session life cycles where we can actually basically hook in and do things. The part that I'm going to talk about are the tool execution. So to call two call results, this is where most of the extensions that we've built play. Yeah we've built. So this is the example that I've showed before. We have this agent with the goal.

**[5:51](https://www.youtube.com/watch?v=svSCh3e7cuI&t=351s)** And we're calling these tools. And now we can ingest lifecycle hooks here. So for example before before we do a tool call or after we've done a tool result. So the the idea here is we cannot control that the LM is calling it. Right. That's the whole magic behind it. But when when it's when it does we can actually ingest and and filter out things or do something with the result. Here's the example from from our system. We have a in the draft email. When it drafts an email we do another sanity check that that the email is in the custom domain of the client. So we're kind of validating the output of of of a tool call and making sure that it does.

**[6:41](https://www.youtube.com/watch?v=svSCh3e7cuI&t=401s)** So far it always has been green. But this way we are making sure. Right. So we're not relying on the instructions, but we can actually make sure that always the right domains. And you can obviously do this with other validations, all types of business logic you can put in here. And that means that the flow of what the agent does is us open, right. But you can still make sure that certain systems, certain guardrails are implemented. Into close. Marc Sloan, who's on the product team at Tessl and worked on dev mode at Figma. Before that, they shipped the MCP server. An agent still produced code that looked right while reinventing components that already existed, which is a very honest story about how far a protocol gets you on its own.

**[7:33](https://www.youtube.com/watch?v=svSCh3e7cuI&t=453s)** moment? Well, everything I've described so far are real challenges that I've faced in my life. Prior to Tesla, when I was working at Figma on their dev mode product. For those who don't know, dev mode is a feature in Figma, which allows designers to hand designs off to developers human developers in this case, back in back in the Stone age, these were the tools we were using and it gives the developer lots of great context about the designs that they can use in manually creating the code to implement those designs. And over the last couple of years, we've seen that feature evolve into Figma, MCP server, the live Connection. Right. And what we're doing here is just taking that exact same design context, but giving it directly to an agent via the MCP server.

**[8:24](https://www.youtube.com/watch?v=svSCh3e7cuI&t=504s)** And it was in building this that we started to see all of those problems that I've been describing. We would see agents picking up the designs and doing a fantastic job in creating front end code that looked just like the design that functioned as the designer intended. But the developers would look at the code and it would have made up a bunch of components when they otherwise existed, or used them in the wrong way, or completely missed that there was a design system that it should have been working towards. These were real problems that I encountered with customers every day. And so we started. We realized quite quickly that we needed to find a way to bridge that product and design context gap with what agents were doing. And to that end, an early feature we started working on to address this was Figma Code Connect product.

**[9:13](https://www.youtube.com/watch?v=svSCh3e7cuI&t=553s)** And here is a tool that explicitly allowed design system teams to connect the design components in that design system with their equivalent in the code base. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
