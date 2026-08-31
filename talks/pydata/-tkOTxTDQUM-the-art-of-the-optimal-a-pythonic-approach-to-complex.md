---
id: -tkOTxTDQUM
title: "The Art of the Optimal: A Pythonic Approach to Complex Decision-Making [PyCon DE & PyData 2026]"
slug: the-art-of-the-optimal-a-pythonic-approach-to-complex
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Justine Broihan"]
channel: "PyData"
duration_min: 33
published_at: 2026-08-04T22:21:03Z
video_id: -tkOTxTDQUM
youtube_url: https://www.youtube.com/watch?v=-tkOTxTDQUM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# The Art of the Optimal: A Pythonic Approach to Complex Decision-Making [PyCon DE & PyData 2026]

**Justine Broihan**

`PyData` · `PyData` · `2026` · `33 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-tkOTxTDQUM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Justine Broihan demonstrate how to move beyond basic heuristics and leverage mathematical optimization to solve complex decision-making challenges in Python.

Speakers:
Justine Broihan

Description:
Complex decision-making problems, such as optimizing a car assembly line's paint shop, are often addressed using heuristics or greedy algorithms. In a scenario where vehicles of various types must be painted in alternating base coats (black or white) with minimum color changes, a greedy approach—such as painting cars in one color until a duplicate type appears—often results in sub-optimal outcomes. For example, a greedy algorithm might produce 38 color changes for a specific sequence, whereas the mathematically proven optimal solution for the same constraints is 23.

Mathematical optimization solves this by shifting the focus from defining a sequence of rules to describing the problem space through decision variables and constraints. By formulating the problem algebraically—defining binary variables for color choice and objective functions to minimize changes—users can employ off-the-shelf solvers to guarantee a mathematically proven optimal solution. GAMSpy is a Python library that facilitates this process by providing a syntax close to algebraic notation and interfacing with 36 different solvers.

The integration of machine learning (ML) and optimization allows for the handling of systems without known mathematical equations. By embedding a PyTorch model into GAMSpy, a predicted defect rate from a neural network can be treated as a constraint. For instance, in a curing oven, the conveyor belt speed and heater temperature can be optimized to maximize throughput while keeping the predicted defect rate below 5%. This hybrid approach is applicable to smart energy grids for minimizing coal usage, dynamic pricing for maximizing sales, and neural network verification to identify minimal perturbations that fool a classifier.

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
