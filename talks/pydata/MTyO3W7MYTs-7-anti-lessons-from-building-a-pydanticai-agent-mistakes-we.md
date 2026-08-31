---
id: MTyO3W7MYTs
title: "7 Anti-Lessons from Building a PydanticAI Agent: Mistakes We Made So You Don't Have To"
slug: 7-anti-lessons-from-building-a-pydanticai-agent-mistakes-we
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Joshua Görner"]
channel: null
duration_min: 45
published_at: 2026-08-04T22:21:41Z
video_id: MTyO3W7MYTs
youtube_url: https://www.youtube.com/watch?v=MTyO3W7MYTs
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# 7 Anti-Lessons from Building a PydanticAI Agent: Mistakes We Made So You Don't Have To

**Joshua Görner**

`PyData` · `PyData` · `2026` · `45 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=MTyO3W7MYTs) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Joshua Görner share seven critical "anti-lessons" from building a PydanticAI agent in the high-stakes world of life sciences compliance to learn how to avoid common pitfalls and accelerate your own AI development.

Speakers:
Joshua Görner

Description:
Building a compliance intelligence chatbot for the life sciences industry revealed that over-engineering agent architectures often degrades performance. Initial attempts using a multi-agent system with a supervisor and specialized agents caused high latency, memory loss during handoffs, and excessive code complexity. Transitioning to a single-agent architecture using PydanticAI reduced these issues.

To prevent context bloat caused by dozens of specific Python functions, the system shifted to an abstraction layer. The agent now uses a discovery tool to query OpenAPI specifications and execute operations dynamically. Complex workflows were moved from deterministic code to markdown-based skill files, allowing business experts to define processes. To maintain plan adherence, the agent utilizes a simple to-do list with write and update tools, where tool return values nudge the agent toward the next task.

Human-in-the-loop checkpoints were implemented for non-idempotent API requests to ensure regulatory compliance and user trust. Testing evolved from standard unit tests to Pydantic AI Evals, employing deterministic checks, accuracy evaluators, and LLM-as-a-judge probabilistic evaluations to establish a ground truth. The final approach emphasizes simplicity, using a temperature of 1.0 and providing the LLM the flexibility to explore solutions within a safe, spec-driven environment.

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
