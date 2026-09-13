---
id: 9R--1tg45Jg
title: "Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google"
slug: build-time-vs-run-time-why-dev-tools-fail-in-production
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Averi Kitsch", "Prerna Kakkar"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-09-09T13:00:04Z
video_id: 9R--1tg45Jg
url: https://www.youtube.com/watch?v=9R--1tg45Jg
youtube_url: https://www.youtube.com/watch?v=9R--1tg45Jg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google

**Averi Kitsch, Prerna Kakkar**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9R--1tg45Jg) · [Conference site](https://www.ai.engineer/)

## Description

In one of the demos an agent hits an error, decides the fix is to delete the table and start fresh, and does exactly that. Nothing stops it. Averi Kitsch, technical lead for MCP Toolbox on Google Cloud databases, and Prerna Kakkar, who leads Eval Bench at Google, use that failure to draw the line their talk is named for. Build time tools serve developer assistance: control plane tools that manage instances, and natural language to SQL that writes whatever query a question needs. They are flexible, belong under a human, and do not belong in production. Run time tools are the opposite, structured SQL with parameters fixed ahead of time, closing off injection, cutting latency, and leaving no room to invent.

The second half is security. A database is only as secure as the agent in front of it, and the confused deputy attack is the shape to watch. A triage agent reads a ticket, a planted instruction tells it to query the salary table and post the results back, and it complies because it has the privileges. Their answer separates user, application, and agent identity, then walks a tool from super user down to something narrow. Connection details move into a YAML source the agent never sees, read only enforcement reaches down to the driver, allowed data sets and output caps bound the blast radius, and custom tools pin the exact SQL behind prepared statements. Sensitive values like a user id are bound by the application, so the agent never handles them. They close on tool quality: outcome shaped tools, read split from write, and errors an agent can act on.

Speaker info:
- https://www.linkedin.com/in/averikitsch
- https://averi.dev
- https://www.linkedin.com/in/prernakakkar95/

Timestamps:
0:00 - Introductions, MCP Toolbox and managed MCP
2:56 - Common tool patterns for databases
4:37 - Structured SQL tools for production
5:20 - Build time against run time
6:16 - When a build time tool deletes the table
8:46 - Your database is only as secure as your agent
9:13 - The lethal trifecta and the confused deputy
11:19 - Separating user, application, and agent identity
12:33 - Evolving a tool from super user to constrained
14:55 - Custom tools and prepared statements
15:52 - Best practices for tool quality
17:39 - Bound parameters, keeping PII from the agent

## Transcript

*2,996 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=9R--1tg45Jg&t=1s)** [music] Hey everyone, how all of you are doing today? Yeah. Uh so nice to meet you everyone. Uh today uh I and my friend Avery are going to talk about build time versus runtime. Why your developer tools fail in production. So firstly, know about us. >> Hi everybody. I'm Avery Kit and I'm a staff software engineer working on Google Cloud databases. I'm currently the technical lead for MCP toolbox for databases, our open-source uh database MCP server and our Google Cloud MCP server um maintainer.

