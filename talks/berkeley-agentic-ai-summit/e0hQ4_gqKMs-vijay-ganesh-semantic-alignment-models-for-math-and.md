---
id: e0hQ4_gqKMs
title: "Vijay Ganesh - Semantic Alignment Models for Math and Software Engineering"
slug: vijay-ganesh-semantic-alignment-models-for-math-and
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Vijay Ganesh"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T02:15:14Z
video_id: e0hQ4_gqKMs
url: https://www.youtube.com/watch?v=e0hQ4_gqKMs
youtube_url: https://www.youtube.com/watch?v=e0hQ4_gqKMs
tags: []
topics: ["Governance, ethics & regulation", "Science, healthcare & applied ML"]
transcript: true
---

# Vijay Ganesh - Semantic Alignment Models for Math and Software Engineering

**Vijay Ganesh**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=e0hQ4_gqKMs) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*902 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=2s)** VIJAY GANESH: All right. Welcome My name is Vijay Ganesh. I'm a professor in computer science at Georgia Tech. And I broadly work in the area of formal methods and neurosymbolic AI for mathematics, physics, and code. So the problem that I'm focused on is a little bit different from the problems that the previous two speakers talked about. The problem I focused on is called autoformalization. What does that mean? Auto formalization means you want to translate natural language math into formal language math. OK, so let me define this a bit more precisely. Natural language math is written in languages, like English, French, et cetera. By formal language, I mean languages such as Lean. And I'm sure many of you have heard

**[0:49](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=49s)** of Lean or some other theorem proving language. Now, why would you translate natural language math into formal language math? What's wrong with natural language math? The problem is that often human-written proofs are incomplete, meaning they are missing steps. And the human mathematicians may not be aware of that. Worse, sometimes the proofs are incorrect. By translating from natural language math to formal language math, we can deploy the Lean theorem prover, and we can check whether or not the theorem was indeed proven. So now we want to build a box that takes this input natural language math and produces this output equivalent formal language math. What do we mean by equivalent? What we mean by equivalent is what

**[1:38](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=98s)** I refer to as semantic equivalence, meaning that the semantic content of the Pythagorean theorem that is input to your box must be the same as the semantic content of the output Lean. It must talk about right angled triangles, and the relationship must be the same. That's what we mean by equivalence. So the task we set ourselves was the following. We wanted to build such a box. We wanted this box to be 1000x smaller than the frontier models, at least 1000x smaller, maybe even smaller. And the question we posed was, how do we train such a model? How do we build such a model such that it outperforms the largest frontier models out there on this one task of autoformalization? So the property that I came up with,

**[2:31](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=151s)** I call it semantic alignment. The concept of semantic alignment is not new. People have talked about it in many settings. But in mathematics, it takes a particular meaning. What we mean by semantic alignment with respect to the autoformalization problem is as follows. So recall, again, what the autoformalization problem is. You have natural language math represented in one modality and formal language math. And the property that we want the model to possess is as follows. If two objects which are represented in different modalities, but they have the same semantic content, then we want them to be close by in the embedding space of the model. If they have different semantic content, then we want them to be far apart. And by imbuing the model with this property, what we then

**[3:22](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=202s)** do is we make it much more effective at the autoformalization problem. At retrieval time, when you do the retrieval, it's far more effective. Now this is valuable, not only for translating natural language math into formal language math, but it's also valuable when you do code translation from one language to another or if you're going from a specification to a circuit. Or if you want to connect definitions from different areas of math, you want to see relationships between different definitions in different areas of math, and thus discover new math and be able to do that with very small-scale models, not necessarily having access to frontier models, this property can get you there. So we trained our models using this technique. And we developed a particular recipe

**[4:09](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=249s)** called semantic contrastive learning, where we imbued the model with this property, meaning that if two objects have the same semantic content, they are close by in the embedding space. And the result was a far more powerful model than frontier models on all the benchmarks that we tested. And now we are taking this idea and to the setting of code translation. So we're building a tool that would take programs in legacy languages, like COBOL, translating them into Python. And we are deploying verification tools and automated testing tools on the input program. In this setting, we don't need specifications because the input program is the specification. And we are using techniques, like LLM-driven symbolic execution to generate a test suite.

**[4:59](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=299s)** Now that we have that test suite, we can use it on the output to check whether or not the input output programs are semantically equivalent. And of course, this has a strong business case out there for code translation and so on and so forth. So the takeaway is in settings where you have access to formal objects, and you're doing translation of formal objects or even informal objects from one modality to a formal object in another modality or two formal objects, then imbuing the model with the property of semantic alignment is a great way to build a system that can scale and be at a much smaller level, but still be able to scale to very large code bases and so on. With that, I'll end my talk.

**[5:46](https://www.youtube.com/watch?v=e0hQ4_gqKMs&t=346s)** Thank you for your attention. [APPLAUSE]
