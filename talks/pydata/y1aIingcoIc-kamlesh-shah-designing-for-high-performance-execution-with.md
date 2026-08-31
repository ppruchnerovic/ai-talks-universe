---
id: y1aIingcoIc
title: "Kamlesh Shah - Designing for high-performance execution with Arrow and Polars | Pydata London 26"
slug: kamlesh-shah-designing-for-high-performance-execution-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Kamlesh Shah"]
channel: null
duration_min: 39
published_at: 2026-06-15T15:55:10Z
video_id: y1aIingcoIc
youtube_url: https://www.youtube.com/watch?v=y1aIingcoIc
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Kamlesh Shah - Designing for high-performance execution with Arrow and Polars | Pydata London 26

**Kamlesh Shah**

`PyData` · `PyData` · `2026` · `39 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=y1aIingcoIc) · [Conference site](https://pydata.org/)

## Description

Kamlesh Shah - Columnar Thinking - Designing for high-performance execution with Arrow and Polars

When building high-performance systems for analytical workload, we often focus on the efficiency of the algorithm, like reducing Big-O complexity or optimising numerical routines. Yet in real world workloads, the decisive factor is not just the algorithm but the shape of how the data is laid out, traversed, and distributed across processes.

This talk will cover aspects of mechanical sympathy, focussing on how structures in memory can benefit from cache-sensitive, SIMD-enabled (vector instructions) CPUs, constrained by memory bandwidth and optimised for predictable, contiguous access.

We will use real-world examples to show how minimising serialisation overhead and enabling efficient cross-process and cross-language data exchange reduces the cost of data movement across systems. Beyond single-system performance, we will examine why Arrow’s standardised, zero-copy columnar format is a critical enabler of distributed execution. We will see how columnar formats support scalable computation across threads, processes, and distributed nodes.

Everyday production-scale data and systems engineering still reflects a row-oriented mental model. Loops, iterations, mutations are seen as easy to read and are understandable. While these work for small datasets and toy models during explorations in notebooks, they fail to perform when workloads scale - be it for rolling analytics, high-throughput pipelines or multi-million row aggregations. This mismatch between row-wise thinking and modern CPU architecture becomes a structural bottleneck that becomes very costly to fix.

We’ll explore the shift from row-oriented design to columnar thinking, designing and developing high-performance workloads right from the onset. Using Arrow’s columnar memory format and Polars’ execution engine, armed with concrete examples from real-life quantitative calculations, we will examine how contiguous buffers, SIMD-compatible layouts, and lazy query planning are a natural combination for performant analytical workloads.

You’ll leave with:
1. A clear understanding of how columnar memory impacts execution, in contrast to row-oriented or traditional vectorised approaches.
2. Practical patterns for structuring column-first transformations.
3. Insights into how Arrow reduces data movement overhead in distributed systems.
4. Guidance on when lazy execution and query optimisation matters.
5. Ideal design principles for building scalable calculation pipelines with Polars and Arrow tools.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
