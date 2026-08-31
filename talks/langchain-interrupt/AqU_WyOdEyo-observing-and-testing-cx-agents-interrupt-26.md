---
id: AqU_WyOdEyo
title: "Observing And Testing CX Agents | Interrupt 26"
slug: observing-and-testing-cx-agents-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 23
published_at: 2026-06-10T12:59:00Z
video_id: AqU_WyOdEyo
youtube_url: https://www.youtube.com/watch?v=AqU_WyOdEyo
tags: []
transcript: true
---

# Observing And Testing CX Agents | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=AqU_WyOdEyo) · [Conference site](https://interrupt.langchain.com/)

## Description

At Interrupt, the agent conference by LangChain, Carlos Pereira from Cisco's Customer Experience team showed how you close the loop between production feedback and code at 16 million customer interactions per year.

The core problem with scaling agents: once adoption climbs, feedback volume outpaces your team. Every thumbs down, every confused user, every low-confidence routing decision is a signal. If you treat it as noise, or if your team becomes the bottleneck processing it, adoption drops. This talk walks through the system Cisco built to take a user's thumbs down all the way to a merged PR, with AI handling triage and diagnostics and humans in the loop only where decisions matter.

Observing And Testing CX Agents | Interrupt 26
0:00 Introduction and Day 2 context
0:49 What today covers: observability, testing, and support
1:11 Cisco support at scale: 16M interactions per year
1:34 When network outages hit: why this matters
1:54 CX methodology and team structure
2:16 Evolution: from chatbot to autonomous teammate
2:51 Today's question: closing the production feedback loop
3:23 The approach: continuous feedback loop, not a ticket queue
4:11 Every signal matters: thumbs down, errors, and confusion
4:41 Why humans become the bottleneck at scale
5:57 Signal capture via LangSmith traces
6:12 Triage agent: LangSmith MCP and Jira MCP in practice
6:55 Code agent: clustering and diagnosing issues
7:35 Human in the loop: only on writes, not reads
7:56 Proactive and reactive feedback pipeline
9:20 Treat evals like tests, not experiments
10:56 MCP as the integration layer
11:21 Human oversight only on writes
12:47 Lessons learned
13:53 Observability is your new bottleneck
14:05 Close the feedback loop with agents
14:36 Evals are infrastructure, not a side project
15:34 Support use case: Cisco technical support
15:48 Live example: enterprise network assessment
17:04 2,176 security findings: where do you start?
18:13 Semantic routing for ambiguous prompts
19:33 Parallel pipeline with guardrails
20:55 Tracing every step with LangSmith
21:36 Self-learning routing system
21:54 Observing LangSmith itself with Splunk
22:22 Closing

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/

## Transcript

*3,687 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=5s)** Good morning, everyone. Good morning. Welcome back for the survivors, for the ones that actually made the second day. That was actually awesome on the demo they're doing today. So we have been using a lot while they're sharing, and some of this is running in production. So day two, my name is Carlos Pereira, for the ones that were here yesterday. We talked about renewals and building agents. Today, we're going to talk about how we went and built the observability and the testing for that. Just one observation. In addition to myself, you have Vince, Amman, John, and Thomas on our booth out there. A lot of people came to understand the details. That is so much I can pack in 20 minutes. Over there, we have all the workflows, how we did the planning yesterday, and all the coding for this, so if you want to check it out. So with that said, I'm going to, for the benefit, for the ones that will watch this

**[0:58](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=58s)** later over on YouTube, explain what customer success is in a minute. And then deep dive on what is the teammate for renewals that we did yesterday, what the observability and the testing looks like, and then we'll cover support. Support at Cisco is an interesting beast. We have an average of 16 million interactions a year, and the amount of tickets and cases last year was 1.6 million, this year is 1.4. So we increase a lot of the deflections, and thanks to some of the systems that I'm going to show you. And also, we are more proactive with customers. But think about Cisco. We have network and security. So when they have a network outage, people really get upset. And there are a lot of things that don't work, pretty much everything, if the network is down.

**[1:46](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=106s)** So when you have those cases, we sometimes have catastrophic outages that bring business down. So how do we deal with that, and how do I use agents for that? So in a nutshell, we have customer experiences, same methodology as the industry, land, adopt, expand, and renew, which covers the teams that you have, Cisco Customer Experience, around a 19,000-person organization. We talked about the renewals team yesterday, and the teammate that is now in agentic fashion belongs to that team, and we're also going to cover technical support today. So with that said, the renewals team, as we mentioned yesterday, we evolved from the initial agentic foundations that we built last year. That was more about how we earned the trust and how we get an interface on a chatbot to now have running in production a workflow-based approach when you bring the notion of delegation where the agent teammate can be part of the team and

