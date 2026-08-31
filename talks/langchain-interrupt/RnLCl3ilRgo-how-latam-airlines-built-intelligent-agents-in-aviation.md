---
id: RnLCl3ilRgo
title: "How LATAM Airlines Built Intelligent Agents in Aviation | Interrupt 2026"
slug: how-latam-airlines-built-intelligent-agents-in-aviation
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 17
published_at: 2026-06-30T12:42:12Z
video_id: RnLCl3ilRgo
youtube_url: https://www.youtube.com/watch?v=RnLCl3ilRgo
tags: []
transcript: true
---

# How LATAM Airlines Built Intelligent Agents in Aviation | Interrupt 2026

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=RnLCl3ilRgo) · [Conference site](https://interrupt.langchain.com/)

## Description

Nico Venegas and Claudio Urbina Lara from LATAM Airlines — the largest airline in Latin America — walk through what it actually takes to run AI agents at scale in a 3–5% margin industry where every interaction is either value created or value lost. They cover the architecture of LATAM Concierge, a LangGraph-based B2C travel agent with 4,000 daily users, and the hard lessons learned from production: a 15% cost reduction through architectural restructuring, and how a 13% out-of-scope rate turned out to be a product gap, not a model failure. They also introduce Compass, LATAM's internal pipeline for turning millions of unstructured agent conversations into a structured knowledge graph in BigQuery — and why, at this scale, the agent is no longer the product.

Chapters:
0:00 What 6,000 passengers in the air right now means for your agents
0:47 LATAM by the numbers: 87M passengers, 3–5% margins, 31 cents of every dollar on jet fuel
2:04 Why extracting intelligence from agents is a different challenge than modeling flights
2:40 Every interaction is value created or value lost
3:51 Why you need a platform before you can build agents: introducing Cosmos
4:12 LATAM Concierge: the B2C travel agent built on LangGraph
4:54 The tool-per-agent architecture and how the supervisor stays in control
5:23 How LangSmith made architectural evolution possible
6:06 What passengers are really telling you when they ask about a restaurant
6:49 Lesson 1: How restructuring the architecture cut costs 15%
7:33 Lesson 2: The 13% out-of-scope problem that turned out to be a product gap
9:10 What questions you can only answer across all conversations, not just one
9:36 Introducing Compass: turning unstructured conversations into a knowledge graph
10:36 The Compass pipeline: parser, mapper, modeler, and ontology registry
11:18 Two examples — UX research interviews and legal contracts
13:09 Bottlenecks, BigQuery Graph, and the architecture decision to ditch Spanner
13:56 The vision: connecting agent graphs across the full passenger journey
15:01 The flywheel: from agent conversations to analytical improvements
15:32 Three takeaways: scale, unstructured data, and why constraints are an advantage
16:30 The agent is not the product anymore — the intelligence across all of them is

Resources:
→ LangGraph: https://www.langchain.com/langgraph
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com

## Transcript

*2,405 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=7s)** The cost of building AI has never been easier. The ecosystem collapsed, the cost of sustaining one up. There are frameworks, tools, protocols, but operating them at a scale is a different history. Right now, while we're sitting here, there are about 6,000 of people on a LATAM flight. And by the time this talk is over, our AI and the agents will receive a few thousand of interactions. And the question that we keep trying to answer is, what do all conversations know that we don't? That is what this talk is about, not about how we build those agents, it's about what we learn operating them at this scale. Two numbers to ground you. LATAM is the

**[0:57](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=57s)** biggest airline in Latin America. The last year we transported more than 87 million of passengers. And there is a big restriction in this industry. We operate with margins between 3% to 5%. A SaaS company runs at 20% That's an order of magnitude less of slack. And the jet fuel is the most important cost that we have. And the jet fuel just doubled year on year, peaking at about 184 the last March. And guess what percentage of the cost is jet fuel? At LATAM, 31% of every operating dollar is jet fuel. In fact, in this industry, every dollar literally competes with

**[1:46](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=106s)** infrastructure. So, we know everything about the flight. We know the routes, the connections, the revenue per seat, the fuel consumption. We model all of that years ago and we do it well. But, if you want to uh use our agent and extract the information and the data from them, it's a really different challenge. So, we want to take advantage of every agent that we have and improve the experience through them. In indus- in in this industry, running uh under 3% every interaction is either value created or value lost. So, if we want to improve the experience

