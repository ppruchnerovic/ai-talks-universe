---
id: zgIj2oCFF1M
title: "Array-Oriented Programming in Python: Libraries, Techniques, and Trade-offs [PyCon DE & PyData 2026]"
slug: array-oriented-programming-in-python-libraries-techniques
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Iason Krommydas"]
channel: null
duration_min: 67
published_at: 2026-08-04T22:20:21Z
video_id: zgIj2oCFF1M
youtube_url: https://www.youtube.com/watch?v=zgIj2oCFF1M
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Array-Oriented Programming in Python: Libraries, Techniques, and Trade-offs [PyCon DE & PyData 2026]

**Iason Krommydas**

`PyData` · `PyData` · `2026` · `67 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zgIj2oCFF1M) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Iason Krommydas break down the modern Python array ecosystem to discover how to choose between NumPy, JAX, Numba, and Awkward Array for maximum performance in your scientific computing workflows.

Speakers:
Iason Krommydas

Description:
Array-oriented programming in Python shifts the focus from individual element manipulation to operations on entire data structures. This paradigm addresses the performance bottlenecks of the Python interpreter by offloading heavy computations to pre-compiled C or C++ libraries. While imperative programming relies on explicit loops and functional programming uses mapping functions, array-oriented programming utilizes implicit loops through vectorization, which aligns with hardware-level SIMD (Single Instruction, Multiple Data) operations common in CPUs and GPUs.

Key tools for this approach include NumPy, JAX, and Numba. NumPy provides the foundational array object and vectorized operations, though it often creates costly intermediate arrays in memory for complex expressions. To mitigate this, NumExpr fuses operations to reduce memory overhead, while Numba uses LLVM to compile Python bytecode into machine code, allowing imperative loops to run at C-like speeds. JAX further optimizes this process by tracing functions to create an intermediate representation (HLO), which is then compiled via XLA (Accelerated Linear Algebra) for efficient execution on CPUs, GPUs, or TPUs.

A primary trade-off in array-oriented programming is the handling of conditional logic. Standard Python if-statements cannot be applied to arrays because the truth value of multiple elements is ambiguous. This is resolved using boolean masking—applying a filter of true/false values to update only specific elements. In many cases, it is computationally faster to perform redundant calculations on all elements than to manage the memory overhead of masking. For datasets exceeding available RAM, libraries like Dask extend these capabilities by implementing chunking and parallelized computation graphs.

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
