---
id: adfw3xJBx1o
title: "A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo"
slug: a-bank-built-its-own-coding-agent-it-took-off-felippe
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Felippe Felisola Caso", "Francesco Galletta"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-20T19:00:34Z
video_id: adfw3xJBx1o
url: https://www.youtube.com/watch?v=adfw3xJBx1o
youtube_url: https://www.youtube.com/watch?v=adfw3xJBx1o
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Monzo", "Felipe Felisola Caso", "Francesco Galletta", "AI coding agents", "in-house agents", "MCP", "MCP gateway", "agent orchestration", "sandboxing", "Slack bot", "platform engineering", "fintech", "banking AI", "AIE NYC"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Science, healthcare & applied ML"]
transcript: true
---

# A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo

**Felippe Felisola Caso, Francesco Galletta**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Monzo` `#Felipe Felisola Caso` `#Francesco Galletta` `#AI coding agents` `#in-house agents` `#MCP` `#MCP gateway` `#agent orchestration` `#sandboxing` `#Slack bot` `#platform engineering` `#fintech` `#banking AI` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=adfw3xJBx1o) · [Conference site](https://www.ai.engineer/)

## Description

Monzo's in-house agent started as an emoji you could react with in Slack. Now it authors over 10% of all merged PRs across Monzo's tech teams and runs more than 1,800 tasks a day. Felipe and Francesco explain why it worked so fast. Their answer is the "lots of little multipliers" Monzo already had: an MCP gateway into internal tools and knowledge, a sandboxed agent orchestration system built for a regulated bank, and a platform that turns the agent itself into a building block. That building block now handles incidents, on-call data quality and requests from non-engineers.

Chapters:
- 00:00 Intro
- 00:28 Monzo by the numbers
- 01:37 The Slack agent that went viral
- 02:51 10% of merged PRs, 1,800 tasks a day
- 03:51 LLMs = lots of little multipliers
- 05:04 The MCP gateway
- 05:59 Agent orchestration in a sandbox
- 08:37 The agent as a building block
- 10:07 Incident mode and on-call
- 12:12 Non-engineers shipping changes
- 12:57 Why keep building it in-house

Felipe Felisola Caso & Francesco Galletta, Monzo: https://monzo.com

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,403 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=adfw3xJBx1o&t=1s)** [music] >> Uh, we are Well, that was loud. Uh, we are Felipe and Francesco. Uh, we come to talk to you about the compound value of building Monzo sync house agents using LLMs. Um so what is Monzo? We are a bank. Digital bank trying to make money work for everyone. Uh, to give you a size of the problem for coding agents, uh, we have our teams of engineers maintaining over 3,000 back-end services, around 13,000 um, data warehouse models, and dozens and dozens of ML uh, predictors.

