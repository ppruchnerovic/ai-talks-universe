---
id: IN-rb-9WmiY
title: "Pinecone 2.0 — Edo Liberty, Pinecone"
slug: pinecone-2-0-edo-liberty-pinecone
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Edo Liberty"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-09-16T13:00:06Z
video_id: IN-rb-9WmiY
url: https://www.youtube.com/watch?v=IN-rb-9WmiY
youtube_url: https://www.youtube.com/watch?v=IN-rb-9WmiY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["RAG, retrieval & knowledge"]
transcript: true
---

# Pinecone 2.0 — Edo Liberty, Pinecone

**Edo Liberty**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=IN-rb-9WmiY) · [Conference site](https://www.ai.engineer/)

## Description

People used to type "am I fat?" into Yahoo Answers. Edo Liberty worked there at the time, and the question stuck with him, because a Q and A forum has no possible way to know. It is a failure of theory of mind, our capacity to model what someone else actually knows, and he argues we are making a subtler version of the same mistake with agents right now. He splits knowledge three ways. General knowledge is what a model absorbed in training and can be relied on for. Specific knowledge is the contract or the codebase, which retrieval and vector search have handled for years. The third kind is tribal knowledge: how things get done here, who owns what, which principles actually govern decisions. It is not public, and unlike a contract it cannot be plucked from any single document, because it is the sum of a great many.

The right mental model for an enterprise agent, then, is a brilliant new hire who is clueless about your company and starts every session on their first day. Liberty's proposal is a persistent, specialized knowledge layer that all agents query, and the requirement he calls hardest is staying current. Replace a CEO and the whole company knows the next morning, while nine thousand documents keep naming the old one, and the new fact has to override all of them. The implementation detail worth the watch is what he calls a runtime coding agent. Rather than answering by query, the system writes and runs code at question time, iterating in something like a notebook until the answer holds, which cut their tooling prompt from roughly 150,000 tokens to under a thousand.

Speaker info:
- https://x.com/edoliberty
- https://www.linkedin.com/in/edoliberty/
- https://edoliberty.github.io/

Timestamps:
0:00 - Theory of mind, and why it matters here
1:06 - The question nobody could answer
1:57 - Three kinds of knowledge
3:17 - Tribal knowledge, and why search cannot reach it
3:56 - A brilliant new hire, every single session
4:49 - What a knowledge layer has to do
6:19 - Why staying current is the hard part
9:07 - The manifest replaces hand written skills
11:42 - Import, curate, and search
13:35 - Giving a query a budget
14:42 - A runtime coding agent
17:00 - From 150,000 tokens of tooling to under a thousand

## Transcript

*3,122 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=1s)** [music] All right, welcome everyone. I want to tell you a little bit about uh the new the new uh knowledge layer and I'll start with telling you a little bit about theory of mind. Uh how many of you uh know what theory of mind is? All right, so a few folks. It's a uh term in psychology about uh our capacity to understand uh and have a mental state or a model of a mental state for other people. What do they know? What do they believe in? How do they act? That's what allows us to socialize. That's what

**[0:48](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=48s)** allows us to lie to each other and so on. Uh but it's a crucial developmental stage for humans. uh in a necessary function. I'll I'll sort of explain it in the best possible way with a funny story just to break the ice. Uh about 15 16 years ago I uh worked at a company called Yahoo um that had a product called Yahoo Answers which was sort of like a Q&A forum. Uh we used then AI which is the stone age of AI you know it's like uh NLP and other statistical models to answer questions. But the funny thing is people would come to uh Yahoo and ask questions like am I fat? Which uh is funny because obviously uh you know Q&A forum would wouldn't have any clue whether you're you're too fat