**[2:40](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=160s)** has authority to act, and you have proof of value. So that was yesterday. For the ones that are watching on YouTube, I recommend you to just watch the YouTube video for yesterday's session. But the question of today is: how did we close the loop between the production feedback that is running at scale and make this into code for fixing, using AI and agents for that? How do we observe in the case of support and actually build a semantic routing, because I run around 10,000 cases at the same time, so there is no way a human is going to be able to fix all of this at the same time. And how observability can become your enabler, but also your bottleneck if you don't watch it carefully. So let's go for that. So, from yesterday, we learned that we built a very nice chatbot interface,

**[3:30](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=210s)** 95-plus percent accuracy, multi-step agentic, all the deterministic RBAC, all the things that were right. And then I told you that people plateau on utilization, they ghost us at some point. So I explained to you, part of this was optionality that we give them, and then we remove with the forced curiosity kind of thing. And another one was building a teammate with more autonomy and give them more personalized and more ability to automate. So we went from low usage to usage climbing up. With that comes an avalanche of feedback now. Good problem to have. So everything is now a signal. Not noise.

**[4:17](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=257s)** When I put something out there, and there is a thumbs down or a feedback, this is a signal. It's not something I can ignore. Because otherwise, what cleans up as an option is going to clean up the feedback. "Those idiots don't know what they're doing." So every thumbs up is a lead. Every trace with an error is a potential regression. And every confused user is a description of a gap that needs to be addressed. Think about it. The human becomes the bottleneck, because the same agent team that built the teammate cannot scale for thousands of thumbs down and thumbs up at the same time, which means triage becomes very important, clustering things, understanding false negatives, false positives, and all of this. And last but not least, the real question is, what is the shortest path for me to get a user's thumbs down

**[5:09](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=309s)** as a feedback or a comment to actually become a merged PR, the pull request, without losing quality and with human oversight. Right? Let it sink for a second. Your success on observability is proportional to how much you'll need to deal with here. I know it's early in the morning, but you need to wake up. OK, let's keep going. So how do we build that? We actually created not a ticket queue system. We went for a continuous feedback loop where we use the production signals and the flow of them, particularly with LangChain, directly into code changes with AI doing the heavy lifting and humans in the loop where it matters. So here is how we approached the problem.

**[5:58](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=358s)** First thing, we actually built an agent to capture the signals. So all thumbs down, all the errors, all the low confidence classifications, everything, we have production traces that we capture via LangSmith. And then we built the triage agent. What the triage agent is, is basically a deep research agent that runs in a browser, it leverages LangSmith's MCP and Jira MCP, and does analysis and diagnostics of the code, and has the ability to open Jiras. Let me give you one comment. I would compliment Ankush and his team on LangSmith, because LangSmith's MCP is absolutely awesome. It's not like an API that people wrap in FastAPI and call it an MCP, where the worse the API you have,

**[6:46](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=406s)** the worse the MCP interface becomes, and then the AI gets all confused because of that. LangSmith's MCP is really, really good. I recommend you use it. So you leverage this, and everything becomes part of the triage agent which then feeds a coding agent. Realize that we have them as two separate tasks. I will explain the UI in a second. And the code agent does deeper diagnostics. It analyzes what the fixes would be. It clusters similar signals that belong to the same domain. I don't want to open 50 Jiras for the same potential bug, right? If I can cluster them, I have one. So it does all the failing traces analysis. And then for review, we have the human in the loop. The human approves. The human redirects or ends it. The human is responsible for the PR as it relates to writing.

**[7:36](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=456s)** Everything that is reading is done by AI agents. And then last but not least, we merge the PR and ship the fix to the code. And that fix is a new evolution in itself. So you don't just say, hey, we fixed it today, nice, pat on the back, move on. No, it feeds itself as part of the evolving ecosystem. And we look at this from two angles, a proactive and a reactive. The proactive is what I have on that bottom side, which is turnkey evals before we ship any agent. We have the data subject matter experts. And by the way, I didn't build this material together with Harrison's team, but you can see a lot of analogies in what they said before. We have this implemented in production at scale already. So we have the data SMEs that validated the routing,

**[8:26](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=506s)** used the LangGraph routing as I mentioned yesterday, create the regression tasks, ship them safely, which we are trying to prevent issues before they can potentially happen. But then, when you have this running in production, the customer may say, hey, that answer is not what I wanted. It's not accurate. It doesn't fit. So they leave feedback. Thumbs down, there is an error or a comment. So we need to deal with that. That's where triage agents and the code agents come in. And after an agent ships, the real feedback gets triaged and we address it. So this is the methodology that we use. It runs in production at scale, which is the key for us. I don't know how many users are going to use it at a given time, and my team is very small. So there is no way I'm ever going to counterbalance with a human approach. Let's go a little bit into the triage agents.

