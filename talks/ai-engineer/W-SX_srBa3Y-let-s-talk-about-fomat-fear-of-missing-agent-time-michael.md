---
id: W-SX_srBa3Y
title: "Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl"
slug: let-s-talk-about-fomat-fear-of-missing-agent-time-michael
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Michael Richman"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-05-24T16:00:06Z
video_id: W-SX_srBa3Y
url: https://www.youtube.com/watch?v=W-SX_srBa3Y
youtube_url: https://www.youtube.com/watch?v=W-SX_srBa3Y
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl

**Michael Richman**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=W-SX_srBa3Y) · [Conference site](https://www.ai.engineer/)

## Description

You kicked off an agent 30 minutes ago. It stopped after two minutes, blocked on a question, and has been waiting ever since. Michael Richman calls this FOMAT: fear of missing agent time. His answer is Cmd+Ctrl, a system that sends you a push notification when the agent needs input, lets you respond from your phone or watch, and lets you start new sessions from wherever you are.

The demo shows Claude Code running in a terminal while the Cmd+Ctrl app on an iPhone mirrors the session in real time. Walk away, get notified when the agent completes or gets stuck, reply from the phone, pick up in the terminal. The same setup works across Claude Code, Cursor, Codex, Gemini CLI, and others through a daemon that runs alongside each agent and reports to a shared control plane. The daemon layer is open source. A standup dashboard summarizes all recent sessions so you can catch up without reading every thread.

Speaker info:
- https://x.com/mrwoofster
- https://www.linkedin.com/in/michael-richman-b7807b2/
- https://github.com/mrwoof

## Transcript

*2,455 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=7s)** [music] >> Thank you, everybody. My name is Michael Richmond. Um I lead several teams at Bitly, the link shortener, but today I'm here to talk to you about FOMAT. Uh fear of missing agent time. You know FOMO, fear of missing out. You also know FOMAT, you just didn't have a name for it. Um What is fear of missing agent time? It's being out on a walk and having an idea that you want to task your agent with and having to wait to get back to your dev machine to actually do it. It is

**[0:54](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=54s)** when you get up from your desk and you had an agent working 30 minutes ago chugging away and you get back and you realize that after 2 minutes it actually stopped to ask you a question. And it's been waiting there blocked the entire time. We all want to believe that our agents are low touch uh sorry, are low touch and high autonomy. But we all know the truth, right? It's back and forth, it's babysitting and you cannot predict when you're going to be needed for input. Right now coding tasks might typically take anywhere between 5 minutes or 45 minutes and you kind of know when to

**[1:43](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=103s)** check back. There isn't that much time that's spent in agent idleness. But that window is only going to get longer. And the longer the agent waits for you, the more agent time that you have missed. If a task is running for 5 hours or eventually 5 days, you can't just check back in a bit. You need to know when it needs you and you need to know when it's done. And that might be whenever you are wherever you are. It may be whenever you can't predict it. You may not be at your dev machine. Did I go back? I went back, sorry. So like once I once I once again, my name is Michael Richmond. I run several engineering teams at Bitly. I also co-lead our AI coding tools strategy. Um I'm a really hands-on

**[2:33](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=153s)** engineering leader. I run teams and I also write code. I co-wrote the Bitly MCP server. And I train our engineers on AI skills and best practices. I think about tools a lot. The tools that we use every day, how they work, whether they are effective for our workflows or not. And agentic coding has really changed the world of software in the last year and the road is very much being paved as we are driving on it. So I built a system called command and control in order to help me work with coding agents outside of the terminal or the IDE because I really needed it and nothing existed to solve it yet.

**[3:21](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=201s)** Anthropic recently released some ways to address this with remote control and uh the teleportation mechanism and I think it was just 2 days ago cursor came out with a solution in the space. So I wrote command and control. One of the things that is nice about command and control and I'll show you it in a minute is it is a way to get all of your coding agents in one place uh on your mobile device or really anywhere. So this is what my setup looks like. I have multiple terminal windows. Each of these windows has multiple tabs. Here's Claude Code. Here's what Codex would look like here. Here's Gemini. Here's the cursor IDE. And at any given moment I might have multiple sessions running multiple agents across all of these in various states of completion.