**[1:37](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=97s)** or not. Uh but this is a funny way to say yeah people have a very bad theory of mind on sort of what the products that they use what information they have and what they don't have. And I want to argue that in some sense we are making that mistake with AI today in a more subtle and less sort of like uh silly way but in a just as fundamental of a mismatch. And so I will categorize roughly three kinds of knowledge. I think there there are many more but you know in broad stro in broad broad strokes this is not a bad way to categorize. First of is general knowledge. Think about that is what's available in the public domain. Things that models are trained on and we expect an LLM to just know out the gate. Uh things about just you know improving your Rust code

**[2:28](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=148s)** uh asking you like you know explaining stuff about the legal terms or uh sort of exploring use cases for for products. Um we know how to do that. Models are really good at that. When we use our agents they have that information. there is specific knowledge [clears throat] the companies of course the models wouldn't have uh any clue about whether we've uh implemented something specific in our codebase what a contract of a specific customer has of course this is information that's private to the company uh but we know how to deal with that and rag and search and of course pine cone veto dbs and so on uh solved these problems a long time ago there's still a lot to go but we by and large know how to do it and then I would say there is tribal knowledge. Okay, tribal

**[3:17](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=197s)** knowledge is the sort of general knowledge inside the company. This is the kind of information that uh an employ a seasoned employee has that a new hireer does not. Okay, it's roughly how we do things, what our processes are, who's in charge of what, uh what are the guiding principles, what are the you know sort of how we get stuff done in this company. Okay. um that is not a that's not general knowledge because it's it's specific to your company but it's also not a specific piece of knowledge because you can't just get it by searching. You can't just get it by plucking it off one place and say yes this document says uh that this is our culture. It's the sum total of a lot of uh things. Um and so if our theory of mind of most of our agents in big

**[4:05](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=245s)** companies today should be something like a new hire. They're brilliant. They have tools. They have we have very high expectations of them. But they are by and large clueless. Okay. They have no idea about your company's goals, culture, priorities, processes. Um they have to read a bunch of documents uh to be able to get any semblance of understanding of where they are in the world. Um and really they start most tasks from scratch. Okay. they really start kind of wake up and every time you start your your session, uh, they're like a new hireer on their first day on the job. So, I would argue that what they need is not necessarily to be smarter, to have better tools, but to have something new,

**[4:53](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=293s)** which I would call a knowledge layer going forward. Um, and I have to explain to you what I think a knowledge layer has to actually do. But just I'll define it generally before explain to you what we do. Um so at the very least it needs to be persistent. We talked about this is the company knowledge, processes, capabilities and goals and so on. It has to be persistent. Uh it sure it uh feels like putting this thing together is going to be a monumental effort. So you want to do it once or at least very rarely. Uh and of course all your agents in company need to have access to this thing. The second thing is that you would argue that this [clears throat] knowledge layer needs to be uh highly specialized. If your agent uh is in charge of HR practices or optimizing

**[5:43](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=343s)** your uh your kernels in your codebase or uh resolving customer issues that they would care about different things they would want to you know address they would want to have different information available to them. Um, and I would argue irrelevant of of specifically how it's created, I would argue that it's a good practice to have the domain experts in the company own those and have being able to interact with them and make sure that they actually uh are aligned with what the company wants to do. And finally, which is the hardest thing is they need to stay up to date and they need to stay concurrent constantly because companies change and you need to make information uh uh deprecated. When it becomes deprecated, if the company replaces its

**[6:31](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=391s)** CEO, the very next day, everybody in the company knows who the CEO is. Okay? Even though 9,000 documents going from, you know, a day before yesterday to uh the last 10 years say it's somebody else. This has become common tribal knowledge immediately. And everything else, even you know, every rag search will tell you otherwise. This is now the overriding fact. Okay. Um I will argue before we move on that I'm not suggesting that this knowledge layer should replace everything else we're doing. Our agents are already very capable and should keep being very capable. Uh they have access to LLMs of course tooling local files search of course like rag vector search text

