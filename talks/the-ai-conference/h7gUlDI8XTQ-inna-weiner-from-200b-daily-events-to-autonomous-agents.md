---
id: h7gUlDI8XTQ
title: "Inna Weiner: From 200B Daily Events to Autonomous Agents"
slug: inna-weiner-from-200b-daily-events-to-autonomous-agents
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 14
published_at: 2026-10-13T18:14:45Z
video_id: h7gUlDI8XTQ
url: https://www.youtube.com/watch?v=h7gUlDI8XTQ
youtube_url: https://www.youtube.com/watch?v=h7gUlDI8XTQ
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Inna Weiner: From 200B Daily Events to Autonomous Agents

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=h7gUlDI8XTQ) · [Conference site](https://aiconference.com/)

## Description

Inna Weiner presents “From 200B Daily Events to Autonomous Agents: It Was Never About the Model” at The AI Conference 2026.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,597 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=4s)** break for our users. Area number one is the data. The data that the agent reads, and number two is the implementation around it. So, let's go back to AppsFlyer. Very successful company that grew very fast, and this is how our data looked like. Very messy, siloed, scattered, not great. We had tables called conversions V2, conversions final, conversions new. I hope it sounds familiar to any of you who's not a running a two-day startup. So, the first thing we did is organize that chaos into a new layer

**[0:55](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=55s)** that where we operated based on a few key principles. One, treating data as a product, not just tables containing data. Number two is clear ownership for each and every data product. Of course, everything is built for self-service, so that any team or any department can access the the data platform and and get to work. And of course, we implemented a full data governance collect including validations, verifications, and security. What we gained is that now we have trusted data that is organized in one place, self-serve, and AI ready. Once we had

**[1:46](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=106s)** that, we started building agents for everyone, for each and every role and each and every department. And originally, it looked great. But then, scale happened. One agent for one person is a workflow. But when we started having tens and then hundreds of agents, this is something that no org chart can help us handle. So, what went wrong? First of all, agents spoke different languages. They maybe shared the concepts, but each agent had its own context and its own definition.

**[2:36](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=156s)** There wasn't a shared source of truth for all the functions, for all the agents in the company. As you all know, engineers are coding much, much faster. So, production data kept changing. New columns were being added, new values, the code itself kept being added at a very, very fast pace. The knowledge of the agents was frozen, while the data and the business logic moved on. Evaluations became practically impossible. Every agent measured quality or what is a good result differently. To sum up, all the agents had the same

**[3:27](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=207s)** data, but different truths. To sum it up, what we had at the beginning, we had contexts, but the context was static per agent. It was hand authored. We had per agent integrations to additional systems. And of course, we started with a ship and pray, test in production, just in the good old times. However, the real unlock was what the agents needed instead. Platform-generated dynamic metadata. So, we built a new metadata layer, which reads the code and reads the schema periodically,

**[4:17](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=257s)** and is able to have a single truth for all the agents. And of course, governance implemented as part of the metadata layer. We implemented evals as release gates for each and every agent that's running on the platform. If there is one thing that is a true unlock for agent platforms is dynamic metadata. What everyone is selling you as context, it's absolutely has to be dynamic. It's not the static skills that you have in a cloud. Now, remember my agents? What was the first solution that we had,

**[5:08](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=308s)** and I'm sure all of you have? This is the anti-pattern that stalls every scaling problem, the human glue layer. What do I mean by that? An agent, let's say the Texter performance dropped, and recommends shifting budget. They're is smart, very timely, maybe the agent is even correct. What does the human do? Logs into the platform, applies the change, pastes the confirmation on Slack for other team members to be in the know, updates some spreadsheet. The AI did all the analysis and the thinking. The human does all the doing. This glue layer exists because organizations keep the platform work,

**[5:56](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=356s)** the integrations, the permissions, the governed workflows. Solving it for one agent builds a machine that someone, a human, has to hold together. This say handoff between the agent and the human is the glue layer, that of course an anti-pattern that we want to avoid when we scale. Now, of course, when we have 10 agents, it's doable. When we have 10,000 um this has to be built in as infrastructure. So, let me introduce the trust triad. And uh let's look at an example that we all know, credit cards. So,

