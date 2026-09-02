---
id: lMCxVorb9wM
title: "You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit"
slug: you-didn-t-ship-a-bug-you-just-wrote-it-for-a-human-ravi
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ravi Madabhushi"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-07-19T16:00:06Z
video_id: lMCxVorb9wM
url: https://www.youtube.com/watch?v=lMCxVorb9wM
youtube_url: https://www.youtube.com/watch?v=lMCxVorb9wM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit

**Ravi Madabhushi**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lMCxVorb9wM) · [Conference site](https://www.ai.engineer/)

## Description

We built a demo agent to show customers how to connect agents to their tools. A simple chat assistant — Gmail, Calendar, a handful of connectors. It ran on a 15-minute schedule. And every 15 minutes, our production database strained. Latency crept up and alerts fired. Then settled.

Then, it fired again.

It took us a while to find it. One line - a "last seen" timestamp updating on every tool call. Written for a human who logs in once. Our agent was calling it sixty times a second. We had built infrastructure to show customers how to connect agents to their tools. We hadn't noticed we'd built it for humans.

That line wasn't a bug. It was a design assumption. And it's not just us - 60% of all production LLM errors trace back to rate limits. They are not model failures or bad prompts. Infrastructure that never anticipated this kind of traffic. As one developer put it: "Rate limits can't tell the difference between agent legitimately needs 100 calls and agent is just looping." Because they were never designed to. They were designed for humans.

Every layer of the stack your agents depend on carries the same assumption — that the user on the other end is a person, doing one thing at a time, at human speed. Your agent isn't. And until your infrastructure knows that, production will keep finding the places where it doesn't.

This talk is about what we learned from finding it, what it actually means to treat agents as a first-class principal, not a fast human, and what changes when you design for that from the start.

Speakers:
- Ravi Madabhushi (Scalekit): Ravi has been building infra for how software talks to other software for more than a decade. He co-founded Pipemonk — a SaaS integration platform acq. by Freshworks (NASDAQ listed) then spent years leading product on Freshworks' auth platform as it scaled to 50K+ businesses and 2M DAUs.

At Scalekit, he's applying that to a harder version of the same problem: not humans logging into software, but agents taking actions inside it. What breaks is different. What it costs when it breaks is worse.
X/Twitter: https://x.com/ravibits

## Transcript

*2,227 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=lMCxVorb9wM&t=0s)** Hi, thank you so much for tuning in. I'm Ravi, I'm one of the co-founders of Scale Grid. Today, I'm going to talk about how you need to think architecturally from the ground up about building your applications APIs, your MCP servers for agents, and how the human-focused architecture doesn't scale well for agents. So, a while back, we were looking at our performance and latency numbers, and one thing that kind of jumped out at us was how our latency was spiking every 15 minutes in a rhythmic manner. Nothing harmful, but just a curious thing for us to analyze. What we noticed was very interesting. So, in our identity and authentication infrastructure platform, we have this little timestamp that we mark for every user to say, "Hey, when was the user last seen?" or "When was the user last

