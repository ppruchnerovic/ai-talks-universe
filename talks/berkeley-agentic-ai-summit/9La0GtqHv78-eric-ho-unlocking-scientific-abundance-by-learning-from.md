---
id: 9La0GtqHv78
title: "Eric Ho - Unlocking Scientific Abundance by Learning from Superhuman AI"
slug: eric-ho-unlocking-scientific-abundance-by-learning-from
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Eric Ho"]
channel: "Berkeley RDI"
duration_min: 13
published_at: 2026-08-11T19:58:40Z
video_id: 9La0GtqHv78
url: https://www.youtube.com/watch?v=9La0GtqHv78
youtube_url: https://www.youtube.com/watch?v=9La0GtqHv78
tags: []
topics: []
transcript: true
---

# Eric Ho - Unlocking Scientific Abundance by Learning from Superhuman AI

**Eric Ho**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=9La0GtqHv78) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,918 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=9La0GtqHv78&t=1s)** ERIC HO: Let me quickly introduce myself. I'm Eric, I'm co-founder and CEO of Goodfire. We're the leading AI interpretability research company, so we spent all day, thinking about what's going on inside the mind of an AI model. And today, I'm going to talk to you about one idea, which is that we can reverse engineer superhuman AI models to understand their computations, to advance science and teach us about the world. And there will soon, hopefully, be slides about this. Well, in the meantime, I can talk a little bit about what we're up to. So Goodfire AI interpretability research company. We spent all of our days thinking about what's actually going on inside the mind of AI models, so really looking inside of an AI model,

