---
id: DonT6K6eiOI
title: "Heat: scaling the Python scientific stack to HPC systems [PyCon DE & PyData 2026]"
slug: heat-scaling-the-python-scientific-stack-to-hpc-systems
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Claudia Comito", "Thomas Saupe"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:21:05Z
video_id: DonT6K6eiOI
youtube_url: https://www.youtube.com/watch?v=DonT6K6eiOI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Heat: scaling the Python scientific stack to HPC systems [PyCon DE & PyData 2026]

**Claudia Comito, Thomas Saupe**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=DonT6K6eiOI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Claudia Comito and Thomas Saupe explain how Heat breaks the "memory wall" by scaling the Python scientific stack across multi-node, multi-GPU HPC systems.

Speakers:
Claudia Comito, Thomas Saupe

Description:
HEAT is an open-source Python library designed to scale scientific data analysis from local workstations to high-performance computing (HPC) systems. It addresses the memory and compute limitations of NumPy, which is restricted to shared-memory parallelization on CPUs. By mirroring the NumPy API, HEAT allows users to develop code on a laptop and deploy it on large-scale clusters, such as the Jupyter system with 6,000 compute nodes, without significant code modification.

The library introduces the DND (distributed n-dimensional) array, which distributes data along a single axis across multiple MPI ranks. Under the hood, HEAT leverages PyTorch for local tensor operations and device acceleration, supporting CPUs and GPUs (including NVIDIA and Apple MPS), while using MPI4Py for inter-node communication. A key technical advantage of HEAT is its implementation of complex linear algebra functions that are difficult to parallelize, such as QR factorization, distributed Singular Value Decomposition (SVD), and Dynamic Mode Decomposition (DMD).

Performance benchmarks demonstrate that HEAT provides significant speedups over serial NumPy and scikit-learn baselines, particularly for large matrices where GPU acceleration is utilized. In weak scaling tests, HEAT maintains a flat memory footprint per compute node, whereas alternatives like Dask show increasing memory consumption as the number of nodes grows. This memory efficiency enables the processing of datasets that exceed the memory capacity of a single GPU or node. The library effectively combines shared-memory parallelization via PyTorch with distributed-memory parallelization via MPI to maximize HPC resource utilization.

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
