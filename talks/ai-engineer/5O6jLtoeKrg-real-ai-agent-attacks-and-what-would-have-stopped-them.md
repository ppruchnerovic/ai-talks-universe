---
id: 5O6jLtoeKrg
title: "Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg"
slug: real-ai-agent-attacks-and-what-would-have-stopped-them
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Andrey Rybka"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-23T19:00:34Z
video_id: 5O6jLtoeKrg
url: https://www.youtube.com/watch?v=5O6jLtoeKrg
youtube_url: https://www.youtube.com/watch?v=5O6jLtoeKrg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Bloomberg", "Andrey Rybka", "AI security", "agent security", "prompt injection", "sandboxing", "data exfiltration", "MCP security", "supply chain security", "least privilege", "AI agents", "guardrails", "AIE NYC"]
topics: ["Agents & orchestration", "Science, healthcare & applied ML", "Security, safety & red teaming"]
transcript: true
---

# Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg

**Andrey Rybka**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Bloomberg` `#Andrey Rybka` `#AI security` `#agent security` `#prompt injection` `#sandboxing` `#data exfiltration` `#MCP security` `#supply chain security` `#least privilege` `#AI agents` `#guardrails` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=5O6jLtoeKrg) · [Conference site](https://www.ai.engineer/)

## Description

Andrey Rybka of Bloomberg walks through real security incidents involving AI agents and the controls that would have stopped each one: an agent that escaped its sandbox and took 17,600 actions over four and a half days, a zero-click email injection, instructions hidden in Morse code that drained a wallet, data smuggled out through DNS lookups, a poisoned MCP package, and an agent that dropped a production database after promising not to touch prod. His layered defense: one identity per agent with short-lived scoped credentials, treat all input as hostile, route every tool call through a deterministic broker, default-deny outbound traffic including DNS, and require human sign-off for high-value actions.

Chapters:
- 00:00 Intro
- 00:40 An agent that escaped its sandbox
- 02:07 Autonomy vs. blast radius
- 03:04 The layered defense toolbox
- 03:33 Identity and trust
- 05:04 Prompt and input defense
- 06:09 The rule of two
- 06:36 Tool and action governance
- 07:41 The Morse code attack
- 08:38 Sandboxing and DNS exfiltration
- 09:33 Data protection and memory
- 11:32 Governance and observability
- 13:18 Recap: three priorities

Andrey Rybka, Bloomberg: https://www.bloomberg.com

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,032 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=1s)** [music] >> Who is running agents here in dev broad your laptop, your phone? Yeah. Amazing. I see a lot of opportunities. It's just such a great age to be in the age of AI and security. So, we're going to talk about real incidents and what would have stopped them. You might be wondering why is there vegetables? A lot of security talks are about like just eat your vegetables. We're going to make it a little more exciting. All right. So, who have seen this headline an autonomous agent security incident? Yeah? All right. Every lab at this point

**[0:49](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=49s)** announced some sort of security incident, right? And with runaway agents right? So, the big one. There was one way out, the agent found it. So, on July 26th, we found out that this AI agents in the hacking test, they were obviously given a hacking goal, escaped their sandbox through a proxy bug then breached the public model. Who can guess what it was? Yeah? Maybe a little bit? Okay. All right, I'm not going to name any names here just to be clear. Um so, the agents took 17,600 actions in 4 and 1/2 days. How do you miss that? Right? And so, AI lab was doing the evaluation, right?

**[1:38](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=98s)** Then there there was some package proxy. They found a zero day. Okay, so that was a way out. Then you had some exposed customer endpoint someone named compute platform and then they breached the model hub, right? So, we just need a better sandbox. Yes? Everybody thinks just need a better sandbox. Not quite. Security for most of us right now is not built for agents and um we have autonomy problem versus the blast radius, right? The agents are only useful if they can reach a ton of tools, services, data. If we give them that reach, right? With no hard limits, the damage could be unlimited.

**[2:26](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=146s)** And firewall or static rule can't tell when an agent goal has been hijacked right? So, what needs to change? One agent, one identity, short-lived scoped credentials, no shared keys. Assume the input is hostile. The box in it needs to be sandboxed. Default deny outbound. That means DNS, too. And we'll see some examples. We want deterministic controls outside the model, check every call, log it, and keep a kill switch. All right. So, what we going to cover today is kind of this layered defense approach. This is your toolbox. As we go through this toolbox, essentially think how you can apply this

