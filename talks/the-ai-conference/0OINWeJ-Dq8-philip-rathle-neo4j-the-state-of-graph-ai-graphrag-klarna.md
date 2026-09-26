---
id: 0OINWeJ-Dq8
title: "Philip Rathle, Neo4j: The State of Graph AI: GraphRAG, Klarna, and beyond!"
slug: philip-rathle-neo4j-the-state-of-graph-ai-graphrag-klarna
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 15
published_at: 2026-09-21T23:29:39Z
video_id: 0OINWeJ-Dq8
url: https://www.youtube.com/watch?v=0OINWeJ-Dq8
youtube_url: https://www.youtube.com/watch?v=0OINWeJ-Dq8
tags: []
topics: ["Governance, ethics & regulation", "RAG, retrieval & knowledge"]
transcript: true
---

# Philip Rathle, Neo4j: The State of Graph AI: GraphRAG, Klarna, and beyond!

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=0OINWeJ-Dq8) · [Conference site](https://aiconference.com/)

## Description

Philip Rathle, CTO, Neo4j

The State of Graph AI: GraphRAG, Klarna, and beyond!

Over the last year, the use of knowledge graphs in AI has exploded. The need for AI knowledge and agentic memory has driven companies like Klarna, Walmart, and Uber to use graph databases at the heart of their AI infrastructure. GraphRAG is becoming a popular way of solving for accuracy, explainability, and governance. Graph data science offers myriad signals that can be used to better understand, predict, and engage with your world. In this talk, Neo4j’s CTO will recap key techniques and latest advances in graph AI, when they are proving to boost AI success, and how to best get started.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,565 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=0s)** Thank you Yuri. So we'll stay with the topic of graphs. Our next speaker last year gave one of our more popular keynotes where he introduced the concept of graph rag and today he'll give us an update on what's the latest. Uh please welcome Philip Bradley of Neo4j. Hope you're allergized and I'm going to try to give you a lot in the next 10 minutes. I was here last year and want to do a quick flashback to where we left off last year to set the stage for talking today about what's happened in the last year in this area because there's a lot going on. So a year ago really the observation was we were at a time when a lot of people were building AI their first AI application and so what do you do? Well,

**[0:47](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=47s)** you're going to start with just LMS. You might fine-tune big models, small models. And a lot of people were realizing that they weren't able to meet the bar that they had for whatever it was they were building. And that bar usually had something to do with accuracy, explanability, or being able to apply privacy or security controls to their data. Enter vector-based rag. So, that was sort of all the rage a year ago, and that definitely raised the bar. But what we were starting to see the beginnings of just a year ago was that you needed to do more and that more um there's this technique called graph rag which looked very promising and a lot of people were having early success in there's a great analogy here with Google who I think of as you know being a graph

**[1:35](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=95s)** person is the world's first trillion dollar plus graph company and there's a good analogy um in parallel with full text being maybe the 1990s version of vector based search and they disrupted that space where everyone else was doing that by introducing a way to rank the text results based on a graph of the topology of how all that data was interconnected. And then they won up themselves 12 years later with a Google knowledge graph which is effectively you could say digital twin of human knowledge which represents the things that are actually being represented on inside of all the pages. And if you go into a Google search now and use AI assisted mode, it's actually using LLM but also their knowledge graph in the background. So great analogy with

**[2:22](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=142s)** what we were saying last year. We define graph very simply as saying like it's just a call to an LLM that includes a call to a knowledge graph at some point along the way. Talked about the benefits and those of you who were in Nia's talk yesterday had a chance to deep dive into some of the basis for this. But answers easier development really stemming from the fact that once your data is in a knowledge graph, it's understandable by the machine but also understandable by humans. So it gives you a bridge between human and machine and then explainability and governance being able to apply access controls to the data that you're using. And then last but not least, we drew a parallel with the human brain and said, well, if LLMs kind of behave a little bit like the way we think of the right