**[0:51](https://www.youtube.com/watch?v=9La0GtqHv78&t=51s)** looking at their neurons, their parameters, their computations, with the hope of understanding what they're doing. The reason why we care so much about understanding what we're doing is that, well, first of all, we really should understand the most consequential technology of all time. We should really understand these systems that we're putting everywhere in the world. But also, we hope to build towards a future of what we call intentional design, which is a future where we can actually understand, and edit, and debug these systems much more written software, not just training them by trial and error, as we do today. And so that's our whole agenda. We're headquartered in SF and have been around for a couple years, looking into these problems. And I think one of the most interesting things about this is that there are already superhuman AI models that

**[1:41](https://www.youtube.com/watch?v=9La0GtqHv78&t=101s)** are out there in the world today, for narrow game-playing scenarios, like AlphaZero and AlphaGo. Those are already superhuman at their tasks. And there are also superhuman scientific models that we hope to reverse engineer, understand, and then, in that way, push forward science. And I think that's one of the most promising directions of our time. Yeah. Yeah, you can ask question. Sure yeah. Kill time. Oh yes questions. AUDIENCE: [INAUDIBLE].

**[2:32](https://www.youtube.com/watch?v=9La0GtqHv78&t=152s)** How do you use it for steering, aligning AI [INAUDIBLE]? ERIC HO: Yeah, so the question was about responsible AI, steering, and aligning AI models. This is a really big part of our original motivation for founding the company. It feels difficult for me to see a future, where we can really align AI models and get the systems that we want without deep understanding. And so a big part of our direction is, yeah, intentional design, in other words, actually steering and guiding training, such that we can pick the updates to models that we actually want and then remove the updates that we don't want. So, for example, we have techniques available. One of these techniques is called reinforcement learning, with feature rewards.

**[3:19](https://www.youtube.com/watch?v=9La0GtqHv78&t=199s)** A feature is an internal computation of a model, that we've extracted, and we understand what it does. And so features can be anything from unsafe behavior, hacking Hugging Face might be a feature. And if we can extract that, and we can say, hey, we don't want that in the model, we can actually steer and use that feature to steer and guide the training of a model. So a big part of our direction, and we've essentially developed these techniques that can take arbitrary features, train on them, and steer and guide the training of models. Yes. AUDIENCE: [INAUDIBLE] ERIC HO: So the question is, it sounds like we're an AI governance company, are we? So, not quite. We are developing a product.

**[4:09](https://www.youtube.com/watch?v=9La0GtqHv78&t=249s)** It's called Silico. Oh slides. Wonderful. But yeah, we're developing a product called Silico. You can think of it like an AI neuroscientist that goes in, and understands, designs, and debugs models. So you can think of us as a different way to train AI models. And we're both doing the science in order to uncover a different way to train models, as well as building the platform that brings that to you. OK great. We have slides. I did not remember what slides I had, so this is very helpful. So we think we can unlock a future of scientific abundance. And one of the best possible ways to do that is by truly understanding superhuman AI models. The hard problem about-- even if you take a superhuman AI model as a given, when you look inside of this model,

**[4:59](https://www.youtube.com/watch?v=9La0GtqHv78&t=299s)** all you're going to see are a bunch of random-looking numbers and computations, that you can't make heads or tails of as a human. These models are getting really big, like a trillion parameter models. No human can actually understand a bunch of trillion numbers that are hidden inside their weights and parameters. And when you also ask a model to explain its own computations, they are often unfaithful. So the actual tokens that the model emits, often, are not actually faithful to their computation. There are clashes between those. So you can't necessarily trust a model to explain exactly what's on its mind, and how it's forming its computation. And so this is really the quest. And the problem of interpretability is how do you take this jumbled mess of numbers and parameters and turn that into a human understandable explanation, such

**[5:48](https://www.youtube.com/watch?v=9La0GtqHv78&t=348s)** that we can understand something about this model. And interpretability, really, is the bridge to reverse engineering the computations of these models to teach us about the world. So I'll give you a problem setup here. Who's familiar with move 37, AlphaGo, Big Moment? OK, so AlphaGo was this go playing AI that Google created. And there's this big moment where AlphaGo was competing against Lee Sedol, who was the best Go player in the world at the time, in this best of-- I believe it was seven series. And in game 2, AlphaGo made a very, very surprising move, move 37, that everyone originally thought was a total mistake.

**[6:37](https://www.youtube.com/watch?v=9La0GtqHv78&t=397s)** It turns out that this was a really consequential move that shifted the dynamic of the game. And AlphaGo beat Lee Sedol handily. And so the question is, what was going on there? What was happening inside of AlphaGo's representations that caused it to have-- to create this move. And it didn't do this by random. There was some rich representation space of AlphaGo, that made it actually be able to some richer understanding of the game than any human had, that made it be able to produce this move of such a high caliber. And so the setup here is we as humans have a representation space. Let's call it H. AlphaGo machines, AI, have some representation space, let's call it M. What we're really interested in is this intersection of M and H, where

**[7:27](https://www.youtube.com/watch?v=9La0GtqHv78&t=447s)** we may be able to learn new things about the world from AI, by actually understanding their computation, but we have the capacity to understand what is actually going on. And this may sound like science fiction, but my co-founder, Tom, he's our chief scientist at Goodfire actually already did this with AlphaZero, the best, better than any chess player alive. So they were able to show in a couple of papers at GDM. He was actually collaborating directly with Demis on this, that reverse engineering AlphaZero is possible, and that we could actually reverse engineering in narrow positions, computation that actually taught human chess grandmasters how to play chess more effectively. And so this is a large part of our mission, which is to understand, really, the scientific foundations of AI models, such that we can extract scientific knowledge

**[8:17](https://www.youtube.com/watch?v=9La0GtqHv78&t=497s)** from these models, and then teach them to humans so that we don't get left in the dust. One of the ways that we actually do this, how you actually operationalize this, is by training, this type of AI neuroscientist that goes in across trillion parameter models, billion parameter models to actually reverse engineer their computations, and understand what looks like gibberish as a neuron to a human, and actually translate that into a human interpretable concept. You can do things with arbitrary concepts inside language models and image models. You can extract the concept of the Golden Gate Bridge or sycophancy, agreeing with the user. But the point of today is to talk about much more interesting behaviors, like novel science in biology. To start, it's really important to be

**[9:08](https://www.youtube.com/watch?v=9La0GtqHv78&t=548s)** able to understand what the structure is of a model. And so we've released recent research, talking about this concept of neural geometry. AI models think in complex shapes. If you take a look at that manifold, usually, it spins, and it's like some type of curved geometry, rather than just words or directions or individual numbers. And so we're really interested in this idea of what is the structure contained inside these models. Because the structure may contain insights about our natural world, that we would not have gotten to ourselves. And we'll walk through a couple examples of the things that we've already done. We are working with a company called Prima Menta. They train an epigenetics foundation model called

**[9:58](https://www.youtube.com/watch?v=9La0GtqHv78&t=598s)** Pleiades, which they use in order to predict Alzheimer's. And it is actually state of the art at Alzheimer's detection from cell-free DNA, but they had no idea how this model actually worked. And so what we were able to do is use our AI neuroscientist to go in, reverse engineer that model's computations, and actually uncovered that the model is mostly using this fragment omic biomarker to predict Alzheimer's. This was a surprising result that wasn't contained in the literature at the time. This was published in the New York Times a few months ago. And it generalized, when tested on an independent cohort. And how it actually represented this fragment signal is in this half-donut manifold shape that represented fragment length.

**[10:50](https://www.youtube.com/watch?v=9La0GtqHv78&t=650s)** And so we needed to both develop the tools in order to extract manifold computations from models, as well as understand exactly what it was doing, which was representing fragment length. Example number 2 is a research that we've done with Mayo Clinic on understanding genetic variants and mutations. So we primarily focused on SNPs here, so single nucleotide polymorphisms, on single genetic variants. We wanted to understand what variants actually caused disease, which ones are pathogenic. And we were able to use the embeddings of a DNA transformer, a DNA foundation model, in order to get state-of-the-art results on predicting which variants actually cause disease. And you have this really rich structure that we were able

**[11:44](https://www.youtube.com/watch?v=9La0GtqHv78&t=704s)** to map the model into, in order to get this state-of-the-art accuracy. So that's the high level of all of this. We're just at the beginning of this quest of taking superhuman scientific models, understanding what they've learned, validating them. You can think of this as a hypothesis generation loop for novel insights and discovery. And then I think this is just one of the most promising ways that we have to advance science, especially since AI capabilities are going up and to the right. And so, yeah, we've developed this system. It's called Silico. It'll actually be in public access next week, so keep an eye out for that. But you will be able to actually apply these techniques to any model that you're training in biology, materials,

**[12:36](https://www.youtube.com/watch?v=9La0GtqHv78&t=756s)** physics, all these scientific models. We have essentially a system that unleashes our AI neuroscientists to go and reverse engineer their computation. OK, that's all I got. Thanks everyone.
