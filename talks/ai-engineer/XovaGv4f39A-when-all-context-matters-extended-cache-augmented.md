---
id: XovaGv4f39A
title: "When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis"
slug: when-all-context-matters-extended-cache-augmented
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 6
published_at: 2026-06-28T20:00:11Z
video_id: XovaGv4f39A
url: https://www.youtube.com/watch?v=XovaGv4f39A
youtube_url: https://www.youtube.com/watch?v=XovaGv4f39A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XovaGv4f39A) · [Conference site](https://www.ai.engineer/)

## Description

This session addresses a critical challenge in knowledge representation: extracting accurate answers from a rapidly changing dataset where every document is highly interconnected and relevant.

Explore the limitations of standard retrieval methods for dynamic, high-context scenarios—including the constraints of Simple RAG and the computational bottlenecks of constantly recomputing a GraphRAG. To overcome these hurdles, this talk introduces a novel solution: Extended Cache Augmented Generation (ECAG).

Speakers:
- Luis Romero-Sevilla (Orbis Operations): Luis Romero-Sevilla is an AI strategist and full-stack software engineer with over 13 years of experience driving mission-critical technological innovation across defense, healthcare, and the public sector, currently serving as the Vice President of AI at Orbis Operations.
X/Twitter: https://x.com/lurose15

## Transcript

*863 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=XovaGv4f39A&t=3s)** [music] >> Hi, I'm Luis Romero Sevilla and I'm the VP of AI at the Orbifold operation. I'm on a mission to solve knowledge representation when all context matters. So, let's start with a very specific example. Let's say we have a large number of documents and all documents represent an event and all documents in the collection are relevant to answer a set of questions that the user has. Not only that, there's one more challenge. The document in the collection becomes obsolete very fast and all documents get replaced with new information. Let's start with a simple approach. We could start with a simple rag. For that, we just need a vector database and an embedding model.

**[0:53](https://www.youtube.com/watch?v=XovaGv4f39A&t=53s)** An embedding model takes the documents and turns them into a learned numerical representation, a vector. Now, we take those vectors and we store them in a database optimized for performing operations with the vectors. Perfect. Now, we can take all of our questions, >> [music] >> turn them into vectors and then look for a vectors that are similar to the initial query. Those vectors that are within the trip similarity threshold are retrieved and we can pass them to the LLM to answer the question. Inserting to a vector database, it's relatively fast. So, whenever a collection becomes obsolete, we can just replace it with a new one. We still have one problem with our very specific scenario.

**[1:41](https://www.youtube.com/watch?v=XovaGv4f39A&t=101s)** All the documents in the collection are relevant for us to answer the question. So, we can't just take all the documents in the collection and pass them to LLM. That's just one of the many limitations with this approach. Wow. >> [screaming] >> Now, let's get a bit more sophisticated. All documents are relevant to answer a global question. Therefore, there must be some connections and relationships between the details within a document in the collections. For us to map out those relationships, we're going to need a knowledge graph. And one implementation we could try is GraphRAG. GraphRAG has many steps, but basically, >> [music] >> it uses an LLM to read through all the documents and extract key entities and relationships between them. It constructs a network, a knowledge

**[2:29](https://www.youtube.com/watch?v=XovaGv4f39A&t=149s)** graph, where all those connections and details are tied together. Then, when a question is asked, it navigates this graph to synthesize a complete answer drawn across the entire collection. If your collection of documents isn't changed very often, GraphRAG is an excellent approach for finding those relationships within details to answer the user's question. However, our very specific scenario states that our data is not only deeply interconnected, but also the data gets replaced very often. Recomputing a knowledge graph every time the data gets replaced is computationally very expensive, and it takes relatively long time. Okay, what if we take an even simpler approach and we continue to build on top of it? If we were to use something like GraphRAG, each document needs to pass

**[3:16](https://www.youtube.com/watch?v=XovaGv4f39A&t=196s)** through an LLM [clears throat] for the entity and relationship structure anyway. Why can't we just throw all the documents into context? This approach would look something like "cache augmented generation" (CAG), where we use a model with a large context window, load the documents into the context, and cache the context by storing the model's KB matrix. The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too. The solution: what if we use more CAGs in parallel and distribute the documents across different context buckets. Now, each cache can answer questions regarding its content. And now we just need something to ask the right questions to the right buckets. So, for this, we can use a smarter model

**[4:05](https://www.youtube.com/watch?v=XovaGv4f39A&t=245s)** to interrogate each bucket and eventually synthesize an answer. How do we distribute the documents? It sounds tempting to organize the documents by domains and tell the supervisor, "Hey, here are the different categories." But in practice, with very dense relationship between documents, the supervisor tends to ignore domains that at first glance seem irrelevant. For this reason, all documents are distributed in no particular order. The only requirement is to balance the number of documents in a way that the least amount of documents are needed. Then the supervisor model start exploring the buckets and progressively builds its internal understanding. And if it finds something interesting, it can ask a specific bucket follow-up questions.

**[4:52](https://www.youtube.com/watch?v=XovaGv4f39A&t=292s)** Because all caches can be loaded in parallel, the knowledge building process is significantly faster than graph rag while providing more accurate answers than a simple rag. And you're probably thinking, "KV cache can be pretty expensive." And you're absolutely right. But there are ways to reduce that cost by optimizing how long each cache lives. And at the end, there are many retrieval strategies, and all of them have their trade-offs, whether it's compute, cost, speed. Currently, there is no one-solution-fits-all. So, each type fits our solution to our very specific problem. Thank you for watching. And for any questions or continuing this conversation, going to leave my details

**[5:40](https://www.youtube.com/watch?v=XovaGv4f39A&t=340s)** here. >> Mhm.
