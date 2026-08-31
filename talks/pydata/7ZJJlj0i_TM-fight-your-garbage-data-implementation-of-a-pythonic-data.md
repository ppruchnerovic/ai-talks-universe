---
id: 7ZJJlj0i_TM
title: "Fight your garbage data: implementation of a pythonic data quality monitoring framework in PySpark"
slug: fight-your-garbage-data-implementation-of-a-pythonic-data
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Rostislaw Krassow", "Joshua Finger"]
channel: null
duration_min: 44
published_at: 2026-08-04T22:21:28Z
video_id: 7ZJJlj0i_TM
youtube_url: https://www.youtube.com/watch?v=7ZJJlj0i_TM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Fight your garbage data: implementation of a pythonic data quality monitoring framework in PySpark

**Rostislaw Krassow, Joshua Finger**

`PyData` · `PyData` · `2026` · `44 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=7ZJJlj0i_TM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Rostislaw Krassow and Joshua Finger demonstrate how to combat "garbage in, garbage out" by implementing a scalable, Pythonic data quality monitoring framework using PySpark and DQX.

Speakers:
Rostislaw Krassow, Joshua Finger

Description:
IoT data quality monitoring in PySpark addresses the challenge of "garbage in, garbage out," particularly when dealing with diverse software versions and unstable connectivity from thousands of global devices. The primary problem is that data quality is often a moving target; hardware manufacturers transitioning to digital services must manage legacy devices and varying data schemas, making it impossible to ensure perfect data at the point of ingestion.

The implemented approach utilizes a reactive monitoring strategy, detecting deviations post-transformation rather than blocking data during ingestion. After evaluating frameworks like Great Expectations and Soda, DQX was selected for its lightweight nature, open-source license for Databricks, and support for a YAML-based domain-specific language. This allows non-Python experts to define rules for completeness, plausibility, uniqueness, and consistency. The framework supports both built-in checks and custom Python functions, such as a monotonically increasing check for operation hour counters using PySpark lag functions. To handle scale, the system leverages the Databricks Change Data Feed to process daily increments of terabyte-scale tables.

Key takeaways include the technical benefit of using LLMs to generate initial YAML check proposals and the organizational necessity of shifting data ownership to the producers. By aggregating DQX error arrays into interpretable Power BI dashboards, the team created a feedback loop that identifies software bugs in specific device versions. This process transforms abstract "data quality" into concrete metrics, enabling data engineers to provide evidence-based bug reports to embedded software teams for permanent resolution.

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