**[0:49](https://www.youtube.com/watch?v=adfw3xJBx1o&t=49s)** So, we do all sorts of things like deciding on credit, deciding on financial crime, and doing very complex use cases both for the app, the back-end, and data. Um So, I'm pretty sure by even by today, but outside of the conference, you have heard a lot of uh, success cases of companies adopting AI agents for coding. Uh, in fact, uh, there was a conference a couple of weeks ago here in New York, and this article came out talking about the state the state of the tech industry in 2026. Uh, and there is this hopefully jokingly quote from X saying that if you're not building your own AI coding harness, are you even a serious tech company? So, some food for thought, right? Uh, then inside of Monzo in January 20

**[1:39](https://www.youtube.com/watch?v=adfw3xJBx1o&t=99s)** 26, this a Slack channel went viral. Agent chip. And hopefully I can Oh, no, what happened? You cannot do this. It's all right. So, hopefully I can bring your attention to this little emoji here. Really cute. We love it. Uh, this became really, really viral inside of the company for a really good reason. You can give it uh, any prompt directly by just reacting with the little emoji to the message and it will pick it up as a, you know, prompt. Uh, so that evolved, we double down, and that became an always available teammate inside our Slack and whole environment. Uh, to give you a few examples, it does feel like a coworker. Uh, it's just there. You can always at Agent Chip and get it to do something for you, answer a question, find out

**[2:27](https://www.youtube.com/watch?v=adfw3xJBx1o&t=147s)** something about some architecture, or just have a chat with you, but I don't I don't think he likes it so much. Uh, it can also do code reviews. So, like a very senior, uh, engineer, you will just tell you it looks good to me and go on your merry way. And you can also assign, uh, linear tasks, as well. So, you can give it tickets and it will just get into it. Um, so all of this is good and well. Uh, forward into today, Agent Chip authors over 10% of all merge PRs across tech, so that's data, uh, machine learning, that's, uh, back in engineering, app, etc. Also runs more than 1,800, uh, tasks per day, which is

**[3:13](https://www.youtube.com/watch?v=adfw3xJBx1o&t=193s)** a lot. Um, and it's being actively, uh, starting to be adopted by business users as well. So, it's not just coding and tech, it's also trying to answer business questions, writing queries, or self-serving anything that a business user may need. So, again, you've heard many success stories about companies adopting AI coding agents, but so what? Why are we What are we trying to share today? Are we saying that we want to brag that we built Claude Tag 6 months before Anthropic released it? We could be. That's not the focus of today's talk. Um, we want to share the secret sauce of what makes Agent Ship a successful product and it's LLMs. But actually LLMs in this case stands

**[4:02](https://www.youtube.com/watch?v=adfw3xJBx1o&t=242s)** for lots of little multipliers. We believe that what enabled us to build Agent Ship so quickly and so invaluable way is a very strong platform at Monzo. So when we say that this went viral and you could write a prompt, react, and profit. Actually this comes from a number of capabilities we already had. So alerting, monitoring, integrations with third parties such as the ones Francesco mentioned, a staging environment that allows us to test easily, queuing abstractions, easy deployment, database abstractions, and a number of other things I could be mentioning here. So first and foremost what we have in our platform is what allowed Agent Ship to be successful. But

**[4:51](https://www.youtube.com/watch?v=adfw3xJBx1o&t=291s)** this does not stop there. We saw even before Agent Ship as a remote agent existed, we started to invest in supporting AI coding agents even in local environments. So the one of the first things we did was develop an MCP gateway that allowed easy access to a set of knowledge sources and internal tools and some of the services that Francesco mentioned. So this is roughly how the architecture looks like. We have the things we want to connect as the internal services and knowledge sources. And we put that behind the MCP server that we built to get the deterministic behavior choosing what are the things we want to expose to the agents and then we manage also authorization, authentication for the number of

**[5:40](https://www.youtube.com/watch?v=adfw3xJBx1o&t=340s)** different agents. Again, this started in the world of local coding agents that wanted to connect and by by now probably everyone has heard in multiple sessions that the more context and the more data we are able to give safely to our agents the better. After that, we built the agent orchestration system, which is exactly what powers Agent Ship behind the scenes and makes it work in a sandbox and with very strict tools and permissions. So, if we go back to our diagram, the whole architecture for the MCP server basically condenses into this box and this is where we connect the rest of the Agent Ship architecture. So, we have remote agents running inside a

**[6:28](https://www.youtube.com/watch?v=adfw3xJBx1o&t=388s)** sandbox in an isolated namespace and then the orchestration system triggers and then reads and gets this information from from that. The main idea here is and again, this is coming across in a multiple of multiple providers and labs and so on is that we want to separate this from the rest of our infrastructure in production. Again, we are a bank, we live in a regulated environment, so we want to make sure that the non-determinism from the agents is controlled. But at the same time, we want to have an environment where we can let it run loose and develop. And again, if we explode this to give you a bit more under the hood visibility of what is going on. So, in this isolated namespace, multiple pods come up with sandboxes that the agents are running

**[7:18](https://www.youtube.com/watch?v=adfw3xJBx1o&t=438s)** on. The agent image is where we define the exact tools the agents will have as as access. So, things like the environment, the CLIs and the authentication and the authorization that again, we get from the gateway itself. The proxy is what allows us to connect to both the exterior world. So, that's how for instance Agent Chip is able to connect to our code, to our repositories, and work with that. Um but, of course, we only get the egress that we choose to do choose to give it. Um so, that is how we make sure that [snorts] it's very controlled and deliberately giving access to the things we want it to be able to see. And finally, the little uh blue-green box there is where the agent itself is

**[8:07](https://www.youtube.com/watch?v=adfw3xJBx1o&t=487s)** running. So, that box inside the box inside the box is where the nondeterminism happens, and it's where the agent can perform everything that it wants. So, this is how the whole diagram looks like when we are able to give our MCP server access to everything that we care about for the agent, we are able to safely give it access to our data, and the agent orchestration system handles everything that's around it. With these as building blocks, any use cases that come after it are much, much easier to be built on top of. So, as Francesco mentioned, this we can connect Slack to, and then we can connect GitHub, and then we connect Linear, and then I just use a different color to

**[8:54](https://www.youtube.com/watch?v=adfw3xJBx1o&t=534s)** show this is the more than 3,000 services that we can be connecting to to this as a building block. So, in the same fashion that we had multiple things in our platform that enabled us to build Agent Chip and get value out of it. Now that Agent Chip is also a building block, the multiple parts of our bank can also leverage it to create other use cases. So, we start to see this building blocks enabled us to not only get more um product features internally, but to drive concrete business outcomes. Um we observed a higher breadth and volume of tasks that engineers are able to run, as you you expect, because then we don't need people to be babysitting their agents all the time. They can use their coding assistant for

**[9:43](https://www.youtube.com/watch?v=adfw3xJBx1o&t=583s)** um specific tasks, but they can also delegate to remote agents. We can automate routine processes much better. So, that allows humans to focus on the higher value problems where the ambiguity lies particularly. Some examples of these that we are able to do. Um this is Agent Chip working in incident mode and leveraging the MCP to get very relevant data. So, what happens here is whenever we identify and trigger a new incident, Agent Chip joins the channel and is able to start an investigation, understanding logs, understanding traces, being able to connect to that exact service, and of course, the code itself to see what's going on and to help the human with a very high signal. We don't want the agent to be saying a lot of things

**[10:31](https://www.youtube.com/watch?v=adfw3xJBx1o&t=631s)** during an incident and testing hypotheses like we want it to maintain high signal, and we give the humans also control of how much Agent Chip will be able to support there. We can continue to use it on Slack, but not only by triggering it by mentioning it, uh but also in what we call ask channels. It's basically squad-to-squad interaction inside Mondzo. A squad needs to have some context on a back-end service, on a product development, on the road map, and Agent Chip can also, since it can connect to our knowledge sources, it's able to draft a response for the human in the loop to get as reference and support there. Maybe the response will be enough, and Agent Chip can just solve that ask ticket by itself. Sometimes it will ask for more

**[11:19](https://www.youtube.com/watch?v=adfw3xJBx1o&t=679s)** context, and the human in the loop can be tagged um and come in to support more. Um something that we're doing very recently that's been uh creating a lot of value is also triaging data quality alerts and checking for back-end changes that can create problems. So, basically we call it Agent Chip on Call and it observes the failures that we have and triggers an investigation automatically. This is the reactive version of it. But, what if the errors never happened in the first place? We created based on this the proactive version that monitors back-end changes and identifies which are the potential outcomes that that can have for our data even before the data is processed in the next batch execution.

**[12:07](https://www.youtube.com/watch?v=adfw3xJBx1o&t=727s)** So, again, all of these are examples of how our technology team is using it, but even better than that, we've observed a lower barrier for non-specialists in the company to contribute to our systems. With a very quick entry point for Agent Chip on Slack, non-specialists can, based on product feedback, based on ideas, based on discussions they are having, just call Agent Chip, get a draft that works, that is already tested in staging, and then, and only then, involve an engineer to make sure we get the changes reviewed and deployed properly. So, this doesn't change the rigor to which we develop software at Monzo, but this does allow a number of non-specialists to also start contributing more closely to the team.

**[12:57](https://www.youtube.com/watch?v=adfw3xJBx1o&t=777s)** You can be thinking now, the market is moving fast. We are hearing a lot of exciting developments and new products and new features coming from multiple companies here in the conference and otherwise. What makes us believe that Agent Chip continues to be a valuable thing at this point in 2026 and moving forward? Um As I said and I like to to reiterate, Agent Chip being composable, it is now a new building block that we have in our platform. So, it very quickly enables new use cases for agentic implementation at Monzo. Now that we can connect it very safely with all our security requirements and all our back end and platform requirements at the same time.

**[13:46](https://www.youtube.com/watch?v=adfw3xJBx1o&t=826s)** Our platform is plat provider agnostic by definition. So, if we come back to the diagram, the little blue/green agent box there can be very easily swapped by any for any model. We can dynamically choose which model best fits the purposes that we have. So, we are not specifically tied to any provider by definition and that gives us flexibility to understand which ones will fit Monzo's needs the best. Um and finally, we are continued to move to cover a bigger development window. So, if we even if we stop development today, this would already be valuable, but we can cover a much broader sense in terms of we draft changes in the back end, we draft changes in the app. We can

**[14:34](https://www.youtube.com/watch?v=adfw3xJBx1o&t=874s)** test these changes in a staging environment, cover the data tests. Who knows? Maybe even predictors on the other side. So, when remote agents are able to do this end-to-end, we can understand and integrate our systems much better. So again, the market is moving, doesn't mean that we are necessarily married to agent chip until until the end, but these and other aspects of it make us strongly believe that is it is a very strong part of our internal platform now. And the key takeaway that I want to I want to you all to take from is how can you benefit from LLMs, but not the traditional LLMs, but the lots of data multipliers that you and your team can use to leverage value.

**[15:21](https://www.youtube.com/watch?v=adfw3xJBx1o&t=921s)** Thank you. >> [applause]
