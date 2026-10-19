---
id: nSkmXakJ6eo
title: "Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS"
slug: auth-for-agents-let-ai-sign-up-for-your-product-with-auth
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Michael Grinich"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-12T05:37:09Z
video_id: nSkmXakJ6eo
url: https://www.youtube.com/watch?v=nSkmXakJ6eo
youtube_url: https://www.youtube.com/watch?v=nSkmXakJ6eo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS

**Michael Grinich**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=nSkmXakJ6eo) · [Conference site](https://www.ai.engineer/)

## Description

Agents are starting to pick your vendors, and most signup flows block them at the door.

NEXT UP: AI ENGINEER CODE SUMMIT
Join us in SF for the second annual AIE CODE Summit, Nov 10–12, our last flagship summit of 2026. Applications live now: https://aie.codes

Michael Grinich, founder and CEO of WorkOS, argues that as agents run for hours and increasingly choose tools on their own, services have to make something agents want. The missing piece is agent registration: today's signup flows assume a human who can fill out forms, solve CAPTCHAs and copy API keys, and MCP auth still needs a person in the loop. He introduces auth.md, an open spec built on OAuth standards that tells agents how to register, then demos an agent that finds Cloudflare's auth.md, proves its identity with ID-JAG, gets a temporary account and deploys an app with no human signup.

In this video:
• Why login boxes and CAPTCHAs block legitimate agents
• What an auth.md file declares for agent signup
• Live demo: an agent registers with Cloudflare and deploys
• Why payment should come after usage, not at signup

SPEAKER
Michael Grinich, Founder & CEO, WorkOS
X: https://x.com/grinich

LINKS
auth.md: https://workos.com/auth-md
auth.md spec (GitHub): https://github.com/workos/auth.md
WorkOS: https://workos.com

CHAPTERS
0:00 Intro
0:32 From human-in-the-loop to autonomous coding
2:22 Lessons from autonomous vehicles
3:27 What agents need to succeed
4:27 Models as engines, harnesses as cars
5:27 Agents are choosing vendors
6:17 Make something agents want
6:52 Missing primitive: agent registration
7:32 Why signup flows block agents
9:12 What agent-native registration needs
10:26 Why MCP is not enough
11:06 Introducing auth.md
12:16 What an auth.md file describes
13:01 Demo: agent signs up for Cloudflare
15:56 Registration flow and ID-JAG
17:01 Benefits for builders and providers
18:46 Salesforce goes headless
19:26 Open spec on GitHub
19:51 Closing

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*4,096 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=12s)** Hello everyone. Good morning. My name is Michael Greenwich. I am the founder of work OS and I'm here to talk with you today about agents and specifically about how we can make agents more autonomous and allow them to access more services on the web. So let's jump in and get started. Shout out to those of you in the front row also. I see you out here. So about a year ago, software engineers were writing code like this. We were using AI, but we would prompt it and then we would write a little bit of code and then prompt it again and it would write some more code. And you would continue to do this human in the loop interactive software engineering. Later in the year, we had things like Ralph loops, if any of you remember those, where we kind of automated this. More or less this is the way that we were

**[0:58](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=58s)** working. It was this human agent human agent back and forth. However, as the models got better and better, they were able to write more and more code and run for longer periods of time. And so today, a lot of software engineering looks like this. You write a single prompt and then the agent can spit out a lot of code. And sometimes it can actually build a whole feature, maybe even a whole product and maybe run for not minutes but uh hours and hours or even days and days. This has really transformed the way that we all write code. I don't write code by hand anymore. Probably you don't as well. And it's not just this one thread. You can actually parallelize this. So there's many different tools out there including, you know, the major code coding harnesses from the labs that allow you to run many of these in parallel. The limiting factor here, really the bottleneck is your brain. How much

