---
id: QSeaZ6qHyXs
title: "Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic"
slug: claude-managed-agents-q-a-evals-ci-cd-and-multi-tenancy
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-12T06:07:45Z
video_id: QSeaZ6qHyXs
url: https://www.youtube.com/watch?v=QSeaZ6qHyXs
youtube_url: https://www.youtube.com/watch?v=QSeaZ6qHyXs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=QSeaZ6qHyXs) · [Conference site](https://www.ai.engineer/)

## Description

How to version agent configs, isolate customers, add GPUs and keep a long-running agent responsive.

NEXT UP: AI ENGINEER CODE SUMMIT
Join us in SF for the second annual AIE CODE Summit, Nov 10–12, our last flagship summit of 2026. Applications live now: https://aie.codes

The workshop closes with audience Q&A for Priyanka Phatak and Gabe Cemaj: syncing agent configs in CI/CD with the ant CLI, what happens when you message an agent waiting on a custom tool, how Anthropic runs evals, sharing resources across a workspace, code-review agents, tenant isolation, GPUs via self-hosted sandboxes, modeling a multiplayer Slack agent, and a coordinator pattern that keeps the main agent free while a subagent handles custom tools.

This is part 4 of 4 of the Claude Managed Agents workshop from Anthropic.

In this video:
• Keeping agent definitions in YAML and syncing them in CI/CD
• Isolating tenants by workspace, org or session metadata
• Self-hosted sandboxes for GPUs and extra memory
• A coordinator pattern for custom tools

SPEAKERS
Priyanka Phatak, Member of Technical Staff, Anthropic (leads the Claude Managed Agents engineering team)

Gabe Cemaj, Member of Technical Staff, Anthropic

LINKS
Claude Managed Agents docs: https://platform.claude.com/docs/en/managed-agents/overview
Scaling Managed Agents: Decoupling the brain from the hands: https://www.anthropic.com/engineering/managed-agents

CHAPTERS
0:00 Q&A: CI/CD for agent configs
1:10 Q&A: messages during custom tool waits
2:06 Q&A: other workshop repos
2:45 Q&A: Anthropic's eval practices
4:42 Q&A: sharing resources across an org
6:29 Q&A: reviewing agent-written code
8:48 Q&A: tenant isolation
9:54 Q&A: one agent, many customers
12:10 Q&A: custom compute and GPUs
13:20 Q&A: a multiplayer Slack agent
14:34 Q&A: very long-running sessions
16:30 Q&A: coordinator pattern for custom tools
18:30 Closing

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,493 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=0s)** All >> [music] >> right, we have a question here. >> Hey, how do you CI/CD the agent convex? Um, >> ah, that's a great question. Uh so we have something called Ant CLI which is a CLI that basically wraps our API to make calls um and allows you to do sort of Terraform like things where you pass in YAML. So you can put your uh long-term uh resources in YAML in your codebase and then build um CI/CD to basically

**[0:50](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=50s)** update the ANC with ANCLI using those YAML uh every time you make a change to your to your resource. Does that make sense? >> Got it. Uh so I assume you guys use the same internally too. >> Yeah, that's how if if we need to build durable long-term resources, we just we can check them in. >> All right. Thanks. >> Thanks. >> Um so I think you mentioned you can send messages whenever you want. Um can you still send messages if the model is waiting for a custom tour result? >> Uh not when it's waiting for a custom tool result. We basically pause execution uh at that time. Um but if the model is doing other work uh then we do allow you to queue up messages. Um but when it's doing a custom to result we're expecting you to send that. Um so because of ordering purposes we we block the calls.

**[1:38](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=98s)** >> But what happens if you do send the message >> you'll get a 400. >> Okay makes sense. >> Uh there was an ask to see the QR code slide one more time. >> Uh >> the uh the credits one. Yeah. Any any other questions? If you're if you're shy we >> Yeah, we'll hang out after for any any questions you don't feel >> Yeah. >> Yeah. I'm looking through the repo. There's a lot of interesting workshop talks. Is there anything that's missing from that like slides that would help us go through other >> sessions like that you can post or is it pretty much self-explanatory through the the read me files? you just like have you know because you had like a skilled at workshop which

