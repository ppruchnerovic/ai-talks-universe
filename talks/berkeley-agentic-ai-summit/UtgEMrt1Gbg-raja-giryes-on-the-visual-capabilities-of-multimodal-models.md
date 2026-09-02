---
id: UtgEMrt1Gbg
title: "Raja Giryes - On the Visual Capabilities of Multimodal Models"
slug: raja-giryes-on-the-visual-capabilities-of-multimodal-models
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Raja Giryes"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T01:57:47Z
video_id: UtgEMrt1Gbg
url: https://www.youtube.com/watch?v=UtgEMrt1Gbg
youtube_url: https://www.youtube.com/watch?v=UtgEMrt1Gbg
tags: []
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# Raja Giryes - On the Visual Capabilities of Multimodal Models

**Raja Giryes**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=UtgEMrt1Gbg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,612 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=2s)** RAJA GIRYES: Hello, everyone. I want to thank the organizers and all the previous speakers for the interesting talks. My talk is taking a slightly different angle than what was presented before. So everyone here was talking about coding agents and how we can extend them. Here, I want to talk about adding new capabilities, which is going to multimodal. So most current models focus on how to improve coding because it's easier to work like that. But when you hear me now, you don't just see a text. You see me. You see everything. So we live in a multimodal world. And the question is, what are the current visual capabilities that we have in multimodal models?

**[0:52](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=52s)** So there are various challenges when we look at multimodal models. And I think that one of the interesting things that we see in the field is that once people start asking the right question, in one or two years, we start seeing solutions. So a few years ago, with my group, we had some works on compositional reasoning. There were some observations that one of the problems of old multimodal models, when they look at captioning of images, so for example, if I want to generate or want to describe an image with three zebras and two giraffes. So basically, all the numbers and names are mixed together. And the model is treating everything as bag of words.

**[1:43](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=103s)** And then there is some problem with compositionality. And then with my group, we had various work on improving the compositionality. And since then, things improved. So we used some tree structures. We took the words and decompose them into trees. We basically had more dense and aligned captions. And basically, we taught this model to be structured. So you can see them in these works. Afterwards, we found other problems that exist in these models. So in two works, we try to analyze what happens if you try to work with these models and see what happened in the workflow of understanding. So in one work that was done with my colleagues, which

**[2:34](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=154s)** is called performance gap in entity knowledge and was published in ASCL one year ago, we basically tried to see where in multimodal models we can see the reasoning. And one of the problems that we see in current multimodal models is that basically, if you look at all modern multimodal models, you have very strong LLM and a nice visual head attached to it. So we invest lots of resources in training LLMs. But then, we have some nice visual language model that we found somewhere. We attach to it. We train them together afterwards with some post-training. And then when you analyze what happens when these models try to do some multimodal understanding,

**[3:22](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=202s)** you see that most of the analyzes that happen happen in the LLM part and not in the visual part. Another work we try to analyze what happened if we try to do in-context learning. So in LLMs, we know that in-context learning is great. But then, the strange thing that we found in VLMs or multimodal models, is that if you give in-context learning that is too long with too many images, basically, the models start to get confused. And again, the reason for that is that currently, when we train multimodal models, we mainly rely on the language part. And the question is maybe we need to make a certain shift. So the focus in my talk would be on a specific ability of multimodal models, which is spatial cognition.

**[4:14](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=254s)** And there is an interesting work of my colleagues that was published two years ago, which is whether spatial cognition emerge in Frontier models. And what they did is they checked various spatial cognition tests on multimodal models. And they checked some tasks like mental rotation. We get a shape. And then we ask, which shape is basically the same shape but rotated? Another interesting task is perspective taking. I am asking, what is, for example, the angle between the bat and the dog? And then, the question is whether such model can answer that. Another question is mass completion. We want to ask a model to solve this maze.

**[5:06](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=306s)** And then, another interesting task is shortcut discovery. In shortcut discovery, basically, you show a model, a walkthrough, through a place, but you don't go in the shortest path. And then you ask the model to go in the shortest path. And you check whether the model is capable to do that. So all of these are very important task in spatial cognition. The interesting thing is that two years ago, all the models were very bad. If you take the Frontier models like GPT and other Frontier models, they would act really bad. But the interesting thing is, that once you start asking the question, you start to see improvement throughout time. So this work that was two years ago, you get that Frontier models are quite close to chance.

**[5:55](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=355s)** They are a bit better. January this year, there was an interesting work called Baby Vision. They made a similar exploration. And then they found that on January this year, the Frontier models will basically at the level of three-year-old child. So from models that don't know anything, we grew up to three years. So the interesting thing is that you see that once question is asked, sometimes, it's more important to ask the question. People start to pursue that. And in one and a half year, we go to three years, which is nice to grow to become three years old in one and a half year. But usually, we want to grow slower. Another interesting work, which is asked, compared how much time it takes for a human to solve a problem,

**[6:46](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=406s)** and then compare this time to what the models can do. And basically, they found that current Frontier models-- and this happened in February 2026-- can solve spatial cognition tasks that take for us as human 10 seconds. So if you think about it, like mental rotation, mess solving, it takes us sometimes to solve. So these models are able to solve only the tasks that we are able to solve in 10 seconds, which is not so great, but better than what we had before. And then if we look at the tasks that I talked before, so here, we can see the state of advance, since the initial work I mentioned by my colleagues was published

**[7:33](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=453s)** two years ago till today. So two years ago, for example, in perspective taking, the best models were close to chance. Two years after now, we can see that, for example, Opus 4.6 and Gemini 3.1 are basically almost close to 100%. Very impressive improvement in just two years. In mass completion, we are still not so great. But just three months ago, from close to chance, we see that, for example, GPT 5.4 got a great leap. And the same happened with shorter discovery. So we see that great improvement in these models. And then the question is, why this happens. So in a recent work that I-- in a work that we have done with my colleagues at Apple,

**[8:25](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=505s)** we ask the question of whether multimodal models imagine electric chip. And the answer is yes. So I don't have much time. I will just mention briefly, and then you can look at the paper. Basically, what we did, we studied various spatial cognition tasks. And we studied them in an open loop case. Open loop case means that we just show a model the first frame. And then we ask the model to try to solve the game by giving us what step it should do. And the interesting thing is, that we found that if we look at the model that is not generating any image, it's just it can receive images but cannot generate image. And basically, we probe the weights. We can take a transformer, attach to the weights, probe it.

**[9:18](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=558s)** The interesting thing that we found is that the model is imagining internally how to solve the problem. So with different tasks. For example, if we ask if two shapes have the same chirality, we basically able to see that the model in its internal weights is reconstructing the visual thing that we would do. If we look at two shapes and want to understand if we rotate them, they become the same. So we found that the model is doing it in its internal weights. And maybe this is the reason for the great improvement that we see that models started to imagine. And the same happened, for example, if we want to assemble characters. So we can see that models in their internal weights assemble characters. And if we see that a model that is not able to generate visual thing is able in internal way to do that.

**[10:13](https://www.youtube.com/watch?v=UtgEMrt1Gbg&t=613s)** So what we've done, we added the ability to the model to imagine. We supervise it to imagine. And suddenly, we have seen improvement in performance by adding this imagination ability. So we have some more results. Because of time, I will skip them. But the interesting point is-- or there are two points I want to mention. One is asking the right question is very important to advance science. Second thing is that if we think about multimodal models, it's very important for the models not to focus on text, but also to focus on generating the visual part, and it helps the model to improve a lot. Thank you very much. [APPLAUSE]
