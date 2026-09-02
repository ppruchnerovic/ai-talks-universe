---
id: fUS6QTTGgjA
title: "Reproducibility and Data version control for LangChain and LLM/OpenAI Models"
slug: reproducibility-and-data-version-control-for-langchain-and
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Amit Kesarwani"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 58
published_at: 2023-12-01T16:25:45Z
video_id: fUS6QTTGgjA
url: https://www.youtube.com/watch?v=fUS6QTTGgjA
youtube_url: https://www.youtube.com/watch?v=fUS6QTTGgjA
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Reproducibility and Data version control for LangChain and LLM/OpenAI Models

**Amit Kesarwani**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `58 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=fUS6QTTGgjA) · [Conference site](https://mlopsworld.com/)

## Description

Speaker: Amit Kesarwani, Director of Solutions Engineering at Treeverse

Abstract: In the last couple of years, Large Language Models (LLMs) have really skyrocketed in popularity and usefulness. Companies have harnessed this novel approach to machine learning and AI to build Foundation Models. A Foundation Model is an AI neural network — trained on mountains of raw data, generally with unsupervised learning — that can be adapted to accomplish a broad range of tasks.

Working with Foundation Models, however, differs from “traditional” ML. Instead of creating a new model from scratch using training and validation data for the task at hand, users of foundation models typically take an existing model, including its knowledge of the world, and “bend” it to fit a new task: adding more business or domain-specific knowledge to the existing model in order to adapt it to a new task. There are various techniques to achieve this, such as Fine Tuning, Prompt Engineering and Retrieval Augmented Generation.

To make an LLM application useful, this step is only one part of a sequence of operations that are required:

That’s where LangChain comes into play. LangChain is a comprehensive library of open-source components that help abstract away a lot of the complexity of working with LLMs.

Foundation models generally learn from unlabeled datasets, saving the time and expense of manually describing each item in massive collections. However, as data grows, the challenge of efficiently managing and controlling large datasets becomes more pronounced. Also, reproducibility, a core problem in ML, is even harder when it comes to LLMs. But you can achieve reproducibility easily with LangChain and lakeFS.

lakeFS is an open source, scalable data version control system that works on top of existing object stores. It allows users to treat vast amounts of data, in any format, as if they were all hosted on a giant Git repository: branching, committing, traversing history – all without having to copy the data itself. LangChain now includes an official lakeFS document loader. Using the document loader, users can now easily read documents from any lakeFS repository and version, with little configuration or coding.
