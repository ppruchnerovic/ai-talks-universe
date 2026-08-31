---
id: FNyheMv6Vt4
title: "When LLMs Are Too Big: Building Cost-Efficient High-Throughput ML Systems for E-Commerce Cataloging"
slug: when-llms-are-too-big-building-cost-efficient-high
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Tobias Senst", "Bastian Wandt"]
channel: null
duration_min: 47
published_at: 2026-08-04T22:20:46Z
video_id: FNyheMv6Vt4
youtube_url: https://www.youtube.com/watch?v=FNyheMv6Vt4
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# When LLMs Are Too Big: Building Cost-Efficient High-Throughput ML Systems for E-Commerce Cataloging

**Tobias Senst, Bastian Wandt**

`PyData` · `PyData` · `2026` · `47 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FNyheMv6Vt4) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Tobias Senst and Bastian Wandt reveal how to scale LLM intelligence for billion-scale e-commerce cataloging using knowledge distillation and high-throughput MLOps.

Speakers:
Tobias Senst, Bastian Wandt

Description:
E-commerce cataloging requires classifying millions of product offers into thousands of categories across multiple languages in real time. High-throughput systems must process peak loads of approximately 80,000 offers per second. While traditional Support Vector Machines (SVM) provide high cost-efficiency and low latency, they lack the contextual understanding and adaptability of transformer-based models. The primary challenge in transitioning to deep learning is balancing classification accuracy with strict operational cost constraints and inference speed.

The technical approach centers on a student-teacher knowledge distillation framework. A large, high-performance teacher model, such as E5-base, is trained using cross-entropy loss to create a sophisticated embedding space. A smaller student model, MiniLM-L12, is then trained to mimic the teacher's embeddings using an L2 loss in addition to the standard cross-entropy loss. This allows the student model to maintain the inference speed of a small architecture while achieving the accuracy of a much larger one. To optimize performance, the system employs bfloat16 quantization and a curated data sampling strategy that transforms long-tail distributions into uniform distributions for training, while matching real-world distributions for evaluation.

Deployment is optimized using AWS Inferentia chips, which offer a better balance of throughput and cost than standard GPUs for small models. The pipeline utilizes a specialized compilation process where models are JIT-compiled for the Neuron runtime with a batch size of one to minimize latency. This architecture resulted in a 30% increase in classification performance over the legacy SVM system with only an 18% increase in operational costs.

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
