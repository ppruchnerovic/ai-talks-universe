---
id: V2UqEUA8NjM
title: "Stop Making Your Customers Click Approve - Emil Chetty, Wise"
slug: stop-making-your-customers-click-approve-emil-chetty-wise
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Emil Chetty"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-11-05T08:00:07Z
video_id: V2UqEUA8NjM
url: https://www.youtube.com/watch?v=V2UqEUA8NjM
youtube_url: https://www.youtube.com/watch?v=V2UqEUA8NjM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Emil Chetty", "Wise", "AI agents", "agentic payments", "fintech", "payments", "authorization", "prompt injection", "AI safety", "human in the loop", "product design", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Stop Making Your Customers Click Approve - Emil Chetty, Wise

**Emil Chetty**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Emil Chetty` `#Wise` `#AI agents` `#agentic payments` `#fintech` `#payments` `#authorization` `#prompt injection` `#AI safety` `#human in the loop` `#product design` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=V2UqEUA8NjM) · [Conference site](https://www.ai.engineer/)

## Description

Emil Chetty, who leads data and AI product at Wise, argues that AI assistants have turned customers into an approval queue. Wise moved $243 billion across borders last year for nearly 19 million customers under more than 80 licenses, so every payment needs proof of what the customer actually authorized. His answer: the customer agrees to the whole job once, as a locked agreement; the agent chooses the steps; and Wise's existing payment software enforces the terms, so even an agent tricked by a prompt injection can't pay a new recipient.

Chapters:
0:00 Intro
0:58 About Wise
3:00 Regulators still expect answers
3:36 A typical agent job
4:05 Approving every step
5:06 What coding agents learned
5:35 Safe action vs. authorized payment
6:42 From intent to a locked agreement
8:15 A worked example
10:27 Granting only what was approved
11:32 Retries and changed quotes
12:35 How it's built
13:25 When the agent gets tricked
14:18 What Wise can answer for

Emil Chetty

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,478 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=1s)** [music] >> Anyone here ever get tired of clicking approve on their coding agents, giving ChatGPT the permission to be able to scrape that websites, or even just giving Hermes the ability to be able to read your the MCP that you definitely told it it's a lot to read? Anyone in the room get annoyed? Sure. Now imagine that was the experience every time you were using an assistant that promised you to save you time, reduce the complexity in your life, and ultimately provide you value. Everyone in this room, the AI evangelists of the world, we promised

**[0:50](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=50s)** our normies are sitting outside this room the an assistant, something that's going to reduce the complexity of their lives. But instead, when it hit reality, we ended up providing them with a queue of requests. So, hi. I'm Emil. Um I lead um data and AI product at Wise. And I'm going to be talking you guys through about how we're thinking about removing that complexity for our users, and trying to give an agent useful autonomy without making our customer the API. So, for those of you who aren't familiar with Wise, um which I suspect some of you might not be given the US-based audience, um we're a technology company that's building the best way to be able to move and manage the world's money. We have this vision of achieving money without borders,

**[1:39](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=99s)** and making sure that people can manage their funds and lifestyle across multiple geographies and currencies. To do that, we've built three products. We've built the Wise account, and that's [snorts] helping regular people manage their life across borders, helping them spend like a local, and save like a local. The second is Wise Business, which allows businesses, small and medium-sized, to be global from day one. And the last is Wise Platform, which allows banks and other financial institutions to tap directly into the payments infrastructure that we've built over the last since 20 11, and provide a Wise-like experience directly to their customers. And to do this, we've built one single global payments network powered by over 90 different local banks

**[2:26](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=146s)** and payment providers from across the world, and connecting directly into domestic payment schemes. And that network has proved really effective. Last year, we've moved over 243 billion in cross-border in cross-border volume, and we're serving over just nearly 19 million active customers. So, we know this this model scales. And to be able to do that, we hold more than 80 different licenses worldwide. And that has meant that in different currencies, different countries, different regulated entities, and different products all bring different requirements. And that doesn't disappear when we put a chatbot in front of it, unfortunately.

