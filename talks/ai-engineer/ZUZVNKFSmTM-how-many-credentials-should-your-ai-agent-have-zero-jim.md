---
id: ZUZVNKFSmTM
title: "How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker"
slug: how-many-credentials-should-your-ai-agent-have-zero-jim
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Jim Clark"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-10-06T00:30:15Z
video_id: ZUZVNKFSmTM
url: https://www.youtube.com/watch?v=ZUZVNKFSmTM
youtube_url: https://www.youtube.com/watch?v=ZUZVNKFSmTM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "MCP", "Model Context Protocol", "MCP gateway", "AI agent security", "agent sandbox", "Docker", "Docker Sandboxes", "sbx", "least privilege", "credentials", "Okta", "Cross App Access", "AI safety", "Jim Clark", "AI Engineer"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker

**Jim Clark**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#MCP` `#Model Context Protocol` `#MCP gateway` `#AI agent security` `#agent sandbox` `#Docker` `#Docker Sandboxes` `#sbx` `#least privilege` `#credentials` `#Okta` `#Cross App Access` `#AI safety` `#Jim Clark` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=ZUZVNKFSmTM) · [Conference site](https://www.ai.engineer/)

## Description

Agents now run long enough that you stop watching them. So what are they allowed to touch?

Jim Clark, principal software engineer at Docker, uses MCP gateways as a way into agent safety. Harnesses are simple loops. Safety comes from what context and tools flow into them, so the boundary to manage is the sandbox. Through two examples, a newsroom split into researcher, fact-checker and publisher sandboxes, and a coding agent that only gets signing keys when it's committing, he shows how to model each sandbox on the task's intent. He explains how a single MCP gateway endpoint per sandbox gives you a control point and makes harnesses interchangeable, why the right number of credentials in a sandbox is zero, and how Cross App Access (XAA) with Okta lets agents use your existing SSO.

In this talk:
• Why safety comes from limiting tools and context, not from the harness
• Splitting one workflow into sandboxes that never mix untrusted input with dangerous tools
• An MCP gateway as the single control point for tools, resources and prompts
• Agent identity and authorization grants with Cross App Access (XAA)

SPEAKER
Jim Clark, Principal Software Engineer, Docker

LINKS
Docker MCP Gateway (GitHub): https://github.com/docker/mcp-gateway
Docker Sandboxes docs: https://docs.docker.com/ai/sandboxes/
sbx CLI reference: https://docs.docker.com/reference/cli/sbx/
Okta Cross App Access: https://www.okta.com/solutions/cross-app-access/

CHAPTERS
0:00 Intro
0:18 Hi from Docker
0:52 This is really about AI safety
1:17 Agents run longer, unsupervised
2:02 Harnesses, sandboxes and MCP
2:32 What a harness is
3:37 What MCPs add
4:37 What a sandbox is
5:56 Example: the newsroom
8:41 Example: a coding agent's signing keys
10:06 One gateway endpoint per sandbox
10:56 A control point, and swappable harnesses
12:05 Zero credentials in the sandbox
12:30 Cross App Access (XAA) with Okta
14:25 Progressive disclosure for tools
15:05 Orchestrators that build the sandbox
16:14 Recap: role separation and intent
17:04 Try it: brew install sbx

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,911 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=1s)** [music] >> I guess I'm ready to start. Uh can everyone can I I actually I can hear myself. Yeah, so you guys can hear me. Uh my name's Jim. Uh I'm a engineer at Docker. Normally when I introduce myself in the slides these days, or at least what I used to do, was I would say, "Hey, I'm Jim. I uh like spaces, not tabs. I use Neovim, not Emacs." But, that's uh all irrelevant now. So, uh I will say that I made this slide with uh I made this presentation with Claude Code.