**[1:47](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=107s)** context do you can keep in your mind to keep all of these going at once? And this has transformed software engineering. People can be more productive. I think we've all seen in the industry how much faster things are moving. At the root of all of this is actually agentic engineering agents going from these token prediction language models to reasoning and now longunning processes that can actually do things autonomously for us. And what I think we've seen in software engineering here around agentic workflows is going to come to a lot of different categories. It won't just be engineers that have this way of working. It'll be people in many different fields. Agents are the next big thing. I think a good reference for this, a way to think about it is actually what's been happening with vehicles. So, you know, this looks like a pretty modern car. It has a, you know, digital display

**[2:35](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=155s)** on it. This is probably what you would have bought in the last, you know, 5 to 10 years. But if you live in San Francisco or one of the cities with these autonomous vehicles, you've probably seen that we're starting to delete the interface. No longer do you get inside of the car and actually, you know, pull up your phone and get maps where you as a human are in the loop. There might be cruise control, but you're still in the loop. Instead, these are autonomous systems. You just say where you want to go, you get in the car, you don't even say anything, and it just takes off and takes you to your destination. I remember the first time I got into a Whimo, I was blown away, mind totally blown. And then after about 3 seconds, I pulled out my phone and started scrolling X. It became common place. And I think we've seen this already happen with engineering. The power of agents allows us actually to work and think at a higher level for us to, you know, exercise more of our executive function

**[3:24](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=204s)** versus just planning and execution. There's a question here of what do agents need to be successful? Actually, when they execute, what do they need? Well, first they need a runtime, a sandbox. They need somewhere that they can run that needs to be safe, secure, performant. They also need tools. They have to be able to go do stuff in the world. An agent's not very useful if it can't take actions. So, it needs tools. Third, it needs context. You know, these new models with the power of the intelligence in them, it's kind of like taking the smartest person you know and dropping them into a company or a project or a team where they don't know anything, they can't really get anything done. They need to have context, information about the system, information about the goals. They need feedback. So a way that they can actually run and validate that they can check that their work is correct and if

**[4:11](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=251s)** it's not correct keep going. And last but not least of course they still need human review. This might be code re review. This might be other forms of evals. This might be forms of checking their work to make sure that these agents are sort of aligned with your goals. The LLM the intelligence engine this new technology we've created in the last last few years you can think of as like an engine. It's like a really high performance. You know, I think this is a a V8 engine. You know, puts out a lot of horsepower. It can convert fuel into, you know, output. But an engine by itself isn't very useful for a car. You need to drop this into the actual car itself. You need the chassis, you need the transmission, you need the drivetrain, you need the wheels. And only with all of that is it going to be effective to take you places. And this

**[4:59](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=299s)** is what a lot of people refer to as the harness. Harness engineering is this new domain where if the models get better but you don't have a good harness you know it's not going to be very effective so as the models improve we change our harnesses we adapt them to it and those things that I mentioned earlier are sort of a form of a harness so agents execute within these harnesses to get stuff done and they they need all those elements to actually be effective and when they drive they drive really really fast so say you have one of these agents that's going off you prompt it to go build something for So, you know, it spins for a while. It says, "Okay, I'm going to need this feature and this feature and I'm going to need a database and I'm going to need, you know, this editing uh, you know, system to deploy and I'm going to need, you know, maybe this thing for image resizing or video transcoding or sending email or whatever." And your agent can actually

**[5:45](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=345s)** go do all this research and build all these systems. And today, what's happening with agents is they're actually selecting vendors. You've probably seen the rise of some of these systems where you know like the CEOs will tweet about their growth graph and it really takes off and it's because agents are picking them. They're picking their systems for sending email or deploying code. Their systems for storing data today actually it might be more important to build for agents than to build for people. Agents are kind of this new consumer class. I'll talk about that in a bit. There's this uh kind of popular thing that people say in San Francisco Silicon Valley. Make something people want. This comes from Y Cominator, you know, the startup factory from Paul Graham. And I think it's time to maybe edit this a little bit. And going forward, we also need to think about making something

