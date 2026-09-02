---
id: OyWElYcMPj0
title: "Tanya Roosta - Information Retrieval in the Age of Agentic AI"
slug: tanya-roosta-information-retrieval-in-the-age-of-agentic-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Tanya Roosta"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T01:53:35Z
video_id: OyWElYcMPj0
url: https://www.youtube.com/watch?v=OyWElYcMPj0
youtube_url: https://www.youtube.com/watch?v=OyWElYcMPj0
tags: []
topics: ["Agents & orchestration", "RAG, retrieval & knowledge"]
transcript: true
---

# Tanya Roosta - Information Retrieval in the Age of Agentic AI

**Tanya Roosta**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=OyWElYcMPj0) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*601 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=OyWElYcMPj0&t=2s)** TANYA ROOSTA: Hi, everyone. I'm Tanya Roosta, and I work at AMD as a director of AI. Sorry, I wasn't able to make it in person, but I'm glad at least we have Zoom. I will be spending the next few minutes discussing evaluation framework for agentic IR. So let's start with the shift. Basically, what has happened in the last few years is that we have moved from traditional information retrieval classic RAG, where you had the straight line of there is a query from the user, the search engine would get the documents, come up with a ranked list, we rank it and then present the list to the user, to this more of an agentic flow, where the agent actually does planning, tries to figure out what the intent of the query is,

**[0:56](https://www.youtube.com/watch?v=OyWElYcMPj0&t=56s)** does the search, gathers the results, analyzes critiques, and then presents the final result. So this means that the unit of work has moved from lookup to an ongoing conversation with the world. And this agentic IR shows up in the deep research agents, as most of you have seen with ChatGPT and other agents, that you're able to put a question out-- for example, here is the question about cholesterol medication-- and the agent basically tries to understand what the intent of the question is. Then it goes and uses various tools to gather the websites, different information, price information, drug interactions, et cetera,

**[1:50](https://www.youtube.com/watch?v=OyWElYcMPj0&t=110s)** and then comes up with the answer, tries to ground the answer into retrieved evidence, and then, finally, presents the results to the user. And this basically saves us many, many hours and having to go through all the document, blog posts, et cetera, and trying to figure all of this out on our own. And a lot of times, this agentic IR is now taking over potentially 20 turns. So it has become a multi-hop thing. But here's the uncomfortable gap that's still exists, and that is that when we want to evaluate these agentic IR, we still tend to look at the final answer,

**[2:42](https://www.youtube.com/watch?v=OyWElYcMPj0&t=162s)** use scores like BLEU and ROUGE to see if the final answer is correct. And given now the information seeking is really interactive, multiturn, it has this temporal aspect, it has to be evidence-driven, simply grading the final answer doesn't work very well. So what do we do? We basically have to look at the trace and try to assess the correctness of every hop. Was it adequate to answer the user, the cost in terms of number of tokens, latency, et cetera? And in terms of where the field is heading, I would say there is a reasoning aware retrieval.

**[3:32](https://www.youtube.com/watch?v=OyWElYcMPj0&t=212s)** So now not only you have the keywords from the query, you're looking at the agent's reasoning traces. There is the multiturn hop-aware benchmarks that are being developed, like Amtrak. There is the retrieval GraphRAG so that you can look at the relationships. There is self Rag to cut through some of the hallucinations, and adaptive RAG to basically route queries based on their complexity and effort. And, finally, actually looking at the number of tokens that are used and optimizing around that as a metric for information retrieval.

**[4:20](https://www.youtube.com/watch?v=OyWElYcMPj0&t=260s)** So what I want to leave you with is that our information seeking has changed. The agents have changed, how we get information. And that means that we have to also change the way we assess, if these agents are doing the right thing and if they're achieving the goal that they have set out. And that's all I have. Thanks for having me.
