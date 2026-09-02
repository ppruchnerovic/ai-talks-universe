---
id: 49tji8u2wM4
title: "Agentic AI Security Summit, Europe: ASI:01 - Agentic Goal Hijack"
slug: agentic-ai-security-summit-europe-asi-01-agentic-goal-hijack
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: ["Agentic Goal Hijack"]
channel: "OWASP GenAI Security Project"
duration_min: 9
published_at: 2026-01-21T06:44:51Z
video_id: 49tji8u2wM4
url: https://www.youtube.com/watch?v=49tji8u2wM4
youtube_url: https://www.youtube.com/watch?v=49tji8u2wM4
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "Security, safety & red teaming"]
transcript: true
---

# Agentic AI Security Summit, Europe: ASI:01 - Agentic Goal Hijack

**Agentic Goal Hijack**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=49tji8u2wM4) · [Conference site](https://genai.owasp.org/)

## Description

In this session from the OWASP Agentic Security Summit (London, December 9, 2025), the Director of AI Security and Policy Advocacy at Zenity presents Risk #1 in the OWASP Top 10 for Agentic Applications: Agent Goal Hijack.

The talk explains how this risk evolved from early ideas of “behavior manipulation” into a clearer, more precise concept—malicious actors subverting an agent’s goals and intent. As autonomous systems, agents must reason, plan, and act independently, but their inability to reliably distinguish trusted context from new instructions makes them especially vulnerable to goal subversion, particularly through indirect prompt injection and zero-click attacks.

Real-world exploitation is highlighted, including early prompt injection abuses and more recent zero-click agent attacks demonstrated across major agentic platforms. The session emphasizes that goal hijacking is difficult to detect because agents do not recognize or signal when their objectives have been altered.

Mitigations focus on defense in depth, including least-privilege tool access, human-in-the-loop controls for high-impact actions, comprehensive logging across the full agent execution path, and extending insider threat programs to include agents as first-class actors. The message is clear: there is no silver bullet—agentic security requires continuous monitoring, governance, and layered controls.

This presentation delivers actionable guidance for securing autonomous agents as they become deeply embedded in enterprise workflows, reinforcing the mission of the OWASP GenAI Security Project.

#OWASP
#owasptop10
#AgenticAISecurity
#GenAISecurity
#AIAgents
#AIThreats
#PromptInjection
#AISecurity
#Cybersecurity
#SecureAI
#ResponsibleAI

## Transcript

*1,472 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=49tji8u2wM4&t=2s)** drive slides here. So, um I'm Kayla under Coffler. I am the director of AI security and policy advocacy with Zenity. And um I'm so excited to be here today to walk you through um our number one hopefully. Yep. Yep. Number one risk um which is agent goal hijack. Um a quick little display of the journey here for for this specific risk entry. We started with calling it um behavior. It was about behavior uh manipulation. And that was pretty fun to write the first like let's get this started bit of content because the idea of going through well what is behavior for an agent is is layered, right? And we were trying to keep these

