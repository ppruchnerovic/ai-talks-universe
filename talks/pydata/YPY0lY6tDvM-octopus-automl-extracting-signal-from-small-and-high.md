---
id: YPY0lY6tDvM
title: "Octopus AutoML: Extracting Signal from Small and High-Dimensional Data [PyCon DE & PyData 2026]"
slug: octopus-automl-extracting-signal-from-small-and-high
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Nils Haase", "Andreas Wurl"]
channel: "PyData"
duration_min: 29
published_at: 2026-08-25T18:20:11Z
video_id: YPY0lY6tDvM
youtube_url: https://www.youtube.com/watch?v=YPY0lY6tDvM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Octopus AutoML: Extracting Signal from Small and High-Dimensional Data [PyCon DE & PyData 2026]

**Nils Haase, Andreas Wurl**

`PyData` · `PyData` · `2026` · `29 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YPY0lY6tDvM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Nils Haase and Andreas Wurl demonstrate how the Octopus AutoML library ensures statistically honest results and prevents data leakage when working with small, high-dimensional datasets.

Speakers:
Nils Haase, Andreas Wurl

Description:
Octopus AutoML is an open-source supervised machine learning library designed specifically for small, high-dimensional tabular datasets, such as those found in clinical trials or material science. In these environments, the number of features often equals or exceeds the number of samples—for example, datasets with only 50 to 100 data points but hundreds of features. This imbalance typically leads to the lottery problem, where model performance varies wildly depending on the random seed of the data split, resulting in unreliable estimates of generalization performance.

To mitigate this, Octopus AutoML implements nested cross-validation. Unlike standard k-fold cross-validation, this approach uses an inner loop for hyperparameter optimization and an outer loop for testing, ensuring that every data point is used for testing exactly once across multiple models. This process reduces the impact of split seeds and allows for model ensembling to improve overall performance. To address high dimensionality, the tool integrates various feature reduction methods directly into the nested cross-validation pipeline to prevent information leakage, ensuring that dimensionality reduction is performed only on training splits.

The framework includes a comprehensive data health check to identify input issues early and a modular benchmarking system to compare different tools, such as the native TACO tool and AutoGluon, under identical conditions. It supports regression, classification, and time-to-event problems. By automating the pipeline from data preparation to evaluation, the tool enables a high-throughput screening approach where numerous use cases are ranked, allowing researchers to prioritize deep-dive investments only on the most promising signals.

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