**[2:25](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=145s)** >> yeah yeah the other workshops came from our code with cloud conference um most of which you can find online u for the version we did in London about a month ago so >> all the all those talks are on YouTube if you're interested in the other repos that are in there but this one should give you like a pretty good overview and it's pretty similar to what we've done at other conferences >> yeah so just going back to eval can you talk a little bit about you know how you guys are maintaining quality best practices around the the eval harness. >> Uh yeah, we run a lot of eval especially as new models come up, as new capabilities come up. We have access to the models before you all do obviously. Um so one of the things that we as a managed offering want to make sure we do is that we uh update our assumptions about the harness as early as possible

**[3:13](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=193s)** so that we can remove things that are no longer needed. Uh and we do all of that in eval. But we have internal tooling that basically looks like different data sets that we can then run our different sessions. It's because it's all in the cloud. It's easy to say like spin up 10,000 sessions to do this uh all in parallel. Um and then we evaluate those results and tune prompts and tune assumptions, remove things, add things uh to make sure that for every model release, we're doing the best we can. Uh and we're evaluating all sorts of things for generic purposes, not just coding. So, so how does that extend into the agents that we would build? Is there a recommended path for um for evals or is it kind of just bring your own solution? >> Uh I think the the best advice we can give you is get high quality data u to

**[4:02](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=242s)** evaluate over. I think clock code is pretty good at building an eval for you but garbage in garbage out. We've seen that some of our initial ideas for how to evaluate things were sort of illdefined and you get 100%. But what does that mean in performance? So iterating on your data and making sure that you're setting up the problem correctly. Um I know it's like not out of the box solution, but it generally the advice that we've seen works. >> And you can probably look at like your historical sessions and like what results you got and then sort of try to score it and see how the model's doing. Um that would be a good way of like building your data set looking at your historical sessions. >> A question over here. >> Hey, thanks for sharing. Uh I have a question about how to share those agent and all the resources across all the the

**[4:50](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=290s)** entire organization. The reason I'm asking is because we use cloud desktop quite a lot. We building shared skills we building shared connectors. But for the uh everything you share today for example agents memory store or MCB channel can we actually share them or can we partially share them across the organization to different departments? So what is boundary? What is the privilege about those resources? Are those resources bounded to my account or how can I control this? So what's the what's the way to do that? >> They're bound to your workspace. So any API key within your workspace can have access to the resources that >> So can my can my teammates edit or modify what I'm building or is completely controlled? Right. >> So I I think your um cloud platform admin. So you'll have an org for your

**[5:39](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=339s)** organization and then your admin will be the one setting up the workspaces and deciding who gets access to which workspace. Yeah. >> So I think you would basically design your workspaces depending on your access control. Correct. >> You'd probably want to do like whatever group of people you want access to resources X put them in one. >> So you can share whatever you want even partially of the you know you build an agent they can do something but I only want to share part of that. For example I share the memory to someone. I share the MCP channel to the others. Is that possible or I need to share the entire text stack of what I'm building? >> We don't have fine grain controls of like this is share, this is not, but you as a a as a builder and integration would be able to control that pretty granularly so that your end users can have access to partial. >> Cool. Sweet. Thanks very much.

**[6:27](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=387s)** >> Thank you. >> Yep. Yeah. So basically we can generate a lot of code with a lot of agents and then we're getting to the bottleneck of uh reviewing that code making sure you can actually merge it. Um how do you guys think about that in terms of are you deploying like I see you deploy every 30 days which uh might be a different definition of deployment but is it deploying something you can actually test to make sure it works well or how are you reviewing uh this many lines of code from all the agents? So the the original workshop that we wanted to do was actually answering that question. How do you how do you build agents to review code? Um what we found is you can build an integration with CMA so that on PR it kicks off one, two, three, many sessions with many sub

**[7:15](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=435s)** agents to evaluate what has changed and find bugs. Internally we we have uh these sorts of agents do a lot of the uplift for us and we've seen that that enables us to uh reduce the amount of time we need to spend on a per PR basis and reduce the number of bugs and keep the quality uh high. Um but this is >> partially an open question of now we've removed the boundary of uh typing and exploded the number of PRs we can make per day, hour, second. Um how do we keep up? And we're still exploring that. But >> yeah, >> CMA is part of the answer, I think. >> Yeah. And you can iterate in a loop, you know, to like review, add comments, review until it's done, but then at some point you still need to run the thing to make sure it works well locally. So I

