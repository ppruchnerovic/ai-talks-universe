---
id: J0U3h9sYAE8
title: "Holistic Optimization: Implementing \"Pipeline-as-a-Trial\" HPO with Ray and Cloud Infra"
slug: holistic-optimization-implementing-pipeline-as-a-trial-hpo
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Abdullah Taha"]
channel: "PyData"
duration_min: 22
published_at: 2026-08-04T22:20:53Z
video_id: J0U3h9sYAE8
youtube_url: https://www.youtube.com/watch?v=J0U3h9sYAE8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Holistic Optimization: Implementing "Pipeline-as-a-Trial" HPO with Ray and Cloud Infra

**Abdullah Taha**

`PyData` · `PyData` · `2026` · `22 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=J0U3h9sYAE8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Abdullah Taha explain how to escape the "local optimization trap" by implementing a scalable "Pipeline-as-a-Trial" HPO architecture using Ray and cloud infrastructure.

Speakers:
Abdullah Taha

Description:
Local optimization in machine learning occurs when a specific model is tuned for its own output rather than the performance of the entire downstream system. This often leads to failures during A/B testing because improvements in one component can negatively impact subsequent steps in the pipeline. To solve this, a "Pipeline-as-a-Trial" approach for hyperparameter optimization (HPO) was implemented, treating the entire end-to-end pipeline as the objective function for tuning.

The technical implementation utilizes Ray, specifically the Ray Tune library and its HyperOpt search model, to manage the search space and trigger trials. Instead of tuning a single model, the trainable component is a customizable function that builds and executes a full pipeline. This pipeline consists of multiple steps, such as short-horizon and long-horizon forecasting models, an assembler, and a post-processor. The system uses a config-based approach where data scientists define the model classes and parameters in a configuration file, which is then translated into a directed acyclic graph (DAG) for execution.

Three proof-of-concept (POC) infrastructures were evaluated for scalability: AWS SageMaker, Databricks, and a custom Ray cluster on EC2 instances. SageMaker utilized SageMaker Pipelines to orchestrate training jobs, while Databricks employed Workflows for similar DAG management. The EC2 approach used Metaflow to define the pipeline structure within a Ray cluster. While Databricks provided superior UI and traceability and EC2 offered maximum configurability, SageMaker was selected for production due to existing data scientist familiarity and integration with the AWS ecosystem.

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
