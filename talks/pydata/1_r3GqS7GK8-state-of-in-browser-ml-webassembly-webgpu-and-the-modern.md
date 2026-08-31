---
id: 1_r3GqS7GK8
title: "State of In-Browser ML: WebAssembly, WebGPU, and the Modern Stack [PyCon DE & PyData 2026]"
slug: state-of-in-browser-ml-webassembly-webgpu-and-the-modern
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Oleh Kostromin", "Iryna Kondrashchenko"]
channel: "PyData"
duration_min: 28
published_at: 2026-08-04T22:20:34Z
video_id: 1_r3GqS7GK8
youtube_url: https://www.youtube.com/watch?v=1_r3GqS7GK8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# State of In-Browser ML: WebAssembly, WebGPU, and the Modern Stack [PyCon DE & PyData 2026]

**Oleh Kostromin, Iryna Kondrashchenko**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=1_r3GqS7GK8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Oleh Kostromin and Iryna Kondrashchenko explore the modern in-browser ML stack to discover how WebAssembly and WebGPU are enabling secure, serverless, and scalable on-device inference.

Speakers:
Oleh Kostromin, Iryna Kondrashchenko

Description:
In-browser machine learning leverages WebAssembly (Wasm) and WebGPU to execute code and models on the client side, reducing server costs and improving user privacy. WebAssembly provides a binary instruction format that allows near-native execution speeds in all major browsers. Because Wasm lacks a standard library for system-level tasks, toolchains like Emscripten are used to compile C/C++ code into Wasm, providing necessary runtime layers and virtual file systems.

Python integration in the browser is primarily achieved through Pyodide, a port of CPython to WebAssembly. Pyodide allows the installation of pure Python packages via micropip and provides pre-compiled builds for libraries with native extensions, such as NumPy and Pandas, through the Pyodide package index. For developers seeking higher-level abstractions, PyScript enables Python logic to be embedded directly in HTML. Alternatively, MicroPython can be used for faster startup times and smaller bundle sizes (under 300 KB), though it supports fewer features and packages than CPython.

Model inference is handled separately from the Python interpreter to avoid overhead and enable GPU acceleration. WebGPU allows for general-purpose compute, moving beyond the graphical limitations of WebGL. The ONNX Runtime Web serves as a universal adapter, executing models converted to the ONNX format on both CPUs and GPUs. For large language models (LLMs), WebLLM provides GPU-accelerated inference, while vLlama enables the execution of GGUF-format models on the CPU via Llama.cpp. While Wasm is currently limited to 32-bit addressing (capping RAM at 4 GB), these tools collectively enable the deployment of models up to 3 billion parameters directly in the browser.

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
