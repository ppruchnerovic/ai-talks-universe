---
id: QkBtqERDlpg
title: "From Research Models to SLAs: Operationalizing TSFMs with Python [PyCon DE & PyData 2026]"
slug: from-research-models-to-slas-operationalizing-tsfms-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jeyashree Krishnan", "Catarina Filipe"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-25T18:20:07Z
video_id: QkBtqERDlpg
youtube_url: https://www.youtube.com/watch?v=QkBtqERDlpg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# From Research Models to SLAs: Operationalizing TSFMs with Python [PyCon DE & PyData 2026]

**Jeyashree Krishnan, Catarina Filipe**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=QkBtqERDlpg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Jeyashree Krishnan and Catarina Filipe explain how to bridge the gap between research and production by operationalizing Time Series Foundation Models (TSFMs) into scalable Python services.

Speakers:
Jeyashree Krishnan, Catarina Filipe

Description:
Operationalizing Time Series Foundation Models (TSFMs) involves transitioning from research-based models to production-ready APIs that meet enterprise service level agreements. The primary challenge in time series forecasting is the traditional requirement for extensive data collection, domain-specific model development, and constant retraining for every new use case. To solve this, a unified API wrapper was developed to encapsulate multiple foundation models, allowing users to perform zero-shot inference, fine-tuning, and real-time predictions without managing the underlying backend infrastructure.

The architecture utilizes Azure Web Apps to host individual model endpoints, all managed through Azure API Management (APIM) to provide a single gateway for authentication via OAuth 2.0, rate limiting, and access control. The platform integrates four specific models: Chronos, LagLama, and TimesFM (open source), and GTT (a proprietary Siemens model trained on industrial IoT data). This abstraction allows users to switch models by simply changing a parameter in the JSON payload. Beyond direct API access, the system is exposed through a front-end application, a Model Context Protocol (MCP) server for natural language interaction with AI agents, and custom plugins.

Key takeaways include the versatility of TSFMs for tasks beyond forecasting, such as anomaly detection using confidence intervals, time series classification, and historical data imputation via embeddings. Benchmarks indicate that foundation models generally offer faster execution times and higher accuracy than classical ML benchmarks like auto-ARIMA, particularly in zero-shot scenarios. While zero-shot inference provides a rapid baseline, fine-tuning remains essential for optimizing performance in domain-specific industrial contexts.

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
