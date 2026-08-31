---
id: gy4_2CwQpPQ
title: "Rediscovering single-node processing: When does it make sense to move from Spark to Polars?"
slug: rediscovering-single-node-processing-when-does-it-make
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jonas Böer"]
channel: null
duration_min: 31
published_at: 2026-08-04T22:21:00Z
video_id: gy4_2CwQpPQ
youtube_url: https://www.youtube.com/watch?v=gy4_2CwQpPQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Rediscovering single-node processing: When does it make sense to move from Spark to Polars?

**Jonas Böer**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=gy4_2CwQpPQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Jonas Böer challenge the Spark status quo as he explores when switching to Polars for single-node processing can streamline your data pipeline and reduce costs.

Speakers:
Jonas Böer

Description:
Apache Spark and Polars represent two different philosophies of data processing: horizontal scaling via distributed clusters and vertical scaling via single-node optimization. Spark, written in Scala and running on the JVM, is designed for terabyte-scale datasets across multiple nodes. It utilizes a lazy execution model and a client-server architecture, making it ideal for massive parallelization but introducing overhead through cluster startup times and complex JVM stack traces during debugging.

Polars, written in Rust, optimizes for single-node performance by utilizing all available CPU cores and memory on a single machine. It supports both eager and lazy APIs and employs a columnar memory layout. While Spark remains faster for simple row-wise parallel processing, Polars often outperforms Spark in complex operations like joins. Polars also offers a more modern, hierarchical API and faster development cycles because it eliminates the need for cluster management and simplifies unit testing.

The decision to migrate from Spark to Polars depends on data volume and infrastructure. Polars is most effective when the data per processing step fits within a single machine's memory (typically in the gigabyte range) and when there are high interdependencies between rows that would otherwise cause expensive shuffles in a distributed Spark environment. While Spark provides superior integration with data warehouses and comprehensive monitoring via the Spark UI, Polars reduces operational complexity by running within a simple container. For users currently employing Pandas, Polars serves as a high-performance replacement with a more consistent API.

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