**[4:10](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=250s)** And here's the thing. I don't know about you, but I cannot keep track of more than two or three sessions at a time. As soon as I get to four or five, I don't know what session two is doing anymore. I don't know which one needs my attention and I have no idea which states of completion things are in. So how do you know when an agent is stuck and needs a decision from you? How do you know to check in on an agent mid-task and that to find out that it's gone off the rails? What if you want to start a new session and you're not at your dev machine? That's exactly why I built this system. So this is what it looks like on an iPhone app. It's on Android, it's on the web and it lets you monitor and interact with agent sessions and launch new

**[5:01](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=301s)** sessions from anywhere. From your phone, from the web, even from your watch. I have a couple of video demos that I'm going to play and show you a few of the features of it. And the point here really is like this is a [clears throat] solution to a workflow problem, one solution. We saw this morning uh what was it called? Agent Craft, which is a gaming version of something similar, which I thought was awesome. So here's the first demo slide. Okay, here I am in the terminal. I'm going to start a Claude Code session and I'm going to issue a command that's pretty run-of-the-mill. I'm not actually exercising Claude Code functionality. I just want to demonstrate command and control. So if I come over here to my phone simulator, you'll see that I've got command and control app over here

**[5:51](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=351s)** and what I've got here is my session. This is all of my sessions grouped by ones I want notifications for and ones that I want to keep my eye on and recent ones. And here you'll see the one we just issued here 27 seconds ago. Let's get out of this session over here and what you'll see here is the response I got from the agent is the same one because it is the same session. Now the beauty of command and control here is that let's say I want to subscribe to this particular session for notifications and I'm going to issue a um response to this one. I'm going to say sleep for 1 second and say hello. And as soon as I hit this, I'm going to leave the agents working. I'm I left the

**[6:39](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=399s)** app cuz what I want to demonstrate here is the push notification that I'm going to get once it actually completes. And there it is. So I can click right into that guy and I got the hello. Now if I come back over to my session and I resume this guy my response is right there with the agent response as well. The beauty of this is that I don't have to stay in my terminal. I can walk away with my phone, get notified when there are answers and respond right from there. So that's one basic feature of command and control, interacting with sessions from anywhere. Let's see another one. This is starting a new session in the

**[7:29](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=449s)** mobile app. I was going to do live demo after I recorded these videos backups, I was like I'm going to show the videos. So here's the next one. I want to demonstrate another important feature of command and control and that is that I can start a new session right from the command and control UI. I can pick any configured agent that I've got here. I'm going to stick with Claude Code, but you see I've got Codex and GitHub Copilot and Cursor here. I'm going to stick with Claude Code and I'm going to switch my directory to a testing directory and I'm going to just ask it what time is it? Now the reason I'm showing you a pretty simple prompt, the prompt doesn't matter cuz the point is that I'm issuing a prompt to my agent and I'm getting a

**[8:19](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=499s)** response. Now you can see I'm working late at night here. And the beauty is I can go over here and resume the session and here's my session right here that I started from command and control. I can go into it here and pick up where I left off. And if I issue a command here, what is the mm date tomorrow, let's say. What I will see over here is the same conversation and that is the beauty of command and control. I often start my day with prompts that I issue from bed, honestly, and start up a bunch of sessions and resume them either in the CLI or I continue them right on my phone.

**[9:09](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=549s)** I hope you're starting to see the power of command and control here. And like I said, this applies to any of the coding agents that I've got configured on my machine. Now to the problem of keeping track of sessions. This third video and then I'll talk a little bit more about the importance of this is uh session management. Now I mentioned how hard it is to keep track of all the sessions you've got going. I mean if you just look at the number of sessions I've got here, um there are a lot and I want to do revisit the different sections that are available in command and control. So as I mentioned, you can subscribe for

