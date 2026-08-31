---
id: hNqLSRB0SM4
title: "Worm2Vec: Embedding Malicious Code for Efficient Clustering & Classification"
slug: worm2vec-embedding-malicious-code-for-efficient-clustering
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 29
published_at: 2018-11-16T17:23:25Z
video_id: hNqLSRB0SM4
youtube_url: https://www.youtube.com/watch?v=hNqLSRB0SM4
tags: ["camlis", "camlis2018"]
transcript: false
---

# Worm2Vec: Embedding Malicious Code for Efficient Clustering & Classification

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `29 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=hNqLSRB0SM4) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Bayan Bruss, Capital One
Worm2Vec: Embedding Malicious Code for Efficient Clustering & Classification (slides: https://www.camlis.org/c-bayan-bruss/)

Every day, a large number of new specimens of malware are detected worldwide. Often these specimens are variants on existing malware or combinations of older functionality. This creates a need to identify if a piece of malware is similar to existing malware and what functionality is known about the new sample.  At the same time, the scale and latency requirements leave little room for full reverse engineering of each sample. Current static methods like signature matching have limited efficacy and are easily bypassed with small changes to the source code. As a result there is a need for a solution that is fast, scalable, can compare observed malware binaries in a way that is robust to small changes and obfuscation tactics. We propose the use of a neural embedding model which learns representations of opcodes and operands in disassembled binaries based on their usage patterns across a large corpus of binaries. In this model each line of a function is treated as a combination of opcodes & operands each drawn from an embedding space. Lines that appear near one another within a function are assumed to be contextually relevant to one another.  The model then seeks to determine lines of embedded opcodes and operands that are contextually relevant from those that are not, learning the best representation of these codes to do so.  Once trained, these learned embeddings can be used to efficiently generate a statistical representation of an unseen binary allowing for clustering and classification. This unsupervised method avoids problems with highly heterogenous or scarce labeled data. It allows for clustering of malware based on functionality in a way that is not affected by small changes in the code. Initial results also indicate that these embeddings can be used to facilitate training of classifiers where labeled data is available.
