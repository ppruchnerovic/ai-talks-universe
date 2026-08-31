---
id: K7Hl3vXB5wA
title: "When Space Weather Breaks Your GPS: Building an Explainable Early Warning System"
slug: when-space-weather-breaks-your-gps-building-an-explainable
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Vincenzo Ventriglia"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:15Z
video_id: K7Hl3vXB5wA
youtube_url: https://www.youtube.com/watch?v=K7Hl3vXB5wA
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# When Space Weather Breaks Your GPS: Building an Explainable Early Warning System

**Vincenzo Ventriglia**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=K7Hl3vXB5wA) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Vincenzo Ventriglia demonstrate how to build an explainable, real-time early warning system using CatBoost and SHAP to protect critical GPS and communication infrastructure from space weather disruptions.

Speakers:
Vincenzo Ventriglia

Description:
Solar activity, such as coronal mass ejections and solar flares, creates plasma density fluctuations in the ionosphere known as Large-Scale Traveling Atmospheric Disturbances (LSTADs). These disturbances bend and delay radio signals, causing positioning errors in Global Navigation Satellite Systems (GNSS) and disrupting high-frequency communications. To mitigate these risks, a multivariate time series binary classification model was developed to predict the onset of LSTADs over the European sector within a three-hour window.

The system utilizes CatBoost for gradient boosting over symmetric decision trees, with Optuna for hyperparameter optimization and MLflow for experiment tracking. The model is trained on a catalog of 1,600 manually labeled events spanning nine years. To ensure the system is explainable and trustworthy, SHAP (SHapley Additive exPlanations) is used to attribute predictions to specific physical drivers, while conformal prediction transforms point predictions into mathematically guaranteed prediction intervals.

The framework offers three operating modes—high precision, high sensitivity, and balanced—allowing users to prioritize either the reduction of false positives or false negatives based on the socio-economic cost of the error. Feature engineering includes moving averages and lagged features covering up to six hours of historical data. The resulting system provides near real-time forecasts via the ESGUA platform to support safety-critical infrastructure and space weather monitoring.

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
