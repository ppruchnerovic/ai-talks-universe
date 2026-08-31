---
id: 6yQmEvqMDCQ
title: "Metashade: Compilerless Immediate-Mode Shader Generation in Pure Python [PyCon DE & PyData 2026]"
slug: metashade-compilerless-immediate-mode-shader-generation-in
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Pavlo Penenko"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:20:28Z
video_id: 6yQmEvqMDCQ
youtube_url: https://www.youtube.com/watch?v=6yQmEvqMDCQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Metashade: Compilerless Immediate-Mode Shader Generation in Pure Python [PyCon DE & PyData 2026]

**Pavlo Penenko**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=6yQmEvqMDCQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Pavlo Penenko demonstrate how to leverage Python metaprogramming to build a compilerless GPU shader generator using pure Python.

Speakers:
Pavlo Penenko

Description:
Metashade addresses the challenges of shader programming, specifically portability across different rendering APIs, the permutation explosion in real-time shading, and the lack of high-level abstractions and modularity in C-like shading languages. While existing solutions like Warp or Taichi use introspection to capture Python's Abstract Syntax Tree (AST) and compile it via C++ backends, Metashade avoids the compiler approach entirely.

The system utilizes a tracing mechanism and immediate-mode code generation. Rather than parsing the AST, Metashade emits target code eagerly as Python code executes. This allows for the interleaving of arbitrary Python logic with shader generation, enabling powerful metaprogramming. A central polymorphic generator object manages the semantic model of the shader, tracking scopes and local variables to ensure semantic correctness without relying on simple string concatenation.

To emulate C-like semantics within Python, Metashade employs specific architectural patterns. It captures symbols by treating meta-variables as members of the generator, which enforces static typing and value-based assignment. Operator overloading is used to implement an expression builder pattern, allowing the system to enforce stricter type safety than the target language—such as prohibiting the addition of a color and a point. C-like scopes are emulated using Python context managers.

Metashade supports multiple targets, including HLSL and GLSL, and integrates with the MaterialX standard for physically based rendering (PBR). By moving design-time decisions to Python, it replaces complex C preprocessor macros with readable, maintainable Python code. This approach improves debuggability, as semantic errors trigger Python exceptions that can be analyzed with standard Python debuggers.

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
