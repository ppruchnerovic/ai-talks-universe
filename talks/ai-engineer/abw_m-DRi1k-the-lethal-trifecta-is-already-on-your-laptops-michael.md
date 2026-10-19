---
id: abw_m-DRi1k
title: "The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder"
slug: the-lethal-trifecta-is-already-on-your-laptops-michael
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Michael Patterson"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-10T15:00:03Z
video_id: abw_m-DRi1k
url: https://www.youtube.com/watch?v=abw_m-DRi1k
youtube_url: https://www.youtube.com/watch?v=abw_m-DRi1k
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "lethal trifecta", "AI agent security", "agentic security", "prompt injection", "coding agents", "Claude Code", "OpenClaw", "cloud development environments", "AI gateway", "agent firewall", "shadow AI", "CISO", "Coder", "Michael Patterson", "AI Engineer"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Security, safety & red teaming"]
transcript: true
---

# The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder

**Michael Patterson**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#lethal trifecta` `#AI agent security` `#agentic security` `#prompt injection` `#coding agents` `#Claude Code` `#OpenClaw` `#cloud development environments` `#AI gateway` `#agent firewall` `#shadow AI` `#CISO` `#Coder` `#Michael Patterson` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=abw_m-DRi1k) · [Conference site](https://www.ai.engineer/)

## Description

Your coding agent can read private data, take in untrusted content and talk to the internet. That's the lethal trifecta, and it's already running on your developers' laptops.

Michael Patterson, staff solutions engineer at Coder, explains Simon Willison's lethal trifecta (access to private data, exposure to untrusted content, and the ability to communicate externally) and why agents like Claude Code, Codex and OpenClaw running on a laptop hit all three. He covers prompt injection, what blocks big companies from rolling out agents (CISO concerns, shadow AI on personal subscriptions, alert fatigue, skeptical senior engineers), and three architectural guardrails: cloud development environments that isolate the agent, a model proxy that logs traffic and strips sensitive data before it reaches the LLM provider, and an agent firewall that denies commands and domains you didn't allow.

In this talk:
• What the lethal trifecta is, and why laptop agents hit all three parts
• How prompt injection turns trusted sources into attacks
• What security teams worry about when agents roll out at scale
• Three guardrails: cloud dev environments, a model proxy and an agent firewall

SPEAKER
Michael Patterson, Staff Solutions Engineer, Coder

LINKS
Coder: https://coder.com
The lethal trifecta (Simon Willison): https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

CHAPTERS
0:00 Intro
0:40 What is the lethal trifecta?
1:20 The agent boom
2:04 When agents delete production
4:04 What Coder does
5:24 The three ingredients
6:44 Prompt injection
8:09 Three pillars of agent security
10:08 Rolling out agents at big companies
12:48 What the CISO worries about
14:08 Alert fatigue
14:48 Skeptical engineers
15:33 Guardrail 1: Cloud dev environments
18:13 Guardrail 2: Model proxy
18:57 Guardrail 3: Agent firewall
20:12 Wrap-up

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,259 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=abw_m-DRi1k&t=12s)** How's everybody doing? Coolio. Well, it's nice to be presenting to you all. I hope we're all having a good time here at the the AI Dev Conference the AI Engineers Conference. Um, my name's Michael Patterson. I'm a staff solutions engineer here at Coda. Today, I want to talk to you about the lethal trifecta. So, we're a bit of a small crowd. Uh, can I get a raise of hands? Has anyone heard of the lethal trifecta? All of us or half of us. So, about 50/50. Fantastic. So, what I'm going to do is explain a little bit about what the lethal trifecta is and what we've learned here at Coda and addressing it. So, I'm going to start off by