**[7:21](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=441s)** search and so on. And I would argue that uh the knowledge layer needs to be a separate entity that all these agents have access to as as I explained why this is sort of a fundamentally different kind of data source. So I want to tell you more about Nexus. Um um Nexus is a product that we're uh uh of course it's a knowledge layer but I need I want to explain to you what it does. uh of course so the the four parts are roughly connectors what I would call context uh uh tasks and queries I'll explain each one of them uh now so connectors of course do the obvious things there's nothing much to talk about them um uh

**[8:10](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=490s)** they bring data into the platform uh respect access uh rights and uh and control and so on um very dull as a topic of discussion but incredibly important in enterprises, incredibly important to do right. Uh and everybody who's built that knows how painstaking it is to get this thing to work well. Um the interesting sort of the first properly interesting part is um the context. So the context think about that as the um the sum of assets that the that Nexus or this knowledge layer saves about a specific topic. Think about this as a context for HR, for operations, for engineering and so on. Okay, of course

**[9:01](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=541s)** it has the sources, the connections to the data and so on. But then it has the manifest. Okay, the manifest is the first truly novel idea and and a important uh entity. Okay, the way that we today give context to our agents is with skills and plugins and uh commands and sort of markdown files we write ourselves. In a knowledge layer, you don't do that anymore. Okay? You tell the you tell the knowledge layer, you tell Nexus what you care about in a manifest. You say what kind of tasks you're you want to complete, what entities you want to track, what kind of information you care about, and it's it's the knowledge layer's work to keep track of those files. Okay? And and organize its own

**[9:50](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=590s)** data. Um uh and then it has the knowledge files themselves. So think about the manifest is the meta knowledge file or set of files. Um and then there's the knowledge the knowledge itself. uh think about this as five types of contents. One of them the the first kind is a semantic map. Okay, this is a file that organizes the catalog of where everything else is, the key schemas, the glosseries, all the information that you need to be able to operate this context. Then there are of course a bunch of markdown files that contain information, decisions, memories, uh all sorts of unstructured information. If you've uh who here has heard about uh LLM wiki

**[10:42](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=642s)** okay so LLM wiki is this uh idea that Andre Karpathy suggested to have agents basically manage some stash of markdown files to sort of keep their own notes of stuff. This is a very similar idea. Okay, sort of on steroids but similar concept but that's not enough. Context contains also a bunch of SQL tables for tabular data for aggregation for facts that they need to memorize. uh a vector database to be able to semantically search and text search and filter a bunch of information and all the information that it itself decides is necessary to keep and and remember and graph entities and graphics to remember uh again entities relationships uh causal chains and so on. Okay. And all

**[11:32](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=692s)** of that is managed and created for you. You don't touch any of this. You don't have to uh know how any of this is created. It's all maintained through the manifest. So these are this is the context. Now what are the tasks? What are the actions? These are the nouns. What are what are the verbs? What can we do with those uh objects? Uh first of all is of course import which is bring new information to the system, new files, new events, new uh concepts. Um curate is probably the most and most elaborate one of the two most elaborate functions. it's uh job is to take um to take the uh the say call it a file it doesn't have to be a file but let's say it's a new PDF or a new meeting

**[12:19](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=739s)** transcription or a new uh presentation for the board and say now I need to update my view of the world okay so it takes that it takes the manifest which tells okay now what what things do I care about what concepts do I need to track what needs to be uh uh what do I need to memorize here and then it takes the semantic map that I told you contains all the like organizes where information is and understands okay fine I need to go update these tables these relationships my graph uh this uh these text indexes and so on um and when it's done it has essentially said okay fine I have assimulated the new information it's already it's it's sort of persisted in your context and we can move on Okay,

**[13:09](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=789s)** search is sort of a internal function very important. It basically abstracts with simple functions all the access to that information so that the agent that I'll tell you in a second doesn't have to know uh how to sort of access the internal parts of the context. Now comes uh the second I think most uh most uh interesting uh part of of the system which is noql. Noql is our way to to uh specify how we want information out of the context. It's not enough to just ask questions. If you're an agent, it's really important for you to give us the budget in tokens or in dollars. how much time you want us to invest in this sort of like do you want us to just a

