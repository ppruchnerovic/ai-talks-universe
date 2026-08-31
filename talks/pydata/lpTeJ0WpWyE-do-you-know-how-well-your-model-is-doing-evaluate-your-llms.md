---
id: lpTeJ0WpWyE
title: "Do you know how well your model is doing? Evaluate your LLMs [PyCon DE & PyData 2026]"
slug: do-you-know-how-well-your-model-is-doing-evaluate-your-llms
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Cheuk Ting Ho"]
channel: "PyData"
duration_min: 34
published_at: 2026-08-04T22:21:34Z
video_id: lpTeJ0WpWyE
youtube_url: https://www.youtube.com/watch?v=lpTeJ0WpWyE
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Do you know how well your model is doing? Evaluate your LLMs [PyCon DE & PyData 2026]

**Cheuk Ting Ho**

`PyData` · `PyData` · `2026` · `34 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lpTeJ0WpWyE) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Cheuk Ting Ho demonstrate how to rigorously evaluate, benchmark, and fine-tune your LLMs using Lighteval to ensure your models deliver objective and high-quality results.

Speakers:
Cheuk Ting Ho

Description:
Evaluating Large Language Models (LLMs) is critical for benchmarking performance, ensuring safety through railguarding, and verifying that fine-tuning actually improves model capabilities rather than degrading them. This process mirrors software testing, where systematic evaluation prevents the deployment of buggy or toxic outputs and ensures the model meets specific hardware performance and response-time requirements.

The technical approach centers on the Hugging Face ecosystem, specifically using the Transformers library for model training and LightEval for benchmarking. To demonstrate these tools, a small GPT-2 model is fine-tuned on math logic data to improve its reasoning capabilities. The workflow involves loading a GPT-2 tokenizer to process question-and-answer pairs and using the Transformers training pipeline to create model checkpoints.

LightEval provides a framework for measuring model quality through built-in tasks and metrics. Available task categories include knowledge and reasoning, question answering, chat and instruction following, coding, and multilingual support. Evaluation metrics range from simple multiple-choice accuracy and log-likelihood to advanced methods such as using a second LLM as a judge to score the primary model's responses.

For specialized business use cases, the framework supports custom tasks and custom metrics. This allows developers to reserve a specific test set from their training data and define precise scoring logic—such as a binary correct/incorrect point system—to measure success against real-world data. While LightEval is optimized for open-source models via the Hugging Face Hub, it can technically evaluate closed-source models by comparing model outputs against defined targets, provided the user manages the specific API prompting requirements.

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