**[1:02](https://www.youtube.com/watch?v=abw_m-DRi1k&t=62s)** removing these Grenada notes from the presenter view. Sorry. Want to start off just uh on a quick recap of agentic AI in 2025. 2025 was undoubtedly the year of the AI agent. Everybody had a new agentic tool, Microsoft Salesforce AWS, uh, Claude Code basically changed the game when it when it came out last March. Everybody was using this stuff. And I have a a quick story. So, Vibe coding was was a really big thing. Um, Jason uh had this Twitter post about how agentic coding changed his life. He's

**[1:51](https://www.youtube.com/watch?v=abw_m-DRi1k&t=111s)** pushing out all of this code, making all of these new changes to his product. This was the future for him. And then, I think less than 24 hours later an agent or 2 days later, he posts on Twitter again and says, "Agentic AI just destroyed my product, deleted my production database. And how can anyone ever use Agentic AI?" Um the thing is a AI agents are very powerful, but they create problems. Um everyone here familiar with Open Claw? Right? So, what's the deal with Open Claw, right? It's a really, really cool tool. You can put your own AI on a computer, and it can essentially be your

**[2:39](https://www.youtube.com/watch?v=abw_m-DRi1k&t=159s)** personal assistant, do all of this really, really awesome stuff for you. But you've probably seen everyone is saying, "If you're going to use Open Claw, you need to buy a Mac Mini and put it on a different computer than your personal computer, right?" Because it's got all these security vulnerabilities. The last thing you want is Open Claw to go download all of your sensitive files, put it up on the internet, download viruses on the internet, put that on your laptop, and then delete all your personal files so that you don't have them, but the rest of the world does. So, there are quite a few issues with agents that we are still wrapping our heads around and how to securely develop with with AI agents. So, today I'm going to spend a little bit of time talking about the lethal trifecta, if you haven't heard of it,

**[3:27](https://www.youtube.com/watch?v=abw_m-DRi1k&t=207s)** and how Coder is addressing uh the principles of Agentic security, and how folks are coming to us so that they can address these problems and scale out AI at their company. So, a little bit about Coder. Coder was founded in 2017. Um it was founded by three teenagers who were making Minecraft mods, and they They tired of having to configure VMs constantly to run Minecraft so that they could develop mods on it. Somehow they stumbled on an $80 million company. Um we're very proud of them. What Coded does is it delivers consistent, reliable, and secure remote development environments. Those environments can be stood up pretty much anywhere you want. They're configured with Terraform. We're

**[4:14](https://www.youtube.com/watch?v=abw_m-DRi1k&t=254s)** open source. We're model agnostic. We're cloud agnostic. Uh you can host this on premise and we find that um this is a really, really good solution if you need a self-hosted model for developer environments or agentic environments. We're trusted by some of the biggest companies here in the United States and across Europe. Uh here's some of the names on our board. We're in I believe six of the top 10 big banks, lots of hedge funds, lots of three-letter government agencies. Essentially, if a SaaS model doesn't work for you, if you've got on-prem infrastructure, if you cannot have code sitting on a developer's laptop or in some kind of uh uh perimeter that you cannot control,

**[5:06](https://www.youtube.com/watch?v=abw_m-DRi1k&t=306s)** Coded is usually a good solution uh just like these companies need it. So, what is the lethal trifecta? The lethal trifecta was a term coined by Simon Ellison and it's a essentially three layers, three threat layers to the attack surface. One is if you have your agent on a laptop, that could be clawed code, open claw, codex, right? Well, that laptop has access to private data. That can be personal information as files on your computer, credentials, company IP, databases. So, now your laptop has access to it. Your agent now has access to this private data.

**[5:52](https://www.youtube.com/watch?v=abw_m-DRi1k&t=352s)** Now that it has access to this private data, it can also ex- uh communicate to the internet. Right? So, it has access to private data and it can put that data on the internet. And not only can it put that data on the internet, it can also download things off the internet. So, this is a problem because you don't have oversight into what exactly that agent might do when you prompt it. So, one of these three isn't really a big problem. But, two out of three is completely unacceptable in any kind of secure enterprise environment. Having all three is basically not acceptable. It's not if, it's when you're going to have some kind of security incident by having an agent on that laptop.

**[6:42](https://www.youtube.com/watch?v=abw_m-DRi1k&t=402s)** And so, here I've got a a couple of attack scenarios. I'm sure everyone here has heard of prompt injection, which is essentially um you have some kind of malicious guidance in the information source that an agent would trust. So, it might be looking at error messages, it might be looking at support tickets, it might be looking at CICD logs. And it's very easy for a malicious actor to put something in any of those messages and the agent just accepts that as a source of truth and can do something that you didn't expect it to do. Context poisoning is in that same realm where you're essentially putting bad information into documentation, into data, anywhere where you're going to your agent is going to grab information. And then, if there's any malicious data

**[7:29](https://www.youtube.com/watch?v=abw_m-DRi1k&t=449s)** in there, the agent is going to go ahead and run with it and do whatever it wants. And then, there's privilege escalation, right? So, everyone's familiar with the privilege the the least privilege access principle, right? And generally, we're giving agents access to pretty much everything because it needs access to do the work, right? And so, any one of these prompt injections or context poisoning can unwittingly escalate the privilege of that agent so it can do things that it shouldn't do, drop a table, upload, make requests, or post things that it shouldn't be able to do. So, how do we address that? Um there are three pillars of the lethal trifecta. There are three pillars of the of agentic security. We call it the

**[8:16](https://www.youtube.com/watch?v=abw_m-DRi1k&t=496s)** trifecta of agent security. The first thing is you want to control data access. If you're going to use an agent, you don't want it on your laptop, you want it in an environment that is secure, preferably a virtual environment, right? That's going to block private file access, is going to prevent destructive actions on your machine because it's on some other machine. Then, you restrict that external communication. So, if you're going to put that agent on some kind of box, a VM, it's going to now be uh isolated architecturally from your network. It's only going to be able to go to domains that you want it to go to. It's going to be on your VPN, your VPC, it's going to go through a firewall, and then anything that that agent is doing on that box, that traffic is going to be

**[9:05](https://www.youtube.com/watch?v=abw_m-DRi1k&t=545s)** governed. You're going to be able to see every little thing that it does, and if it ever breaches that perimeter, you should have some way of alerting your admins, alerting yourself that your agent is going somewhere it shouldn't so that you can effectively kill that VM, kill that agent. And then, you want to lock down uh the content and the contact and the access. So, you want to lock down the permissions, you want to restrict what access it has to, you want tightly scoped credentials credentials. The thing about agentic security is it's really no different from sound security practices for anyone, right? And we think that because AI is so powerful, we can just give it whatever it needs and it's not going to make the same kind of mistakes, not going to it's not exploitable by other vulnerabilities

**[9:53](https://www.youtube.com/watch?v=abw_m-DRi1k&t=593s)** that a human would be. So, we want to make sure to separate that machine, secure that environment, intercept any kind of uh communication that that agent might do to the uh to the wider internet. So, I'm going to kind of quickly go over what it looks like uh deploying agents at scale at really, really large companies. What are the blockers to adoption? Why companies don't want to do this? Uh what are the challenges if you do uh decide to roll out agentic AI at a company? And the questions you can expect if you're trying to lead an initiative to get uh AI at your company. So, some challenges to expect, right? Before adoption, um you pretty much need security

**[10:40](https://www.youtube.com/watch?v=abw_m-DRi1k&t=640s)** approval from CISOs. You need buy-in from DevOps because they're the ones that have to roll this out to teams. You're going to need real-world examples of, "Hey, this is why I need it. This is the workflow I want to do." And the trick here is if you're not getting these approvals, if you're at a company right now and they are not letting you use agents, most people are going to use their personal cloud subscriptions, their personal uh ChatGPT subscriptions, put that on the laptop because they do get tangible benefits from using AI. They're just not being authorized by the company. They're going to get that stuff done anyway. We call that shadow AI. Just like shadow IT, when you're bringing your own VMs, you're bringing your own uh technology into your company to get the work done. Shadow AI is just

**[11:28](https://www.youtube.com/watch?v=abw_m-DRi1k&t=688s)** unauthorized usage of AI on your laptops. Um it's a real problem because once you get AI on your laptop, you're using your personal subscription, the enterprise doesn't know what's happening, and usually uh agentic AI can do a lot of damage really fast. We're starting to see a new term in the industry called ninja AI, which is shadow AI at scale, where you're not just having one agent breaking stuff, you've got multitudes of agents doing lots of things at an organization that no one knows until it's too late that a whole lot of stuff has gotten broken. So, um if you were going to adopt AI at your company, you need to make sure that there are good outcomes, right? Usually, companies come to us, they start with

**[12:18](https://www.youtube.com/watch?v=abw_m-DRi1k&t=738s)** the developers because they're getting the most use out of using AI, but you want to be adaptable. You need to be rethinking your architecture. You need to be rethinking how you're going to protect your organization from incidents like agents dropping databases, uh deleting personal information, uploading customer information, essentially uh extracting your company's IP onto the public internet. So, once you start wanting to bring AI, you're going to definitely need to be talking to the security people. What are they What is the CISO uh concerned about? How do I stop agents from violating best practices? How do I put boundaries around these agents, right? I I I personally talk to to CISOs probably once or twice a week, and

**[13:07](https://www.youtube.com/watch?v=abw_m-DRi1k&t=787s)** they're saying, "Hey, we understand the value of AI. We want to bring AI. We want people to go as fast as they can on the the development AI superhighway, but I need guardrails for them, right? And I can't just have my platform team or this business team come to me and say, 'Hey, we need AI. I need you to bless it because if anything goes wrong, it's not anyone's fault but the chief security team's problem, right?" And they don't want the finger being pointed at them because someone used Agentic AI and they didn't know what they were doing or they didn't have the proper guardrails for Agentic usage at the company. Uh platform admins, DevOps, infrastructure, security engineering, they're worried about observability.

**[13:56](https://www.youtube.com/watch?v=abw_m-DRi1k&t=836s)** What are these agents doing? How do I know it's doing? How do I get every call that they make to an LLM provider in some kind of observability tool? And how can I then set up some kind of alerting for that without also getting alert fatigue? So, another thing that's happening is maybe we do get some kind of observability around AI, but now there's alerts going all over the place. Once you get alert fatigue, you stop really looking at what's actually happening. Everything AI is doing just becomes noise and you're missing the really, really critical things that actually need to be addressed. And then another thing is if I am going to roll out AI, how do I actually set this up in a repeatable, consistent, reliable, secure way for everyone at the company? Lastly, developers are going to have

**[14:45](https://www.youtube.com/watch?v=abw_m-DRi1k&t=885s)** concerns as well. There is still a holy war happening where some of the most technical people are not quite converted that AI can do code better than them, right? They're worried about more technical debt, more code bloat, more security vulnerabilities, and spending most of their time fixing AI slop versus just doing it themselves. And then if they are going to put Claude on YOLO mode and have it crank out a bunch of PRs, how do I make sure that that agent isn't doing stuff that would actually get me in trouble, right? Because at the end of the day, someone is going to be accountable when an agent actually does something that we didn't expect it to do. So, I'm going to talk a little bit about how you can address all of these guardrails that everyone is concerned

**[15:33](https://www.youtube.com/watch?v=abw_m-DRi1k&t=933s)** for. Uh the first thing is cloud development environments, and this is something that Coder does, right? You want a remote execution layer. You want a remote environment. You don't want it on your laptop. You want to go to a URL. You want to RDP. You want to SSH into something that is not your laptop, but something that is in a secure environment that has been blessed by the security team, by the platform team, and let agents write code, execute code on cloud infrastructure that um is isolated, that has right-scoped permissions, and cannot communicate to anything unless you allow it to communicate to that um to that public internet. So, this is kind of what it would look like, right? Instead of putting things

**[16:21](https://www.youtube.com/watch?v=abw_m-DRi1k&t=981s)** on your local machine, you go to an isolated cloud environment. Right now, it can only do You can only work on the code that's in there. It can only touch credentials that are in there. It can only touch data that you purposely put into that development environment. Right? Um CDEs accelerate AI productivity because the thing is if you grab a a project and you put it on your laptop, what do you have to do to get that project running? You got to download dependencies. You got to update your your path. If your computer's running Python version 3, but this project needs Python version 2, you're going to get conflicts. You have to create virtual environments. You have to do a lot of extra stuff that

**[17:10](https://www.youtube.com/watch?v=abw_m-DRi1k&t=1030s)** while it may not break your laptop, you really don't want to go through the trouble of doing that. It would be better if you had a consistent cloud environment that was already configured to run that application, right? And so, everything that Coder does uh that helps developers, they don't have to worry about mucking around the shell, mucking around their precious laptop. They can just go to this lightweight or heavy VM, and everything's already ready to go, and they can just start developing. Well, that same thing is true for agents, right? If you put an agent on a fresh box and say, "Download this GitHub repo and run the project." What is it going to do? It's going to read the contents. It's going to say, "Oh, I need to start downloading stuff." You never know where it's going to download things from, and if it grabs things from some kind of registry, that registry could be contaminated. You really want things to already be ready so that the agent could

**[18:00](https://www.youtube.com/watch?v=abw_m-DRi1k&t=1080s)** just start developing. Um the next thing is a model proxy. And this is really just something in between that uh agent or that model on your machine before it hits the LLM provider, it needs to go through a box where we're sniffing all of that traffic, and we're able to log every little thing that it's doing, right? So, here you can see normally in in a in a normal scenario, the agent would be sitting somewhere, and it can just go straight to the internet, straight to the model provider, and get what it needs. But the solution is really simple, right? Before the agent hits the model provider, it goes to your proxy server, it goes through your gateway, right? And it can sanitize, it can strip injections. If

**[18:48](https://www.youtube.com/watch?v=abw_m-DRi1k&t=1128s)** you have like if you accidentally put credit card data into a prompt, you don't want that going to the LLM provider. Uh model proxy can strip that, and it logs everything that's happening. Lastly, you want an agent firewall. So, when that agent starts executing at the process level, you want to make sure that uh it can't run commands that you haven't already blessed, right? So, on that remote environment that goes to the proxy, if it runs if that agent for whatever reasons runs gh repo delete or drop this table, you want some kind of agentic firewall that's looking at the process logs and saying, "Do not run this." That that command is denied. And so, these

**[19:37](https://www.youtube.com/watch?v=abw_m-DRi1k&t=1177s)** are the three ways architecturally you can protect your organization from an agent going crazy. So, don't have time to run a demo right now, but if you're interested, please come over to our Curder booth. We're opposite and to the We're opposite of this stage and over to the left. Um And just some key takeaways, right? Agents are powerful, but be aware of that lethal trifecta. Make sure that you've got some way of seeing everything that that agent is does. It's okay to go slow so that you can think about your architecture, know what your infrastructure actually needs. My name is Michael Patterson, staff solutions engineer. Would love to talk to you guys about how you can securely develop with agents.

**[20:24](https://www.youtube.com/watch?v=abw_m-DRi1k&t=1224s)** Thank you for your time.
