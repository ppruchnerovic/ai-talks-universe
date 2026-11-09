---
id: HvboD89DyQ8
title: "No, That's Not a Software Factory — Ryan Cooke, WorkOS"
slug: no-that-s-not-a-software-factory-ryan-cooke-workos
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ryan Cooke"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-09-27T15:30:30Z
video_id: HvboD89DyQ8
url: https://www.youtube.com/watch?v=HvboD89DyQ8
youtube_url: https://www.youtube.com/watch?v=HvboD89DyQ8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "WorkOS", "Ryan Cooke", "software factories", "coding agents", "MCP gateway", "Model Context Protocol", "engineering productivity", "outcome metrics", "Linear", "Slack", "GitHub", "product engineering", "AI agents", "Claude Code", "Devin", "AI Engineer", "AI Engineer World's Fair"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# No, That's Not a Software Factory — Ryan Cooke, WorkOS

**Ryan Cooke**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#WorkOS` `#Ryan Cooke` `#software factories` `#coding agents` `#MCP gateway` `#Model Context Protocol` `#engineering productivity` `#outcome metrics` `#Linear` `#Slack` `#GitHub` `#product engineering` `#AI agents` `#Claude Code` `#Devin` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=HvboD89DyQ8) · [Conference site](https://www.ai.engineer/)

## Description

The standard software factory puts an agent in a sandbox, prompts it and merges the PR. When WorkOS built one, the results were hard to tell apart from engineers running Claude Code on their laptops. Ryan Cooke, an engineer at WorkOS, argues that counting PRs or lines of AI code is the wrong measure. What matters is outcomes: are you actually shipping more to customers?

WorkOS's answer is to build its engineering process into the factory itself. TARS, its agent, lives in Slack, Linear and GitHub and uses webhooks to track projects and pick up the next ticket on its own. A PM agent drafts the "Hilltop" product doc and breaks approved work into tickets, which solves the blank-page problem. Horizon, the orchestration layer, sits in front of an internal MCP gateway that connects every tool, including Snowflake. Cooke calls that gateway the single best investment for any team starting a factory. He also covers bug and support triage, why WorkOS is building its own sandboxes and a company-wide memory layer, and how it measures success with defect rates, recovery time and adoption.

Related links:
WorkOS: https://workos.com

Timestamps:
0:00 Intro: the standard software factory
1:17 Output metrics hide what's working
2:37 Measuring outcomes instead
3:12 Why a basic sandbox wasn't enough
4:07 TARS and Horizon
5:22 Webhooks: from code work to product work
6:32 Building the Hilltop doc into the factory
8:07 The PM agent
8:52 Demo: kicking off a project from Slack
10:17 Solving the blank-page problem
11:02 Works with Devin and Claude Code too
11:57 The MCP gateway: a context engine
13:37 Why every factory needs an MCP gateway
14:07 Bugs, support triage and our own sandboxes
15:27 Next: a company-wide memory layer
15:57 How we measure success
17:02 Owning the infrastructure to self-improve
18:02 Wrap-up

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,978 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=HvboD89DyQ8&t=12s)** Well, thank you for joining the final day of the conference here. I know it's been a long week. But I'm excited to talk about a topic here that is very near and dear to me. Software factories. Um You this is probably not a new concept to any of you. I'm guessing if you're all here, you're very familiar with software factories. You know, Ramp blogged about their inspects several months ago. I think maybe December last year. I forget exactly when. It's been a little while. And that really kind of like excited the entire industry of thinking like, oh, we can actually build software very differently now that AI is extremely capable of writing code. Um a lot of other companies have followed suit. Um and there's kind of like a standard set up