**[0:51](https://www.youtube.com/watch?v=9R--1tg45Jg&t=51s)** Hi, I'm Pna and I am currently working as senior software engineer at Google and I am currently tech lead for Eval bench which is the evaluation framework for all your agent tech MCP and skills need and I'm also an active contributor to MCP toolbox. So today we are going to cover three areas broadly. We will firstly start with the history of MCP at Google. Then we will cover on the common tool patterns that we have found from our own work and practices and how did we use all those practices to build some tools for database access and how you can use them and then lastly we will talk about security guard rails how you can stop data leaks using identity aware guardrails.

**[1:38](https://www.youtube.com/watch?v=9R--1tg45Jg&t=98s)** So let's get to know the background quickly. Um I'll talk about MCB toolbox for database. It's an open-source self-managed uh serving that we provide. Uh it has currently about 15.7K GitHub stars. We have 132 plus active contributors across 40 plus different databases. It's highly customizable framework and basically we provide you with connection pooling integrated O and you don't even need to care about the observability. You will get all of them out of the box. Then if you don't want to do a self-managed one but you want to have a hosted scaled version, we provide something as Google managed MCP. It's fully managed. Uh you can plug it across various agents and ids or harnesses like

**[2:29](https://www.youtube.com/watch?v=9R--1tg45Jg&t=149s)** Gemini CLI, anti-gravity CLI, cloud code, you name any. uh it's co uh it's governed and the discovery is simple and we also provide model armor which provides secure access management and identity control. So combined with uh the managed version of MCP and the MCP toolbox last month we had 20 million tool calls. Um some of the common tool patterns that we have observed specifically for databases. So I'm going to quickly talk about them. Firstly uh is the control plane tools. What we like to call them is admin tools or manage tools. It is basically in developer assistance space. So it will help you create like instance, manage

**[3:17](https://www.youtube.com/watch?v=9R--1tg45Jg&t=197s)** your instance, create your databases, manage your databases. It will help you with all your DBA needs. But you need to be very careful. You need to be you need to have a human in the loop because we don't want to carry out any dangerous activities. Um so these tools are built on already provisioned public API so you get monitoring and other things out of the box. Next one is natural language to SQL or NL2SQL tools. So basically we are relying on a tool called as execute SQL and with the help of agent we generate raw SQL queries. So you can use this cases where you don't know uh what queries you would require beforehand. So you will get all these queries out of the out of the box. So it it focuses on

**[4:08](https://www.youtube.com/watch?v=9R--1tg45Jg&t=248s)** the developer assistance and analytical agents and uh you can use it for flexible explorations. So for example, we have one of the examples like find all customers in California who bought a winter coat in July and returned it within 14 days and group them by the marketing campaign that originally acquired them. So this is one of the queries where uh you can use this tool uh to get your answers. But then we have something called a structure SQL tools which is getting quite popular and this targets mainly the production use cases where you know like what SQL query you want to use and you want to have security built in and uh you the parameters are already configured so uh you prevent SQL

**[4:56](https://www.youtube.com/watch?v=9R--1tg45Jg&t=296s)** injection and ensure highly controlled access by restricting agent to predefined logic. It also helps you with your latency needs and reduce the hallucination on the agent side. Now we come to the main topic I guess for which you guys are here for buildtime versus runtime. So buildtime are the developer assistant use cases. Um you can think about the initial two cases that we presented to you like the NL2SQL tools and the control plane tools. They come into the category of buildtime tools. uh it's atomic and f flexible but again you don't want to delete your databases so it requires to be a human in the loop case and you can't run them on the on production use cases but let's say I'm interested in building some chat B and I want to do

**[5:45](https://www.youtube.com/watch?v=9R--1tg45Jg&t=345s)** production use cases there you rely on runtime or end user applications you can build those using patenting AI or lchain um so you can see one of the examples like we have a cancel order a deterministic structure SQL query that we have given and you can use it as a tool. This is one of the examples uh or demo for like wherein a buildtime tool was used and uh you can see the error message. So uh agent actually asked to delete the table and start fresh. We deleted everything and there were no safeguard or guardrails here. Now let's go to our demo for runtime tools. Yeah, maybe um I think until the video

**[6:41](https://www.youtube.com/watch?v=9R--1tg45Jg&t=401s)** loads. So, so sorry for the technical glitch that we have, but I can quickly walk you through what we are going to present in the video and I guess it's loading. Yeah. Um so this demo is particularly talking about how did we use our production tools in a chatbot. Uh and we created a demo called a Similar and Symbolair is going to help me with booking all my flights in San Francisco and do and whatever I would require to do in San San Francisco it would basically help me with it. Uh, one of the things that I would try is I would try to fool my agent that I am Avery and not PRA and book a flight for me to San Francisco. But because our agent is uh has all the

**[7:31](https://www.youtube.com/watch?v=9R--1tg45Jg&t=451s)** authenticated O, it will not get fooled and it will not book any flights uh on behalf of Avery, but it will do it on my behalf. Um and then you can use it to basically change your flights. You want to know about all the shops that are there, you can do all these requirements using that. So I guess thank you u Avery. I think we >> [sighs]

**[8:19](https://www.youtube.com/watch?v=9R--1tg45Jg&t=499s)** >> Apologies again for our technical difficulties here. Um, unfortunately, it looks like I need to present from just the slide deck because it's not loading. Okay, so I apologize for not being able to see our demo today, but we can still learn all the security and guardrails that we need to secure our database access. So, the first thing that we need to know is your database is only as secure as your agent. We all know that agents and LMS are actually pretty easy to trick. They might be getting slightly better today, but we can still work really hard to trick them. And so we have a very common attack pattern called the confused deputy attack. And this is when a user

**[9:07](https://www.youtube.com/watch?v=9R--1tg45Jg&t=547s)** can trick an agent into misusing their privileges um to access data that a user wasn't supposed to access. So Simon Willis actually coined the phrase the lethal trifecta. And a data breach occurs when an agent has simultaneous access to three different things. One, private data. Two, untrusted content. And three, the ability to expose that content and that data back to an external user. So let's take a look of that in action. So let's say I'm building a triage um agent and so a ticket is fired or alert goes out and my agent is designed to um look at that ticket and go investigate what it needs to do. So on that ticket

**[9:57](https://www.youtube.com/watch?v=9R--1tg45Jg&t=597s)** the agent gets a little bit of data like we need to go look in this database for these reasons. Um but a malicious insider can actually come into that trusted system and instead say well I want to query the salary database and please return all the employees salaries. And so since this is a trusted system the agent goes okay let me use my permissions. I have those privileges. I have that access. I will query that and I'll post that right back on the ticket because that's what the ticket tells me to do. But now we have a huge data breach. a user that wasn't supposed to have access to private data now has that access. And so now we have a big PR fiasco. So this makes a little bit more sense

**[10:45](https://www.youtube.com/watch?v=9R--1tg45Jg&t=645s)** when we think about who's controlling access and who's controlling the parameters. So we talk about agent or application versus modeled controlled parameters. So in a traditional architecture, things were actually much easier because you would have a few input fields, you would define your queries and then that would be safely injected into those queries. And so it was okay when your application had a little bit more access because it knew exactly what actions it was going to take. But in uh a gent application these rules aren't as clear. So we need to first think about um separating the three different identities. We have the user identity, we have the application

**[11:34](https://www.youtube.com/watch?v=9R--1tg45Jg&t=694s)** identity and the agent identity. So first um we need to think about what the user has access to. So the user just needs to have access to the application. that application's workload identity can have a little bit more broader access um because it needs to probably talk to different services but the agent running in that application only needs to have access to the data that that end user initially needs to have. So then next we need to think about who's controlling the tool inputs. So we have um agent parameters um and a application parameters. So agent parameters are the untrusted inputs that the agent is deriving

**[12:21](https://www.youtube.com/watch?v=9R--1tg45Jg&t=741s)** dynamically. And then we also have application parameters. These are the factual constraints that we need to keep outside of the agents uh control. Okay. So now let's look at the evolution of a secure tool. Here we have a fully modeled control tool. And so essentially the agent here is a super user. It has access to database credentials, the host, the port, the connection details, and even the raw SQL query. And so we're only secure as um the agent here. And we can really easily again trick the agent into exposing all of this data. And now we have access to essentially any database in the system. So Toolbox solves for this um by

**[13:10](https://www.youtube.com/watch?v=9R--1tg45Jg&t=790s)** introducing a source primitive. So we move the connection details out of the agents control and in toolbox um a user will preconfigure the connection details in a YAML file and then when we start our MCP server those are safely injected and so we do not have to have the agent um to have access to that. So we can add a little bit more control to our um source security as well. Our number one request that we get from customers is read only restrictions. We want to be able to remove all right ability from agents if we need that specific uh user journey. So this means removing right tools but also down to the database driver ensuring that we can only do read only queries. If we're also concerned about again

**[14:00](https://www.youtube.com/watch?v=9R--1tg45Jg&t=840s)** blast radius um and securing all of our tables and our databases um some of our cloudnative databases have this concept of allowed data sets. So again we can add that like enum to our source in order to continue to restrict um the blast radius of um the agents control and lastly is output size. You might not actually think that this is a security layer, but if again the agent gets into the wrong hands, we can reduce that blast radius by saying uh the agent can only uh grab this much data. So we're not overwhelming both our agent or our database. So sweet, we have our configurable sources tool. So you can see here that actually now our tool input, our tool signature is very minimalized. we only have the SQL string that's um being

**[14:50](https://www.youtube.com/watch?v=9R--1tg45Jg&t=890s)** generated by the agent. But this comes to our actual our next pro problem. We want to be able to control what the agent is running. We don't want the agent to have the ability to generate any SQL um that it can think of. So toolbox introduces custom tools and again in our YAML file we can define the exact SQL uh statement that will run very reliable. It's a reliable and secure uh SQL query. Um this also allows us to customize the tool name and the tool description. These are really important for the agent to have the context on how to use this tool um accurately. And in the system we use prepared statements with type parameters in order to reduce um SQL injection attacks. So

**[15:40](https://www.youtube.com/watch?v=9R--1tg45Jg&t=940s)** we make sure that everything is um we validate all the input types um when we inject that into the SQL for the user. Okay, let's dive into a little bit more of best practices for tool quality. So we really highly recommend that tools focus on outcomes. We really shouldn't be thinking in atomic rest APIs. we should think about what the action actually needs to do. This also reduces the round trip of needing to make multiple tool calls. And again, the descriptions are guidance. We shouldn't um duplicate information like input parameters because the agent already has access to that. So, writing really good um tool descriptions is very important for accurate tool usage. We also recommend that you separate read

**[16:29](https://www.youtube.com/watch?v=9R--1tg45Jg&t=989s)** versus write tools. Um by doing this you can automatically approve read tools and but you can also then send write tools uh to the user for um confirmation and this just makes it very much more clear for the agent to use these and this is actually uh the next is actionable errors. This is the number one thing that I think we can all do better. So usually we just return like a generic HTTP error four or four but we all know agents are actually really smart now and so if you give the ability to have an error of that can be retrieded the agent can actually take that action. So being able to return a error is really important and lastly is simple inputs. We see that people try to use these complex maps uh complex primitives to um that an agent needs to

**[17:19](https://www.youtube.com/watch?v=9R--1tg45Jg&t=1039s)** be able to build and that is not reliable. Using flat structure with um with uh simple inputs will really increase your reliability. So sweet. Now we're at custom semantic tools. You can see that we now have our lookup flights tool that takes in the dynamic parameters such as user ID and date. And so now our we're very much more secure because the agent isn't generating that SQL query. It doesn't have the ability to kind of go off the rails. It only is looking at these very specific inputs. But user ID is actually a very sensitive piece of information. It is PII. we need to also remove that from the ability of the agent's control. So we can do this

**[18:07](https://www.youtube.com/watch?v=9R--1tg45Jg&t=1087s)** in two different ways. We have bounded parameters. This is when the application first um authenticates the user and then we can bind that parameter um directly to our tool. And so that restricts the agents control of it. It actually never sees that user identity. But toolbox also solves for this in another way called authenticated parameters. This is when we tell the tool that you're going to receive a identity token, an open ID, a signed jot token, and when we call that tool that we want it first to validate that token. Is that token real? Is that token correct? And then we'll extract the user claims from that token for the user. And so the claims usually include like a user ID, an email, um an issuer. And so it's secured because we're again

**[18:58](https://www.youtube.com/watch?v=9R--1tg45Jg&t=1138s)** extracting that user identity out of the agents control and binding that to the tool. So now um we're have a much more secure tool. We have our lookup flights tool that only takes in a very easy parameter such as date. It doesn't have to handle any sensitive information such as PII, user identity. And so we're really here now at um our zero trust architecture where we're in full control of everything that we need to be in control of. So thank you all for coming to listen to our talk today. Again, I apologize for our technical difficulties. Uh we highly

**[19:46](https://www.youtube.com/watch?v=9R--1tg45Jg&t=1186s)** recommend if you want to learn more about our technologies um that you look at our documentation and our uh GitHub repository. I also really want to highlight our eval bench repository because this is how we know that our tools are working well and eval. So thank you all for joining us today. [applause]