**[2:34](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=154s)** across all of them, is how we grow the revenue without growing the cost. So, I will let you go with Claudio, who is our GenAI tech lead. He will present one of those agents running in production. Okay, so Nico just gave us the scale. But, behind those numbers, behind the 87 million passengers, there are real moments happening. Right now, there are thousand of people planning their next trip, planning their next vacation. And a hundred of them is calling our contact center because they need help with this trip. And right now, as Nico said before, there are thousand of people on a LATAM flight. And the thing is that all these people, all of our passengers, need us to be there.

**[3:21](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=201s)** And to be there at that scale made us to take a bigger step. And that is the step is to build agents. But, before you build agent at a scale, you need somewhere to build them. You need infrastructure, you need CICD, you need access to model templates, observability, monitoring, and much more. You actually need a whole platform that let you that handle that and let your teams to focus on the actual problem and not to rebuild every foundations every time. To us, that is Cosmos. Cosmos is our proprietary AI and data platform, and we have been building Cosmos for over 5 years. Right now, Cosmos uh have around 120 G&A products in production across 20 different business

**[4:10](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=250s)** domains at LATAM. And one of them is LATAM Concierge. So, Concierge is our B2C agent that lives in the LATAM app phone application and helps our passengers to plan their trips. They can find flights, they can look for hotels, they can even discover whole experiences in their destinations. They just need to open the application and talk with Concierge. And just to give you an idea, the first month of the beta launch, we had 52,000 of users. And that made us the first airline in Latin America to deploy something like that at that scale. Right now, we're having around 4,000 of users interacting with Concierge daily. Architecturally, it's built on LangGraph, and it has a super agent

**[4:58](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=298s)** pattern. That means that we have a supervisor that stays in control at all time, and instead of doing everything itself, it delegates to seek a specialist agent. Flights, booking, destinations activities insurance and customer care. Each specialist handles its jobs, and they respond with what they found, and their supervisors put it all together in the final response. But what you're seeing now is not how we started. The architecture has evolved, and we were able to do it because we put LangSmith in as the observability layer as from day one. So, what Concierge generate is open, messy, and predictable conversations. Uh over time, we uh learned that when a user or a passenger is asking us, "Is

**[5:46](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=346s)** there any Italian restaurant near my hotel? They are not just looking for an answer. They are telling us what they what they like, what they need, and what they want. So, in that conversation, there is more than just a question about food or about a place. And I want you to keep that in mind for the whole presentation. So, Concierge has been running for over a year, and it's generating thousands of conversation daily. And I want to share with you two things that we learned operating in at production. The first one is a structure where it counts. So, at the beginning, we didn't have a supervisor. We had a triage agent that classifies the user's query, and hand off the control directly to the right specialist. And each specialist was the responsible for the final

**[6:35](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=395s)** structured response. Every one of them. And it worked it worked very well, actually. But, the thing is that when you live in a context where every dollar competes with jet fuel, you're always looking for efficiencies. And there is where a tool like Lancelot become fundamental. When we try to look for optimizations, we found that we were structuring at every step. And when we measured it, we found roughly 15% overhead in latency and token consumption, just because we were structuring it at every step. The fix redesigning the architecture. We changed to the tool per agent pattern, and the supervisor that stays in control at all time is the only one responsible for formatting the final response.

**[7:25](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=445s)** Same agents, same output quality, 15% less cost. Then, uh what we see was that 13% of our messages to Concierge were classified as out of out of context. So, uh our first reaction was, "Okay, the people is testing our application. They are going off-topic. They are trying to bypass. They're even asking concierge to solve a Python problem. That's normal. That's okay." But, um but when you But, still 13% was a lot. So, uh we used LangSmith again, and we dig into those conversation to understand what the user were asking. And we realized that 95% of those questions were legitimate passengers' needs. They

**[8:14](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=494s)** were asking about checking questions. They were asking about baggage, Latam Pass benefits, and special services. You things that passengers really need help. So um the model wasn't failure, neither was the architecture. We had simply never built concierge to handle that. So, this year we integrate the customer care agent that I showed you before. Uh the out-of-scope messages dropped from 13% and the return rate improved 6.6 percentage points. And 12 of those conversations are now flowed through the customer care agents. So, these two things taught us one thing. And you can only solve this kind of problem if you deeply

**[9:02](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=542s)** understand what is happening inside your application and what is flowing through it. Okay, so as you can see, this question, what topic are still out of scope, or what preference passengers reveal in concierge, or what topic generate the most escalation, is something that we can face using LangSmith. But, if you want to take an advantage of all the different agents that we have, the question is not anymore what happened in this conversation, is what happening across all of them. So, we decide to to something on top of that. That is Compass. So, Compass is what we build when we realize that agents alone are not enough. So, the conversation are really valuable, but only if we can extract a structured signal from them at