**[6:32](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=392s)** that agents want. There will be more agents in the future than people, maybe even today. They'll be faster to spin up. They'll do things quicker. They'll be making decisions on our behalfs. And so, if you want to build for the next era of consumers, you should be building for agents as well as people. But there's a problem today. You can access the web. You can access mobile. But agents themselves can't really access systems. Your business probably isn't open for agents today. Even though there's a lot of them out there, they can spawn very quickly. The door is not open. And we think this is because there's a missing primitive. Agentic registration, agent registration. There's a lot of great stuff around agents connecting and bringing context to systems and

**[7:19](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=439s)** different open source frameworks, but that first step of an agent actually signing up for a service is actually missing. It hasn't been solved and it's a huge blocker to getting adoption. For the last like 20 years, maybe 30 years, automated traffic on the web has been bad. We've tried to block all of it. And so there's all these systems that we've put in place to detect automated actors and stop them in their tracks. DOS prevention, credential stuffing, and attacks. The login box, for example, is very hardened against agentic registration today. Not intentionally, but just because of the legacy systems of what we built. And it's very hard to distinguish between what's a good automated user versus a bad automated user. If any of you have

**[8:08](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=488s)** used any of these like cloud-based uh browser execution environments, one of the selling features they often have is to break captures, which is pretty wild. You know, we're trying to go backwards. The capture today though is is still kind of dead. There's rampant abuse. There's lots of token fraud. And so, we need to find a better way to allow the good agents in and then block the bad agents, right? Because like I said earlier, if you don't build for the agent economy, your product might not win. It might not be successful. Today's signup flows assume that a human can read the landing page, that they can fill out a form, you know, put their email address, their password in it, that they can solve a capture, that they can verify their email, not just put it in, but go click something somewhere. Remember, an agent probably doesn't have an email address. If it's signing up for a service, it

**[8:56](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=536s)** needs to have a, you know, a human can choose a plan to pay for it. You know, human can copy the API key out, paste it somewhere, use it somewhere else, and really even a dashboard. Think of a dashboard experience. It's not really agent native. All this stuff is built for people. It's kind of a human interface, not an agent interface. Agents need something else. They need native discoverability. Can they register for a system? Are the doors open for agents or not? Capability declaration. What can it do? Registration intent. Why are you registering? What are you trying to do within this? Or the intent to actually just sign up. There's a lot of stuff around risk here. So for an agent native registration, maybe you want to you're not sure if the agent signing up is going to be good or bad. So you need to actually do a risk assessment of that. There might be different forms of

**[9:43](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=583s)** identity verification for an agent. If something like claude is going and signing up, maybe it can bring the user's identity with it or if you have a you know open claw or like your pi harness or something else, maybe it doesn't bring the user's identity and gets verified out of band. There's the whole thing around organizations doing this. So if I'm building something within a company, how does my company identity come in? You know, my organization, entitlements permissions credential issuance, auditability, the list goes on. There's so many things that need to be changed. In fact, probably most things need to be changed going from, you know, human registration to agent registration, agent native systems. I'm sorry to say MCP is not enough. Probably more than anybody, I'm a big

**[10:31](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=631s)** MCP fan. We've done a bunch of events in San Francisco around MCP. I see somebody wearing one of our run MCP shirts up here that we made. Love MCP. MCP is great for connecting, for providing tools, skills, context, but it doesn't solve the registration step. Today, authentication through MCP requires your human to still be in the loop. You give consent. You add an MCP server, say for Post Hog to Claude, you sign in with your Post Hog credentials. What we're talking about here for agent native registration needs to happen without the human involved or at least not involved initially. So we've been working on this for a while and our proposal. This is a new spec we have called o.md because markdown files are the future right? Well, how does this actually work? What

