---
id: 6V6BAb3qG6U
title: "Daniel Fink - Scaling Up Config Driven Multi Agent Networks with Neuro SAN"
slug: daniel-fink-scaling-up-config-driven-multi-agent-networks
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Daniel Fink"]
channel: "Berkeley RDI"
duration_min: 7
published_at: 2026-08-12T07:52:05Z
video_id: 6V6BAb3qG6U
url: https://www.youtube.com/watch?v=6V6BAb3qG6U
youtube_url: https://www.youtube.com/watch?v=6V6BAb3qG6U
tags: []
transcript: true
---

# Daniel Fink - Scaling Up Config Driven Multi Agent Networks with Neuro SAN

**Daniel Fink**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `7 min`

[Watch the recording](https://www.youtube.com/watch?v=6V6BAb3qG6U) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,009 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=2s)** DANIEL FINK: Thanks, everybody. Let's see. A little bit about where I come from. I'm from Cognizant AI Lab. We are a big R, little D small group of maybe 30, 40 people or so centered in San Francisco. We got some people in Bangalore. There's my people. And what I generally do is I take the research problems that are promising and then push them out so that they can be scaled up. And the greatest example of this is like 2 and 1/2 years ago, we were experimenting with multi-agent systems, and we quickly realized that the glue code of agents calling other agents was the noise in what we were really trying to do.

**[0:50](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=50s)** And so we wanted to lift that up. And what we came up with is now known as neuro SAN. And neuro SAN is basically a configuration-driven system where agents can call other agents. Agents can call coded tools. Coded tools can call back into the agent system. And all of this is described in JSON, basically, except, of course, for the code, the coded tool aspect. Every node in the system describes upward to its up-chain callers what it can do, what it needs in order to operate in terms of information, who it can talk to. And then, of course, there's the system prompts overall. And one of the bits of secret sauce about what's going on is that the ultimate up-chain is the user.

**[1:40](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=100s)** And when it comes to secure credentials and stuff like that, we have a side channel of data, which we call slide data, which allows you to put in the tokens that you never want to get in the chat stream, basically. So I'm going to focus on the last two bits here. So early on, we actually figured out that we don't really need to wait for the next great model in order to boost our capability. The real win is breaking your problems down so that a smaller model can handle it and handle it more reliably and more cheaply, for that matter. And the other interesting thing was that when given the right tools, we had all kinds of people starting to make multiagent systems. Even our marketing people had some really, really great ideas

**[2:31](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=151s)** and tools that they still use today. So some of the really interesting things that come from the configuration-driven aspect of these multi-agent systems, I'll start with the second one first-- agentic webs. So if you develop a multi-agent system, it's actually pretty easy for that multi-agent system to then call out to another multi-agent system as a tool, ad infinitum. We can call MCP servers, A2A servers, whatever other agent system you want. We could do that. The other interesting thing is that the common tooling for actually calling our agents in the first place, even with the secrets, is since that's all standardized, the testing itself becomes data-driven in and of itself. This is the interaction that I want to have that becomes data-driven.

**[3:18](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=198s)** And then it gets even crazier because it's the JSON files or HOCON files that describe these systems, they're just forms to fill in. So we now have multi-agent systems that are basically vibe coding other multi-agent systems. And they can call them as a thought, as a perishable thought. They can then be downloaded and used as part of the overall system. There's some other stuff on there I'm going to glaze over. So how can we apply this stuff? It sounds kind of fancy. What we're seeing here in the center is what we call the front man. He's basically the root of the system,

**[4:05](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=245s)** and he is calling out to other agents that are kind of middle tier in the center circle, and then in the outer circle are the actual leaf node agents that are actually doing something. So the example here is a corporate internet. So think of your corporate homepage that you probably look at at least once a week, if not more. And different departments-- HR, finance, IT-- they all have different needs. They all have different agents that actually everybody kind of needs to be able to access. And so the-- sorry, how do I go back?

**[4:58](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=298s)** Here we go. So we have this prompting infrastructure that's called AAOSA. And the idea is that the guy who is answering the current question, he doesn't know anything, but he knows who else to call. And that all trickles down so that different aspects of the same question can be answered by HR, by legal, yada yada yada. So the coordinator doesn't know anything, but the people down below do. And then as information comes up, there is an aggregation of knowledge that happens on the way up. So we actually convinced our corporate IT department to help us eat our own dog food. And currently, they have about 200 leaf level agents coordinated by this AAOSA infrastructure.

**[5:50](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=350s)** Everything from ServiceNow, Salesforce, PeopleSoft-- all the stuff that people know and love. It scales up ridiculously, which we're very happy about. And the results are basically in the ticket counts. So the blue line that starts in the upper-left of that graph and goes to the middle-left of that graph is the ticket count. And the blue vertical line in the center there is when things were deployed-- actually a little bit to the left. And when we deploy that, we basically found we had about 30% drop in overall tickets because the agent system was handling requests better than people overall. And I just want to say that this stuff is freely available. It's agreeably licensed.

**[6:41](https://www.youtube.com/watch?v=6V6BAb3qG6U&t=401s)** We encourage you to try it out for yourselves, and we look forward to actually working with the AAIF to make this happily available in the Linux Foundation. And we're going to have a site, bring your own key site, which this whole system supports, where you can vibe code your own multi-agent systems. Thank you very much. [APPLAUSE]
