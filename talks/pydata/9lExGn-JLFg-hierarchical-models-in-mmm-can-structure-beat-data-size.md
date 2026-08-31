---
id: 9lExGn-JLFg
title: "Hierarchical Models in MMM: Can Structure beat data size? [PyCon DE & PyData 2026]"
slug: hierarchical-models-in-mmm-can-structure-beat-data-size
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Mohamed Amine Jebari"]
channel: null
duration_min: 25
published_at: 2026-08-04T22:20:38Z
video_id: 9lExGn-JLFg
youtube_url: https://www.youtube.com/watch?v=9lExGn-JLFg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Hierarchical Models in MMM: Can Structure beat data size? [PyCon DE & PyData 2026]

**Mohamed Amine Jebari**

`PyData` · `PyData` · `2026` · `25 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9lExGn-JLFg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Mohamed Amine Jebari demonstrate how hierarchical modeling and partial pooling in PyMC can stabilize ROAS estimates and outperform raw data volume in Marketing Mix Modeling.

Speakers:
Mohamed Amine Jebari

Description:
Marketing Mix Modeling (MMM) often faces the challenge of insufficient data for specific regions, where the number of available data points is equal to or less than the number of coefficients required for prediction. This data scarcity leads to high uncertainty and unreliable coefficients, particularly in smaller markets. To address this, hierarchical Bayesian modeling is used to implement partial pooling, which allows models for data-poor regions to borrow statistical strength from data-rich regions.

The approach utilizes PyMC for probabilistic programming and the Hypothesis library for property-based testing of transformation functions. To reflect real-world consumer behavior, the model incorporates ad stock functions to account for the delayed effect of advertising and saturation functions (such as the Hill function) to model the plateauing of returns as spend increases. Testing ensures these functions remain bounded between zero and one to prevent unrealistic simulations.

Three modeling strategies are compared: pooled (all regions combined), unpooled (separate models per region), and hierarchical (partial pooling). While pooled models ignore regional variance and unpooled models fail in data-sparse regions, the hierarchical model uses a group mean and a deviation parameter to balance these extremes. To improve sampler efficiency and avoid restrictive distributions, a non-centered parameterization is applied.

Key takeaways include the importance of calibration and uncertainty intervals over simple metrics like RMSE or R-squared. Hierarchical models are most effective when regions share domain similarities, such as shared culture or audience demographics. However, they fail if regional behaviors are too divergent or if data is uniformly sparse across all groups.

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
