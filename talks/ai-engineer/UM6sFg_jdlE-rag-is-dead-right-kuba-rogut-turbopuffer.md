---
id: UM6sFg_jdlE
title: "RAG is dead, right?? — Kuba Rogut, Turbopuffer"
slug: rag-is-dead-right-kuba-rogut-turbopuffer
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kuba Rogut"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-06-09T17:00:27Z
video_id: UM6sFg_jdlE
url: https://www.youtube.com/watch?v=UM6sFg_jdlE
youtube_url: https://www.youtube.com/watch?v=UM6sFg_jdlE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# RAG is dead, right?? — Kuba Rogut, Turbopuffer

**Kuba Rogut**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=UM6sFg_jdlE) · [Conference site](https://www.ai.engineer/)

## Description

Cursor added semantic search and measured a 24% increase in answer accuracy on their composer model, a 2.6% gain in code retention in large codebases, and a 2.2% drop in dissatisfied user requests. Those numbers look small until you factor in that semantic search does not fire on every query. Meanwhile Google search volume for RAG hit a new inflection point in mid 2025 and went through the roof. The Twitter "RAG is dead" discourse and the actual usage curve are moving in opposite directions.

Kuba Rogut's argument is that the problem was never retrieval, it was the narrow definition of it. RAG is not just a vector search call. It is vector search, full text search, glob, regex, and filters used iteratively by an agent that keeps searching until it has what it needs. He contrasts Claude Code (grep per session, no index, repeat cost every run) with Cursor (one time upfront indexing, lightweight tool calls at runtime). Claude Code's approach is not wrong, it is a deliberate tradeoff. The frame that clarifies it: embeddings are cached compute, and whether to cache depends on query volume. Jeff Dean's version: you do not need a trillion tokens at once, you need the right million.

Speaker info:
- https://www.linkedin.com/in/kubarogut/
- https://x.com/rogutkuba

Timestamps:
0:00 Introduction to the "RAG is dead" discourse
1:12 Google search volume trends for RAG
1:39 Defining RAG vs. Agentic Search
3:15 Cursor's indexing and semantic search approach
6:10 Contrasting Claude Code (grep) vs. Cursor (indexed)
6:40 The concept of embeddings as cached compute
8:38 The shift from simple RAG to Agentic Retrieval
9:44 Jeff Dean on context windows and stage retrieval

## Transcript

*2,187 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=7s)** [music] >> All right, welcome everyone. Thanks for coming out. I see it's a full room, so I appreciate everyone coming out. So welcome to the talk about rag is dead, right? So my name is Kuba. I'm deployed engineer at Turbo puffer. So for those that don't know what Turbo puffer is, we are a full text search and vector search database built from first principles on top of object storage. If you would love to learn more, I'll just come find me after the talk if you have any questions. So let's get started. So this talk I get is up sorry about how rag is dead, how hybrid tool tool rich retrieval is becoming a default for serious agentic search. So you guys have been on Twitter or other social media platforms or I guess X they call it now,

**[0:54](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=54s)** you might have seen a lot of tweets like this about how rag is dead. You can see there's lots of tweets especially in the last you know in end of 2025 and in the early of this year about how you know rag is dead, agentic file search is all we need and there's kind of a a lot of tweet and a lot of kind of content about this now. But you know interestingly if you're to look at something like the Google Google search volume over the last 2 years or last couple years you can see that you know in 2023 kind of like AI starts we have the kind of this this you know increase kind of caps out a little bit in 2024 settles down for about a year and then about midway through 2025 we hit this new inflection point where search volume just goes through the roof. So take that Twitter. Um So let's clarify first what is rag and what is agentic search. These are kind

**[1:41](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=101s)** of the two terms a lot of people are throwing out these days. So rag what a lot of people think rag is is just simple vector search. They just think that this is just simply you know embedding a bunch of you know a corpus of contents passing an embedding vector and getting it back passing it through your LLM. And what I Turbo puffer what we think this actually means, you know if you break down rag into retrieval augmented generation, you know retrieval is not just vector search. It's a lot of different things. It could be vector search full text search using stuff like BM25, grepping, globbing, using regex, using other just basic filters. And the augmented generation is obviously just passing it into your LLM of choice. And then agentic search. This is kind of the terms people are throwing out a lot these days. And generally when people start talking about agentic search what they usually talk about is essentially

**[2:29](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=149s)** just file system grep. So if you guys are familiar with something like Cloud Code and kind of that's what Cloud Code Codex you know a lot of people call this agentic search and this just essentially is grepping through your file system and this is kind of why these terms are so correlated. And what we actually believe it is and you know kind of the definition we want to we want to give it is it's really giving the agents a set of tools to kind of progressively and iteratively find and reason over context. So with Cloud Code you can you know if you guys have are familiar with it it can read your file you start grepping through your file system read a file decide that it hasn't found what it needed what it what it needed to actually complete the task and it will you know find something again and then keep doing this until it's happy you know it's reached a happy state where it can continue on with the task. So we're going to take a step back

**[3:17](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=197s)** and talk about one of the companies that use Turbo puffer that we believe is doing an excellent job with agentic search. This is a company called Cursor you might have heard of them. Fun fact they're actually one of Turbo puffer's very first customers. And they have this excellent blog post that came out in the beginning of 2026 about how they index code bases. So for those unaware when you open up a new code base or new branch in Cursor what happens is that Cursor will start embedding your code base. So what they'll do is you know chunk out you parse chunk and embed your code base and make it available for semantic search. And this blog post goes into an excellent kind of excellent technical detail of how they do this. Just to give you the gist essentially the cool thing they do is that they found that you know most people working in a team let's say there's 100 engineers when they open up code bases they're normally the same code base you know 99%

