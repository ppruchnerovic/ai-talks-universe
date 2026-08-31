---
id: t6oX0fbQHAY
title: "From Prompt to Production: How to use AI Code Assistants for Python Data Systems"
slug: from-prompt-to-production-how-to-use-ai-code-assistants-for
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Serhii Sokolenko"]
channel: null
duration_min: 49
published_at: 2026-08-04T22:21:39Z
video_id: t6oX0fbQHAY
youtube_url: https://www.youtube.com/watch?v=t6oX0fbQHAY
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# From Prompt to Production: How to use AI Code Assistants for Python Data Systems

**Serhii Sokolenko**

`PyData` · `PyData` · `2026` · `49 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=t6oX0fbQHAY) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Serhii Sokolenko demonstrate how to move beyond "vibe coding" to build production-ready Python data systems using a disciplined, engineering-first approach to AI code assistants.

Speakers:
Serhii Sokolenko

Description:
Building production-ready Python data systems with AI coding agents requires moving beyond linear prompting toward a structured framework of skills, personas, and state management. While LLMs can rapidly generate initial code, they often struggle with existing codebases, environment configurations, and the non-linear nature of debugging and deployment. To solve this, a system can be implemented using a combination of persona-based skills, a fuzzy state machine for workflow orchestration, and a specialized runtime environment.

The approach utilizes markdown-based skill files to define specific roles, such as a business analyst for requirement reviews or a data architect for structural validation. Instead of a simple chain of commands, a fuzzy state machine identifies the user's intent—such as deploying a hotfix versus building a new feature—and assesses the current state of the repository to determine the necessary path. This is complemented by hooks that monitor tool calls and suggest debugging utilities, such as increasing logging verbosity or limiting data samples, when a pipeline fails during its first execution.

In a practical application, this framework was used to build a data pipeline that fetches issues from a public GitHub repository using DLT and loads them into DuckDB. The process involved using the Tower platform to manage secrets via a built-in vault and deploying the application through a unified CLI. The final system expanded the pipeline to write data to Apache Iceberg and integrated a Discord webhook for real-time bug notifications. This methodology transforms AI agents from simple code generators into expert collaborators capable of maintaining architectural standards and operational reliability.

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
