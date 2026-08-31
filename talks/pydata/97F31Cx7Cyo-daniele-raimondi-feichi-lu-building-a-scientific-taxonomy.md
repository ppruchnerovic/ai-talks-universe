---
id: 97F31Cx7Cyo
title: "Daniele Raimondi, Feichi Lu - Building a Scientific Taxonomy at Scale | Pydata London 26"
slug: daniele-raimondi-feichi-lu-building-a-scientific-taxonomy
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Daniele Raimondi"]
channel: null
duration_min: 37
published_at: 2026-06-15T15:50:45Z
video_id: 97F31Cx7Cyo
youtube_url: https://www.youtube.com/watch?v=97F31Cx7Cyo
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Daniele Raimondi, Feichi Lu - Building a Scientific Taxonomy at Scale | Pydata London 26

**Daniele Raimondi**

`PyData` · `PyData` · `2026` · `37 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=97F31Cx7Cyo) · [Conference site](https://pydata.org/)

## Description

Daniele Raimondi,
Feichi Lu - Building a Scientific Taxonomy at Scale with Graph Clustering, Embeddings, and LLMs

Scientific publishers tag millions of articles with author-provided keywords, but these keywords are noisy, inconsistent, and semantically ambiguous. "Machine learning," "ML," and "machine-learning" all mean the same thing, while other terms shift meaning across disciplines.

This talk presents a production pipeline that extends OpenAlex's 4-level hierarchy with a fifth in-house Concept layer, producing a 115K-concept scientific taxonomy.

SPECTER2 embeddings model semantic similarity, and per-field Leiden clustering with CPM resolution groups 100K+ concepts via mutual kNN graphs — with hyperparameters selected through grid search and custom pair-based evaluation. Qdrant enables vector-based hierarchical attachment.

LLMs are deployed at five targeted stages — granularity filtering, field classification, cluster renaming, explanation generation, and topic-assignment validation — while deterministic methods handle everything else, ensuring scalability and reproducibility.

The resulting taxonomy powers a paper-tagging pipeline where SPECTER2 retrieves ~150 candidates per paper across multiple text-splitting strategies, deterministic filters prune by field/subfield distribution and near-synonym merging, and an LLM reranker selects the final 5–8 concepts. These assignments enable applications such as temporal trend detection over emerging research topics and more.

Attendees will learn when to integrate LLMs in large-scale NLP pipelines, how to scale graph clustering to 100K+ nodes, and how to design hybrid embedding–LLM systems that turn noisy metadata into reliable scientific intelligence.

The problem
If you've ever tried to make sense of author-provided keywords across millions of papers, you know the pain. "Machine learning", "ML", "machine-learning": same thing, three entries. Other terms look identical but mean completely different things depending on the field. Manual cleanup? Doesn't scale. Regex and string matching? Misses the semantics entirely.

What we built
We took OpenAlex's 4-level hierarchy (Domain → Field → Subfield → Topic) and added a fifth in-house Concept layer: 115K+ fine-grained concepts, each with a clear position in the tree.

The core idea: embed all candidate concepts with SPECTER2, build a mutual kNN similarity graph per field, and cluster it with Leiden (CPM resolution) at 100K+ node scale. We tuned hyperparameters via grid search, scored against hand-curated concept pairs - things like "Cryptocurrency" and "Crypto Currency" must land together, while "Decision Trees" and "Random Forest" must stay apart.

LLMs come in at five specific points where embeddings alone aren't enough: filtering concept granularity, classifying into fields, renaming clusters, generating explanations, and validating topic assignments. Everything else is deterministic: no LLM in the loop means reproducible and cheap.

Paper tagging
Once the taxonomy exists, we use it to tag papers. With SPECTER2 embeddings, we retrieve an initial pool of ~150 candidate concepts per paper (eight different text-splitting strategies over title, abstract, and keywords). Deterministic filters prune by field/subfield distribution and merge near-synonyms with Jaccard + union-find. Then an LLM reranker picks the final 5–8 concepts with domain verification and keyword mapping, ranked.

What comes next
With millions of papers tagged consistently, the obvious next step is trend detection: tracking how concept frequency and co-occurrence shift over time to spot emerging research areas. We'll sketch out the approach.

Tech stack
SPECTER2 (embeddings) · igraph + leidenalg (Leiden/CPM clustering) · hnswlib (ANN for kNN graphs) · Qdrant (vector search for hierarchical attachment) · Azure OpenAI (structured LLM inference) · human + automated validation framework

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
