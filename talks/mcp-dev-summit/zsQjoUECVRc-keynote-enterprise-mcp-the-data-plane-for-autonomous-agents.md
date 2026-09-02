---
id: zsQjoUECVRc
title: "Keynote: Enterprise MCP - The Data Plane for Autonomous Agents - Adam Seligman & Zayne Turner"
slug: keynote-enterprise-mcp-the-data-plane-for-autonomous-agents
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: ["Adam Seligman", "Zayne Turner"]
channel: "Agentic AI Foundation"
duration_min: 10
published_at: 2026-04-13T23:19:13Z
video_id: zsQjoUECVRc
url: https://www.youtube.com/watch?v=zsQjoUECVRc
youtube_url: https://www.youtube.com/watch?v=zsQjoUECVRc
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Keynote: Enterprise MCP - The Data Plane for Autonomous Agents - Adam Seligman & Zayne Turner

**Adam Seligman, Zayne Turner**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=zsQjoUECVRc) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: Enterprise MCP - The Data Plane for Autonomous Agents - Adam Seligman, CTO & Zayne Turner, Developer Advocate, Workato

Connecting agents to tools is the easy part. Governing what they do with that access — what they can reach, under what conditions, with full visibility into what happened — that's the layer most enterprises are still building from scratch.

After 100+ enterprise MCP deployments across finance, HR, IT, and operations, one pattern keeps emerging: every organization is building the same missing layer. Not the model. Not the tools. The data plane that governs how autonomous systems operate inside the enterprise.

Workato CTO Adam Seligman will name the pattern and frame what that layer looks like at scale. Developer Advocate Zayne Turner will open the architecture behind a real deployment — showing how the data plane turns MCP from demo-ready integration into production-ready infrastructure.

Autonomy without control is risky. Data control without autonomy is stagnation. The enterprises that win will build both.

## Transcript

*1,938 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=zsQjoUECVRc&t=0s)** Hey, everybody. Good morning, New York. Uh I'm Adam Seligman at Workato and >> And I'm Zane Turner, also at Workato. And we want to talk about this control and data plane for autonomous agents. And look, I I think all of us that are using this stuff today realize that you, all of you, are building agents way faster than sort of the governance and controls can quite keep up, right? It's That's kind of the moment that we're in. And there's data that support that. Prompt injection risks and and all sorts of this stuff. So, it it's kind of leading all of us, I think, as an industry to think through, what is the correct architecture going to be to support this going forward? Now, we think a lot about architecture. Workato is has been an integration platform for