**[4:05](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=245s)** of the time because you have a team of 100 people most of the time working on one two maybe a few code bases, right? And it's really expensive to have to like re-chunk re-embed and re-upload these code bases every single time. So they essentially use like Merkle trees which essentially is this crypto hash tree to calculate similarities between code bases people open on the same team. And if they're similar enough they will essentially copy over the data and then only update the and re-chunk and re-embed the files that have changed and use Turbo puffer in order to make sure this is done securely. And yeah it's just excellent blog post. They they do some really cool stuff. And you may think like this is a lot of work. Why do they do this? Well the reason they do this is also covered in a in a different blog post about how they use semantic search. Again they use

**[4:52](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=292s)** Turbo puffer Turbo puffer for this. And what they find is on average across models I think it's like a 12 and a half or 13 and a half percent increase in answer accuracy. This is in cross across their internal Cursor context benchmark. So you know not not a public benchmark but you can trust the numbers they give us. And you can see on on the right side their composer model so it's this this is before composer two they had a almost a 24% increase in answer accuracy. So giving semantic search to these tools and to these models is really can drive real performance gains. And you can see on the on the bottom right this is from an online AB test they did which is also covered in their thing in in their blog post about how it's almost like a 2.6% retention code retention in large code bases and there's a 2.2% decrease in

**[5:42](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=342s)** dissatisfied user request. And you may be thinking like oh well these numbers aren't that big like 2.6% 2.2% not that large but they also covered that semantic search isn't used in every single query. So in their online AB test you know if you give it if you give this tool to 100 query 100 random queries not every 100 query will actually benefit from the existence of a semantic search tool so that's why these numbers look kind of small. Um And now let's talk a little bit about Cloud Code. So Cloud Code doesn't use vector search as covered by the tweet from Boris Cherney. So those unfamiliar with Boris he's essentially the founding father of Cloud Code. And he says that in early iterations of Cloud Code they actually did use rag in their local vector DB but they found that it just didn't really work out for them. But this is something that

**[6:32](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=392s)** is important to understand is something we like we've kind of like taken on a lot internally understanding um here at Turbo puffer is this idea that like embeddings and semantic search are kind of cash compute. And you may be thinking like cash compute like kind of throwing out a lot of terms at me right now. Like I don't know exactly what that means. And I think it's like best to walk through an example of essentially almost like a Cloud Code looking trace and a Cursor looking trace. Of how how these agents will understand your code base. So on the left is kind of a per session discovery of Cloud Code. So for example if we're to ask the agent to understand how metadata filtering works what it have to do is grep read assess and repeat and try to find the files it needs in order to gain this understanding on a per session basis. So

**[7:21](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=441s)** what this means is you could have you know 10 agents on 10 different days across 10 developers and you they can be asking the same question multiple times you know in day every day every time the agent's going to have to repeat these same exact steps to gain the kind of like same understanding of this code base. And this could you know cost quite a few tokens. You know 6,000 doesn't seem like a lot here but just remember this is like one sub step of an agent. And then on the right is kind of like a more Cursor looking trace where there's this upfront cost of indexing but then we're able to allow for this like lightweight tool to help the agent kind of retrieve this information at runtime. So obviously there's this like upfront cost of parsing a code base embedding it and making it available but this is like a one-time cost and then at runtime the agent can just query something like how

**[8:09](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=489s)** is metadata filtered? It can get some simple results and it would save a lot of tokens a lot of time and just a lot of money. And this just helps the agent to become a lot faster. You know a lot of people on the team now that maybe were big Cloud Code users here at Turbo puffer they've you know they've actually started switching to Cursor just because of how fast it's becoming especially with their composer two models and also this semantic understanding it's just become we're finding really really good. So from rag to agentic retrieval. Um So what we're finding now is that a lot of people are no longer doing the simple rag you know the the Twitter quote unquote rag of just doing vector search once and throwing it into the context windows. What we're finding

**[8:56](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=536s)** is that this worked you know back in 2023 early 2024 at kind of the beginnings of AI but a lot of the more sophisticated customers are doing agentic search and it's giving like real real big performance gains and kind of unlocking like new products. Um And what we're finding is you know they're doing a ton of calls they're reasoning these agents are reasoning through several steps. They're searching semantically or through full text etc. as needed and they're only fetching what's needed for that specific specific use case but the important thing to know is that you know retrieval is no longer just this like simple one-time call to vector DB. It's becoming super iterative and these agents are really understanding what they're searching and searching to understand more in a sense. It's kind of like interesting loop. You

**[9:44](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=584s)** know Google's Jeff Dean he went on a I forget if it was a show or podcast or whatever and he had this really good quote that we like to use that we also we thought was super interesting. He was talking a little bit about I believe about how Gemini's models were kind of having these really big context windows. Uh, I forgot the exact question the the host asked them, uh, but he was saying, you know, big context windows, it doesn't matter if you get to a trillion context window size, what you really need is stage retrieval, like a lightweight mechanism to narrow down these trillion tokens into essentially millions at a time. And like the exact quote is you don't need a trillion at once, you need the right million. Um, this is something we think a lot about Turbo here at Turbo Buffer. Um, you know, we have customers that embed, you know, have trillions of tokens inside Turbo Buffer, and

**[10:33](https://www.youtube.com/watch?v=UM6sFg_jdlE&t=633s)** as we see like the really important part is just getting down to this right 100,000, right 10,000, right million in order to pass into these context windows. Uh, that's about it for the talk. Um, if you have any questions about any specifics, I'd love to, you know, either have them ask now or you can find me after the talk. Uh, but appreciate you guys coming out. >> [applause] [music]
