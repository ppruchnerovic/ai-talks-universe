---
id: M0lHvt1PWiQ
title: "Building Trust in Your Data Pipelines with Observability [PyCon DE & PyData 2026]"
slug: building-trust-in-your-data-pipelines-with-observability
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Stefan Dienst"]
channel: null
duration_min: 30
published_at: 2026-08-04T22:21:48Z
video_id: M0lHvt1PWiQ
youtube_url: https://www.youtube.com/watch?v=M0lHvt1PWiQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Building Trust in Your Data Pipelines with Observability [PyCon DE & PyData 2026]

**Stefan Dienst**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=M0lHvt1PWiQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Stefan Dienst explain how to implement the three pillars of observability to eliminate silent failures and build unwavering trust in your data pipelines.

Speakers:
Stefan Dienst

Description:
Data pipeline observability addresses the problem of "black box" pipelines, where engineers only discover failures through stakeholder complaints or cryptic error messages. To build trust and transparency, a three-pillar approach is used: metrics, alarms, and logs.

Metrics provide numeric measurements of pipeline health over time. A robust foundation relies on the "four golden signals": latency (duration of execution), traffic (input and output record counts), errors (counts of dropped or failed records), and saturation (CPU and memory utilization). These metrics are visualized on dashboards to perform explorative data analysis, allowing engineers to detect anomalies, such as unexpected spikes in specific event types or silent data corruption caused by hidden bugs.

Alarms transform monitoring from a pull-based approach to a push-based system by triggering notifications when metrics cross defined thresholds. Effective alarms must be actionable, reliable to avoid false positives, and contextual, providing clear implications and documentation. To prevent alarm fatigue, noise is reduced by disabling non-actionable alerts and fine-tuning thresholds.

Logs provide granular, time-stamped details of internal pipeline states, acting as breadcrumbs for debugging. Best practices include using appropriate log levels to avoid noise and implementing structured logging—converting unstructured strings into JSON format—to enable robust querying and filtering. Together, these pillars allow engineers to identify a failure via an alarm, analyze the trend through metrics, and pinpoint the root cause using structured logs. Tools such as Grafana, Prometheus, AWS CloudWatch, and Datadog are commonly used to implement these strategies.

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