**[9:51](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=591s)** this a scale. So, what you're seeing right now is the core pipeline. So, we have the unstructured data, for instance, the UX research interview, we have a lot of them. Uh transcription of our contact center calls, also the conversation of the of our agents, or even legal documents. All of them flows in, Compass processes it, and generate a structured signal as a knowledge graph in BigQuery graph. This is based on ontology. What is an ontology for us? It's only the different concept and relationship that helps to the LLM to parse the data. Okay, so the pipeline

**[10:39](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=639s)** under the hood is in looks in this way. So, the first step is the parser that transform um all the data, any input format to a multimodal representation that can handle the LLM, and then is the mapper that take that data, and we use Gemini Flash by default and Pro when we have a really complex ontology to identify those relationships, and then is the modeler that deposit all the structured information in the graph, in BigQuery graph. The we have also the ontology registry and evaluator because measuring the semantic extraction it's not trivial. I wanted to bring you two examples. The first one is about the UX research interviews. So, this is something that we tried with a team.

**[11:28](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=688s)** So they they were just doing the same the same work but manually with ChatGPT prompting and generating those structured structured data and into Google Sheet. So, when we when we when we realized that we can use Compass for this, they have thousand of UX research interviews. So, we defined the ontology and the the work collapsed from weeks just to days. There is something amazing as that we have a coverage of all almost 98% with that ontology. So, the second example is about the legal contracts. So, as you can see, there is a different ontology here. We have the pain point, feature request and user segment for the user experience.

**[12:15](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=735s)** But for the legal contract, we have the party, clause, obligation or expiration. So, this is the same pipeline, the same infrastructure but with a different ontology. So, this one is really good and surprised us. So, another team came came to the Compass team they wanted to process and parse their data data that they have already parsed. They were confident with their process. They they they even validated with the business team. But we use Compass just to compare and Compass did it better. So we we we realized that the problem was the definition of the business when big was. So, Compass can take an advantage of the

**[13:03](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=783s)** ontology and improve the performance of the parsing. I wanted to bring you also the bottleneck. The bottleneck is the access to the LLM. So, we're facing with that challenge with the Google team. We think that if we allocate AI infrastructure just for this process, we're going to have a better process and improve the performance. And something about architecture and lessons that we want to share is about that what we started with was a spanner. So, te- technically it's it's really good. It's it's sensational, it's fast, but the reality is that we have the whole company working in Google BigQuery. So, we have thousands of people making queries every day in Google BigQuery. So, BigQuery launched BigQuery graph. So, we moved to BigQuery for that

**[13:54](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=834s)** reason. So, this is something that is happening right now. So, we put the data of concierge, what Claudio dimensioned before, in Google and in Compass. So, the thing is that we can generate right now this graph for this part of the journey of our passengers. But, we have also another agents. We have the the agents, for instance, in the contact center. That that's a really different one, but we can also have that knowledge of graph right now. So, as you can see, our vision is to complement those graph and have a more um a smart data. So, our our different people, the different data scientists, we have more than 100 of data scientists

**[14:43](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=883s)** can access to that data and extract the im- the important information right now. So, and this is not only in the pre-trip or travel day that is part of the journey that we have today, we want also go beyond that and post-trip or the next trip. So, the flywheel. So, as you can see, today we have agents with million of interaction with our passengers. And with Plan Smith, we can know what works well and what doesn't. And we can use also that information through Compass to generate this a structure signal and processes it with all our capabilities, analytical capabilities, and with those analytical capability we can improve the agent that we are have right now running today. So, three

**[15:33](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=933s)** takeaways. AI got really cheap right now, but operating it operating it at a scale at this scale where if we have a mistake in a really regulated industry have consequence. So, I think we think that is where the real value live right now. The next analytical bottleneck is not the compute. We can face that. The real bottleneck is the access and processing the unstructured data. The fifth one is about our different constraint about the margin, about the challenges that we have. Those those constraints are not a disadvantage. We think that those constraints force us to generate something that today

**[16:21](https://www.youtube.com/watch?v=RnLCl3ilRgo&t=981s)** is really powerful and just one just a bunch of document can process for 1 cent. And to finish, is that when you have million of interaction with your passengers or your customer the chatbot or the agent is not the the the the product anymore. The product is the intelligence and the opportunities that you can have across of all of them. Thank you, guys. >> [applause]
