---
id: Usv9kEwi93c
title: "Serverless Data Processing Architecture for Binary Analysis"
slug: serverless-data-processing-architecture-for-binary-analysis
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: "CAMLIS"
duration_min: 22
published_at: 2018-11-16T17:20:46Z
video_id: Usv9kEwi93c
url: https://www.youtube.com/watch?v=Usv9kEwi93c
youtube_url: https://www.youtube.com/watch?v=Usv9kEwi93c
tags: ["camlis", "camlis2018"]
topics: []
transcript: false
---

# Serverless Data Processing Architecture for Binary Analysis

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `22 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=Usv9kEwi93c) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Kyle Gwinnup, CarbonBlack
Serverless Data Processing Architecture for Binary Analysis (slides: https://www.camlis.org/kyle-gwinnup/)

Building a file processing pipeline can sometimes be a requirement of many data scientists. However, this ever expanding role of a data scientist doesn’t have to take a large part of our time. Serverless architectures, as many large tech companies are developing, provide just the solution data scientist are looking for. At CarbonBlack Threat Research, we were able to quickly stand up a scalable system for our binary analysis needs. This system enabled us to focus more on the data and thinking of features rather than the maintenance and configuration of systems and services. This talk will walk through, with code examples, how we were able to build a scalable serverless system using AWS to build a feature rich dataset for various types of file analysis.

Three main topics will be covered:
Cloud design patterns for ingesting and pre processing binaries to prepare for analysis,
deploying serverless docker containers for custom analysis, and finally,
how data is stored and accessed.

As part of our analysis step, a description of the modular approach we took to feature extraction which allows our researchers to pose questions about binaries and quickly extract features from the corpus or sample set. Additionally, some tips when developing these types of system.
