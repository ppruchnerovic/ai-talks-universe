---
id: Rk9y-27dpko
title: "Skills Didn't Kill MCP: Supabase Engineer Settles the Debate"
slug: skills-didn-t-kill-mcp-supabase-engineer-settles-the-debate
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 23
published_at: 2026-04-13T23:18:16Z
video_id: Rk9y-27dpko
url: https://www.youtube.com/watch?v=Rk9y-27dpko
youtube_url: https://www.youtube.com/watch?v=Rk9y-27dpko
tags: []
transcript: true
---

# Skills Didn't Kill MCP: Supabase Engineer Settles the Debate

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `23 min`

[Watch the recording](https://www.youtube.com/watch?v=Rk9y-27dpko) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Combine Skills and MCP To Close the Context Gap - Pedro Rodrigues, Supabase

Pedro Rodrigues, AI Tooling Engineer at Supabase and co-founder of Lisbon AI Week, argues the Skills vs MCP debate is the wrong frame.** In this MCP Dev Summit talk, Pedro breaks down why Skills and MCP solve different problems, walks through a real Supabase benchmark where MCP + Skills outperforms MCP alone, and shows a Row Level Security bypass that happens when agents rely on training data instead of product docs.
- **Skills vs MCP, explained**: Why one solves integration and the other solves context saturation, not the same problem
- **The three MCP primitives**: Tools, resources, and prompts, and how each maps to a Skills equivalent
- **Tools vs scripts**: Typed JSON schemas and isolation versus instant iteration and self-authored workflows
- **Resources vs references**: Why MCP resources are an underused feature and how Skills reference files fill the gap
- **Prompts vs skill.md**: Agent-pulled workflows with conditional logic versus user-invoked static prompts
- **The Supabase RLS demo**: A team task summary view that leaks data when built by MCP alone, but ships securely when a Skill pushes the agent to search the docs
- **Benchmark results**: MCP + Skills outperformed MCP-only and Skill-only baselines across three Supabase and three Postgres tasks
- **The context bottleneck**: Why capability is no longer the limit for 2026 agents, context delivery is
- **Progressive disclosure in practice**: How Skills load on demand to avoid bloating the window
**Built for engineers building on Supabase, Postgres, or any product that needs AI agents to write secure production code, and for MCP server authors deciding what to keep in tools versus what to push into Skills.**
**Links and Resources:**
- Supabase MCP server - https://github.com/supabase-community/supabase-mcp
- Supabase Agent Skills (open source) - https://github.com/supabase/agent-skills
- Postgres Best Practices for AI Agents (Supabase blog) - https://supabase.com/blog/postgres-best-practices-for-ai-agents
- AI Agents Know About Supabase. They Don't Always Use It Right - https://supabase.com/blog/supabase-agent-skills
- Supabase MCP docs - https://supabase.com/docs/guides/getting-started/mcp
- Lisbon AI Week - https://lisbonaiweek.com/
- Pedro Rodrigues on LinkedIn - https://pt.linkedin.com/in/pedro-neves-rodrigues
- Claude Agent Skills overview - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
**Timestamps (approximate, adjust before publishing):**

00:00 - Intro and Supabase audience survey
01:00 - The Skills vs MCP debate setup
01:30 - Meet Pedro Rodrigues, AI Tooling Engineer at Supabase
02:30 - Quick MCP primer: tools, resources, prompts
03:30 - What are Skills? Folders, not files
04:30 - Anatomy of a skill.md (front matter, instructions, bundled resources)
05:30 - Tools vs scripts: pros and cons of each
07:30 - Resources vs references: the underused MCP primitive
09:00 - Prompts vs skill.md: agent-pulled versus user-invoked
09:40 - The debunk: Skills and MCP solve different problems
11:00 - The pilot and co-pilot analogy
11:30 - Supabase MCP tour: 20+ tools across database, edge functions, storage
12:30 - Building a Supabase-specific Skill
13:00 - The demo: team task summary view with Claude 4.6
14:00 - The RLS bypass: why MCP alone leaked team data
15:00 - How the Skill fixed it with security_invoker
15:30 - Benchmark: MCP + Skill vs MCP-only vs Skill-only vs baseline
16:30 - Trade-offs: more turns, more tokens, more complete output
17:00 - Lessons: MCP alone is not enough, agents default to training data
18:00 - The real bottleneck is context, not capability
19:00 - Wrap-up and Supabase Mac Mini giveaway
19:30 - Q&A: execute_sql and arbitrary SQL
20:30 - Q&A: why Skills over MCP resources for agent-pulled context
21:30 - Q&A: search_docs tool vs web search, keeping workflow out of tool descriptions
22:40 - Close

## Transcript

*3,590 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Rk9y-27dpko&t=0s)** Uh be before I start I just want to quickly survey the the room. Uh how many of you guys have uh heard of or used superbase before? Oh cool. Yeah. So most of the room. Great. Uh so to for any of our fans or regular users, we do have some gears uh some gear uh that we want to distribute. So, my colleague here calling here uh has some um t-shirts and and other things that you be sure to drop by if you want some uh wearables. So, um I'm here. I I hope uh I don't um it's not too many um talks about how uh MCP uh is dead, but it's actually it's not. uh we had talks in here in this ballroom

