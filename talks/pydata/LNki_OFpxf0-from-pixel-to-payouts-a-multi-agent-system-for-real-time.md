---
id: LNki_OFpxf0
title: "From Pixel to Payouts: A Multi-Agent System for Real-Time Insurance Claims Processing"
slug: from-pixel-to-payouts-a-multi-agent-system-for-real-time
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Claudio Giorgio Giancaterino"]
channel: null
duration_min: 30
published_at: 2026-08-04T22:20:22Z
video_id: LNki_OFpxf0
youtube_url: https://www.youtube.com/watch?v=LNki_OFpxf0
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# From Pixel to Payouts: A Multi-Agent System for Real-Time Insurance Claims Processing

**Claudio Giorgio Giancaterino**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=LNki_OFpxf0) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Claudio Giorgio Giancaterino demonstrate how a sophisticated multi-agent AI system can disrupt the insurance industry by transforming raw damage photos into real-time, auditable claim payouts.

Speakers:
Claudio Giorgio Giancaterino

Description:
Insurance claims processing for vehicle damage is traditionally a slow manual process, often taking weeks or months due to the sequential nature of investigation, cost evaluation, and approval. Traditional deep learning approaches using Convolutional Neural Networks (CNNs) for this task are often limited by a lack of labeled datasets, a lack of adaptability to new pricing, and a "black box" nature that hinders explainability.

To address these inefficiencies, a multi-agent system was developed using a Python-based framework to maintain governance and stability without the constraints of external orchestration libraries. The system utilizes a ReAct (Reason, Action, Observation) loop, allowing agents to reason through tasks, execute functions, and observe results. The architecture consists of an orchestrator agent that manages a sequential pipeline of specialized agents: a vision agent powered by the OpenAI Vision API to identify damaged parts and classify severity (minor, moderate, or severe), and two cost agents using the Perplexity API to provide comparative repair estimates from web-based market data. A final shop finder agent identifies local repair facilities based on the user's location.

The system is deployed on Hugging Face Spaces using Gradio. In testing, the pipeline processes a claim in approximately 50 seconds. Key advantages over linear prompt flows or CNNs include modularity, the ability to perform end-to-end assessments (from image analysis to shop location), and transparency provided by the ReAct trace. While cost estimations remain approximations based on web searches rather than static databases, the system demonstrates how multi-agent collaboration can automate repetitive data review and accelerate the insurance payout lifecycle.

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
