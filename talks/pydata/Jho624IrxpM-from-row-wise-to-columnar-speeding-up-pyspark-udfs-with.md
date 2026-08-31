---
id: Jho624IrxpM
title: "From Row-Wise to Columnar: Speeding Up PySpark UDFs with Arrow and Polars [PyCon DE & PyData 2026]"
slug: from-row-wise-to-columnar-speeding-up-pyspark-udfs-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Aimilios Tsouvelekakis"]
channel: null
duration_min: 37
published_at: 2026-08-04T22:20:44Z
video_id: Jho624IrxpM
youtube_url: https://www.youtube.com/watch?v=Jho624IrxpM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# From Row-Wise to Columnar: Speeding Up PySpark UDFs with Arrow and Polars [PyCon DE & PyData 2026]

**Aimilios Tsouvelekakis**

`PyData` · `PyData` · `2026` · `37 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Jho624IrxpM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Aimilios Tsouvelekakis demonstrate how to eliminate PySpark UDF bottlenecks by leveraging Arrow and Polars for high-performance, columnar data processing.

Speakers:
Aimilios Tsouvelekakis

Description:
PySpark User Defined Functions (UDFs) often suffer from performance bottlenecks due to row-wise execution and heavy serialization overhead between the Java Virtual Machine (JVM) and Python workers. Traditional Spark UDFs rely on Pickle for serialization, while Pandas UDFs utilize Apache Arrow to move data in batches. However, Pandas UDFs still incur memory overhead during the conversion between Arrow and Pandas formats and are limited by single-threaded execution.

To resolve these issues, Arrow UDFs and the mapInArrow method provide a zero-copy mechanism, allowing Python to read directly from memory buffers. Integrating Polars as a query engine further improves performance because Polars is written in Rust, supports multi-threaded execution, and shares the Arrow memory layout.

Benchmarks demonstrate that when computations are lightweight, such as string normalization, Arrow-based methods significantly outperform row-wise UDFs. For compute-heavy tasks like HTML cleaning or string similarity, the performance gap narrows unless the logic is vectorized. By replacing Python loops with native Rust kernels via Polars, execution speed increased by approximately 2.2 times for complex string similarity tasks. The key takeaway is that maximum efficiency is achieved by avoiding Python loops and utilizing columnar memory formats to minimize cache misses.

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
