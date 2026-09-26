---
id: jA_x7F8caHI
title: "No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle"
slug: no-memory-no-harness-why-the-database-is-the-last-line-of
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["No Memory", "Kay Malcolm"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-09-14T16:30:33Z
video_id: jA_x7F8caHI
url: https://www.youtube.com/watch?v=jA_x7F8caHI
youtube_url: https://www.youtube.com/watch?v=jA_x7F8caHI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Science, healthcare & applied ML"]
transcript: true
---

# No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle

**No Memory, Kay Malcolm**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=jA_x7F8caHI) · [Conference site](https://www.ai.engineer/)

## Description

Half of Kay Malcolm's team sits in Europe and half in the United States, so when the Netherlands side commits code at four in the morning her time, the Americans wake up to the code and none of the reasoning behind it. Git records what changed, not why anyone decided it. AI had made every individual on the team faster without making the team any more productive, and she went looking for the missing layer. Malcolm runs outbound database product management at Oracle, where she has spent twenty years, and her framing is anatomical. If the model is a brain floating in a jar, the harness is the body that lets it act, and memory is the central nervous system carrying context between the two. She walks through five kinds worth distinguishing: short term within a session, long term across sessions, episodic for what happened last time, procedural for the steps taken, and semantic for meaning.

Then comes the storage question, and she answers it with a story about a previous job where every specialized database she took on added two standing meetings a week, one for security and one for patching. Relational made two. Document made four. Graph made six. She quit. The live version of that argument puts four audience volunteers on stage as a relational, document, graph, and vector store, gives them one sentence to remember, and forbids them from talking above a whisper. They cannot agree on who holds the truth, which is the point: an agent asked to reconcile four stores will often guess wrong and spend tokens doing it.

Speaker info:
- https://www.linkedin.com/in/kaymalcolm
- https://blogs.oracle.com/authors/kay-malcolm

Timestamps:
0:00 - The team, and why AI was not helping
3:36 - Git records code, not human intent
5:24 - What an enterprise agent actually is
7:14 - The harness as body, memory as nervous system
8:09 - Five kinds of memory
10:54 - Counting meetings, one database at a time
13:29 - Where should memory actually live?
14:24 - Four volunteers, four databases, one sentence
15:16 - Storing every type in one place
17:01 - A memory broker for a distributed team
18:46 - Shared memory as a team multiplier

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIE New York, October 12–14 — the first AI Engineer Finance mainstage summit
- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*3,054 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=jA_x7F8caHI&t=12s)** Everyone, are we having fun? >> Oh, you've got to give me way more than that. So, let me tell you, um, my name is Kay Malcolm. I am a retired hiphop instructor. So, if I don't get more energy than that, we will start. We'll start. Are you having fun? [cheering] >> Okay. All right. So, here's what we're going to talk about today. Now, you guys have heard a lot about two letters. Does anyone want to guess what those two letters are that I'm going to talk about today? >> Data. That was pretty good. DB. I'm going to talk about AI, but I'm specifically going to talk about agent harnesses. But before I do that, I want to introduce you all to a few people. Is that okay? Yes or yes. Is that okay?