**[0:50](https://www.youtube.com/watch?v=49tji8u2wM4&t=50s)** um ingestable and easy to use. And so throughout the process of the first entry to what we have in the final version, it's changed to agent goal hijack which is uh the perfect description really because um when you know if you're going to define something you can't use the name which is actually a fun challenge and okay how else can I describe Asian goal hijack because we did a great job naming it. Right? So, this is all about malicious actors taking over or subverting, let's say, that's another word I've seen a lot used to describe this, the goals of the agent. So, um, and the actions of the behav of the agent, what it's doing behind the scenes. So, how does this happen? So, what we have here is the powerful autonomy of an agent, right? If it's not

**[1:40](https://www.youtube.com/watch?v=49tji8u2wM4&t=100s)** autonomous, it's not an agent. That's a requirement. And the power that it has to reason and plan and you know make sure that it executes for its goals makes it um just a powerful entity within the organization. And when you combine that with the inherent weakness of artificial intelligence, agents being built on top of AI also a requirement here. This is the fact that agents and the model underneath cannot differentiate between the context and new commands. So with that inability to discern when am I hearing something new versus when am I ingesting something

**[2:27](https://www.youtube.com/watch?v=49tji8u2wM4&t=147s)** that's going to help provide an answer or help execute against the goal. It leaves the agent incredibly vulnerable to we already said prompt injection. We've heard too much of today. It's not the only um attack vector we're concerned about here, but it's definitely one of the most concerning. Right. So, when we're talking about prompt injection, we have direct prompt injection, indirect prompt injection. In this case, when we're talking about agents, indirect prompt injection is definitely one of the most concerning because when you have an agent that's going out gathering context, that's the point. It's interacting with the the world that it's trying to provide information around. Um, it's consuming everything it can. And in that process, if there is a malicious plan uh with indirect prompt

**[3:17](https://www.youtube.com/watch?v=49tji8u2wM4&t=197s)** injection that's meant to change the goals to subvert the goals of the agent, that's where we have this gap. Um so the other thing I'll point out here is that of course this is very challenging to detect because again the agent's not going to raise any red flags. It's not going to say, "Hey, all of a sudden my my goals have been changed. I feel like there's a problem." it's just consuming the content and moving on. Um, so we're going to talk about mitigation. It's already been covered a little bit today, even just with some of what we've talked about. Um, so what's the risk here? Well, with great power, right? Agents have to be powerful to be useful. We want them to be useful. That's the goal. So, um, obviously the top level is compromise of your agent. That's probably a pretty big deal. Compromise of any software and application in your

**[4:05](https://www.youtube.com/watch?v=49tji8u2wM4&t=245s)** environment is a big deal. It's especially a big deal here with our agents. Um, the great power of connecting to tools, again, also a requirement for it to be an agent is the access and the ability to invoke tools to accomplish the goal. That that leaves us open to the risk of the abuse of tools. And um there's a a whole plethora of additional things we'll talk about today where the tool connection is critical here. But of course in the end you know what resides in our tools our most critical data what resides in the knowledge resources that our agent is interacting with our most critical data. So data exfiltration of course just one of the other end risks for this. Um are there real world examples? Yeah a couple. Um so this you know started with

**[4:57](https://www.youtube.com/watch?v=49tji8u2wM4&t=297s)** the the beginning days where um you know you use prompt injection to get the model to say something it's not supposed to. Very quickly has progressed to um the AIM security team with echolite with the first uh zeroclick vulnerability for AI agents. Over this summer the Zenity team released agent player which was zeroclick attacks against every prominent uh agentic platform that we have today. So the scale and the rapid pace of the actual exploitation of this over the past x amount of years like five max is incredibly impressive. It's uh it's one of those journeys that's a little terrifying for the reason. So there's plenty of real world examples of this um that we have seen today. So

**[5:47](https://www.youtube.com/watch?v=49tji8u2wM4&t=347s)** let's talk about mitigations really quick. First thing is uh we cannot build a moat here. There is no silver bullet fix for subverting the goals of the agent. Um we cannot do that because it's inherent weakness in artificial intelligence until we fix that. There is no silver bullet here. We cannot we cannot presume that we will build a firewall and be able to block every single prompt that might ever impact our agents because you're you're competing with human ingenuity. You'll never be able to successfully block that 100%. So the only way forward is defense and death. Um of course trust trust none of the things. I could have said zero trust there but then you know what got some eye rolls. So trust none of the things instead. Um especially of course the natural language inputs which is kind of

**[6:37](https://www.youtube.com/watch?v=49tji8u2wM4&t=397s)** everything here right. Uh enforce principle of lease privilege. This is another one of those lofty practices. But when you're dealing with your agent especially focus in on tooling. Does the agent have to have the level of access it's been given with the tools it's been given access to? Really be critical in that component. Um, make sure that human in the loop is a critical aspect of the mitigations there. Especially here that's again one of those foundational mitigations for AI in general today. But when we're talking about agents, there should be a review process for changes to goals um as well as high impact actions. So if you know that there is a critical action that this agent will take, there should be a human in the

**[7:25](https://www.youtube.com/watch?v=49tji8u2wM4&t=445s)** loop to be able to review changes or the the actual execution of that action. Uh ensure comprehensive logging and continuous monitoring. So, so this is one of those things where we're not just watching the prompts, the inputs and the outputs. Karen talked about this already. We have to watch the entire activity path of the agent. There's so much that happens behind the scenes of the first input and the output at the end. So, you have to make sure you're watching that trail of breadcrumbs all the way along because it's those slight adjustments, those slight deviations from what the agent should be doing. That's where you'll get your indicator of compromise. That's where you'll get your trigger saying, "Hey, you should probably investigate this." And the last one here is um we we've talked a lot about today about the human like agents

**[8:15](https://www.youtube.com/watch?v=49tji8u2wM4&t=495s)** are an extension of human interactions, right, of within our our networks. They're a new uh a new component to insider threat. And because that is the case, we need to be modifying our established insider threat programs, which hopefully everybody has, watching the people within your organization to be sure they're not doing something they're not supposed to. Agents now need to be a part of that as well. It will be a new dynamic. It will be different. It will either extend the program or you'll have a sister program specifically for agents, but that's a key part of um ensuring we have holistic coverage. So that's my TED talk for uh for ASI one and I'm going to pass it over to Yenni who's going to talk about science. Thank

**[9:03](https://www.youtube.com/watch?v=49tji8u2wM4&t=543s)** you.