**[0:47](https://www.youtube.com/watch?v=zsQjoUECVRc&t=47s)** over a decade. We do enterprise orchestration. We do enterprise MCP across thousands of applications. So, our customers are like pulling us to this space really quickly. So, what I thought we could do is dive into the sort of the architectural principles that are in play here. And get right to like a framework for thinking about the path forward and how all of us will make our agents more reliable and really work inside business. That sounds great. So, behind this concept that we're introducing or trying to ask everyone to get behind of the the agentic control plane, there's a core concept of any agentic system really has two layers, two systems, whether or not we fully realize it. There's what we're calling the reasoning layer, the LLM,

**[1:35](https://www.youtube.com/watch?v=zsQjoUECVRc&t=95s)** the agent, that handles things like figuring out the request, whether it was a human or another agent, what what's happening, the intent, what might need to happen next, that sort of what's going on, what should happen. And that's a probabilistic layer. That's a probabilistic caller in our new systems. And then there's the second layer that you may or may not have that is that control plane. That's a lot of the themes that we've been talking about this morning, where governance should live, where authentication and authorization concerns probably should live, where things like your business logic being validated lives. All of those things that make it safe for that probabilistic layer to take action in the enterprise. >> I think we actually saw this in every presentation so far. Yeah. Yeah. And as we say, these are not equal partners

**[2:23](https://www.youtube.com/watch?v=zsQjoUECVRc&t=143s)** because that probabilistic layer may or may not do things correctly, as we've talked about. But the control plane needs to be correct every single time because in business there are consequences. You need one charge. You need a clinician to have the right prescription, those sorts of things. So, that's why that control plane is deterministic. So, you have those guarantees where you need them. And so, we think there are seven factors that can indicate whether or not you actually have an agentic control plane, whether or not you're going to have that healthy system. And it is these seven things, ranging from governed operations, deterministic mutations, all of these things to let you know whether or not you have that. And You want to step through them a little bit? >> Yeah, it's true. Again, when when you build this, uh it was a reflection of work you've done building systems this

**[3:10](https://www.youtube.com/watch?v=zsQjoUECVRc&t=190s)** way and what you and the team have learned from architectural principles. There's nothing specific to Workato here. It's something for all of us as an industry to to think about and how we sort of like that core architectural path to go forward. Absolutely. And this QR code, you can scan it. It's a set of white papers that went live today. This is just the beginning. We're going to be publishing more behind this and we actually want contributors and get a whole community behind this as well. But this is expertise from across Workato, from working with our customers. This is not just specific to us as well. This is distilling what we think the field is probably finding. The themes that you we've heard throughout this morning, it's going to be familiar as we dive into these seven factors. These are, I think, what the field is converging on architecturally. Like if we dive into this first thing about governed operations, we can see it's

**[4:00](https://www.youtube.com/watch?v=zsQjoUECVRc&t=240s)** starts with a simple idea that's hard in execution. The beginning of this idea is that the protocols themselves, things like MCP or as we're seeing people talking about skills MD, agents MD, these agentic protocols, they're thin by design. They are purpose-built for specific things in that reasoning layer. But they aren't taking care of necessarily all of the enterprise concerns. There's always going to be more stuff around the protocol, the standard, the protocols. There's going to be more stuff around that that a business cares about. And we can't just wait for the the standard to adopt those things. They they have to be in place right now for And And they're kind of in some cases unique to a company, right? >> Absolutely. And you can't assume that the standard should take care of it for you. Don't try to put it in a place where it doesn't belong, forcing authentication into a place where it

**[4:48](https://www.youtube.com/watch?v=zsQjoUECVRc&t=288s)** wasn't designed to handle it. Don't don't build that way. Take care of it yourself. I I remember I'm old enough to remember the early days of banking and e-commerce, the site would have a little badge that says, "Don't worry, we use HTTPS." And so, you shopping or banking with us is totally secure. And then I'm like, "Well, there's a lot more than that to go think about." >> Exactly. And if you are in a regulated industry, what you have to protect is you sort of have to turn the dial up depending on how much you need to protect, this becomes even more important. So, that's the core of this governed operations principle is you need to take care of everything that the protocols don't give you. The second thing of determinist mutations, this control plane should own all of the creates and writes and deletes. You shouldn't be allowing that reasoning layer to have direct access to the state that it could destroy. The

**[5:36](https://www.youtube.com/watch?v=zsQjoUECVRc&t=336s)** control plane, that deterministic layer, should be controlling at the the mutations to data that your business cares about. >> Makes sense. Intent-based communication, this is really about that the layer of how, whether we're calling it tool calls or skills, how those probabilistic callers are calling into the control plane, to those systems that you care about. It should be done in ways that are about the tool's intent, what the tool's getting done, not leaking details about the implementation. I think And I think we've seen this a lot recently in like the debate over MCP. And I think this kind of connects to if you start with like your API surface, you just swamp context with a ton of APIs that I used to work at other companies and, you know, like the sequence of API calls needed to get some mutation done was was

**[6:24](https://www.youtube.com/watch?v=zsQjoUECVRc&t=384s)** really complex and that would be get pushed to the LLM. So, this kind of go the other way, start with the intent uh of the tool and then work backwards and then behind that then offer all the API and everything. Do that outside in this deterministic layer. Absolutely. And it's abstracting that away from the reasoning layer for a couple reasons. One, it lets leaves more context for the reasoning layer to do what it's good at, have richer interactions with that human or the other agent. And it's also minimizing that potential exfiltration surface as well, hiding that implementation layer away so it's not knowing what system it's talking to or the 17 underlying APIs. Okay. Bounded access, as we were just talking about whether it's that gateway level filtering or restricting the MCP server tools itself. This is principle of least privilege, but for the agentic era, for these probabilistic callers that have

**[7:13](https://www.youtube.com/watch?v=zsQjoUECVRc&t=433s)** different behaviors. So, figuring out the layers of security that you need to actually make sure that if you have that lethal trifecta and a prompt injected agent, you've made sure that that blast radius is minimized as possible. >> Yeah, least privilege is not new, but it's really important here. Exactly. And the patterns are going to look different in this new system. Safe retries, when you have callers that don't know whether or not they're calling in for the first time or a second time, which is true of probabilistic callers, it's a new game. Suddenly, things like idempotency keys, it's different. Your back-end systems that are used to those external callers being able to send genuinely the same key the same way, your layer for deduping may not dedupe anymore. It's it's a different sort of system that

**[8:01](https://www.youtube.com/watch?v=zsQjoUECVRc&t=481s)** you're going to have to be building for. So, you have to build for different kinds of retry patterns. That makes a ton of sense. And of course, recovery contracts, if retries are different, errors are going to be different. If logic can't always branch deterministically based on a 400 versus a 500, that's just part of a message that is going to be interpreted as a, "Well, then what should I do next?" by a reasoning caller, you have to build different kinds of retry behavior as well. >> Yes, this is robust, reliable, deterministic layer. These are kind of core architectural principles brought forward to this this agentic world. Exactly. So, giving a message of whether or not it's safe to retry to that reasoning caller versus just the static error code. You got the word confabulating in there. Yeah, I like that. And of course, the last one of

**[8:48](https://www.youtube.com/watch?v=zsQjoUECVRc&t=528s)** structural observability. If you're already letting the control plane control the the mutations, the rights that you care about, if you're doing a lot of these great things like the beautiful error handling and the retries, none of this will come for free, but you're getting that observability at runtime. What happened, what was the intent, what system was called and why. Observability by design, not just because a developer decided to capture a log. Yeah, and not like that, the LLMs are a black box. Even if you ask it to tell you what it did, you're not guaranteed to get a truthful answer. So, we have to enforce that outside the deterministic layer. Yeah, absolutely. All right. So, if you want to go deeper, as we said, this is live today. This is just the first cut. This is a living thing that we want to evolve with all of you. You can get it at workato.com/7factors. And of course, you can see some of the

**[9:37](https://www.youtube.com/watch?v=zsQjoUECVRc&t=577s)** principles in action. We have an open source application, Dewey Resort, where we've put some of these ideas in action. You can see the patterns yourself and we'll be around all week. >> And it's it's an open conversation. So, Zane, thanks for getting this started. Many of you will have a different perspective. Maybe there'll be an eighth factor we didn't think of. But we'd really like to make this an industry thing that we can build solidity around so we can raise the reliability bar and the advanced state of agents across the industry. Absolutely. Thank you. Thanks. >> [applause]