**[9:59](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=599s)** push notifications. That's this top section here. The on my radar section is ones that I just want to keep my eye on, but I might not want to have be as chatty as push notifications for every message. Then there's a recent section here, which is basically the last 24 hours, and then the rest. Now, you can see there are thousands of sessions here. I couldn't possibly keep track of them all, but here they all are organized for me. Another useful feature in Command and Control is what is referred to as the overview dashboard. One of the really nice features of this one is you can get a kind of stand-up summary of the most recent sessions. And this is just using the last several messages to kind of

**[10:47](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=647s)** give you an overview of what's been going on for each of those. So, I hope you can see the the power here, and I think this is the kind of thing that we need in our new world of agent orchestration. This is a number of things. This is interacting with your agent sessions or starting new sessions from wherever you are. It is session management. It is notifications, so you know when your agent needs you, and you don't have to guess. And it's also all of the coding agents that you might be using in one place. It's all those things from wherever you are. A little bit about the architecture of this, which you might be curious about.

**[11:35](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=695s)** So, the each agent platform, Cloud Code, Cursor, Codex, Gemini, Open Code, they have a Command and Control daemon that runs alongside. They talk to a control plane layer. They monitor life cycle of the agent. When things change, it's blocked, it needs your help. It communicates up to the control plane layer, and then the UI talks back to that API layer and notifies you of things. The control plane aggregates all of the agents, regardless of where they're running or what framework they're running on. And so, this could be your dev machine, this could be a cloud VM, or it could be both. And this is an important point that I want to emphasize. I needed a system that is a single pane of glass into all of my agent sessions. Regardless of

**[12:26](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=746s)** which platform they're running on, regardless of what machine they are on. I might have Cloud Code running on my Mac and Codex CLI running in a cloud VM, and all of the sessions from both of those are available via a single UI. And like I said, it's coding tool agnostic by design. It works with almost all of them. I will also add that the daemon layer is open source, so you could plug it into any of your agent frameworks that you're working on, and then access it through the the single UI today. So, whatever your agent, you can reach it, and it can reach you. And this brings me to the point of like we all want our agents to be maximally autonomous, right? And the honest truth is that they are not yet, as much as we

**[13:15](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=795s)** hype it. And especially not if you're limited to how you can interact with them to their native environments. This is one solution that addresses that problem. And I want to talk about a little bit of a broader concept here that this is related to. And that is that just in the last year, the agentic coding workflow has completely transformed what software development is. It is transformed how we work, and it is also transformed how we enjoy how we work. So, you know the old the concept of flow, which is like being totally in the zone, locked into your code, hyper-focused on a single thing. You and your code

**[14:03](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=843s)** solving a problem. And I think that the new type of flow in the agentic world is more about agent choreography. Multiple agents working in parallel with you moving between them, unblocking one, redirecting another. And the new flow comes from the elegance of that choreography and the results on the other side. So, then maybe that some of that fear of missing agent time can be alleviated. Another thing I really want to note here is that this paradigm of the always available agent is actually highlighting the value and importance of time away from your

**[14:52](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=892s)** agents. Matt Pocock alluded to this yesterday. I don't know if you heard the Simon Wilson interview on Lenny's podcast last week. The cognitive load of managing multiple agent sessions is really high. And it is exhausting, as you all probably are aware. You need a break. And here's the thing. It is in those breaks that we often have our best ideas. We need systems that make it possible to reach our agents during those breaks, wherever we might be and whenever that happens. And that is how we truly alleviate the fear of missing agent time. Once again, my name is Michael Richmond.

**[15:42](https://www.youtube.com/watch?v=W-SX_srBa3Y&t=942s)** I'd love to hear about your workflows, your hacks, the pain points that you encounter. I invite you to give Command and Control a try if you're interested. Here's where to find it online, and here's where to find me on LinkedIn. I'd love to connect and continue the conversation. Thank you. >> [applause] [music]