**[3:10](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=190s)** brain, which is spontaneous, creative, mostly right, sometimes wrong, and I never know why, that the knowledge graph, both in terms of the data, the memory, memories it stores, and the way you can run certain times of reasoning against it, gives you something of a left hemisphere for the kinds of AI problems that need both sides of the brain. Okay. So, where does that leave us today? What's happened? I included CLA in the title of my talk because they're widely known as one of the large enterprise successes in AI. Um, they got massive employee productivity boost out of their Genai um uh chatbot called Kiki. It's like caro wiki. And it turns out that this was um backed by Neoforj. they went a step

**[4:00](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=240s)** further, unplugged a bunch of SAS apps, uh that may or may not be the right decision for you. It's certainly not where I would start. Um but uh but this is a really powerful real world example that's occurred in the last year at the leading edge of enterprise AI. A few months ago, Sat was on stage at Build and he made some pretty strong statements about the need for an enterprise knowledge graph. In addition to models, which he described as only part of the equation. Um, and he specifically says it's not good enough to have just vector search and some embeddings. You need the entire enterprise knowledge graph when building your enterprise application. And I've had the privilege the last couple months of joining some of our uh road show where we had customers

**[4:49](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=289s)** standing up and talking about their inproduction use cases um that are leading edge AI that incorporate knowledge graphs in various ways. One is Walmart that have a people graph of their 1.6 billion employees to take um feedback from everyone and help um management better understand and react to that feedback. Another is Uber's config graph. Another is Adobe has a project called Graph Minds. Building an AI agent that thinks in connections really captures the essence of what we're talking about here. Um, AppV has something called the Arc knowledge graph that they've progressively built. One nice thing about graphs is you can start small, get value, add more data, get network

**[5:38](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=338s)** effects, get more value, and so on and so forth. you don't need to build um you know to spend years slurping all your data before you know whether you're going to get value or not and then a bunch of other examples including customer journey analysis and improvement at discover and if I look at these and I look at the technical patterns underneath them because a lot of us here are practitioners you end up with maybe a newer view of graph rag where you have many patterns of graph rag the original one was hybrid search with graph context. I'm going to start with a vector based search and I'm or a text based search and I'm going to land a chunk and then I'm going to chunk to the entities and relationships around it. Bring things back a few levels out, feed

**[6:25](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=385s)** that to the LM. The LM makes the decision. Um I have reasoning happening in the LLM. Uh but it's better and I have something like gray box explanability where you know what information was fed to the LLM. So you have a little bit of a better idea of where the answer came from even though you can't prove it. And then you can also take another step and filter based your results based on the graph. So that's graph filtering. Something I'm seeing much more of just in the last six months is text decipher is using a model to generate a query. And something that was surprising even to me is that for complex queries, which you naturally get as you put humans in front of a chat interface and let them dig deeper and ask more and more questions, you naturally end up getting to more and more hops and levels of

**[7:14](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=434s)** context and causality. And then the model's ability to generate SQL that a will even run and b will even run in a reasonable period of time, assuming the query can can even execute, um, gets pretty difficult. So text to cipher surprisingly actually is proving out to work better than text to SQL in the real world just because the tity of the graph query language and it's uh more expressable and the machine's better able to compose um a human question into a graph query graph vectors. So these are not all that used but turns out there's a topological vector against which you can do similarity uh which is very powerful. um who's got the shape of this uh bad actor, who's got the shape of this high

**[8:01](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=481s)** value customer just based on how people interact. So it's a topological similarity distinct from um from um similarity of word meaning. And then you've got multi-step complex agentic architectures. We'll get more into this in a moment. The other thing that's come up is more refinement on what goes into a knowledge graph in the context of AI. And at the highest level it's this world tends to show up in networks. This is true of the real world and it's true of the digital world. And let's think about this. Computer networks, social and people networks, communications networks biology ecology transportation, payment. These things all show up as networks. The other is hierarchies or payment uh

**[8:51](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=531s)** supply chain bill of materials asset ownership ultimate beneficial owner that kind of thing if you're in banking and networks and hierarchies are naturally graphs. And so you know why would you shove these into tables when you have the option of actually putting it into a database technology that's designed to store these in the same format in which they show up. So what kinds of data show up in this? Well, there's the domain graph which we just talked about. It's the digital part of the world that shows up. Um you also have a graph of the shape of the vectors. This is akin to maybe the page rank example with Google with the web is what's the shape of my vector chunks. I talk about this more in the graph manifesto for those of you who haven't