**[11:19](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=679s)** is o.md? Well, the idea here is that OMD tells agents how they can become legitimate users. It's a set of instructions that tells an agent registering for a service, this is what you need to do to sign up and be considered legit and for me to give you access. And the goal here is to give these service providers, you know, people that are building building services an agent native signup experience, but it's built on existing standards instead of inventing a crazy new religion or something really complicated. With OMD, we're not solving the whole problem around agent identity, you know, permissions, long duration, you know, connective services. We're just trying to solve this narrow one around registration because I think it's a huge blocker. Let's start small and grow from there. This is built on open

**[12:08](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=728s)** standards. It's built on a bunch of work that's already been done across the OS specifically tailored to that registration step. often do you can answer what does the service do tell agents how to register it can tell them what identity proofs are accepted how to how how an agent or user is proving their identity what offflows are supported can you sign up with SSO or email address or MFA what scopes and entitlements can exist kind of what capabilities are here what free tier constraints apply you might have a system where you want to give an agent a little bit of free capacity but not too much until they verify or pay in some Okay. And then of course, how does the human get involved later? A human or an organization claiming it afterwards. So an agent can sign up, but you want the

**[12:56](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=776s)** human to have custody later on. This is what A&D is designed to solve. These are the main questions around the registration step. So how does this actually work? Well, here's a little uh kind of cartoon demo that I'll show you. And all this works, by the way, you can go try it after this. So say I'm here in u whatever coding harness or system I'm using pi or clot or something and it says welcome back Michael at work OS that's actually my email if you want to email me do you want to keep working on your spelled app like yeah sure I'd like to share this with my friends but they can't access it and the agent's like oh well local host only works on your machine so your friends won't be able to hit it of course to share it I need to deploy it somewhere real some providers actually let me handle the sign up so you know you wouldn't have to sign up and do this you want me to look

**[13:45](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=825s)** Yes please agent look for services that advertise through author here does have an OMD and so the agent here can say ah Cloudflare that's the one cloudflare is a winner because I can go sign up for it I can access the service I can actually use it so I can do the whole thing you want to go with it yeah Let's do it. This is the registration step. This is kind of where the magic happens. What my agent is actually doing is minting an identity assertion and giving that to Cloudflare. And then Cloudflare is able to verify that or not. Cloudflare can choose actually to verify out of band. AMD is very flexible. There's different ways you can dial it

**[14:32](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=872s)** in depending on the behavior that you're looking for. One size does not fit all. Every application is different. Constraints are totally different. If you're building something that's like a database service where there's going to be very little amount of information, you might want to give away a little bit of traffic for free. But if you're building something maybe like an email service or something certainly if you access the physical world, you you maybe don't want to give anything away for free. It's very application specific. So here Cloudflare says, "Okay, we're willing to let you deploy maybe for 72 hours or something like that. Get the identity assertion. Boom, boom, boom. Go through. It's called ID Jag is what the standard is." And then it returns back and says you're set up with a Cloudflare account. Now in this experience, my you know human I didn't go click anywhere. I didn't sign up anywhere. It just it just got the token. I can make a couple small tweaks. It knows how to use Wrangler.

**[15:20](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=920s)** Want me to make those changes? Go ahead. Does anybody prompt their agents like this? It's just like yes, yes, do it, please. Not really saying much. It's able to write the Wrangler, get the thing set up, go through the full deployment process, and then boom, it's live. We actually have this working as a live demo. We did some collaboration with Cloudflare on this too. It's pretty cool. And you can tell the prompting that I was giving through this not exactly rocket science. The agent could just run through the whole thing. Actually, there's nothing actually that I was doing through prompting it other than just approving, approving, approving. It should be able to do this one shot. This is what it looks like graphically. So agent registration with OMD, you have your agent harness pi for example. within that is your LLM, maybe your memory, different, you know, context