**[0:49](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=49s)** I used the Codex model. The MCPs that I that helped me write these slides were Marp and uh Mermaid. And I'm going to talk to you about MCP Gateways. But, I'm really going to be talking to you about AI safety. So, I'm going to kind of go through sandboxes, gateways, harnesses, and sort of motivate why we're talking about AI safety at Docker right now. So, like probably the last 6 months has been similar for all of you as it's been for me. Agents are doing way more than I thought they were doing uh than I thought they were going to do. And I'm no longer going to sit in front of my laptop and say, "Yes. Yes. Yes. Yes." They're doing longer running things, and

**[1:38](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=98s)** I like that. And as I get more and more accustomed to them doing longer running things, I sort of decide that my metric for me having designed a problem that an agent can sink its teeth into is that I don't really need to give it a lot of supervision. But if I'm not going to supervise it, maybe I'm also a little bit worried about what it's going to get up to. So I think just to set context, this is what I think is so the sort of shape of the problem right now. We need to talk about agent harnesses, what the what the agent harnesses do for us. We need to talk about sandboxes. Like when a agent harness delivers work, what is the what is the thing it delivers work into? And then of course

**[2:27](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=147s)** we've got MCPs, which which everybody knows, and we'll talk a little bit more about what we're doing there. But let's start with the agent harness. So I I mean it's it would be an oversimplification to say that an agent harness is something which just takes in context and emits tool calls. But there's also a little bit of truth to that. It's not the most complex part of it. It's a loop that takes in some context that you give it and asks you to do something on its behalf. But belaying that simplicity, we get we're all using a lot of different harnesses. And the inter the ability to why why do we pick up different harnesses all the time? Like we love the new sort of interactive interactive possibilities

**[3:15](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=195s)** that they bring us. So let's just admit right from the beginning, we're going to be using a lot of harnesses. They're going to evolve pretty quickly. We're going to be swapping in different harnesses for one another. But a harness by itself is just kind of in a little bit of a dead room. Like uh hello, someone give me some context. Some somebody give me something to do. This is where this is of course where MCPs come in. MCPs allow us to do new things. They allow us to go outside of ourselves, pull in new context, pull in new tools, and and get actual work done. So, I think it's when you're trying to think about safety, I don't think it's an oversimplification to say that one of the things that you need to do is figure out what are the

**[4:05](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=245s)** resources that you need to do your job. Like anytime, even for us, one of the first things you'd analyze when you want to do a new task is what do I need to get this tasks done? What information do I need? What tools do I need to actually get this done? And if you knew that the sandbox that you built had the right resources, had the right tools, and only the right those resources and tools, it would make you feel safer. It would make you feel like you limited the blast radius for what could go wrong when that agent is working. So, this is kind of where sandboxes come in. Sandbox is a place for an agent to do to do work. So, our typical sandboxes today, you're most of us are accustomed to the

**[4:54](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=294s)** Yeah, we have code sandboxes. We give it We give it a bunch of code. We give it all the tools on our laptop. Maybe like when you first started using some of these agents, the sandbox was your entire laptop. As over time, we're starting to learn how to get that a bit smaller. We're trying to make the sandbox boundaries small enough that they can actually just do the task that we want to do want them to execute. That helps us feel safer about letting the agent run for longer periods of time if this if the sandboxes is a little is is is smaller. And you know, it's not that we're trying to sandbox the harness itself. The harness is kind of already sandboxed. Like it's a it's a pretty simple thing. We're trying to harness

**[5:42](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=342s)** the tools and the context that are flowing into this harness. So, in order to kind of illustrate some of these concepts, I came up with two stories that I'm I'm just going to walk you through. The first one is um a newsroom analogy. So, if you've got a newspaper reporter, they go out in the world, they find cool stories, find cool information, they bring it back. Maybe someone inside of that agent agency uh look it does some fact-checking on that, make sure the information is right, and then you write a story. It's totally natural that those roles are completely separate. The actual reporter is not going to be allowed to like publish to the website or or or write write the actual article. We