**[1:00](https://www.youtube.com/watch?v=HvboD89DyQ8&t=60s)** here. Uh you have a sandbox that you put your code into. Um you put a an AI agent in there. Maybe a Claude code section or an open code. Um and with a prompt, it generates a PR and you merge it. Um You might be building this already [clears throat] yourself. We have taken a slightly different approach at WorkOS. Um and the motivation for what we are building is that we see a lot of the kind of success metrics um really focusing on output, right? Like you'll see posts on X and blogs talking about the percentage of PRs or the number of pull requests or how much code uh is being generated by AI moving into production. Um and this is

**[1:49](https://www.youtube.com/watch?v=HvboD89DyQ8&t=109s)** just really output metrics that um you know, this can actually disguise how well these systems are working. Percentage of PRs or number of PRs may be lying in overall increase in PRs. It's very hard to distinguish whether the output is actually driving outcomes. And so that's kind of where we focus our efforts when we're thinking about a software factory. It's like if we're going to go put engineering time into building this level of automations and there's a bit of work that needs to go into this. Full-time teams dedicated to this. How do we want to think about the success of this and whether this is actually driving value for our organization, our engineering organization?

**[2:36](https://www.youtube.com/watch?v=HvboD89DyQ8&t=156s)** And so we measure instead of just code output, we're looking at outcome metrics. And that is really about like are we accelerating our ability to deliver features? We think that the dream of the software factory is that it gives each of our engineers a small engineering team for themselves. And so the consequence of that really needs to be that we're building more and we're shipping more and that as we embark on complex features, those can get built a lot more a lot more quickly. So what does this actually look like? Well, we kind of started with the same thing you've seen in other other factories. We start with a sandbox we built on top of Cloudflare. We put an open code model

**[3:26](https://www.youtube.com/watch?v=HvboD89DyQ8&t=206s)** router in there. We're feeding it prompts. Um, and we kind of very quickly kind of ran into this situation where this wasn't driving more outcomes. This was not an incremental increase or an exponential increase over engineers just driving cloud code on their laptops. It was actually pretty indistinguishable for us. And so we really kind of started to think about, well, how can we embed our engineering processes into the factory itself? It's not sufficient that the factory is producing code. We actually want it to take a lot of the other work that our engineers do to produce products and automate that as well. So, we kind of split this into two parts. One is we have the system we call TARS. This is a way for users to interact with

**[4:18](https://www.youtube.com/watch?v=HvboD89DyQ8&t=258s)** the coding agent. And it is embedded into the tools that we use. So, not just Slack, but also Linear and GitHub. We subscribe to webhooks through TARS so that TARS can actually track the progress of projects in addition to generating the code outputs. And then we built a separate system called Horizon. And this is the infrastructure orchestration layer. This is a lot more similar to Inspects and Minions and and some of the other systems that other companies have built. But, it sits in front of an MCP gateway. And I'm going to talk a little bit more about why that MCP gateway has been really transformational for us. So by

**[5:08](https://www.youtube.com/watch?v=HvboD89DyQ8&t=308s)** feeding our webhooks, activities that are happening in other uh source code systems and project tracking systems, we're starting to get to that level of autonomy where our factory is performing product engineering work, not just code work. So, what's an example of this? In Linear, we can define tickets that have dependencies. So, one ticket blocks another ticket. Pretty common for, you know, breaking down uh large units of work into smaller ones. Because uh TARS is getting webhooks on ticket completion, it can automatically pick up the next ticket in a cycle. And so, we can do through our planning process construct like a map of how this plan we think this plan is going to get executed and TARS can start to execute on that

**[5:57](https://www.youtube.com/watch?v=HvboD89DyQ8&t=357s)** autonomously. The other thing that we have is in between those steps when a ticket is completed, we can ask TARS "Can you reevaluate the linear project and let me know if it's missing now tickets?" Because as you do work, you're learning about where the gaps in your plan. And we want to continuously keep our our plan fresh by using the agent itself. Because the agent is determining that there may be missing pieces to what we initially planned for the project and the goal that we have in mind. So, we run this product engineering culture at WorkOS. This is where engineers are responsible for a lot of the product functions. We don't have product managers on teams today. Um and one of the rituals as part of this product engineering process is we

**[6:46](https://www.youtube.com/watch?v=HvboD89DyQ8&t=406s)** create a hilltop document. It's a PRD and it is intended to both define what is the purpose of this project, but also incorporate um what are customers talking about? Like where are we seeing the need for this unit of work? Uh it looks at competitive analysis. Like are there similar products out in the market today that we can draw inspiration from? We start to bring design early design screens into this. Um and we outline like what are the major milestones. And so, by kind of consolidating and canonicalizing this information into a document, this is something our product engineers have been doing uh throughout the entire uh company. Um now we can ask give this resource to an agent and an agent can break this into units of work.

**[7:34](https://www.youtube.com/watch?v=HvboD89DyQ8&t=454s)** Uh and so, this has been a really uh powerful way for us to take existing processes and encode them into the factory themselves. Like I mentioned that it's listening for web hooks. I'll show an example of what this looks like, but it it can see that the hilltop document through linear tickets has been reviewed and approved and by virtue of it being approved can start work on this project automatically. So we don't need a human to be shepherding this agent through every single step of the life cycle. So we created an agent specifically for this part of the process. We call it the PM. And it is doing the first draft of the hilltop based on the brief specification that we give it.

**[8:21](https://www.youtube.com/watch?v=HvboD89DyQ8&t=501s)** It's adding context to that in addition to reading the human reviews and then it picks up the implementation and breaking that into tickets. And there's an opportunity for humans to stay in the loop for each part of this process. I mean it's very common for a human to intervene or comment on a ticket that's generated by AI, give it further guidance or refinements. Um but it's really about that like cold start problem where we can kind of get over the hump of creating all these different resources. Okay, so what does this actually look like? So here's a project I kicked off last month two months ago. Um we're adding a new API to products I lead called Vaults. And with a command here in um

**[9:08](https://www.youtube.com/watch?v=HvboD89DyQ8&t=548s)** in Slack I can kick off this project with a simple description, usually a few sentences of what I'm trying to accomplish. Tarsin goes in and creates all these resources for me. I don't need to go and create the project in linear. I don't need to create a draft of the notion document. Um all of the decision logs and the open questions. Um Tars is creating a first pass at that. And so this then gives me an easy framework for me to step into as the lead product engineer and start giving more specification, rounding out areas that aren't well defined with knowledge that I had know about what we're trying to accomplish with the project, and then hand it back to Tars uh for execution. So, here's an example of uh the project. Um and it's like I said, it sets up

**[9:58](https://www.youtube.com/watch?v=HvboD89DyQ8&t=598s)** these first milestones around our product engineering process. So, we haven't done the hilltop review yet here. When that's done, we'll uh we'll we'll mark this ticket as complete and Tars will pick that up and move on to the next stage of project implementation. So, what we found is like a lot of teams are now doing more project brief and hilltop work because our agent can seed all that information. It's that blank page problem with writing. If you can come into a document that already has information, and you know, these agents aren't perfect. There are times where it grossly overestimates what we're trying to accomplish with this project, and we have to cut out a lot of the scope that it comes up with. But, that's fine. That's a lot simpler for an

**[10:47](https://www.youtube.com/watch?v=HvboD89DyQ8&t=647s)** engineer to add input into into rather than them spending time to set up all these primitives themselves. And then we can continue to drive this work, you know, through Slack, through Linear, um and ultimately uh results in PRs in GitHub. The other thing that this lets us do is we don't necessarily always need to use our coding agent to implement uh pieces of work. Uh Devin is very popular. We have a lot of folks that really like using Devin. They can point Devin to these tickets and the same documentation to give Devin the context it needs to go and implement different parts of the work. Uh same with the local cloud code if you're just using Opus in a local harness. Um it can grab through MCP all of these uh

**[11:34](https://www.youtube.com/watch?v=HvboD89DyQ8&t=694s)** all of these pieces of documentation and use that as context for its work. And then, of course, we have people that collaborate in these project channels as well. You'll notice our security team will come in and look take a look at new projects, weigh in on the security implications, and so forth. So, I alluded to we we kind of early on in the the development of our factory is created our own MCP gateway. Um, we call it our context engine. Um, this connects into all of our internal systems, but it also builds system prompts and context around what how to navigate these tools and when to use these tools.

**[12:21](https://www.youtube.com/watch?v=HvboD89DyQ8&t=741s)** So, it is connected into Snowflake, which is our main data lake. We have semantic tables that we've built in Snowflake that describe product utilization or customer conversations. And then, we can provide an agent through our MCP server in the tool description list of here are the tables, this is the content they contain. If you're trying to answer questions about this type of content, write a query for these tables. And so, it gives us a little bit of orientation to an agent to understand how to use how we use our tools, how we've organized linear in Snowflake, and give some guidance on where to find information. What has been really surprising about this is we actually now

**[13:10](https://www.youtube.com/watch?v=HvboD89DyQ8&t=790s)** use this MCP server across a lot of other different internal tools. We open it up for people to query directly from Slack to do data or customer analysis. And so, while we initially kind of envisioned that this would just be a way to connect our agent or coding agent to all of our systems. Uh this has been an incredible piece of leverage for a lot of our internal teams, and we're building a lot of other tools on top of this MCP gateway. So, if you're just getting started with thinking about a software factory, it's well worth your time to invest in an internal MCP gateway server that both connects all your tools, has descriptions that can tell the agent how to use those tools and how you specifically organize the information in them, and I think you'll find that that

**[13:58](https://www.youtube.com/watch?v=HvboD89DyQ8&t=838s)** ends up being useful in a lot of other use cases. Like I mentioned, we try to automate other parts of our software development. Um we have like bug bug requests that come in through Slack. Uh so, TARS through webhooks can listen to those and take a first pass at triaging and implementing opening PRs to fix bugs. Uh we have a lot of our customers uh in shared channels in Slack, as well. Uh we found TARS to be pretty useful to uh triage support requests that we're getting through them, because it can look at the code, it can often understand like where the customer might be running into problems with our product uh from the code perspective.

**[14:46](https://www.youtube.com/watch?v=HvboD89DyQ8&t=886s)** Um I showed you an example of how we kind of organize major features around this. Uh and then the last place I think is really exciting, we're all trying to get to the self-improving software, or the self-driving software. So, we're using uh TARS to actually build out our own uh sandbox infrastructure. So, we want to move off of some of the sandboxes as a service and own that infrastructure layer ourselves. Um Some of the reasons we have for that is we want really deep control over the session information, and uh be able to move workloads around different parts of our infrastructure. Uh so what we're building out next is our memory layer and we want this to be an evergreen context uh about what every person in the company is working on,

**[15:36](https://www.youtube.com/watch?v=HvboD89DyQ8&t=936s)** what team do they sit in, what products are they responsible for, and then at an organization level, what is the semantics about Work OS and how we do our work. And this we want to be able to plug into both our software factory, but lift that context out of our factory and into our other AI tools as well. So, I think this is kind of our our major takeaway of where we've seen a lot of folks invest effort just around outputs and where we think we can actually get that human exponential value out of our factory. Can we be actually delivering values to our customers? We think a lot about shipping and customer impact and so we want to encode that into their our software factory itself. Um certainly worried about, you know, introducing

**[16:26](https://www.youtube.com/watch?v=HvboD89DyQ8&t=986s)** instability into our products. So, all right, can we measure uh defect rate and other um you know, time to recovery uh metrics? Um and then a lot of anecdotal, like we want to see our engineers using TARS as a sign that this is giving them value and accelerating their work. We want to see that they're moving off electing to move out of their local harness and into a cloud sandbox. And then the real goal is we can use this information because we own the infrastructure, we can see what's happening in the infrastructure. We use this information to self-improve the factory. We want it to learn, we want it to get better about how it writes code. We want to see where um our engineers

**[17:17](https://www.youtube.com/watch?v=HvboD89DyQ8&t=1037s)** can improve their skills. There's so much moving quickly in AI. It's kind of like a constant race to keep up with the latest um you know, tips and techniques. We can actually point agents at sessions and see where are the gaps and how people are using our factory. Where is there a skill that we should be building because the agent made a mistake. What skills are no longer relevant? Maybe the code has changed to a degree where a skill that we wrote six months ago is now obsolete. So, that continues verification. Semi-online is where we kind of see a big advantage to actually owning all the infrastructure ourselves. So,

**[18:04](https://www.youtube.com/watch?v=HvboD89DyQ8&t=1084s)** say it for the third time, it's worth repeating. Sandboxes are great. It's cool to run an agent and have it open a PR. We really think about our software engineering practices and processes and we want to encode those in automation. I'm Ryan. I'm one of the engineers here at WorkOS. We have a booth right opposite the speaking area. If you are building software factories, I would love to talk to you. I would really love to hear how you're handling authorization. This is something I don't talk about because we haven't figured it out yet for ourselves, but maybe you all you all have some insights. So, please come by the booth, talk to me, would love to chat. Thank you. >> [music]