**[0:48](https://www.youtube.com/watch?v=lMCxVorb9wM&t=48s)** active or last acted in our system?" so that we can predictively say, "Hey, this user is an active user. This user is not so active." But, one thing that we realized was this system was primarily built for humans, but when agents started hitting our APIs in the last 12 months or so, we realized that this last seen update is happening 60 times faster than what it would, and that is creating unnecessary pressure in our DB write system. So, of course, it's a harmless thing. We were able to fix it very easily. We would just batch the update at a second level and not at every single time we had to update it. That kind of took us down a rabbit hole. So, the assumption that broke was how often would our system have to update

**[1:36](https://www.youtube.com/watch?v=lMCxVorb9wM&t=96s)** this timestamp on every row, and that's okay. It's just about speed, it's about latency etc. But, what I was worried about is, "Hey, what if some of our assumptions that we made about authentication, authorization need to be rewired and rethought completely when it comes to agents because we would have designed earlier for humans as actors in mind?" Now, just to give you a context, I worked on identity and authentication operations for the last 10 years building an identity platform at Freshworks, which is being used by millions of daily users, hundreds and thousands of customers all over the world. But, this is predominantly human users, right? Or at best, APIs. But, the way I think about it is APIs are also accessed by machines that are written by humans. That's not too bad, right? But, what I

**[2:25](https://www.youtube.com/watch?v=lMCxVorb9wM&t=145s)** realized is the fundamental picture has changed drastically in the last three, four years or so. We have a unique ringside view to see how developers nowadays are building agents and how they're giving context to these agents with data from third-party applications like Salesforce or or Databricks or HubSpot or Notion. What we have realized is most of the agents our customers are building have way too permissions and scopes than the agent's responsibility or the agent's job is. Again, it's not because the developers who are building the agents are careless, but somehow this became a default pattern of giving [snorts] the agents what they need access to, and the existing primitives

**[3:13](https://www.youtube.com/watch?v=lMCxVorb9wM&t=193s)** that we have don't let us give extremely fine-grained permissions to the agents. Now, I'll tell you how we ended up here, right? We predominantly have two slots, and neither of the slots was built for agents in mind. There's a human who's acting the application, either a web application or a mobile application, or their own little script that they wrote, and they give it their API key so that their program can access data from the application. This is all the fundamental principle here is it's the same user who is authenticating, and it's the same user who's acting, right? And the second slot is the traditional service account scenario or end-to-end account scenario where you create a service account, you give it certain permissions, and then say this machine has its own identity. That's where the likes of SPIFFE and and

**[4:01](https://www.youtube.com/watch?v=lMCxVorb9wM&t=241s)** OAuth and all of that came into picture, but you would give them certain credentials and say, "Hey, now this machine has access to whatever data that it needs at any single point of time." And this is the existing pattern, right? So, the fundamental philosophy that we've always maintained is whoever is authenticating is the one that is acting. Every action the program or the human takes is based on fixed set of permissions that actor was granted at some time. If you take traditional authentication mechanisms for humans, including password, you just say, "Hey, if an identity has the same password that it was set at the time of registration, if they come back and if they present the same password again, then you say, "Okay, this is how I validate the identity. This is how I authenticate the human." And every action subsequently is tied to that

**[4:50](https://www.youtube.com/watch?v=lMCxVorb9wM&t=290s)** human identity. Again, the same is the case with API key or the same is the case with web session tokens or even the same case for service account. You define the permissions at the time of registration, and then every single time it acts based on the registration time permissions and scopes. Now, this is okay all this while because for decades the service account and OAuth principle even is working fine even though there are their own problems, but it's still working fine because these machines are using a program in a deterministic way by the way the human developer wrote that program. So, there is absolute guarantees about what the program could or what the program won't

**[5:39](https://www.youtube.com/watch?v=lMCxVorb9wM&t=339s)** do, but it is still intentional based on what the human wrote, right? In this particular case, again, if it is using API keys, then that actor and the principal is the same, then there is some sort of a delegated permission for the program to act based on what consent the user has granted. But, the second one is the most important part, which is it's a deterministic program, and it always stays in its own lane. It can never do what it was not programmed to do. And you could inspect the code to say, "Okay, is the program doing what it's supposed to do?" Even if you apply for a Google developer account, and then ask for client ID, and you need to access these scopes, you have to go through a security review. So, what they're doing is they're looking at your code base to see, "Are you doing enough checks? The appropriate practices in place?" So, these programs are deterministic. These programs behave

**[6:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=388s)** the exact same way a developer programmed them to work. But, agents fundamentally break this assumption. Right? First of all, in the case of agents, the principal is not the same as an actor. You need to give delegated access, so that the agent can act on behalf of the user. Agent can access the user's Gmail. Agent can access the user's Salesforce data, and whatever the case may be. But, again, unfortunately, not a lot of systems, even today, support OAuth. So, here again, there is no on behalf of principal that is working. So, you don't even know if there is a program that is acting on behalf of the user, or the user acting by themselves. Right? That's a fundamental problem. The second problem is even more dangerous, which is right now, the program is not written by

**[7:15](https://www.youtube.com/watch?v=lMCxVorb9wM&t=435s)** human. There is no determinism baked in to say what the agent will do or won't do. Right? Just because an agent does certain things today, you can't be 100% certain that the agent can't do the same or the exact same thing tomorrow, day after, or even if it's the next immediate run. Right? Because of this non-deterministic nature of agent, we usually pick one of the two lanes, right? You give a specific identity to the agent, which is what we call as client ID in the context of OAuth, and then say, you act on behalf of this particular user, or we go back to the agent acts as the user, which is even worse. The fundamental reason why I'm harping on the same thing is because when an agent is acting on behalf of

**[8:04](https://www.youtube.com/watch?v=lMCxVorb9wM&t=484s)** user one versus user two or user three, the agent needs specific permissions based on the user's context. Now, the OAuth solved this perfectly fine by saying, hey, the user will grant specific scopes or permissions to the agent. So, when the agent is acting on behalf of the user, it can't do everything but the agent will only do certain things. Now, in the kind of the world that we're living in, most of the MCP servers that we've worked with don't actually limit the tool context access to the agent based on which user authorized the agent. They typically surface all the tools that the user has access to, or all the tools that the application can even support,

**[8:52](https://www.youtube.com/watch?v=lMCxVorb9wM&t=532s)** and then let the agent determine what they are can or cannot do. And now the agent ends up picking the wrong tool, doing wrong things. Maybe there is some runtime check in the application that prevents some of these things, but the agent is still seeing the same surface regardless whom it is acting for. Now, two things that we need to solve for. One is the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity. Agent should have extremely fine-grained credentials, not the OAuth scopes that we are seeing today. If you inspect the scopes for some of these applications, like even very popular applications like Gmail, it'll say, can this client send emails on your behalf? There's no extremely fine-grained scoping to say can this agent act at this hour? Can

**[9:41](https://www.youtube.com/watch?v=lMCxVorb9wM&t=581s)** this agent read emails only from these senders? Can this agent send emails to only this recipients? The reason why that is important is because again, we spoke about this earlier in the context of non-deterministic agent workflows, it's extremely important that the agent should have permissions for limited amount of time that they're operating in number one. Every agent has a goal, every agent has a job. So, you should be able to deterministically say that this agent should have access only to those tools or only to those jobs it has access to. So, gone are the days when the broad scoped auth scopes that we defined is okay because in that case developer was writing a deterministic application and you can review the code to make sure that he's not doing

**[10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s)** anything sinister. But in the case of agents is extremely non-deterministic, it is probabilistic. Agents are bound to do things whatever they can get a hold of. So, in the context of when you're giving access to the agents, you should be in a position to give extremely fine-grained scopes. It should be at an attribute level scoping, it should be context level scoping, it should be principal level scoping. So, all of that is extremely important. Again, I think everyone agrees that agents should be least privileged by default and they should be able to ask for just-in-time authorization if they want elevated scopes. Now, the reason why we're talking about this is because it's not some futuristic thing. It is happening today. We have seen enough incidents where agents end up doing rogue things. They end up deleting production databases and stuff like that. So, how

**[11:16](https://www.youtube.com/watch?v=lMCxVorb9wM&t=676s)** do you put deterministic guardrails in place is an important problem to be solved right now. Again, one of our customers, ref.tools, they don't even have humans as actors. Their predominant product is about how to give context to coding agents so that they can do their job effectively. So, they built the entire OAuth scoping. How do you do things the right way and things like that. So, the reason why I give this example is not to say that this is a warning shot, but this is a problem of today and not for tomorrow. Before I go, you have to have absolute visibility into what your agent can do, every action that's taken in your system, who took it, on behalf of whom, and who authorized it, when was the authorization given, what authorization was given, how long is it given for.

**[12:03](https://www.youtube.com/watch?v=lMCxVorb9wM&t=723s)** If you don't have visibility into all these actions at every single time, and if you can't deterministically control what your agent can or cannot do, then you're just praying that agent doesn't end up doing what it's not supposed to do. And praying is not a strategy, as we all know. One last thing to take away. If you architected so far with humans and APIs in mind, you need to start rethinking about how you need to give deterministic guardrails and deterministic authorization controls to the agent. And OAuth is a good place to start, but you need something beyond OAuth to make sure that the agents have extremely fine-grained access controls, and agents are always acting by themselves on behalf of certain users. Thank you so much for your time.