**[3:14](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=194s)** Our regulators still expect us to know what a customer is authorized, control what happens to their money, and explain the outcome. So, how can we give an agent useful autonomy that is actually going to simplify our users' life, and still answer for what it does? So, here's what a typical job might look like that we might give to an agent. So, some small business owner might say, "Handle this week's approved payment suppliers, reconcile the results, and bring back the exceptions to me." The business wants the work handled. They don't want to coordinate every lookup. They don't want to coordinate every status check. And they want this to ultimately provide them with the ability to focus on what matters most to them, running their business. So, how do we So, how are we going to

**[4:01](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=241s)** about achieving How are we going about achieving this? This might look very familiar to you if anyone's using agent relatively recently. You will have list of different approved steps. Checking whether or not you are can look up there the payment account details, checking whether or not you can scan a PDF in to be able to understand the the invoice, etc. etc. Took eight steps, probably some time in between to be able to get to something that was ultimately small. And so for the engineers in the room, this might look relatively familiar, right? In the If anyone can remember the before times and if you weren't using dangerously skip permissions, this is what coding agents used to look like. We have to go through and approve every step while watching the terminal, check your run your tests, sure,

**[4:50](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=290s)** fetch that face first lady documentation from Confluence, sure, and click approve all the way through. We ended up having to watch the terminal instead of getting real work handled. >> [snorts] >> We ultimately made the human the API. So how did co-coding agents solve this? Anthropic came up with this idea of auto mode, right? And that meaningfully reduced the friction that we experience as engineers. Permission rules, classifiers, sandbox helped be able to introduce controls necessary for us to be able to trust the agent wasn't going to go delete our production databases. These controls matter. But a payment needs a different kind of answer to a different kind of question. Well, a coding agent is asking, "Does

**[5:37](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=337s)** this action look safe?" What a payment is asking is, "Did this customer authorize this payment to this recipient on these terms?" So again, we're at an AI conference. You might say, "Cool. Let's Let's chuck some eval's at it." For those of you who are on the bleeding edge, let's say we can build a harness to be able to do this and embed the controls inside the harness. But unfortunately, it doesn't give us the answer to whether or not the customer actually agreed to this job. What we need is an agreement. We need something immutable that a customer has agreed to that allows the agent to operate from within those bounds. I'm not saying we don't need the emails, we don't need the harness, we're still

**[6:23](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=383s)** going to need both. But what we don't want is that the model said this is what the customer wanted and authorizing that payment based on that. We want them to agree to the job, not every step. So, how we how are we thinking about this? So, the idea is we want to be able to go from intent to something that is immutable. So, we want something to be able to take that take the vague customer a prompt that we have, ingest that, have trusted verified software that we've built that we spent the last 25 years building, verify it, and show the customer a particular outcome, and have them confirm whether or not that is the bounds by which they want the agent to be able to operate

**[7:11](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=431s)** within. We can then take that, embed that into our trusted the our trusted stack, and provision the authority based on what the customer agreed to. The agent can then plan and act as usual. Our services, which are actually executing that payment, can then check whether or not the the payment should be executed on. And the results and exceptions can get surfaced back to the user. If something needs to change, and that changes that fundamental agreement, we surface back to the user. But if the if something is changing that's not going to affect the payment terms, we can still go back and have the agent re-plan. So, a different plan can still stay within side that agreement.

**[7:58](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=478s)** Different terms ultimately need a revised proposal and a customer decision. So, we need the customer to agree to the job, the agent to choose the steps. And our software to enforce that agreement. So, let's take a hypothetical example. Let's say Sarah, our business owner from before, sends this off to an agent. What does this ultimately look like? So, first, we take Sarah's credentials, and we take the the all the setup that Sarah's had, and we go gather the context necessary to be able to propose a job. So, first, the agent explores with limited read-only access all the information necessary to be able to close that loop. The trusted software that we've attached to the account actually resolves the

**[8:47](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=527s)** suppliers, the bank details, the amounts from those records. And this preparation doesn't actually give the agent permission to be able to execute anything meaningful. We then surface that to Sarah. And here's the job that she'll see. She'll see this is the thing that we want to be able to do. This is like the three suppliers, $775 with around like some for the fees that she might have to pay. And this is the draft that she will see. What also gives What's also important is the balance in which the agent is able to operate in. So, the decisions that she's comfortable offsetting to the agent versus the decisions that she wants to be able to be um looped back into. Any missing or conflicting details need to be resolved before the before before the job gets um made immutable. And so, what this means is we have two

