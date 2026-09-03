---
id: CBLUhM25I4A
title: "Shaghayegh Gharghabi - One Environment, Whole Lifecycle: Agentic Post Training for Nemotron in..."
slug: shaghayegh-gharghabi-one-environment-whole-lifecycle
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Shaghayegh Gharghabi", "One Environment"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:15:53Z
video_id: CBLUhM25I4A
url: https://www.youtube.com/watch?v=CBLUhM25I4A
youtube_url: https://www.youtube.com/watch?v=CBLUhM25I4A
tags: []
topics: ["Agents & orchestration", "Training, fine-tuning & model building"]
transcript: true
---

# Shaghayegh Gharghabi - One Environment, Whole Lifecycle: Agentic Post Training for Nemotron in...

**Shaghayegh Gharghabi, One Environment**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=CBLUhM25I4A) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*832 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=CBLUhM25I4A&t=1s)** SHAGHAYEGH GHARGHABI: Yeah. Hi everyone. I'm Shaya from NVIDIA. So I'm working as a deep learning scientist. And our team is mostly working on post-training reasoning model for finance using Nemotron model, LLM model, for NVIDIA. Today, I'm going to talk about a general goal of our team and what's the challenges we are facing, going through an example to show the challenges specifically and finally showing our result and impact on industry. About the goal, so our goal is basically sharing the open-source model that is doing the finance reasoning so everyone can use it. But it's not just sharing a checkpoint so everyone can load it and run the model, but we want to share the whole pipeline.

**[0:50](https://www.youtube.com/watch?v=CBLUhM25I4A&t=50s)** We want to share our data open so everyone can use our data. Not only that, they can generate the data using our pipeline, using our recipe, our model, and using our environment and pipeline. So basically, we want to share all orchestra that how we are going through this process. But before that, let's go to an example and show why this is challenging, why the finance is the issue and we are focusing on that. So just a big picture that-- for the finance model to answer a finance question, it should go through multiturn reasoning. So it's basically calling multiple tools, doing the web search, retrieving the different SEC filing. And not only retrieving them.

**[1:40](https://www.youtube.com/watch?v=CBLUhM25I4A&t=100s)** It's the long document. It's a complex document, different structure-- unstructured data, structured data. Models should understand all these documents. And not only understand that, it should do the financial math on those documents and, at the end, cite what part of this document was helpful to answer the question. So to clarify it, let's go through an example. So let's say it's calculate the inventory turnover for US steel in 2024. So model, to answer this question, should know what's the turnover formula and how to calculate that. Not only that, what kind of filing, what kind of form it needs to be called from which tool, from web, from SEC, and, when it's calling, do the extraction, understanding all

**[2:30](https://www.youtube.com/watch?v=CBLUhM25I4A&t=150s)** those documents, and calculate the formula, as you are seeing at the bottom of the slide. And I guess the last step is cite which part of this document was helpful for the model, so we can say these are the answers based on evidence, and we can confirm this is the correct one or not. But let's see how the models currently are doing on this benchmark. So we look at one of the famous benchmark that has been recently released on finance, and this is the result. The best closed model is approximately 64%. And open-source model performance is only 60%. They recently actually released a little more complicated finance benchmark. And the best performance currently is only 58%. So you can see how much gap we have to fill in.

**[3:22](https://www.youtube.com/watch?v=CBLUhM25I4A&t=202s)** To show our contribution, to summarize, I summarize it in four different pillars. We have done four main contribution. First is sharing to SDG pipeline, document-based SDG, template-based SDG. We shared our data publicly. We have more than one million data that you can access it right now. We trained some models using our own data based on our pipeline using SFT recipe, RL recipe, and we saw a great improvement on those model performance. Our pipeline also supporting RL fine-tuning using tool call, and all in all in one pipeline. Not only that, we already have two customers, finance, institute that, of course, the security is important for them because they are using finance data.

**[4:11](https://www.youtube.com/watch?v=CBLUhM25I4A&t=251s)** But they can use our pipeline without accessing to the internet. So they don't need to be worried about the security. And it's already enterprise ready. So you can use our pipeline. So to show that improvement we made through this pipeline and based on the data we generate, you can see, after fine-tuning Qwen model or Nemotron model, we have seen about 11% on Qwen model and 7% on Nemotron model performance. Not only that, without losing any accuracy, we reached 25% less token usage-- which less token, less cost, better life. So how we have done that, we have done all of this

**[5:01](https://www.youtube.com/watch?v=CBLUhM25I4A&t=301s)** through one pipeline orchestrated under NVFlow. You can do all the synthetic data generation model, fine-tuning, evaluation, and RL training only on one pipeline. And not only that, we made a big important decision in our pipeline having the shared single environment. And what does that mean? It means all the synthetic data generation, SFT tuning, RL tuning, all of them is just using the same tools, same formats. So no need for the worry about being consistent. All in all, we invite you to collaborate with us. Our [INAUDIBLE] data, all of them is shared publicly. So you can use it. And feel free to reach out to us for more collaboration. Yeah. Thank you for your time.