**[9:14](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=554s)** So I get a thumbs down as an example of people giving feedback. And that thumbs down can be just a thumbs down as a signal, or with a comment: hey, I don't like it. It's inaccurate. It doesn't serve my purpose. It doesn't fit my business. Whatever that is. So we fetch that trace, we read the code that actually maps to that trace, we put it through a classifier, and we route it to Jira. So what does it do? In production, it pulls the traces from LangSmith over the next X amount of hours. We can define what X amount of hours are, and then it filters the thumbs down errors or low confidence routing, and reads the related code to understand what the agent was trying to do at that given time. For that particular set of traces, what do I mean by set of traces?

**[10:02](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=602s)** Because you have the agent clustering the ones that are similar, because we don't want to, first, open a bunch of them that could be correlated. Second, we need to decide whether this is a false positive or not. The person may be having a bad day, or they don't understand that answer, or maybe it was an authentication error, and that person shouldn't even be in that environment, which is still something you need to trace. And we only open a Jira when there is something to fix. And how it is built, as I said, we use the LangChain deep agent library for the harness and structured system prompts that define the boundaries, the tools, and the heuristics for the triage. And we decompose those triages into explicit steps with sub-agents that go from coding

**[10:52](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=652s)** and actually finding the duplicates in the cluster. It's important. I'm talking about thousands at the same time. We need an agent that actually correlates them and says, hey, you're dealing with three problems, 10 problems, not a thousand problems. So a thousand Jiras, the whole thing gets out of control very quickly. And LangSmith's MCP we use for traces. Jira MCP we use for issue creation. So we have separation of concerns very clearly. So think about it like that, because if you start to mix domains, the context starts to get messed up, and the AI that's helping you loses context and loses the boundaries. And every action is traced, including the triage itself. So it traces itself, so it traces what the trace is doing,

**[11:41](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=701s)** and you see more of that behavior. What made it work? There are four things worth highlighting. First please please please if you want to get this in production at scale, treat evals like tests, not like experiments. Let me repeat it again. Treat evals like actual tests as part of the pipeline, not experiments. Evals live in the repo, not in CI, not in Slack messages, not on the PowerPoint that is shared to your boss, none of that. Do component-level analysis and end-to-end analysis as well for the triage, both. Not just: hey, I did a component test, it looks good. And then end to end, it looks bad. Datasets are versioned inside the code,

**[12:31](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=751s)** not on the dashboard. Dashboards are for the bosses to look at. The agents don't care about the dashboards. I'm making a joke, but you realize what I'm trying to say, because it's very realistic in real life. MCP is our integration layer. Agents talk to LangSmith, to Jira, to Git, and run the evals through MCP. It matches what Harrison just said before. We just have it running in production for some time already. Swapping the backend without touching the front end is only possible if you use MCP as the interface layer. It gives you the decoupling and flexibility to play with. The same MCP tools now become what powers your UI, powers the IDE.

**[13:17](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=797s)** You saw that in the demo before, the triage agent, and so on and so forth. And last but not least, as I mentioned before, human in the loop only on writes, not on reads. Everything like reading traces, opening Jiras, drafting the pull request, all of that is autonomous. What I mean by autonomous is: you give authority to the AI to do that. You give authority for the AI to act. You set the boundaries. Everything that involves writing, the human is in the loop. So the goal is to leverage, not to replace. So some lessons learned. Observability is your new bottleneck. If you're going to ship agents, and you're going to ship them at scale, look at my smile, observability is going to be your trouble. Just embrace it. Second, close the loop with agents. So you have the feedback and you want to fix it.

**[14:08](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=848s)** In between, you can have triage, you can have diagnostics, you can have a PR. Use the agents to help you do the work along the way. Keep humans only for the decisions. Don't fall into the trap of a human-orchestration-based system, because it's not going to scale. When you get successful and you get adoption, that's where you get feedback. You want that. And if you become a bottleneck on your feedback, your adoption is going to fall. Third, evals are part of the infrastructure, not a side project. Every fix that we do generates a new test. If you think that way, the test suite compounds. And regression becomes a permanent thing. It's not an exception. And as you think about using agents for this, shift the agent authority to the left,

**[14:58](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=898s)** which means the data subject matter experts, which aligns to the demo that was done before, ship agents with the routing guarantees, which means the subject matter experts in a particular domain, in my case renewals, in your case it's going to be whatever runs in your business, they know better what the answer should be. The coding folks that are building the agents and the PRs have no clue. So the subject matter experts are the ones that are defining the routing that is embedded in the system, which has the most MCP-driven workflows and the interface with the IDE as was demoed before. So that was for renewals. Let me take a breath because I was going fast. Let's go to the support section. So in support, we have a very interesting thing.

