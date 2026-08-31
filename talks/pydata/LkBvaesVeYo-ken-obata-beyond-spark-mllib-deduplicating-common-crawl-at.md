---
id: LkBvaesVeYo
title: "Ken Obata - Beyond Spark MLlib: Deduplicating Common Crawl at Scale | Pydata London 26"
slug: ken-obata-beyond-spark-mllib-deduplicating-common-crawl-at
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Ken Obata"]
channel: null
duration_min: 35
published_at: 2026-06-15T15:52:07Z
video_id: LkBvaesVeYo
youtube_url: https://www.youtube.com/watch?v=LkBvaesVeYo
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Ken Obata - Beyond Spark MLlib: Deduplicating Common Crawl at Scale | Pydata London 26

**Ken Obata**

`PyData` · `PyData` · `2026` · `35 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=LkBvaesVeYo) · [Conference site](https://pydata.org/)

## Description

Ken Obata - Beyond Spark MLlib: Deduplicating Common Crawl at Scale

Training large language models requires massive, high-quality text corpora—but web-scale datasets like Common Crawl contain significant near-duplicate content that degrades model performance and wastes compute. Existing solutions like Spark MLlib's MinHashLSH suffer from UDF serialization overhead and shuffle explosion, causing out-of-memory failures at scale.

We present a partition-aware MinHash LSH system that co-locates similar documents within Spark partitions, dramatically reducing cross-partition shuffles during similarity computation. Our approach combines vectorized MinHash generation using mathematical permutation tricks, band-based candidate filtering with configurable collision limits to handle edge cases like boilerplate false positives, and GraphFrames-based connected components for transitive deduplication.

Benchmarks on Common Crawl 253.4 million documents, generating 2.1 billion candidate pair
completed in under five hours on a 9-node r5d.8xlarge EMR cluster. We discuss key optimizations including partition-aware MinHash LSH and band collision filtering for common boilerplate content.
Attendees will learn partition-aware LSH design patterns, strategies for handling boilerplate-induced false positives, and how to integrate deduplication into existing Spark ETL pipelines. The system will be open-sourced, enabling practitioners to deploy production-ready deduplication pipelines for their own LLM training workflows.

Why This Matters for LLM Practitioners
Training data quality is the bottleneck for LLM performance. Research shows duplicate content causes memorization, reduced generalization, and wasted compute (Lee et al., 2022). Yet existing tools fail at web scale: Spark MLlib's MinHashLSH suffers shuffle explosion causing OOM errors, while Google's deduplicate-text-datasets requires 600GB+ RAM on a single machine.

What You'll Learn
This talk introduces a partition-aware MinHash LSH system built with PySpark and NumPy that scales horizontally on commodity clusters. The key innovation: using LSH band hashes to drive Spark's partitioning, co-locating similar documents before comparison and eliminating cross-partition shuffles entirely.

Target Audience
Data engineers and ML practitioners working with large text corpora for NLP/LLM applications. Familiarity with PySpark basics and general understanding of similarity matching is helpful but not required.

Talk Outline
Minutes 0-5: The deduplication challenge - why LLM training data needs deduplication, why O(N²) comparisons are infeasible, why you can't split into independent batches
Minutes 5-10: Why existing tools fail - MLlib shuffle explosion, Google's memory requirements
Minutes 10-18: Our solution - partition-aware MinHash LSH architecture, code walkthrough showing pandas_udf vectorization and band-based partitioning
Minutes 18-25: Worked example - following two documents through the pipeline: hashing → band assignment → partition co-location → local candidate generation → connected components
Minutes 25-30: Benchmarks and practical lessons - 253M documents, 2.1B candidate pairs, under 5 hours, under $100. boilerplate filtering with MAX_BAND_SIZE
Minutes 30-40: Q&A

Key Takeaways
How to use LSH band hashes to drive Spark partitioning for local similarity computation
Vectorized MinHash generation with NumPy and pandas_udf to avoid Python UDF overhead
Strategies for handling boilerplate-induced false positives at scale
A production-ready architecture that will be open-sourced

Background Knowledge
Basic PySpark familiarity (DataFrames, partitions). No prior knowledge of MinHash or LSH required — these concepts will be explained.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
