---
id: uu9BfD1A9uU
title: "Alessandra Costantino - What We Expect from XAI - A scientist’s experience Pydata London 26"
slug: alessandra-costantino-what-we-expect-from-xai-a-scientists
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Alessandra Costantino"]
channel: null
duration_min: 31
published_at: 2026-06-15T15:55:11Z
video_id: uu9BfD1A9uU
youtube_url: https://www.youtube.com/watch?v=uu9BfD1A9uU
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Alessandra Costantino - What We Expect from XAI - A scientist’s experience Pydata London 26

**Alessandra Costantino**

`PyData` · `PyData` · `2026` · `31 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=uu9BfD1A9uU) · [Conference site](https://pydata.org/)

## Description

Explainable AI is frequently invoked to make machine learning systems understandable and trustworthy. In real applications, however, explanations are often expected to justify decisions and support action. Drawing on experience with remote sensing–based risk monitoring, this talk examines the gap between the guarantees of explainability methods and the expectations placed on them by different users. It discusses how explanations can inform practice, how they can be misinterpreted, and when focusing on explainability may obscure deeper problems in models or data.

Explainable AI (XAI) emerged as a major research topic with the rise of deep learning and is now being adopted in domains where predictive models support high-impact decisions such as healthcare, finance, environmental monitoring, and public policy. As machine learning systems move into operational use, explanations are increasingly relied upon not only to understand models but also to justify and guide real decisions.
Conceptually, an explanation provides information that allows a human observer to understand a system’s behaviour. In machine learning, the term refers to a broad family of approaches, ranging from interpretable models to post-hoc analysis methods. These techniques are often presented as a way to make complex models understandable and usable by human stakeholders.
A concrete example comes from a project in which I applied machine learning to earth observation data for urban resilience, where explanations were expected to help local authorities plan maintenance and intervention actions to mitigate the impacts of natural hazards in cities. My role as the data scientist placed me between the domain specialists curating the data and the end users relying on the model’s outputs. In practice, this meant translating between different questions: domain specialists wanted to know whether the model’s behaviour made sense given their knowledge of the phenomenon, while end users wanted to know how the outputs could guide concrete actions and planning decisions.
This experience motivates a closer look at what contemporary explainability methods are intended to provide to different users. Many widely used approaches—particularly post-hoc feature attribution techniques—are often interpreted as revealing the reasoning of a model. In practice, however, they typically provide local approximations or sensitivity analyses rather than faithful descriptions of the decision process. For example, feature attribution methods such as SHAP may be read as identifying causal factors, and saliency maps may appear meaningful even when weakly connected to the model’s actual reasoning.
I unpack explainability in contemporary machine learning practice by asking what explanation methods actually guarantee—and what they do not. Drawing on my experience working between domain experts and end users, I reflect on how XAI functions in operational settings and on the expectations attached to explanations when they are used to support decisions.

Intended audience
The talk is aimed at machine learning practitioners, researchers, data scientists, and applied scientists who work with predictive models, as well as anyone who is interested in interpretation of model outputs in practice (including domain experts and decision-makers). No prior expertise in XAI is required.
Type and tone of the talkThe presentation is conceptual and experience-driven rather than mathematical. It will use concrete examples and intuitive explanations rather than formal derivations. The tone is reflective and discussion-oriented, focusing on practical interpretation rather than algorithmic detail.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
