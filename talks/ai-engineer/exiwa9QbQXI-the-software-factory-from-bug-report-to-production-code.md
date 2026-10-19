---
id: exiwa9QbQXI
title: "The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory"
slug: the-software-factory-from-bug-report-to-production-code
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Davis Palmie"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-07T20:00:04Z
video_id: exiwa9QbQXI
url: https://www.youtube.com/watch?v=exiwa9QbQXI
youtube_url: https://www.youtube.com/watch?v=exiwa9QbQXI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "software factory", "AI agents", "agentic engineering", "Factory AI", "Droids", "SDLC", "agent readiness", "AI governance", "developer productivity", "model agnostic", "AI coding", "engineering metrics", "Davis Palmie", "AI engineering", "AI Engineer"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Governance, ethics & regulation"]
transcript: true
---

# The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory

**Davis Palmie**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#software factory` `#AI agents` `#agentic engineering` `#Factory AI` `#Droids` `#SDLC` `#agent readiness` `#AI governance` `#developer productivity` `#model agnostic` `#AI coding` `#engineering metrics` `#Davis Palmie` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=exiwa9QbQXI) · [Conference site](https://www.ai.engineer/)

## Description

Engineers are going from typing code to governing agents. The next step is a system that turns bug reports into production code.

Davis Palmie, member of technical staff at Factory, explains the software factory: a system of agents that takes input signals like bug reports and user feedback and turns them into production code. He covers the questions every leader asks, from runaway costs and model choice to what happens to engineers and org charts, and argues coding was never the bottleneck: review, debugging, docs and testing are. He lays out the principles a factory needs (model-agnostic, sovereign deployment, integrated across the SDLC, available on every surface), why to start with something narrow like incident triage, and Factory's eight pillars of agent readiness. He closes with why token leaderboards are Goodhart's law in action, and the outcome metrics to track instead.

In this talk:
• What a software factory is, and why coding was never the bottleneck
• Model-agnostic, sovereign and SDLC-wide: principles for a factory
• Agent readiness: eight pillars that help agents and engineers alike
• Metrics that matter: signal-to-production time, interventions, cost per PR

SPEAKER
Davis Palmie, Member of Technical Staff, Factory
X: https://x.com/davispalmie

LINKS
Factory: https://factory.com
Factory on X: https://x.com/FactoryAI

CHAPTERS
0:00 Intro
0:57 Three eras of AI engineering
1:42 Climbing the abstraction ladder
2:07 From typing code to governing agents
2:52 Question 1: cost overruns
3:36 Question 2: access to the best models
4:06 Question 3: what happens to engineers
4:31 Question 4: the organization
4:56 Coding was never the bottleneck
6:21 What a software factory is
7:16 Start narrow: incident triage
8:11 Principle 1: model agnostic
9:00 Principle 2: sovereign deployment
9:25 Principle 3: integrated across the SDLC
10:00 What it looks like in practice
11:20 From O(n) to O(1)
12:40 Agents on every surface
13:35 Agent readiness: eight pillars
14:44 Governance and incremental rollout
15:29 Humans still set direction
16:29 Measure outcomes, not tokens
17:09 Metrics that matter

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,292 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=exiwa9QbQXI&t=1s)** [music] Hey folks, I'm Davis Palmy, a member of technical staff here at factory. Uh before this I co-founded Lummetric which was an agent platform for investment teams that we took through Y Combinator and was acquired by factory and prior to that I was a engineering lead for Slalom's innovation lab. So I've seen AI deployments both across large enterprises and more AI native orgs. With that in mind, today I'm going to be talking to you about the software factory and how you can move towards an autonomous system that translates input

