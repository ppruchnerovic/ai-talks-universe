---
id: TFz0spBvAq4
title: "The Cost Nobody Budgets for When Building With AI Agents"
slug: the-cost-nobody-budgets-for-when-building-with-ai-agents
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 5
published_at: 2026-03-02T13:00:45Z
video_id: TFz0spBvAq4
url: https://www.youtube.com/watch?v=TFz0spBvAq4
youtube_url: https://www.youtube.com/watch?v=TFz0spBvAq4
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# The Cost Nobody Budgets for When Building With AI Agents

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=TFz0spBvAq4) · [Conference site](https://tessl.io/devcon/)

## Description

AI agents can build software faster than ever. But can they actually maintain it?

In this episode, Guy Podjarny and Simon Maple dive into why agentic development is harder than the demos suggest and how the teams getting it right treat context as an engineering discipline, not an afterthought.

They dive into:
• why agents keep rewriting code instead of reusing what already exists
• how AI makes building cheaper but running it more expensive
• why managing an LLM is more like managing a team than writing code
• why defining what you want is the hardest part of the whole loop
• why evaluation looks more like server monitoring than unit testing
A new development paradigm is emerging. The question is whether your process is ready for it.

• Tessl: https://www.linkedin.com/company/tesslio/
• Guy Podjarny: https://www.linkedin.com/in/guypo/
• Simon Maple: https://www.linkedin.com/in/simonmaple/

## Transcript

*1,002 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=TFz0spBvAq4&t=0s)** We think there is a new development paradigm in agentic development. The primary challenges in agentic development are it's non-deterministic. LLMs and agents are constantly a little bit outdated. Their knowledge is at least a few months old from the time the last model was trained. LLMs and agents have a bias for re-implementation versus reuse because creating software is cheaper than ever before. And then I think of LLMs and agents as cheap then expensive. They are cheap in the sense that you can build things so much faster and with so much less human effort than before. But then once you start using them, now [music] Opus 4/6 runs with its fast mode that is, you know, 2 and 1/2 times the speed at 6 times the cost, you know, and already at the top model, it's amazing. It adds up. So, there's a lot of problems there, guy. What is the

**[0:46](https://www.youtube.com/watch?v=TFz0spBvAq4&t=46s)** solution to this? The hammer that we have is context. LLMs eventually are just stateless machines that we pass a bunch of context to when they calculate their weights and they figure out what the next words are. And so, managing what are the words that come in, what is the information that comes in, is really our primary tool. An easy way to understand this is is to think about humans. What are your tools for managing a team? Communication. Well, that that's that's really, you know, how you can work with it, you know, how do you incentivize behavior as in, you know, what do you respond to and how do you respond to it? And there are a lot of types of context. There are rules that you are kind of kind of explicitly and

**[1:35](https://www.youtube.com/watch?v=TFz0spBvAq4&t=95s)** aggressively pushing. There are skills that you are hinting and making available to the agent to try and pull down. There are docs, that is information that is available for the agents to find and use at its time. And I'm sure there will be other variations of how do you drive the agents to consume and load the right context. And and then you have to think for yourself when you think about the development paradigm, how do you manage that context? When we use something like context, what are the what is the key to to using context and making agentic development successful? So, I think there's a bit of a loop here that we can talk about more, but the the sequence of steps are one, you have to define and capture, kind of write down, what it is that you want the agent to

**[2:23](https://www.youtube.com/watch?v=TFz0spBvAq4&t=143s)** do. That's often times quite hard. You know, I think we've had some analogies in our in other conversations where, you know, if someone asks you, "What do you want for your birthday?" You know, you it's easy to say, "Well, you know, you should just know it." Uh but I've got a list, guy. I never thought you'd ask for it. We can start I can start. >> [laughter] >> Uh so, a list is useful. It's useful, you know, something for me to do. >> But it makes you But the doesn't it? When when you know, it's hard to just be able to go uh this is what I want. You have to actually, you know, spend time to think about Exactly. What is the answer? Yeah, and even more so when you have a team, right, that has opinions and preferences. Not everybody agrees things. And so, you have to have some of those conversations and write that down. So, you have to define the correct behavior. And there are many, many levels of that. There might be the correct behavior in a specific product

**[3:11](https://www.youtube.com/watch?v=TFz0spBvAq4&t=191s)** in the specific screen that you're modifying. Uh there might be you know, overall company uh practices or in ecosystems uh best practices. But you have to define that. You have to capture that. It's totally okay to use agents, to use LLMs to help you write this down, right, and then refine it. But these are the documents or the definitions that are important for you to review and to ensure that they are correct. Call them specs, call them docs, call them whatever it is that you want, but you have to define those. Uh once you've done those, you need to evaluate how well do they work. Um I think it's easy to understand that if you wrote uh you know, a 20-page document to the LLM, uh and it was just, you know, repeating and giving analogies and, you know, all all some things like that. Uh, it would be harder for the other one to understand

**[3:58](https://www.youtube.com/watch?v=TFz0spBvAq4&t=238s)** what you meant than if you gave a very concise set of bullets. Again, very similar to humans. Uh, so those are relatively easy to imagine how one might be better than the other, but it it really is a lot more elaborate than that. Uh, and you need to consider different models, understand different formats of communication differently, uh, different, uh, types of instructions married, for instance, code examples versus others that married more kind of looseness. Uh, there are many, many different variations. And so for that, and we've spoken about this at length, including in our last conversation on this podcast, uh, you have to build a competency to evaluate. I find the best analogy here is to think about monitoring runtime systems. The the the closest analogy to have to kind of non-deterministic systems, uh, is is servers. Is they run and we understand

**[4:48](https://www.youtube.com/watch?v=TFz0spBvAq4&t=288s)** that, you know, you have to uh, instrument the systems, you have to, you know, observe them. DevOps has taught us that. And so similarly for agentic development, you have to, uh, be able to assess and evaluate how well does something work so that you you you can monitor, you can try it, you can see how often it works. Mhm. >> [music]