**[13:56](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=836s)** quick off-the- cuff kind of immediate answer or do you want us to go full tilt and scour everything we know to make sure we give you the most accurate answer uh and so on the structure and and so on. It's a you know it's an agentic tool. This is not like a chat interface. Okay. Um and of course what you get back is like something that's agent friendly. This is uh you know grounded text and and kind of structured in the right way format. This again is not designed to be like a chat interface. This is really what your agents expect. Okay. Um so this is this is a uh um this is a uh trying to figure out how much time I

**[14:45](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=885s)** have. Okay, I need to go a little bit faster. So uh this is a sophisticated crowd. I want to sort of uh pop the hood and show you a little bit about how things work. So uh if anything this is the interface I want to there are many many cool ideas uh that make this work but I want to tell you a little bit about just one of them. Okay. What you're seeing is the interface for Nexus. Okay. You will see at the top a question that the uh the agent issued and you see you see on the left uh the different steps that it went through. Okay. What you see on the bottom right is probably the most interesting. You see generated code on the bottom right. What Nexus does which is very different

**[15:34](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=934s)** than other systems. It's what we call a runtime coding agent. Okay. Unlike other coding systems in in that you're used to uh where the task is take a large code base and then help me edit it right but when the edits are done what I have is a piece of software and that is deployed that is the artifact okay what is running does not contain the model anymore it's just the code okay this is not what's happening here the in query time you should think about the engine essentially building something like a Jupyter notebook, something like uh like a Python ripple, right? And they literally write code and execute it and write code and execute and if they get the answer, they know what to do with

**[16:22](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=982s)** it. And if it's, you know, if it's not what they expected, they rewrite that piece of the code and what you get in the end is a is a piece of code that completes the task that gets the information that you want to get. Okay, that is savable. that's rerunnable. Okay. But it's also incredibly flexible because now the the answer is got not by by a query to a database. It's it's written by code which is of course incredibly flexible. Okay, that code is by the way, interestingly enough, if you replace if you write software this way, the the amount the amount of prompting that you need is significantly reduced. We went down from having something like

**[17:10](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=1030s)** 150,000 tokens to give our agents all the tooling they need to less than a thousand tokens to specify all the interfaces they need to get information out of Nexus. Okay. And so the the so what it looks like when you run it is like this. Okay. So on the left of course you'll see Nexus with uh NoQL answering the question and then on the right is sort the same uh task given to an agent with all the tooling to complete the task. Okay, but remember this on the right it's uh severely handicapped. It's like the employee on the first day on the job. They have to read a bunch. They have to figure out where the data is. They have to figure out what the task is. They have to write a bunch of code. Uh it's just it's just severely handicapped and there's

**[17:59](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=1079s)** I don't know if you okay stopped but um needless to say this is by far slower. It's a lot more expensive in terms of token consumption. Uh but interestingly enough it's also a hell of a lot less accurate because again they don't have the right context, the right objectives and so on in your company. Um, I'll just say that [clears throat] we work uh obviously with a bunch of early access customers already. Uh, you see some results here, but I'll just sort of fly through them and say that across different domains, across different enterprises, across different kinds of task, you we universally see the same thing that if you shift to this paradigm, you get significant cost savings. uh 77 90 you know percent token

**[18:52](https://www.youtube.com/watch?v=IN-rb-9WmiY&t=1132s)** consump token reduction is pretty common. Um uh it gets a hell of a lot faster anywhere from 20 30% to sometimes uh uh uh 77% faster. Okay. But and the most important thing is it actually becomes a lot more accurate as well in the same time. So this is really uh it's a slam dunk. I'll just wrap up by saying that uh um the that Nexus is coming out of early access and into public preview literally tomorrow. So go uh try it out.
