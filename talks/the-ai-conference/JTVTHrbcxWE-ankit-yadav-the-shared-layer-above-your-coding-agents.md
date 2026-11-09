---
id: JTVTHrbcxWE
title: "Ankit Yadav: The Shared Layer above Your Coding Agents"
slug: ankit-yadav-the-shared-layer-above-your-coding-agents
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 10
published_at: 2026-10-07T23:08:05Z
video_id: JTVTHrbcxWE
url: https://www.youtube.com/watch?v=JTVTHrbcxWE
youtube_url: https://www.youtube.com/watch?v=JTVTHrbcxWE
tags: []
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Ankit Yadav: The Shared Layer above Your Coding Agents

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=JTVTHrbcxWE) · [Conference site](https://aiconference.com/)

## Description

Developers now have many capable coding agents, but each lives inside its own harness, interfaces, sessions, and control model. Omnigent provides a shared layer across them. It lets developers compose work across existing agents, move between CLI, web, and mobile while preserving and sharing sessions, and apply contextual policies across agent activity. This talk introduces the meta-harness and explains how Omnigent turns a collection of separate agents into one coherent system.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,919 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=5s)** Please welcome solutions architect from Databricks Ankit Yadav. >> Is this So this is on, right? Okay. Uh hey everyone, good afternoon. Uh as mentioned, my name's Ankit Yadav. I'm a solutions architect at Databricks and I've been with the company for the last two two and a half years. Uh when I heard that I'd be doing a lightning show talk for 10 minutes uh during lunch, I thought it takes me around 10 minutes to actually decide what I want to watch on Netflix. So I'll try and keep this quick just to make sure that you guys get the most out of the session. Uh quick show of hands here. Who's used a coding agent here for real work in the last month? Yep. Uh and can you keep your hands up if you've used two coding agents like a cloud code and a code X? Okay, great. That's That's That's what I wanted to

**[0:53](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=53s)** see. Uh so uh what we're going to discuss today is is basically Omnigen which was launched in June by our CTO Matei Zaharia, who's also the initial inventor of Spark. He open sourced this project for everyone and this is the meta harness. Uh if I had to give you like one word on what Omnigen is, it's a harness above your already existing harnesses. Uh and the problem that we're trying to solve with this is uh initially you start with one agent and one harness, but then as you start seeing the benefits of all these other harnesses, you want to use all of them together. And the harder question becomes, you know, what happens when you want to use several of these agents several on several projects and then with several of your teammates. You know, it's software engineering is is a team sport. You're working with a team developing a project. Uh and that's

**[1:40](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=100s)** where uh you have to work with uh each harness uh where it has its own interface, it has its own session model, its own permissions, and then you know, its own way of working. So it gets difficult if you want to move between all of these. And that's the problem that we're trying to solve with Omnigen because it adds a shared layer above all your coding harnesses. Uh it In today's talk, I'll I'll cover composition, collaboration, and control, and how these are provided by Omnigen for all your harnesses. So, let's get started with the part where today coding agents are actually fragmented in the way that they operate. If you use a cloud code, a codex, or a pie, the each of these arrive in their own different harnesses, right? And the harness decides a lot. It decides where the sessions live, how [snorts] you interact with them, which

**[2:28](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=148s)** tools are available to that particular harness, and how actions get approved on it. This is again, as I said, this is good if you're one person and you're working with one agent. It's all fine, it works well. But, it breaks down the moment you want more of anything. If you add one more one more harness like a codex and a cloud code, then you're now jumping between both of these harnesses. Uh and if you want more of these, then three questions start to arise. You know, how do one is composition. How do agents in these different harnesses work together? Collaboration. How does one person move between say, I start off from my terminal, but then I want to go and, you know, work on my laptop in a web browser or in my mobile app. You know, how do I move across these? And then how do I share my actual session with a teammate? Uh and then finally, control. You know, how do you apply consistent rules across

**[3:17](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=197s)** these harnesses? I can set up rules in one harness, but then the moment I switch to a different harness for a different task, those rules go away and I'll have to, you know, do that again. So, these aren't model questions. These are infrastructure problems, and that's where Omnigen comes in and it helps you solve them by reducing the duplicate work that you would have to do and get locked in into these individual harnesses. Uh Just a moment. Okay. Yep. So, I'll start off with composition. Uh the key thing to note is this is a layer above your agents that you're already running. So, you keep your setup as it is. Uh Omnigent uses the coding agents that you already have. Uh you do not have to, you know, move over from any of your existing agents. You see there's a whole list of configured harnesses that

