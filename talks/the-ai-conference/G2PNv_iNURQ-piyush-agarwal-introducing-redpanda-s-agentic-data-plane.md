---
id: G2PNv_iNURQ
title: "Piyush Agarwal: Introducing Redpanda's Agentic Data Plane"
slug: piyush-agarwal-introducing-redpanda-s-agentic-data-plane
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 10
published_at: 2026-10-07T22:53:49Z
video_id: G2PNv_iNURQ
url: https://www.youtube.com/watch?v=G2PNv_iNURQ
youtube_url: https://www.youtube.com/watch?v=G2PNv_iNURQ
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: true
---

# Piyush Agarwal: Introducing Redpanda's Agentic Data Plane

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=G2PNv_iNURQ) · [Conference site](https://aiconference.com/)

## Description

AI agents are increasingly deployed as digital employees—accessing enterprise data, making decisions, and acting autonomously. But agents are both less predictable than humans (prone to hallucination, misinterpretation, and adversarial manipulation) and more capable, with deep system access and machine-speed execution that can cascade damage fast. This makes it unsafe to trust agents to faithfully interpret or propagate security-critical metadata like access policies, data classifications, and behavioral constraints. We present Redpanda's Agentic Data Plane (ADP): an architecture using out-of-band metadata channels that carry security context, policy signals, and audit trails deterministically—entirely outside the agent's read/write path, across heterogeneous infrastructure. These channels enforce governance at every stage of the agent lifecycle: scoping data access going in, constraining actions during execution, and capturing tamper-proof audit trails coming out.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,673 words · source: supa (en, exact timings)*

**[0:11](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=11s)** Everyone, super excited to be here. My name is Piyush Agarwal. I'm the VP of engineering at Redpanda, and today we're going to talk about Redpanda's agentic data plane. Before I talk about the agentic data plane, what is Redpanda? Redpanda handles mission-critical data and agentic AI workloads for the world's most consequential companies. Uh we have New York Stock Exchange, Paramount Poolside Rivian Vodafone and many more that can fit in this slide. We power literally hundreds of such mission-critical workloads for our customers. The problem that I think the industry stands at and that Redpanda is identifying is that agents are too capable, too fast, and too easy to fool. And we cannot govern them the way that we might have wanted to or thought that we could.

**[0:59](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=59s)** Agents can misinterpret, be manipulated, and circumvent any policy that they can see. They move faster and they go further than any rogue employee ever could. There was a proof of this with Core Break just a few weeks ago at Black Hat, where three different vendors, three different frameworks, were forced into emergency fixes because their policies were visible to the agent and hence circumvented. The insight that Redpanda is bringing to the table is that agents are not the problem. Agents and LLMs are always going to become smarter and smarter. The missing layer is between the agents and the data that they're accessing. That's what we need to focus on. We never ask human employees to be

**[1:46](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=106s)** perfect. We build governance so we can take imperfect ones and get them to deliver impact. Agents need the same identity, access control, and accountability for every single action that they're taking. And all of this is, by the way, not just talk. I'm going to show you screenshots of our platform that we use internally and our customers use, as well. We haven't built such a thing for agents until now, which is why enterprise AI is stuck. The solution, then, is to have these data access policies that are invisible to the agent. What an agent cannot see, it shall not be able to circumvent. These policies are to be enforced at the connection point, so that any MCP, any tool call, any LLM, all tokens pass through this connection

**[2:36](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=156s)** point where we can enforce the policies to make sure that agents remain on track and you have the confidence to take these and put them into production. Every action will get checked, independent of the model, with full context, not just whether I have the credentials to be able to do the action that the agent is attempting to do. Now, let's talk about what is the Red Panda platform. We call it bring your own anything. You can bring your own cloud, you can bring your own MCP, you can bring your own agents, or you can use Red Panda's. No matter what you do, you have the same policies enforced, same guarantees either way. That is the freedom that you get with Red Panda platform. And you get one gateway to rule them

**[3:23](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=203s)** all. You can control access to models, to data, and to the agent's own behavior. And again, something that agent cannot see, because if it could see it, it is going to circumvent it. And all of that from a single gateway. Now, this is kind of how it fits all together. On the left, you see Red Panda agents, again, that agents you can build on the Red Panda platform, or you can bring your own agents, again, using open protocols, which is A2A. You can integrate with external systems like Microsoft Teams, Slack, and many more. And that gets you to the middle layer, which is the gateway, where you have the gateway acting as a gateway for MCPs and for LLM providers, all of them together. And that is the choke point where you

**[4:12](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=252s)** get to apply all of your out-of-band policies identity guardrails spend caps, and kill switch as well. I'm going to talk about all of them pretty much in this talk. And then, you use that gateway to then access the systems of record and MCP servers, which live across your infrastructure, including the LLM providers. Again, we work with Anthropic, OpenAI, and anything compatible with their API, Gemini, as well as Bedrock. And all of the interactions that this the my agents are having with MCPs and tools and um uh LLM providers, all of that is going via open telemetry, again an open to the Red Panda's data platform, which is the streaming log and a SQL layer on top for you to get cost um accounting, auditing, and other

**[5:00](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=300s)** capabilities. Just to kind of reiterate, we work with all industry standard open protocols. There is no vendor lock-in with Red Panda. All of it is A2A. It is MCP. It is open telemetry. It is OIDC. It is um um Iceberg for the for actually storing the data. None of it needs to be in the walled garden of Red Panda, and that is one of our core operating premise. Now, let's say that your agents are actually running in production. How do we hold them accountable? We need to be able to see every single agent that is being run, and we want to be able to prove every single action that they're taking. Here is the agent network view, which I'll show on the next screen.

**[5:48](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=348s)** Agent network view provides you that visibility where every agent in your entire enterprise and infrastructure is out there on one screen. Transcripts of every single conversation that each agent is having with every tool call, every MCP invocation for audit and compliance. With guardrails, I don't want you to be uttering uh leaking PII, uttering, you know, uh cursing, or anything that you call as forbidden, and all of those enforced as well. So, again, that you have confidence for putting these agents in production. Evaluations to manage your rollout of agents, as well as a kill switch where that actually reaches the target. Now, this is an internal deployment of our platform internally that we dogfood and we use day in and day out, and you can see we have 100-plus agents that are currently being

**[6:36](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=396s)** used. The number of conversations that we are having, the number of tool calls, the costs, the tokens, and many more. And the network view is this unified view where you can get all of the agents in one view that I can drill down to say what are my agents doing, what MCP servers are they calling, what tools are they invoking. Every single bit of that information is available to you in this view, and again, exported via Open Telemetry as well. And you can drill down on the cost aspects. Now, who hasn't run into the cost equation with AI usage? We want to be able to spend caps, uh rather, assign spend caps and say I don't want this particular group, this individual, or our entire company to spend more than X number of dollars. And this is just an internal screenshot of, again, uh we using our own platform to manage our

**[7:25](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=445s)** costs. Let's talk about kill switch. Obviously, that's gaining momentum with the recent, um let's say um you know, the governor of uh California, I think, and other politicians as well getting into the race of kill switch. We think the kill switch is actually in the wrong place because a model can be throttled by the lab that built it, but it cannot stop the agent that is already wired and running in your infrastructure and being used. So, we have built and actually let's go back in history a little bit. We've built things that escaped their boundaries before, right? And back in 1988, we had the modest worm which was written to estimate the size of the internet. It took down thousands of machines. It was measuring within a day. So, we've built we've we've run through

**[8:13](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=493s)** this before where we build things that escape their controls. And that is exactly what agents are except that agents are now inside your business not just in a lab. They're accessing live your customer records, your financial systems, your source code, your infrastructure. They're calling APIs, they're moving money, they're changing production states faster than any human can ever review. All of that means that you need a platform to be able to contain that risk and yet deploy agents in production. Now, this is essentially what kind of give you a full picture of what it takes to get agents into production. You give agents a job, that is you again have your agents externally or managed by Repanda. Then you set the rules. You control and govern access to models. You control and govern access to data and you control and govern the behavior with guardrails.

**[9:03](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=543s)** Then you connect to all of the data that makes the agent useful. And once you've connected the data to your agent, then you get to observe and hold the agents accountable with all the things that I was talking about which is again the kill switch, the transcripts, the guardrails, the monitoring, and the evaluations. And that is it. That's pretty much it from Repanda. To summarize, the Repanda platform is these four products together. We have the Repanda SQL which allows is a post-rest compatible OLAP system. It's the best performing query engine tested on Nvidia beta as well. We have a banner connect that allows you to connect disparate sources to make your agents effective. We have a banner streaming which allows for the substrate to capture the transcripts and the audit log from all interactions that the

**[9:51](https://www.youtube.com/watch?v=G2PNv_iNURQ&t=591s)** agents are going through and all of that percolates up to the agent data plane that allows you with the confidence to put agents in production. Thank you. Happy to take any questions.
