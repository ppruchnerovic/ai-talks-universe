---
id: dKZxUcuOb8A
title: "PyTorch and CPU-GPU Synchronizations [PyCon DE & PyData 2026]"
slug: pytorch-and-cpu-gpu-synchronizations-pycon-de-pydata-2026
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Tomas Ruiz"]
channel: null
duration_min: 27
published_at: 2026-08-04T22:21:37Z
video_id: dKZxUcuOb8A
youtube_url: https://www.youtube.com/watch?v=dKZxUcuOb8A
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# PyTorch and CPU-GPU Synchronizations [PyCon DE & PyData 2026]

**Tomas Ruiz**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=dKZxUcuOb8A) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Tomas Ruiz reveal how to identify and eliminate hidden CPU-GPU synchronizations in PyTorch to unlock maximum hardware performance and throughput.

Speakers:
Tomas Ruiz

Description:
PyTorch executes GPU operations asynchronously, allowing the CPU to schedule tasks and run ahead of the GPU. Performance degradation occurs during CPU-GPU synchronization, which happens when the CPU must block and wait for data to return from the GPU to make a decision or allocate memory. This creates "bubbles" of inactivity on both the CPU and GPU, reducing overall hardware utilization.

Common triggers for synchronization include calling .item(), .cpu(), or printing tensors, as well as using GPU tensors within conditional if-else branching. More subtle synchronizations arise from operations that result in dynamic shapes, where the output size depends on the tensor data. Examples include boolean indexing, slicing with a GPU-resident integer, torch.non_zero(), and torch.unique(). Because the CPU manages memory allocation, it must synchronize to determine the output shape before the GPU can proceed.

To mitigate these issues, developers can reduce the frequency of synchronization—such as printing loss every 100 iterations instead of every one—or use padding to maintain static shapes. Some PyTorch APIs, such as torch.repeat_interleave(), provide optional parameters to specify the output size, bypassing the need for synchronization.

Profiling tools like NVIDIA Nsight Systems can visualize these delays as CUDA stream synchronize calls. For automated detection, PyTorch offers an experimental debug mode via torch.cuda.set_synchronize_debug_mode(), which can be set to warning or error. This allows for the creation of unit tests using decorators that fail if a function triggers a GPU synchronization, ensuring production code remains efficient.

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