**[8:03](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=483s)** think that's where the deployments can come in where you can um you know, auto deploy something that you can test with a custom deploy agent like you said. Um, it just depends like if you have different environments for each branch, but >> you you can run your application in the sandbox as well and have claude self validate the changes that it made >> um and make sure that >> like it acts as a QA agent as well. >> Are these like long running sessions that you can go in and actually play around on the UI? >> We don't have uh kind of tunneling today but >> So you would have Claude go in there, play around with the browser. >> That's right. and then and validate it and then maybe even give you back a video maybe. >> Yep. Exactly. >> Cool. Thanks. >> Any other?

**[8:49](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=529s)** >> Hello. >> Hi. >> Uh for an enterprise company, if at all we want to maintain true tenant isolation that we want to support. I heard that you are not supporting yet the enterprise uh company uh uh use cases. Probably >> we're not supporting onrem. >> Onrem. Yeah. But what if I want to have >> uh let's say I have 100 customers that we support as an enterprise company. Can I have separate uh cloud managed agent instances >> per uh company of ours that we want to support? Is that a viable option that you support? Is it only one instance that we get or can we get one instance per company that we support as an >> it's however you choose to define it. You can define an agent per customer and then that way the data will be segregated. You can use a workspace per

**[9:38](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=578s)** customer if you want like true isolation. You could do an org per customer. Uh so it depends on how you want to set up uh your agents and you would probably want to maintain that mapping of like which customer maps to which agent. >> Okay. >> Yeah. >> I think I have a followup question. So uh just given the scenario that uh we have two customers and we want to build uh the agent once but the agent going to be shared by the two customers. Uh how to achieve that? >> There's many ways to do it. You could do it through automation. So you could have your agent definition live in YAML in your code and then build tooling to update it to both of your workspaces and basically synchronize them. Or you can model everything in a single

**[10:24](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=624s)** organization and then do the the modeling that way. Um >> so you could create like a single agent across all your customers and then you manage the mapping of like which customers using which session. >> Yeah. >> Yeah. Then in uh in which workspace I create this agent. >> Yeah. If if you do it per workspace then you need we give you tooling to synchronize yeah >> a single definition in your code to multiple places so that whenever you update it in your code through CI you can update all of the definitions at once. >> So you can either make a copy of your agent which is essentially a template of system prompt model name tools and you can like make a copy across every workspace. Let's say you go down like the one workspace per customer or you can just put all your customers in a single workspace and then you maintain

**[11:13](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=673s)** the mapping of which either you do again have like copies of your agent or you use a single agent and then have the mapping of like which session maps to which customer. We have like a metadata field on the session where you can put in like let's say customer ID so you know which session map to which customer. >> Okay, that you know like putting all the customer data in one workspace. How do we uh satisfy the data segre segregation uh >> requirement you know >> yeah if you if you care about data segregation then you need to put them in individual workspaces and the resources are allocated per workspace but >> there's basically tooling to enable you to do uh each of each of those things >> and when you say data segregation like is is that like a legal requirement or is that something just you want to

**[11:59](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=719s)** >> yes something legal like customer doesn't want to share data with other customers you know they want to dedicate. >> Yeah, you would do it per workspace. >> Okay. Okay. Thank you. >> I saw a question here. You're have to speak up or >> um is there a way to modify the compute environment, meaning um in some cases I may need to have higher memory for my agent to do the work or I need a GPU for my agent to actually do the work. Is it supported in this or >> to to the today? If you want to do custom resource allocations for your sandbox, you would use self-hosted sandboxes. You would use something like modal that has GPU offerings. Yeah. >> And we have cookbooks and kind of first-party integrations so that you can

**[12:48](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=768s)** hook up your modal instances to run your agent loop uh inside of modal instead of our provided sandboxes which today are all the same. Uh so if you care about different scale you would use a different provider for that. >> And do you have like a list of uh specifications of what the environment these agents have access to? >> Yeah, you you can find that in our docs and you can find cookbooks to integrate with thirdparty providers as well in our docs. >> Yeah, we have a bunch of cookbooks on like how to work with Moto or EB2, Daytona, whatever provider that you want to use for sandboxes. Yeah. >> Yep. >> Hi. >> Hi. Thanks again. So out of curiosity, how to build a sim similar version of cloud tag using CMA in a different chat channel especially for the multiplayer mode.

