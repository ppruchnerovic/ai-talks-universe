---
id: kJXtLXMA4eo
title: "Ryan Lopopolo - Harness Engineering: How to Build Software When Humans Steer and Agents Execute"
slug: ryan-lopopolo-harness-engineering-how-to-build-software
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Ryan Lopopolo"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-09T18:48:17Z
video_id: kJXtLXMA4eo
url: https://www.youtube.com/watch?v=kJXtLXMA4eo
youtube_url: https://www.youtube.com/watch?v=kJXtLXMA4eo
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Ryan Lopopolo - Harness Engineering: How to Build Software When Humans Steer and Agents Execute

**Ryan Lopopolo**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=kJXtLXMA4eo) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,265 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=2s)** Hello everyone. Small update from me. Uh it is as of 2 weeks ago, I am at Google. Uh so >> [laughter] >> And uh you know small disclaimer here that these words are mine. Not speaking on behalf of Google here, but we can kind of get into this right now as I back up to the beginning. What is harness engineering? Just to kind of set a base layer uh before we dive into the talk here. It is the mindset and understanding that even keeping the model and its containing harness constant, we are in what we call a capability overhang today. The models are far more capable and far

**[0:50](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=50s)** more intelligent than they are able to side effect into the world today. They don't know what local and global good looks like to their operators. They don't have the context in order to have full autonomy within the organizations in which they are deployed. So it's our role as the humans trying to steward these agents into the real world to give them the tools, context, guardrails, and coaching and trust necessary in order to fulfill the fullness of the job that we want them to do. The reason I'm here talking to you today is because more than a year ago, I had the belief that the earliest versions of these reasoning models were capable of doing my full job. Uh and I kind of put my money where my

**[1:38](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=98s)** mouth was there by not doing my job back in June of last year. Uh I haven't written any code since then and neither have anyone who are on my teams. It's just not a permitted activity. The only thing we permit these humans to do is to get the agent to do the parts of their job that they need to do. And back in June, July of 2025, the models were much less capable. This was a much more challenging proposition. Uh it was not the case that I could get the model to read Slack and respond to pages on my behalf. Just the level of tool usage and capability and complex orchestration was just not there. So, in order to get that to work, kind of had to double-click into the task and double-click and and double-click until

**[2:27](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=147s)** we bottomed out on a thing the model could do. And as you kind of popped back up the stack there to reassemble those capabilities, you had permanently accrued value to the agent's ability to reliably and safely side effect into the world. And as you get teams of people collaborating on a single agent in this way, you really get the best parts of everyone. And this fundamentally is what I mean when I say the way we build software has changed. We can take an agent with level and solve problems with the way it executes by writing code. And code is free to produce now. The model spike very highly in their ability to produce code. In this world though, where implementation is abundant, there are still a couple of scarce areas that require continued investment in order to

**[3:16](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=196s)** make sure that the agent is able to cohere over long timelines, right? Uh it is not the case today even with as advanced the models are that you can say make me a billion-dollar business and you will end up with something coherent at the other end. They are still struggling to operate vending machines, so I hear. Uh so that's really part of what the human expertise in these human agent systems is meant to do. To constrain the areas of latent and physical space that we permit the machine to go in order to make sure we are tracking continuously in the right direction over time. What does it mean to continuously evolve an artifact, whether it is a code base or a word document or a confluence-sized wiki of the organization's knowledge? So, as we think about what it means for

**[4:06](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=246s)** humans and agents to collaborate together, there are three near-term scarce resources that you kind of have to think about in terms of how you think about applying agents and human expertise to go do something. Human time is always going to be scarce. It's actually pretty foundational to how we have built organizations up until this point. When you see platform teams or central dashboards, what you're really trying to do is concentrate a scarce pool of human labor to produce high-leverage things that are able to empower an organization. And that same constraint holds true with agents. One of the things I very often like to say is that when a human or a team of humans are interacting with agents, they must be incredibly ruthless by tracking their time, identifying what it is that

**[4:55](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=295s)** they find themselves doing, whether it's going back and forth one-on-one with an agent to put a plan together, whether it's to review code, whether it's to reject slop. They need to identify what they are doing and then figure out ways to make it so they don't do that. And this natural sort of self-improvement loop will increase the autonomy of the agent part of the system to permit more and more complex, more and more autonomous, and more and more parallel work over time. On the agent side of things, model context window is like a foundational limitation of what it means to put together a model. Context windows may increase in size, auto-compaction may get better, but coherence over long horizon work with a single trajectory is still something that you're going to have to keep in mind over time.

**[5:43](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=343s)** And both human and model and model attention are going to be constrained. This is kind of necessary fact of the world, which means the way we structure tasks and work has to take into account the ability for these humans and models to focus and avoid scattering their attention across many, many competing concerns. I often have had the experience where if I find I need to intervene more than three times with an agent, I'm probably going to have a bad time. Sometimes I will still want to see how I have a bad time, but that's ultimately to learn where the agent has failed to take into account the right things that I needed to do, so I can kind of back propagate, reflect that back into the environment that I provision for the agent, so that the next time I reroll the task, it's able to pull the right bits of context

**[6:31](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=391s)** just when it needs it to avoid scattering its attention. We want focus and the ability to execute on our goals. So, we kind of keep coming back to like how to build good organizations when we talk about building good parallel autonomous agentic systems because a lot of the same principles on how we empower humans in a complex organization apply to empowering agents as well. If you think about what it means to onboard people to your team, you're hiring generally capable humans, but they don't necessarily know what good looks like for you in this context. So, surfacing the collections of non-functional requirements that go into making good local work for you is the name of the game of harness engineering,

**[7:20](https://www.youtube.com/watch?v=kJXtLXMA4eo&t=440s)** and curating context in the background and via tools to constrain the agent's ability to work is what it means to go chase after a well-constructed agent harness. Thank you, folks.
