---
id: a2As90UbmcQ
title: "Michel Semaan - Querying the queries: SQL Metaprogramming in Python | Pydata London 26"
slug: michel-semaan-querying-the-queries-sql-metaprogramming-in
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Michel Semaan"]
channel: "PyData"
duration_min: 35
published_at: 2026-06-15T15:54:11Z
video_id: a2As90UbmcQ
youtube_url: https://www.youtube.com/watch?v=a2As90UbmcQ
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Michel Semaan - Querying the queries: SQL Metaprogramming in Python | Pydata London 26

**Michel Semaan**

`PyData` · `PyData` · `2026` · `35 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=a2As90UbmcQ) · [Conference site](https://pydata.org/)

## Description

Large SQL codebases inevitably accumulate duplication, inconsistency, deep nesting, and subtle logic errors, making refactoring slow, risky, and often unrealistic to do by hand. This talk shows how Python metaprogramming can turn SQL itself into data that can be analyzed and transformed safely and automatically.

Instead of relying on fragile regex patterns or manual inspection, we use Python to parse queries into Abstract Syntax Trees (represented as nested dictionaries) using libraries such as sqloxide. Once SQL itself is encoded as data, entirely new workflows become possible.

The session walks through practical examples of treating SQL programmatically via tree operations in Python: computing subquery depth for linting, wrapping all denominators in NULLIF() with a simple AST rewrite, auto‑aliasing aggregate expressions, and generating dependency graphs of temporary tables used across pipelines, among others. Each example highlights how metaprogramming enables precise, automatable refactors that would be error‑prone or impossible through text manipulation alone. This talk is designed for analytics and data engineers who work with large SQL codebases.

SQL sits at the heart of most analytics and data engineering work, yet the way we maintain SQL rarely scales with the complexity of our pipelines. As codebases grow, SQL tends to accumulate structural debt: duplicated logic, subtle inconsistencies, deeply nested subqueries, and transformations that are difficult to apply reliably. Teams often end up relying on manual pattern‑matching, ad‑hoc scripts, or one‑off rewrites, approaches that are fragile and nearly impossible to generalise.

This talk presents a more systematic solution: treat queries as manipulable data through metaprogramming in Python. Instead of working with SQL as raw text, we use Python to parse queries into Abstract Syntax Trees (ASTs), unlocking the ability to inspect, analyze, and modify SQL with precision at scale.

After introducing the intuition behind SQL ASTs, we walk through what they look like in practice using Python libraries such as sqloxide. With queries represented as nested dictionaries, we can traverse them, detect patterns, and apply targeted modifications without breaking syntactic structure. The session demonstrates several real examples that highlight the power of this approach: evaluating subquery depth for complexity diagnostics, adding defensive transformations such as wrapping denominators in NULLIF(), generating consistent aliases for aggregation expressions, and extracting table references to infer dependency graphs across staging or temporary‑table‑heavy pipelines.

Rather than offering a single tool or framework, this talk focuses on the underlying metaprogramming techniques that empower engineers to build their own SQL analysis and refactoring utilities. Attendees will leave with a clear mental model of how SQL parsing works, how ASTs can be manipulated in Python, and how these patterns can be applied to enforce standards, build linters, or automate large‑scale refactors.

Background required:
- Intermediate familiarity with Python (nested dictionaries, basic tree algorithms).
- Intermediate familiarity with SQL (CTEs, subqueries, aggregates)
- No prior knowledge of compiler theory or ASTs is assumed

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