**[9:39](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=579s)** read it just you can find it online. The ontology graph. So the graph of actually maybe your product hierarchy, that type of thing. Lots of memory graphs out there and in fact a lot of memory frameworks use um graphs in Neoforj on the back end to name a few. Cognney Zep me zero. There's one called paper that actually just um if I'm not mistaken is still number one on the Stanford Stark leaderboard for uh rag thanks to using graph rag. And then what's also cool about graphs is you have all these forms of unsupervised graph machine learning that you can run like centrality and community detection and so on. So you can run those and then enrich your graph and have your domain or your lexical or memory graph enriched with information about what the shape of the network says

**[10:30](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=630s)** about each individual thing. How do this emerge as a new application stack where you have UI at the top, a model and agents kind of at the middle layer, a knowledge graph layer underneath that, and then various data sources either alongside or underneath. And here's an example. I actually snagged this last night from a paper that was just published to archive. Uh so swapped it in for my contrived example because this is a real real world example from Walmart. You'll see a a reference to the paper here. It's pre-publication, so not yet peer-reviewed. Um, but this is their um AI application I mentioned earlier where at the top you can see a chat history and workflow with someone who's applying

**[11:17](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=677s)** for a job and at the bottom you can see a workflow for an employee who just took a new course and is looking for um what are the available career journeys to me to a new job. So, great real world example of a more complex workflow um that's been deployed. Okay, I'm going to close with two super quick slide demos with AI building blocks and there are lots of new building blocks. MP MCP server ability to create um your agents, but the two things that come up the most are how do I create my graph? Where does the graph come from in the first place? And usually it comes either from structured data or unstructured. So here's an example of each. This is a UI that's out there. You can use it. There's a free version. But I'm going to import data

**[12:04](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=724s)** from Snowflake. Snowflake famously often does not have primary and foreign key relationships between their tables. Um so here I've got a schema of a bunch of tables. I'm going to choose a few. And using AI, we now propose a schema based not on the foreign keys because there aren't any, but based on the column names and other stuff that uh you know that that makes logical sense. So this would normally take a professional services team working hand inand with a customer, maybe a week to do. Now you can get it in a few clicks, click a button, all the data comes over and you're off to the races. I can start navigating and exploring the data, writing queries. That's example number one. Example number two from unstructured is let's use an example of what I'm pretty sure has to be the

**[12:55](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=775s)** longest web page on the entire internet or at least the longest page in Wikipedia. Microsoft's wiki entry has more than 300 references duper long. Um we suck that into something called the LM graph builder open source tool that we host for free. You can check this out too. Um give it a little bit of information. what to look for. So for example, person works for company tell the LM go look for that as part of its entity and relationship extraction from the text and before you know it you can visualize the entities and you also have a lexical graph here. So graph of the chunks and the relationships between those and we're also running some community detection and graph algorithms. So I've actually got three kinds of graphs all over here just in a few clicks. And then here's the beautiful thing

**[13:44](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=824s)** about this. I can ask a question of a chatbot and then um through an MCP server it will go and delegate questions that it knows are available on the graph to the graph and then bring that result back. So here I say who's on the board of directors of Microsoft. Turns out I get a result. It's qualifies it as saying it's from from September 2023 which is actually when that uh part of the page was last updated. But then I can look at the explanability and see um where does this come from and you can actually see the notes and relationships that were used to answer the question. This is giving me my explanability and I can see the board. This matches up with the answers on the previous page. You can even see the people who are or were um employees of Microsoft tied to the Microsoft part of

**[14:33](https://www.youtube.com/watch?v=0OINWeJ-Dq8&t=873s)** the graph. That's it for today. Pay us a visit. more different demos at the booth and then uh if you follow this QR code, we've prepared a landing page just for you at this punk conference with all kinds of breadcrumbs to more learning and follow-ups that you can take. So, thanks very much. Appreciate your time.
