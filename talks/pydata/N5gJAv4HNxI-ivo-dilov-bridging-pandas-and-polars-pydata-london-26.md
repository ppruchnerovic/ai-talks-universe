---
id: N5gJAv4HNxI
title: "Ivo Dilov - Bridging Pandas and Polars | Pydata London 26"
slug: ivo-dilov-bridging-pandas-and-polars-pydata-london-26
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Ivo Dilov"]
channel: null
duration_min: 34
published_at: 2026-06-15T15:52:27Z
video_id: N5gJAv4HNxI
youtube_url: https://www.youtube.com/watch?v=N5gJAv4HNxI
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Ivo Dilov - Bridging Pandas and Polars | Pydata London 26

**Ivo Dilov**

`PyData` · `PyData` · `2026` · `34 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=N5gJAv4HNxI) · [Conference site](https://pydata.org/)

## Description

Ivo Dilov - Bridging Pandas and Polars: The Hidden Costs of Dataframe Interoperability

The Python data ecosystem is migrating from NumPy-based arrays toward Apache Arrow. Polars is built entirely on Arrow, and Pandas is heading in the same direction. Yet differences in string encoding, missing values, schemas, and index metadata make interoperability between the two formats surprisingly costly and error-prone. This talk examines these challenges through a case study of how ArcticDB, the open-source client-side dataframe database, navigated this same migration.

As organisations adopt Polars alongside Pandas, a critical question emerges: how do you move data between the two without silent data loss, performance regressions, or broken round-trips? The answer is more complex than calling polars.from_pandas.

Pandas stores data in NumPy arrays by default, though as of 3.0 it uses Arrow for strings. Polars is built entirely on Apache Arrow's columnar format. For each area where these formats diverge, this talk will explain the problem and show how ArcticDB, a dataframe database that must serialize, store, and reconstruct both formats, solves it in practice:

Memory layout: How NumPy and Arrow represent the same logical data differently, and how a dataframe database can bridge the two
Strings: NumPy object arrays vs. Arrow's offset-based binary buffers -- why Arrow is dramatically more efficient and the cost of conversion
Missing values: NaN/NaT/None sentinels vs. Arrow's validity bitmask -- why a Pandas NaN behaves differently from a Polars null and what breaks during conversion
Schema differences: Different supported data types and different allowed column names -- e.g. Pandas allows mixed-type columns that Arrow cannot represent
Pandas-specific metadata that has no Arrow equivalent: Index and RangeIndex semantics, and MultiIndex which uses an entirely different memory layout with its own performance implications
Together, these issues make conversion between Pandas and Polars far from trivial. This is especially challenging for a dataframe database like ArcticDB, where petabytes of Pandas DataFrames are stored and users increasingly want to read them back as Arrow. The talk will include benchmarks comparing native format reads against conversion-based approaches, and practical takeaways for anyone migrating a codebase, building a library that supports both formats, or choosing a dataframe database. The talk will include benchmarks comparing native format reads against conversion-based approaches, and practical takeaways for anyone migrating a codebase, building a library that supports both formats, or choosing a dataframe database.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
