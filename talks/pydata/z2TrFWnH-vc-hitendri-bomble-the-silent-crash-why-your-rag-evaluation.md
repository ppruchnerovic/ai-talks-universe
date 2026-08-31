---
id: z2TrFWnH-vc
title: "Hitendri Bomble-The Silent Crash:Why Your RAG Evaluation Metrics Are Lying to You | PyData London 26"
slug: hitendri-bomble-the-silent-crash-why-your-rag-evaluation
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 33
published_at: 2026-06-15T15:55:10Z
video_id: z2TrFWnH-vc
youtube_url: https://www.youtube.com/watch?v=z2TrFWnH-vc
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Hitendri Bomble-The Silent Crash:Why Your RAG Evaluation Metrics Are Lying to You | PyData London 26

**Speaker not identified**

`PyData` · `PyData` · `2026` · `33 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=z2TrFWnH-vc) · [Conference site](https://pydata.org/)

## Description

Hitendri Bomble - The Silent Crash: Why Your RAG Evaluation Metrics Are Lying to You

We rely on dashboards to tell us if our RAG system is working. But most standard metrics, Cosine Similarity, BLEU, and even BERTScore, are fundamentally broken for measuring factual correctness. They measure text overlap or semantic drift, not truth.

This means you can have a "90% Accurate" system on paper that hallucinates dangerous misinformation in production. This talk dismantles the current state of RAG evaluation. We will look at why "Golden Datasets" are often contaminated, why "LLM-as-a-Judge" is biased towards its own output, and how to build a robust, adversarial evaluation pipeline that actually catches failures before your users do.

Picture this: You’ve just finished your RAG pipeline. The test dashboard is all green, Context Recall is 85%, Answer Relevance is 92%. You deploy with confidence. Ten minutes later, a user asks a simple question, and the bot confidently gives the wrong answer.

Why did the metrics pass? Because similarity is not correctness. To a vector database, "The treatment is safe" and "The treatment is not safe" look nearly identical, they share the same words and sentence structure. But logically, they are opposites. Standard metrics like Cosine Similarity or BLEU often completely miss these critical negations.

In this talk, we are going to stop relying on "vibe checks" and start treating Evaluation as a software testing problem. We’ll look at why traditional NLP metrics are useless for RAG and move toward the new standard: LLM-as-a-Judge. We will discuss the messy reality of using GPT-4 to grade Llama-3, how to catch "Self-Preference Bias" (where models just like their own writing style), and how to do all of this without bankrupting your API budget.

Outline
- Real-world examples where high metrics hid major failures, and why "Finding the doc" (Retrieval) is different from "Answering the question" (Generation).
- Why Your Metrics Are Broken: Why Cosine Similarity is good for search but bad for truth, and why BLEU scores punish correct answers just for using different synonyms.
- Using models (like G-Eval) to grade logic and tone, and solving the "Judge Paradox" by swapping options to remove Position Bias.
- Building a "Hard" Test Set: How to stop testing on easy questions and generate adversarial "Trick Questions" that specifically target your retrieval gaps.
- Key Takeaways: A practical strategy for using metrics, plus a look at tools like Ragas and DeepEval.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