**[0:51](https://www.youtube.com/watch?v=exiwa9QbQXI&t=51s)** signals into production code. So, first we've moved through three distinct eras of AI engineering. First, we had tab autocomplete, next token prediction, and the engineer was still firmly in the driver's seat. Then AI could generate entire files and the software engineer became a bit of a discerning copy pastaster. Um, but they still heavily had control over the output of the AI. And then you had agents that were more tightly coupled with the code. They could gather their own context, call tools, and debug their own output. Now, autocomplete used to feel magical, and now at best it's it's a quaint thing we remember. You want to

**[1:40](https://www.youtube.com/watch?v=exiwa9QbQXI&t=100s)** look at the speed at which AI engineering is climbing the abstraction ladder from tokens to files to context now to entire systems. Every shift you have here is an adjustment. But each move up the abstraction ladder has made engineers more valuable, not less. And so now we're at a transformational point. Engineers are going from typing code to governing agents and eventually you'll organize those agents into a system. That's your software factory. So with this the engineer's role shifts to keeping guard rails tight, catching code drift

**[2:27](https://www.youtube.com/watch?v=exiwa9QbQXI&t=147s)** and setting the highle priorities and direction. But meanwhile, the system is ingesting input signals like bug reports or user feedback and outputting production code. So if you have AI systems that are producing more code than humans, there are some big questions that everyone is rightly asking. First, how can I prevent massive cost overruns? We've all seen the headlines about Uber's CTO blowing through the years, AI budget by April, or Microsoft clawing back clawed code licenses to try and cut down on spend. At Factory, you're not locked into a single model provider. And this means

**[3:15](https://www.youtube.com/watch?v=exiwa9QbQXI&t=195s)** you unlock the entire spectrum of cost performance with LLMs. You want the maximum uh cost efficiency and the minimum effectiveness necessary for each task. As our CEO likes to say, uh if your kid needs a algebra tutor, you can definitely find someone cheaper than Albert Einstein. Second point, how can I ensure the best access to whatever model is top right now? Well, we think that having to back the right horse is a false choice. Um, especially with the increasing effectiveness of open source models. We're strong proponents of being able to choose the right tool for the right job or even now have it dynamically routed.

**[4:05](https://www.youtube.com/watch?v=exiwa9QbQXI&t=245s)** Number three, what happens to software engineers? What does the future of software engineering look like? Well, the role is obviously evolving and the line between product and engineering is blurring. Engineers will now build and maintain the system that's responsible for building your production code and they'll set the highle direction for the software factory. And lastly, how is this going to change the organization? Well, team boundaries are also starting to blur and context needs to flow seamlessly across these boundaries. Information can't be siloed. That was true for humans, but it's especially true for AI agents. Everyone across all your teams will have a shared

**[4:55](https://www.youtube.com/watch?v=exiwa9QbQXI&t=295s)** responsibility for the pillars of the software factory. Now, coding was the easy part. This actually was never the bottleneck. Your context is laid out in natural language. I bet if you look at your real engineering metrics, what's the median time to review a PR? How long does it take you to reproduce user bug reports or go through and debug code? Who keeps your docs current with every PR and who keeps it current with every strategy meeting? Who maintains your test suites? oftentimes the testing teams and the engineering teams and the product teams are each on their own continent. If you pull your dora metric, the time from code written to time in

**[5:42](https://www.youtube.com/watch?v=exiwa9QbQXI&t=342s)** production, I would bet dwarfs the time actually making those engineering changes. The real need you have today is cohesion across all of these surfaces. Right now, docs will go stale, dead code lingers, and there are so many layers of communications between your different teams. Again, this is hard for human engineers, but it is especially more pronounced for agents. The necessary undertaking to build your factory is to make sure the agents can bridge all of these services and understand the nuance within your organization. So this brings us to the software factory which is the system of agents that will take you from input signal to

**[6:33](https://www.youtube.com/watch?v=exiwa9QbQXI&t=393s)** production deployment. Your agent's not just coding anymore. It's taking on customer support, product engineering, deployment ops, and many other roles. Across these pillars, your agent should be triaging incidents, making plans, creating and updating docs, actually executing the code, reviewing it, testing it, rolling it out, and then monitoring that release. Now, that's obviously a ton of work, and you don't want to jump into that all at once. For one, it's too heavy of an undertaking, but for two, your teams will not have time to build trust in this system. You want to start with something narrow and verifiable like

**[7:23](https://www.youtube.com/watch?v=exiwa9QbQXI&t=443s)** incident triage. Let your agent read a sentry alert, pull the traces in other context, and then post in Slack. But keep it so your engineers can review this and decide what to do. And as more correct diagnoses roll in and in from the agent, your team can start to build trust and an understanding of this pillar. So each step in the software factory needs careful ownership and monitoring before you even think about letting the the pipeline loop. But once you can tie the output of this system back to the input signal, that's when you unlock organizational self-improvement. Now we feel pretty strongly that your software factory should have a few key

**[8:13](https://www.youtube.com/watch?v=exiwa9QbQXI&t=493s)** principles. First, it should be model agnostic. Obviously, different models excel at different tasks and with very different cost efficiencies. We found, for instance, that you can achieve the same performance on code review with GPT 5.2 as with the latest Opus models, but at half the price. And now if you look at the open- source alternatives that can slash your cost down to 10 to 30x cheaper. So at factory again you have the entire interplay of speed to task efficacy to cost. Not being locked into a single lab means you unlock the entire PTO frontier of LLMs. Now number two your deployment model

**[9:02](https://www.youtube.com/watch?v=exiwa9QbQXI&t=542s)** should be sovereign. You shouldn't have to compromise on your security architecture or your policies to try and fit your AI deployment model in. Now at factory you can choose your workspace and your deployment model. We support everything from fully managed to bring your own machine to entirely airgapped. And number three, your software factory needs to be integrated across the SDLC. These are no longer separate uncoupled concerns. Docs changing should inform your code and vice versa. Planning goals should inform what you test for, not however many communication layers there are between strategy, product, engineering, and your testing teams.

**[9:50](https://www.youtube.com/watch?v=exiwa9QbQXI&t=590s)** Each one of these pillars supports the software factory. And weakness in one means a weakness in the entire system. So tactically in an AI native or what does this look like? Well, we typically see it as the fusion and the incremental automation of many sub teams under the umbrella of one software factory. Some really common patterns we see are triaging incoming signals like sentry alerts, having the agent make diagnosis before the human can even answer the page. Proactively testing security, scanning for secrets or vulnerabilities. Creating, maintaining your tests,

**[10:41](https://www.youtube.com/watch?v=exiwa9QbQXI&t=641s)** monitoring the ones that are becoming brittle or unneeded. Again, keeping docs in sync with code. keeping docs in sync with your different meeting channels and then the classic reviewing code, commenting on PRs, rollouts, monitoring releases and with the agent doing all of this, the human engineer's role shifts to responding to exercising judgment and correcting the AI in such a way that it can learn from these mistakes. Now everything is transitive across sub teams. An improvement to one group means an improvement to the entire system. So why should your enterprise care about a software factory? Well, the larger and

**[11:31](https://www.youtube.com/watch?v=exiwa9QbQXI&t=691s)** the more fragmented you are, the more you feel the linear pain of managing teams. In tech terms, your software factory should take this pain from O of N to O of one conservatively. You can define your guardrails, your agents, your docs, testing policies, really governance just one time and then standardize it across the organization. And this standard should make sure that everyone is pulled to the highest bar, not the lowest common denominator. Now also if agents can move across these surfaces then they can hold that quality bar across teams without you having to linearly scale your time to manage each

**[12:19](https://www.youtube.com/watch?v=exiwa9QbQXI&t=739s)** one. And if agents are moving across all these services then you have one place where context can be unified and you can have executive visibility into how the entire SDLC is performing. Now, just like model agnosticism removes lock in, your agents should also be surface agnostic. They need to be highly available to your teams. Regardless of what tools they use, your teams should not have to compromise on their processes or their tooling to try and fit your AI provider in. At Factory, we have agents available everywhere from remote machines to the CLI to Slack, any tool your teams use. And even though

**[13:08](https://www.youtube.com/watch?v=exiwa9QbQXI&t=788s)** humans and agents may use different services, everything should share the same underlying harness and context. So the undertaking of building the factory will expose tribal knowledge, manual processes, and outdated info. Unblocking these is not only going to help your agents, but it's also going to help your engineering teams. At factory, we have the concept of agent readiness and we evaluate this based on eight pillars. The first is validation. Do you have guard rails like llinters and formatterers in place? Then your build system. Are your build commands and CI well documented?

**[13:56](https://www.youtube.com/watch?v=exiwa9QbQXI&t=836s)** Feedback loops. You have unit and integration tests tight and you have docs like readmes, agents.mmd files. Are your dev environments cleanly reproducible such that an agent can use them? Is your code modular with clear boundaries and rules against sprawl? Do you have observability? How long does it take you to find out why something went wrong? and are you proactively security scanning so that you don't have to worry about leaked secrets or vulnerabilities. Basically, the key takeaway here is that if your agents and your human engineers are going to walk the same roads, paving them well is doubly useful.

**[14:45](https://www.youtube.com/watch?v=exiwa9QbQXI&t=885s)** Now, you can't govern what you can't see. And that's true for agents and human engineers. You can start with this agent readiness assessment, but no matter what, your engineers must monitor agent performance and control behavior. At factory, every action is auditable. It operates under your standards with role-based access control and least privilege. For example, your teams that are building this software factory need to first build trust and understanding. That's why you should roll this out incrementally. You want to automate the individual pillars first before you turn this system into a loop. And again, precise execution

**[15:35](https://www.youtube.com/watch?v=exiwa9QbQXI&t=935s)** does not prevent poor design. It never has. You still heavily need humans in the loop for architecture, for strategy, and for setting direction. Engineers will not be replaced, but judgment and prioritization now beat mechanical implementation skill. Agents won't be able to handle everything. There will be guardrails to tighten, code that drifts. Humans need to stand as validation gates in this factory. But just like we don't have to feed punch cards into the machine anymore, code does not have to be written by hand. Your team should be able to set the strategy and their risk parameters and then let agents execute. And knowing if your agents are executing

**[16:27](https://www.youtube.com/watch?v=exiwa9QbQXI&t=987s)** well comes down to measuring the right things. Basically, you want to measure outcomes, not tokens. Lines of code and tokens generated are gameable metrics. These are not actually associated with outcomes. Token leaderboards at big companies just encourage proflegate spending. It's goodart's law in real time. If you decide to measure token usage, engineers are going to optimize for token usage and then it's no longer a good metric. It's not about who spends the most on tokens. It's about who can get the highest leverage outcomes from that spend. Some metrics that we like at Factory are signal to production time, human

**[17:17](https://www.youtube.com/watch?v=exiwa9QbQXI&t=1037s)** intervention count, median time to repair, shelf life of code, and cost per PR. These are real tangible outcomes. So agent readiness is really a precursor to effective engineering. Whether it's an agent or a human that ends up in that system, your agents need the exact same careful governance as your engineers, tooling, access levels, systems for review. Don't just turn them loose in your codebase. And don't token max. Measure what actually matters. Your end users don't care about how much you're spending on AI. They care about

**[18:08](https://www.youtube.com/watch?v=exiwa9QbQXI&t=1088s)** feeling the dramatic improvements that will come from your software factory. Thank you. >> [music]
