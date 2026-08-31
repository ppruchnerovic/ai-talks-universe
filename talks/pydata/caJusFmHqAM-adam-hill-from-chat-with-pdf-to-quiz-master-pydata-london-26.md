---
id: caJusFmHqAM
title: "Adam Hill - From Chat-with-PDF to Quiz-Master | Pydata London 26"
slug: adam-hill-from-chat-with-pdf-to-quiz-master-pydata-london-26
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Adam Hill"]
channel: "PyData"
duration_min: 38
published_at: 2026-06-15T15:54:12Z
video_id: caJusFmHqAM
youtube_url: https://www.youtube.com/watch?v=caJusFmHqAM
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Adam Hill - From Chat-with-PDF to Quiz-Master | Pydata London 26

**Adam Hill**

`PyData` · `PyData` · `2026` · `38 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=caJusFmHqAM) · [Conference site](https://pydata.org/)

## Description

From Chat-with-PDF to Quiz-Master: Live-Grading RAG with LLM-as-Judge in Python

Most RAG demos stop at retrieval and summarisation. In practice, we also need to measure the understanding of users, models, and the source material. This talk introduces a reusable evaluation pattern that turns any document into a live-graded “exam engine” using Python tools including Docling, DeepEval, and Marimo.

We will build a stateful application that generates multiple-choice and free-text questions from complex documents, creates realistic distractors, and scores answers in real time using an LLM-as-judge pipeline. The demo is intentionally playful, but each component maps to a production concern: layout-aware ingestion (tables and figures), synthetic QA dataset creation, semantic grading, and interactive evaluation loops.

Attendees will learn how to move beyond passive RAG towards systems that benchmark knowledge, support training workflows, and enable human-in-the-loop evaluation.

RAG systems typically answer questions but rarely evaluate whether the answer, or the user, actually demonstrates understanding. That requires structured datasets, grading logic, and application state, not just retrieval.

In this talk, we build a live-graded “knowledge arena”: a Python application that converts a dense technical document into an interactive quiz with two modes:
- Easy mode - automatically generated multiple-choice questions with plausible distractors
- Expert mode - free-text answers scored in real time using semantic LLM metrics

The implementation illustrates several reusable production patterns:
- Document ingestion (Docling): Extracting layout, tables, and figures so evaluation covers the full source rather than plain text only.
- Synthetic dataset generation (DeepEval): Creating “golden” QA pairs and automated distractors for benchmarking and training.
- LLM-as-judge grading: Scoring free-text answers with semantic metrics instead of brittle string matching.
- Stateful Python UI (Marimo): Managing interaction and evaluation loops without custom JavaScript.

Although the interface is playful, the architecture generalises to production RAG and agentic knowledge systems for benchmarking, training, and human-in-the-loop evaluation.

This talk presents a reusable LLM-as-judge architecture for evaluating understanding in RAG systems using synthetic QA generation and real-time semantic grading in Python. All demo components are pre-built and run locally with cached models and datasets.

Audience / Prerequisites
- Intermediate Python users familiar with basic LLM and RAG concepts (embeddings, retrieval).
- No prior experience with Docling, DeepEval, or Marimo required.

Key Takeaways
- A reusable LLM-as-judge evaluation pattern for RAG
- How to generate QA benchmarks from documents automatically
- Techniques for handling tables and figures in ingestion
- Where live grading fits into production workflows

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