**[6:30](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=390s)** we break those up. That's actually how we already build complicated systems. We split them up into little pieces. So, on this slide, what you see is I've broken down three sandboxes in blue here. So, we've got a researcher, we've got a fact-checker, and we've got a reporter. So, that researcher sandbox, I think I think about that as the reporter. Now, when we define that sandbox, let it access the web. Let it access as much of the as much of the internet as we want because we're not going to give it the MCPs that it can like write to our our corporate site. It can't publish anything. We're just going to let it do we're just going to let it go out, go crazy, do research. So, our sandbox is like, "Yeah, not too many tools. I'm not going to give you

**[7:17](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=437s)** too much write access, but definitely do lots of research. Just write your research out to a I don't know, to some temp directory, some private thing that is local to this agent." A fact-checker is going to need some MCPs, but it's not going to need any network. So, then let's start the fact-checker up. Let's put that in a different sandbox. Let's say no network. Yeah, and you can read the research that's been done for you, and you can fact-check it. And you can have access to our our fact database. You know, filter that out. And then finally, we get to the little blue thing on the right. And this certainly doesn't need any any access to networks. In fact, it shouldn't have any, but we do want to give it our notion MCP or our publisher MCP because it's just looking at filtered research.

**[8:06](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=486s)** So, you know, look at this whole slide, draw a box around this entire slide, and that effective agent has a bunch of MCPs. Maybe it has an MCP for publishing, it has an MCP for fact-checking. At one point in time, it has access to the entire internet. But we break it up into logical sandboxes, so at each individual point, we have a don't have a dangerous concept a dangerous combination of both being able to read in crazy unfiltered context and do things with our tools. So, let's look at example number two. And I'm just going to talk about uh building a Actually, this is how I I build my coding agent right now. I tend to send the the coding agent off to do pretty

**[8:56](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=536s)** long-running tasks. And let's just say that they work for about an hour. But as the as the work is happening, I also like it if it just does commits along the way. But the ratio of the amount of time that it's my agent is actually committing is almost nothing. In an In an hour, it might be it might need, say, my my my Git signing keys for like 2 minutes of that time. And when I'm committing, I need to see my my Git commit tree. I need to make that commit. I need some signing keys, but I don't need anything else. So, I would like it if the actual sandbox that an agent is running a task in is modeled after the intent of what I'm

**[9:43](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=583s)** doing. So, if I'm not going to make a commit, I don't want my commit signatures, my commit signing keys inside that sandbox. And I think this this you can map across a lot of different tasks. If you know the if your agents know the intent of what you're trying to do, then use that intent to model the capabilities that you give to that. So, this is driving in in our our Docker sandbox product, this is defining a lot of how we're thinking about exposing things like an MCP gateway. So, when you build a sandbox, of course you have to put a harness in in that to do things for you. And then we're just putting a little gateway endpoint into that.

**[10:30](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=630s)** And that gateway endpoint funnels all MCP traffic. So, imagine it's something like MCP an internal an an internal URL mcp.gateway.docker.internal or something like this that every single agent harness has and all traffic, all resources that you need to pull in, all tool calls move through this one this one single gateway. So, what does this buy us? Well, we end up with a control point. So, the gateway manages which tools, resources, and prompts are given to each sandbox. So, you're starting to see the beginnings of your ability to say, "Okay, I'm giving you a harness. I'm giving you this gateway endpoint. The gateway this the configuration of the sandbox controls what you can do inside

**[11:20](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=680s)** of that sandbox with things like MCP." Another nice thing is suddenly all your harnesses are MCP agnostic. So, you don't have to go to codex and configure your MCPs one way and go to uh cloud code and configure your MCPs one way. You just have one you almost make the harness a parameter of the sandbox. Stick a harness in, stick the MCPs you need in, give it some network rules, Bob's your uncle. So it's it feels the MCP MCP is is a good place to manage things like credentials. In fact, I would say that a maxim that you can use here is how many credentials should be in uh a sandbox. Well, I mean the the the right answer is always zero.

