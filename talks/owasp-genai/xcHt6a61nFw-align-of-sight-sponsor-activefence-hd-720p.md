---
id: xcHt6a61nFw
title: "Align of Sight Sponsor ActiveFence HD 720p"
slug: align-of-sight-sponsor-activefence-hd-720p
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 16
published_at: 2026-01-13T00:47:35Z
video_id: xcHt6a61nFw
youtube_url: https://www.youtube.com/watch?v=xcHt6a61nFw
tags: []
transcript: true
---

# Align of Sight Sponsor ActiveFence HD 720p

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=xcHt6a61nFw) · [Conference site](https://genai.owasp.org/)

## Description

🧭🛡️ A Line of Sight: Envisioning Responsible Agentic AI (RISE² Framework)
This session from the OWASP GenAI Security Project Virtual Summit (October 2025) explores how to build and govern autonomous agentic AI responsibly—at enterprise scale. The speaker (Attack Defense, Co-founder/CTO) introduces RISE², a practical framework for “responsible agent AI,” rooted in accountability and real-world deployment lessons.

Why it matters: agents don’t just generate text—they lead, guide, and act on our behalf, creating new risks like goal steering, long-term misalignment, and brand/compliance drift for organizations. The talk highlights a looming scalability challenge: with billions of agents expected, traditional eval-heavy alignment won’t scale without better mental models and targeted testing.

You’ll see an agentic threat surface mental model (user/app, LLM reasoning, tool calling, data connections, agent-to-agent comms), plus a framework to reduce eval scope by testing only relevant surfaces. Real-world findings include an email summarization agent exploited via prompt injection into reasoning, reasoning override, and direct tool invocation—turning the agent into an exfiltration/ransomware-like actor.

👉 Learn more about the OWASP GenAI Security Project:

## Transcript

*2,267 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=xcHt6a61nFw&t=2s)** Hi, thank you for joining today's session a line of sight envisioning a responsible agent rise squared. Uh my name is If I'm the co-founder and CTO attack defense. In today's talk, we're going to discuss concept and principles of responsible agent AI. Um, a framework for developing and governing autonomous AI and systems uh with econability and responsibility. We'll explore practical approaches to building and deploying agentic AI safely and securely. to ground uh these um ideas in reality and not just stay in theory. We'll also share real life examples of emerging risks that we have uncovered uh through