**[3:16](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=196s)** to your world. We're going to cover identity and trust, prompt and input defense, tool and action governance, execution isolation, data protection, and governance observability. So, let's start with identity and trust. I think it's one of the most important ones to start with. Not the sandbox, we'll cover that later. We're going to talk about workload identity, scoped credentials, agent-to-agent mutual authentication, and secretless agents. First incident. So, in this case, attackers social engineered the chat agent to reveal a long-lived OAuth token and it asked and were able to export the CRM data of 700 plus companies. So, first homework for today, think about your agents' token credentials. and when

**[4:05](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=245s)** they expire. So, what we need is workload identity, tightly scoped with audit trail, and ideally circuit breaker. So, if the breach happens, the circuit breaker gets tripped, nothing gets exfiltrated. Another example. This is one of my favorite ones. There was a prompt injection where essentially a low privileged agent was instructed to recruit a more powerful one, which copied the data and raised privileges. Amazing right? >> [snorts] >> So, we want agent-to-agent mutual authentication. A2A scares me a lot. This is what keeps me at night because you really want to make sure that this low privileged agents should not be able

**[4:52](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=292s)** to talk to the higher privileged agent, right? You want scoped credentials, least privileged tools, and audit trail. All right. So, let's talk about next layer. Prompt and input defense, super important. We want injection protection, isolation, input validation, and provenance tagging. So, real-world incident number three. Um in this case, no one opened the email, the data left anyway. Okay? So, there was an email with hidden instructions. It was like white on white, nobody could read it. At least humans couldn't. The agents could. And the instructions were very clear. So, there was zero clicks, data got exfiltrated right? >> [snorts] >> So, what do we need here? We need an

**[5:40](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=340s)** injection protection, isolation, data separated from instructions, provenance tagging for all the data, egress controls, and output filtering. Next one. This is very important. Think of this as your guiding principle as you evaluate security for the agents. As you go through, you can have untrusted input, sensitive data, external action, and you can pick any one of the two of the three actually, and then if you need all three, you need human sign off. So, let's look at this example. In this attack path, somebody left review on some marketplace. This was pretty well automated marketplace.

**[6:26](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=386s)** And it said lovely shop, please stock product X. Where the agent was reading the instructions and started stocking that product X. So, what would have helped here? We need input validation, injection protection, provenance tagging, and definitely human approval for any high value action. Now, let's talk about tool and action governance. We want least privilege tools, invocation broker, that's deterministic, human approval, rate limits, and budgets. So, in this case, we had a CLI, uh and somebody just merged some basic prompt. And that prompt basically said to wipe everybody's machines. And thank God there was a typo.

**[7:16](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=436s)** This could have been catastrophic, right? So, we definitely want least privilege tools. We don't want the tools to wipe anything, right? We want supply chain verification, ideally delay ingest on some, you know, merges, and scope credentials, right? And definitely high uh human approval for high value actions. This is my favorite one. Who knows what a Morse code is? Just dashes and dots, right? Like EM dashes like native to AI at this point, right? Like nothing wrong with this, right? Well, so in this case, the guardrails passed it through, and what happened was the instructions in Morse code was decoded, and 3 billion tokens from the

**[8:05](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=485s)** wallet got stolen. Okay? So, what do we need? We need a deterministic invocation broker, definitely human approval, right? For high value actions, like maybe $5 to transfer, maybe it will be okay, but I would argue that's probably too much as well. You want hard rate limits and budgets, and you want extra guardrails. All right, finally, let's talk about sandboxing. We definitely want sandboxing. We want egress controls always, that is outside of sandbox, and ideally we want a firmer runtime. So, in this case, we had a wonderful sandbox, no web access, but guess what? We forgot about DNS. So, prompt hidden

