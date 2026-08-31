---
id: AHePPIVx31s
title: "Don’t call your LLM too often! How to build your dialog graph with confidence and sleep at night."
slug: dont-call-your-llm-too-often-how-to-build-your-dialog-graph
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Evgeniya Ovchinnikova", "Andrei Beliankou"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:20:41Z
video_id: AHePPIVx31s
youtube_url: https://www.youtube.com/watch?v=AHePPIVx31s
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Don’t call your LLM too often! How to build your dialog graph with confidence and sleep at night.

**Evgeniya Ovchinnikova, Andrei Beliankou**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=AHePPIVx31s) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Evgeniya Ovchinnikova and Andrei Beliankou reveal how to replace unpredictable LLM prompt chains with explicit dialog graphs and rigorous tracing to reduce costs and increase system reliability.

Speakers:
Evgeniya Ovchinnikova, Andrei Beliankou

Description:
Large Language Model (LLM) integration in corporate environments often leads to excessive operational costs and system inefficiencies due to redundant API calls and complex, looping dialogue graphs. These issues frequently emerge when systems evolve from simple prototypes into production environments without rigorous observability, resulting in "death paths" or infinite loops where competing evaluation checks—such as faithfulness versus hallucination rates—force the model into repetitive regeneration cycles.

To mitigate these inefficiencies, a structured approach to dialogue graph optimization is employed. This involves implementing observability tools like Langfuse, Arize Phoenix, or MLflow to trace individual spans, track request inputs and outputs, and analyze cost breakdowns. By analyzing these traces, developers can identify redundant paths and restructure the dialogue graph. Optimization techniques include implementing a routing layer to bypass the retrieval process for simple queries (e.g., greetings or out-of-scope questions), disambiguating queries before retrieval to avoid irrelevant document searches, and summarizing conversational history to reduce token consumption.

The effectiveness of these optimizations is measured by comparing a "redundant graph" against a "clean graph" using a golden dataset. Success is evaluated through a trade-off between routing quality—measured by the number of LLM and database calls and the depth of the graph—and outcome quality, which includes metrics for groundedness, usefulness, and correctness. This methodology allows for the reduction of latency and cost while maintaining the integrity of the final response, ensuring that LLM calls are only executed when necessary for the specific intent of the user query.

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