**[4:05](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=245s)** you can configure and then start using with Omnigent. Uh and then once you have them configured, you can choose by task which harness or which model works on that particular task. So, if there's different parts of a job that need different harnesses and, you know, need different strengths, you can actually do that on Omnigent very easily. Uh an example would be I want my Claude code to do coding, but then I want Codex and OpenAI model to do the review. In one Omnigent session, I can ask Claude code to write the code and then Codex to actually review it. And I will not have to jump between different harnesses and everything happens in the same place. Uh additionally, portability is a big catch here. If you define these tools, policies, prompts, everything in Omnigent, it's at the end of the day it's a YAML file. You

**[4:53](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=293s)** can just pick this up and port it over to another system if you want to. Uh finally, if you want to extend this system, if if you see that your harness of choice is not on the list yet, we will add it, but then if if you feel like you, you know, you want to use one of your coding agents and develop your own agent harness, you can actually use the ACP protocol and define your custom agents and put them into data into Omnigent as well. Uh yep, so keep what you have, use the right agent for the for each task and, you know, you will you don't need to get locked into only one harness. Uh next up is collaboration. I think one thing I mentioned is and this is this comes from one of our founders, Renald, who mentioned that one day he was traveling and going to a dentist appointment and he had his agent running. And so, he had to keep his laptop up slightly open, the lid open so

**[5:41](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=341s)** that he could the agent did not die and, you know, he could it could continue working. So, this is where collaboration comes in and Omni agent helps with this in the way that the agent session does not belong to only the terminal of the harness that you're using. We We have a web version. We have a mobile app version. And once the session is running in the in Omni agent, you can just move between these different surfaces and test them out. Uh yeah, so start in the CLI, continue in the web app, and then check from your phone of how the agent's doing. Uh additionally, the other use case that I mentioned with regards to collaboration was if you and your teammate are working on a project together, uh you can actually share the session with your teammate, and they can come into the same chat chat session and actually work with the same agent that you're working in. So, they

**[6:30](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=390s)** you will not be copy-pasting code and just sending that over or copy-pasting the transcript and sending that over. They will actually see what context the agent already has and how it came up to the decision that it came up to. Uh finally, control. And I feel this is one of the most important ones as most organizations for most organizations, this decides you know, whether any of this actually gets deployed or adopted in in your enterprise today. So, every agent can call tools. It can touch data, take actions, but the risk depends on the actual context of what the agent is going to do. It's not just the action, right? So, I'll take an example that's on the screen right now. So, if you see on the right, if the agent I'll start from the bottom. If the agent touches public information, and it says that okay, I should publish this to the company website. I think this is still okay

**[7:17](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=437s)** because it's already public information. It can go into the public website, and we're fine with that. But say for example, the agent has touched customer sensitive, you know, data that's that has PII. Now, this needs different level of setting when it comes to what the agent can do next. For example, if if it has PII data and it wants to send it to a co-worker, we can allow that. That's okay. If it wants to update a CRM system like Salesforce, uh, it will ask the human so a human can be brought into the loop. Uh, but if it if it says that, "Okay, I have PI and I want to publish it to the public website, uh, company website." That's a hard deny. Uh, so that uh, you can set these kind of policies in Omnigent and then Omnigent will make sure that it follows it as per the context. Uh, and when I say context, that's where if you see the last two, they're actually the

**[8:05](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=485s)** the same action. It's publish data to a company website. But it's the context that has differed and that's why there's an allow for one and there's a deny for the other. So Omnigent is aware of everything that has happened in the session. It has the context of it and only then it uses that context to actually come up with these uh, answers. Yep. Uh, I think to bring it all together and you know, I can say say this that everything that we've covered with regards to composition, we want to we want to make sure that you keep the agents that you already use today and you put them to work together. Uh, we want to make sure that your collaboration uh, piece is also in place. So one session across the CLI, the web, or the app. Uh, and then you can share it with your team and they can work in it in the same session. Very similar to how they do it in Google Docs. Uh, and then controlling all of this

**[8:51](https://www.youtube.com/watch?v=JTVTHrbcxWE&t=531s)** from one place a layer above your agent harnesses. And that's where you know, you have one policy layer and you see the full extraction of it execution of it along all your harnesses. So yeah, keep your agents add one shared layer above them. Uh, and yeah, you can learn more at omnigent.ai. That's my time. Thank you everyone. Uh, one final thing. We we have a booth in Sharday. Uh, we have one of the software engineers who's working on Omnigent. I'll be there. So if there's any questions, please uh, feel free to drop by. Uh, and yeah, we'd love to talk to you. Thank you. >> [applause]
