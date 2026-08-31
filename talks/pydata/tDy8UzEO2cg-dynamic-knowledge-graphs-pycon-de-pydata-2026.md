---
id: tDy8UzEO2cg
title: "Dynamic Knowledge Graphs [PyCon DE & PyData 2026]"
slug: dynamic-knowledge-graphs-pycon-de-pydata-2026
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jakob Leander Müller"]
channel: null
duration_min: 31
published_at: 2026-08-04T22:21:47Z
video_id: tDy8UzEO2cg
youtube_url: https://www.youtube.com/watch?v=tDy8UzEO2cg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Dynamic Knowledge Graphs [PyCon DE & PyData 2026]

**Jakob Leander Müller**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=tDy8UzEO2cg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Jakob Leander Müller explain how to build a production-ready dynamic knowledge graph that overcomes the limitations of traditional RAG to handle real-time data evolution.

Speakers:
Jakob Leander Müller

Description:
Dynamic knowledge graphs address the fragmentation of information across disconnected sources, such as Jira tickets, Git repositories, and Swagger documentation. While vector stores offer fast similarity searches, they lack global connectivity and struggle with conflicting entries. Static graph-based RAG systems provide holistic views but are slow to update and often lose traceability to source documents.

The proposed approach utilizes a property graph implemented in FalkyDB to maintain a machine-readable integration pipeline. The schema consists of four node types: document nodes (anchors with content hashes), entity nodes (deduplicated via similarity matching), fact nodes (atomic nuggets of information), and relationship nodes. Document nodes use outgoing edges to support all other nodes, ensuring full traceability and enabling precise deletions of outdated information without collapsing the entire graph.

Insertion involves a multi-stage pipeline using LLMs for structured output via Pydantic classes. To maximize connectivity, the system merges new nodes with existing ones using a hierarchy of matching techniques: exact matches, Jaro-Winkler string similarity, and semantic embedding comparisons, all verified by an LLM. Inference is handled by AI agents that explore the graph using tools for embedding queries, keyword searches, and neighborhood exploration, or by generating Cypher queries directly.

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