**[1:02](https://www.youtube.com/watch?v=jA_x7F8caHI&t=62s)** >> I gave choices. Yes. Anyway. All right. Okay. All right. This is my team. I run an outbound database product management team at Oracle. I've been at Oracle a really long time, 20 years. Funny story, I started when I was 12. So, don't do the math and don't start start adding in your head. Um, and we've got a problem. That problem is I've got one group that does platform development and then I have another group that does content development for live labs, a platform that I wrote myself. So yeah, I'm an engineer but I'm kind of a developer poser too. And then I've got another group who does QA and then I have another group who does

**[1:49](https://www.youtube.com/watch?v=jA_x7F8caHI&t=109s)** my front-end development with AI. Here's what I found out as a leader. Because in the token maxing era of 2025, because you know, we're not token maxing anymore, right? We are responsible AI now. But in the token maxing era, the thing that I found out was while AI was making the individuals on my team faster, there was another problem it was creating. It wasn't making my team more productive. And the reason was when one team from the Netherlands checked in code at my 4:00 a.m. in the morning because I've

**[2:37](https://www.youtube.com/watch?v=jA_x7F8caHI&t=157s)** got half of my team that's in AMIA and I have half of my team who that are here in the United States. They checked in the code but they didn't check in their context from Codeex. We use Codeex at Oracle. So then when the US team woke up, they got the code but no information about the context. So we used AI to solve a problem that AI created. And here's what we did. Oh well, let me talk about this first. So some of the issues, the context, like I said, wasn't shared. GitHub wasn't tracking that. I had repositories that were diverging and I was asking the managers who work for me, what's happening to your teams? Why why

**[3:27](https://www.youtube.com/watch?v=jA_x7F8caHI&t=207s)** are we not going faster? We're spending all of this money on tokens. We're spending all this money on AI, yet something is missing because we're still spending time doing testing and validation. So our netn net wasn't really wasn't really working for us because git records the code and not human intent. So it's a problem and even though code creation was no longer our problem still had a bottleneck. We needed a collaboration layer. Now, I do have members of my team in the audience, so don't judge me, and you know who you are. I'm not saying that you all didn't collaborate. But now,

**[4:18](https://www.youtube.com/watch?v=jA_x7F8caHI&t=258s)** we've got a new team member, and that new team member is AI. So, we needed to figure out how to track our progress in our next steps. how to rationalize decisions that the agent was making. We needed to figure out how to resolve questions in conflicts. Okay, hold my problem. Will you all hold my problem for me right here? We're going to just tuck that in a little box. Let me define what a enterprise agent actually is. Now, most people think that an enterprise agent is the model and workflow. How many people agree with me?

**[5:08](https://www.youtube.com/watch?v=jA_x7F8caHI&t=308s)** Man, this tough crowd you. Okay, one person. Okay, the rest of you think it's a little bit more. Okay, let's see what could it be that a real enterprise agent has tools. Tools are how it does things. Context. The context. That's a context window. That's what's in the actual prompt. Memory. Huh? And if you're thinking, "But wait, K, memory, you just said that the model is kind of like the brain of the operation." Hold tight. We're going to talk a little bit more about memory retrieval because you don't want to get

**[5:58](https://www.youtube.com/watch?v=jA_x7F8caHI&t=358s)** everything back. So that's being able to to retrieve the right information back. And then I know that there are a lot of developers here and you all don't care about security. I care about security because I work for the most secure database company and I used to work for um agency that has no name. But guard rails is also important. This is the harness. I speak in analogies and I and I speak in stories because if I tell you this and Marvel, you know exactly what I'm talking about. So the agent, think of it as the model, little brain floating a in a glass jar plus this harness. This harness is the

**[6:50](https://www.youtube.com/watch?v=jA_x7F8caHI&t=410s)** body. So it's how the agent can actually do things and get things done. That memory, that's the part of the central nervous system. And you remember the central nervous system connects the brain to the rest of the body, legs, arms. That's the part of the central nervous system that carries context. So you remember my problem with Git. What I needed was memory. Okay, so there are a number of memory types. I chose five, the five most common ones that people talk about and these are the ones that I want you to remember. The first one is short-term memory. That's the session, right? And so if you're storing memory of an AI uh process, that is the

**[7:42](https://www.youtube.com/watch?v=jA_x7F8caHI&t=462s)** short-term memory is if you're with chat, cloud code, right? Codeex, pick your poison. The long-term memory is what persists across sessions. Episodic memory. Hm. What happened the last time I interacted with fill in the blank? That's your episodic memory. Procedural memory tools, steps that were taken. And then finally, semantic memory. And semantic memory because we're talking enterprise agents. We're not talking the agent that I built, Sasha Fierce, because remember I told you guys that I was a I'm a a dancer. So, of course, my my chief of staff is going to be called

**[8:32](https://www.youtube.com/watch?v=jA_x7F8caHI&t=512s)** Sasha Fierce because that was Beyonce. Any Beyonce fans? Okay, I'm sorry. All right, we got to focus. Okay, so these are the memory types. Now, when you're defining this real enterprise agent in this memory, there's something you need to consider where to store it. And so, I'm going to tell you guys a story. But when I tell you the story, you have to promise me that you're not going to judge me. Do you promise? Do you promise >> you're not recording me, right? Because this doesn't paint me in a good light. Okay. All right. The world of data was one simple. I've been at Oracle a long time, but I came from a customer. That customer's name was Southern Company. It

**[9:19](https://www.youtube.com/watch?v=jA_x7F8caHI&t=559s)** was a power company. I'm based out of Atlanta. And I was hired at Southern Company because I was a rockar performance tuner. You had a SQL query. I mean, I'm dating myself, but whatever. You had a SQL query. I knew all of the innit.org parameters. Even the ones when you called support and they said, "Don't remember these. Don't write them down." I wrote them down in my little notebook. I could tune a query within one inch of its life. Then one of you came to my desk because I mean the world the world was rows and columns. It was a great time back in my Albundy days um and said hey I need to store data unstructured. Why I need to do that? And so me being K the the diligent DBA, I was like, "Let me figure it out and

**[10:11](https://www.youtube.com/watch?v=jA_x7F8caHI&t=611s)** get back to you." Did I get back to him? I didn't get back to him. Now, the thing you have to know about Southern Company was for every database system that a DBA managed, I had to attend two meetings. Today, when I hear Sarbain Oxley, I still throw up a little bit in the back of my throat. So I had to attend a security meeting and a patching meeting every week. Never failed. Now because this developer installed a database that was specialized for unstructured. Okay, there are really smart people in the room. How many meetings am I going to now? Four. Okay, I'm a little annoyed, but I'm like, okay, we can we can we can do

**[10:59](https://www.youtube.com/watch?v=jA_x7F8caHI&t=659s)** this. Then they said, "Okay, since you're such a good tuner, I need you to figure out this relationship." Now, the way that Southern Company worked, there was this people could die application, um, and it was a it was like a Nokia phone that people who were climbing the towers, right? So, you guys have have been in a storm and the power goes out, right? And then you're pretty sure that within maybe an hour or two the power will go on. Well, that system that would tell the people who were climbing those trees and risking their lives to turn the power back on sometimes would have false positives or false negatives. So, they wanted to look at all of the other um uh polls in the area to try to get away from the false

**[11:48](https://www.youtube.com/watch?v=jA_x7F8caHI&t=708s)** positive or the false negative. And so I did that in a SQL query and it was it was amazing. It was a five nested union all statement. It was some of my best work. Now it might have taken like 20 minutes to work but it was like a predecessor to graph. Yeah, they they install Neo4j. So now how many meetings am I going to? Six. That's a problem. So I um Oh, let me I got ahead of myself. So you know what I did? I quit. I left and I came to Oracle because I was like this is a problem and maybe I can go to Oracle to help solve it. So then Joe Mundy called me and he said hey um we are installing Reddus. Oracle is late to the game. We've got a vector

**[12:36](https://www.youtube.com/watch?v=jA_x7F8caHI&t=756s)** database. Okay. But here's your problem, Joe. Agents now need access to all of this data. So if data is in an Oracle database, if then it's also in an unstructured JSON database, if it's in a graph database and it's in a vector database, where is your single source of the truth? The agent has to figure that out. Sometimes it'll get it right. Most times it'll get it wrong and it's going to burn up a whole bunch of tokens. And so now if you want to store your memory somewhere, you can store it in a file system. You can store it in clawed or chatgpt because we all know

**[13:25](https://www.youtube.com/watch?v=jA_x7F8caHI&t=805s)** about the memory.md file. But that's going to be a problem. Now I want to illustrate this. I need four volunteers. I can see you raise your hand. One, two. Okay, I can't. Maybe I can. Three. I need a fourth. Ah, fourth in the back. Okay. Fourth in the back. You are going to be our old reliable. You're going to be a relational database. Yes or yes. You got your So, you have your assignment. Okay. And then there was someone here. You're going to be my unstructured database. Okay. And then where was my other? Ah, very good. You're going to be my graph database. You good? Relationship guy. You look like a relationship guy. All right. Very good. Fourth. Where was my fourth? Was it you? Yes. Yeah. You are my vector database. Okay. Now, everybody be

**[14:18](https://www.youtube.com/watch?v=jA_x7F8caHI&t=858s)** really, really quiet. For my four volunteers, I need you all. I'm going to say something to you. And I need you all to decide how you're going to store it and who's going to have the single source of the truth. You can't get up from your seats and you have to whisper because if you talk loud that's 5x the tokens for you. Yes. Okay. Are we ready? All right. The cow jumped over the moon. Go. Doesn't really work, does it? That's a problem. Okay, Oracle. And if you don't forget one, if you forget everything I say and you remember one thing,

**[15:06](https://www.youtube.com/watch?v=jA_x7F8caHI&t=906s)** Oracle is not the Oracle that you think that is why I am here today. How many of you knew that Oracle could natively in the same table down to the same partition store JSON graph vector my vector friend over there my JSON friend spatial you want your memory to be immutable blockchain in the same database raise your hand yeah we have a marketing problem so any data type can be stored in a 26AI database any workload anywhere AWS GCP Azure OCI on prem choice and flexibility so now when we take this and we talk

**[15:56](https://www.youtube.com/watch?v=jA_x7F8caHI&t=956s)** about the agent I want to be able to store my long-term and procedural memory in relational on in JSON I want to store my short-term and my long-term memory graph I want to store procedural because procedural that's how I figure out the relationships right the steps my episodic and semantic memory. I need to do some vector and then store it also as text. Now, if I have four different databases, you all saw they can't talk to each other. It's going to be a problem. And so, what I'm saying to you today is the Oracle AI database is the best place to store this agent memory that's going to power your harness. Remember your harness is your body [music] and that memory is your central nervous system. Okay, back to PY. So the

**[16:47](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1007s)** problem that I had, we solved it with a memory broker named Py. We used agent memory. We got out of that automatic continuity. So with my team, they were able to share not just their code, but PY also kept track of the context. So if one context window was had procedural memory, episodic memory, information about the long-term memory, that was then shared with the other folks on the team. You could call them agents, if you will. They're just human agents shared across forks. The developers on the team remained in control while Polly was able to create the context, figure out which fork and

**[17:37](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1057s)** branch it belonged to and which commit it belonged to. Now this is a very simplistic example but when you take this to the enterprise here's what happens. Memory is the thing that becomes non-negotiable in an agent's harness. Now these are three papers that that I read um on the airplane. This first one is from open AI and it's about its in-house data agent and the thing that it says is it is saying that its in-house data agent actually needs memory. Memory was crucially important to ensure that its agent was able to filter correctly instead of trying to string match. Harrison Chase said, "Your harness, your memory. And if you don't own your

**[18:24](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1104s)** harness, you don't own your memory." Which is key. And then I'm sure you all are wondering, "Well, Claude has memory. Why can't I use that?" Well, it's kind of like file system memory and it works with one, but just like in my example, when you scale past one, and you're going to scale past one in the enterprise, it creates a problem. So Oracle has a Oracle agent memory pap package. PIP install Oracle agent memory. You get access to it. And this memory is this SDK that we have is the thing that will hold your live conversations, your memories, your facts and figure out what is worth keeping. So if we look at Py now, Kevin can share his context with Py, our

**[19:15](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1155s)** memory broker. We use the Oracle agent memory SDK. It's stored in an Oracle autonomous database. We can use the LLM of our choice or we can use a local model through the Oracle private AI services container. And then Linda, who's actually sitting right here, can interact and work with Kevin, no issues. So yes, AI makes individuals faster. Shared memory on an Oracle AI database makes teams faster. So I don't want you all to compromise. In the age of AI, what 26AI does is you can choose and pick what's best for agent memory file system stored in a database file system or in the database. If you need

**[20:03](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1203s)** to do data modeling, you've got JSON, you've got relational. We've got choice. Okay, I've got some goodies for you. The Oracle AI developer hub. That's where you can guys you guys can get coding materials, the applications, what I talked about today. Livelabs.oracle.com. If you've done any of our workshops today, that happens to be something that I wrote myself about six years ago and 40 million users um ago. Spend my OCI tenency money. kick the tires on any Oracle technology um for six hours, 12 hours, however long you need. Um and then I'm giving you all all a Mac Mini. No, I'm just kidding. I'm giving you an OCI Mini. So, I don't know if you knew, but there is an always free OCI. It is the most generous of any

**[20:52](https://www.youtube.com/watch?v=jA_x7F8caHI&t=1252s)** of the hyperscalers where you can get a free Oracle database, free compute, you can send 3,000 emails a month, 200 gig in storage, and if you click on that, you can get access to it. Or just search Google for Oracle Cloud, always free. Connect with me. If you build something, will you all message me and let me know? Yes or yes? >> Thank you. >> [music]