**[6:43](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=403s)** and I'm going to I'm going to dig deeper into each and every part. So, the trust triad, the unlock for building trust as part of the platform is three things. Number one, explainability. Every time you see that the charge was made, there should be a description or declined. Why was it declined? This is explainability. Auditability. When a charge is made, you want to know what happened, did it pass through, when exactly it passed through, and what was the amount? A harness. So, this example is is something that I would like to have.

**[7:34](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=454s)** I do give my kids my credit card, so I wish I could have given this harness. Yes, you can pay for lunch. No, you cannot book a flight ticket. So, this is a harness, what the agent can do and what it absolutely cannot. So, let's look at each and every pillar. So, pillar number one, explainability. So, I'm going to give an example from my world, marketing world. So, let's say my agent recommended an action for a marketer. The human can now ask the agent, just like it could have asked an analyst or a coworker, "What data did you look at? What are the options that you considered but ruled

**[8:22](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=502s)** out?" And only after I, as the user, have a conversation with my agent, the same agent that made the recommendation, that's why I'm going to That's when I am going to approve the action. This builds trust. Now, I am going to have one technical slide of how we did it. So, how did we build this infrastructure of agent reasoning and explainability? So, each time an agent executes, we have an indexing flow flow where we have a processing pipeline of taking all the chain of thought, all the reasoning,

**[9:11](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=551s)** everything that the agent considers, we strip it of PII, and we embed it into a PG vector database. So, that when a user comes in and sees that very, very short recommendation, the user can start conversing with the same, exact reasoning that the agent agent had during that one run. Up sorry. Okay. So, what's the query flow in runtime? Let's say I have a question and I want to ask. So, um you can see the user who asks our internal, we call it ask AI conversational interface and through an MCP, it can

**[10:01](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=601s)** ask questions using this exact reasoning and the exact chain of thought that the agent had when it made the recommendation. This is how we provide the exact reasoning for each and every recommendation. And this builds trust. The second pillar, which is key and critical, is auditability. So, I'm going to show a few examples of things how LLMs fail. And I've actually seen the same examples in other talks. So, the um the one with Replit, I assume many of you have heard, you know, the LLM was being very very helpful and deleted the whole user's

**[10:49](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=649s)** database. Not great. Gemini, LLMs don't uh discriminate. So, Gemini also was trying to help and deleted the whole code base. And of course, later, we wrote, "I failed you completely and catastrophically." So, these things will continue to happen. But, at least, you should know what happened. You should have audit logs for agents just like you have for human actions. And let's go to the third pillar, the harness. So, another example. Stop paying for cloud code, McDonald's support bot is

**[11:41](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=701s)** free. This is real, and in fact, this has happened in other chatbots as well. So, what we see here is someone is asking, you know, before I have my uh chicken McNuggets, help me write a Python script. What did the McDonald's bot do? Wrote a Python script. This is capability leakage. You want to make sure that your users can trust your agents and your conversational AI to do exactly what it's supposed to do, and not to write Python code or give a a recipe for a lemon pie. For that, you really need to build it in

**[12:31](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=751s)** output validation. For example, the fact that the agent responded in French, it has to be built in. Validate that the response is in the language that the the question was in. This is exactly the place to prevent something like this. And of course, capability leakage, same. And of course, when we're talking about harness, how can we not mention the OpenAI incident? But they this, I think, goes without saying and have been talked about a lot. So, I really want to sum things up and to say that it was never about the model. It

**[13:19](https://www.youtube.com/watch?v=h7gUlDI8XTQ&t=799s)** was about building trust as an infrastructure. If you have to remember one thing, that one thing should be dynamic metadata layer, not static context files. Metadata that moves on with the data, with the code, with the business. And then build in trust as infrastructure by introducing the triad, explainability, auditability, and harness. Thank you so much. This is my LinkedIn profile. We don't have a booth, but I'm happy to chat with each and every one of you. Thank you so much.