**[13:35](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=815s)** >> Yeah. Uh this definitely is something you could do uh today where >> you would on a per thread level map it to a session >> and then anytime a user >> messages that session you inject that as a user message letting the agent know hey this is coming from Gabe or this from Priyanka and so everybody can message uh that agent independently. You can have it share memory across sessions so that it learns uh from each other. you can give it tools to reply back uh using like the Slack post tool or something like that so that the agent can decide when it wants to post. You don't necessarily want to just mirror whatever the agent is responding. You want it to be explicit. Uh but you could definitely model this uh using CMA and >> and if you wanted to be like cloud tag,

**[14:23](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=863s)** you'd probably do like one agent per Slack channel and then every agent has its separate memory and only has access to messages within that Slack channel. >> Yes. >> Hey, thank you for the presentation. Very useful. Quick question. in terms of um looping and doing long runs um in this cloud console, how do you see that? Um is this something you have like some specific module that I I'm not finding or um are you planning to develop that um more in the future? Thank you. >> Do you mean how do we provide you observability for really long sessions or >> No, no, no. Um so more focus on um using this platform to build those long

**[15:12](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=912s)** running agents like hours and hours like last six hours for example. Um is this something that is already embedded in what you have built in the agents or I'm more curious to know if you are developing something specifically for that or how do you see that trend? the the outcome system that I demoed is the best way to do really long sessions because you define an exit criteria and cloud will just keep going until it meets that criteria and it could be a really long task like you know rebuild blank uh and it will just mercilessly iterate until it matches the the rubric. >> There there's nothing special you would need to do to get the session running longer than >> six hours. should it should just keep keep going.

**[16:00](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=960s)** >> One quick followup. So if I run the agent for hours and hours and I want to understand like checkpoints status, the best way to do that will be through the session tab. >> Uh yeah, >> it would be the session event stream. Yeah, there's the events API on under the session. Okay, >> you could have a custom tool called like update status for human or something like that and Claude would on interval whenever it feels like it's made progress call that tool and give you a status update. >> Thank you. Thank you very much. >> All right, any other final questions? Yes. Um, following up on that previous question about using this for cloud tag or similar functionality, I've been uh analyzing a whole bunch of uh agent frameworks. So if you get a message while the um

**[16:48](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=1008s)** agent is waiting for a custom tool result, for example, human in the loop, um you said it would 400. >> Do you have uh any suggestions on how you would deal with that? >> Um >> can you do custom tools on a sub agent? I forget >> you could do custom tools because then you could basically have like a sub agent that's handling your custom tool and then that way your main kind of coordinator agents always free for receiving >> in the API. Can you directly return a custom tool for the sub agents tool? Well, the sub agent would emit the custom tool use and then you would populate it back to that. >> Essentially, you define like your main coordinator agent and then you can say agent A can talk to agent B and C and then agent B is the one let's say processing your custom tool. So, your agent B definition is where you'll

**[17:37](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=1057s)** define your custom tool and then that's the session thread that you would listen to to get the >> Is that a different session thread or the same? >> No, it's it's part of like the same core session. It's a different thread technically, but you only interact with the main thread and we correctly delegate because we know where it needs to go based on ids. >> Um, >> okay. >> And then the main agent will pass it >> pass the sub agent. >> So the session is still idle even though the other >> if if a sub agent is doing work, it's not idle. It's >> but like if the main coordinator agent is idle, the sub agents could still be >> still doing work. Yeah, you can see that here. But really impressive. this uh gap here. The main session is is idle. The main the main thread is idle while the sub agents were doing work >> and they could be waiting for tool results.

**[18:22](https://www.youtube.com/watch?v=QSeaZ6qHyXs&t=1102s)** >> Exactly. >> Yeah. So, if you're trying to do something where you want like the main agent to be always chatty, then I think the coordinator pattern works pretty well for that. >> That's awesome. >> Yeah. >> I think we're we're at time, but we'll we'll be just outside if you want to come talk to us. Uh thank you for having us. >> All right. Thank you so much. [applause] >> [music]
