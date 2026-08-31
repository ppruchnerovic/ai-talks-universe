---
id: FsJM7TGwc-A
title: "Demystifying Parallel Programming in Python: from CPU to quantum processors, including GPU and TPU"
slug: demystifying-parallel-programming-in-python-from-cpu-to
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Gaël Pegliasco"]
channel: "PyData"
duration_min: 54
published_at: 2026-08-04T22:20:57Z
video_id: FsJM7TGwc-A
youtube_url: https://www.youtube.com/watch?v=FsJM7TGwc-A
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Demystifying Parallel Programming in Python: from CPU to quantum processors, including GPU and TPU

**Gaël Pegliasco**

`PyData` · `PyData` · `2026` · `54 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FsJM7TGwc-A) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Gaël Pegliasco demystify Python’s parallel programming ecosystem, from optimizing CPUs and GPUs to exploring the frontier of quantum computing.

Speakers:
Gaël Pegliasco

Description:
Parallel programming in Python requires an understanding of hardware architecture to optimize performance. Central Processing Units (CPUs) rely on clock frequency, physical cores, and cache memory. While hyper-threading allows a single core to switch between two logical threads to hide I/O latency, it can hinder heavy computational tasks. Furthermore, Non-Uniform Memory Access (NUMA) means that cores access certain memory nodes faster than others; aligning processes with their local memory nodes can reduce execution time.

For massively parallel tasks, Graphical Processing Units (GPUs) offer thousands of cores that execute the same instruction across large datasets, making them superior to CPUs for matrix operations. Tensor Processing Units (TPUs) further optimize this by specializing in tensor operations with lower power consumption than GPUs, while Neural Processing Units (NPUs) are designed specifically for low-power machine learning inference.

Python offers several libraries to leverage this hardware. PyPy provides a just-in-time compiler that can increase speed by 100x for simple loops. Numba uses decorators to compile Python functions into machine code for CPUs or GPUs. For distributed computing and large-scale data, Dask parallelizes NumPy and Pandas operations by splitting data into chunks. Optimizing these chunks to fit within the CPU's L1 or L2 cache—rather than relying on slower external RAM—can result in performance gains exceeding the number of available physical cores. Other specialized tools include CuPy for GPU-accelerated NumPy operations and Ray for distributing machine learning models across clusters.

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
