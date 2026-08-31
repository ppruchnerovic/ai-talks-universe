---
id: nlTn6-kyyFI
title: "Small Language Models for Tool Calling Are Better Than You Think [PyCon DE & PyData 2026]"
slug: small-language-models-for-tool-calling-are-better-than-you
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Gabi Kadlecova"]
channel: "PyData"
duration_min: 29
published_at: 2026-08-04T22:20:26Z
video_id: nlTn6-kyyFI
youtube_url: https://www.youtube.com/watch?v=nlTn6-kyyFI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Small Language Models for Tool Calling Are Better Than You Think [PyCon DE & PyData 2026]

**Gabi Kadlecova**

`PyData` · `PyData` · `2026` · `29 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=nlTn6-kyyFI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Gabi Kadlecova reveal how to leverage knowledge distillation to build small language models that outperform LLMs in specialized tool-calling tasks.

Speakers:
Gabi Kadlecova

Description:
Small Language Models (SLMs), typically defined as models with under 4 billion parameters, offer significant advantages over Large Language Models (LLMs) regarding latency, energy costs, and data privacy. Because SLMs can be deployed locally, they allow organizations to freeze model versions to ensure pipeline stability and keep sensitive data off external servers. While SLMs excel at classification, routing, and structured information extraction, they often struggle with complex tool calling—the process of selecting a function and providing correct arguments based on a user request—due to a tendency to omit arguments or select incorrect functions.

To improve tool calling performance, a knowledge distillation approach is used where a teacher LLM generates synthetic training data for a student SLM. The pipeline involves providing the teacher model with task descriptions, constraints, and a small set of real examples to generate a synthetic dataset of 1,000 to 10,000 examples. To ensure data quality, the pipeline filters out malformed JSON, removes hallucinated tools, and uses ROUGE comparisons to eliminate duplicate examples. The student model is then fine-tuned using supervised fine-tuning with Low-Rank Adaptation (LoRA) over a few epochs.

Experimental results using the Qwen 0.6B model demonstrate that this method can move a model from under 50% accuracy to near-perfect accuracy on simple tool-calling tasks. Key challenges in this process include ensuring full coverage of all available functions and parameters, varying user phrasing to increase robustness, and managing the complexity of multi-turn conversations. In multi-turn scenarios, the model must maintain accuracy across long sequences, as a single error in a chain of five calls can render the entire workflow incorrect.

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