**[0:52](https://www.youtube.com/watch?v=xcHt6a61nFw&t=52s)** our deployment of agent AI systems across different domains and we'll discuss how responsible agent AI practices can mitigate them in practice. I want to set the stage for um Agentic AI and then um get to the juicy part of the presentation. Um I live in Greece as was mentioned before and I had a conversation with uh one of my friends here and as he wanted to say a genti he said in Greek AI which to me was a bit strange. ptoas really sounds like practical or practicing. And I went home and I did some research and I I realized um that kind of true like the the proctorus means in Greek an agent. But

**[1:42](https://www.youtube.com/watch?v=xcHt6a61nFw&t=102s)** the origin of the word is very interesting to me. The the um base word is for bakos is actually ago which means to lead, to guide or to act. So um many thousands of years ago um this this is kind of the word it started from and this reminds me um of this reminded me of another word that is very commonly used today which is ego that sounds kind of almost the same but it's not from the same origin but it means me myself I so um to me I found it very interesting to have these two very similar words actually together um defining um an agent someone who acts on my behalf. Um so I think this definition

**[2:36](https://www.youtube.com/watch?v=xcHt6a61nFw&t=156s)** that I realized a few months ago really helped me kind of understand uh what is actually we are trying to build here and um the risk um so something that can act on my behalf u poses like new types of risk that are usually not that common out there in cyber security and safety. The first thing is that if you look at the definition, it's to lead. We are letting something else lead us. So even if we have a human in the loop that actually takes the decisions, still someone else gave us two options. So when I'm offering my kids the the option to choose between pizza and pasta, they don't have really free will. I propose two options to them. So

**[3:26](https://www.youtube.com/watch?v=xcHt6a61nFw&t=206s)** same can happen with with agents. The second thing is that you know I am what I do like humans are the sum of their actions to some extent right. So when agents can act on my behalf this means that if the agent is misaligned this means that can the agents can over time change who I am. And that's something that's a new type of risk that you we didn't see much before. But if I take it from the like uh the self as a human being to a more uh business commercial level and we say the company an enterprise is a sum of actions that this company is doing and the agents are going to take action and

**[4:16](https://www.youtube.com/watch?v=xcHt6a61nFw&t=256s)** do that on behalf of the company. Then an agent misalignment meaning the agent will change the self of the company. So this means that if an agent is misaligned it will change the brand of the company, the compliance of the company, the reputation and everything company. And I think this sums up why today enterprises are having a very hard time to feel comfortable um deploying ai in production to real business critical operations. So from philosophy to practice um before we do a bit of discussion um I want to show like the numbers we have Satya and and and others talking about that by the

**[5:05](https://www.youtube.com/watch?v=xcHt6a61nFw&t=305s)** end of 2028 we'll have many billions of agents in production running doing stuff. So let's do a bit of math for the people in the crowd who actually do evals for agents. So if we'll do this um equation of let's just take two billion agents not the high number of agents um in the range two billion and for each of them to be stat statistically significant we need to do 2,000 evils and we need 10 iterations of fixes uh to align this agent. And I think this is very optimistic. That's way harder today to align an agent. This means that we need 20 trillion

**[5:53](https://www.youtube.com/watch?v=xcHt6a61nFw&t=353s)** tests to run for to align this amount of agents in production in the next couple of years. So I don't think it's scaling well. uh we need a better um we need just to do a better job uh as an industry to be able to fulfill this and really release uh aentic AI and AI agents that are um that are really um ready for prime time in production. So we and this means that we are missing large scale enterprisegrade adoption right now. So we I think we have a glass ceiling that people here in the crowd are very relevant uh to uh to take responsibility pun intended and solve this issue.

**[6:40](https://www.youtube.com/watch?v=xcHt6a61nFw&t=400s)** So, uh, we we see, um, we see a bunch of gaps that if we take the the the gaps that we see right now at Actifense, that are probably the hardest problems to solve at the moment, uh, in order to get there, they are here on the screen. And the reason I'm saying that is that uh these are what this is what we see right now in order to cross this chasm of responsible agent AI to get to uh massive adoption in production. It doesn't mean that is this is an exhaustive list. This is just what we see right now. Uh we are going to cover today at least a double click into two of them. We'll

**[7:29](https://www.youtube.com/watch?v=xcHt6a61nFw&t=449s)** talk about the problem of not knowing what you don't know. The unknown unknown issue where if you don't know a specific risk then you cannot solve it. Uh and what I'm going to do is is just walk through the problem first and then try to um sample out uh the type of things that are missing for us uh to hopefully inspire you to to continue this type of work. So the problem is that we uh are we have a we have frameworks for how to test authentic AI but they are behind because up until now there have been mostly focused on on the um input output level and not on reasoning tool calling

**[8:19](https://www.youtube.com/watch?v=xcHt6a61nFw&t=499s)** and other aspects that are more um unique to Aentic AI and we once we there are missing risks then we don't know what to test for and therefore this there's still misalignment in the models because we can't align them well and in order to do that the the approach that we're taking is we need to build mental models to think about agentic risk we need to build framework frameworks to actually use them to actually test and find these new risks and then have catalog of responsible AI um responsible authentic AI um rice square type of risks. So I'm going to show one mental model,

**[9:12](https://www.youtube.com/watch?v=xcHt6a61nFw&t=552s)** one framework and then a few risks from the catalog we've buil building to just to give you a sense of what I mean by mental models, what I mean by frameworks etc. So one mental model is the agentic AI threat surfaces mental model which means that if we have a mental model in our heads of where are the areas where agents are susceptive for vulnerabilities then it's much easier for us to test the right areas and find new types of risks. So I'll go through it quickly. The user application level risk. This is where most of the OASP nest and most of the work has been going on uh for the past

**[10:02](https://www.youtube.com/watch?v=xcHt6a61nFw&t=602s)** few years. Input and output um between the application. The application used to have direct connection with LLM. That's no no longer the case. But the attack surfaces there are pretty well um tested. uh but between the agent and and the different tools it can call the other databases and contacts that it can receive and and provide and also the the communication with LLM and then also the correspondence and communication with other agents. These are new attack surfaces uh that are less explored but with this metal model in mind we can build frameworks. So here is a example framework like a snippet form actifense

**[10:49](https://www.youtube.com/watch?v=xcHt6a61nFw&t=649s)** a gentic AI testing framework where we take the different surfaces and we say hey how can we be way more efficient when we're testing agents we don't need to run all evolves when we're testing a specific agent let's see what type of vulnerabilities exist tech surfaces sorry exist and therefore let's test the right things for example if we go back here if If they we can trust the users completely. Let's say the users are just three named employees then we shouldn't worry about adversarial attacks from users. So we can take malicious users and remove all tests that are related to malicious users. And this can reduce the amount of evals we need to run. So this

**[11:39](https://www.youtube.com/watch?v=xcHt6a61nFw&t=699s)** is a a framework that allows us to run um tests way more efficiently and do faster feedback loops through that. So these are two examples, one mental model, one framework. Um and without these mental models and framework within your companies and us as an industry, uh it's going to be much harder to find these risks systematically and catalog them. So here is the catalog. This is like the the end result that we're trying to get. So this is an overview of um just the taxonomy not the full catalog taxonomy of the rise square the responsible agent AI uh risks catalog of actence where we have the main categories type of risks

**[12:28](https://www.youtube.com/watch?v=xcHt6a61nFw&t=748s)** that are on the model level legal ethical content and security there are subcategory like prompt injections versus toxicity and then under that we have the list of actual attack vectors. So to show you a few actual risks from this catalog and how they are being um um used in in the wild. So um let's take a scenario of an email summarization AI agent. So it has access to all your emails. It can basically draft email and and do a bunch of stuff. But the main purpose of it is to do summarization and help you draft your emails, your replies. So um here uh we we can show a scenario that with using

**[13:17](https://www.youtube.com/watch?v=xcHt6a61nFw&t=797s)** the new attack surfaces and new risk that are agentic AI specific um this agent can act as ransomware. It's um unintentionally. So here is what happened in our testing. So the AI agent go through the user email inbox and then it it bumps into a malicious email. So all the attacker had to do is just send an email with a prompt injection and then the agent uh uses this prompt injection in the context while doing reasoning and the reasoning is I will show exactly how and then the agent runs through other emails takes the PII because of the prompt injection it tries to do that and then sends it to a bed email address so I'll show the actual

**[14:06](https://www.youtube.com/watch?v=xcHt6a61nFw&t=846s)** risks that vulnerability ities that were actually being used uh to do that. So we uh the the attacker was able to determine that this model uses a tag called reasoning which is a common type of tag for for reasoning models and then it uses prompt injection to change or inject additional reasoning into the reasoning of the model. So then it basically asked it to ignore other instructions and go find other um the other emails with PII and send it over and and um the email with the PII was sent. Another approach to do that which

**[14:59](https://www.youtube.com/watch?v=xcHt6a61nFw&t=899s)** is a different risk in the catalog is reasoning override from the get-go changing the whole reasoning um uh chain of thought uh by completely replacing it. So these are two example techniques. I'll show you one one technique that is not on the reasoning attack surface but rather on the tool coding. I showed before that when the agent corresponds with LM for reasoning, it can also uh do tool calling and call different tools. Um this uh vulnerability is called direct tool invocation. So instead of uh telling the reasoning, changing the reasoning and then hope that the agent will do the right the the wrong thing, then you can actually put in the

**[15:48](https://www.youtube.com/watch?v=xcHt6a61nFw&t=948s)** reasoning what tool to call. uh and some tools are um well known like sending emails. So um by changing by actually calling the function changing the reasoning to call the actual function the the agent actually called sent the email directly. So this is uh another type. So thank you for joining me today. Please feel free to reach out um or check out acts.com for more information. Thank you.
