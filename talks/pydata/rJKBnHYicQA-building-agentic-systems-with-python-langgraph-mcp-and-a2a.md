---
id: rJKBnHYicQA
title: "Building Agentic Systems with Python, LangGraph, MCP, and A2A [PyCon DE & PyData 2026]"
slug: building-agentic-systems-with-python-langgraph-mcp-and-a2a
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Holger Nösekabel"]
channel: "PyData"
duration_min: 47
published_at: 2026-08-25T18:20:14Z
video_id: rJKBnHYicQA
youtube_url: https://www.youtube.com/watch?v=rJKBnHYicQA
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Building Agentic Systems with Python, LangGraph, MCP, and A2A [PyCon DE & PyData 2026]

**Holger Nösekabel**

`PyData` · `PyData` · `2026` · `47 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=rJKBnHYicQA) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Holger Nösekabel, CTO at TD Reply, reveal how to build scalable, real-world agentic systems using Python, LangGraph, MCP, and A2A to orchestrate dynamic data acquisition and validation.

Speakers:
Holger Nösekabel

Description:
Agentic systems can be constructed using a hub-and-spoke architecture to automate complex business processes, such as identifying and scoring companies for mergers and acquisitions. This approach utilizes a coordinator agent to delegate tasks to specialized agents responsible for data retrieval, scoring, and outreach. To ensure the system remains flexible and loosely coupled, the architecture separates the conversational interface, built with FastAPI and Nginx, from the underlying agent logic and data storage, which employs SQLite for structured data and Redis for real-time status propagation to the user interface.

The system integrates the Model Context Protocol (MCP) to expose specific tools—such as web scrapers and API connectors—to agents, allowing them to fetch dynamic data from sources like LinkedIn, partner websites, and Perplexity. To prevent context window saturation and agent confusion, tools are limited to approximately ten per agent. While autonomous ReAct patterns are useful, the system employs LangGraph to implement structured workflows. This ensures that critical data retrieval steps occur in parallel and are completed before the agent processes the final result, avoiding the reliability issues associated with over-prompting.

Agent-to-agent (A2A) communication allows the coordinator to interact with specialized agents via URIs, facilitating a scalable ecosystem where new capabilities can be added without rewriting the core logic. To maintain data integrity, a dedicated check agent validates outputs for hallucinations or outliers, such as unrealistic revenue-to-employee ratios. Final system reliability is ensured through AI-generated test suites and human evaluation of the response quality.

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