**[9:37](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=577s)** views of that job. One is the thing that Sarah sees, which is the is the promise that we're making in human language. The second is what our services can see. And that's ultimately a machine-readable promise that we're making that allows our services to be able to verify that this payment is a is is operating within a specific set of bounds, and gives the agent very specific instructions in which to operate within those bounds. And so, when she clicks approve, that then becomes immutable. She confirms and authenticates, and her decision is recorded against that exact version. And that draft becomes an authorized job. What you approve is ultimately what we enforce. And that's how we're thinking about reducing the complexity.

**[10:25](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=625s)** So, what happens next? So, we take that we take that confirmed job, and we give a trusted provisioning platform the ability to be able to provision access purely based on what's been approved. The code deterministically checks three things: the confirmed job, what wise permits the agent to do, and Sarah's current rights. And we look at the intersection between those, as long along with what the job has proposed to be able to provision limited access rights to an execution agent. Those then split out into two workers. One is a payment worker and a reconciliation worker. And those are what is going to be able to actually execute based on that job. This still allows the plan to be able to change.

**[11:12](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=672s)** The agent is still deciding how to best achieve the job that has been provisioned to them. What does What doesn't is the agreement. And so, the flexibility that that we promised, the ability for a customer to be able to delegate the job instead of supervising that implementation, still remains. So, there's fundamentally two different loops, and this gives us some element of resilience here, right? So, let's say um the job needs to be retried for whatever reason. A Kubernetes pod needs to be restarted, and then the job or the app crashes on her phone, and she needs to be able to restart that job. Given that that job is immutable, and we're sharing that payment state, it's on a second payment. Services will share the ability to be able to um execute that payment, but also be able to look up what has already been

**[12:00](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=720s)** executed. And so, the worker follows the existing payment job rather than creating another one. However, if they discover that a quote has changed later on, or quote might have expired, service that back to Sarah cuz she wants to know. Sarah approved that specific quote and the agent then will prepare an updated proposal but can't approve the replacement itself. And so we control Sarah what's changed, get her to agree to a new version. And within that arrangement, the agent still keeps working. So it's a rough like sketch of what we're trying of what we've done on a white so far is we have like our different gateways that ultimately allow for the provisioning of these agents and also the ability to be able to have that

**[12:47](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=767s)** immutable job be it be be verified against our We have the very controlled routes to our LM providers and we have an agent gateway which ultimately provides mechanisms for our tools to be able to be registered but also be evidenced. So we follow that one payment through the gateway. The worker checks what what tools it can use. Executes that against the payment surface. And make sure that the bounds mode they're operating within still comply with the promise we made the user. That immutable job record. But let's say there's some nefarious actions happening, right? So suppo- suppose we get prompt we get it get it gets prompt injected somewhere and the

**[13:35](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=815s)** an agent says pay our payment details is updated. And let's actually say that the agent actually believes it, right? It's belief itself can't change the confirmed job. So the new PA fails when the at the service check. And the agent can't rewrite its own agreement. So the boundary doesn't actually depend on the model spotting the scam. It depends on our downstream services supporting the ability to be able to check those but also enforcing on what we agreed. So the software stack that we built over the last since 2020 since 2011 is still the one that we're going to be relying on and it's still the one that's going to be remaining compliant for all of the orders in the room. So, what can we answer for? We know who authorized the job.

**[14:24](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=864s)** We know what the agent can do. We know what happened when that payment went through. We know what we can stop. We ultimately know who who is responsible. And we know whether or not it's doing good work. And so, that one chain of evidence, we get everything we need to be able to allow for our customers to be able to reduce the complexity when using agents, but still make sure that that money is safe. So, there's one thing I want you to take away from this. If you want to introduce a new approval flow, if you want to introduce a new agent into your like into your stack, get the customer to agree to the job and delegate it out. Allow your agent to be able to choose how it wants to execute that job. Allow your services to be able to enforce that agreement.

**[15:12](https://www.youtube.com/watch?v=V2UqEUA8NjM&t=912s)** And that way, Sarah doesn't have to worry about needing to approve 100 different steps. So please stop making your hu- humans your agency API. Thank you. >> [applause]
