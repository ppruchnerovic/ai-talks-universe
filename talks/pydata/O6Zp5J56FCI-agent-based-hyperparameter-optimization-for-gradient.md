---
id: O6Zp5J56FCI
title: "Agent-Based Hyperparameter Optimization for Gradient Boosted Trees [PyCon DE & PyData 2026]"
slug: agent-based-hyperparameter-optimization-for-gradient
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Huijo Kim"]
channel: null
duration_min: 28
published_at: 2026-08-04T22:20:31Z
video_id: O6Zp5J56FCI
youtube_url: https://www.youtube.com/watch?v=O6Zp5J56FCI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Agent-Based Hyperparameter Optimization for Gradient Boosted Trees [PyCon DE & PyData 2026]

**Huijo Kim**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=O6Zp5J56FCI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Senior Data Scientist Huijo Kim demonstrate how to transform hyperparameter optimization from a tedious search into an intelligent reasoning process using agent-based workflows.

Speakers:
Huijo Kim

Description:
Hyperparameter optimization for Gradient Boosted Trees, such as LightGBM and XGBoost, typically requires tuning 14 to 19 parameters. While frameworks like Optuna use Bayesian optimization to navigate this search space, they often require hundreds of iterations to move from exploration to exploitation. When model training times are long, this iterative process becomes computationally expensive and time-consuming for human operators to monitor and adjust.

The proposed approach integrates Large Language Models (LLMs) into the decision loop using the Model Context Protocol (MCP) and a structured "skills" framework. In this architecture, MCP acts as a toolset—providing the LLM with specific capabilities to fetch campaign status, summarize rounds, and review history—while skills provide domain-specific recipes and step-by-step instructions in markdown format. Instead of running a single massive batch of 200 trials, the process is split into multiple smaller rounds. After each round, the LLM analyzes the results against the provided domain knowledge and official documentation to decide whether to continue the current path, discard specific hyperparameters, or shift the search region.

Testing on four public scikit-learn datasets demonstrated that this agent-driven framework consistently achieves competitive performance compared to standard tuning. The system functions as a guardrailed loop where the LLM proposes actions that are executed via a predefined CLI, ensuring the agent cannot perform unauthorized operations. This pattern is extensible to other computationally intensive decision loops, such as deep learning training, infrastructure scaling, and A/B test management.

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