**[16:08](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=968s)** layers. It connects to your backing identity service. So this is the user identity. And when that agent goes and registers, it sends the discovery call to Cloudflare. It looks for that aund or whatever service. We also have this working with fire call. It's pretty cool. It sends that ID Jag, the identity JSON access grant. It's essentially a signed credential that represents the user says this is an identity receives back the access token actual API token and then boom it's it's done you can make normal API requests you can call MCP everything else still works so you can see that OMD is just for the registration step your normal API keeps working the rest of your docs don't have to change it's just that registration step for agents but with the simplicity comes actually

**[16:56](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=1016s)** an enormous amount of power because suddenly it lets agents do things end to end. I hate the planning step. When I write something, I just want the agent to go do it. Usually it kind of knows what I'm trying to get at and I want to come back to actually a running prototype and not like, hey, here's my long plan. Here's a bunch of services to sign up for. If I'm building new prototypes, especially, I would prefer it just to get deployed on something for free so I can see it and click around and not put me through the burden of going sign up for all these different vendors. And that's what OMD allows for. And if you're a service provider, if you're building APIs or services, this allows you to become a customer of those systems and you can think about it increasing your growth funnel starting from, you know, maybe just humans and adding the whole world of agents on top. Pretty great. We think this is going to be huge. Your

**[17:46](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=1066s)** door will be open for agents to actually sign up, register, use your services. This should be an immediate growth boom for your products. And I'm not saying everything that agents are going to build will be useful. Maybe not everything they build will go into production or last that long, but some things will. Just like with PLG or Premium before that, this is the way to grow your business and get more customers and actually become, you know, larger and more successful. And where there's usage, we believe there's also intent to pay. There's a lot of interesting work being done for agents to actually pay for stuff. There's crypto-based protocols like X42. There's other things that the payment providers are building, but we think that should be downstream. We don't want payments to be upfront. We don't want to have to force your agent to sign up with a credit card. That seems backwards. We moved away from that in the world of SAS. With OMD, agents

**[18:35](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=1115s)** can sign up, they can register, they can start using it and then downstream choose to pay on your terms based on your own pricing, based on your own model. If you don't believe me or on the headless type of products, this is Mark Beni off. He's the CEO and founder of Salesforce, the guys at the big building here in town. They believe in agents more than anything. Our API is the UI. Entire Salesforce and agent force Slack platforms are now exposed as API, MCP, and CLI. Talk about going agent fork first. A company that many people consider to be sort of a legacy SAS vendor really invented the category of software as a service. They're getting rid of their dashboard and UI. I mean, they're not getting rid of it, but they believe that agents are the future. So, if you're not thinking about this, I definitely encourage you to start building some prototypes, talking to

**[19:22](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=1162s)** users, because you don't want to miss miss this. If you want to use this, this is available today. We have open spec for it. There's a GitHub repo. You can actually have your agent go implement it. I know it's kind of meta. It's an open spec. Work OS doesn't control it. We have a version of it that we host, but you can build it yourself. You can run it yourself in your existing systems. I think this is so important that no single vendor owns this. It's one click enabled if you use our stuff, but you can build it on whatever platform you want instead. Last thing I'll close with, this actually happened almost 20 years ago, I think actually here at Moscone, which is pretty awesome. in uh January of 20 uh 2007 I believe Steve Jobs introduces iPhone and I was in college and I remember or yeah like first year of college I remember this

**[20:09](https://www.youtube.com/watch?v=nSkmXakJ6eo&t=1209s)** super super clearly. It was the next great software platform that got built. So many companies got started because they could build on top of these devices. smartphone revolution and there hasn't really been a moment like this since I think in the the era of technology at least for me the stuff we did around B2B SAS and cloud and all that is great but this was a totally new paradigm a new software platform and I think agents are this agents are the next big wave and so what I would say to all of you is go out and build with AMD we're hoping to unlock this for you unlock this for your business and for your growth but we want to hear from you here the places you get stuck and I think together we can build for this next exciting era of software and build for the agentic revolution. Thank you so much
