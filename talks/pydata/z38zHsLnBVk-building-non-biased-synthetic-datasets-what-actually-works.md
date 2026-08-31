---
id: z38zHsLnBVk
title: "Building Non-Biased Synthetic Datasets: What Actually Works (and What Fails)"
slug: building-non-biased-synthetic-datasets-what-actually-works
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Shiva Banasaz Nouri"]
channel: "PyData"
duration_min: 45
published_at: 2026-08-04T22:21:14Z
video_id: z38zHsLnBVk
youtube_url: https://www.youtube.com/watch?v=z38zHsLnBVk
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Building Non-Biased Synthetic Datasets: What Actually Works (and What Fails)

**Shiva Banasaz Nouri**

`PyData` · `PyData` · `2026` · `45 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=z38zHsLnBVk) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Senior Data Scientist Shiva Banasaz Nouri reveal the engineering pitfalls and proven best practices for building reproducible, bias-aware synthetic datasets that actually work in production.

Speakers:
Shiva Banasaz Nouri

Description:
Generating synthetic datasets for sensitive domains, such as legal text under GDPR, addresses the challenge of data scarcity and privacy restrictions. While large language models (LLMs) can generate data, free-form prompting often leads to label leakage, distribution collapse, and inconsistent JSON formatting. To mitigate these failures, a template-based generation approach is more effective than zero-shot or one-shot prompting.

The process involves a decoupled pipeline where an LLM generates sentence templates with placeholders (e.g., PER, LOC) rather than final text. Simultaneously, balanced entity lists are created to ensure demographic diversity and prevent bias. A Python script then randomly substitutes placeholders with entities from these lists, preserving statistical structures and ensuring reproducible, privacy-compliant annotations.

Key takeaways include the necessity of strict task definitions and the use of validation scripts to check for class imbalance and lexical heuristics. This method is particularly suited for classification, named entity recognition, and relation extraction, serving as a complement to real-world data to fill gaps in underrepresented groups.

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
