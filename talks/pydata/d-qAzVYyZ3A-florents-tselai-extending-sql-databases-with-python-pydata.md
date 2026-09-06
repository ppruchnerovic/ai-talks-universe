---
id: d-qAzVYyZ3A
title: "Florents Tselai - Extending SQL Databases with Python - PyData Eindhoven 2025"
slug: florents-tselai-extending-sql-databases-with-python-pydata
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: ["Florents Tselai"]
channel: "PyData"
duration_min: 31
published_at: 2025-12-19T12:01:27Z
video_id: d-qAzVYyZ3A
url: https://www.youtube.com/watch?v=d-qAzVYyZ3A
youtube_url: https://www.youtube.com/watch?v=d-qAzVYyZ3A
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Data engineering & MLOps"]
transcript: false
---

# Florents Tselai - Extending SQL Databases with Python - PyData Eindhoven 2025

**Florents Tselai**

`PyData` · `PyData` · `2025` · `31 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=d-qAzVYyZ3A) · [Conference site](https://pydata.org/)

## Description

Florents Tselai - Extending SQL Databases with Python - PyData Eindhoven 2025

What if your database could run Python code inside SQL? In this talk, we’ll explore how to extend popular databases using Python, without needing to write a line of C.

We’ll cover three systems—SQLite, DuckDB, and PostgreSQL—and show how Python can be used in each to build custom SQL functions, accelerate data workflows, and prototype analytical logic. Each database offers a unique integration path:
- SQLite and DuckDB allow you to register Python functions directly into SQL via sqlite3.create_function, making it easy to inject business logic or custom transformations.
- PostgreSQL offers PL/Python, a full-featured procedural language for writing SQL functions in Python. We’ll also touch on advanced use cases, including embedding the Python interpreter directly into a PostgreSQL extension for deeper integration.

By the end of this talk, you’ll understand the capabilities, limitations, and gotchas of Python-powered extensions in each system—and how to choose the right tool depending on your use case, whether you’re analyzing data, building pipelines, or hacking on your own database.

Introduction (3 min)
• Who this talk is for: devs, data engineers, extension hackers
• Motivation: why embed Python in databases?
• Overview of the 3 systems (SQLite, DuckDB, PostgreSQL)

SQLite & DuckDB: Python Functions via sqlite3.create_function (7 min)
• How sqlite3.create_function() works in SQLite
• Example: creating a simple text-processing SQL function in Python
• Use cases: rapid prototyping, lightweight data pipelines

PostgreSQL with PL/Python (6 min)
• Enabling and using the PL/Python extension
• Writing SQL functions in Python
• Pros and limitations (e.g., sandboxing, permissions, virtualenvs)

Advanced: Embedding Python into PostgreSQL Extensions (7 min)
• Writing PostgreSQL extensions in C that embed Python
• Use cases: integrating ML models, custom procedural logic
• Short demo or diagram: C + Python working inside Postgres

Trade-offs and Comparison (3 min)
• Performance, deployment, complexity, ecosystem
• When to use which approach

Q&A (4 min)
• Invite questions and deeper discussion from the audience

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
