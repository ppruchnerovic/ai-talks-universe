---
id: XvsrRUqyTpg
title: "SQL is Dead, Long Live SQL: Engineering reliable analytics agent from scratch"
slug: sql-is-dead-long-live-sql-engineering-reliable-analytics
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Mehdi Ouazza", "Dumky de Wilde"]
channel: "PyData"
duration_min: 87
published_at: 2026-08-04T22:20:19Z
video_id: XvsrRUqyTpg
youtube_url: https://www.youtube.com/watch?v=XvsrRUqyTpg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# SQL is Dead, Long Live SQL: Engineering reliable analytics agent from scratch

**Mehdi Ouazza, Dumky de Wilde**

`PyData` · `PyData` · `2026` · `87 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XvsrRUqyTpg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Mehdi Ouazza and Dumky de Wilde explore the limits of Text-to-SQL and demonstrate how to engineer a reliable analytics agent from scratch using DuckDB.

Speakers:
Mehdi Ouazza, Dumky de Wilde

Description:
Reliable analytics agents can be engineered by combining an in-process analytical database with a structured agentic loop and semantic context. Using DuckDB as the core engine allows agents to execute SQL queries locally in memory, providing the fast feedback loops necessary for Large Language Models (LLMs) to iterate on query generation without the latency of client-server architectures.

The basic approach involves a "while" loop where an LLM generates a SQL statement, executes it via a Python tool, and analyzes the result. To move beyond simple query generation and handle real-world data ambiguity, semantic context is integrated through two primary methods: skill files (Markdown documents containing business logic and KPI definitions used as system prompts) and database comments (metadata attached directly to table columns). These additions reduce the number of tool calls required for a correct answer and enable smaller, more efficient models to perform as well as larger ones.

For deterministic results on critical metrics, the architecture incorporates specific tools using Pydantic AI. While the agent remains flexible for exploratory questions, deterministic tools ensure that complex KPIs are calculated using a fixed, verified logic. To scale and distribute these capabilities, the Model Context Protocol (MCP) is used to decouple the agent's logic from the tool implementation. By hosting tools on an MCP server, agents can dynamically discover and utilize a standardized set of functions, allowing for a clean separation of concerns between the agent's identity and the organization's analytical tools.

⭐️ About PyCon DE:
PyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for collaboration, knowledge sharing, and innovation.

The PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.

PyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.

•  Newsletter: https://2027.pycon.de/newsletter/
•  LinkedIn: https://www.linkedin.com/company/pyconde
•  X: https://www.x.com/pyconde

Links:
• Conference website: http://pycon.de
• Other sessions: https://2026.pycon.de/talks/

The conference was organized by
• Python Softwareverband e.V.: http://pysv.org
• Pioneers Hub gemeinnützige GmbH: http://pioneershub.org
in collaboration with NumFOCUS Inc.: http://numfocus.org

If you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.
Share this video with your network to spread the knowledge!

Hashtags:

Acknowledgements:
Special thanks to all the volunteers and sponsors who made this event possible.

About:
Python Softwareverband e.V.:
PySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.

Pioneers Hub gemeinnützige GmbH:
is a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.

NumFOCUS Inc.
supports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable development and collaboration.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.