**[0:51](https://www.youtube.com/watch?v=Rk9y-27dpko&t=51s)** about uh the debate around MCP versus CLI versus code mode versus skills. So this is yet another talk about how MCP is different from skills in this case and how we should use them combined instead of uh against each other. Um as a quick note before introducing myself and starting with the presentation uh I wanted to highlight that I vip coded the presentation. So, what you're looking at, it's actually NextJS app instead of uh a Google slide presentation. Uh, and if you don't believe me, uh, I was actually more of a dark mode guy. So, I think now we're set to for a great start. Uh, thank you. So, for those of you who don't know me, my name is Pedro. I come from a little town in Portugal called Lisbon, which is the capital city. Uh I'm I'm AI tooling

**[1:46](https://www.youtube.com/watch?v=Rk9y-27dpko&t=106s)** engineer at Superbase. Uh and I'm also co co-founder of the Lisbon AI week which is like a week uh all dedicated of AI events happening this year from October 19th to 23rd in Lisbon. Uh I'm also a second time speaker at the MCP Dev Summit. Last time I was in London speaking uh about user on boarding and now I'm here to debunk twice skills are not the MCP killer. uh make sure to follow me on social media uh and connect me on LinkedIn or talk to me after the the presentation. So even though this is an MCP specific summit, I still find useful for the ones that are hearing about MCP for the first time to make a little introduction of of what it is. uh for the sake of this presentation what it's worth to highlight is that MTP is an integration protocol that is composed

**[2:38](https://www.youtube.com/watch?v=Rk9y-27dpko&t=158s)** mainly for by uh three primitives tools which allows the agents to perform actions resources that provide more context to the to the agent and prompts which are basically pre uh templates of uh text that we can provide to the agent. uh we as the MCP uh servers the that guide the user on how to use the MCP server and the workflows. It also comes with another with a bunch of other uh features like oath based on the on the spec uh multiple transports uh uh support sampling and elicitation that I will not cover in this one but are very useful uh when working with MCP and what exactly are skills. So for for the ones who are not familiar what all skills are, skills are folders uh not just files uh as probably most of you have heard about skills uh can think of

**[3:35](https://www.youtube.com/watch?v=Rk9y-27dpko&t=215s)** uh are folders uh containing instructions, scripts and resources. So, I'm not saying that they're just files because probably when you think about skills, you're thinking about the skills.mmd file, the the central file will will you have the main information of a skill. where a skill can actually uh be composed by scripts that you c that you can call from this the skill.mmd file uh to perform actions and also have a lot of references which you can uh think of it at like um attachments on on a book on on an email you can reference from the skill.md these reference files uh for information that are is important to be included but not as important to be highlighted it in the message. So a skill will have this type of format. Let's see if the yeah

**[4:25](https://www.youtube.com/watch?v=Rk9y-27dpko&t=265s)** the the pointer is working. So you can think of a skill.md uh as the an email envelope, right? You would have the envelope as the front matter where you only have the name of the skill and the description. This is what the agent will load once it reads the skill. Uh so it will not load the full content of the file unlike unlikely the um unlike the it does with the MCP server but instead it just loads uh the name of what it what the skill does. If it finds relevant for the workflow it will read the instructions inside of this the skill.md file and then it's also composed and this is an optional one. Not all skills have to have this one. Only the skill.mmd is mandatory. We'll have the bundle resources. This includes the scripts, the references, and the

**[5:15](https://www.youtube.com/watch?v=Rk9y-27dpko&t=315s)** assets that this might contain. So, comparing each primitives, um, if you find both descriptions of the tools, resources, and prompts similar to uh script to the to the skills primitives, well, you're not the only one. There there are some resembles uh on both. And it's uh understandable why well while they can confuse some on why they're competing when apparently they're actually not. So starting with tools versus scripts which are the both primitives for both concepts that allow uh the agents to perform actions. Uh the pros on on MCP tools is that they're basically typed arguments through adjacent schemas. Uh they're isolated. Uh they have their own process and they have they have no access to the credentials. The credentials are usually

**[6:04](https://www.youtube.com/watch?v=Rk9y-27dpko&t=364s)** on the MCP host uh and they can uh be ran remotely. So the agent will doesn't have to have access to a bash to actually run the codes. You can call the MCP server remotely and it will run the the the execute the function for you and return just the output. Uh the downsides of them are basically the schema bloat which has is being uh fixed or or trying to be included in the MCP protocol as you may recall from the talk from David this morning. Uh and other workarounds have been implemented like the uh cloud codes tool search tool or um our codes code execution mode to try to to go around work around uh this limitation. While for scripts, uh they're basically script files. Everything that you know about script files apply here. Uh they're they have no schema, no uh no

**[6:59](https://www.youtube.com/watch?v=Rk9y-27dpko&t=419s)** implied schema, no limitations on the structure. And this could be uh an advantage and also a disadvantage on on its own. Uh you can instantly iterate on it and you'll have instant feedback. Uh you don't have to reload neither the MCP server or the skill to to to load. you just change the script and the agent will uh detect the the change and just run the script with the new behavior and also agents could how to um can self- author scripts so they can create scripts and cannot change the behavior of MCP tools. Uh the downsides are they need shell access. So your agent needs to be plugged or have access to a bash. Um and they might have some portability issues across different environments. Uh commands Linux based commands could have a different um um have a different behavior uh if they're running on Mac OS for example. And if you're running on

**[7:54](https://www.youtube.com/watch?v=Rk9y-27dpko&t=474s)** Windows, well, good luck. The command probably has a different name. Um, for MCP resources, I'll be a bit faster than on MCP tools because tools are probably the most used primitive on MCP. But for resources, they basically appd driven. It's the your application that decides when it's useful to to bring a resource or not. Uh, and essentially there are already standardized across the the protocol. So you you don't have to worry about the formatting. uh the the MCP already established all the the resources to be formatted and distributed. Uh they can be accessed remotely which skills currently cannot uh and they have they can load dynamic content uh based on the input. So you have these templates that you can state on the on the URL to fetch a script uh sorry to fetch a resource uh and that will provide you different outputs

**[8:47](https://www.youtube.com/watch?v=Rk9y-27dpko&t=527s)** depending on the input that you that you give. Um well the the downside is that they're a very underrated feature and they actually haven't been quite adopted um streamlined adopted uh for for skills. Well the this they're basically you can you can tell that the reference files are basically the resources themselves but more agentic friendly if you ask me. Uh it's easier to to find them. it's they they have no structure attached and they can work offline and the agent can also um author them. Uh moving to to prompt. Prompt is also an underused feature of the MCP uh protocol and earlier I was talking with with Curtis from from Google uh about are prompts actually still worth to to to discuss about um and I think for the time being they are but they could be

**[9:42](https://www.youtube.com/watch?v=Rk9y-27dpko&t=582s)** replaced for something like like a skill.md. So what exactly does the skill MD brings that the the MCP prompts don't? Um well they there are agent pools. So it's the agent that controls when to fetch the information instead of instead of being user invoked. Uh and they have rich content uh uh about it. You have conditional logic. You can have multiple workflows and tool callings inside of it while the the prompt is just like what you see is what what you get. So to debunk the the the skills versus the MCP debates, they're solving different problems, right? The MCP is solving the integration problem. Solving you want to connect N M agents with M different services. Uh as long as they talk the the same language uh the the through the protocol the MTP protocol uh

**[10:34](https://www.youtube.com/watch?v=Rk9y-27dpko&t=634s)** the you could connect any agent with any service while skills they solve the context saturation. Why right the biggest uh plus on skills are progressive disclosure. You don't get you don't load everything into context at once. you can just load what's necessary and uh and let the agent discover as it needs for for the task. So, you can think of it like you you get I don't know if there's any uh racing car um fans out here, but you can think of it as the uh the MCP as the pilots and the skills as the navigator or the co-pilot. Uh you would not fire the the pilot just because the co-pilot knows the way, right? So I see the debates uh skills versus MCP this way. Let me tell you about the experience that that we have with skills plus MCP at superbase.

**[11:26](https://www.youtube.com/watch?v=Rk9y-27dpko&t=686s)** So we we do expose an MCP server uh has uh more than 20 tools uh aggregated into categories like the database the edge functions branching storage uh and other features that that Superbase provides. Um I'm highlighting these ones the execute SQL get advisor and search dogs because our uh the ones that are relevant uh for the workflows that we define on on our skills and then we are designing a superbase specific skill for to to define and to help users to use superbase as a product uh that it's not out there yet but I can tell you that is along these lines. So uh it motivates or incentivize the agent to search the docs because we found out that agents are very lazy to go beyond their training data and they need a push to search the web or to find the right information uh

**[12:17](https://www.youtube.com/watch?v=Rk9y-27dpko&t=737s)** to to to to actually get up-to-date information on the product. Uh we get a security checklist because we are very concerned with security and want the approach or the the solutions that the agent builds on top of superbase to be secure from the beginning. uh and we would like to include some opinionated workflows for example on schema management how we think it's more efficient for the agent to securely and efficiently change a database schema uh we without getting a bunch of migration files or without messing the the production database. Um so giving you an example uh we gave the um uh an agent in this case cla 4 4.6 six the same prompts. uh when changing an application like a collaborative view, you can think of

**[13:10](https://www.youtube.com/watch?v=Rk9y-27dpko&t=790s)** like a Trello or or a or a Jira application like a collaborative team tool um to provide okay you have for different teams tasks like different teams have different boards now for each team we would like to have a view so we will be the we'll build the postgress view uh on to summarize the the task so to list the task tasks that have been done the pro in progress and on to-do. Um so the prompt was very simple. We just said create a team task summary view uh so team members can see how their team is doing. So in the case where we just provided the MCP to our um to to the agent uh the MCP had the execute SQL uh apply migration and the search docs tool uh on on its disposal but it completely ignored the search docs. decided that he knew he knew what

**[14:04](https://www.youtube.com/watch?v=Rk9y-27dpko&t=844s)** a Postgress view was and he was going to build one. Um it executed that SQL on the database uh and found well here's your here's our view now the users can see the the team the their team is doing. The only issue was on Postgress when you build a view on top of a table that has row level security enabled and if you don't know role level security it's basically enables on a database level the that the users can only see the data they have access to. Uh so when you build a view on top of a table that has RLS enabled uh it bypasses the RLS. So in in this solution uh provided by the MCPon um condition um the view showed this team summary but also any other team summary. Well, this

**[15:01](https://www.youtube.com/watch?v=Rk9y-27dpko&t=901s)** internally for an internal tool it's okay if you're exposing this to your users. You do do not want this data leak uh to um when you're shipping new uh applications when you're using agents, right? So with the with the skill it actually because we have uh incentivized to search our docs it actually built with this with security invoker which is the flag that it should enable to keep the RLS uh policies from the tables into the view and now this solution was way more robust and secure that the one presented uh by by the MCP only. We didn't just satisfy ourselves with just one prompt. We decided to run this using our internal tool evaluation tool uh to run against three superb specific projects uh and three uh postgress specific uh problems. So to be sure that

**[15:56](https://www.youtube.com/watch?v=Rk9y-27dpko&t=956s)** we are just not overfeeding on our products and surprising surprisingly or not surprisingly um the MCP plus the skill for superbase for both superbase and postgress specific uh um tasks perfor outperformed any of of the other conditions. And just to uh give you some context, the baseline here is that without any MCP or skill at all, just the tools that the agent has uh on its uh on its display. Uh was also not uh worth to note that yes, the the MCB plus skill took a bit more um turns. So it it allowed the agent who would would actually perform more actions uh when when working and it also averaged uh an increased usage of tokens. But I would argue that if your final version it's

**[16:49](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1009s)** it's more complete or secure than without the skills. I think it's a a good tradeoff. What we learned about using skills with MCP at superbase was one MCP alone is not enough. It's good as it stands, but the agent can go as far with the tools as long as it knows how to how to work with them, how to use them. Uh agents default to training data quite a lot. So they if you're building a product, it's extremely useful to guide them to the documentation, the uh up-to-date documentation that you have because they really need a push for it. they would never be able to um to to to implement the security uh the the security invoke flag if we didn't incentivize to search the docs. And finally, we do think that the bottleneck here is context, not capability tools.

**[17:43](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1063s)** Uh and MCP in general, it's already capable enough. If we circle back 10 months ago, uh sorry, not 10 months ago, this was the last MCP dev summit. uh if we circle back to November 2024 when MCP started uh the agents uh we would not trust the agents to perform basic tasks without human supervision. Nowadays agents are way more capable uh and on deciding which tools to use detecting workflows and uh deciding what exactly what the user wants or what how to um deconstruct the prompts for the the user intention. The real issue is uh how to get up to date and um know how to work with the with such rapid evolving products that we have at the moment. So while I uh finish, if you want to try Superbase and see and hopefully in in an upcoming weeks working with the

**[18:36](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1116s)** Superbase skill, we're actually running uh a giveaway. So feel free to participate. just enroll on the um on the platform and uh have a chance to we to win a a Mac Mini. For me, that was all. I would love to discuss with you about uh anything related to build uh both an MCP uh production ready or a skill for a product specifically and also to discuss better ways and more efficient ways to distribute skills which we think are currently the the the limitation for for uh the ecosystem. Thank you very much. I give you time to sign up for the for the giveaway. Uh and without wanting to get to try to steal the spotlight or giveaway, does anyone has any questions

**[19:28](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1168s)** about the presentation or the topic? >> Yeah. >> The benchmark We have uh an execute SQL uh tool uh to allow the agent to run arbitrary SQL uh whenever it feels like it needs to do some changes on the on the database. >> Yeah. If I understand >> exactly >> I guess one question is why not >> that's a very interesting question uh which I think the the the best uh

**[20:28](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1228s)** argument that you could have of skills over uh MCP resources are that MCP resources are uh userdriven or applicationdriven. Well, you would will have to have a human or someone to say this is relevant for your context while skills are loaded by the by the agent. The agent realizes and is currently smart enough to understand I need this piece of information to be loaded into my context so I know how to in this case work with Postgress securely. Right? So if you want to get rid of the the human in the loop for some workflows uh I would argue that using a solution like skill which is agent pulled it's better than using the an MCP resource. >> One last question sorry this general search is search also a tool or what powers that

**[21:24](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1284s)** >> we do we do have a a search docs tool as well. So uh for this benchmark uh the ba on the baseline agents currently also have native web search tools like uh web fetch or web search. They would use that one if they don't have access to our MCP server. On our MCP server, we have this search docs which is actually built on top of our GraphQL um um API to to search our documentation through this uh um not not saying reax but like a this query per right it's a it's more sophisticated than just a web search. Um the thing is uh when does the agent actually knows uh when to search the docs and you don't want to bloat or incrementally or define the workflows or

**[22:16](https://www.youtube.com/watch?v=Rk9y-27dpko&t=1336s)** the use cases where when the agent needs to search the docs on the the MCP tool you don't want to bloat the context right you want to say this tool is used to search superbase docs that's it that's what the the other part the workflow when to search how to search you should keep it in a skill outside of the MCP server. Well, I I think we we ran out of time ran out of time, but I'll be around today and tomorrow. So, please do find me and happy to hear your questions. Thank you. Run.
