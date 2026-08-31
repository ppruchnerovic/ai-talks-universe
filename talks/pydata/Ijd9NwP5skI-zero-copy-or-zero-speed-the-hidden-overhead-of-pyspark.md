---
id: Ijd9NwP5skI
title: "Zero-Copy or Zero-Speed? The hidden overhead of PySpark, Arrow & SynapseML for inference"
slug: zero-copy-or-zero-speed-the-hidden-overhead-of-pyspark
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Petar Ilijevski"]
channel: null
duration_min: 28
published_at: 2026-08-04T22:21:44Z
video_id: Ijd9NwP5skI
youtube_url: https://www.youtube.com/watch?v=Ijd9NwP5skI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Zero-Copy or Zero-Speed? The hidden overhead of PySpark, Arrow & SynapseML for inference

**Petar Ilijevski**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Ijd9NwP5skI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Petar Ilijevski dismantle the "zero-copy" myth to reveal how to eliminate serialization bottlenecks and optimize distributed inference performance in PySpark.

Speakers:
Petar Ilijevski

Description:
Scaling machine learning inference to 6 billion daily predictions using an Ensemble LightGBM model requires overcoming the performance bottleneck created by the Python-JVM boundary in PySpark. In standard PySpark User Defined Functions (UDFs), data is serialized via pickle and sent row-by-row through sockets, resulting in hundreds of millions of boundary crossings and underutilizing the C++ engine of LightGBM. While Apache Arrow aims to provide zero-copy data sharing, in PySpark it still involves CPU-intensive format conversion from Tungsten rows and socket-based data movement.

To optimize throughput, four execution methods were evaluated. Standard UDFs served as the baseline. Pandas UDFs improved performance by vectorizing batches, reducing boundary crossings from 400 million to approximately 4,000. Mapping Pandas further increased speed by introducing a stateful iterator, allowing the model to load once per partition rather than once per batch. SynapseML provided the highest throughput by executing the model natively on the JVM, eliminating the Python boundary, the Global Interpreter Lock (GIL), and serialization overhead entirely.

Benchmarks on a 20-node cluster demonstrated a 9x total performance improvement moving from standard UDFs to SynapseML, reducing total runtime from seven hours to four minutes. For maximum throughput, SynapseML is the most efficient choice, though it lacks the flexibility for complex custom Python transformations. Mapping Pandas is recommended for workloads requiring custom logic, as it offers a 4x speedup over the baseline. Additionally, tuning the spark.sql.execution.arrow.maxRecordsPerBatch parameter to a "Goldilocks zone" of 50,000 to 200,000 records prevents both networking overhead and out-of-memory errors.

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
