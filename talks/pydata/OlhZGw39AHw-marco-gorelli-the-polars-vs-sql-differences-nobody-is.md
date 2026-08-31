---
id: OlhZGw39AHw
title: "Marco Gorelli - The Polars vs SQL differences nobody is talking about | Pydata London 26"
slug: marco-gorelli-the-polars-vs-sql-differences-nobody-is
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Marco Gorelli"]
channel: "PyData"
duration_min: 20
published_at: 2026-06-15T15:52:36Z
video_id: OlhZGw39AHw
youtube_url: https://www.youtube.com/watch?v=OlhZGw39AHw
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Marco Gorelli - The Polars vs SQL differences nobody is talking about | Pydata London 26

**Marco Gorelli**

`PyData` · `PyData` · `2026` · `20 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=OlhZGw39AHw) · [Conference site](https://pydata.org/)

## Description

Polars is a dataframe library which has taken the world by storm over the last 4-5 years. Because people love benchmarks, people often compare it with SQL-like engines such as DuckDB, PySpark, Daft, and others. But what if, instead of comparing performance, we compared semantics?

This talk will make no mention whatsoever of performance differences. Instead, it will focus entirely on the semantic differences - which don't get nearly enough attention - of Polars vs SQL. Attendees will leave with a heightened appreciation for the differences between the Polars and SQL models, and an understanding of the consequences this has on their code.

Polars is a dataframe library that started gaining significant traction in the data science community around 2022/2023. It is now generally regarded as a safer and more performant alternative to its extremely popular counterpart pandas. As such, it has attracted several performance comparisons with SQL-like engines such as DuckDB, PySpark, Daft, and more. What's typically missing from these comparisons is an explanation of the semantic differences.

For example:
- Why does Polars let me do pl.col('price') - pl.col('price').mean(), but SQL doesn't?
- Why does Polars let me filter using window functions, and how can I get SQL to?
- Are there operations that are more dangerous in Polars than in SQL?
- How do they differ when working with time zones?
- Why did SQL reorder my rows when Polars didn't?

Outline of the talk:
- Motivation: why care about Polars or about SQL?
- Relational model background, row order
- Polars model, how it differs from the relational model, and what this means for you
- Abstracting the Polars and SQL differences away in Narwhals, and advice for non-Narwhals users
- Q&A

This is a technical but accessible talk aimed at data practitioners. Data engineers, data scientists, data analysts, and anyone else working with data will leave the talk with stronger theoretical foundations regarding the Polars and SQL data models. Most importantly, they will learn what this means for them, and what they can do about it.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