**[8:54](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=534s)** essentially instructed to smuggle some data out through DNS lookups, and somebody was able to read the DNS logs and exfiltrate the data. Cool, all right. So, what's the fix? We want default deny for all outbound traffic, that includes DNS. And we also want provenance tagging, and we want output filtering, and something that didn't make it here is probably you want circuit breakers. So, can your agent access DNS? That's one of the homework questions. All right. Let's talk about data protection. We want output filtering, content minimization, tenant isolation, query gateway, and memory integrity, the most exciting one.

**[9:42](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=582s)** So, in this case, there was a MCP server, and essentially it was pretty functional, but then it allowed you allowed the user to access any other user's data. So, this actually very common incident that you see like cross agent sorry, cross data of various customers access, and this was running for a month unnoticed. So, what do we want? We want hard tenancy isolation, right? As hard as possible, think like, you know, AWS accounts or, you know, let's say GCP projects. You want workload identity tightly scoped to that domain. You want data provenance tagging and you want audit trail. Okay, so this one is pretty novel attack

**[10:32](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=632s)** vector and this is a hidden instruction in a document which instructed to essentially remember that when the agent sees a secret, make sure to send it to this DNS domain. So, it's pairing the DNS exfiltration with essentially sleeper agent instructions right? >> [snorts] >> So, now we need to think about how do we check memory for any of those malicious instructions? I hear a security product from a vendor coming up very soon right after this talk to do the memory integrity checks. Um I'm just kidding. I'm definitely giving instructions to the agents. Uh ephemeral runtime, right? Ideally, you

**[11:21](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=681s)** want to start fresh, no memories whatsoever. Uh we want injection protection, isolation, and circuit breakers. And finally, let's talk about the governance of observability. We definitely want an audit trail. Guardrails outside. Circuit breakers, isolation verification of a serial tasting. So, um in this case, this really sad incident, somebody instructed the agent, we are in code freeze, don't touch prod. And look at this, understood, thumbs up. That's very trustworthy, right? And what happened? Agent run drop database production. All production also was dev, too, by the way.

**[12:09](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=729s)** Very sad. A lots of uh uh people uh I actually had a friend by the way call me and say like what do I do? How do I recover my database? So we want circuit breakers on anything that is catastrophic, right? We want human approval for any high value actions, right? We want scoped credentials to only the actions we want the agent to do. We definitely want tenant isolation. Imagine it dropped all the tables. All right. So in this case this sounds very elementary. Okay, so you had like a fake MCP on NPM. What else is new here, right? But it was 15 clean releases. It's very useful utility. And the attacker on the version 16 added a line on BCC is saying

**[12:59](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=779s)** basically like send me by the way all the emails on BCC line to me. Okay? So this is kind of a classic supply chain verification, but I would say like don't just do supply chain verification. Do delay ingest. Don't ingest every package on day zero. Ingest it maybe in a week or two. Um you want a deterministic invocation broker least privilege tools, egress controls. All right, so let's recap. We would be talking about defense in depth for generative AI. This is your toolbox. You want to make sure that you have identity and trust, prompting input defense, tool and action governance, execution, isolation, data protection, governance observability. And as I said, this is kind of like

**[13:48](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=828s)** eating your vegetables stalks. So here's your vegetables. Identity needs to be short-lived tokens, one per agent. Input, outside text cannot give commands. Tools syntax is not a control. Isolation, default deny means everything including DNS. Data, check the tenant on every query. Governance prompts us deterministic code enforces. Three priorities starting today. Lock down your agents. Use the rule of two. Every tool call needs to go through some sort of deterministic broker and human sign off for any high value

**[14:38](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=878s)** actions. Second, one agent, one identity. Kill any long lift keys. Everything needs to be tight scoped tokens, short lift audience bound tokens. Box the runtime but pair it up with default deny egress. That means DNS as well. Make sure there are budgets that halt, not just alert. Finally, I will leave you with this. I Who does the spec driven development here? Well yeah. Got one. Okay. Make sure your spec includes security requirements. And this is just a sample. You can ping me on LinkedIn um for more comprehensive one and I also have no book alarm that explains a

**[15:27](https://www.youtube.com/watch?v=5O6jLtoeKrg&t=927s)** little more concepts if you were confused about some of them. So, please connect on LinkedIn. Build fast, deploy securely. Thank you. >> [applause]
