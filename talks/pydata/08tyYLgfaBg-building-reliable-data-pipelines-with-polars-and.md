---
id: 08tyYLgfaBg
title: "Building reliable data pipelines with polars and dataframely [PyCon DE & PyData 2026]"
slug: building-reliable-data-pipelines-with-polars-and
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Oliver Borchert", "Andreas Albert"]
channel: "PyData"
duration_min: 88
published_at: 2026-08-04T22:20:51Z
video_id: 08tyYLgfaBg
youtube_url: https://www.youtube.com/watch?v=08tyYLgfaBg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Building reliable data pipelines with polars and dataframely [PyCon DE & PyData 2026]

**Oliver Borchert, Andreas Albert**

`PyData` · `PyData` · `2026` · `88 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=08tyYLgfaBg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Oliver Borchert and Andreas Albert demonstrate how to build fast, bug-free data pipelines by combining the power of Polars with the validation capabilities of dataframely.

Speakers:
Oliver Borchert, Andreas Albert

Description:
Data pipelines often suffer from reliability issues due to inconsistent data types, poor memory management, and silent runtime failures. To address these problems, a combination of Polars and DataFramely is used to create efficient, maintainable, and validated software. Polars provides the high-performance processing backbone, written in Rust and utilizing the Apache Arrow memory layout. This layout employs a validity bit mask to handle nullable values efficiently and uses contiguous buffers to optimize cache performance.

The approach focuses on optimizing data types to reduce memory footprints and increase execution speed. Techniques include casting strings to categorical or enum types—which store data as unsigned integers while maintaining logical readability—and reducing float precision from 64-bit to 32-bit. To handle "dirty" data, the Polars expression API is used for complex transformations, such as using regular expressions to strip prefixes from IDs or splitting combined string columns into separate numeric fields.

A key performance feature is the use of LazyFrames, which defer execution until a collect call is made. This allows Polars to perform query optimization, specifically predicate pushdown, which moves filters earlier in the execution graph to reduce the volume of processed data. While eager execution is preferred for debugging, lazy execution provides significant speedups by eliminating unnecessary intermediate computations. To ensure long-term reliability, the pipeline is structured as a Python package rather than a notebook, using data classes to group related DataFrames and preventing in-place mutations to maintain data integrity.

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
