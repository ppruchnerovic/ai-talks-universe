---
id: RA0XVLMKdm4
title: "Navrina Singh - Earning Autonomy: Governance as Code for the Agentic Enterprise"
slug: navrina-singh-earning-autonomy-governance-as-code-for-the
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Navrina Singh"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T06:45:04Z
video_id: RA0XVLMKdm4
url: https://www.youtube.com/watch?v=RA0XVLMKdm4
youtube_url: https://www.youtube.com/watch?v=RA0XVLMKdm4
tags: []
transcript: true
---

# Navrina Singh - Earning Autonomy: Governance as Code for the Agentic Enterprise

**Navrina Singh**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=RA0XVLMKdm4) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,039 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=1s)** EHRIK ALDANA: All right. Great. Hi everybody. My name is Ehrik Aldana, and I lead product at credo AI. The first thing you should know about me is I am not Navrina Singh. Unfortunately, Navrina, our CEO and founder, couldn't be here today. So you get me. But for those of you who don't know us, so Credo AI is an AI governance platform. And we work with the people at large enterprises and government agencies who are accountable for AI. So not just those who build it, but those who have to decide which AI systems are safe and trustworthy to build, to buy, and to deploy across their organizations. Now, this is the AI safety track. And depending on what circles you run in, what jargon decoder ring you're using, safety and governance are often treated as separate disciplines. But at their core, I'd argue that they share the same job, which is making sure

**[0:50](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=50s)** that AI systems can act in a way that the people behind them intend. And at a large enterprise, a company, intent isn't just one person's decision. It's a coordination problem between the engineers building the system, the business owners defining what the problems they're trying to solve are, the compliance, the legal teams deciding what actions the organization is OK with. Customers now are writing requirements into their contracts for procurement, and regulators and auditors are writing the standards that carry real penalties. So governance, at an organization, is how all of these different intentions get reconciled and then enforced into how an AI system actually behaves. Now, when a large enterprise lets a human act autonomously on consequential decisions, that authority was earned through some sort of structure.

**[1:40](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=100s)** Like every intern engineer, they start with limited production access, and they earn more as they rise through the ranks. Or every trader at an investment firm. They have to earn their limits on what they can invest. So organizations have built these ladders of earned authority over years of trial and error. But for agents, that ladder largely doesn't exist yet. Many agents, they receive full authority the moment they're deployed. And that is a design error that I want to address today. So capability might come from the model, but autonomy must be earned from the enterprise. So from most of our six years of shipping AI governance processes and tools, the unit of governance we operated under was the use case, so an AI tool and the context that it's deployed in. So say, for example, a chatbot that answers employees' questions about company policy.

**[2:29](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=149s)** You could draw a really clear boundary around this. But what agents have done is dissolve this boundary. So what is a use case for an agent that can plan its own steps? What connectors should it have access to, what data sources? When the use case blurs, the parameters that you use to govern it also are going to blur. And so this pressure gave us a new mental model for how we at Credo AI are thinking about governing agents. And this is separated into three ideas. The first is, Can. So this is capability. What is a model and its tools technically able to do? The second is May. So this is authority. What is the agent permitted to do here and now with the data and tools it has access to? And Act is autonomy. And so this is the authority it can exercise without having to wait for a person. Capability is benchmarked. Authority is scoped and revocable.

**[3:17](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=197s)** And in this framing, autonomy is not just a model property. It is an enterprise permission earned through evidence or a system property, as we've heard earlier today, used. So if autonomy is an enterprise permission, where in the stack does it get granted? So security typically asks whether an attacker can make an agent do something bad. Observability is asking whether it can do its job well. And these systems are essential, but they all speak to that Can layer right, what the agent is able to do and whether it's doing it well. None of them are really addressing this May piece. So when we think about AI and agentic governance, we want to make sure that that system is able to do three things. The first is compose. So take the full context of the AI system and its organization and create a governance plan.

**[4:04](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=244s)** What are the risks and controls that need to be applied to it? It'll conduct that plan, execute it, whether it's through evaluations or guardrails for the system, and then keep a record, of all of those different pieces. So I'll skip ahead and talk about what we're doing at Credo AI to actually enforce this. So one way we're thinking about this is directly through the agent's harness, the actual runtime code that sits between the agent and the systems it can touch. This isn't an evaluation harness, but instead it's a governing one. So you take that governance plan we discussed, that was composed, and you embed it into a versioned, configurable set of code that a harness can enforce. So we're thinking about things like skills, hooks, guidance, manage settings, installed directly where the agent runs, not something like an MCP or an API gateway or proxy. So if you're thinking about a governed Claude Code session,

**[4:54](https://www.youtube.com/watch?v=RA0XVLMKdm4&t=294s)** for example, this would be like it's trying to read an approved repo. The system allows that. It's trying to open a credential score. The configuration blocks it. Dependency above a risk threshold. This ultimately gets escalated to that code owner. Each of these checks that the action goes through needs to ultimately be surfaced, and that's being done through that configuration. So, yeah, at the end of the day, this ladder that we talked about for earning autonomy that we said didn't exist for agents, this is it, so a system where the enterprise can collectively decide what the agents can do, enforce those decisions where the agents act, and keep the proof. So anyway, that's all I have for today. And on Credo AI and Navrina's behalf, thank you very much.