**[15:48](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=948s)** Every customer of Cisco that has a support contract and opens a ticket has automatic access to all that we're going to show you. This is actually an anonymized scenario that we ran last week. This is a network customer, an enterprise, and they have footprints around the globe. So we went and did an analysis of all the potential configuration assessments of every device on their network. It looks big, but it's not. Think about this. This is a very small network for our standards, because if you think about a store, a store may have two devices for connectivity, three access points. This venue has a lot more than that. So if you think about five to seven devices, 113, I'm talking about 15 branches.

**[16:36](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=996s)** That's not that big. For being an international company, it could be a clothing company, it could be a restaurant, it could be a bank, it could be anything. But you have 2,176 potential security findings. Every one of you, if you look at your hands, you have 10 fingers, right? Usually. Some of them may make fat-finger mistakes. You've heard about fat-fingering configuration? We get that a lot. We get that a lot. A lot. So what you did in the assessment, this is one customer configuration assessment. This is real. I just had to remove the name and the customer's configurations. So you have this running, and then the question is: where do I even start? What should I do here? So we then provide the customer with this,

**[17:24](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1044s)** which is part of the support analysis from their assessment. So we say, hey, out of this environment that you have, you have some positive things. We have this product line that is actually compliant and secure, but we have some areas that you should actually look at. So what happened? We already went through the entire configuration environment for the customer globally. We already used AI to analyze against best practices. We already found potential vulnerabilities that exist. We already have the attack surface exposure for that customer. So: here is your environment. Then we have an AI system. We explain to them: hey, we can help you. And the feedback from the customer is: what should I focus on first? So think about it.

**[18:15](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1095s)** There is no mention of configuration. No mention of assessment. No mention of mitigation. None of those words that give you a clue. The customer just said: what should I focus on first? It's as vague as it can get. It's like marriage. Your wife comes to you and says: do I look good to go out? You're in trouble if you say yes. You're in trouble if you say no. If you say yes, you're a monster because yesterday you said I'm not pretty enough. If you say no, you're a monster now. So it's like this: very high-level context. I have some customers that just say "help." So for an AI agent, if someone sends a message that just says "help," what do you do?

**[19:02](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1142s)** Right? So we realize that behind the scenes, you already have over 350 potential high-critical severity issues that are going to hit this customer. So we use the context of the customer in real time, plus the best practices, plus the historical data, plus the fat-finger patterns, plus all the customer cases and tickets that were opened before, and you surface the most likely scenario that will impact them. How do we do that? We built a semantic router. So the semantic router, what it does, is actually define based on context which specialized agent would be hit given a scenario where you don't have enough context in the prompt. It's exactly the opposite of what we had yesterday. Yesterday I had a very detailed prompt that I needed to create a planner with a hierarchy. Here I don't have enough context from the prompt.

**[19:54](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1194s)** So I need to derive the context from the real-time environment plus the historical data, then route across specialized agents. So I have agents for configuration, for security, for troubleshooting, for assets, for inventory, all of that. Who am I going to hit? And we run this in a parallel pipeline. And it must run in parallel with the guardrail. Let me explain why. Here, I'm actually being proactive. I'm sharing with the customer what may happen before it does. There are some situations where we are in the middle of an outage. And people get really heated. So someone says something harsh, and then the model comes back and says: "I don't believe that the genealogical lineage of the engineer would help solve that problem." And I'm looking at the model like: "Dude, it's responding to a curse. Do you understand that?" But you need guardrails before that, because it contaminates

**[20:48](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1248s)** the routing. With semantic routing, you filter that out and semantic routing defines the agents. But again, every step is traced. So we go through the guardrails, the agent selection, and execution through LangSmith. So the current state feeds the routing on how you do the semantic approach. And every specific specialized agent has a dataset. And as we start to learn, the router gets updated based on what context exists in order to actually improve the routing. So this happens automatically. You have this done across multi-thousands at the same time because I cannot be manually reviewing what the AI is routing. It needs to be done at scale.

**[21:36](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1296s)** So we have this running and the paths are being regressed and we have human-driven recommendations that are goal-prioritized, and the ones that are learned and proven, we run this with LangSmith over and over again in a loop in real time as the system self-learns. And last but not least, we observe the observer. Because LangSmith becomes super critical for our business, we actually treat this as infrastructure and we observe it. We leverage Splunk to observe how it's doing. To give you an idea, we have 153K requests concurrently at the time that I was just taking those screenshots, and 100% SLO accomplished.

**[22:22](https://www.youtube.com/watch?v=AqU_WyOdEyo&t=1342s)** With that said, hopefully this helped you as you embark on your agentic journey. We are all out at the booth. Thank you very, very much. [APPLAUSE]