**[12:08](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=728s)** It just they should just never be in there. And the blast radius of an agent going doing something going going uh doing something incorrect, if there are absolutely no no credentials in there, is is reduced. So one of the things that um Docker, Entropic, Octo are all partnering on is a is a new thing called XAA, cross app application. And I think this is a really great illustration of why sandboxes and um and managing credentials in this way is important. So today in your well you're you're working at at at your companies, you have some sort of identity management, you have SSO set up, and you've got all these resource servers that that manage that that that

**[12:56](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=776s)** you work with for OAuth. It could be Notion or it could be Atlassian or GitHub or Slack. They're you've already configured SSO for those. But it's not yet accessible to your agent. So with a cross app application scenario, your harness, your your your sandbox, and your gateway can define things like agent identity or who are you that this agent is behaving on behalf of? And by extension by exchanging identity claims with your identity provider, which is already there, you can get back a new thing, which is a new part of this spec that you you'll now see in the latest version of MCP, called an ID jag, an authorization

**[13:45](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=825s)** grant. And with that authorization grant, we're granting access to this act to the to this actor to this agent to the same authorization servers that you've been using. There's nothing new here. We're not We're leveraging all this existing investment that these corporate internet corporate networks already have, but suddenly, without any crazy consent screens, yeah, you can do that. Yeah, you do that. Yeah, you can do that. We can centralize the administration of what an agent now does with all these existing resource servers. It's a great It's a huge simplification. So, the MCP gateways, I like to think are we're starting to talk about progressive disclosure, which is a term we learned from from skills. I like to think we're starting to use this now

**[14:33](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=873s)** we're able to progressively disclose tools and resources and MCPs into these sandboxes using very, very similar principles. And of course, it's amazing because we keep contact size down. Just because you might at some point in a workflow use 50 different MCPs, doesn't mean that each sandbox has to have all 50 of those MCPs. Give your agents room to solve problems, but let individual sandboxes represent the intent of the task. Let them represent what you're actually trying to do in this task. So, I like this picture because suddenly we start to think about orchestrators as one of their jobs is to go, "Well, what am I doing? What's my task? And I need to put a task into a sandbox. So, what

**[15:22](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=922s)** sandbox do I put it in? What capabilities does this need? And of course, it needs a harness. Like, what do you put in? Open code? Put in Claude? Put in Gemini? Put in Codex? It's going to need some MCPs. Take a look at the task, decide what MCPs are allowed to be used in this. Um what networking rules should you apply? Does this need access to api.github.com? Does it need access to surf the web in in in random ways? Or does it just need nothing? What resources? What work trees? We get used to thinking about modeling capabilities, building the right sandbox for the task, putting the task in, and now we're starting to see that this individual loop is safer because it has less access than the entire workflow

**[16:11](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=971s)** effectively has. So, this is um this is about containers. This is about containerizing agents, which is why uh I guess this is why we're at I'm I'm at Docker. But this ties together as a kind of like role separation. What are the roles that you that your agents have? How do you map them and containerize them and and make sure that you're giving them sandboxes that express that intent. Never have any any creds anywhere in any in any harnesses. Disclose capabilities progressively into agents as they need them. The sandboxes for you are are are what actually represent intent. And if we allow some of these things to run longer, but they're more sandboxed, we feel a little bit safer about that.

**[17:00](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=1020s)** That's this is where safety comes from. So, we have a demo. Our our EVP of of engineering, Tushar Jain, is I got to talk upstairs today. I think it's at 4:00, and he's taking a lot of these ideas and just demo demo demo. How do you make move sandboxes to the cloud? How do you build orchestrators? He'll be really showing a lot of these things live. We also have a booth over here. Um it's a great opportunity to come over if you're interested in any of this stuff. We can show you the command line that's available today. Anyone uh just brew install sbx. That Everything I've been talking about today is this tool sbx. This is This is how we build we build containers. Um so yeah, please please uh please come over and talk to us at the booth. We'd uh we'd love to

**[17:48](https://www.youtube.com/watch?v=ZUZVNKFSmTM&t=1068s)** hear what you're uh what you're doing with AI safety and how we might be able to help. But uh thank you very much. >> [applause] [music]
